"""Exact cell identities; numerical spectral projections; finite diagnostics only."""
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import itertools, json
import numpy as np
counts=Counter(); cancellation=None

def check(p,S,omega):
 global cancellation
 B=np.array([int(x in S) for x in range(p)])
 H=np.array([sum(int(B[(x+d)%p]*B[(x+2*d)%p]*B[(x+3*d)%p]) for d in range(1,p)) for x in range(p)])
 assert not np.any(B*H)
 q=[F(int(x),p) for x in H]
 h=[q[x]+F(int(B[x]),p) for x in range(p)]
 assert all(B[x]*h[x]==F(int(B[x]),p) for x in range(p))
 threefree=not any(B[x]*B[(x+d)%p]*B[(x+2*d)%p] for x in range(p) for d in range(1,p))
 assert (not np.any(H))==threefree
 b=np.fft.fft(B)/p; qhat=np.fft.fft(np.array([float(x) for x in q]))/p
 assert max(abs(sum(b[r]*qhat[(t-r)%p] for r in range(p))) for t in range(p))<1e-11
 if threefree and S:
  a=F(len(S),p);bound=max(F(0),(a*a-F(1,p))/(1-a))
  assert max(abs(b[1:]))+1e-11>=float(bound)
  counts['q_zero_Fourier_branch']+=1
 for factor in ('trivial','quarter','parity'):
  cells=[[x for x in omega if (0 if factor=='trivial' else 4*x//p if factor=='quarter' else x%2)==j] for j in range(4 if factor=='quarter' else 2 if factor=='parity' else 1)]
  cells=[C for C in cells if C]
  u={};k={};z={};w={};gm={};tm={};Smean=F(0);W=F(0);U=F(0);component=F(0)
  for C in cells:
   g=F(sum(int(B[x]) for x in C),len(C));T=sum(q[x] for x in C)/len(C)
   alpha=T/(1-g) if g!=1 else F(0)
   for x in C:
    gm[x]=g;tm[x]=T
    u[x]=F(int(B[x]))-g;k[x]=q[x]-T;w[x]=alpha*u[x];z[x]=k[x]+w[x]
    assert k[x]==-w[x]+z[x]
   assert sum(z[x] for x in C)==0
   assert all(B[x]*z[x]==0 for x in C)
   assert sum(u[x]*z[x] for x in C)==0
   assert sum(w[x]*z[x] for x in C)==0
   Smean+=len(C)*g*T;component+=len(C)*g*T*alpha
   counts['exact_cell_identities']+=1
  n=len(omega);Smean/=n;component/=n
  U=sum(u[x]**2 for x in omega)/n;W=sum(k[x]**2 for x in omega)/n
  assert sum(u[x]*k[x] for x in omega)/n==-Smean
  assert W==component+sum(z[x]**2 for x in omega)/n
  assert Smean*Smean<=U*W
  assert Smean*Smean<=U*component
  a=sum(F(int(B[x])) for x in omega)/n;T=sum(q[x] for x in omega)/n
  v=sum((gm[x]-a)**2 for x in omega)/n
  between=sum((tm[x]-T)**2 for x in omega)/n
  covariance=sum((gm[x]-a)*(tm[x]-T) for x in omega)/n
  assert Smean==a*T+covariance
  assert covariance*covariance<=v*between
  assert sum((q[x]-T)**2 for x in omega)/n==between+W
  # Relative projection onto cell-centered characters, with the actual Gram.
  uv=np.array([float(u[x]) for x in omega]);kv=np.array([float(k[x]) for x in omega])
  wv=np.array([float(w[x]) for x in omega]);zv=np.array([float(z[x]) for x in omega])
  for freqs in ((1,), (1,2,3)):
   M=np.exp(2j*np.pi*np.outer(omega,freqs)/p)
   for C in cells:
    ids=[omega.index(x) for x in C];M[ids]-=M[ids].mean(axis=0)
   P=M@np.linalg.pinv(M,rcond=1e-12)
   pu=P@uv;pk=P@kv;tail=np.linalg.norm(kv-pk)/np.sqrt(n)
   gain=float(np.vdot(pu,pu).real/n);energy=float(np.vdot(pk,pk).real/n)
   if energy>1e-20:
    lower=max(0,float(Smean)-np.sqrt(float(U))*tail)**2/energy
    assert gain+1e-10>=lower
   cross=float(np.vdot(P@wv,P@zv).real/n)
   if cancellation is None and cross>1e-8:
    cancellation={'p':p,'set':sorted(S),'window':omega,'factor':factor,'frequencies':freqs,'projected_w_z_inner_product':cross,'global_w_z_inner_product':float(np.vdot(wv,zv).real/n),'meaning':'positive cross term reduces projected energy of k=-w+z'}
   counts['relative_Gram_projection_checks']+=1
  counts['exact_pairing_and_variance_checks']+=1
 counts['AP_free_sets_checked']+=1

for p in (7,11):
 for bits in itertools.product((0,1),repeat=p):
  S={i for i,b in enumerate(bits) if b}
  if any(all((x+j*d)%p in S for j in range(4)) for x in S for d in range(1,p)):continue
  check(p,S,list(range(p)))
for p,n,S in [(101,25,{0,1,3}),(59,14,{sum(b[j]*3**j for j in range(3)) for b in itertools.product((0,1),repeat=3)}),(277,69,{x+16*y for x in (0,1,4) for y in (0,1,4)}),(11,3,{0,1,2})]:
 check(p,S,list(range(n)))
# A window can hide all endpoint completions while containing a 3-AP.
p=11;S={0,1,2};omega=list(range(3))
H=[sum(all((x+j*d)%p in S for j in (1,2,3)) for d in range(1,p)) for x in range(p)]
assert all(H[x]==0 for x in omega) and any(H) and {0,1,2}<=S
assert cancellation is not None
result={'status':'passed; exact partial theorem; SELECT unresolved','counts':dict(counts),'spectral_cancellation_example':cancellation,'window_zero_example':{'p':11,'set':[0,1,2],'window':[0,1,2],'completion_counts':H,'scope':'finite normalization diagnostic; not target-regime evidence'},'scope':'Integer/Fraction identities exact; Fourier and Gram checks tolerance 1e-10. No asymptotic character budget proved.'}
(Path(__file__).resolve().parents[1] / "results" / 'COMPLETION_PROJECTION_VERIFICATION_20261013.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
