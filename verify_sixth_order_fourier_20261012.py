"""Independent exact geometry/global-law checks and numerical Fourier checks."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json, math
import numpy as np
counts=Counter(); finite=[]
for filename in ['degree_six_finite_extension_20261012.json','sixth_order_p29_k6_extension_20261012.json']:
 data=json.loads(Path(filename).read_text());p=data['p'];k=data['k']
 def orbit(S):return {tuple(sorted((b+d*x)%p for x in S)) for b in range(p) for d in range(1,p)}
 expected={};classes={}
 for index,row in enumerate(data['fourth_moments']):
  O=orbit(row['representative']);assert len(O)==row['orbit_size']
  for T in O:
   assert T not in expected;expected[T]=F(row['moment']);classes[T]=index
 actual=Counter();support=set();weights=[]
 for row in data['global_law']:
  O=orbit(row['representative']);w=F(row['orbit_probability']);weights.append(w)
  assert len(O)==row['orbit_size'] and w>0 and not support.intersection(O)
  support.update(O)
  for S in O:
   assert not any(all((x+j*d)%p in S for j in range(4)) for x in S for d in range(1,p))
   for r in range(5):
    for T in combinations(S,r):actual[T]+=w/len(O)
 assert sum(weights)==1
 # Full column rank modulo a prime certifies full rank over the rationals.
 columns=[Counter(classes[T] for T in combinations(row['representative'],4)) for row in data['global_law']]
 matrix=[[col[i] for col in columns] for i in range(len(data['fourth_moments']))]
 rank=0;mod=65537
 for j in range(len(columns)):
  pivot=next((i for i in range(rank,len(matrix)) if matrix[i][j]%mod),None)
  assert pivot is not None
  matrix[rank],matrix[pivot]=matrix[pivot],matrix[rank]
  inv=pow(matrix[rank][j],-1,mod);matrix[rank]=[x*inv%mod for x in matrix[rank]]
  for i in range(rank+1,len(matrix)):
   val=matrix[i][j];matrix[i]=[(x-val*y)%mod for x,y in zip(matrix[i],matrix[rank])]
  rank+=1
 assert rank==len(data['fourth_moments'])-1
 counts['independent_exact_support_rank_certificates']+=1
 for r in range(5):
  for T in combinations(range(p),r):
   assert actual[T]==(expected[T] if r==4 else F(math.comb(k,r),math.comb(p,r)))
   counts['exact_global_moments']+=1
 # Verify universal completion inequalities on orbit representatives exactly.
 for row in data['global_law']:
  S=set(row['representative']);H=[sum(all((v+j*d)%p in S for j in (1,2,3)) for d in range(1,p)) for v in range(p)]
  for r in (2,3,4):
   assert sum(x**r for x in H)*(p-k)**(r-1)>=sum(H)**r
   counts['exact_finite_law_higher_moment_checks']+=1
 finite.append({'p':p,'k':k,'support_sets':len(support),'positive_orbit_weights':len(weights),'minimum_orbit_weight':str(min(weights)),'minimum_set_probability':str(min(F(row['orbit_probability'])/row['orbit_size'] for row in data['global_law'])),'linear_constraint_rank':len(weights),'affine_solution_dimension':data.get('AP_free_k_set_orbits',data.get('AP_free_five_set_orbits'))-len(weights),'note':'rank follows from exact independent support columns plus the single zero AP row; positivity only on the listed support'})
print('Independent finite global certificates passed.',flush=True)
for p in (11,13,17,23,29,41,101):
 R={i*pow(j,-1,p)%p for i in (1,2,3) for j in (1,2,3)}
 assert len(R)==7
 for d in range(1,p):
  T={j*d%p for j in (1,2,3)};hist=Counter()
  for e in range(1,p):
   U={j*e%p for j in (1,2,3)};r=len(T&U);hist[r]+=1
   assert r==(3 if d==e else 1 if e*pow(d,-1,p)%p in R else 0)
   counts['exact_intersection_pairs']+=1
  assert hist==Counter({0:p-8,1:6,3:1})
 # The incidence Gram is exactly a multiplicative ratio graph plus 3I.
 I=np.array([[int(x*pow(d,-1,p)%p in (1,2,3)) for d in range(1,p)] for x in range(1,p)],dtype=int)
 G=I.T@I
 assert all(G[d-1,e-1]==(3 if d==e else int(e*pow(d,-1,p)%p in R)) for d in range(1,p) for e in range(1,p))
 counts['exact_incidence_Gram_matrices']+=1
rng=np.random.default_rng(142)
for p in (11,13,23,29):
 R={i*pow(j,-1,p)%p for i in (1,2,3) for j in (1,2,3)};m=p-1
 for trial in range(20):
  B=(rng.random(p)<.25).astype(int);a=B.mean();H=np.array([sum(int(B[(v+d)%p]*B[(v+2*d)%p]*B[(v+3*d)%p]) for d in range(1,p)) for v in range(p)])
  h=(H+B)/p;b=np.fft.fft(B)/p
  K=np.array([sum(b[(2*t+r)%p]*b[(-t-2*r)%p]*b[r] for r in range(p)) for t in range(p)])
  assert np.max(np.abs(K-np.fft.fft(h)/p))<1e-11
  triples=H.sum()/p/m;fives={}
  disjoint=0
  for r in R-{1}:
   U={1,2,3,r,2*r%p,3*r%p}
   assert len(U)==5
   fives[r]=sum(math.prod(int(B[(v+d*j)%p]) for j in U) for v in range(p) for d in range(1,p))/p/m
  for v in range(p):
   active=[d for d in range(1,p) if all(B[(v+j*d)%p] for j in (1,2,3))]
   disjoint+=sum(e*pow(d,-1,p)%p not in R for d in active for e in active)
  assert abs(np.mean(H**2)-(m*triples+m*sum(fives.values())+disjoint/p))<1e-9
  lam=np.mean(B*h)
  assert abs(np.mean(H**2)-(p*p*np.sum(abs(K)**2)-2*p*lam+a))<1e-9
  counts['numerical_Fourier_and_exact_count_expansions']+=1
  if not np.any(B*H):
   assert fives[2]==0 and fives[pow(2,-1,p)]==0
   for r in (2,3,4):
    assert int(sum(int(x)**r for x in H))*(p-int(B.sum()))**(r-1)>=int(H.sum())**r
   counts['AP_free_higher_moment_examples']+=1
# Polynomial certificates, with Boolean y and H*y=H.
for y in (0,1):
 for H in range(12):
  if not y and H:continue
  for t in (F(0),F(1,3),F(5,2)):
   assert H**3-3*t*t*H+2*t**3*y==(H-t*y)**2*(H+2*t*y)
   assert H**4-4*t**3*H+3*t**4*y==(H*H-t*t*y)**2+2*t*t*(H-t*y)**2
   counts['exact_higher_moment_polynomial_identities']+=2
# Quadratic weighted obstruction: test both the resonant expansion and Fourier bound.
from itertools import product
modes=(0,1,-1,3,-3)
assert {ell for ell in product(modes,repeat=3) if ell[0]+4*ell[1]+9*ell[2]==0}=={(0,0,0),(3,-3,1),(-3,3,-1)}
counts['exact_quadratic_resonance_classifications']+=1
toy=[]
for p in (101,1009):
 x=np.arange(p,dtype=np.int64);phase=2*np.pi*(x*x%p)/p;beta=.25
 Fv=1+2*beta*np.cos(phase)+2*beta*np.cos(3*phase);M=Fv.mean();a=.001
 f=a*Fv/M
 h=np.array([np.mean(f[(v+x)%p]*f[(v+2*x)%p]*f[(v+3*x)%p]) for v in range(p)])
 approx=(a/M)**3*(1+2*beta**3*np.cos(phase))
 assert np.max(abs(h-approx))<=8*(a/M)**3/math.sqrt(p)+1e-20
 rho=max(abs(np.fft.fft(f)[1:]/p));assert rho<=a/M/math.sqrt(p)+1e-15
 toy.append({'p':p,'density':float(f.mean()),'sixth_energy_over_a6':float(np.mean(h*h)/a**6),'nonzero_Fourier_max':float(rho),'scope':'weighted non-AP-free diagnostic; asymptotic claim proved symbolically'})
 counts['quadratic_weighted_diagnostics']+=1
result={'status':'D: NEW RIGOROUS PARTIAL THEOREM; SELECT and target unresolved','counts':dict(counts),'finite_global_laws':finite,'quadratic_weighted_diagnostics':toy,'scope':'Exact integer/rational checks for combinatorics and global laws; Fourier comparisons numerical at tolerance 1e-9 or tighter. No finite check proves an asymptotic assertion.'}
Path('SIXTH_ORDER_VERIFICATION_20261012.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
