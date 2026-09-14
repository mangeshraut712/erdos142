"""Offline finite checks of auxiliary identities, not a proof of Erdos 142.

Python standard library only. All exhaustive assertions use exact rational
arithmetic. The final Fourier probability check uses floating point and is
explicitly reported as such; its radical values are proved in the write-up.
"""

from fractions import Fraction as F
from itertools import product
from math import cos, sin, pi, sqrt
import json


def mean(values):
    values = list(values)
    return sum(values, F(0)) / len(values)


def check_atoms(bits):
    p = len(bits)
    alpha = F(sum(bits), p)
    f = [x - alpha for x in bits]
    a, b = 1 - 2 * alpha, alpha * (1 - alpha)
    for h in range(p):
        shifted = [f[(x + h) % p] for x in range(p)]
        g = [f[x] * shifted[x] for x in range(p)]
        c = mean(g)
        pair = alpha * alpha + c
        q, z = alpha - pair, 1 - 2 * alpha + pair
        assert max(F(0), 2 * alpha - 1) <= pair <= alpha
        assert all(v * v == a * v + b for v in f)
        assert all(g[x] ** 2 == a * a * g[x]
                   + a * b * (f[x] + shifted[x]) + b * b
                   for x in range(p))
        if b + c == 0:
            # Empty/full sets or the complementary pair at alpha = 1/2.
            assert all(g[x] == c for x in range(p))
            continue
        lam = a * c / (b + c)
        residual = [g[x] - c - lam * (f[x] + shifted[x])
                    for x in range(p)]
        assert mean(residual) == 0
        assert mean(residual[x] * f[x] for x in range(p)) == 0
        assert mean(residual[x] * shifted[x] for x in range(p)) == 0
        variance = mean(v * v for v in residual)
        assert variance == q * z * pair / (b + c)
        assert variance == (b - c) * (a * a * c + (b + c) ** 2) / (b + c)
        vals = {(0, 0): q * pair / (b + c),
                (0, 1): -z * pair / (b + c),
                (1, 0): -z * pair / (b + c),
                (1, 1): q * z / (b + c)}
        assert all(residual[x] == vals[bits[x], bits[(x + h) % p]]
                   for x in range(p))


def check_counting_and_energy(bits):
    p, n = len(bits), sum(bits)
    if n in (0, p):
        return False
    alpha, b = F(n, p), F(n * (p - n), p * p)
    f = [p * x - n for x in bits]  # Integer p times the balanced function.
    raw = [0, 0, 0, 0, 0]
    ap_free = True
    for x in range(p):
        for d in range(p):
            i, j, k = (x + d) % p, (x + 2 * d) % p, (x + 3 * d) % p
            indicator = bits[x] * bits[i] * bits[j] * bits[k]
            raw[0] += indicator
            if d and indicator:
                ap_free = False
            raw[1] += f[x] * f[i] * f[j]
            raw[2] += f[x] * f[i] * f[k]
            raw[3] += f[x] * f[i] * f[j] * f[k]
            raw[4] += f[x] * bits[i] * bits[j] * f[k]
    count, r, s, quad, endpoints = (
        F(raw[0], p ** 2), F(raw[1], p ** 5), F(raw[2], p ** 5),
        F(raw[3], p ** 6), F(raw[4], p ** 4))
    assert count == alpha ** 4 + 2 * alpha * (r + s) + quad
    assert count - alpha ** 4 == endpoints + 2 * alpha * r
    if ap_free:
        assert count == alpha / p

    corr = [sum(f[x] * f[(x + h) % p] for x in range(p))
            for h in range(p)]
    energy = F(sum(c * c for c in corr), p ** 7)  # U2^4
    cube = sum(sum(f[x] * f[(x + h) % p] * f[(x + d) % p]
                   * f[(x + h + d) % p] for x in range(p)) ** 2
               for h in range(p) for d in range(p))
    u3_8 = F(cube, p ** 12)
    assert r * r <= b * energy
    assert endpoints ** 4 <= alpha ** 4 * u3_8
    assert energy * energy <= u3_8
    if ap_free and p * alpha ** 3 >= 2:
        assert u3_8 >= alpha ** 12 / 256

    conv = [sum(corr[t] * corr[(h - t) % p] for t in range(p))
            for h in range(p)]
    positive = F(sum(corr[h] ** 2 * conv[h] for h in range(p)), p ** 14)
    fourth = F(sum(c * c for c in conv), p ** 15)  # sum_xi A_xi^4
    defect = energy ** 2 - positive
    assert defect >= fourth >= energy ** 3 / b ** 2
    assert defect / energy ** 2 >= F(2, 625) * (1 - b ** 2 / (p * energy))
    return ap_free


def residual(bits, h):
    p, alpha = len(bits), F(sum(bits), len(bits))
    f = [v - alpha for v in bits]
    c = mean(f[x] * f[(x + h) % p] for x in range(p))
    lam = (1 - 2 * alpha) * c / (alpha * (1 - alpha) + c)
    return [f[x] * f[(x + h) % p] - c - lam * (f[x] + f[(x + h) % p])
            for x in range(p)]


def check_counterexamples():
    difference_set = [int(x in (0, 1, 3, 9)) for x in range(13)]
    assert check_counting_and_energy(difference_set)
    points = [0, 1, 3, 9]
    assert sorted((x-y) % 13 for x in points for y in points if x != y) == list(range(1, 13))
    r = residual([1, 1, 0, 0, 0], 1)
    assert r == [F(v, 7) for v in (2, -2, 1, 1, -2)]
    assert mean(r[x] * r[(x + 2) % 5] for x in range(5)) == F(4, 245)
    r1, r2 = residual([1, 1, 0, 1, 0, 0, 0], 1), residual([1, 1, 0, 1, 0, 0, 0], 2)
    assert (r1[1], r1[2]) == (r1[2], r1[3]) == (F(-1, 5), F(-1, 5))
    assert r2[1] == F(2, 5) and r2[2] == F(1, 5)

    def spectrum(v):
        values = [abs(sum(v[x] * complex(cos(-2 * pi * k * x / 5),
                                        sin(-2 * pi * k * x / 5))
                          for x in range(5))) ** 4 for k in range(5)]
        return [w / sum(values) for w in values]

    nu1, nu2 = spectrum([9, -6, 4, 4, -6]), spectrum([-6, -6, 4, -6, -6])
    expected = [1 / 645, (161 - 72 * sqrt(5)) / 645,
                (161 + 72 * sqrt(5)) / 645, (161 + 72 * sqrt(5)) / 645,
                (161 - 72 * sqrt(5)) / 645]
    assert max(abs(x - y) for x, y in zip(nu1, expected)) < 1e-12
    assert abs(nu2[0] - 4 / 5) < 1e-12
    assert abs(sum(nu1[k] * nu1[-k % 5] for k in range(5)) - 41473 / 83205) < 1e-12

    g = [F(1), F(1, 2), F(1, 2), F(1, 2), F(1, 2)]
    progression = mean(g[x] * g[(x+d) % 5] * g[(x+2*d) % 5] * g[(x+3*d) % 5]
                       for x in range(5) for d in range(5))
    u3_8 = mean(mean(g[x] * g[(x+h) % 5] * g[(x+d) % 5] * g[(x+h+d) % 5]
                       for x in range(5)) ** 2 for h in range(5) for d in range(5))
    assert progression == F(7, 50) and u3_8 == F(11, 625)
    assert progression ** 2 > u3_8


def check_general_spectral_arrays():
    count = 0
    for p in (5, 7, 11):
        for half in product((0, 1, 2), repeat=(p - 1) // 2):
            if not any(half):
                continue
            v = [0] + list(half) + list(reversed(half))
            b, s = sum(v), sum(x*x for x in v)
            eplus = sum(v[k] ** 2 * sum(v[x] * v[(x-k) % p] for x in range(p))
                        for k in range(p))
            defect = s*s - eplus
            direct = F(sum(v[k] ** 2 * (v[x] - v[(x-k) % p]) ** 2
                           for k in range(p) for x in range(p)), 2)
            assert defect == direct
            assert F(defect, s*s) >= F(2, 625) * (1 - F(b*b, p*s))
            if F(defect, s*s) < F(2, 625):
                assert 1 - F(b*b, p*s) <= F(5, 4) * F(defect, s*s)
            count += 1
    return count


def main():
    subsets = ap_free_count = atom_subsets = 0
    for p in (5, 7, 11):
        for bits in product((0, 1), repeat=p):
            check_atoms(bits)
            ap_free_count += check_counting_and_energy(bits)
            subsets += 1
            atom_subsets += 1
    # Even groups exercise the complementary-pair Gram degeneration.
    for p in (4, 6):
        for bits in product((0, 1), repeat=p):
            check_atoms(bits)
            atom_subsets += 1
    check_counterexamples()
    general_arrays = check_general_spectral_arrays()
    print(json.dumps({
        "status": "finite auxiliary checks passed; no asymptotic theorem proved",
        "exact_counting_energy_subsets": subsets,
        "nonempty_proper_4ap_free_subsets": ap_free_count,
        "exact_four_atom_subsets": atom_subsets,
        "exact_general_even_spectral_arrays": general_arrays,
        "groups_for_counting": [5, 7, 11],
        "extra_groups_for_degeneracies": [4, 6],
        "spectral_kernel_counterexample": "float check of exact radical formulas, tolerance 1e-12",
        "external_dependencies": [],
    }, indent=2))


if __name__ == "__main__":
    main()
