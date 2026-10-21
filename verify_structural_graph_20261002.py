"""Finite checks of double Fourier, margins and Boolean cocycle. Not target proof."""
import cmath, math, json

def ft(v):
    p=len(v)
    return [sum(v[x]*cmath.exp(-2j*math.pi*k*x/p) for x in range(p))/p for k in range(p)]

def apfree(v):
    p=len(v)
    return not any(all(v[(x+j*d)%p] for j in range(4)) for x in range(p) for d in range(1,p))
checks=0; cocycles=0; af=0
for p in (5,7,11):
    for mask in range(1<<p):
        B=[(mask>>x)&1 for x in range(p)]
        b=ft(B); a=sum(B)/p; W=[abs(z)**2 for z in b]
        C=[[B[x]*B[(x+d)%p] for x in range(p)] for d in range(p)]
        F=[ft(row) for row in C]
        for k in range(p):
            D=ft([F[d][k] for d in range(p)])
            for t in range(p):
                assert abs(D[t]-b[(k-t)%p]*b[t])<1e-10
            R=sum(abs(F[d][k])**2 for d in range(p))/p
            conv=sum(W[t]*W[(k-t)%p] for t in range(p))
            assert abs(R-conv)<1e-10
            if k:
                rho=max(abs(z) for z in b[1:])
                assert R<=(a+a*a)*rho*rho+1e-10
        L=sum(all(B[(x+j*d)%p] for j in range(4)) for x in range(p) for d in range(p))/p**2
        Z=sum(F[d][k]*F[d][k].conjugate()*cmath.exp(4j*math.pi*k*d/p) for d in range(p) for k in range(p))/p
        assert abs(Z-L)<1e-10
        spec=sum(b[(k-t)%p]*b[t]*b[(-k-t)%p].conjugate()*b[(t+2*k)%p].conjugate() for k in range(p) for t in range(p))
        assert abs(spec-L)<1e-10
        if p<=7:
            for d in range(p):
                for e in range(p):
                    for x in range(p):
                        G=B[x]*B[(x+d)%p]*B[(x+d+e)%p]
                        assert C[d][x]*C[e][(x+d)%p]==G==C[(d+e)%p][x]*B[(x+d)%p]
                        cocycles+=1
        checks+=1
        af+=int(apfree(B))
for pg in (5,7,13,101):
    for theta in (1/pg,0.2,0.25):
        if not 1/pg<=theta<=0.25: continue
        DD=2*theta*(1-pg*theta)/(pg*(pg-3))
        CC=(theta-theta*theta+DD)/(pg-1)
        for d in range(1,pg):
            row=[theta*theta]+[CC+DD*math.cos(4*math.pi*k*d/pg) for k in range(1,pg)]
            assert min(row)>=-1e-12
            assert abs(sum(row)-theta)<1e-10
            assert abs(sum(row[k]*math.cos(4*math.pi*k*d/pg) for k in range(pg)))<1e-10
        for k in range(1,pg):
            deg=sum(CC+DD*math.cos(4*math.pi*k*d/pg) for d in range(1,pg))/pg
            assert abs(deg-((pg-1)*CC-DD)/pg)<1e-10
p=13; A={0,1,3,9}; B=[int(x in A) for x in range(p)]
assert apfree(B)
x_d={d:next(x for x in range(p) if B[x]*B[(x+d)%p]) for d in range(1,p)}
assert all(sum(B[x]*B[(x+d)%p] for x in range(p))==1 for d in range(1,p))
k={d:d*d%p for d in range(1,p)}
violations=[]
for d in range(1,p):
    for e in range(1,p):
        if (d+e)%p==0: continue
        T=[x for x in range(p) if B[x]*B[(x+d)%p]*B[(x+d+e)%p]]
        if T and (k[d]+k[e]-k[(d+e)%p])%p:
            violations.append([d,e,T[0],(k[d]+k[e]-k[(d+e)%p])%p])
assert violations
print(json.dumps({'status':'passed finite identities; no structural H proof', 'Boolean_sets':checks,'AP_free_sets':af,'pointwise_cocycles':cocycles, 'saturated_signal_nonadditive_witness':{'p':p,'A':sorted(A),'frequency_rule':'k_d=d^2 mod p','first_triangle':violations[0],'violating_triangles':len(violations)}},indent=2))
