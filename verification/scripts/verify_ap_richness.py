# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Mangesh Raut

"""Exact finite diagnostics for AP_RICHNESS_COUNTEREXAMPLE.md.

Small geometry parameters are checked directly. The asymptotic deterministic
sets are specified by the written construction, not generated here.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial, isqrt
import json

from verify_energy_counterexample import next_prime


def ap_counts(points,p):
    points=set(points);counts={}
    for x in points:
        for y in points:
            h=(y-x)%p
            if (x+2*h)%p in points and (x+3*h)%p in points:
                counts[h]=counts.get(h,0)+1
    return counts


def effective(counts):
    values=[n for h,n in counts.items() if h]
    return F(sum(values)**2,sum(n*n for n in values)) if values else None


def geometry_case(d,L):
    Q0=16*L+1;fac=factorial(d)
    moduli=[Q0]+[1+Q0*fac*i for i in range(1,d+1)]
    M=1
    for q in moduli:M*=q
    R=M//Q0
    assert R%Q0==1
    p=next_prime(100*M*moduli[-1])
    assert p<200*M*moduli[-1]
    coords=[((p+Q0-1)//Q0,p*(2*L+1)//(2*Q0))]
    for i,Q in enumerate(moduli[1:],1):
        coords.append(((p+Q-1)//Q,3*p//(2*Q)))
        H=L*fac*i+1
        den=Q*Q0;num=p*(H*Q0+Q)
        coords.append(((num+den-1)//den,p*(4*H*Q0+Q)//(4*Q*Q0)))
    assert 3*(M-1)<p and all(0<g<p and 3*cap<p for g,cap in coords)
    actual={x for x in range(M) if all(g*x%p<=cap for g,cap in coords)}
    units=[(M//q)*pow(M//q,-1,q)%M for q in moduli]
    cube={sum(bit*u for bit,u in zip(bits,units[1:]))%M
          for bits in product((0,1),repeat=d)}
    core=cube-{0};spine={R*z for z in range(L+1)}
    omega=core|spine
    assert not core&spine and actual==omega
    assert len(cube)==2**d and len(omega)==2**d+L
    assert all(x==y or (2*y-x)%p not in core for x in core for y in core)
    counts=ap_counts(omega,p)
    expected={0:len(omega)}
    for e in range(1,L//3+1):
        expected[R*e%p]=L+1-3*e
        expected[-R*e%p]=L+1-3*e
    assert counts==expected
    assert sum(counts.values())==((L+1)**2+2)//3+2**d-1
    child={x for x in omega if coords[0][0]*x%p<=p//(2*Q0)}
    assert child==cube and ap_counts(child,p)=={0:2**d}
    assert core<=child
    for removed in [{next(iter(core))},{0},spine-{0}]:
        smaller=omega-removed;cs=ap_counts(smaller,p)
        assert all(v<=counts.get(h,0) for h,v in cs.items())
        mass=sum(v for h,v in counts.items() if h)
        mass2=sum(v for h,v in cs.items() if h)
        assert mass-mass2<=4*len(removed)*(len(omega)-1)
        if mass and mass2:
            assert effective(cs)>=F(mass2,mass)**2*effective(counts)
    return p,coords,omega,core,spine,{
        'd':d,'L':L,'p':p,'CRT_range_exhaustively_checked':M,
        'window_size':len(omega),'AP_free_core_size':len(core),
        'nontrivial_AP_count':sum(v for h,v in counts.items() if h),
        'effective_direction_support':str(effective(counts)),
        'refined_window_nontrivial_AP_count':0,
        'A_mass_retention_in_refinement':'1',
        'asymptotic_parameters':False,'asymptotic_A_d_generated':False}


def profile_checks(p,coords,omega,core):
    n=len(omega);u=len(core);tested=0
    for k in range(1,u+1):
        a=F(k,n);b=F(k,u)
        profile={x:b*int(x in core)-a for x in omega}
        profile_var=sum(v*v for v in profile.values())/n
        assert profile_var==a*a*F(n-u,u)
        for gamma,_ in coords:
            for offset in (0,p//8):
                cells={}
                for x in omega:cells.setdefault(4*((gamma*x+offset)%p)//p,[]).append(x)
                noise_sum=energy_sum=F(0);count=0
                profile_proj=sum(F(len(cell),n)*(sum(profile[x] for x in cell)/len(cell))**2
                                 for cell in cells.values())
                for chosen in combinations(sorted(core),k):
                    aset=set(chosen)
                    energy=noise=F(0)
                    for cell in cells.values():
                        size=len(cell);inside=len(aset.intersection(cell));c=len(core.intersection(cell))
                        energy+=F(size,n)*(F(inside,size)-a)**2
                        noise+=F(1,n*size)*(inside-b*c)**2
                    assert energy<=2*noise+2*profile_var
                    noise_sum+=noise;energy_sum+=energy;count+=1;tested+=1
                expected_noise=sum(F(1,n*len(cell))*b*(1-b)*len(core.intersection(cell))
                                   *F(u-len(core.intersection(cell)),u-1)
                                   for cell in cells.values())
                assert noise_sum/count==expected_noise
                assert energy_sum/count==expected_noise+profile_proj
    return tested


def power_ceiling(x):
    e=x.numerator.bit_length()-x.denominator.bit_length()
    def power(k):return F(2**k) if k>=0 else F(1,2**(-k))
    while power(e)<x:e+=1
    while power(e-1)>=x:e-=1
    return e


def asymptotic_bounds():
    rows=[]
    for d in (256,512,1024,4096):
        S=2**d;L=2**((d+1)//2)*d**8;s=isqrt(d)
        assert 2*L<=S and S>=2*d**3
        variance_bound=F(128*d**10*d**s,S)+F(2*(L+1),S-1)
        richness_lower=F(d**7,48)
        assert richness_lower>8
        rows.append({'d':d,'characters_controlled':s,
                     'a_cubed_n_beta_lower_bound':str(richness_lower),
                     'variance_over_a_squared_upper_bound':'2^'+str(power_ceiling(variance_bound)),
                     'effective_support_over_window_size_upper_bound':str(F(2*L,3*S)),
                     'bounds_only_not_generated_sets':True})
    return rows


def main():
    records=[];cases=0
    for d,L in ((2,3),(2,5)):
        p,coords,omega,core,spine,row=geometry_case(d,L)
        records.append(row);cases+=profile_checks(p,coords,omega,core)
    print(json.dumps({'status':'finite geometry and energy checks passed; asymptotic theorem is in the written proof',
                      'geometry':records,'profile_energy_cases':cases,
                      'asymptotic_bound_diagnostics':asymptotic_bounds(),
                      'arithmetic':'exact integers and fractions','r4_target':'OPEN',
                      'full_checkpoint_energy_lemma':'OPEN','external_dependencies':[]},indent=2))


if __name__=='__main__':main()
