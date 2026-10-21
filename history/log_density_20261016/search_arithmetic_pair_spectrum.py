import numpy as np
from itertools import combinations
for p in [11,17,29,53,101]:
 for H in [1,max(1,p//4),(p-1)//2]:
  def f(z):return max(0,H+1-min(z%p,(-z)%p))/(H+1)
  for kind in ['linear','quadratic','mixed']:
   Om=list(range(p))
   K=np.zeros((p,p))
   for x in range(p):
    for h in range(p):
     F=(f(h) if kind!='quadratic' else 1)*(f(2*x*h)*f(h*h) if kind!='linear' else 1)
     for i,j in combinations(range(4),2):
      v=(x+i*h)%p;w=(x+j*h)%p;K[v,w]+=F;K[w,v]+=F
   J=np.eye(p)-np.ones((p,p))/p
   ev=np.linalg.eigvalsh(J@K@J)
   if ev[0]<-1e-8:
    print(p,H,kind,ev[0]);raise SystemExit
print('all PSD')
