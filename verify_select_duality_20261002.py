"""Exact degree-two pseudo-moment certificate; does not construct an AP-free law."""
from fractions import Fraction as F
import json,math
checks=0
for p in (5,7,11,13,17,43,101):
 for k in range(1,p//3+1):
  a=F(k,p);rho=F(k*(k-1),p*(p-1));lam=a-rho
  assert lam>0
  assert a+(p-1)*rho-p*a*a==0 # covariance uniform eigenvalue
  assert a+(p-1)*rho==k*a # fixed-size row sum
  assert 4*a<=3
  assert a+3*rho<=3*a
  assert 4*rho<=3*a
  assert 3*a-3*rho<=3*(1-a)
  assert 4*a-4*rho<=3*(1-a)
  assert lam/p==a*(1-a)/(p-1)
  checks+=1
samples=[]
for p in (101,1009,10007,100003,1000003):
 k=max(1,int(p/math.log(p)));a=k/p
 ratio=(a*(1-a)/(p-1))/(a**2.5*math.log(2/a))
 samples.append({'p':p,'k':k,'a':a,'pseudo_Fourier_SELECT_ratio':ratio})
print(json.dumps({'status':'degree-two certificate checks passed','exact_parameter_cases':checks,'asymptotic_samples_only':samples},indent=2))
