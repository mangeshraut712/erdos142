"""Supporting finite checks for the new offline research run.

Exact rational identities are separate from floating Fourier/scalar diagnostics.
The asymptotic conditional closure and auxiliary theorems have symbolic proofs;
this script does not prove H or the r4 target. Standard library only.
"""
from fractions import Fraction as F
from itertools import product
from math import ceil, comb, cos, exp, isqrt, log, pi, sin, sqrt
from pathlib import Path
import json
import random


def primes_to(limit):
    return [n for n in range(2, limit + 1)
            if all(n % d for d in range(2, isqrt(n) + 1))]


def check_fourier():
    checked = ap_free = counting_hypothesis_cases = 0
    worst_error = 0.0
    for p in (5, 7, 11):
        roots = [complex(cos(-2*pi*k/p), sin(-2*pi*k/p)) for k in range(p)]
        for bits in product((0, 1), repeat=p):
            n = sum(bits)
            a = F(n, p)
            f = [p*b-n for b in bits]
            count = t = s = q = 0
            free = True
            for x in range(p):
                for d in range(p):
                    ids = [(x+j*d) % p for j in range(4)]
                    c = bits[ids[0]]*bits[ids[1]]*bits[ids[2]]*bits[ids[3]]
                    count += c
                    if d and c:
                        free = False
                    t += f[ids[0]]*f[ids[1]]*f[ids[2]]
                    s += f[ids[0]]*f[ids[1]]*f[ids[3]]
                    q += f[ids[0]]*f[ids[1]]*f[ids[2]]*f[ids[3]]
            count, t, s, q = F(count,p*p), F(t,p**5), F(s,p**5), F(q,p**6)
            assert count == a**4+2*a*(t+s)+q
            if free:
                assert count == a/p
                ap_free += 1
            bh = [sum(bits[x]*roots[(k*x) % p] for x in range(p))/p for k in range(p)]
            fh = [z-(float(a) if k == 0 else 0) for k,z in enumerate(bh)]
            fourier_count = sum(bh[(u+2*v) % p]*bh[(-2*u-3*v) % p]*bh[u]*bh[v]
                                for u in range(p) for v in range(p))
            error = abs(fourier_count-float(count))
            worst_error = max(worst_error,error)
            assert error < 1e-10
            rho = max(abs(z) for z in fh[1:])
            b = float(a*(1-a))
            assert abs(float(t)) <= b*rho+1e-10
            assert abs(float(s)) <= b*rho+1e-10
            if a and rho <= float(a*a)/16 and q >= -a**4/2:
                assert count >= a**4/4-F(1,10**9)
                counting_hypothesis_cases += 1
            checked += 1
    # This is a real counterexample to the log_3 bound, not just a failure of its proof.
    assert all((c0+2*c1) % 5 for c0,c1 in product((-1,0,1),repeat=2) if c0 or c1)
    assert 2 > log(5)/log(3)
    return {'subsets': checked, 'ap_free_including_empty_full_test_range': ap_free,
            'counting_sufficient_hypothesis_cases': counting_hypothesis_cases,
            'worst_float_fourier_error':worst_error, 'float_tolerance':1e-10,
            'dissociation_counterexample':'{1,2} in Z_5 has size 2 > log_3(5)'}


def check_atoms():
    checked = 0
    for p in (5,7,11):
        partitions = [[x % 2 for x in range(p)], [x % 3 for x in range(p)],
                      [4*x//p for x in range(p)]]
        for mask in range(1,(1 << p)-1):
            bits = [(mask >> x) & 1 for x in range(p)]
            k = sum(bits)
            a = F(k,p)
            for labels in partitions:
                cells = [[x for x in range(p) if labels[x] == label] for label in sorted(set(labels))]
                mu = [F(len(cell),p) for cell in cells]
                density = [F(sum(bits[x] for x in cell),len(cell)) for cell in cells]
                variance = sum(m*(b-a)**2 for m,b in zip(mu,density))
                if not variance:
                    continue
                eta = min(F(1,4),variance/a**2)
                witnesses = [i for i,b in enumerate(density)
                             if b >= a*(1+eta/2) and mu[i]*b/a >= eta*a/(2*len(cells))]
                assert witnesses
                for i in witnesses:
                    r = mu[i]*density[i]/a
                    assert mu[i] == r*a/density[i]
                checked += 1
    return {'exact_rational_atom_instances':checked}


def check_scalar_budget():
    rng = random.Random(20261002)
    checked = 0
    worst_rank_ratio = worst_loss_ratio = 0.0
    for eta in (0.01,0.1,0.25):
        q = 1+eta/2
        for k in (1,3,10):
            for t in (1e-2,1e-4,1e-8,1e-12,1e-16):
                ell = log(2/t)
                jbound = ceil(ell/log(q))+1
                ubound = jbound+k/(1-q**-0.5)*(2*t**-0.5/ell+t**-0.25/log(2.5))
                sbound = ell+jbound*(log(2/eta)+ell)+log(4)*ubound
                for mode in range(4):
                    a = t*(1+rng.random())
                    a_initial = a
                    ranks = retained_log_loss = 0.0
                    steps = 0
                    while a <= 0.8:
                        s = ceil(k/(sqrt(a)*log(2/a)))
                        ranks += s
                        retained_log_loss += log(2/eta)+log(1/a)+s*log(4)
                        multiplier = q if mode == 0 else q*(1+rng.random()*mode/2)
                        a = min(1,a*multiplier)
                        steps += 1
                    loss = log(a/a_initial)+retained_log_loss
                    assert steps <= jbound
                    assert ranks <= ubound*(1+1e-12)
                    assert loss <= sbound*(1+1e-12)
                    worst_rank_ratio=max(worst_rank_ratio,ranks/ubound)
                    worst_loss_ratio=max(worst_loss_ratio,loss/sbound)
                    checked += 1
    substitution = []
    eta=0.1; q=1+eta/2; k=1; epsilon=1
    for x in (1e8,1e16,1e32,1e64,1e128):  # x means log N, not N.
        t=epsilon/x; ell=log(2/t); j=ceil(ell/log(q))+1
        u=j+k/(1-q**-0.5)*(2*t**-0.5/ell+t**-0.25/log(2.5))
        d=1+u; s=ell+j*(log(2/eta)+ell)+log(4)*u
        substitution.append({'log_N':x,'terminal_product_over_log_N':d*(s+log(2*d)+1)/x,
                             'rank_over_sqrt_log_N':d/sqrt(x),
                             'loss_over_sqrt_log_N':s/sqrt(x)})
    return {'scalar_trajectories':checked,'worst_rank_envelope_ratio':worst_rank_ratio,
            'worst_loss_envelope_ratio':worst_loss_ratio,'asymptotic_substitution_diagnostics':substitution,
            'scope':'floating diagnostics, not an asymptotic proof'}


def check_terminal():
    rng=random.Random(14220261002)
    windows=subsets=0
    for p in (5,7,11,17,31,43):
        for d in (1,2,3,4):
            for _ in range(12):
                chars=[1]+[rng.randrange(1,p) for _ in range(d-1)]
                intervals=[]
                for i in range(d):
                    width=rng.randrange(1,(p-1)//3+2)
                    start=rng.randrange(p)
                    intervals.append({(start+j) % p for j in range(width)})
                omega={x for x in range(p) if all(chars[i]*x % p in intervals[i] for i in range(d))}
                if not omega or len(omega)==p:
                    continue
                r=1
                while (r+1)**d <= p-1:
                    r += 1
                boxes={}
                h=None
                for u in range(r**d+1):
                    box=tuple(r*(u*xi % p)//p for xi in chars)
                    if box in boxes:
                        h=u-boxes[box]
                        break
                    boxes[box]=u
                assert h is not None and 0<h<p
                residues=[h*xi % p for xi in chars]
                deltas=[v if 2*v<=p else v-p for v in residues]
                assert all(abs(v)<=p//r for v in deltas)
                boundary=len(omega-{(x+h) % p for x in omega})
                assert boundary <= sum(abs(v) for v in deltas) <= d*(p//r)
                points=sorted(omega); index={x:i for i,x in enumerate(points)}
                forbidden=set()
                for x in points:
                    for diff in range(1,p):
                        progression={(x+j*diff) % p for j in range(4)}
                        if progression <= omega:
                            forbidden.add(sum(1 << index[y] for y in progression))
                if len(points)<=10:
                    masks=range(1 << len(points))
                else:
                    masks=[0]
                    for _ in range(20):
                        order=list(range(len(points)));rng.shuffle(order);mask=0
                        for i in order:
                            candidate=mask | (1 << i)
                            if not any(candidate & bad == bad for bad in forbidden):mask=candidate
                        masks.append(mask)
                for mask in masks:
                    if any(mask & bad == bad for bad in forbidden):
                        continue
                    assert F(mask.bit_count(),len(points)) <= F(3,4)+F(3*boundary,4*len(points))
                    subsets += 1
                windows += 1
    return {'coordinate_windows':windows,'exact_terminal_ap_free_instances':subsets}


def check_prime_step():
    primes=primes_to(2000)
    primorial=1; checked=0
    for m in range(1,1001):
        if m in primes:primorial *= m
        assert primorial <= 4**m
        checked += 1
    # Each factorial-valuation digit is zero or one, and a prime power contribution <=2u.
    valuations=0
    for u in range(2,151):
        assert comb(2*u,u)*(2*u+1) >= 4**u
        for prime in [q for q in primes if q<=2*u]:
            power=prime;v=0
            while power<=2*u:
                digit=(2*u)//power-2*(u//power)
                assert digit in (0,1)
                v += digit;power *= prime
            assert prime**v <= 2*u
            if prime>sqrt(2*u):assert v<=1
            if prime>sqrt(2*u) and F(2*u,3)<prime<=u:assert v==0
            valuations += 1
    return {'primorial_bounds':checked,'prime_valuation_checks':valuations}


def main():
    results={'status':'supporting finite checks passed; H and unconditional target not proved',
             'fourier':check_fourier(),'energy_atoms':check_atoms(),
             'scalar_budget':check_scalar_budget(),'terminal':check_terminal(),
             'prime_step':check_prime_step(), 'external_dependencies':[]}
    print(json.dumps(results,indent=2))


if __name__=='__main__':
    main()
