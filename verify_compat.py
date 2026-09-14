"""Checks for COMPATIBILITY.md. Identities and small-set variance only."""

from fractions import Fraction as F
from itertools import combinations
import json

REGIME = [
    0, 20, 22, 25, 30, 32, 33, 34, 37, 38, 39, 48, 49, 52,
    53, 54, 58, 59, 78, 79, 81, 84, 88, 90, 93, 94, 95, 97,
]


def fiber_moments(p, A):
    A = set(A)
    a = F(len(A), p)
    rows = []
    for d in range(1, p):
        q = t = 0
        for x in range(p):
            if (x + d) % p in A and (x + 2 * d) % p in A:
                q += 1
                if x in A:
                    t += 1
        if q:
            rows.append((F(q), F(t), F(t, q)))
    Qstar = sum((r[0] for r in rows), F(0)) / p
    if Qstar == 0:
        return None
    mean_r = sum((r[0] * r[2] for r in rows), F(0)) / (p * Qstar)
    var = sum((r[0] * (r[2] - a) ** 2 for r in rows), F(0)) / (p * Qstar)
    S = (sum((r[1] for r in rows), F(0)) / p + a) / p
    # First-moment identity if r were identically a: Sigma_A predicted
    pred_S = a / p + a * (a ** 2 - a / p)
    return {
        "p": p,
        "size": len(A),
        "a": str(a),
        "mean_r": str(mean_r),
        "mean_r_minus_a": str(mean_r - a),
        "var_r": str(var),
        "var_over_a2": str(var / a ** 2),
        "S": str(S),
        "center_S": str(pred_S),
        "n_fib": len(rows),
        "r_constant": len({r[2] for r in rows}) == 1,
    }


def apfree(p, pts):
    A = set(pts)
    for d in range(1, p):
        for x in range(p):
            if (
                x in A
                and (x + d) % p in A
                and (x + 2 * d) % p in A
                and (x + 3 * d) % p in A
            ):
                return False
    return True


def min_var(p):
    best = None
    n = 0
    for k in range(3, p):
        for pts in combinations(range(p), k):
            if not apfree(p, pts):
                continue
            n += 1
            st = fiber_moments(p, pts)
            if st is None:
                continue
            v = F(st["var_r"])
            if best is None or v < best[0]:
                best = (v, pts, st)
    return n, best


def main():
    z7 = fiber_moments(7, [0, 1, 2, 4])
    z11 = fiber_moments(11, [0, 1, 2, 4, 7])
    z13 = fiber_moments(13, [0, 1, 3, 9])
    z101 = fiber_moments(101, REGIME)
    n7, b7 = min_var(7)
    n11, b11 = min_var(11)
    out = {
        "status": "compatibility checks passed; local r4 target not proved",
        "Z7_constant_r": z7,
        "Z11_minvar_set": z11,
        "Z13_flat": z13,
        "Z101_regime": z101,
        "Z7_4apfree_count": n7,
        "Z7_min_var": str(b7[0]) if b7 else None,
        "Z11_4apfree_count": n11,
        "Z11_min_var": str(b11[0]) if b11 else None,
        "Z11_min_var_set": list(b11[1]) if b11 else None,
    }
    assert z7["r_constant"] is True
    assert F(z7["var_r"]) == F(1, 196)
    assert F(z11["var_over_a2"]) == F(1, 100)
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
