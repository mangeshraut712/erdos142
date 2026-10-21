"""Exact truncated Boolean degree-four moment certificate; not an AP-free law."""
from fractions import Fraction as F
from itertools import combinations
import json

def apedges(p,om):
 U=set(om)
 return {frozenset((x+j*d)%p for j in range(4)) for x in om for d in range(1,p) if all((x+j*d)%p in U for j in range(4))}
def centered(S,a):
 return {frozenset(T):(-a)**(len(S)-len(T)) for r in range(len(S)+1) for T in combinations(S,r)}
counts={'parameter_cases':0,'Gram_entries':0,'pair_rows':0}
for p,om in ((5,list(range(5))),(7,list(range(7))),(11,list(range(11))),(13,list(range(4))),(19,list(range(6)))):
 edges=apedges(p,om);basis=[frozenset()]+[frozenset((x,)) for x in om]+[frozenset(t) for t in combinations(om,2)]
 pairs=basis[1+len(om):]
 degs=[sum(S.isdisjoint(T) and S|T in edges for T in pairs) for S in pairs]
 assert max(degs,default=0)<=6
 counts['pair_rows']+=len(pairs)
 for a in (F(1,20),F(1,10),F(1,5),F(2,7)):
  b=a*(1-a);assert b*b>=6*a**4
  pol=[centered(tuple(S),a) for S in basis]
  def L(S):return F(0) if len(S)==4 and S in edges else a**len(S)
  for i,S in enumerate(basis):
   for j,T in enumerate(basis):
    value=sum(c*d*L(R|Q) for R,c in pol[i].items() for Q,d in pol[j].items())
    expected=(F(1) if len(S)==0 else b**len(S)) if S==T else F(0)
    if len(S)==len(T)==2 and S.isdisjoint(T) and S|T in edges:expected-=a**4
    assert value==expected
    counts['Gram_entries']+=1
  assert sum(L(frozenset((x,y)))-a*a for x in om for y in om)==len(om)*b
  counts['parameter_cases']+=1
# Universal constant6 is sharp for this construction: Z7 pairgraph regular degree6.
p=7;om=list(range(p));edges=apedges(p,om);pairs=[frozenset(t) for t in combinations(om,2)]
assert all(sum(S.isdisjoint(T) and S|T in edges for T in pairs)==6 for S in pairs)
a=F(1,3);b=a*(1-a);assert b*b-6*a**4<0
print(json.dumps({'status':'quartic relaxation identities and PSD certificate checks passed','checks':counts,'PSD_sufficient_condition':'a <= 1/(1+sqrt(6))','exact_cardinality_enforced':False,'residual_mean_zero_as_polynomial_identity':False,'Z7_negative_direction_at_a_one_third':str(b*b-6*a**4)},indent=2))
