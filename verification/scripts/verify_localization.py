# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Mangesh Raut

"""Finite checks of LOCALIZATION_BRIDGE.md. No asymptotic proof or network.

Exact arithmetic is used throughout; scalar powers/roots are integer checked.
"""
from fractions import Fraction as F
from itertools import product
from random import Random
import json

from verify_phase2 import REGIME_SET


def free4(aset, p):
    return not any((x+d)%p in aset and (x+2*d)%p in aset
                   and (x+3*d)%p in aset for x in aset for d in range(1,p))


def integer_root(n,d):
    lo,hi=1,n+1
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**d<=n:lo=mid
        else:hi=mid
    return lo


def dirichlet_step(p, freqs):
    R=integer_root(p-1,len(freqs))
    bins={}
    for t in range(R**len(freqs)+1):
        key=tuple(((t*xi)%p)*R//p for xi in freqs)
        if key in bins:
            q=t-bins[key]
            shifts=[min(xi*q%p,(-xi*q)%p) for xi in freqs]
            assert 0<q<p and max(shifts)<=p//R
            return R,q,shifts
        bins[key]=t
    raise AssertionError('Pigeonhole failed')


def terminal_geometry(p, coordinates):
    omega={x for x in range(p) if all((xi*x-start)%p<length
                                      for xi,start,length in coordinates)}
    if not omega or len(omega)==p:return None
    R,q,shifts=dirichlet_step(p,[row[0] for row in coordinates])
    starts={x for x in omega if (x-q)%p not in omega}
    assert 0<len(starts)<=sum(shifts)<=len(coordinates)*(p//R)
    seen=set();blocks=[];remainder=set()
    for start in starts:
        run=[];x=start
        while x in omega:
            assert x not in seen
            seen.add(x);run.append(x);x=(x+q)%p
        full=4*(len(run)//4)
        blocks.extend(run[i:i+4] for i in range(0,full,4))
        remainder.update(run[full:])
    assert seen==omega and len(remainder)<=3*len(starts)
    return omega,R,q,blocks,remainder,len(starts)


def check_terminal():
    rng=Random(20260913);windows=free_cases=0
    candidates=[]
    for p in (5,7,11,13):
        candidates.extend((p,[(1,0,n)]) for n in range(1,p))
    for _ in range(80):
        p=rng.choice((13,31,101,1009));d=rng.choice((1,2,3))
        coords=[(rng.randrange(1,p),rng.randrange(p),rng.randrange(1,p)) for _ in range(d)]
        candidates.append((p,coords))
    for p,coords in candidates:
        geom=terminal_geometry(p,coords)
        if geom is None:continue
        omega,R,q,blocks,rem,D=geom;windows+=1
        # The local one-cycle packing bound, independent of other differences.
        extremizer=set(rem)
        for block in blocks:extremizer.update(block[:3])
        assert len(extremizer)==3*len(blocks)+len(rem)
        assert 4*len(extremizer)<=3*len(omega)+3*D
        if len(omega)<=10:
            points=sorted(omega)
            for bits in product((0,1),repeat=len(points)):
                aset={x for x,b in zip(points,bits) if b}
                if not free4(aset,p):continue
                assert all(len(aset.intersection(block))<=3 for block in blocks)
                assert 4*len(aset)<=3*len(omega)+3*D
                assert 4*len(aset)<=3*len(omega)+3*len(coords)*(p//R)
                free_cases+=1
    return {'windows':windows,'actual_4ap_free_subsets':free_cases,
            'arithmetic':'integer roots, residues, and exact packing'}


def useful_atom(sizes, counts, eta):
    n=sum(sizes);mass=sum(counts);a=F(mass,n);M=len(sizes)
    candidates=[]
    for i,(s,k) in enumerate(zip(sizes,counts)):
        density=F(k,s)
        if density>=a*(1+eta/2) and F(k,mass)>=eta*a/(2*M):
            candidates.append(i)
    assert candidates
    return candidates[0]


def check_atom_lemma():
    checked=0
    for sizes in ((1,1),(1,2,3),(2,3,4),(1,2,2,3)):
        for counts in product(*(range(s+1) for s in sizes)):
            n=sum(sizes);a=F(sum(counts),n)
            if not 0<a<1:continue
            variance=sum(F(s,n)*(F(k,s)-a)**2 for s,k in zip(sizes,counts))
            if not variance:continue
            eta=min(F(1),variance/(a*a))
            useful_atom(sizes,counts,eta);checked+=1
    return checked


def check_signed_factors():
    results=[]
    for p,aset in ((5,{0,1}),(13,{0,1,3,9}),(101,set(REGIME_SET))):
        a=F(len(aset),p)
        Gnum=[sum(y in aset and (2*x-y)%p in aset for y in range(p)) for x in range(p)]
        G=[F(v,p) for v in Gnum]
        T=sum((F(x in aset)-a)*G[x] for x in range(p))/p
        K=max(F(2),max(G)/(a*a));count=preserved=single_preserved=0
        witnesses=[]
        for freqs in [(xi,) for xi in range(1,p)]+[(1,3)]:
            for offset in (0,p//4):
                cells={}
                for x in range(p):
                    label=tuple(4*((xi*x+offset)%p)//p for xi in freqs)
                    cells.setdefault(label,[]).append(x)
                sizes=[len(cell) for cell in cells.values()]
                counts=[sum(x in aset for x in cell) for cell in cells.values()]
                h=[sum(G[x] for x in cell)/len(cell) for cell in cells.values()]
                variance=sum(F(s,p)*(F(k,s)-a)**2 for s,k in zip(sizes,counts))
                hvar=sum(F(s,p)*(v-a*a)**2 for s,v in zip(sizes,h))
                corr=sum(F(s,p)*(F(k,s)-a)*v for s,k,v in zip(sizes,counts,h))
                assert corr*corr<=variance*hvar
                assert hvar<=(K-1)*a**4
                if T<0 and abs(T-corr)<=(-T)/2:
                    c=-T/a**3
                    eta=min(F(1),c*c/(4*(K-1)))
                    assert variance>=eta*a*a
                    useful_atom(sizes,counts,eta);preserved+=1
                    single_preserved+=len(freqs)==1
                    witnesses.append({'frequencies':list(freqs),'offset':offset,
                                      'cells':len(cells),'correlation':str(corr)})
                count+=1
        level_checked=False
        if T<0:
            c=-T/a**3;u=[1-v/(K*a*a) for v in G]
            assert sum(F(x in aset)*u[x] for x in range(p))/sum(u)>=a*(1+c/(K-1))
            good=[]
            for threshold in sorted(set(u)):
                E={x for x in range(p) if u[x]>=threshold}
                if E and F(len(E&aset),len(E))>=a*(1+c/(2*(K-1))) and F(len(E&aset),len(aset))>=c/(2*K):
                    good.append(threshold)
            assert good;level_checked=True
        results.append({'p':p,'size':len(aset),'T':str(T),'low_cubic':T<0,
                        'coarse_factors_checked':count,'signed_preserving_factors':preserved,
                        'single_character_preserving_factors':single_preserved,
                        'preserving_witnesses':witnesses,
                        'soft_level_set_checked':level_checked,
                        'scope':'finite diagnostic; no uniform compression theorem inferred'})
    return results


def main():
    assert free4({6,8,9,10},11) and not free4({0,2,3,4},5)
    for k in range(6,60):
        # A logarithmic number of vertices remains within the local-law range.
        a=F(1,2**k);m=3*k
        assert a*m<=F(1,3)
    print(json.dumps({'status':'proved bridge checks passed; extraction and target remain OPEN',
                      'terminal':check_terminal(),'factor_atom_cases':check_atom_lemma(),
                      'signed_factors':check_signed_factors(),
                      'Z11_wrap_counterexample':True,'external_dependencies':[]},indent=2))


if __name__=='__main__':main()
