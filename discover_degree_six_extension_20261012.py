"""Exact affine-orbit global extension for a finite averaged-trade instance.
This is a finite diagnostic, not an asymptotic extension theorem.
"""
from itertools import combinations,permutations,product
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json,math
import numpy as np
from scipy.optimize import linprog
p=23;k=5
mask=lambda S:sum(1<<x for x in S)
def orbit(S):
 return {mask({(b+d*x)%p for x in S}) for b in range(p) for d in range(1,p)}
classes={};orbits=[];reps=[]
for S in combinations(range(p),4):
 key=mask(S)
 if key in classes:continue
 O=orbit(S);idx=len(orbits)
 for x in O:classes[x]=idx
 orbits.append(O);reps.append(S)
ap=orbit((0,1,2,3)); assert len(ap)==p*(p-1)//2
root=(0,1,2,3);patterns=list(product([0,1],repeat=4));sums=Counter();accepted=0
for ys in permutations(range(4,p),4):
 trans=[(mask([ys[i] if b[i] else root[i] for i in range(4)]),-1 if sum(b)%2==0 else 1) for b in patterns]
 if any(s in ap for s,sgn in trans[1:]):continue
 accepted+=1
 for s,sgn in trans:sums[classes[s]]+=sgn
assert accepted>0
rho4=F(math.comb(k,4),math.comb(p,4))
t=[F(len(ap)*sums[i],accepted*len(O)) for i,O in enumerate(orbits)]
m4=[rho4*(1+v) for v in t]
assert all(x>=0 for x in m4)
print('exact trade averaging:',accepted,'choices;',len(orbits),'four-set orbits',flush=True)
seen=set();freereps=[];inc=[];sizes=[]
for S in combinations(range(p),5):
 key=mask(S)
 if key in seen:continue
 O=orbit(S);seen.update(O)
 four=list(combinations(S,4))
 if any(mask(T) in ap for T in four):continue
 c=Counter(classes[mask(T)] for T in four)
 freereps.append(S);sizes.append(len(O));inc.append([c[i] for i in range(len(orbits))])
b=[len(O)*v for O,v in zip(orbits,m4)]
A=np.array(inc,dtype=float).T
sol=linprog(np.zeros(len(inc)),A_eq=A,b_eq=np.array([float(x) for x in b]),bounds=(0,None),method='highs')
assert sol.success,sol.message
support=[j for j,w in enumerate(sol.x) if w>1e-8]
# Independently reconstruct and verify exact rational weights on the LP support.
M=[[F(inc[j][i]) for j in support]+[b[i]] for i in range(len(b))]
r=0;piv=[]
for col in range(len(support)):
 pivot=next((i for i in range(r,len(M)) if M[i][col]),None)
 if pivot is None:continue
 M[r],M[pivot]=M[pivot],M[r];v=M[r][col];M[r]=[x/v for x in M[r]]
 for i in range(len(M)):
  if i!=r and M[i][col]:
   v=M[i][col];M[i]=[x-v*y for x,y in zip(M[i],M[r])]
 piv.append(col);r+=1
assert len(piv)==len(support)
assert all(any(row[:-1]) or row[-1]==0 for row in M)
w=[F(0) for _ in support]
for i,j in enumerate(piv):w[j]=M[i][-1]
assert all(v>=0 for v in w) and sum(w)==1
for i in range(len(b)):
 assert sum(F(inc[j][i])*v for j,v in zip(support,w))==b[i]
# Cardinality down-summing then implies agreement of all lower moments.
for rsmall in range(4):
 expected=F(math.comb(k,rsmall),math.comb(p,rsmall))
 for T in combinations(range(p),rsmall):
  q=sum(m4[classes[mask(S)]] for S in combinations(range(p),4) if set(T)<=set(S))/math.comb(k-rsmall,4-rsmall)
  assert q==expected
print('exact global extension:',len(support),'positive affine-orbit weights',flush=True)
result={'status':'EXACT FINITE GLOBAL EXTENSION VERIFIED','p':p,'k':k,'scope':'p=23 lies below the uniform n>=200 theorem; no asymptotic extension or SELECT counterexample is claimed','admissible_root_trade_choices':accepted,'four_set_orbits':len(orbits),'AP_free_five_set_orbits':len(freereps),'cap':'120a/n exceeds a^2 here, so each supporting set satisfies that cap automatically','fourth_moments':[{'representative':list(S),'orbit_size':len(O),'trade_average':str(tv),'moment':str(mv)} for S,O,tv,mv in zip(reps,orbits,t,m4)],'global_law':[{'representative':list(freereps[j]),'orbit_size':sizes[j],'orbit_probability':str(v)} for j,v in zip(support,w) if v]}
Path('degree_six_finite_extension_20261012.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:value for key,value in result.items() if key not in ('fourth_moments','global_law')},indent=2))
