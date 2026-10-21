"""Focused checks for cellwise completion overlap and its operator."""
from fractions import Fraction as F
from collections import Counter
from itertools import product
from pathlib import Path
import json,math
import numpy as np
counts=Counter();examples=[]
def completion(B):
 p=len(B)
 return np.array([sum(int(B[(v+d)%p]*B[(v+2*d)%p]*B[(v+3*d)%p]) for d in range(1,p)) for v in range(p)],dtype=int)
def apfree(B):return not np.any(B*completion(B))
def check_cells(p,S,omega):
 B=np.array([int(x in S) for x in range(p)]);H=completion(B);q=[F(int(x),p) for x in H]
 assert not np.any(B*H)
 for factor in ('trivial','quarter','parity'):
  labels={x:0 if factor=='trivial' else 4*x//p if factor=='quarter' else x%2 for x in omega}
  cells=[[x for x in omega if labels[x]==lab] for lab in sorted(set(labels.values()))]
  pairing=F(0);Ssum=F(0);gmap={};umap={}
  for C in cells:
   g=F(sum(int(B[x]) for x in C),len(C));T=sum(q[x] for x in C)/len(C)
   z={x:q[x]-T*(1-int(B[x]))/(1-g) if g!=1 else F(0) for x in C}
   assert sum(z.values())==0
   assert all(B[x]*z[x]==0 for x in C)
   assert sum((int(B[x])-g)*z[x] for x in C)==0
   lhs=sum((q[x]-T)**2 for x in C)/len(C)
   rhs=(g*T*T/(1-g) if g!=1 else 0)+sum(z[x]**2 for x in C)/len(C)
   assert lhs==rhs
   for x in C:
    gmap[x]=g;umap[x]=int(B[x])-g
    pairing+=umap[x]*q[x];Ssum+=g*q[x]
   counts['exact_cell_decompositions']+=1
  assert pairing==-Ssum
  # Relative Parseval: full normalized zero extension versus relative u.
  uz=np.zeros(p);qz=np.zeros(p)
  for x in omega:uz[x]=float(umap[x]);qz[x]=float(q[x])
  cu=np.fft.fft(uz)/len(omega);hq=np.fft.fft(qz)/p
  assert abs(np.vdot(hq,cu)-float(pairing/len(omega)))<1e-11
  counts['relative_Parseval_checks']+=1
 # Exact nonzero-difference derivative matrix, stored before division by p.
 D=np.zeros((p,p),dtype=int)
 for v in range(p):
  for d in range(1,p):
   for j in (1,2,3):
    D[v,(v+j*d)%p]+=math.prod(int(B[(v+i*d)%p]) for i in (1,2,3) if i!=j)
 assert np.array_equal(D@B,3*H)
 assert not np.any(D[np.ix_(list(S),list(S))])
 assert D.sum(axis=0).max()<=3*len(S) and D.sum(axis=1).max()<=3*len(S)
 a=F(len(S),p);TE=F(int(H.sum()),p*p)
 TM=F(sum(int(B[v]*B[(v+2*d)%p]*B[(v+3*d)%p]) for v in range(p) for d in range(1,p)),p*p)
 centered=[F(int(x))-a for x in B]
 lhs=sum(centered[i]*int(D[i,j])*centered[j] for i in range(p) for j in range(p))/(p*p)
 rhs=-2*a*(2*TE+TM)+3*a*a*(a*a-a/p)
 assert lhs==rhs
 counts['exact_derivative_operator_checks']+=1
 b=np.fft.fft(B)/p;h=(H+B)/p;K=np.fft.fft(h)/p
 formula=np.array([sum(b[(2*t+r)%p]*b[(-t-2*r)%p]*b[r] for r in range(p)) for t in range(p)])
 assert np.max(abs(formula-K))<1e-11
 conv=np.array([sum(b[r]*K[(t-r)%p] for r in range(p)) for t in range(p)])
 assert np.max(abs(conv-b/p))<1e-11
 counts['completion_and_Bh_Fourier_checks']+=1
for filename in ('degree_six_finite_extension_20261012.json','sixth_order_p29_k6_extension_20261012.json'):
 data=json.loads(Path(filename).read_text());p=data['p']
 for row in data['global_law']:check_cells(p,set(row['representative']),list(range(p)))
 counts['global_law_orbit_representatives']+=len(data['global_law'])
# Proper-window finite obstructions to universally positive endpoint completion.
cube={sum(bits[j]*3**j for j in range(3)) for bits in product((0,1),repeat=3)}
prodset={x+16*y for x in (0,1,4) for y in (0,1,4)}
for name,p,n,S in [('three_point',101,25,{0,1,3}),('ternary_cube',59,14,cube),('digit_product',277,69,prodset)]:
 B=np.array([int(x in S) for x in range(p)]);H=completion(B)
 assert not np.any(H)
 assert n-1<p/3 and n>=p*math.exp(-math.sqrt(math.log(p)))
 a=len(S)/n;assert .5/(2*math.log(n))<=a<=.8
 check_cells(p,S,list(range(n)))
 examples.append({'name':name,'p':p,'window_size':n,'set':sorted(S),'relative_density':a,'endpoint_completion_identically_zero':True,'geometric_and_density_conditions_epsilon_half':True,'scope':'finite test; unknown asymptotic p0 not tested; not a SELECT counterexample'})
# Other requested test families, with hypotheses explicitly reported.
p=101;x=np.arange(p);phase=np.exp(2j*np.pi*(x*x%p)/p)
for name,B in [('interval',(x<12).astype(int)),('quadratic_Boolean_host',((x*x%p)<13).astype(int))]:
 H=completion(B);b=np.fft.fft(B)/p
 examples.append({'name':name,'p':p,'size':int(B.sum()),'AP_free':bool(not np.any(B*H)),'nonzero_AP_count':int(np.dot(B,H)),'completion_mean':float(H.mean()/p),'maximum_linear_Fourier':float(max(abs(b[1:]))),'scope':'full-group diagnostic, not a proper H-window counterexample'})
assert np.max(abs(abs(np.fft.fft(phase)/p)-1/math.sqrt(p)))<1e-11
examples.append({'name':'genuine_quadratic_phase','p':p,'Boolean':False,'all_Fourier_magnitudes':1/math.sqrt(p),'scope':'fails Boolean premise'})
# Exact telescoping on B versus its factor projection, including diagonal.
for row in json.loads(Path('sixth_order_p29_k6_extension_20261012.json').read_text())['global_law'][:8]:
 p=29;S=set(row['representative']);B=[F(int(i in S)) for i in range(p)]
 cells=[[i for i in range(p) if 4*i//p==j] for j in range(4)]
 g=[next(sum(B[x] for x in C)/len(C) for C in cells if i in C) for i in range(p)]
 u=[B[i]-g[i] for i in range(p)]
 def lam(fs):return sum(math.prod(fs[j][(v+j*d)%p] for j in range(4)) for v in range(p) for d in range(p))/(p*p)
 terms=[]
 for j in range(4):terms.append(lam([B if i<j else u if i==j else g for i in range(4)]))
 assert lam([B]*4)-lam([g]*4)==sum(terms)
 assert lam([B]*4)==F(len(S),p*p)
 counts['exact_direct_counting_telescopes']+=1
result={'principal_status':'D: NEW RIGOROUS PARTIAL THEOREM','executed_date':'2026-10-13','counts':dict(counts),'example_tests':examples,'scope':'Fraction and integer tests are exact; Fourier tests use 1e-11 tolerance. No asymptotic concentration premise or degree-six target extension is established.'}
Path('COMPLETION_SPECTRUM_VERIFICATION_20261012.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
