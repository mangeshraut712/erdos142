"""Finite normalization diagnostics. No proof of SELECT."""
import cmath, itertools, json, math
from fractions import Fraction

def ft(v):
    p=len(v)
    return [sum(v[x]*cmath.exp(-2j*math.pi*k*x/p) for x in range(p))/p for k in range(p)]
def lam(vs):
    p=len(vs[0]); return sum(math.prod(vs[j][(x+j*d)%p] for j in range(4)) for x in range(p) for d in range(p))/p**2
checks=0; groups=0; moments=0; signs=0
for p in (5,7):
  for mask in range(1<<p):
    B=[Fraction((mask>>x)&1) for x in range(p)]; a=sum(B)/p
    for labels in ([0]*p,[x%2 for x in range(p)],[4*x//p for x in range(p)]):
      cells={k:[x for x in range(p) if labels[x]==k] for k in set(labels)}
      g=[sum(B[y] for y in cells[labels[x]])/len(cells[labels[x]]) for x in range(p)]
      u=[B[x]-g[x] for x in range(p)]; h=[g[x]-a for x in range(p)]
      v=sum(z*z for z in h)/p; b=sum(z*z for z in u)/p
      assert b==a*(1-a)-v
      for cell in cells.values():
        gg=g[cell[0]]
        for k in (2,3,4):
          actual=sum(u[x]**k for x in cell)/len(cell)
          target=gg*(1-gg)**k+(1-gg)*(-gg)**k
          assert actual==target
          moments+=1
      Lg=lam([g]*4)
      assert abs(float(Lg-a**4))<=4*float(a)*float(v)**1.5+float(v)**2+1e-12
      Rs=[Fraction(0) for j in range(5)]
      for bits in itertools.product((0,1),repeat=4):
        Rs[sum(bits)]+=lam([u if bits[j] else g for j in range(4)])
      assert sum(Rs)==lam([B]*4)
      assert Rs[0]==Lg
      rho=max(abs(z) for z in ft(u)[1:])
      af=float(a); vf=float(v); bf=float(b)
      bounds=[0,12*af*rho*vf+4*math.sqrt(bf)*vf**1.5,
              12*af*rho*math.sqrt(bf*vf)+6*bf*vf,
              4*af*rho*bf+4*math.sqrt(vf)*bf**1.5,bf*bf]
      for j in range(1,5):
        assert abs(float(Rs[j]))<=bounds[j]+1e-10
      checks+=1; groups+=16
      if v<=Fraction(1,4)*a**Fraction(9,4) if a else True:
        assert float(Lg)+1e-10>=7/16*float(a)**4
        signs+=1
print(json.dumps({'status':'all finite algebra/moment checks passed; SELECT unproved','fullgroup_B_factor_cases':checks,'expanded_terms':groups,'conditional_moments':moments,'low_energy_mainterm_cases':signs},indent=2))
