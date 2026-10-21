"""Finite exact weighted-completion checks; no spectral compression claimed."""
from fractions import Fraction as Q
from collections import Counter
from pathlib import Path
import itertools
import json
import numpy as np

counts = Counter()
asymmetry = None
positive_collision = None

def tent_num(t, p, H):
    d = min(t % p, (-t) % p)
    return H + 1 - d if d <= H else 0

def run_host(p, H, linear, quadratic, samples=None):
    global asymmetry, positive_collision
    omega = [v for v in range(p)
             if all(xi*v % p in residues for xi, residues in linear)
             and all((c*v*v+b*v+e) % p in residues
                     for c,b,e,residues in quadratic)]
    assert omega
    n = len(omega)
    den = (H+1)**(len(linear)+2*len(quadratic))
    weights = {}
    for x in range(p):
        for h in range(p):
            v = 1
            for xi,_ in linear:
                v *= tent_num(xi*h,p,H)
            for c,b,e,_ in quadratic:
                v *= tent_num((2*c*x+b)*h,p,H)*tent_num(c*h*h,p,H)
            weights[x,h] = v
        assert weights[x,0] == den
    idx = {v:i for i,v in enumerate(omega)}
    aps = [set((x+j*h)%p for j in range(4)) for x in range(p) for h in range(1,p)]
    records = {}
    for v in omega:
        records[v] = [(j,h,weights[(v-j*h)%p,h],
                       frozenset((v+(i-j)*h)%p for i in range(4) if i!=j))
                      for j in range(4) for h in range(1,p)
                      if weights[(v-j*h)%p,h]]
    candidate_sets = ({v for i,v in enumerate(omega) if mask >> i & 1}
                      for mask in range(1 << n)) if samples is None else samples
    for A in candidate_sets:
        assert A <= set(omega)
        if any(ap <= A for ap in aps):
            continue
        a=Q(len(A),n); w=Q(n,p)
        qj={v:[Q(0) for _ in range(4)] for v in omega}
        q={}; coll=Q(0); disjoint=Q(0)
        for v in omega:
            active=[rec for rec in records[v] if rec[3] <= A]
            for j,h,wt,triple in active:
                qj[v][j] += Q(wt,p*den)
            q[v]=sum(qj[v])
            assert v not in A or q[v]==0
            for rec1 in active:
                for rec2 in active:
                    prod=Q(rec1[2]*rec2[2],n*p*p*den*den)
                    if rec1[3] & rec2[3]:
                        coll += prod
                    else:
                        disjoint += prod
        m=sum(q.values())/n
        means=[sum(qj[v][j] for v in omega)/n for j in range(4)]
        moments=[Q(0) for _ in range(5)]
        for x in range(p):
            for h in range(p):
                vv=[(x+j*h)%p for j in range(4)]
                if all(v in idx for v in vv):
                    B=[int(v in A) for v in vv]
                    for degree in range(5):
                        moments[degree] += Q(weights[x,h],p*p*den)*sum(
                            int(np.prod([B[i] for i in slots]))
                            for slots in itertools.combinations(range(4),degree))
        T,M1,M2,M3,M4=moments
        R1=a**3*M1-4*a**4*T
        R2=a*a*M2-3*a**3*M1+6*a**4*T
        R3=a*M3-2*a*a*M2+3*a**3*M1-4*a**4*T
        assert M4 == a*w/p
        if a:
            assert M3==4*a**3*T+3*R1/a+2*R2/a+R3/a
        assert w*m == M3-4*a*w/p
        assert sum(q[v]**2 for v in omega)/n == coll+disjoint
        assert coll <= (24*(means[0]+means[3])+26*(means[1]+means[2]))/p
        assert coll <= 26*m/p
        counts['exact_diagonal_mean_and_collision_cases']+=1
        if a==1:
            assert m==0
            continue
        u={v:Q(int(v in A))-a for v in omega}
        k={v:q[v]-m for v in omega}
        z={v:q[v]-m*(1-int(v in A))/(1-a) for v in omega}
        assert all(k[v]==-m*u[v]/(1-a)+z[v] for v in omega)
        assert sum(z.values())==0
        assert sum(u[v]*z[v] for v in omega)==0
        assert sum(u[v]*k[v] for v in omega)/n == -a*m
        W=sum(k[v]**2 for v in omega)/n
        Z=sum(z[v]**2 for v in omega)/n
        assert W == a*m*m/(1-a)+Z
        assert coll+disjoint == m*m/(1-a)+Z
        assert disjoint >= m*m/(1-a)-26*m/p
        counts['exact_projection_and_disjoint_energy_cases']+=1
        if asymmetry is None and any(qj[v][0]!=qj[v][3] for v in omega):
            asymmetry={'p':p,'H':H,'omega':omega,'A':sorted(A),
                       'channel_means':[str(x) for x in means],
                       'meaning':'original weight can separate endpoint channels'}
        if positive_collision is None and coll>0 and disjoint>0:
            positive_collision={'p':p,'H':H,'omega':omega,'A':sorted(A),
                                'm':str(m),'collision':str(coll),'disjoint':str(disjoint)}
        if a==0 or m==0:
            continue
        uv=np.array([float(u[v]) for v in omega])
        kv=np.array([float(k[v]) for v in omega])
        gamma=[(0,1),(1,0),(1,1),(0,2)]
        X=np.array([[np.exp(2j*np.pi*(c*v*v+t*v)/p) for c,t in gamma] for v in omega])
        X-=X.mean(axis=0)
        coeff=np.linalg.pinv(X,rcond=1e-12)@kv
        approx=X@coeff; err=np.linalg.norm(kv-approx)/np.sqrt(n)
        ell1=float(sum(abs(coeff)))
        delta=max(abs(np.mean(uv*np.exp(-2j*np.pi*(c*np.array(omega)**2+t*np.array(omega))/p)))
                  for c in range(p) for t in range(p) if (c,t)!=(0,0))
        assert float(a*m) <= delta*ell1+np.sqrt(float(a*(1-a)))*err+1e-10
        gram=X.conj().T@X/n
        vals=np.linalg.eigvalsh(gram); vals=vals[vals>1e-10]
        energy=float(np.vdot(approx,approx).real/n)
        if len(vals):
            assert ell1**2 <= len(gamma)*energy/min(vals)+1e-8
        counts['numerical_atomic_and_Gram_cases']+=1
    counts['hosts']+=1

# Independent exact check of every colliding ratio, including small-prime
# modular coincidences and additional wrapped AP exclusions.
for p in (5,7,11,13,17,19,23,29,31):
    aps=[set((x+i*h)%p for i in range(4)) for x in range(p) for h in range(1,p)]
    for j in range(4):
        first={(i-j)%p for i in range(4) if i!=j}
        row_total=0
        for ell in range(4):
            allowed=0
            for ratio in range(1,p):
                second={((i-ell)*ratio)%p for i in range(4) if i!=ell}
                if first & second and not any(ap <= first|second for ap in aps):
                    allowed+=1
            expected=5 if j in (0,3) and ell in (0,3) else 6 if j in (1,2) and ell in (1,2) else 7
            assert allowed<=expected
            row_total+=allowed
            counts['exact_overlap_geometry_channel_pairs']+=1
        assert row_total<=(24 if j in (0,3) else 26)

for p,H,linear,quadratic in [
    (7,1,[(1,set(range(7)))],[]),
    (11,2,[(1,set(range(8)))],[(1,1,0,set(range(10)))]),
    (13,2,[(1,set(range(9)))],[(1,2,0,set(range(11)))]),
]:
    run_host(p,H,linear,quadratic)
run_host(101,10,[(1,set(range(31)))],[(1,0,0,set(range(101)))],
         [set(),{1,2,3,10,20,30}])
assert asymmetry is not None
assert positive_collision is not None
result={'status':'passed; finite weighted identities only; O2 and P12 remain open',
        'counts':dict(counts),'weighted_reversal_asymmetry':asymmetry,
        'positive_collision_and_disjoint_example':positive_collision,
        'verification_scope':'Exact Fraction diagonal, projection, and collision bounds; floating atomic/Gram checks at stated tolerances. No spectral compression or asymptotic phase-selection claim.'}
Path('WEIGHTED_COMPLETION_VERIFICATION_20261018.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
