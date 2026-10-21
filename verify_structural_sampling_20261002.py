from itertools import product, combinations
from fractions import Fraction as F
import cmath, math, json

def four(v):
 p=len(v);return [sum(v[x]*cmath.exp(-2j*math.pi*k*x/p) for x in range(p))/p for k in range(p)]
conv_checks=0
for p in (5,7,11):
 for B in product((0,1),repeat=p):
  bh=four(B);W=[abs(z)**2 for z in bh]
  sums=[0.0]*p
  for d in range(p):
   C=[B[x]*B[(x+d)%p] for x in range(p)]
   for k,z in enumerate(four(C)):sums[k]+=abs(z)**2/p
  for k in range(p):assert abs(sums[k]-sum(W[t]*W[(k-t)%p] for t in range(p)))<1e-10
  conv_checks+=1
sampling_checks=0
for nums in ((1,1,1),(1,2,3),(0,2,3)):
 den=sum(nums);q=[F(x,den) for x in nums];z=[F(1,10),F(1,3),F(2,5)]
 for s in range(1,6):
  ET=ET2=F(0)
  for seq in product(range(3),repeat=s):
   prob=math.prod(q[x] for x in seq);T=sum(z[x] for x in set(seq))
   ET+=prob*T;ET2+=prob*T*T
  expected=sum(z[x]*(1-(1-q[x])**s) for x in range(3))
  assert ET==expected
  assert ET2-ET*ET<=sum(z[x]**2*(1-(1-q[x])**s) for x in range(3))
  sampling_checks+=1
kap=2*math.sqrt(2)/math.pi
rotation_checks=0
for p in (5,7):
 for mask in range(1,2**p):
  om=[x for x in range(p) if mask>>x&1];n=len(om)
  B=[int(x%3==0) for x in om];a=sum(B)/n;u=[b-a for b in B]
  for k in range(1,p):
   e=[cmath.exp(2j*math.pi*k*x/p) for x in om]
   m=sum(e)/n;c=sum(u[i]*e[i].conjugate() for i in range(n))/n
   bounds=sorted(set([0.0,1.0]+[((k*x/p-j/4)%1) for x in om for j in range(4)]))
   avg=[0j]*n;cor2=norm2=0.0
   for lo,hi in zip(bounds,bounds[1:]):
    if hi-lo<1e-14:continue
    th=(lo+hi)/2
    const=[cmath.exp(2j*math.pi*((math.floor(((k*x/p-th)%1)*4)+.5)/4)) for x in om]
    integ=(cmath.exp(2j*math.pi*hi)-cmath.exp(2j*math.pi*lo))/(2j*math.pi)
    for i in range(n):avg[i]+=const[i]*integ
    cm=sum(const)/n
    cor=sum(u[i]*const[i].conjugate() for i in range(n))/n
    cor2+=(hi-lo)*abs(cor)**2
    norm2+=(hi-lo)*(1-abs(cm)**2)
   assert max(abs(avg[i]-kap*e[i]) for i in range(n))<1e-10
   assert cor2+1e-10>=kap**2*abs(c)**2
   assert norm2<=kap**2*(1-abs(m)**2)+1-kap**2+1e-10
   rotation_checks+=1
residual_checks=0
for p in (5,7):
 for mask in range(1,2**p):
  om=[x for x in range(p) if mask>>x&1];n=len(om)
  for typ in (0,2,3):
   labels=[0 if typ==0 else x%typ for x in om]
   B=[int(x%3==0) for x in om]
   means={lab:sum(B[i] for i in range(n) if labels[i]==lab)/labels.count(lab) for lab in set(labels)}
   u=[B[i]-means[labels[i]] for i in range(n)]
   for k in range(1,p):
    c=sum(u[i]*cmath.exp(-2j*math.pi*k*x/p) for i,x in enumerate(om))/n
    bounds=sorted(set([0.0,1.0]+[((k*x/p-j/4)%1) for x in om for j in range(4)]))
    avgenergy=0
    for lo,hi in zip(bounds,bounds[1:]):
     if hi-lo<1e-14:continue
     th=(lo+hi)/2;cells={}
     for i,x in enumerate(om):
      j=math.floor(((k*x/p-th)%1)*4)
      cells.setdefault((labels[i],j),[]).append(i)
     energy=sum(sum(u[i] for i in cell)**2/(n*len(cell)) for cell in cells.values())
     avgenergy+=(hi-lo)*energy
    assert avgenergy+1e-10>=kap**2*abs(c)**2
    residual_checks+=1
multi_checks=0
for p in (5,7):
 for mask in sorted(set([1,3,7,2**p-1,(2**p-1)//3,(2**p-1)//2])):
  om=[x for x in range(p) if mask>>x&1];n=len(om)
  for typ in (0,2,3):
   labels=[0 if typ==0 else x%typ for x in om]
   B=[int(x%3==0) for x in om]
   means={lab:sum(B[i] for i in range(n) if labels[i]==lab)/labels.count(lab) for lab in set(labels)}
   u=[B[i]-means[labels[i]] for i in range(n)]
   es=[[cmath.exp(2j*math.pi*k*x/p) for x in om] for k in (1,2)]
   ms=[sum(e)/n for e in es]
   cs=[sum(u[i]*e[i].conjugate() for i in range(n))/n for e in es]
   G=[[sum((es[r][i]-ms[r]).conjugate()*(es[t][i]-ms[t]) for i in range(n))/n for t in range(2)] for r in range(2)]
   M=[[kap**2*G[r][t]+int(r==t)*(1-kap**2) for t in range(2)] for r in range(2)]
   det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
   inv=[[M[1][1]/det,-M[0][1]/det],[-M[1][0]/det,M[0][0]/det]]
   lower=kap**2*sum(cs[r].conjugate()*inv[r][t]*cs[t] for r in range(2) for t in range(2)).real
   opts=[]
   for k in (1,2):
    bounds=sorted(set([0.0,1.0]+[((k*x/p-j/4)%1) for x in om for j in range(4)]))
    opts.append([[math.floor(((k*x/p-(lo+hi)/2)%1)*4) for x in om] for lo,hi in zip(bounds,bounds[1:]) if hi-lo>1e-14])
   maximum=0
   for j1,j2 in product(*opts):
    cells={}
    for i in range(n):cells.setdefault((labels[i],j1[i],j2[i]),[]).append(i)
    gain=sum(sum(u[i] for i in cell)**2/(n*len(cell)) for cell in cells.values())
    maximum=max(maximum,gain)
   assert maximum+1e-10>=lower
   multi_checks+=1
print(json.dumps({'status':'checks passed','convolution_subsets':conv_checks,'exact_sampling_moments':sampling_checks,'relative_rotation_integrals':rotation_checks,'relative_residual_refinement_checks':residual_checks,'simultaneous_regularized_Gram_checks':multi_checks},indent=2))
