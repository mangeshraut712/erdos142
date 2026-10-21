"""Finite checks of the relative progression marginal/main-term inequality."""
import json, math
from fractions import Fraction as Q
from pathlib import Path
checks=0
for p in (7,11,13,17):
 for n in range(4,p+1):
  omega=list(range(n)); os=set(omega)
  aps=[tuple((x+j*d)%p for j in range(4)) for x in omega for d in range(p) if all((x+j*d)%p in os for j in range(4))]
  deg=[{x:0 for x in omega} for _ in range(4)]
  for e in aps:
   for j,x in enumerate(e): deg[j][x]+=1
  T=len(aps); r=[{x:Q(n*deg[j][x],T) for x in omega} for j in range(4)]
  R=[sum(t*t for t in row.values())/n for row in r]
  for mask in range(1,min(1<<n,64)):
   B={x:int(mask>>x&1) for x in omega}; a=Q(sum(B.values()),n)
   for mod in (1,2,3):
    g={x:Q(sum(B[y] for y in omega if y%mod==x%mod),sum(y%mod==x%mod for y in omega)) for x in omega}
    v=sum((g[x]-a)**2 for x in omega)/n
    main=sum(math.prod(g[x] for x in e) for e in aps)/T
    lower=float(a**4)*(1-math.sqrt(float(v))/(2*float(a))*sum(math.sqrt(float(t))+math.sqrt(float(t-1)) for t in R))
    assert float(main)+1e-12>=lower
    assert all(t<=Q(n*n,T) for t in R)
    checks+=1
result={'status':'passed','relative_main_term_cases':checks,'scope':'finite checks support the symbolic relative-marginal proof; SELECT unresolved'}
Path('select_window_verification_20261002.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
