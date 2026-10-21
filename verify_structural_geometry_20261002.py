"""Supporting finite checks for structural geometry; H is not proved."""
import cmath
import itertools
import json
import math
import random
from pathlib import Path

rng=random.Random(1421002)
counts={"interval_l1":0,"gauss":0,"window_boundary":0,"short_shift":0,"quadratic_cell_energy":0,"relative_quadratic_count":0}
for p in [5,7,11,13,17,23,31,47]:
    ep=lambda t:cmath.exp(2j*math.pi*(t%p)/p)
    Cp=2+math.log(p)
    for start in range(p):
        for length in range(1,p+1):
            J={(start+i)%p for i in range(length)}
            hats=[sum(ep(-k*x) for x in J)/p for k in range(p)]
            assert sum(map(abs,hats))<=Cp+1e-10
            counts["interval_l1"]+=1
    for c in range(1,p):
        for b in [0,1,p-1]:
            val=sum(ep(c*x*x+b*x) for x in range(p))/p
            assert abs(abs(val)-p**-.5)<1e-10
            counts["gauss"]+=1
    for repeat in range(30):
        d=rng.randint(1,3)
        chars=[rng.randrange(1,p) for _ in range(d)]
        arcs=[]
        for xi in chars:
            start=rng.randrange(p)
            arcs.append({(start+t)%p for t in range(rng.randint(1,max(1,p//3)))})
        omega={x for x in range(p) if all(xi*x%p in arc for xi,arc in zip(chars,arcs))}
        if not omega:
            continue
        for h in range(p):
            moved={(x+h)%p for x in omega}
            delta=[min(xi*h%p,p-xi*h%p) for xi in chars]
            assert len(omega-moved)<=sum(delta)
            counts["window_boundary"]+=1
        for Q in [2,3,5]:
            bins={}
            for x in range(p):
                key=tuple((xi*x%p)*Q//p for xi in chars)
                bins.setdefault(key,[]).append(x)
            points=max(bins.values(),key=len)
            assert len(points)>=math.ceil(p/Q**d)
            shifts={(x-points[0])%p for x in points}
            for h in shifts:
                assert all(min(xi*h%p,p-xi*h%p)<=p//Q for xi in chars)
                moved={(x+h)%p for x in omega}
                assert len(omega^moved)/len(omega)<=2*d*p/(len(omega)*Q)+1e-10
            counts["short_shift"]+=1
        s=rng.randint(1,3)
        xis=[rng.randrange(1,p) for _ in range(s)]
        rotations=[rng.random() for _ in range(s)]
        cells={}
        for x in omega:
            key=tuple(int(4*((xi*x/p-t)%1)) for xi,t in zip(xis,rotations))
            cells.setdefault(key,[]).append(x)
        c=rng.randrange(1,p); b=rng.randrange(p)
        energy=sum(len(V)/len(omega)*abs(sum(ep(c*x*x+b*x) for x in V)/len(V))**2 for V in cells.values())
        bound=4**s*p**-.5*(p/len(omega))*Cp**(d+s)
        assert energy<=bound+1e-10
        # Sharper individual-cell bound, before the loose atom-count sum.
        for V in cells.values():
            corr=abs(sum(ep(c*x*x+b*x) for x in V)/p)
            assert corr<=p**-.5*Cp**(d+s)+1e-10
        counts["quadratic_cell_energy"]+=1
        slength=rng.randrange(1,p)
        Sset={t for t in range(slength)}
        Shat=[sum(ep(-t*x) for x in Sset)/p for t in range(p)]
        Z=sum(abs(Shat[t])**2*abs(Shat[3*t%p])**2 for t in range(p))
        WB={x for x in omega if (c*x*x+b*x)%p in Sset}
        lc=lambda U:sum(all((x+j*h)%p in U for j in range(4)) for x in range(p) for h in range(p))/p**2
        Wnorm=sum(abs(sum(ep(-t*x) for x in omega)/p) for t in range(p))
        Snorm=sum(map(abs,Shat))
        assert abs(lc(WB)-Z*lc(omega))<=p**-.5*Wnorm**4*Snorm**4+1e-10
        assert lc(omega)+1e-10>=(len(omega)/p)**2/3**d
        if slength/p<=1/12:
            assert Z+1e-10>=8/(3*math.pi**4)*(slength/p)**3
        counts["relative_quadratic_count"]+=1

result={"checks":counts,"status":"finite supporting checks passed; H unresolved"}
Path(__file__).with_name('structural_geometry_verification_20261002.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
