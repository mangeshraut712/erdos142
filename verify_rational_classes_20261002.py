"""Run: python3 verify_rational_classes_20261002.py. Checks for
RATIONAL_CLASSES_20261002.md: for the symmetric candidate A (greedy B),
the energy of the partition by X(u) mod q, split into the mod-15 part
(frequencies h with q | 15h) and the rest. Exact Fourier coefficients
E[1_A e(hX/q)] by a dynamic program over partial count vectors."""
import cmath
import json
import math
import random

from verify_symmetric_candidate_20261002 import build_T, greedy_4ap_free, log_mult

QS = (7, 13, 17, 51)
RS = (16, 24, 32, 40)


def coefficient(r, tset, h, q):
    """sum over u with n(u) in T of e(hX(u)/q), divided by 4^r."""
    layer = {(0, 0, 0): 1 + 0j}
    for i in range(r):
        w = cmath.exp(2j*math.pi*h*pow(16, i, q)/q)
        powers = (1, w, w*w, w*w*w)
        nxt = {}
        for (n0, n1, n2), amp in layer.items():
            for d, key in enumerate(((n0 + 1, n1, n2), (n0, n1 + 1, n2),
                                     (n0, n1, n2 + 1), (n0, n1, n2))):
                nxt[key] = nxt.get(key, 0) + amp*powers[d]
        layer = nxt
    total = 0j
    for (n0, n1, n2), amp in layer.items():
        if (n0, n1, n2, r - n0 - n1 - n2) in tset:
            total += amp
    return total/4**r


def kappa(h, q, grid=20000):
    """min over gamma of the mean of ||16^i h/q - gamma||^2 over one period of i."""
    orbit, x = [], h % q
    while x not in orbit:
        orbit.append(x)
        x = 16*x % q
    best = 1.0
    for g in range(grid):
        gamma = g/grid
        val = sum(min(abs(o/q - gamma) % 1, 1 - abs(o/q - gamma) % 1)**2
                  for o in orbit)/len(orbit)
        best = min(best, val)
    return best


def dist(x):
    x %= 1
    return min(x, 1 - x)


def check_orbit_bound(rng, trials=300, r=12, grid=4000):
    """min_gamma sum_i ||16^i x-gamma||^2 >= (1/4) sum_{i<r-1} ||15*16^i x||^2."""
    worst = 0.0
    for _ in range(trials):
        x = rng.random() if rng.random() < 0.5 else \
            rng.randrange(15)/15 + rng.uniform(-1, 1)*16.0**(-rng.randrange(1, r))
        pts = [(x*16**i) % 1 for i in range(r)]
        lhs = min(sum(dist(p - g/grid)**2 for p in pts) for g in range(grid))
        rhs = sum(dist(15*p)**2 for p in pts[:-1])/4
        assert lhs >= rhs - 1e-3/grid
        if lhs > 0:
            worst = max(worst, rhs/lhs)
    return worst


def main():
    rng = random.Random(142)
    kappas = {q: min(kappa(h, q) for h in range(1, q) if (15*h) % q)
              for q in QS}
    print("kappa_min", kappas, flush=True)
    assert abs(kappas[17] - (1/34)**2) < 1e-6
    for q in QS:
        assert kappas[q] >= 1/(4*q*q) - 1e-9
    worst = check_orbit_bound(rng)
    print("orbit bound worst ratio", worst, flush=True)
    rows = []
    for r in RS:
        B = greedy_4ap_free(3*r + 1, rng)
        T = build_T(r, B)
        tset = set(T)
        a = sum(math.exp(log_mult(n) - r*math.log(4)) for n in T)
        assert abs(coefficient(r, tset, 0, 7) - a) < 1e-9*a
        for q in QS:
            e15 = rest = 0.0
            worst_rest = 0.0
            for h in range(1, q):
                c = abs(coefficient(r, tset, h, q))**2/a**2
                if (15*h) % q == 0:
                    e15 += c
                else:
                    rest += c
                    worst_rest = max(worst_rest, c)
            row = {"r": r, "q": q, "density": a, "mod15_part": e15,
                   "rest": rest, "worst_rest_coefficient": worst_rest}
            rows.append(row)
            print(row, flush=True)
    with open("rational_classes_verification_20261002.json", "w") as fh:
        json.dump({"kappa_min": kappas, "rows": rows, "target_proved": False},
                  fh, indent=1)


if __name__ == "__main__":
    main()
