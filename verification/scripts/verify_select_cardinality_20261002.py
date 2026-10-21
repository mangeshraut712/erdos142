"""Exact finite balanced-trade checks; no AP-free construction is asserted."""
from collections import Counter
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import random

rng=random.Random(1422026100203)
counts={"root_edges":0,"balanced_trades":0,"cardinality_triples":0,
        "PSD_row_certificates":0,"harmonic_quadratic_forms":0,
        "slow_threshold_trajectories":0}
cases=[]
for n,p in [(40,127),(64,193),(200,607)]:
    assert n-1 < p/3
    omega=list(range(n))
    edges={tuple(x+j*d for j in range(4))
           for d in range(1,(n-1)//3+1) for x in range(n-3*d)}
    changes=Counter(); loads=Counter()
    attempts=0
    for root in sorted(edges):
        outside=[i for i in omega if i not in root]
        while True:
            attempts+=1
            ys=rng.sample(outside,4)
            trans=[]
            for bits in itertools.product([0,1],repeat=4):
                S=tuple(sorted(ys[i] if bits[i] else root[i] for i in range(4)))
                trans.append((S,-1 if sum(bits)%2==0 else 1))
            if all(S not in edges for S,_ in trans[1:]):
                break
        # itertools begins with the all-zero root.
        assert trans[0][0]==root
        local=Counter()
        for S,sign in trans:
            changes[S]+=sign
            for T in itertools.combinations(S,3): local[T]+=sign
            for P in itertools.combinations(S,2): loads[P]+=1
        assert all(v==0 for v in local.values())
        counts["balanced_trades"]+=1
    assert all(changes[e]==-1 for e in edges)
    row_abs=Counter()
    for S,value in changes.items():
        if value:
            for P in itertools.combinations(S,2): row_abs[P]+=abs(value)
    assert all(row_abs[P]<=loads[P] for P in row_abs)
    Bn=800+16*math.log(n)
    if n>=200: assert max(loads.values())<=Bn
    # Check every triple if small; random triples if large, in addition to
    # the exact balancing check of EVERY individual trade above.
    triples=list(itertools.combinations(omega,3)) if n<=64 else [
        tuple(sorted(rng.sample(omega,3))) for _ in range(200)]
    for T in triples:
        assert sum(changes[tuple(sorted(T+(i,)))] for i in omega if i not in T)==0
        counts["cardinality_triples"]+=1
    checked=[]
    for k in [4,6,8]:
        rho=lambda j: Fraction(math.prod(k-i for i in range(j)),
                               math.prod(n-i for i in range(j)))
        lam=rho(2)-2*rho(3)+rho(4)
        assert lam==rho(2)*Fraction((n-k)*(n-k-1),(n-2)*(n-3))
        # Use the actual verified row norm, also valid below theorem n>=200.
        if lam < rho(4)*max(row_abs.values()): continue
        counts["PSD_row_certificates"]+=1
        for _ in range(50):
            i,j,k0,l=rng.sample(omega,4)
            c={tuple(sorted(P)):v for P,v in [((i,j),1),((k0,l),1),((i,k0),-1),((j,l),-1)]}
            val=lam*sum(v*v for v in c.values())
            for P,v in c.items():
                for Q,w in c.items():
                    if not set(P)&set(Q):
                        val+=rho(4)*v*w*changes[tuple(sorted(P+Q))]
            assert val>=0
            counts["harmonic_quadratic_forms"]+=1
        # Explicit fixed-cardinality moment identities through cubic multipliers.
        for T in triples[:25]:
            modified_sum=3*rho(3)+sum(rho(4)*(1+changes[tuple(sorted(T+(i,)))])
                                     for i in omega if i not in T)
            assert modified_sum==k*rho(3)
        checked.append(k)
    assert checked
    counts["root_edges"]+=len(edges)
    cases.append({"n":n,"p":p,"edges":len(edges),"alternative_attempts":attempts,
        "max_pair_load":max(loads.values()),"max_absolute_pair_row":max(row_abs.values()),
        "verified_k_values":checked,
        "negative_nonAP_fourth_moments":sum(v<-1 for S,v in changes.items() if S not in edges),
        "scope":"degree-four PSD functional only; no representing law or pointwise Fourier caps"})

# Focused scalar check of the strictly weaker stopping threshold.
R=lambda a:math.log(math.log(math.e**2/a))
ell=lambda a:math.log(2/a)
for t,overshoot in itertools.product([.001,.01,.1],[1,3,10]):
    eta=lambda a:.125*a**.25*R(a)/ell(a)
    rank=lambda a:math.ceil(a**-.25/ell(a))
    assert 0<R(t)<ell(t)
    D,S=1.0,math.log(1/t)
    e=t
    while e<=.8:
        hi=min(2*e,.8); m=eta(e)
        rmax=math.ceil(e**-.25/ell(hi)); M=1+4*math.log(2)/m
        D+=M*rmax; S+=M*(math.log(2/(m*e))+rmax*math.log(4)); e*=2
    a=t; d=1; loss=0.0
    while a<=.8:
        s=rank(a); ap=min(1,a*(1+overshoot*eta(a)/2))
        loss+=math.log(ap/a)-math.log(eta(a)*a/2)+s*math.log(4)
        d+=s; a=ap
    assert d<=D+1e-8 and loss<=S+1e-8
    counts["slow_threshold_trajectories"]+=1

result={"status":"exact finite trade/PSD/cardinality checks passed; SELECT unresolved",
        "checks":counts,"cases":cases,"external_dependencies":[]}
(Path(__file__).resolve().parents[1] / "results" / 'select_cardinality_verification_20261002.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
