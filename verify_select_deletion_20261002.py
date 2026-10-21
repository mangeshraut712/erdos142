"""Finite checks of the deletion degree certificate; SELECT is unresolved."""
import cmath
import itertools
import json
import math
from pathlib import Path

counts={"hosts":0,"degree_vertices":0,"apfree_hole_certificates":0,"codegree_pairs":0}
for p in [5,7,11,13]:
    ep=lambda t:cmath.exp(2j*math.pi*(t%p)/p)
    edges=[tuple((x+j*h)%p for j in range(4)) for x in range(p) for h in range(1,p)]
    for v in range(p):
        for z in range(v+1,p):
            assert sum(v in e and z in e for e in edges)<=12
            counts["codegree_pairs"]+=1
    for length in range(1,p+1):
        S=set(range(length)); beta=length/p
        coeff=[sum(ep(-t*y) for y in S)/p for t in range(p)]
        K=sum(map(abs,coeff))
        C={x for x in range(p) if x*x%p in S}
        if not C:
            continue
        PPhiE=[sum(coeff[t]*abs(coeff[3*t%p])**2*ep(t*y) for t in range(p)) for y in range(p)]
        PPhiM=[sum(coeff[3*t%p]*abs(coeff[t])**2*ep(3*t*y) for t in range(p)) for y in range(p)]
        assert all(abs(z.imag)<1e-10 and -1e-10<=z.real<=beta**2+1e-10 for z in PPhiE+PPhiM)
        assert sum(abs(coeff[t])*abs(coeff[3*t%p])**2 for t in range(p))<=beta**2+1e-10
        assert sum(abs(coeff[3*t%p])*abs(coeff[t])**2 for t in range(p))<=beta**2+1e-10
        hC=[sum(all((v+(j-i)*h)%p in C for j in range(4) if j!=i) for i in range(4) for h in range(p))/p for v in range(p)]
        Lambda=sum(all((x+j*h)%p in C for j in range(4)) for x in range(p) for h in range(p))/p**2
        b=len(C)/p
        assert abs(sum(hC[v] for v in C)/p-4*Lambda)<1e-10
        for v in range(1,p):
            H=(2*PPhiE[v*v%p]+2*PPhiM[v*v%p]).real
            assert abs(hC[v]-H)<=4*K**3/math.sqrt(p)+1e-10
            counts["degree_vertices"]+=1
        # All subsets for smaller hosts; deterministic sampled masks otherwise.
        cvec=sorted(C)
        masks=range(1<<len(cvec)) if len(cvec)<=9 else range(0,1<<len(cvec),17)
        for mask in masks:
            A={v for i,v in enumerate(cvec) if mask>>i&1}
            if any(all(v in A for v in e) for e in edges):
                continue
            D=C-A; theta=len(D)/len(C)
            rr=[(v in D)-theta*(v in C) for v in range(p)]
            corr=sum(rr[v]*hC[v] for v in range(p))/p
            assert corr+1e-10>=(1-4*theta)*Lambda-b/p
            rho=max(abs(sum(rr[v]*ep(t*v*v) for v in range(p))/p) for t in range(1,p))
            lower=max(0,(1-4*theta)*Lambda-4*K**3/math.sqrt(p)-5/p)/(4*beta**2)
            assert rho+1e-10>=lower
            counts["apfree_hole_certificates"]+=1
        counts["hosts"]+=1

result={"checks":counts,"status":"supporting checks passed; SELECT and target unresolved"}
Path(__file__).with_name('select_deletion_verification_20261002.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
