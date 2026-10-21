"""Finite supporting checks; no target asymptotic proof by computation."""
import itertools
import json
import math
from pathlib import Path

c0=math.log(1.5)
cases=0
for sizes in itertools.product(range(2,8), repeat=3):
    r=len(sizes)
    S=sum(math.log(m) for m in sizes)
    lower=sum(math.log(2*m-1) for m in sizes)
    for pad in [0,0.1,1,5,25,100]:
        L=lower+pad
        beta=L-S+math.log(max(sizes))
        assert beta+1e-12>=min(L/2,math.sqrt(2*c0*L))
        cases+=1

finite=0
for r in range(1,4):
    for m in range(2,6):
        box=list(itertools.product(range(m), repeat=r))
        shells={}
        for u in box:
            shells.setdefault(sum(x*x for x in u),[]).append(u)
        assert max(map(len,shells.values()))<=2*m**(r-1)
        diffs={tuple(x-y for x,y in zip(u,v)) for u in box for v in box}
        assert len(diffs)==(2*m-1)**r
        # q>4(m-1) gives inverse preservation of every four-point sum.
        q=4*m-3
        encode=lambda u:sum(x*q**i for i,x in enumerate(u))
        top=max(map(encode,box))
        candidate=2*top+1
        while candidate<5 or any(candidate%d==0 for d in range(2,math.isqrt(candidate)+1)):
            candidate+=1
        p=candidate
        by_image={}
        for d in diffs:
            image=sum(x*q**i for i,x in enumerate(d))%p
            assert image not in by_image or by_image[image]==d
            by_image[image]=d
        assert len(by_image)==len(diffs)<=p
        for shell in shells.values():
            image={encode(u)%p for u in shell}
            for x,y in itertools.product(image, repeat=2):
                if x!=y:
                    assert (2*y-x)%p not in image
            alpha=len(image)/p
            bound=2*math.exp(-min(math.log(p)/2,math.sqrt(2*c0*math.log(p))))
            assert alpha<=bound+1e-12
            finite+=1

result={"parameter_cases":cases,"finite_shells_and_embeddings":finite,
        "status":"supporting checks passed; general claims proved in accompanying markdown; target unresolved"}
Path(__file__).with_name('route_constructions_verification_20261002.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
