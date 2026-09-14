# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Mangesh Raut

"""Offline Phase 2 checks. Exact integers/Fractions unless explicitly labelled.

Finite checks corroborate the proofs in PHASE2_AUDIT.md; they do not prove
an asymptotic result. No dependencies, network, or changes to earlier verifiers.
"""

from fractions import Fraction as F
from itertools import product
import cmath
import json


REGIME_SET = [0, 20, 22, 25, 30, 32, 33, 34, 37, 38, 39, 48, 49, 52,
              53, 54, 58, 59, 78, 79, 81, 84, 88, 90, 93, 94, 95, 97]


def moments(v):
    """Integer-valued real input, normalized norms computed exactly."""
    p = len(v)
    shifts = [[v[(x + h) % p] for x in range(p)] for h in range(p)]
    corr = [sum(a * b for a, b in zip(v, row)) for row in shifts]
    u2_4 = F(sum(c * c for c in corr), p ** 3)
    cube = 0
    for h in range(p):
        derivative = [v[x] * shifts[h][x] for x in range(p)]
        for k in range(p):
            s = sum(derivative[x] * derivative[(x + k) % p]
                    for x in range(p))
            cube += s * s
    return u2_4, F(cube, p ** 4)


def check_indicator(bits):
    p, n = len(bits), sum(bits)
    alpha, b = F(n, p), F(n * (p - n), p * p)
    v = [p * bit - n for bit in bits]
    sums = [0] * 16
    mixed = count = 0
    ap_free = True
    for x in range(p):
        for d in range(p):
            indices = [(x + j * d) % p for j in range(4)]
            vals = [v[j] for j in indices]
            terms = [1] * 16
            for mask in range(1, 16):
                bit = mask & -mask
                terms[mask] = terms[mask ^ bit] * vals[bit.bit_length() - 1]
            for mask, term in enumerate(terms):
                sums[mask] += term
            indicator = product_value(bits[j] for j in indices)
            count += indicator
            if d and indicator:
                ap_free = False
            mixed += vals[0] * bits[indices[1]] * bits[indices[2]] * vals[3]
    averages = [F(s, p ** (2 + mask.bit_count()))
                for mask, s in enumerate(sums)]
    assert all(averages[m] == 0 for m in range(16) if m.bit_count() in (1, 2))
    assert averages[7] == averages[14]
    assert averages[11] == averages[13]
    t, u, q = averages[7], averages[11], averages[15]
    m, count = F(mixed, p ** 4), F(count, p ** 2)
    assert count == alpha ** 4 + 2 * alpha * (t + u) + q
    assert m == 2 * alpha * u + q
    assert count - alpha ** 4 == m + 2 * alpha * t
    if ap_free:
        assert count == alpha / p
    u2_4, u3_8 = moments(v)
    u2_4 /= p ** 4
    u3_8 /= p ** 8
    assert t * t <= b * u2_4
    assert m ** 4 <= alpha ** 4 * u3_8
    assert u2_4 ** 2 <= u3_8 <= b ** 4
    regime = ap_free and p * alpha ** 3 >= 2
    if regime:
        assert u3_8 >= alpha ** 12 / 256
    if n == 1:
        assert t * t == b * u2_4
        assert u3_8 == (alpha ** 4 - 8 * alpha ** 5 + 28 * alpha ** 6
                        - 44 * alpha ** 7 + 23 * alpha ** 8)
    return {"p": p, "size": n, "alpha": str(alpha), "ap_free": ap_free,
            "p_alpha_cubed": str(p * alpha ** 3), "in_regime": regime,
            "T": str(t), "mixed": str(m), "U2_fourth": str(u2_4),
            "U3_eighth": str(u3_8)}


def product_value(values):
    out = 1
    for value in values:
        out *= value
    return out


def general_mixed(f, middle):
    p = len(f)
    return F(sum(f[x] * middle[(x + d) % p] * middle[(x + 2*d) % p]
                 * f[(x + 3*d) % p] for x in range(p) for d in range(p)), p*p)


def check_general_functions():
    count = 0
    for f in product((-1, 0, 1), repeat=5):
        _, cube = moments(f)
        for middle in product((0, 1), repeat=5):
            m = general_mixed(f, middle)
            assert m ** 4 <= F(sum(middle), 5) ** 4 * cube
            count += 1
    return count


def check_counterexamples():
    for f, middle, expected_m, expected_cube in (
        ([1, 1, 0], [1, 1, 1], F(2, 3), F(8, 81)),
        ([1, 1, 1, 0], [1, 0, 1, 1], F(1, 2), F(41, 256)),
    ):
        m = general_mixed(f, middle)
        _, cube = moments(f)
        assert (m, cube) == (expected_m, expected_cube)
        assert m ** 4 > F(sum(middle), len(f)) ** 4 * cube
    v = [6, -1, -3, 2, -3, -1]
    t = F(sum(v[x] * v[(x+d) % 6] * v[(x+2*d) % 6]
              for x in range(6) for d in range(6)), 6 ** 5)
    b = F(sum(x*x for x in v), 6 ** 3)
    energy, _ = moments(v)
    energy /= 6 ** 4
    assert (t, b, energy) == (F(5, 54), F(5, 18), F(17, 648))
    assert t*t > b*energy
    g = [2, 1, 1, 1, 1]
    lam = F(sum(product_value(g[(x+j*d) % 5] for j in range(4))
                for x in range(5) for d in range(5)), 5**2 * 2**4)
    _, cube = moments(g)
    cube /= 2**8
    assert (lam, cube) == (F(7, 50), F(11, 625))
    assert lam**2 > cube


def check_complex_cs():
    """Floating-point conjugation check, separate from exact rational tests."""
    p = 7
    f = [0.2 + 0.3j, -0.4j, 0.5, -0.3 + 0.1j, 0.7j, 0.1, -0.2j]
    middle = [0.4j, 0.2, -0.5, 0.3 + 0.2j, 0.1j, -0.3, 0.7]
    kernel = [[f[(2*y-z) % p] * f[(2*z-y) % p] for z in range(p)]
              for y in range(p)]
    m = sum(middle[y] * middle[z] * kernel[y][z]
            for y in range(p) for z in range(p)) / p**2
    q = sum(abs(sum(kernel[y][z] * kernel[y][zz].conjugate()
                    for y in range(p)) / p)**2
            for z in range(p) for zz in range(p)) / p**2
    def parallelogram(h, k):
        return sum(f[x] * f[(x+h) % p].conjugate()
                   * f[(x+k) % p].conjugate() * f[(x+h+k) % p]
                   for x in range(p)) / p
    fs = [[parallelogram(h, k) for k in range(p)] for h in range(p)]
    factorized = sum(fs[2*h % p][-k % p] * fs[-h % p][2*k % p]
                     for h in range(p) for k in range(p)) / p**2
    cube = sum(abs(z)**2 for row in fs for z in row) / p**2
    norm = sum(abs(z)**2 for z in middle) / p
    assert abs(q - factorized) < 1e-12
    assert abs(m)**4 <= norm**4 * q + 1e-12
    assert q <= cube + 1e-12


def quadratic_moments(p, points, expected_cube):
    """All global polynomial quadratics: numerical check, not exact proof."""
    alpha = len(points) / p
    f = [int(x in points) - alpha for x in range(p)]
    phases = [cmath.exp(-2j * cmath.pi * k / p) for k in range(p)]
    spectra = [[abs(sum(f[x] * phases[(a*x*x+b*x) % p] for x in range(p)) / p)**2
                for b in range(p)] for a in range(p)]
    weights = [w for row in spectra for w in row]
    b = alpha*(1-alpha)
    assert abs(sum(weights) - p*b) < 1e-10
    assert abs(sum(w*w for w in weights) - (2*b*b-b*(1-3*b)/p)) < 1e-10
    total_energy = sum(abs(sum(row[k]*phases[k*h % p] for k in range(p)))**4
                       for row in spectra for h in range(p)) / p
    diagonal = sum(abs(sum(f[x]**2 * phases[k*x % p] for x in range(p)) / p)**4
                   for k in range(p))
    residual = float(expected_cube) - diagonal/p - (total_energy-b**4)
    assert abs(residual) < 1e-10
    return {"maximum_correlation": max(weights)**0.5,
            "all_derivative_mass_identity_residual": residual, "tolerance": 1e-10}


def check_localization():
    p, m, points = 101, 10, {0, 1, 3, 9}
    bits = [int(x in points) for x in range(p)]
    alpha, lam = F(len(points), p), F(m, p)
    energy, cube = moments(bits)
    assert energy >= alpha**4 / (2*lam)
    assert cube >= alpha**8 / (16*lam**4)
    buckets = {}
    for digits in product(range(3), repeat=3):
        radius = sum(x*x for x in digits)
        buckets.setdefault(radius, []).append(sum(x*6**i for i, x in enumerate(digits)))
    sphere = max(buckets.values(), key=len)
    assert len(sphere) >= F(3**3, 3*2**2+1)
    assert all(a == c for a in sphere for c in sphere
               if (a+c) % 2 == 0 and (a+c)//2 in sphere)
    assert 2*6**3 < 653
    assert all(a == c for a in sphere for c in sphere
               if ((a+c)*pow(2, -1, 653)) % 653 in sphere)
    return {"support_energy_example": {"p": p, "interval_length": m,
                                       "A": sorted(points)},
            "sphere_example": {"p": 653, "base": 6, "dimension": 3,
                               "A": sorted(sphere)},
            "scope": "construction sanity checks; asymptotic obstruction proved algebraically"}


def main():
    tested = ap_free = regimes = 0
    for p in (5, 7, 11):
        for bits in product((0, 1), repeat=p):
            result = check_indicator(bits)
            tested += 1
            ap_free += result["ap_free"] and result["size"] > 0
            regimes += result["in_regime"]
    for p in (13, 17):
        check_indicator([int(x == 0) for x in range(p)])
    witness = check_indicator([int(x in REGIME_SET) for x in range(101)])
    assert witness["ap_free"] and witness["in_regime"]
    witness["A"] = REGIME_SET
    witness["numerical_quadratic_scan"] = quadratic_moments(
        101, REGIME_SET, F(witness["U3_eighth"]))
    general = check_general_functions()
    check_counterexamples()
    check_complex_cs()
    localization = check_localization()
    print(json.dumps({
        "status": "phase 2 finite checks passed; no asymptotic density bound proved",
        "exact_exhaustive_indicator_subsets": tested,
        "nonempty_4ap_free_subsets_in_exhaustive_scan": ap_free,
        "eligible_sets_in_exhaustive_scan": regimes,
        "extra_singleton_groups": [13, 17],
        "exact_general_endpoint_middle_pairs": general,
        "eligible_4ap_free_witness": witness,
        "rejected_extensions": ["mixed estimate on Z3", "mixed estimate on Z4",
                                "cubic estimate on Z6", "Lambda4(g) <= U3(g)^4"],
        "complex_cs_check": "floating point, tolerance 1e-12",
        "localization_checks": localization,
        "external_dependencies": [],
    }, indent=2))


if __name__ == "__main__":
    main()
