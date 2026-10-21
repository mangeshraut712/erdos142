"""Run: python3 verify_two_run_20261002.py. Check for MIXED_FACTORS_20261002.md
section 2: a frequency whose base-16 orbit sits near k1/15 on the low half
and near k2/15 on the high half has small orbit sum Psi, but large
single-centre sum, and its Fourier coefficient against the symmetric
candidate decays. Exact rational orbits; Fourier coefficients by the
dynamic program of verify_rational_classes_20261002.py, with real x."""
from fractions import Fraction
import cmath
import json
import math
import random

from verify_symmetric_candidate_20261002 import build_T, greedy_4ap_free, log_mult

MOD = 15


def frac_dist(q):
    f = q - math.floor(q)
    return min(f, 1 - f)


def orbit(x, r):
    return [(x*16**i) % 1 for i in range(r)]


def psi(x, r):
    return sum(float(frac_dist(15*p))**2 for p in orbit(x, r)[:-1])


def single_centre(x, r, grid=3000):
    pts = [float(p) for p in orbit(x, r)]
    return min(sum(min(abs(p - g/grid), 1 - abs(p - g/grid))**2 for p in pts)
               for g in range(grid))


def coefficient(r, tset, x):
    layer = {(0, 0, 0): 1 + 0j}
    for i in range(r):
        w = cmath.exp(2j*math.pi*float((x*16**i) % 1))
        powers = (1, w, w*w, w*w*w)
        nxt = {}
        for (n0, n1, n2), amp in layer.items():
            for d, key in enumerate(((n0 + 1, n1, n2), (n0, n1 + 1, n2),
                                     (n0, n1, n2 + 1), (n0, n1, n2))):
                nxt[key] = nxt.get(key, 0) + amp*powers[d]
        layer = nxt
    return sum(amp for (n0, n1, n2), amp in layer.items()
               if (n0, n1, n2, r - n0 - n1 - n2) in tset)/4**r


def main():
    rng = random.Random(5)
    rows = []
    for r in (16, 24, 32, 40):
        B = greedy_4ap_free(3*r + 1, rng)
        T = build_T(r, B)
        tset = set(T)
        a = sum(math.exp(log_mult(n) - r*math.log(4)) for n in T)
        for k1, k2 in ((1, 1), (1, 2), (3, 7), (0, 5)):
            x = Fraction(k2, MOD) + Fraction(k1 - k2, MOD)/16**(r//2)
            row = {"r": r, "k1": k1, "k2": k2, "psi": psi(x, r),
                   "single_centre": single_centre(x, r),
                   "coef_over_a": abs(coefficient(r, tset, x))/a}
            rows.append(row)
            print(row, flush=True)
            assert row["psi"] <= 0.5
            if k1 != k2:
                d = frac_dist(Fraction(k1 - k2, MOD))
                assert row["single_centre"] >= 0.9*r*float(d/2)**2
    fast = [x["coef_over_a"] for x in rows
            if (x["k1"], x["k2"]) in ((3, 7), (0, 5)) and x["r"] == 40]
    assert max(fast) < 1e-6
    with open("two_run_verification_20261002.json", "w") as fh:
        json.dump({"rows": rows, "target_proved": False}, fh, indent=1)


if __name__ == "__main__":
    main()
