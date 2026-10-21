"""Exact finite moment certificates and numerical Fourier-cap PSD checks.
Finite averaged samples are checked directly; the analytic theorem uses
expectations over ALL admissible trades, not this sample approximation.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json, math, random
import numpy as np
rng=random.Random(14220261012)
counts=Counter(); results=[]
# Independent exhaustive check of the zero-sum fourth-moment identity.
for n,k in [(6,2),(7,3),(8,4)]:
 rho=lambda j:F(math.prod(k-i for i in range(j)), math.prod(n-i for i in range(j)))
 lam=rho(2)-2*rho(3)+rho(4)
 kap=rho(1)-7*rho(2)+12*rho(3)-6*rho(4)
 for _ in range(20):
  z=[rng.randrange(-3,4) for _ in range(n-1)];z.append(-sum(z))
  w=[rng.randrange(-3,4) for _ in range(n-1)];w.append(-sum(w))
  lhs=sum(F(sum(z[i] for i in S)**2*sum(w[i] for i in S)**2) for S in combinations(range(n),k))/math.comb(n,k)
  rhs=lam*(sum(x*x for x in z)*sum(x*x for x in w)+2*sum(x*y for x,y in zip(z,w))**2)+kap*sum(x*x*y*y for x,y in zip(z,w))
  assert lhs==rhs
  counts['exact_fourth_moment_identities']+=1
for n,p,reps,ks in [(40,127,16,[4]),(64,193,16,[4,5]),(200,607,8,[4,8])]:
 edges={tuple(x+j*d for j in range(4)) for d in range(1,(n-1)//3+1) for x in range(n-3*d)}
 changes=Counter(); attempts=0
 bits=list(product([0,1],repeat=4))
 for root in sorted(edges):
  outside=[x for x in range(n) if x not in root]
  for _ in range(reps):
   while True:
    attempts+=1; ys=rng.sample(outside,4)
    trans=[(tuple(sorted(ys[i] if b[i] else root[i] for i in range(4))), -1 if sum(b)%2==0 else 1) for b in bits]
    if all(S not in edges for S,sgn in trans[1:]):break
   local=Counter()
   for S,sgn in trans:
    changes[S]+=sgn
    for T in combinations(S,3):local[T]+=sgn
   assert all(v==0 for v in local.values())
   counts['exact_balanced_trades']+=1
 assert all(changes[S]==-reps for S in edges)
 counts['AP_zero_moments']+=len(edges)
 changes={S:v for S,v in changes.items() if v}
 rows=Counter(); triple_rows=Counter()
 for S,v in changes.items():
  for P in combinations(S,2):rows[P]+=abs(v)
  for T in combinations(S,3):triple_rows[T]+=abs(v)
 rowmax=F(max(rows.values()),reps)
 triplemax=F(max(triple_rows.values()),reps)
 tv={F(v,reps) for v in changes.values()}|{F(0)}
 mindelta=min(tv); maxdelta=max(tv)
 checks=[]
 for k in ks:
  rho=lambda j:F(math.prod(k-i for i in range(j)),math.prod(n-i for i in range(j)))
  lam=rho(2)-2*rho(3)+rho(4);nu=rho(1)-rho(2)
  assert lam>=400*rho(4) and rowmax<=400
  counts['PSD_row_certificates']+=1
  assert triplemax*rho(4)<=rho(3)-rho(4)
  counts['exact_all_pair_literal_localizer_row_certificates']+=1
  for t in tv:
   for r in range(5):
    base=F(math.prod(k-i for i in range(r))*math.prod(n-k-i for i in range(4-r)),math.prod(n-i for i in range(4)))
    assert base+(-1)**(4-r)*rho(4)*t>=0
    counts['exact_cylinder_value_checks']+=1
  kap3=rho(1)-3*rho(2)+2*rho(3)
  kap4=rho(1)-7*rho(2)+12*rho(3)-6*rho(4)
  P=np.eye(n)-np.ones((n,n))/n
  for xi in (1,7):
   chars=np.exp(-2j*np.pi*xi*np.arange(n)/p)
   z=(chars-chars.mean())/n
   dH=np.zeros((n,n))
   for S,val in changes.items():
    for pair in combinations(S,2):
     other=[i for i in S if i not in pair]
     d=float(rho(4)*F(val,reps))*2*(z[other[0]]*z[other[1]].conjugate()).real
     i,j=pair;dH[i,j]+=d;dH[j,i]+=d
   H=float(lam)*(np.vdot(z,z).real*np.eye(n)+2*np.real(np.outer(z,z.conjugate())))+float(kap4)*np.diag(abs(z)**2)
   M=np.zeros((n+1,n+1));M[0,0]=float(nu)*np.vdot(z,z).real
   M[0,1:]=M[1:,0]=float(kap3)*(P@(abs(z)**2))
   M[1:,1:]=P@(H+dH)@P
   # All two-literal products times this cap, reconstructed using Xi=a+Q_i.
   a=float(rho(1)); tau=120*a/n
   first=a*M[0,0]+M[0,1:]
   joint=a*a*M[0,0]+a*(M[0,1:,None]+M[None,0,1:])+M[1:,1:]
   off=~np.eye(n,dtype=bool)
   for weighted,prob in [(joint,float(rho(2))), (first[:,None]-joint,a-float(rho(2))), (M[0,0]-first[:,None]-first[None,:]+joint,1-2*a+float(rho(2)))]:
    assert np.min((tau*prob-weighted)[off])>=-1e-10
    counts['numerical_cap_times_literal_pair_checks']+=n*(n-1)
   Q=np.zeros_like(M);Q[0,0]=1;Q[1:,1:]=float(nu)*P
   tau=120*float(rho(1))/n
   eigen=np.linalg.eigvalsh(tau*Q-M)
   assert eigen[0]>-1e-10,(n,k,xi,eigen[0])
   counts['numerical_all_linear_multiplier_cap_PSD_checks']+=1
  checks.append(k)
 results.append({'n':n,'p':p,'repetitions_per_edge':reps,'edges':len(edges),'attempts':attempts,'min_trade_mean':str(mindelta),'max_trade_mean':str(maxdelta),'max_absolute_pair_row':str(rowmax),'max_absolute_triple_row':str(triplemax),'checked_k':checks})
 print('passed n=',n,flush=True)
# Exact rational bounds imply all-n inequalities by monotonicity of factors.
n=200
bad=F(48,n-7)+F(144,(n-7)**2)+F(96*n,(n-7)**3)+F(24*n*n,(n-7)**4)
negative=F(288,(n-4)*(n-5))+F(48*n*n,math.prod(n-i for i in range(4,8)))
positive=F(96,n-4)+F(192*n,math.prod(n-i for i in range(4,7)))
load=12+F(48*n,n-4)+F(24*n*n,(n-4)*(n-5))
tripleload=12+F(144,n-4)+F(144*n,(n-4)*(n-5))+F(48*n*n,(n-4)*(n-5)*(n-6))
assert bad<F(1,2) and negative<1 and positive<1 and 4*load<400 and 2*tripleload<32
result={'status':'passed; no SELECT proof or actual AP-free counterexample','counts':dict(counts),'cases':results,'analytic_n200_bounds':{'bad_probability':str(bad),'negative_trade_bound':str(negative),'positive_trade_bound':str(positive),'pair_row_bound':str(4*load),'triple_row_bound':str(2*tripleload)},'numerical_tolerance':1e-10}
Path('select_positive_moments_verification_20261012.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
