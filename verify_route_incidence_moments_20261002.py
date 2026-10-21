"""Exact finite diagnostics; does not prove an asymptotic theorem."""
from fractions import Fraction as F
import json
from itertools import product

def mm(A,B):
 return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def tr(A): return sum(A[i][i] for i in range(len(A)))
counts={'subsets':0,'ap_free':0,'schur':0}
for p in (5,7,11):
 inv3=pow(3,-1,p)
 for bits in product((0,1),repeat=p):
  A=[i for i,b in enumerate(bits) if b]
  if not A: continue
  J=[[int(y!=z)*bits[(2*y+z)*inv3%p]*bits[(y+2*z)*inv3%p] for z in range(p)] for y in range(p)]
  K=[[J[y][z]+int(y==z)*bits[y] for z in range(p)] for y in range(p)]
  J2=mm(J,J);J3=mm(J2,J);J4=mm(J3,J)
  K2=mm(K,K);K3=mm(K2,K);K4=mm(K3,K)
  deg=sum(J2[y][y] for y in A)
  assert tr(K3)==len(A)+3*deg+tr(J3)
  dj= sum(J[y][z]**2 for y in A for z in A)
  assert tr(K4)==len(A)+4*deg+2*dj+4*sum(J3[y][y] for y in A)+tr(J4)
  counts['subsets']+=1
  if any(J[y][z] for y in A for z in A):continue
  counts['ap_free']+=1
  cols=[(u,v) for u in A for v in A if u!=v]
  R=[[int(y in ((2*u-v)%p,(2*v-u)%p)) for u,v in cols] for y in range(p)]
  G=mm(R,list(map(list,zip(*R)))) if cols else [[0]*p for _ in range(p)]
  assert all(G[y][z]==2*J[y][z] for y in range(p) for z in range(p) if y!=z)
  active=[y for y in A if G[y][y]]
  for y in active:
   assert all(G[y][z]==0 for z in A if y!=z)
  C=[y for y in range(p) if y not in A]
  S=[[F(R[y][j])-sum(F(G[y][x]*R[x][j],G[x][x]) for x in active) for j in range(len(cols))] for y in C]
  gram=mm(S,list(map(list,zip(*S)))) if cols else [[F(0)]*len(C) for _ in C]
  for i,y in enumerate(C):
   for j,z in enumerate(C):
    rhs=G[y][z]-sum(F(G[y][x]*G[x][z],G[x][x]) for x in active)
    assert gram[i][j]==rhs
  counts['schur']+=1
print(json.dumps({'status':'finite exact checks passed','checks':counts},indent=2))
