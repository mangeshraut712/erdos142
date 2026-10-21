#!/usr/bin/env python3
"""Explicit Selberg/Vaaler constants used in MIXED_FACTORS sections 7-8.

For an arc I=[alpha,beta] and degree N, with Vaaler's polynomial V_N and
Fejer kernel Delta_{N+1},
  S^{+-}(x) = (beta-alpha) + V(x-beta) - V(x-alpha)
              +- (Delta(x-beta) + Delta(x-alpha)) / (2N+2).
Checks: S^- <= 1_I <= S^+ on a grid, |S^{+-}| <= 3, the integral of
S^+ - S^- equals 2/(N+1), every Fourier coefficient of S^+ - S^- is at most
2/(N+1), and the arithmetic sum over q | t stays at most 2/(N+1) + 4/q.
Also checks the l^1 Fourier mass of interval indicators on Z_q.
Standard library only.
"""

import cmath
import json
import math
import random


def vaaler_coeffs(n):
    out = []
    for k in range(1, n + 1):
        u = k / (n + 1)
        j = math.pi * u * (1 - u) / math.tan(math.pi * u) + u
        out.append(-j / (math.pi * k))
    return out


def vaaler(coeffs, x):
    return sum(c * math.sin(2 * math.pi * (k + 1) * x) for k, c in enumerate(coeffs))


def fejer(k, x):
    s = math.sin(math.pi * x)
    if abs(s) < 1e-12:
        return float(k)
    return math.sin(math.pi * k * x) ** 2 / (k * s * s)


def indicator(alpha, beta, x):
    y = (x - alpha) % 1.0
    return 1.0 if y < (beta - alpha) else 0.0


def selberg_pair(coeffs, n, alpha, beta, x):
    base = (beta - alpha) + vaaler(coeffs, x - beta) - vaaler(coeffs, x - alpha)
    corr = (fejer(n + 1, x - beta) + fejer(n + 1, x - alpha)) / (2 * n + 2)
    return base - corr, base + corr


def check_sandwich(rng, ns=(4, 8, 16, 32), arcs=6, grid=1500):
    worst_violation = 0.0
    worst_sup = 0.0
    worst_int_err = 0.0
    for n in ns:
        coeffs = vaaler_coeffs(n)
        for _ in range(arcs):
            alpha = rng.random()
            length = rng.uniform(0.01, 0.5)
            beta = alpha + length
            total = 0.0
            for g in range(grid):
                x = (g + 0.5) / grid + 1e-7
                lo, hi = selberg_pair(coeffs, n, alpha, beta, x)
                ind = indicator(alpha, beta, x)
                worst_violation = max(worst_violation, lo - ind, ind - hi)
                worst_sup = max(worst_sup, abs(lo), abs(hi))
                total += (hi - lo) / grid
            worst_int_err = max(worst_int_err, abs(total - 2 / (n + 1)))
    assert worst_violation <= 1e-9, worst_violation
    assert worst_sup <= 3.0, worst_sup
    assert worst_int_err <= 1e-6, worst_int_err
    return worst_violation, worst_sup, worst_int_err


def difference_coeff(n, alpha, beta, t):
    """Fourier coefficient of S^+ - S^- at t (exact formula)."""
    if abs(t) > n:
        return 0.0
    fej = 1 - abs(t) / (n + 1)
    return abs(fej * (cmath.exp(-2j * math.pi * t * beta)
                      + cmath.exp(-2j * math.pi * t * alpha))) / (n + 1)


def numeric_coeff(coeffs, n, alpha, beta, t, grid=4096):
    acc = 0j
    for g in range(grid):
        x = g / grid
        lo, hi = selberg_pair(coeffs, n, alpha, beta, x)
        acc += (hi - lo) * cmath.exp(-2j * math.pi * t * x)
    return abs(acc / grid)


def check_coefficients(rng, ns=(8, 16, 32), qs=(2, 3, 5, 7, 12)):
    worst_formula_err = 0.0
    worst_ratio = 0.0
    worst_arith = 0.0
    for n in ns:
        coeffs = vaaler_coeffs(n)
        alpha = rng.random()
        beta = alpha + rng.uniform(0.05, 0.4)
        for t in range(-n - 1, n + 2):
            exact = difference_coeff(n, alpha, beta, t)
            num = numeric_coeff(coeffs, n, alpha, beta, t)
            worst_formula_err = max(worst_formula_err, abs(exact - num))
            worst_ratio = max(worst_ratio, exact * (n + 1) / 2)
        for q in qs:
            s = sum(difference_coeff(n, alpha, beta, t)
                    for t in range(-n, n + 1) if t % q == 0)
            worst_arith = max(worst_arith, s / (2 / (n + 1) + 4 / q))
    assert worst_formula_err <= 1e-9, worst_formula_err
    assert worst_ratio <= 1.0 + 1e-12
    assert worst_arith <= 1.0 + 1e-12
    return worst_formula_err, worst_ratio, worst_arith


def zq_l1(q, length, start):
    total = 0.0
    for t in range(q):
        c = sum(cmath.exp(-2j * math.pi * t * ((start + l) % q) / q)
                for l in range(length)) / q
        total += abs(c)
    return total


def check_zq(qs=(3, 7, 17, 64, 255, 1024)):
    worst = 0.0
    for q in qs:
        for length in sorted({1, max(1, q // 3), max(1, q // 2), q - 1}):
            val = zq_l1(q, length, 0)
            worst = max(worst, val / (2 + math.log(q)))
    assert worst <= 1.0, worst
    return worst


def main():
    rng = random.Random(20261002)
    viol, sup, interr = check_sandwich(rng)
    ferr, ratio, arith = check_coefficients(rng)
    zq = check_zq()
    out = {
        "sandwich_max_violation": viol,
        "sup_abs_S": sup,
        "integral_error": interr,
        "coefficient_formula_error": ferr,
        "max_coeff_over_2_by_N_plus_1": ratio,
        "max_arith_sum_over_bound": arith,
        "zq_l1_over_2_plus_log_q": zq,
        "target_proved": False,
    }
    print(out)
    with open(Path(__file__).resolve().parents[1] / "results" / "selberg_constants_verification_20261002.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
