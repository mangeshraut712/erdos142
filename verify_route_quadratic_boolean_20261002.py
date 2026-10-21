"""Finite diagnostics only for ROUTE_QUADRATIC_BOOLEAN_20261002.md."""
import cmath, math, json
from fractions import Fraction

def ft(v):
    p=len(v)
    return [sum(v[x]*cmath.exp(-2j*math.pi*k*x/p) for x in range(p))/p for k in range(p)]
def apfree(v):
    p=len(v)
    return not any(all(v[(x+j*d)%p] for j in range(4)) for x in range(p) for d in range(1,p))
count=0; deletion=0; boolean=0; margin=0
for p in (5,7,11):
    for mask in range(1<<p):
        g=[(mask>>x)&1 for x in range(p)]
        c=ft(g); beta=sum(g)/p; K=sum(abs(z) for z in c)
        B=[g[x*x%p] for x in range(p)]
        Z=sum(abs(c[t])**2*abs(c[3*t%p])**2 for t in range(p))
        L=sum(all(B[(x+j*d)%p] for j in range(4)) for x in range(p) for d in range(p))/p**2
        assert abs(L-Z)<=K**4/math.sqrt(p)+1e-10
        for i in range(4):
            for u in range(1,p):
                val=sum(all(B[(u+(j-i)*d)%p] for j in range(4) if j!=i) for d in range(p))/p
                assert val<=beta**2+K**3/math.sqrt(p)+1e-10
        count+=1
        if p<=7 and sum(B):
            support=[x for x in range(p) if B[x]]
            for amask in range(1<<len(support)):
                A=[0]*p
                for i,x in enumerate(support): A[x]=(amask>>i)&1
                if apfree(A):
                    holes=sum(B[x] and not A[x] for x in range(p))/p
                    assert Z-K**4/math.sqrt(p)-5/p<=4*holes*(beta**2+K**3/math.sqrt(p))+1e-10
                    deletion+=1
        if not apfree(g): continue
        a=Fraction(sum(g),p)
        avg_neg=0.0; avg_margin=0.0
        for d in range(1,p):
            C=[g[x]*g[(x+d)%p] for x in range(p)]
            theta=Fraction(sum(C),p)
            Cft=ft(C)
            cor=sum(C[x]*C[(x+2*d)%p] for x in range(p))
            assert cor==0
            spec=sum(abs(Cft[k])**2*math.cos(4*math.pi*k*d/p) for k in range(p))
            assert abs(spec)<1e-10
            neg=sum(abs(Cft[k])**2 for k in range(1,p) if math.cos(4*math.pi*k*d/p)<0)
            assert neg+1e-10>=float(theta**2)
            if theta:
                z=float(theta)/2
                negmargin=sum(abs(Cft[k])**2 for k in range(1,p) if math.cos(4*math.pi*k*d/p)<=-z+1e-12)
                assert negmargin+1e-10>=float(theta**2)/(2-float(theta))
                margin+=1
                avg_margin+=negmargin/p
            avg_neg+=neg/p
        assert avg_neg+1e-10>=float(a**4-a*a/p)
        assert avg_margin+1e-10>=float(a**4-a*a/p)/2
        sharp=(a*a-a/p)**2/Fraction(p-1,p)
        assert avg_neg+1e-10>=float(sharp)
        assert avg_margin+1e-10>=float(sharp)/2
        boolean+=1
p=13
flat=[int(x in (0,1,3,9)) for x in range(p)]
assert apfree(flat)
assert all(abs(abs(z)**2-3/169)<1e-10 for z in ft(flat)[1:])
for d in range(1,p):
    C=[flat[x]*flat[(x+d)%p] for x in range(p)]
    assert sum(C)==1
    assert all(abs(abs(z)**2-1/169)<1e-10 for z in ft(C))
print(json.dumps({'status':'finite diagnostics passed; symbolic proofs in note; no asymptotic target proved', 'quadratic_host_subsets':count, 'AP_free_host_subsets_checked':deletion,'Boolean_AP_free_subsets':boolean,'nonempty_margin_fibers':margin},indent=2))
