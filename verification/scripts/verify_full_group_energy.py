# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Mangesh Raut

"""Finite checks for FULL_GROUP_ENERGY_AUDIT.md (Omega = Z_p case of the energy theorem).

Exact rationals for all factor energies and identities; floating point only for
Fourier coefficients, reported separately with tolerances. Standard library only.
"""

from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import cmath
import json
import math
import random

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"

REGIME = [0, 20, 22, 25, 30, 32, 33, 34, 37, 38, 39, 48, 49, 52,
          53, 54, 58, 59, 78, 79, 81, 84, 88, 90, 93, 94, 95, 97]
FLOAT_TOL = 1e-9


def fhat(bits, p):
    a = sum(bits) / p
    f = [b - a for b in bits]
    return [sum(f[x] * cmath.exp(-2j * math.pi * xi * x / p) for x in range(p)) / p
            for xi in range(p)]


def cells_rank1(p, xi, t):
    out = {}
    for x in range(p):
        th = F((xi * x) % p, p) - t
        th -= math.floor(th)
        out.setdefault(int(4 * th), []).append(x)
    return out


def var_and_num(bits, p, cells):
    """Var(E(f|F)) and sum_V |<f,1_V>|^2, both exact."""
    a = F(sum(bits), p)
    var = num = F(0)
    for V in cells.values():
        d = F(sum(bits[x] for x in V)) - a * len(V)
        var += d * d / (p * len(V))
        num += d * d / (p * p)
    return var, num


def rank1_scan(bits, p, xi):
    """Exact max_t and mean_t over the 4p generic rotation intervals."""
    best, tot_var, tot_num = F(-1), F(0), F(0)
    for k in range(4 * p):
        cells = cells_rank1(p, xi, F(2 * k + 1, 8 * p))
        v, n = var_and_num(bits, p, cells)
        best = max(best, v)
        tot_var += v
        tot_num += n
    return best, tot_var / (4 * p), tot_num / (4 * p)


def w(m):
    return 0.25 if m == 0 else 4 * math.sin(math.pi * m / 4) ** 2 / (math.pi ** 2 * m * m)


def apfree(p, A, k):
    A = set(A)
    return not any(all((x + j * d) % p in A for j in range(1, k))
                   for d in range(1, p) for x in A)


def check_rank1(out):
    p = 101
    bits = [1 if x in REGIME else 0 for x in range(p)]
    a = F(28, 101)
    fh = fhat(bits, p)
    M = 4000
    tail = 8 / (math.pi ** 2 * M) * max(abs(c) for c in fh) ** 2
    rows = []
    min_ratio = None
    sup_var = F(0)
    for xi in range(1, 51):
        best, mean_var, mean_num = rank1_scan(bits, p, xi)
        sup_var = max(sup_var, best)
        lat = sum(w(m) * abs(fh[(m * xi) % p]) ** 2 for m in range(-M, M + 1) if m)
        assert abs(float(mean_num) - lat) <= tail + FLOAT_TOL, xi
        lb = (16 / math.pi ** 2) / (1 + 4 / p) * abs(fh[xi]) ** 2
        assert float(best) >= lb - FLOAT_TOL and float(mean_var) >= lb - FLOAT_TOL, xi
        ratio = float(best) / lb
        min_ratio = ratio if min_ratio is None else min(min_ratio, ratio)
        if xi <= 3:
            rows.append({"xi": xi, "mean_t_numerator": str(mean_num),
                         "lattice_formula_float": lat, "max_t_var": str(best),
                         "lower_bound_float": lb})
    out["rank1_rotation_identity"] = {
        "p": p, "set": "Z101 size-28 4AP-free witness", "characters_checked": 50,
        "truncation": M, "tail_bound": tail, "sample_rows": rows,
        "min_ratio_maxVar_over_lower_bound": min_ratio,
        "sup_rank1_var_over_a2": str(sup_var / a ** 2),
        "cutoff_eligible": p >= 8 * (F(101, 28)) ** 3,
    }


def check_trivial_regime(out):
    rows = []
    for (p, s) in ((61, 3), (101, 4), (251, 4), (1021, 5)):
        keys = {tuple(int(4 * F((pow(4, j, p) * x) % p, p)) for j in range(s))
                for x in range(p)}
        assert 4 ** s >= p and len(keys) == p
        rows.append({"p": p, "s": s, "cells": len(keys), "all_singletons": True})
    out["trivial_regime_digit_factor"] = rows


def check_affine(out, rng):
    q = 31
    while True:
        A = sorted(rng.sample(range(q), 6))
        if apfree(q, A, 4):
            break
    results = []
    for (u, v) in ((7, 11), (30, 3), (2, 0)):
        A2 = sorted((u * x + v) % q for x in A)
        b1 = [1 if x in A else 0 for x in range(q)]
        b2 = [1 if x in A2 else 0 for x in range(q)]
        s1 = max(rank1_scan(b1, q, xi)[0] for xi in range(1, q))
        s2 = max(rank1_scan(b2, q, xi)[0] for xi in range(1, q))
        assert s1 == s2
        results.append({"u": u, "v": v, "sup": str(s1)})
    out["affine_invariance_rank1_sup"] = {"p": q, "A": A, "images": results}


def check_thinning(out, rng):
    q = 31
    rows = []
    for theta in (F(1, 3), F(1, 2), F(4, 5)):
        S = sorted(rng.sample(range(q), 8))
        cells = cells_rank1(q, 1, F(0))
        bS = [1 if x in S else 0 for x in range(q)]
        varS, _ = var_and_num(bS, q, cells)
        EV = F(0)
        for k in range(len(S) + 1):
            for sub in combinations(S, k):
                bA = [1 if x in sub else 0 for x in range(q)]
                EV += theta ** k * (1 - theta) ** (len(S) - k) * var_and_num(bA, q, cells)[0]
        bracket = sum(F(sum(bS[x] for x in V), q * len(V)) for V in cells.values()) - F(len(S), q * q)
        pred = theta ** 2 * varS + theta * (1 - theta) * bracket
        assert EV == pred and bracket >= 0 and EV >= theta ** 2 * varS
        rows.append({"theta": str(theta), "S": S, "E_Var_A": str(EV),
                     "theta2_Var_S": str(theta ** 2 * varS), "bracket": str(bracket)})
    out["thinning_identity"] = rows


def check_3apfree_energy(out, rng):
    p = 101
    best = []
    for _ in range(3000):
        order = list(range(51))
        rng.shuffle(order)
        cur = []
        for x in order:
            if all((2 * y - x) not in cur and (2 * x - y) not in cur
                   and not ((x + y) % 2 == 0 and (x + y) // 2 in cur) for y in cur):
                cur.append(x)
        if len(cur) > len(best):
            best = sorted(cur)
    A = best
    assert apfree(p, A, 3)
    bits = [1 if x in A else 0 for x in range(p)]
    a = len(A) / p
    assert p * a * a >= 2
    fh = fhat(bits, p)
    lhs = sum(fh[xi] ** 2 * fh[(-2 * xi) % p] for xi in range(p))
    assert abs(lhs.real - (a / p - a ** 3)) < FLOAT_TOL and abs(lhs.imag) < FLOAT_TOL
    T2 = [xi for xi in range(1, p) if abs(fh[(2 * xi) % p]) >= a * a / 4]
    energy = sum(abs(fh[xi]) ** 2 for xi in T2)
    assert energy >= a * a / 8 and len(T2) <= 16 / a ** 3
    v, _ = var_and_num(bits, p, cells_rank1(p, 1, F(0)))
    assert v >= F(1, 4) * F(len(A), p) ** 2
    gm = max(abs(fh[xi]) for xi in range(1, p))
    assert gm >= (a * a - 1 / p) / (1 - a) - FLOAT_TOL
    out["threeAPfree_level_a2_energy"] = {
        "p": p, "A": A, "a": a, "p_a2": p * a * a,
        "identity_a_over_p_minus_a3": a / p - a ** 3, "fourier_sum": lhs.real,
        "T_prime_size": len(T2), "bound_16_a_minus3": 16 / a ** 3,
        "energy_on_T_prime": energy, "a2_over_8": a * a / 8,
        "interval_supported_rank1_var_over_a2": float(v) / a ** 2,
        "max_fhat_over_a2": gm / a ** 2,
    }


def main():
    rng = random.Random(7)
    out = {"status": "finite diagnostics for FULL_GROUP_ENERGY_AUDIT.md; not an asymptotic proof"}
    check_rank1(out)
    check_trivial_regime(out)
    check_affine(out, rng)
    check_thinning(out, rng)
    check_3apfree_energy(out, rng)
    out["all_checks_passed"] = True
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with (RESULTS_DIR / "full_group_energy_verification.json").open("w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
