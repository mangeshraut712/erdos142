"""Independent deterministic finite checks; no asymptotic selection claim.

Physical progression weights and cell statistics use integers/Fraction.
Fourier transforms, Gauss envelopes and phase correlations use floating point.
Only LOG_DENSITY_VERIFICATION_20261016.json is written.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parent
counts = Counter()
errors = Counter()
rng = np.random.default_rng(14220261016)


def close(label, x, y, tol=2e-10):
    err = float(np.max(np.abs(np.asarray(x)-np.asarray(y))))
    errors[label] = max(errors[label], err)
    assert err < tol, (label, err)
    counts[label] += 1


def tent_int(t, p, H):
    return max(0, H+1-min(t % p, (-t) % p))


def mu_exact(p, H, linear, quad):
    """Physical M4, independent of the Fourier decomposition implementation."""
    base = H+1
    first = sum(math.prod(tent_int(xi*t,p,H) for xi in linear)*
                math.prod(tent_int(b*t+c*z,p,H) for c,b in quad)
                for t in range(p) for z in range(p))
    second = sum(math.prod(tent_int(c*y,p,H) for c,b in quad)
                 for y in range(p))
    return Q(first*second, p**3*base**(len(linear)+2*len(quad)))


def ap_free(A, p):
    return not any((2*y-x)%p in A and (3*y-2*x)%p in A
                   for x in A for y in A if x != y)


spectral_records = []
spectral_configs = [(7,1,[1],[(1,0)]), (11,1,[],[(1,0),(2,1)]),
                    (13,2,[1],[(2,3)]), (7,1,[1,2],[]),
                    (7,1,[1,1],[(1,0)]), (7,1,[],[(1,1),(1,1)]),
                    (11,2,[],[(3,4)]), (13,1,[1,3],[])]
for p,H,linear,quad in spectral_configs:
    assert p>3 and all(p%i for i in range(2,math.isqrt(p)+1)) and 2*H<p
    f=np.array([tent_int(t,p,H)/(H+1) for t in range(p)])
    V=set(range(H+1))
    for t in range(p):
        convolution=sum(x in V and (x-t)%p in V for x in range(p))
        assert Q(convolution,H+1)==Q(tent_int(t,p,H),H+1)
        counts['exact_tent_convolution']+=1
    hat=np.fft.fft(f)/p
    assert np.max(abs(hat.imag))<1e-13 and min(hat.real)>-1e-13
    hat=hat.real
    close('floating_tent_transform_mass',sum(hat),1)
    close('floating_tent_zero',hat[0],(H+1)/p)
    d=len(linear);s=len(quad);k=d+2*s
    mu=mu_exact(p,H,linear,quad)
    assert mu>=Q(H+1,p)**k and 0<mu<=1
    counts['exact_persistent_baseline_lower_bound']+=1
    mu_fourier=0.;spikes=np.zeros((4,p));quad_mass=np.zeros(4)
    for ix in product(range(p),repeat=k):
        l=ix[:d];m=ix[d:d+s];n=ix[d+s:]
        W=math.prod(hat[t] for t in ix)
        C=sum(c*t for (c,b),t in zip(quad,m))%p
        B=(sum(xi*t for xi,t in zip(linear,l))+sum(b*t for (c,b),t in zip(quad,m)))%p
        N=sum(c*t for (c,b),t in zip(quad,n))%p
        if C==B==N==0:mu_fourier+=W
        for i in range(4):
            Ai=(N-2*i*C)%p
            if Ai:quad_mass[i]+=W
            elif C:
                vertex=(-B*pow(2*C,-1,p))%p
                spikes[i,vertex]+=W
    close('floating_persistent_vs_physical',mu_fourier,float(mu))
    degree=[]
    for i in range(4):
        D=[]
        for v in range(p):
            numer=0
            for h in range(p):
                x=(v-i*h)%p
                numer+=math.prod(tent_int(xi*h,p,H) for xi in linear)*math.prod(
                    tent_int((2*c*x+b)*h,p,H)*tent_int(c*h*h,p,H) for c,b in quad)
            D.append(Q(numer,p*(H+1)**k))
        E=np.array([float(t) for t in D])-float(mu)-spikes[i]
        assert min(spikes[i])>=-1e-13
        assert spikes[i].mean()<=1/p+1e-12
        assert max(abs(E))<=quad_mass[i]/math.sqrt(p)+1e-11
        counts['floating_all_vertex_degree_decomposition']+=p
        degree.append(D)
    spectral_records.append({'p':p,'H':H,'linear':linear,'quad':quad,
                             'mu_exact':str(mu), 'max_exception_mean':float(spikes.mean(axis=1).max()),
                             'largest_quadratic_mass':float(max(quad_mass))})


# Exact weighted incidence and diagonals on proper, wrapped and resonant hosts.
def host(p,linear,quad,erosion):
    result=set()
    for x in range(p):
        tests=[(xi*x-start)%p>=erosion and (xi*x-start)%p<length-erosion
               for xi,start,length in linear]
        tests += [((c*x*x+b*x+e)-start)%p>=erosion and
                  ((c*x*x+b*x+e)-start)%p<length-erosion
                  for c,b,e,start,length in quad]
        if all(tests):result.add(x)
    return result


physical_configs=[
 (53,1,[(1,0,50)],[]),
 (53,1,[],[(1,0,0,40,50)]),
 (101,2,[(1,90,95)],[(1,2,3,80,95)]),
 (101,1,[],[(1,0,0,80,100),(1,0,0,80,100)]),
 (101,1,[(1,0,100),(2,0,100)],[(2,3,1,80,100)]),
 (257,3,[],[(1,0,0,220,250)]),
 (257,2,[(1,230,250)],[(2,3,7,200,250)]),
 (29,1,[(1,27,16)],[(2,1,3,25,25)])]
physical_records=[]
for p,H,linear,quad in physical_configs:
    omega=host(p,linear,quad,0);inner=host(p,linear,quad,12*H)
    assert omega
    d=len(linear);s=len(quad);k=d+2*s;r=d+s
    denom=(H+1)**k
    mu=mu_exact(p,H,[l[0] for l in linear],[(q[0],q[1]) for q in quad])
    w=Q(len(omega),p);wm=Q(len(inner),p);b=w-wm;K=2+math.log(p)
    assert float(b)<=24*r*H/p+2*s*K/math.sqrt(p)+1e-12
    D=[[0]*p for _ in range(4)];actual=[[0]*p for _ in range(4)]
    edges=[];total=0;inner_total=0
    for x in range(p):
        for h in range(p):
            weight=math.prod(tent_int(xi*h,p,H) for xi,_,_ in linear)*math.prod(
                tent_int((2*c*x+b0)*h,p,H)*tent_int(c*h*h,p,H)
                for c,b0,_,_,_ in quad)
            if not weight:continue
            vertices=[(x+j*h)%p for j in range(4)]
            for i,vtx in enumerate(vertices):D[i][vtx]+=weight
            if any(v in inner for v in vertices):
                assert all(v in omega for v in vertices)
                counts['exact_eroded_slot_support']+=1
            if x in inner:inner_total+=weight
            if all(v in omega for v in vertices):
                total+=weight
                edges.append((h,vertices,weight))
                for i,vtx in enumerate(vertices):actual[i][vtx]+=weight
    for i in range(4):
        assert all(actual[i][v]==D[i][v] for v in inner)
    assert total>=inner_total
    assert sum(weight for h,v,weight in edges if h==0)==len(omega)*denom
    T=Q(total,p*p*denom)
    assert float(T)>=float(wm)*(float(mu)-1/math.sqrt(p))-1e-12
    # Exact algebra for the expansion and physical AP-free hitting, no spectral code used.
    examples=[]
    for seed in range(3):
        perm=list(sorted(omega));rng.shuffle(perm);A=set()
        for vtx in perm:
            candidate=A|{vtx}
            if ap_free(candidate,p):A=candidate
        assert A and ap_free(A,p)
        a=Q(len(A),len(omega))
        hole_degree=sum(weight*sum(v not in A for v in vertices)
                        for h,vertices,weight in edges if h!=0)
        assert hole_degree>=total-len(omega)*denom
        for i in range(4):
            error=sum(abs(Q(actual[i][v],p*denom)-mu) for v in omega)/p
            rhs=float(mu*b)+(float(w+b)/math.sqrt(p))+2/p
            assert float(error)<=rhs+1e-12
            counts['floating_first_degree_error_envelope']+=1
        # Enumerate the coefficient polynomial with exact rational arithmetic.
        coefficients=[Q(0)]*5
        for h,vertices,weight in edges:
            polynomial=[Q(1)]
            for vtx in vertices:
                uv=int(vtx in A)-a
                nxt=[Q(0)]*(len(polynomial)+1)
                for j,z in enumerate(polynomial):
                    nxt[j]+=a*z;nxt[j+1]+=uv*z
                polynomial=nxt
            for j,z in enumerate(polynomial):coefficients[j]+=weight*z/(p*p*denom)
        assert coefficients[0]==a**4*T
        assert sum(coefficients)==a*w/p
        r1_phys=a**3*sum((int(v in A)-a)*actual[i][v]
                         for i in range(4) for v in omega)/(p*p*denom)
        assert coefficients[1]==r1_phys
        bound=4*float(a**3)*(float(mu*b)+float(w+b)/math.sqrt(p)+2/p)
        assert abs(float(coefficients[1]))<=bound+1e-12
        counts['exact_weighted_APfree_hitting_diagonal_expansion']+=1
        examples.append({'A':sorted(A),'density':str(a),'coefficients':[str(z) for z in coefficients]})
    physical_records.append({'p':p,'H':H,'linear':linear,'quad':quad,'n':len(omega),
                             'inner_n':len(inner),'mu':str(mu),'T':str(T),
                             'nonzero_weighted_edge_count':sum(h!=0 for h,_,_ in edges),
                             'examples':examples})
    counts['exact_weighted_host_degree_cases']+=1
assert any(r['nonzero_weighted_edge_count']>0 for r in physical_records)
assert any(r['inner_n']>0 for r in physical_records)


# Direct atom extraction: exact cells/discrepancies; floating chirp correlation.
cell_records=[]
kappa=2*math.sqrt(2)/math.pi
for p,omega in [(7,list(range(7))),(11,list(range(6))),
                (17,[0,1,2,4,6,8,10,11,15]),(29,list(range(3,26)))]:
    n=len(omega)
    for size in sorted({1,min(3,n-1),n//2,n-1}):
        for trial in range(3):
            A=set(rng.choice(omega,size=size,replace=False).tolist());a=Q(size,n)
            for c,b in [(0,1),(0,2),(1,0),(1,3),(2,1)]:
                phases={x:Q((c*x*x+b*x)%p,p) for x in omega}
                # Rotations in [0,1/4), avoiding all cell boundaries.
                events=sorted({Q(0),Q(1,4)}|{v%Q(1,4) for v in phases.values()})
                delta=abs(sum(float(int(x in A)-a)*np.exp(-2j*np.pi*float(phases[x]))
                              for x in omega)/n)
                best=None
                for left,right in zip(events,events[1:]):
                    theta=(left+right)/2
                    cells=[[] for _ in range(4)]
                    for x in omega:cells[int(((phases[x]-theta)%1)*4)].append(x)
                    for C in cells:
                        if not C:continue
                        m=sum(Q(int(x in A))-a for x in C)/n
                        if best is None or m>best[0]:best=(m,C,theta)
                m,C,theta=best
                assert float(m)+1e-12>=kappa*delta/8
                aprime=Q(len(A&set(C)),len(C));mass=Q(len(A&set(C)),len(A))
                assert aprime-a>=m and mass>=m/a
                assert float(aprime-a)+1e-12>=kappa*delta/8
                assert float(mass)+1e-12>=kappa*delta/(8*float(a))
                counts['floating_direct_atom_correlation_bound']+=1
                counts['exact_direct_atom_gain_and_mass']+=1
                if len(cell_records)<8:
                    cell_records.append({'p':p,'omega':omega,'A':sorted(A),'phase':[c,b],
                                         'correlation':float(delta),'theta':str(theta),'cell':C,
                                         'discrepancy':str(m),'density_gain':str(aprime-a),
                                         'occupied_mass_retained':str(mass)})

# Exact telescoping identity for a nested chain of actual finite sets.
A={0,1,2,4};chain=[set(range(17)),set(range(11)),set(range(7)),{0,1,2,3,4}]
a0=Q(len(A&chain[0]),len(chain[0]));rhs=Q(1)
for C,D in zip(chain,chain[1:]):
    ac=Q(len(A&C),len(C));ad=Q(len(A&D),len(D));occupied=Q(len(A&D),len(A&C))
    mu=Q(len(D),len(C));assert mu==occupied*ac/ad;rhs*=occupied*ac/ad
assert rhs==Q(len(chain[-1]),len(chain[0]))
counts['exact_retained_mass_telescope']+=1

# A real arithmetic pair kernel with positive-Fourier tent weights is not PSD.
# This is a weighted-function example, NOT an actual Boolean AP-free set.
p=53;H=26;base=27
v=[0,8,3,-16,0,2,9,-3,-8,-2,0,9,-9,5,0,-15,16,6,0,-5,-6,-9,40,-8,-40,8,
   15,15,8,-40,-8,40,-9,-6,-5,0,6,16,-15,0,5,-9,9,0,-2,-8,-3,9,2,0,-16,3,8]
assert len(v)==p and sum(v)==0
pair_numerator=0
for x in range(p):
    for h in range(p):
        weight=tent_int(2*x*h,p,H)*tent_int(h*h,p,H)
        vertices=[(x+j*h)%p for j in range(4)]
        pair_numerator+=weight*sum(v[vertices[i]]*v[vertices[j]]
                                   for i,j in combinations(range(4),2))
negative_pair=Q(pair_numerator,p*p*base*base)
assert negative_pair==Q(-8242732,2047761)
assert all(0<=Q(1,2)+Q(z,100)<=1 for z in v)
weighted_R2=negative_pair/Q(40000)
assert weighted_R2==Q(-2060683,20477610000)
counts['exact_arithmetic_pair_kernel_not_PSD']+=1
pair_obstruction={'p':p,'H':H,'q':'x^2','omega':'full group',
                  'mean_zero_integer_vector':v,'pair_quadratic_form':str(negative_pair),
                  'weighted_B':'1/2+v/100','R2':str(weighted_R2),
                  'Boolean':False,'AP_free_counterexample_claimed':False}

# These are finite exponent and envelope checks, not tests of selection existence.
for theta in [Q(51,100),Q(3,5),Q(13,20),Q(2,3)-Q(1,1000)]:
    assert 2-4*theta<0 and -2+3*theta<0 and -Q(1,2)+3*theta/4<0
    counts['exact_sparse_band_exponents']+=1
assert Q(3)-Q(5,2)==Q(1,2)
assert Q(3)-4==-1
assert Q(1,2)-Q(1,50)==Q(12,25)
assert 1-Q(1,100)-Q(1,50)==Q(97,100)
counts['exact_new_threshold_exponents']+=4
ledger=[]
C=0.01
for log_power in [1.,.5]:
    for log_inv_t in [5.,10.,20.,40.,80.,160.]:
        t=math.exp(-log_inv_t);ej=t;D=0;S=log_inv_t
        while ej<.8:
            upper=min(2*ej,.8)
            lower=C*math.sqrt(ej)*math.log(2/upper)**log_power*math.log(math.log(math.e**2/upper))
            samples=np.geomspace(ej,upper,25)
            assert all(C*math.sqrt(a)*math.log(2/a)**log_power*math.log(math.log(math.e**2/a))>=lower*(1-1e-12)
                       for a in samples)
            Bj=1+math.ceil(2*math.log(2)/lower)
            D+=Bj;S+=Bj*math.log(1/lower);ej*=2
        ledger.append({'ell_power':log_power,'log_inv_t':log_inv_t,
                       'explicit_D_upper':D,'explicit_S_upper':S,
                       'D_over_t_inverse_sqrt':D*math.sqrt(t),'S_over_t_inverse_sqrt':S*math.sqrt(t),
                       'product_times_t':D*S*t})
        counts['floating_explicit_conditional_epoch_ledger']+=1

out={'date':'2026-10-16','offline':True,'target_proved':False,
     'scope':'Finite checks support the written proofs; DIRECT-Q, DIRECT-L and weighted signed closure remain open.',
     'counts':dict(counts),'max_floating_identity_errors':dict(errors),
     'spectral_cases':spectral_records,'weighted_host_cases':physical_records,
     'direct_atom_examples':cell_records,'conditional_ledger_examples':ledger,
     'pair_kernel_obstruction':pair_obstruction,
     'limitations':['No target-density AP-free counterexample is claimed.',
                    'Small-prime terminal error bounds can be vacuous; these tests audit identities and inequalities.',
                    'No numerical test proves an inverse theorem or asymptotic selection.',
                    'No global quadratic inverse theorem is assumed.']}
out['source_sha256']={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                       for name in ['MIXED_QUADRATIC_TERMINAL_20261016.md','LOG_DENSITY_ATTACK_20261016.md',Path(__file__).name]}
(ROOT/'LOG_DENSITY_VERIFICATION_20261016.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'counts':out['counts'],'max_errors':dict(errors)},indent=2))
