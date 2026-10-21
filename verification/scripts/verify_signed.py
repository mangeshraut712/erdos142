# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Mangesh Raut

"""Offline exact signed-form checks; labelled numerical Fourier diagnostics.

Standard library only. Finite checks are not an asymptotic proof.
Run: python3 verification/scripts/verify_signed.py > verification/results/signed_verification.json
"""

from fractions import Fraction as F
from itertools import product
from math import cos, sin, pi, sqrt, copysign
import json

from verify_phase2 import REGIME_SET


def data(bits):
    p, n = len(bits), sum(bits)
    alpha = F(n, p)
    inv3 = pow(3, -1, p)
    kernel = [[bits[(2*u+v)*inv3 % p] * bits[(u+2*v)*inv3 % p]
               for v in range(p)] for u in range(p)]
    rows = [sum(row) for row in kernel]
    assert sum(rows) == n*n
    assert sum(kernel[u][u] for u in range(p)) == n
    assert all(kernel[u][v] == kernel[v][u] for u in range(p) for v in range(p))
    assert all(r <= n for r in rows)
    assert all(rows[u] == sum(bits[y]*bits[(2*y-u) % p] for y in range(p))
               for u in range(p))
    if 2 <= n < p:
        # Strict HS(H)^2 > tr(H)^2 proves negative spectrum without eigenvalue rounding.
        assert sum(r*r for r in rows) < n**3
    q, triples, fours, md = [], [], [], []
    scaled = [p*x-n for x in bits]
    for d in range(p):
        pair = sum(bits[(x+d) % p]*bits[(x+2*d) % p] for x in range(p))
        triple = sum(bits[x]*bits[(x+d) % p]*bits[(x+2*d) % p] for x in range(p))
        right = sum(bits[(x+d) % p]*bits[(x+2*d) % p]*bits[(x+3*d) % p]
                    for x in range(p))
        four = sum(bits[x]*bits[(x+d) % p]*bits[(x+2*d) % p]*bits[(x+3*d) % p]
                   for x in range(p))
        mixed = sum(scaled[x]*bits[(x+d) % p]*bits[(x+2*d) % p]*scaled[(x+3*d) % p]
                    for x in range(p))
        assert triple == right
        assert F(mixed, p**3) == F(four, p)-2*alpha*F(triple,p)+alpha**2*F(pair,p)
        q.append(pair); triples.append(triple); fours.append(four); md.append(mixed)
    count3 = F(sum(triples), p*p)
    count4 = F(sum(fours), p*p)
    t = count3-alpha**3
    m = F(sum(md), p**4)
    direct = F(sum(scaled[u]*kernel[u][v]*scaled[v] for u in range(p) for v in range(p)), p**4)
    assert direct == m == count4-2*alpha*count3+alpha**4
    assert count3 == F(sum(bits[u]*rows[u] for u in range(p)), p*p)
    assert sum(q) == n*n
    ap_free = not any(fours[1:])
    if ap_free:
        assert count4 == alpha/p
        assert all(bits[u]*kernel[u][v]*bits[v] == (bits[u] if u == v else 0)
                   for u in range(p) for v in range(p))
        for d in range(1,p):
            assert 2*triples[d] <= q[d]
            assert 3*q[d] <= 2*n
            assert n-2*q[d]+triples[d] >= 0
            if q[d]:
                r = F(triples[d], q[d])
                assert F(md[d], p*p*q[d]) == alpha**2-2*alpha*r
    c0 = F(1,4)
    signed = ap_free and m <= -c0*alpha**4 and n > 0
    popularity = None
    if signed:
        Q = alpha**2-alpha/p
        assert Q > 0
        rbar = F(sum(triples[1:]), sum(q[1:]))
        correction = ((1-alpha)**2+c0*alpha**2)/(2*p*Q)
        assert rbar >= (1+c0)*alpha/2+correction
        popular = [d for d in range(1,p) if q[d] and F(triples[d],q[d]) >= alpha/2]
        mass = F(sum(q[d] for d in popular), sum(q[1:]))
        assert mass >= c0*alpha/(1-alpha)+2*correction/(1-alpha)
        number_bound = F(3,2)*(c0*p*alpha**2/(1-alpha)+(1-alpha)/alpha)
        assert len(popular) >= number_bound
        popularity = {"count": len(popular), "count_lower_bound": str(number_bound),
                      "weighted_endpoint_density": str(rbar), "weighted_mass": str(mass)}
    return {"p":p, "size":n, "alpha":str(alpha), "ap_free":ap_free,
            "in_regime":bool(p*alpha**3 >= 2), "T":str(t), "M":str(m),
            "three_ap_count":sum(triples), "signed_mixed":signed,
            "popularity":popularity}, kernel, rows


def dft(values):
    p = len(values)
    return [sum(values[x]*complex(cos(-2*pi*k*x/p),sin(-2*pi*k*x/p))
                for x in range(p))/p for k in range(p)]


def fourier_checks(bits, exact, kernel):
    p, n = len(bits), sum(bits)
    alpha = n/p
    bhat = dft(bits)
    fhat = bhat.copy(); fhat[0] -= alpha
    mixed = sum(fhat[r]*bhat[(s-2*r) % p]*bhat[(r-2*s) % p]*fhat[s]
                for r in range(p) for s in range(p))
    assert abs(mixed-float(F(exact["M"]))) < 1e-10
    t = sum(fhat[k]**2*fhat[-2*k % p] for k in range(p))
    assert abs(t-float(F(exact["T"]))) < 1e-10
    pairs = ((0,0),(0,1),(1,1),(1,2),(2,3),(p-1,p-2))
    for r,s in pairs:
        matrix = sum(kernel[u][v]*complex(cos(2*pi*(s*v-r*u)/p),sin(2*pi*(s*v-r*u)/p))
                     for u in range(p) for v in range(p))/(p*p)
        assert abs(matrix-bhat[(2*r+s) % p]*bhat[(-r-2*s) % p]) < 1e-10
    phase_count = 0
    coefficients = product(range(p),repeat=2) if p <= 13 else ((a,b) for a in range(4) for b in range(4))
    minimum = 1.0
    for a,b in coefficients:
        phases = [complex(cos(2*pi*((a*x*x+b*x) % p)/p),sin(2*pi*((a*x*x+b*x) % p)/p)) for x in range(p)]
        rayleigh = sum(phases[u].conjugate()*kernel[u][v]*phases[v]
                       for u in range(p) for v in range(p))/(p*p)
        expected = abs(sum(bits[x]*phases[x]**3 for x in range(p))/p)**2
        assert abs(rayleigh-expected) < 1e-10
        assert rayleigh.real >= -1e-10
        minimum = min(minimum,rayleigh.real)
        phase_count += 1
    return {"mixed_formula_residual":abs(mixed-float(F(exact["M"]))),
            "quadratic_phases_checked":phase_count,"minimum_quadratic_rayleigh":minimum,
            "arithmetic":"floating point, tolerance 1e-10"}


def jacobi_eigenvalues(matrix):
    a = [row.copy() for row in matrix]
    n = len(a)
    for _ in range(100*n*n):
        p,q = max(((i,j) for i in range(n) for j in range(i+1,n)), key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[p][q]) < 1e-13:
            return sorted(a[i][i] for i in range(n))
        tau = (a[q][q]-a[p][p])/(2*a[p][q])
        t = copysign(1.0,tau)/(abs(tau)+sqrt(1+tau*tau))
        c = 1/sqrt(1+t*t); s = t*c
        apq = a[p][q]
        a[p][p] -= t*apq; a[q][q] += t*apq
        a[p][q] = a[q][p] = 0.0
        for k in range(n):
            if k in (p,q): continue
            akp,akq = a[k][p],a[k][q]
            a[k][p] = a[p][k] = c*akp-s*akq
            a[k][q] = a[q][k] = s*akp+c*akq
    raise AssertionError("Jacobi iteration did not converge")


def quadratic_overlap_check(bits, exact_m):
    p,alpha = len(bits),F(sum(bits),len(bits))
    b = alpha*(1-alpha)
    phases = [complex(cos(-2*pi*k/p),sin(-2*pi*k/p)) for k in range(p)]
    qb,qf = {},{}
    for a in range(p):
        for r in range(p):
            values = [phases[(a*x*x+r*x) % p] for x in range(p)]
            value_b = sum(bits[x]*values[x] for x in range(p))/p
            value_f = value_b-float(alpha)*sum(values)/p
            qb[a,r] = abs(value_b)**2
            qf[a,r] = abs(value_f)**2
    overlap = sum(qf[a,r]*qb[3*a % p,3*r % p] for a in range(p) for r in range(p))
    expected = alpha*b+F(exact_m)-alpha*(1-alpha)**2/p
    assert abs(overlap-float(expected)) < 1e-10
    return {"overlap":overlap,"exact_target":str(expected),
            "residual":abs(overlap-float(expected)),"tolerance":1e-10}


def semicircle_checks():
    checked = 0
    for n in range(2,9):
        for k in range(1,2*n+1):
            phases = [F(k*x,2*n+1) % 1 for x in range(n)]
            boundaries = sorted({z for ph in phases for z in (ph,(ph-F(1,2)) % 1)})
            cuts = [(boundaries[i]+(boundaries[i+1] if i+1<len(boundaries) else boundaries[0]+1))/2 % 1
                    for i in range(len(boundaries))]
            masks = [[x for x in range(n) if (phases[x]-t) % 1 < F(1,2)] for t in cuts]
            for bits in product((0,1),repeat=n):
                size = sum(bits)
                if size in (0,n): continue
                alpha = F(size,n)
                h = [sum((F(bits[x])-alpha for x in cell),F(0))/n for cell in masks]
                for cell,value in zip(masks,h):
                    if cell:
                        assert F(len(cell),n)*(F(sum(bits[x] for x in cell),len(cell))-alpha) == value
                eta = abs(sum((float(bits[x]-alpha))*complex(cos(2*pi*float(phases[x])),sin(2*pi*float(phases[x]))) for x in range(n))/n)
                assert float(max(h)) >= eta/2-1e-12
                checked += 1
    # Opposite phases attain the improved universal constant one half.
    assert F(1,2)*(1-F(1,2)) == F(1,2)/2
    return checked


def concentration_checks():
    checked = 0
    for n in range(2,10):
        for bits0 in product((0,1),repeat=n):
            size0 = sum(bits0)
            if size0 == 0: continue
            bits = list(bits0); alpha0 = F(size0,n); retained = F(1); steps = 0
            while True:
                m,size = len(bits),sum(bits)
                candidate = None
                for start in range(m):
                    for step in range(1,m+1):
                        points=[]; count=0
                        for x in range(start,m,step):
                            points.append(x); count += bits[x]
                            if 2*count >= size and count*m >= 2*size*len(points):
                                candidate=points.copy(); break
                        if candidate: break
                    if candidate: break
                if candidate is None: break
                new = [bits[x] for x in candidate]
                retained *= F(sum(new),size)
                bits = new; steps += 1
            final_alpha = F(sum(bits),len(bits))
            assert F(len(bits),n) == retained*alpha0/final_alpha
            assert len(bits) >= alpha0**2*n
            assert 2**steps*alpha0 <= 1
            checked += 1
    return checked


def relative_window_checks():
    checked = 0
    for p in (5,7):
        for states in product((0,1,2),repeat=p):
            w=[int(x>0) for x in states]
            bits=[int(x==2) for x in states]
            m,n=sum(w),sum(bits)
            if m == 0: continue
            if any(all(bits[(x+j*d) % p] for j in range(4)) for x in range(p) for d in range(1,p)):
                continue
            a=F(n,m)
            g=[m*bits[x]-n*w[x] for x in range(p)]
            mixed=phi=left=right=0
            for x in range(p):
                for d in range(p):
                    y,z,v=(x+d) % p,(x+2*d) % p,(x+3*d) % p
                    mixed += g[x]*bits[y]*bits[z]*g[v]
                    phi += w[x]*bits[y]*bits[z]*w[v]
                    left += bits[x]*bits[y]*bits[z]*w[v]
                    right += w[x]*bits[y]*bits[z]*bits[v]
            assert left == right
            assert F(mixed,m*m*p*p) == F(n,p*p)-2*a*F(left,p*p)+a*a*F(phi,p*p)
            checked += 1
    return checked


def affine_spreading_checks():
    results=[]
    for p,points in ((7,{0,1,3}),(13,{0,1,3,9})):
        n=len(points); alpha=F(n,p)
        images=[[int(x in {(a*y+b) % p for y in points}) for x in range(p)]
                for a in range(1,p) for b in range(p)]
        for length in range(1,p+1):
            deviations=[F(sum(bits[:length]))-alpha*length for bits in images]
            assert sum(deviations) == 0
            variance=sum(d*d for d in deviations)/len(images)
            assert variance == alpha*(1-alpha)*F(length*(p-length),p-1)
        qmax=(4*p+n-1)//n
        worst=[]
        for bits in images:
            discrepancy=0
            for q in range(1,min(qmax,p)+1):
                for residue in range(q):
                    prefix=0; lo=0; hi=0
                    for x in range(residue,p,q):
                        prefix += p*bits[x]-n
                        lo=min(lo,prefix); hi=max(hi,prefix)
                    discrepancy=max(discrepancy,hi-lo)
            worst.append(F(discrepancy,p))
        h=1+(p-1).bit_length()
        mean_square=sum(d*d for d in worst)/len(worst)
        assert mean_square <= 20*h*h*p
        results.append({"p":p,"A":sorted(points),"affine_images":len(images),
                        "exact_mean_squared_max_discrepancy":str(mean_square),
                        "scope":"finite covariance and discrepancy checks; asymptotic counterexample proved analytically"})
    return results


def main():
    total = ap_free = signed = negative_generic = 0
    for p in (5,7,11,13):
        for bits in product((0,1),repeat=p):
            result,_,_ = data(bits)
            total += 1
            ap_free += result["ap_free"] and result["size"] > 0
            signed += result["signed_mixed"]
            negative_generic += 2 <= result["size"] < p
    examples = []
    for p,points in ((7,[0,1,2,4]),(11,[3,6,8,9,10]),(13,[0,1,3,9]),(101,REGIME_SET)):
        bits=[int(x in points) for x in range(p)]
        result,kernel,rows=data(bits)
        result["A"]=points
        result["numerical_fourier"]=fourier_checks(bits,result,kernel)
        result["numerical_quadratic_overlap"]=quadratic_overlap_check(bits,result["M"])
        if p == 7:
            alpha = len(points)/p
            kmatrix = [[v/p for v in row] for row in kernel]
            hmatrix = [[(kernel[u][v]-rows[u]/p-rows[v]/p+alpha**2)/p for v in range(p)] for u in range(p)]
            eigk,eigh=jacobi_eigenvalues(kmatrix),jacobi_eigenvalues(hmatrix)
            assert min(eigk) <= -9/49+1e-10 and min(eigh) <= -9/49+1e-10
            result["numerical_eigenvalues"]={"K":eigk,"H":eigh,"tolerance":1e-10}
        examples.append(result)
    eligible=examples[-1]
    assert eligible["in_regime"] and eligible["signed_mixed"]
    assert F(eligible["T"]) > -F(eligible["alpha"])**3/8
    # Negative fiber product need not imply negative unconditional endpoint correlation.
    bits=[int(x in (7,8,10,11,12)) for x in range(13)]
    result,_,_=data(bits)
    assert result["ap_free"]
    a=F(5,13)
    assert a*a*F(3,13)-2*a*F(1,13) == F(-55,2197)
    assert F(sum(bits[x]*bits[(x+3) % 13] for x in range(13)),13)-a*a == F(1,169)
    print(json.dumps({"status":"signed-form diagnostics passed; no target asymptotic theorem proved",
                     "exact_indicator_subsets":total,"nonempty_4ap_free_subsets":ap_free,
                     "signed_mixed_subsets":signed,"generic_negative_spectrum_cases":negative_generic,
                     "examples":examples,"semicircle_localization_checks":semicircle_checks(),
                     "concentration_regularization_checks":concentration_checks(),
                     "relative_window_identity_checks":relative_window_checks(),
                     "affine_spreading_checks":affine_spreading_checks(),
                     "false_fiber_inference":{"p":13,"A":[7,8,10,11,12],"d":1,
                                               "m_d":"-55/2197","c_3d":"1/169"},
                     "external_dependencies":[]},indent=2))


if __name__ == "__main__":
    main()
