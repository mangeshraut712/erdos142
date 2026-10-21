"""Run: python3 verify_full_group_hostile_20260914.py. Diagnostics, not a target proof."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
import cmath
import json
import math


def cells(p, coordinates):
    out = defaultdict(set)
    for x in range(p):
        # A rotation t/(8p) includes every critical and intermediate state.
        label = tuple(((8*((xi*x) % p)-t) % (8*p)) // (2*p)
                      for xi, t in coordinates)
        out[label].add(x)
    return list(out.values())


def energy(p, a_set, partition):
    a = Q(len(a_set), p)
    return sum(Q(len(a_set & v)**2, p*len(v)) for v in partition)-a*a


def transform(p, values):
    return [sum(values[x]*cmath.exp(-2j*math.pi*k*x/p) for x in range(p))/p
            for k in range(p)]


def exact_checks():
    counts = defaultdict(int)
    for p in (5, 7, 11, 13, 17, 31, 61, 101, 257, 1009):
        t, power = 0, 1
        while power < p:
            t += 1
            power *= 4
        partition = cells(p, [(4**j % p, 0) for j in range(t)])
        assert len(partition) == p and all(len(v) == 1 for v in partition)
        for x in range(p):
            digits = [4*((4**j*x) % p)//p for j in range(t)]
            encoded = sum(d*4**(t-1-j) for j, d in enumerate(digits))
            assert encoded == power*x//p
            counts['base_four_point_encodings'] += 1
        for k in (1, max(1, int(p**0.75)-1)):
            a = Q(k, p)
            assert k**4 <= p**3
            assert t <= 3*math.log(2/float(a))
            assert energy(p, set(range(k)), partition) == a*(1-a)
            assert a*(1-a) >= a*a/4
            counts['sparse_singleton_factors'] += 1
    for p in (5, 7, 11):
        seed = {0, 1, 3} if p > 5 else {0, 1}
        k = len(seed)
        partition = cells(p, [(1, 0), (2, 3)])
        e = energy(p, seed, partition)
        chi = sum((Q(len(seed & v), k)-Q(len(v), p))**2/Q(len(v), p)
                  for v in partition)
        assert e == Q(k, p)**2*chi
        for u in range(1, p):
            for b in range(p):
                image = {(u*x+b) % p for x in seed}
                pulled = cells(p, [(u % p, -8*b), (2*u % p, 3-16*b)])
                assert energy(p, image, partition) == energy(p, seed, pulled)
                counts['affine_pullbacks'] += 1
        samples = [{(u*x+b) % p for x in seed}
                   for u in range(1, p) for b in range(p)]
        a = Q(k, p)
        assert sum(energy(p, x, partition) for x in samples)/len(samples) == (
            a*(1-a)*Q(len(partition)-1, p-1))
        for v in partition:
            values = [len(x & v) for x in samples]
            mean = Q(sum(values), len(values))
            variance = sum((Q(x)-mean)**2 for x in values)/len(values)
            assert mean == Q(k*len(v), p)
            assert variance == Q(k*(p-k)*len(v)*(p-len(v)), p*p*(p-1))
            counts['affine_cell_moments'] += 1
        host = set(range(p//2+1))
        size = len(host)
        take = 2
        thinnings = [set(c) for c in combinations(sorted(host), take)]
        expected = Q(take, size)**2*energy(p, host, partition)
        for v in partition:
            t = len(host & v)
            variance = Q(take*(size-take)*t*(size-t), size*size*(size-1))
            expected += variance/(p*len(v))
        assert sum(energy(p, x, partition) for x in thinnings)/len(thinnings) == expected
        counts['thinning_sets'] += len(thinnings)
        quarter = cells(p, [(1, 0)])
        for v in quarter:
            for size_a in range(1, len(v)+1):
                for c in combinations(sorted(v), size_a):
                    a_set = set(c)
                    assert energy(p, a_set, quarter) >= Q(size_a, p)**2*(Q(p, len(v))-1)
                    counts['support_subsets'] += 1
    return dict(counts)


def fourier_checks():
    counts = defaultdict(int)
    tol = 2e-10
    for p in (5, 7, 11, 13):
        seed = {x for x in range(p) if x*x % p < max(2, p//3)}
        a = len(seed)/p
        f = [int(x in seed)-a for x in range(p)]
        fh = transform(p, f)
        for coordinates in ([(1, 0)], [(2, 1)], [(1, 0), (2, 3)], [(1, 1), (1, 5)]):
            partition = cells(p, coordinates)
            fourier_energy = 0.0
            for v in partition:
                vh = transform(p, [int(x in v) for x in range(p)])
                correlation = sum(fh[k]*vh[k].conjugate() for k in range(p))
                fourier_energy += abs(correlation)**2/(len(v)/p)
            assert abs(fourier_energy-float(energy(p, seed, partition))) < tol
            counts['fourier_energy_identities'] += 1
        for t in range(8*p):
            for v in cells(p, [(1, t)]):
                vh = transform(p, [int(x in v) for x in range(p)])
                for k in range(1, p):
                    assert abs(vh[k]) <= min(len(v)/p, 1/(2*min(k, p-k)))+tol
                    counts['arc_coefficient_bounds'] += 1
    for p, m in ((17, 2), (17, 4), (29, 7), (101, 20)):
        raw = [abs(sum(cmath.exp(2j*math.pi*j*z/p) for j in range(m)))**4
               for z in range(p)]
        normalizer = (2*m**3+m)/3
        assert abs(sum(raw)/p-normalizer) < 1e-7
        rho = [value/(p*normalizer) for value in raw]
        assert sum(rho[z]*min(z, p-z)/p for z in range(p)) <= 3/m+tol
        rh = transform(p, rho)
        for k in range(p):
            if min(k, p-k) > 2*(m-1):
                assert abs(rh[k]) < tol
        counts['jackson_kernels'] += 1
    # Verify L1 smoothing estimate and energy comparison, including repeated generators.
    p, m = 17, 4
    raw = [abs(sum(cmath.exp(2j*math.pi*j*z/p) for j in range(m)))**4
           for z in range(p)]
    rho = [v/sum(raw) for v in raw]
    for coordinates in ([(1, 0)], [(1, 2), (3, 7)], [(1, 2), (1, 7)]):
        seed = {0, 1, 4, 7}
        a = len(seed)/p
        s = len(coordinates)
        def label(point):
            return tuple(((8*y-t) % (8*p))//(2*p)
                         for y, (_, t) in zip(point, coordinates))
        groups = defaultdict(list)
        for x in range(p):
            groups[label(tuple(xi*x % p for xi, _ in coordinates))].append(x)
        lookup = {key: sum(int(x in seed)-a for x in xs)/len(xs)
                  for key, xs in groups.items()}
        h = [lookup[label(tuple(xi*x % p for xi, _ in coordinates))] for x in range(p)]
        hm = []
        for x in range(p):
            value = 0.0
            for shift in product(range(p), repeat=s):
                point = tuple((xi*x-z) % p for (xi, _), z in zip(coordinates, shift))
                weight = math.prod(rho[z] for z in shift)
                value += weight*lookup.get(label(point), 0.0)
            hm.append(value)
        delta = sum(abs(u-v) for u, v in zip(h, hm))/p
        assert delta <= 12*s/m+tol
        lambdas = {sum(t*xi for t, (xi, _) in zip(ts, coordinates)) % p
                   for ts in product(range(-2*(m-1), 2*m-1), repeat=s)}
        fhat = transform(p, [int(x in seed)-a for x in range(p)])
        mass = sum(abs(fhat[k])**2 for k in lambdas)
        e = float(energy(p, seed, cells(p, coordinates)))
        assert e <= mass+4*delta+tol
        counts['smoothed_factor_checks'] += 1
    return dict(counts)


def construction_checks():
    result = []
    for p in (101, 503, 1009):
        length = int(p/math.log(p))
        a_set = {x for x in range(p) if x*x % p < length}
        a = len(a_set)/p
        fh = transform(p, [int(x in a_set)-a for x in range(p)])
        bound = (1+math.log(p))/math.sqrt(p)
        assert abs(a-length/p) <= bound
        assert max(abs(v) for v in fh[1:]) <= bound
        assert {0, 1, 2, 3} <= a_set
        result.append({'p': p, 'size': len(a_set), 'contains_0_1_2_3': True})
    # Sphere cutoff estimates use integers, with no enormous sphere enumeration.
    for d in (16, 32, 64):
        assert Q(2**(d*d-8*d), 64*d**3) >= 8
    return result


def main():
    print(json.dumps({'status': 'passed', 'exact': exact_checks(),
                      'numerical_diagnostics': fourier_checks(),
                      'quadratic_examples_not_ap_free': construction_checks(),
                      'energy_theorem_proved': False, 'target_proved': False}, indent=2))


if __name__ == '__main__':
    main()
