# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Mangesh Raut

"""Exact checks for GLOBAL_COMPATIBILITY.md; not an asymptotic proof.

All arithmetic is rational or integer. No network or external dependencies.
The finite local laws are NOT asserted to arise from one fixed cyclic set.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import json


REGIME_SET = {0,20,22,25,30,32,33,34,37,38,39,48,49,52,53,54,
              58,59,78,79,81,84,88,90,93,94,95,97}


def local_law(m, a):
    weights = [1-m*a+comb(m,2)*a*a-comb(m,3)*a**3,
               a-(m-1)*a*a+comb(m-1,2)*a**3,
               a*a-(m-2)*a**3, a**3]
    return {mask: weights[mask.bit_count()] if mask.bit_count() <= 3 else F(0)
            for mask in range(1 << m)}


def check_local_laws():
    tested = 0
    for m in range(4, 11):
        for a in (F(1,m-2), F(1,2*(m-2)), F(1,10*m)):
            law = local_law(m,a)
            assert min(law.values()) >= 0 and sum(law.values()) == 1
            for subset in range(1 << m):
                j = subset.bit_count()
                expected = a**j if j <= 3 else F(0)
                assert sum(prob for mask,prob in law.items() if mask & subset == subset) == expected
            # Restricting a law to fewer coordinates gives the same law.
            marginal = {mask:F(0) for mask in range(1 << (m-1))}
            for mask,prob in law.items():
                marginal[mask & ((1 << (m-1))-1)] += prob
            assert marginal == local_law(m-1,a)
            q = sum(prob for mask,prob in law.items() if mask & 6 == 6)
            left = sum(prob for mask,prob in law.items() if mask & 7 == 7)
            right = sum(prob for mask,prob in law.items() if mask & 14 == 14)
            joint = sum(prob for mask,prob in law.items() if mask & 15 == 15)
            mixed = sum(prob*(F(bool(mask&1))-a)*int(mask&6 == 6)
                        *(F(bool(mask&8))-a) for mask,prob in law.items())
            assert q == a*a and left/q == right/q == a and joint == 0
            assert mixed == -a**4
            assert (a*(1-a))**2-a**4 == a*a*(1-2*a) >= 0
            tested += 1
    return tested


def check_overlap_hypergraph():
    # A generic affine 4x4 grid. All represented AP exclusions are imposed.
    points=[(x,y) for x in range(4) for y in range(4)]
    index={point:i for i,point in enumerate(points)}
    edges=set()
    for x,y in points:
        for u,v in points:
            dx,dy=u-x,v-y
            if dx==dy==0:
                continue
            line=[(x+j*dx,y+j*dy) for j in range(4)]
            if all(point in index for point in line):
                edges.add(sum(1 << index[point] for point in line))
    m=len(points); denominator=64
    assert denominator >= 3*m
    moments=[0 if any(mask&edge==edge for edge in edges)
             else denominator**(m-mask.bit_count()) for mask in range(1 << m)]
    probabilities=moments.copy()
    # Superset Mobius inversion, entirely in integers with common denominator.
    for bit in range(m):
        for mask in range(1 << m):
            if not mask & (1 << bit):
                probabilities[mask]-=probabilities[mask | (1 << bit)]
    assert min(probabilities)>=0
    assert sum(probabilities)==denominator**m
    reconstructed=probabilities.copy()
    for bit in range(m):
        for mask in range(1 << m):
            if not mask & (1 << bit):
                reconstructed[mask]+=reconstructed[mask | (1 << bit)]
    assert reconstructed==moments
    assert all(probabilities[mask]==0 for mask in range(1 << m)
               if any(mask&edge==edge for edge in edges))
    assert all(moments[mask]==denominator**(m-mask.bit_count())
               for mask in range(1 << m) if mask.bit_count()<=3)
    disjoint_triples=sum(1 << index[(x,y)] for x in range(3) for y in (0,2))
    assert disjoint_triples.bit_count()==6
    assert moments[disjoint_triples]==denominator**(m-6)
    return {'points':m,'distinct_4AP_edges':len(edges),'density':'1/64',
            'assignments':1 << m,'all_constraints_satisfied':True,
            'independent_six_point_moment':'(1/64)^6',
            'scope':'finite probability law, not a fixed cyclic set or target-density construction'}


def check_fixed_size_extension():
    p,k,m=1009,32,10
    points=[(0,0),(1,0),(2,0),(3,0),(0,1),(0,2),(0,3),(1,1),(2,1),(1,2)]
    index={point:i for i,point in enumerate(points)}
    edges=set()
    for x,y in points:
        for u,v in points:
            if (x,y)==(u,v): continue
            line=[(x+j*(u-x),y+j*(v-y)) for j in range(4)]
            if all(z in index for z in line): edges.add(sum(1<<index[z] for z in line))
    def falling(n,j):
        out=1
        for i in range(j):out*=n-i
        return out
    assert F(k*m,p)<=F(1,3) and m<=k<=p-m
    den=falling(p,m)
    moments=[0 if any(mask&e==e for e in edges) else
             falling(k,mask.bit_count())*falling(p-mask.bit_count(),m-mask.bit_count())
             for mask in range(1<<m)]
    probabilities=moments.copy()
    for bit in range(m):
        for mask in range(1<<m):
            if not mask&(1<<bit): probabilities[mask]-=probabilities[mask|(1<<bit)]
    assert min(probabilities)>=0 and sum(probabilities)==den
    comparisons=0
    for subset in range(1<<m):
        r=subset.bit_count()
        if r>3:continue
        for s in range(4-r):
            val=sum(probabilities[mask]*falling(k-mask.bit_count(),s)
                    for mask in range(1<<m) if mask&subset==subset)
            actual=F(val,den*falling(p-m,s))
            assert actual==F(falling(k,r+s),falling(p,r+s))
            comparisons+=1
    assert F(k-2,p-2)==F(k,p)-2*(1-F(k,p))/(p-2)
    return {'ground_set_size':p,'fixed_sample_size':k,'local_points':m,
            'local_4AP_edges':len(edges),'global_moment_comparisons':comparisons,
            'conditional_endpoint_rate':str(F(k-2,p-2)),
            'global_density':str(F(k,p)),
            'scope':'fixed-size random sets avoid only the represented local edges'}


def fiber_stats(p, aset):
    n = len(aset)
    if n < 2 or n == p:
        return None
    a = F(n,p)
    fibers = []
    for d in range(1,p):
        k = sum(x in aset and (x+d)%p in aset for x in range(p))
        ell = sum(x in aset and (x+d)%p in aset and (x+2*d)%p in aset for x in range(p))
        if not k:
            assert ell == 0
            continue
        z = p*ell-n*k
        assert z != 0  # gcd(n,p)=1 and 0<k<p.
        assert 1 <= k <= n-1
        fibers.append((k,ell,z))
    assert sum(k for k,_,_ in fibers) == n*(n-1)
    active = len(fibers)
    assert active >= n
    variance = sum(F(z*z,k) for k,_,z in fibers) / (p*p*n*(n-1))
    lattice = F(active*active,p*p*n*n*(n-1)*(n-1))
    assert variance >= lattice >= F(1,p*p*(n-1)*(n-1))
    mean_r = F(sum(ell for _,ell,_ in fibers),n*(n-1))
    T = F(n+sum(ell for _,ell,_ in fibers),p*p)-a**3
    Q = a*a-a/p
    assert T-a*(1-a)/p == Q*(mean_r-a)
    return {'p':p,'size':n,'active_differences':active,'weighted_variance':str(variance),
            'lattice_lower_bound':str(lattice),'weighted_mean_r':str(mean_r),'alpha':str(a)}


def check_prime_fibers():
    tested = 0
    for p in (5,7,11):
        for bits in product((0,1),repeat=p):
            if fiber_stats(p,{i for i,b in enumerate(bits) if b}) is not None:
                tested += 1
    return tested, fiber_stats(101,REGIME_SET)


def check_relative_center():
    count = 0
    for p,n in ((19,5),(31,8)):
        window = set(range(n))
        w = F(n,p)
        for bits in product((0,1),repeat=n):
            aset = {i for i,b in enumerate(bits) if b}
            if not aset or len(aset)==n:
                continue
            a = F(len(aset),n)
            q = [0]*p; left=[0]*p; right=[0]*p; joints=[0]*p
            mixed = F(0)
            for y in aset:
                for z in aset:
                    u,v = (2*y-z)%p,(2*z-y)%p
                    if u not in window or v not in window:
                        continue
                    d=(z-y)%p
                    q[d]+=1; left[d]+=u in aset; right[d]+=v in aset
                    joints[d]+=(u in aset and v in aset)
                    mixed+=(F(u in aset)-a)*(F(v in aset)-a)
            if any(joints[1:]):
                continue
            phi=F(sum(q),p*p); sigma=F(sum(left),p*p); M=mixed/(p*p)
            assert sum(left)==sum(right)
            Q=phi-a*w/p
            center=a*w*(1-a)**2/p-a*a*Q
            assert M==a*w/p-2*a*sigma+a*a*phi
            assert M-center==-2*a*(sigma-a*phi-a*(1-a)*w/p)
            if Q:
                delta_mean=sum(F(left[d]+right[d])-2*a*q[d] for d in range(1,p))/(p*p*Q)
                assert M-center == -a*Q*delta_mean
            count += 1
    return count


def check_scalar_recurrences():
    # Rational near-extremizer of the sharp endpoint bound: r=1/3.
    a=F(1,1000); kappa=F(1,64); initial=a; mu_product=F(1); retained=F(1)
    for j in range(200):
        ap=a/(1-3*kappa*a)
        mu=(1-3*kappa*a)/3
        r=mu*ap/a
        delta_u=1/a-1/ap
        assert mu*(ap-a)==kappa*a*a
        assert r==F(1,3) and r*delta_u==kappa
        mu_product*=mu;retained*=r;a=ap
        assert mu_product==retained*initial/a
    # Current rank-dependent guaranteed gains allow bounded total progress.
    a=F(1,10); u0=1/a
    for d in range(20):
        old=a;mu=1-a/F(64*3**d);a=old/mu
        assert mu*(a-old)==old*old/F(64*3**d)
        assert mu*a/old==1
    assert u0-1/a==F(3,128)*(1-F(1,3**20))
    # Exact generic quadratic-increment reciprocal update.
    a=F(1,20);k=F(1,10)
    for _ in range(6):
        ap=a+k*a*a
        assert 1/a-1/ap==k/(1+k*a)
        a=ap
    return {'endpoint_path_steps':200,'rank_stalling_steps':20,
            'interpretation':'scalar feasible bounds only, not a sequence of actual sets'}


def check_small_spectral_family():
    out=[]
    for p in (19,31,61):
        window=set(range(6));aset={1,2,3};a=F(1,2);w=F(6,p)
        g={x:F(x in aset)-a for x in window}
        inv3=pow(3,-1,p)
        K={(u,v):int((2*u+v)*inv3%p in aset and (u+2*v)*inv3%p in aset)
           for u in window for v in window}
        M=sum(g[u]*K[u,v]*g[v] for u in window for v in window)/(p*p)
        assert M==F(-1,4*p*p)
        assert all(sum(g[x] for x in window if x%3==label)==0 for label in range(3))
        v=F(3,2*p)
        baseline=a*a*(w-F(1,p))*v+a*(1-a)*w*v
        excess=M-a*w*(1-a)*(1-a-a*a)/p
        assert baseline==F(33,8*p*p) and excess==F(-5,8*p*p)
        assert -excess/baseline==F(5,33)
        out.append({'p':p,'relative_deficit':'5/33',
                    'largest_atom_upper_bound':str(F(252,11*p*p)),
                    'window_size':6,'meets_large_window_cutoff':False})
    return out


def check_weighted_sampling():
    results=[]
    for p,aset in ((5,{0,1}),(13,{0,1,3,9}),(101,REGIME_SET)):
        alpha=F(len(aset),p)
        B=[int(x in aset) for x in range(p)]
        G=[F(sum(B[y]*B[(2*x-y)%p] for y in range(p)),p) for x in range(p)]
        nu=[(b+alpha)/(2*alpha) for b in B]
        triple=sum(B[x]*G[x] for x in range(p))/p
        low_cubic=triple<=alpha**3
        assert sum(G)/p==alpha**2 and sum(nu)/p==1
        EG=sum(nu[x]*G[x] for x in range(p))/p
        EG2=sum(nu[x]*G[x]**2 for x in range(p))/p
        assert EG==(triple+alpha**3)/(2*alpha)
        if low_cubic:
            assert EG<=alpha**2
        K=max(G)/alpha**2
        for k in (1,2):
            total=F(0);cases=0
            for ys in product(sorted(aset),repeat=k):
                H=[alpha*sum(B[(2*x-y)%p] for y in ys)/k for x in range(p)]
                err2=sum(nu[x]*(H[x]-G[x])**2 for x in range(p))/p
                err1=sum(nu[x]*abs(H[x]-G[x]) for x in range(p))/p
                total+=err2;cases+=1
                corr=sum((B[x]-alpha)*(H[x]-G[x]) for x in range(p))/p
                assert corr*corr<=4*alpha*alpha*err2
                assert err1>=alpha**2*(1-K*k*alpha)/2
            expectation=total/cases
            assert expectation==(alpha*EG-EG2)/k
            if low_cubic:
                assert expectation<=alpha**3/k
            results.append({'p':p,'size':len(aset),'samples_per_tuple':k,
                            'tuples_checked':cases,'expected_weighted_squared_error':str(expectation),
                            'low_cubic_hypothesis':low_cubic,
                            'low_cubic_upper_bound':str(alpha**3/k) if low_cubic else None,
                            'spread_K':str(K)})
    return results


def main():
    local=check_local_laws()
    fibers,witness=check_prime_fibers()
    result={'status':'exact compatibility diagnostics passed; local target remains OPEN',
            'overlapping_local_laws':local,'prime_subset_fiber_checks':fibers,
            'overlap_hypergraph':check_overlap_hypergraph(),
            'fixed_size_extension':check_fixed_size_extension(),
            'relative_center_checks':check_relative_center(),
            'Z101_fiber_witness':witness,'scalar_recurrences':check_scalar_recurrences(),
            'spread_weighted_spectrum_family':check_small_spectral_family(),
            'weighted_sampling':check_weighted_sampling(),
            'arithmetic':'integers and exact fractions','external_dependencies':[]}
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
