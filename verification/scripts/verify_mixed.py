# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Mangesh Raut

"""Exact checks for MIXED_INCREMENT.md. Identities and witnesses only.

Finite output is not an asymptotic proof. Standard library only.
"""

from fractions import Fraction as F
import json

REGIME = [
    0, 20, 22, 25, 30, 32, 33, 34, 37, 38, 39, 48, 49, 52,
    53, 54, 58, 59, 78, 79, 81, 84, 88, 90, 93, 94, 95, 97,
]


def fibers(p, A):
    A = set(A)
    alpha = F(len(A), p)
    rows = []
    offdiag_4ap = 0
    S_off = 0
    for d in range(1, p):
        q = t = both = 0
        for x in range(p):
            if (x + d) % p in A and (x + 2 * d) % p in A:
                q += 1
                left = x in A
                right = (x + 3 * d) % p in A
                if left:
                    t += 1
                if left and right:
                    both += 1
                    offdiag_4ap += 1
        if q:
            r = F(t, q)
            mq = alpha ** 2 - 2 * alpha * r
            rows.append({"d": d, "q": q, "t": t, "both": both, "r": r, "mq": mq})
            S_off += t
    S = (F(S_off, p) + alpha) / p
    M = alpha / p - 2 * alpha * S + alpha ** 4
    return {
        "p": p,
        "size": len(A),
        "alpha": alpha,
        "p_alpha3": p * alpha ** 3,
        "offdiag_4ap": offdiag_4ap,
        "M": M,
        "M_over_a4": M / alpha ** 4,
        "S": S,
        "rows": rows,
    }


def identity_ok(st):
    alpha = st["alpha"]
    p = st["p"]
    # Re-sum physical M from fibers plus diagonal.
    Q = sum((F(row["q"], p) for row in st["rows"]), F(0)) / p
    M_fib = sum((F(row["q"], p) * row["mq"] for row in st["rows"]), F(0)) / p
    M_diag = alpha * (1 - alpha) ** 2 / p
    return M_fib + M_diag == st["M"] and st["offdiag_4ap"] == 0 and Q == alpha ** 2 - alpha / p


def summarize(st):
    alpha = st["alpha"]
    rows = st["rows"]
    qs = sum((F(r["q"]) for r in rows), F(0))
    wr = sum((F(r["q"]) * r["r"] for r in rows), F(0)) / qs
    return {
        "p": st["p"],
        "size": st["size"],
        "alpha": str(st["alpha"]),
        "p_alpha3": str(st["p_alpha3"]),
        "offdiag_4ap": st["offdiag_4ap"],
        "M": str(st["M"]),
        "M_over_a4": str(st["M_over_a4"]),
        "n_pos_q": len(rows),
        "n_r_gt_half_a": sum(1 for r in rows if r["r"] > alpha / 2),
        "n_r_gt_a": sum(1 for r in rows if r["r"] > alpha),
        "max_r": str(max(r["r"] for r in rows)),
        "weighted_r": str(wr),
        "max_q": max(r["q"] for r in rows),
        "max_q_among_r_gt_a": max((r["q"] for r in rows if r["r"] > alpha), default=None),
        "identity_ok": identity_ok(st),
        "all_r_le_a": all(r["r"] <= alpha for r in rows),
        "center_model_M": str(
            alpha * (1 - alpha) ** 2 / st["p"] - alpha ** 4 + alpha ** 3 / st["p"]
        ),
    }


def main():
    z7 = fibers(7, [0, 1, 2, 4])
    z11 = fibers(11, [6, 8, 9, 10])
    z13 = fibers(13, [0, 1, 3, 9])
    z101 = fibers(101, REGIME)
    out = {
        "status": "mixed-form obstruction checks passed; local r4 target not proved",
        "Z7": summarize(z7),
        "Z11_wrap": summarize(z11),
        "Z13_flat": summarize(z13),
        "Z101_regime": summarize(z101),
    }
    assert out["Z7"]["identity_ok"] and out["Z7"]["all_r_le_a"]
    assert F(out["Z7"]["M_over_a4"]) < 0
    assert out["Z101_regime"]["identity_ok"]
    assert F(out["Z101_regime"]["p_alpha3"]) > 2
    assert F(out["Z101_regime"]["M_over_a4"]) < F(-1, 4)
    assert out["Z101_regime"]["offdiag_4ap"] == 0
    # Center model: r=a gives M = a/p - a^4, which is <= -7/8 a^4 under p a^3 >= 8.
    a = F(28, 101)
    center = a * (1 - a) ** 2 / 101 - a ** 4 + a ** 3 / 101
    assert center < -a ** 4 / 4
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
