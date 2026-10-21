"""Exact checks for harmonic extension identities and completion certificates."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import json,math
counts=Counter()
# Independently expand the saved rational global law; no LP solver is used.
finite=json.loads((Path(__file__).resolve().parents[1] / "results" / 'degree_six_finite_extension_20261012.json').read_text())
fp=finite['p'];fk=finite['k']
def affine_orbit(S):
 return {tuple(sorted((b+d*x)%fp for x in S)) for b in range(fp) for d in range(1,fp)}
actual=Counter();total=F(0);support_sets=set()
for row in finite['global_law']:
 O=affine_orbit(row['representative']);w=F(row['orbit_probability'])
 assert len(O)==row['orbit_size'] and w>0 and not support_sets.intersection(O)
 support_sets.update(O);total+=w
 for S in O:
  assert not any(all((x+j*d)%fp in S for j in range(4)) for x in S for d in range(1,fp))
  for r in range(5):
   for T in combinations(S,r):actual[T]+=w/len(O)
assert total==1
expected4={}
for row in finite['fourth_moments']:
 O=affine_orbit(row['representative'])
 assert len(O)==row['orbit_size']
 assert F(row['moment'])==F(math.comb(fk,4),math.comb(fp,4))*(1+F(row['trade_average']))
 for T in O:
  assert T not in expected4
  expected4[T]=F(row['moment'])
for r in range(5):
 for T in combinations(range(fp),r):
  expected=expected4[T] if r==4 else F(math.comb(fk,r),math.comb(fp,r))
  assert actual[T]==expected
  counts['independent_finite_global_moment_checks']+=1
assert F(120*fk,fp*fp)>=F(fk,fp)**2
counts['independent_AP_free_support_sets']=len(support_sets)
# A single signed cube trade is harmonic at level four.
n=12; root=tuple(range(4)); ys=tuple(range(4,8)); t=Counter()
for bits in product([0,1],repeat=4):
 S=frozenset(ys[i] if bits[i] else root[i] for i in range(4))
 t[S]=-1 if sum(bits)%2==0 else 1
sets={j:list(combinations(range(n),j)) for j in range(3,7)}
for T in sets[3]:
 assert sum(t[frozenset(T+(x,))] for x in range(n) if x not in T)==0
 counts['exact_triple_balances']+=1
lift=lambda S:sum(t[frozenset(T)] for T in combinations(S,4))
for r in (4,5):
 for T in sets[r]:
  assert sum(lift(T+(x,)) for x in range(n) if x not in T)==(n-r-4)*lift(T)
  counts['exact_up_down_identities']+=1
for k in (4,5,6):
 rho=lambda j:F(math.prod(k-i for i in range(j)),math.prod(n-i for i in range(j)))
 alpha={4:F(1),5:F(n-4,n-8),6:F((n-4)*(n-5),(n-8)*(n-9))}
 def moment(S):
  r=len(S)
  return rho(r)*(1+alpha[r]*lift(S))
 for r in (4,5):
  for T in sets[r]:
   assert sum(moment(T+(x,)) for x in range(n) if x not in T)==(k-r)*moment(T)
   counts['exact_canonical_cardinality_identities']+=1
# Degree-five/six homogeneous freedom: harmonic five-trade and its lift.
z=Counter()
for bits in product([0,1],repeat=5):
 S=frozenset(i+5 if bits[i] else i for i in range(5))
 z[S]=(-1)**sum(bits)
for T in sets[4]:
 assert sum(z[frozenset(T+(x,))] for x in range(n) if x not in T)==0
for T in sets[5]:
 up=lambda S:sum(z[frozenset(R)] for R in combinations(S,5))
 assert sum(up(T+(x,)) for x in range(n) if x not in T)==(n-10)*z[frozenset(T)]
 counts['exact_degree_five_harmonic_lift_identities']+=1
# Global reconstruction endpoint from nonnegative top moments.
nend,kend=9,4
support=[S for S in combinations(range(nend),kend) if not (S[1]-S[0]==S[2]-S[1]==S[3]-S[2])]
weights={frozenset(S):1+sum(S) for S in support};den=sum(weights.values())
def moment_end(T):
 return F(sum(w for S,w in weights.items() if set(T)<=S),den)
for r in range(kend+1):
 for T in combinations(range(nend),r):
  assert sum(moment_end(S) for S in combinations(range(nend),kend) if set(T)<=set(S))==moment_end(T)
  counts['exact_global_reconstruction_checks']+=1
z=[i-4 for i in range(nend)]
tau=max(F(sum(z[i] for i in S)**2,nend*nend) for S in support)
for S in combinations(range(nend),kend):
 lhs=tau*moment_end(S)-sum(F(z[i]*z[j],nend*nend)*moment_end(set(S)|{i,j}) for i in range(nend) for j in range(nend))
 rhs=(tau-F(sum(z[i] for i in S)**2,nend*nend))*moment_end(S)
 assert lhs==rhs and lhs>=0
 counts['exact_top_moment_cap_support_checks']+=1

# Universal polynomial certificates on every AP-free subset of small groups.
for p in (7,11,13):
 edge_masks={sum(1<<x for x in {(s+j*d)%p for j in range(4)}) for s in range(p) for d in range(1,p)}
 for mask in range(1<<p):
  if any(mask&e==e for e in edge_masks):continue
  B=[(mask>>i)&1 for i in range(p)];k=sum(B)
  H=[sum(math.prod(B[(v+j*d)%p] for j in (1,2,3)) for d in range(1,p)) for v in range(p)]
  assert all(B[v]*H[v]==0 for v in range(p))
  for v in range(p):
   for c in (F(1,2),F(3,2)):
    lhs=H[v]**2-2*c*H[v]+c*c*(1-B[v])
    rhs=(H[v]-c*(1-B[v]))**2-2*c*B[v]*H[v]
    assert lhs==rhs and lhs>=0
    counts['exact_degree_six_certificate_checks']+=1
  left=(p-k)*sum(h*h for h in H)-sum(H)**2
  right=sum(((1-B[i])*H[j]-(1-B[j])*H[i])**2 for i in range(p) for j in range(i+1,p))
  assert left==right and left>=0
  counts['exact_degree_eight_global_identity_checks']+=1
# Relative completion/Fourier inequality, including proper windows and factors.
import cmath
for p in (11,13):
 for nwin in (p//2,p):
  omega=list(range(nwin)); edges={frozenset((x+j*d)%p for j in range(4)) for x in range(p) for d in range(1,p)}
  for mask in range(1,min(1<<nwin,256)):
   A={i for i in omega if mask>>i&1}
   if any(e<=A for e in edges):continue
   a=F(len(A),nwin)
   h={x:F(sum(all((x+j*d)%p in A for j in (1,2,3)) for d in range(1,p)),p) for x in omega}
   T=sum(h.values())/nwin;V=sum((h[x]-T)**2 for x in omega)/nwin
   for factor in ('trivial','quarter'):
    labels={x:0 if factor=='trivial' else 4*x//p for x in omega}
    g={x:F(sum(y in A for y in omega if labels[y]==labels[x]),sum(labels[y]==labels[x] for y in omega)) for x in omega}
    u={x:F(x in A)-g[x] for x in omega}
    v=sum((g[x]-a)**2 for x in omega)/nwin
    rho=0.;mass=0.;pairing=0j
    for xi in range(1,p):
     cu=sum(float(u[x])*cmath.exp(-2j*math.pi*xi*x/p) for x in omega)/nwin
     hh=sum(float(h[x])*cmath.exp(-2j*math.pi*xi*x/p) for x in omega)/p
     rho=max(rho,abs(cu));mass+=abs(hh);pairing+=cu*hh.conjugate()
    direct=sum(u[x]*h[x] for x in omega)/nwin
    assert abs(pairing-complex(float(direct)))<1e-10
    assert rho*mass+1e-10>=max(0.,float(a*T)-math.sqrt(float(v*V)))
    counts['relative_completion_Fourier_checks']+=1

# Analytic bounds for the actual averaged construction, not a sampled proxy.
def P(n):return F(96,n-4)+F(192*n,(n-4)*(n-5)*(n-6))
assert P(400)<F(1,4)
assert 200*P(200)<100
assert F((200-4)*(200-5),(200-8)*(200-9))<F(21,20)
alpha5=F(396,392)
fifth_ratio=1+alpha5*(-2+3*P(400))
assert fifth_ratio<-F(1,4)
# Exactly verify a target-scale scalar instance; trial division certifies p.
p=2147483647
assert all(p%d for d in range(2,math.isqrt(p)+1))
n=(p-1)//4;k=n//43;a=F(k,n);m=(n-1)//3
rho=lambda j:F(math.prod(k-i for i in range(j)),math.prod(n-i for i in range(j)))
assert (n-k)*(n-k-1)>=400*(k-2)*(k-3) and n-k>=32*(k-3)
required=F(m*m)*rho(3)**2/(1-a)
canonical_upper=F(m*m)*rho(6)*(1+F(1600,n))+9*m*a**3
assert canonical_upper<required
assert m*a**4>=36 and n*a>12800
assert math.log(n/p)+math.sqrt(math.log(p))>0 and 1<=math.sqrt(math.log(p))
assert float(a)>=0.5/(2*math.log(n))
assert (Path(__file__).resolve().parents[1] / "results" / "select_positive_moments_verification_20261012.json").read_bytes()==(Path(__file__).resolve().parents[2] / "history/degree-six-20261012/select_positive_moments_verification_20261012.json").read_bytes()
results={'status':'passed; canonical extension refuted; arbitrary degree-six extension and SELECT unresolved','counts':dict(counts),'fifth_moment_ratio_upper_at_n400':str(fifth_ratio),'scalar_degree_six_witness':{'p':p,'n':n,'endpoint_star_size':m,'window':'{0,...,n-1}', 'k':k,'density':float(a),'epsilon_relative_to_log_p':float(a)*math.log(p),'required_completion_second_moment':float(required),'canonical_second_moment_upper':float(canonical_upper),'positive_gap_lower':float(required-canonical_upper),'note':'exact rational bounds at a certified prime; no enumeration of this large group'},'prior_degree_four_verifier':'rerun passed; output identical to preserved checkpoint','scope':'Combinatorial and polynomial identities use exact integers/rationals. Relative Fourier checks and window eligibility use tolerance 1e-10; decimal moment outputs are display only.'}
(Path(__file__).resolve().parents[1] / "results" / 'DEGREE_SIX_VERIFICATION_20261012.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
