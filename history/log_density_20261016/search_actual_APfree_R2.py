import numpy as np
from fractions import Fraction as Q
from itertools import combinations
rng=np.random.default_rng(14216)
for p in [7,11,13,17,23,29,53]:
 for H in sorted({1,2,p//4,(p-1)//2}):
  for c,b,xi in [(1,0,0),(1,1,1),(0,0,1)]:
   for start,length in [(0,p),(p-2,p//2),(0,p-2)]:
    Om=[v for v in range(p) if ((c*v*v+b*v if c else v)-start)%p<length]
    if not Om:continue
    P=np.array([int(v in Om) for v in range(p)])
    def fi(z):return max(0,H+1-min(z%p,(-z)%p))
    den=(H+1)**((1 if xi else 0)+(2 if c else 0))
    K=np.zeros((p,p),dtype=np.int64)
    for x in range(p):
     for h in range(p):
      V=[(x+j*h)%p for j in range(4)]
      if not all(P[v] for v in V):continue
      F=(fi(xi*h) if xi else 1)*(fi((2*c*x+b)*h)*fi(c*h*h) if c else 1)
      for i,j in combinations(range(4),2):K[V[i],V[j]]+=F;K[V[j],V[i]]+=F
    for it in range(100):
     A=set()
     perm=rng.permutation(Om)
     for v in perm:
      cand=A|{int(v)}
      if not any((2*y-x)%p in cand and (3*y-2*x)%p in cand for x in cand for y in cand if x!=y):A=cand
     av=len(A);n=len(Om);u=np.array([n*int(v in A)-av*P[v] for v in range(p)],dtype=np.int64)
     val=int(u@K@u)
     if val<0:
      print({'p':p,'H':H,'c':c,'b':b,'xi':xi,'start':start,'length':length,'Omega':Om,'A':sorted(A),'R2':str(Q(av*av*val,2*n**4*p*p*den))});raise SystemExit
print('No example in this search')
