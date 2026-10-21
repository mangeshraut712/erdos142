"""Run: python3 verify_target_scale_20260914.py. Auxiliary checks only."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
import cmath
import json
import math


def partition(p, frequencies):
    cells = defaultdict(set)
    for x in range(p):
        cells[tuple(4*((xi*x) % p)//p for xi in frequencies)].add(x)
    return list(cells.values())


def conditional(values, cells):
    out = [F(0)]*len(values)
    for cell in cells:
        mean = sum(values[x] for x in cell)/len(cell)
        for x in cell:
            out[x] = mean
    return out


def dft(values):
    p = len(values)
    return [sum(float(values[x])*cmath.exp(-2j*math.pi*k*x/p)
                for x in range(p))/p for k in range(p)]


def exact_checks():
    cases = points = 0
    for p in (5, 7):
        old = partition(p, [1])
        new = partition(p, [1, 2])
        arcs = partition(p, [2])
        for mask in range(1 << p):
            b = [F((mask >> x) & 1) for x in range(p)]
            g = conditional(b, old)
            u = [v-w for v, w in zip(b, g)]
            refined = conditional(b, new)
            delta = sum(v*v-w*w for v, w in zip(refined, g))/p
            formula = sum(sum(u[x] for x in v)**2/(p*len(v)) for v in new)
            coarse = sum(sum(u[x] for x in v)**2/(p*len(v)) for v in arcs)
            assert delta == formula and delta >= coarse
            variance = conditional([v*v for v in u], old)
            for x in range(p):
                assert u[x]**2 == (1-2*g[x])*u[x]+g[x]*(1-g[x])
                assert variance[x] == g[x]*(1-g[x])
                points += 1
            cases += 1
    return {'conditional_increment_cases': cases, 'conditional_boolean_points': points}


def fourier_checks():
    tol = 2e-9
    counts = defaultdict(int)
    for p in (5, 7, 13):
        seed = {0, 1, 3} if p != 13 else {0, 1, 3, 9}
        a = len(seed)/p
        b = [int(x in seed) for x in range(p)]
        fh = dft([v-a for v in b])
        bh = dft(b)
        direct = sum(math.prod(b[(x+j*h) % p] for j in range(4))
                     for x in range(p) for h in range(p))/p**2
        spectral = sum(bh[(u+2*v) % p]*bh[(-2*u-3*v) % p]*bh[u]*bh[v]
                       for u in range(p) for v in range(p))
        triple = sum(fh[t]**2*fh[-2*t % p] for t in range(1, p))
        skipped = sum(fh[t]*fh[2*t % p]*fh[-3*t % p] for t in range(1, p))
        quartic = sum(fh[(u+2*v) % p]*fh[(-2*u-3*v) % p]*fh[u]*fh[v]
                      for u in range(p) for v in range(p))
        assert abs(direct-spectral) < tol
        assert abs(direct-(a**4+2*a*(triple+skipped)+quartic)) < tol
        for xi in range(p):
            lhs = sum(fh[t]*fh[(xi-t) % p] for t in range(p))
            rhs = (1-2*a)*fh[xi]+(a*(1-a) if xi == 0 else 0)
            assert abs(lhs-rhs) < tol
            counts['boolean_fourier_identities'] += 1
        counts['four_term_expansions'] += 1
        for size in range(1, 4):
            for ds in combinations(range(1, p), size):
                dissociated = all(sum(c*x for c, x in zip(cs, ds)) % p != 0
                                  for cs in product((-1, 0, 1), repeat=size) if any(cs))
                if not dissociated:
                    continue
                assert 2**size <= p
                tau = min(abs(fh[x]) for x in ds)
                if tau < 1e-12:
                    continue
                t = tau/(2*a)
                values = [math.prod(1+t*math.cos(2*math.pi*xi*x/p+cmath.phase(fh[xi]))
                                    for xi in ds) for x in range(p)]
                assert abs(sum(values)/p-1) < tol
                assert size <= 4*(a/tau)**2*math.log(1/a)+tol
                counts['dissociated_riesz_products'] += 1
    for p in (5, 7):
        for aa, bb, cc in product(range(p), repeat=3):
            rank = 0 if aa == bb == cc == 0 else (2 if (aa*cc-bb*bb) % p else 1)
            value = sum(cmath.exp(2j*math.pi*((aa*x*x+2*bb*x*y+cc*y*y) % p)/p)
                        for x in range(p) for y in range(p))/p**2
            assert abs(abs(value)**2-p**(-rank)) < tol
            counts['quadratic_matrix_sums'] += 1
    return dict(counts)


def quadratic_counts():
    result = []
    for p in (101, 503, 1009):
        length = int(p/math.log(p))
        interval = [int(x < length) for x in range(p)]
        ih = dft(interval)
        b = [int(x*x % p < length) for x in range(p)]
        size = sum(b)
        total = sum(all(b[(x+j*h) % p] for j in range(4))
                    for x in range(p) for h in range(p))
        resonance = sum(abs(ih[t])**2*abs(ih[3*t % p])**2 for t in range(p))
        error = (1+math.log(p))**4/math.sqrt(p)
        assert abs(total/p**2-resonance) <= error+1e-9
        assert resonance >= 4*(length/p)**3/(3*math.pi**4)-1e-9
        result.append({'p': p, 'size': size, 'ordered_nontrivial_4aps': total-size,
                       'lambda4': total/p**2, 'positive_resonance': resonance})
    return result


def budget_checks():
    cases = 0
    for start in (1/16, 1/64, 1/256):
        l0 = math.log(2/start)
        k0 = 0.25/l0
        r0 = math.ceil(0.5*l0*l0)
        jbound = math.ceil(4*l0/k0)+1
        dbound = 1+jbound*r0
        sbound = l0+jbound*(math.log(2/k0)+l0+r0*math.log(4))
        a = start
        rank = 1
        steps = 0
        retained_loss = 0.0
        while a <= 0.8:
            ell = math.log(2/a)
            kappa = 0.25/ell
            r = math.ceil(0.5*ell*ell)
            retained_loss += math.log(2/kappa/a)+r*math.log(4)
            rank += r
            a *= 1+kappa/2
            steps += 1
        size_loss = math.log(a/start)+retained_loss
        assert steps <= jbound and rank <= dbound and size_loss <= sbound
        cases += 1
    return cases


if __name__ == '__main__':
    print(json.dumps({'status': 'passed', 'exact': exact_checks(),
                      'numerical_fourier': fourier_checks(),
                      'quadratic_counts': quadratic_counts(),
                      'conditional_budget_cases': budget_checks(),
                      'target_energy_proved': False, 'r4_target_proved': False}, indent=2))
