"""Finite SELECT discovery and a failed first-moment LP certificate. No extrapolation."""
import json,math,itertools,time
import numpy as np
from scipy.optimize import linprog

def edges(p,om):
 idx={x:i for i,x in enumerate(om)};out=set()
 for x in om:
  for d in range(1,p):
   pts={(x+j*d)%p for j in range(4)}
   if pts<=idx.keys():out.add(sum(1<<idx[y] for y in pts))
 return sorted(out)
def partition(p,om,xis,rots):
 labels=[tuple(math.floor(4*((xi*x/p-th)%1)) for xi,th in zip(xis,rots)) for x in om]
 keys=sorted(set(labels));return [np.array([i for i,k in enumerate(labels) if k==key]) for key in keys]
def evaluate(p,om,kind):
 n=len(om);ee=edges(p,om)
 masks=[m for m in range(1,1<<n) if all(m&e!=e for e in ee)]
 B=np.array([[(m>>j)&1 for j in range(n)] for m in masks],dtype=float)
 a=B.mean(axis=1);keep=(a<=.8);B=B[keep];a=a[keep];masks=np.array(masks,dtype=np.int64)[keep]
 E=np.exp(-2j*np.pi*np.outer(om,np.arange(1,p))/p)
 Fs=[('trivial',[],[])]+[(f'quarter_{xi}_{th}',[xi],[th]) for xi in (1,2,3) for th in (0.0,.125)]
 best={};checks=0;eligibility={}
 for name,xis,rots in Fs:
  cs=partition(p,om,xis,rots);g=np.zeros_like(B)
  for cell in cs:g[:,cell]=B[:,cell].mean(axis=1)[:,None]
  V=((g-a[:,None])**2).mean(axis=1);u=B-g
  rho=(np.abs(u@E/n)**2).max(axis=1)
  cert=p*(a*(1-a)-V)/(n*(p-1))
  assert np.all(rho+1e-10>=cert)
  ratios=rho/(a**2.5*np.log(2/a));checks+=len(a)
  for zeta in (.03125,.125,.25):
   admissible=V<zeta*a**2.25-1e-12
   # epsilon=.1 is just a finite recorded density threshold, not a p0 claim.
   if kind=='proper_window':admissible&=a>=.1/(2*math.log(n))
   if not np.any(admissible):continue
   inds=np.flatnonzero(admissible);i=inds[np.argmin(ratios[inds])]
   rec={'ratio':float(ratios[i]),'p':p,'omega':om,'A':[om[j] for j in range(n) if masks[i]>>j&1],
        'factor':name,'new_characters':len(xis),'a':float(a[i]),'energy':float(V[i]),'rho_squared':float(rho[i]),
        'parseval_lower':float(cert[i]),'greedy_intermediate_requires_c_less_than':float(zeta*a[i]**(-.25)/((8/math.pi**2)*math.log(2/a[i]))) if len(xis) else None}
   key=str(zeta)
   if key not in best or rec['ratio']<best[key]['ratio']:best[key]=rec
 if kind=='proper_window':
  eligibility={'epsilon':.1,'window_rank':1,'rank_bound_satisfied':1<=math.floor(math.sqrt(math.log(p))),
               'size_bound_satisfied':n>=p*math.exp(-math.sqrt(math.log(p))),
               'narrow_diameter_satisfied':n-1<p/3,
               'intermediate_factor_family':'trivial and six explicitly listed rank-one quarter partitions',
               'asymptotic_p0':'not known; these are finite diagnostics'}
 return {'kind':kind,'p':p,'n':n,'ap_edges':len(ee),'ap_free_subsets_density_le_point8':len(a),'residual_cases':checks,'minima':best,'eligibility':eligibility}
results=[]
for p in (5,7,11,13,17):results.append(evaluate(p,list(range(p)),'full_group_diagnostic'))
for p in (13,17,19,23,29,31,43):results.append(evaluate(p,list(range(p//3)),'proper_window'))
# First-moment LP: binary replaced by [0,1], exact density, AP sum<=3,
# constrain all real/imag Fourier components by one T.
p=13;a=4/13;om=list(range(p));n=p
Aub=[];bub=[]
for e in edges(p,om):
 row=np.zeros(n+1)
 for j in range(n):row[j]=int(e>>j&1)
 Aub.append(row);bub.append(3.)
for k in range(1,p):
 for wave in (np.cos(2*np.pi*k*np.arange(p)/p),np.sin(2*np.pi*k*np.arange(p)/p)):
  for sign in (-1,1):Aub.append(np.r_[sign*wave/p,-1]);bub.append(0.)
res=linprog(np.r_[np.zeros(p),1.],A_ub=np.array(Aub),b_ub=np.array(bub),A_eq=[np.r_[np.ones(p),0]],b_eq=[p*a],bounds=[(0,1)]*p+[(0,None)],method='highs')
assert res.success and abs(res.fun)<1e-9
# A proper-window residual LP has the same analytic obstruction.
p2=43;om2=list(range(p2//3));n2=len(om2);a2=.5;Au2=[];bu2=[]
for e in edges(p2,om2):
 row=np.zeros(n2+1)
 for j in range(n2):row[j]=int(e>>j&1)
 Au2.append(row);bu2.append(3.)
for k in range(1,p2):
 for wave in (np.cos(2*np.pi*k*np.array(om2)/p2),np.sin(2*np.pi*k*np.array(om2)/p2)):
  for sign in (-1,1):Au2.append(np.r_[sign*wave/n2,-1]);bu2.append(sign*a2*sum(wave)/n2)
r2=linprog(np.r_[np.zeros(n2),1.],A_ub=np.array(Au2),b_ub=np.array(bu2),A_eq=[np.r_[np.ones(n2),0]],b_eq=[n2*a2],bounds=[(0,1)]*n2+[(0,None)],method='highs')
assert r2.success and abs(r2.fun)<1e-9
out={'status':'finite exhaustive checks and LP completed','results':results,'first_moment_LP':{'p':p,'density':a,'optimal_component_bound':float(res.fun),'solver_message':res.message,'analytic_certificate':'constant fractional B=a is feasible and has zero nonzero Fourier coefficients'},'proper_window_LP':{'p':p2,'n':n2,'density':a2,'optimal_residual_component_bound':float(r2.fun),'analytic_certificate':'B=a inside Omega makes u=0 and satisfies every AP sum<=3'}}
print(json.dumps(out,indent=2))
