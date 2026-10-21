"""Run: python3 verify_rank1_hostile_search_20261002.py. Finite diagnostics only.

Searches for 4-AP-free sets in Z_p whose best rank-one rotated-quarter
factor energy is small, and compares them with random sets of equal size.
Cells follow verify_full_group_hostile_20260914.cells exactly.
"""
from fractions import Fraction as Q
import json
import math
import random

from verify_full_group_hostile_20260914 import cells, energy

PRIMES_GREEDY = (211, 401, 797)
PRIMES_HOSTILE = (101, 151, 211)
SEEDS = 6
RANDOM_BASELINES = 8
HOSTILE_STEPS = 150


def creates_4ap(p, member, x):
    for h in range(1, p):
        for j in range(4):
            start = (x - j*h) % p
            if all(member[(start + i*h) % p] for i in range(4) if i != j):
                return True
    return False


def is_4ap_free(p, a_set):
    member = [False]*p
    for x in a_set:
        member[x] = True
    return not any(member[x] and member[(x+h) % p] and member[(x+2*h) % p]
                   and member[(x+3*h) % p]
                   for x in range(p) for h in range(1, p))


def greedy_4ap_free(p, rng):
    order = list(range(p))
    rng.shuffle(order)
    member = [False]*p
    for x in order:
        if not creates_4ap(p, member, x):
            member[x] = True
    return member


def best_rank1(p, member):
    """Return (scaled energy p^2*E as Fraction, xi, t) maximising over all
    nonzero xi and all 8p rotations, using cyclic prefix counts."""
    k = sum(member)
    best = (Q(-1), None, None)
    for xi in range(1, p):
        pos = [0]*p
        for x in range(p):
            if member[x]:
                pos[(xi*x) % p] = 1
        pref = [0]
        for v in pos:
            pref.append(pref[-1] + v)

        def count(lo, hi):
            lo_m, hi_m = lo % p, hi % p
            n = hi - lo
            if n <= 0:
                return 0, 0
            full, rem = divmod(n, p)
            c = full*k
            end = lo_m + rem
            if end <= p:
                c += pref[end] - pref[lo_m]
            else:
                c += pref[p] - pref[lo_m] + pref[end - p]
            return c, n

        best_float = -1.0
        best_t = None
        for t in range(8*p):
            s = 0.0
            for q in range(4):
                lo = -(-(t + 2*p*q) // 8)
                hi = -(-(t + 2*p*(q + 1)) // 8)
                c, n = count(lo, hi)
                if n:
                    s += c*c/n
            if s > best_float + 1e-12:
                best_float, best_t = s, t
        if best_t is not None:
            partition = cells(p, [(xi, best_t)])
            a_set = {x for x in range(p) if member[x]}
            e = energy(p, a_set, partition)
            if e > best[0]:
                best = (e, xi, best_t)
    return best


def random_member(p, k, rng):
    member = [False]*p
    for x in rng.sample(range(p), k):
        member[x] = True
    return member


def summary(p, member, rng):
    k = sum(member)
    a = Q(k, p)
    e, xi, t = best_rank1(p, member)
    baseline = sorted(float(best_rank1(p, random_member(p, k, rng))[0]/a**2)
                      for _ in range(RANDOM_BASELINES))
    return {
        "p": p, "size": k, "density": float(a),
        "rank1_energy_over_a2": float(e/a**2),
        "rank1_energy_over_a2_exact": str(e/a**2),
        "best_xi": xi, "best_t": t,
        "target_scale_1_over_log": 1/math.log(2/float(a)),
        "random_same_size_median": baseline[len(baseline)//2],
        "random_same_size_min": baseline[0],
    }


def hostile_search(p, rng):
    """Local search keeping 4-AP-freeness and size, minimising best rank-1."""
    member = greedy_4ap_free(p, rng)
    current = best_rank1(p, member)[0]
    for _ in range(HOSTILE_STEPS):
        inside = [x for x in range(p) if member[x]]
        out = rng.choice(inside)
        member[out] = False
        candidates = [y for y in range(p) if not member[y] and y != out
                      and not creates_4ap(p, member, y)]
        if not candidates:
            member[out] = True
            continue
        new = rng.choice(candidates)
        member[new] = True
        value = best_rank1(p, member)[0]
        if value <= current:
            current = value
        else:
            member[new] = False
            member[out] = True
    return member


def main():
    rng = random.Random(20261002)
    out = {"greedy": [], "hostile": []}
    for p in PRIMES_GREEDY:
        for _ in range(SEEDS if p < 500 else 2):
            member = greedy_4ap_free(p, rng)
            assert is_4ap_free(p, {x for x in range(p) if member[x]})
            out["greedy"].append(summary(p, member, rng))
    for p in PRIMES_HOSTILE:
        member = hostile_search(p, rng)
        a_set = {x for x in range(p) if member[x]}
        assert is_4ap_free(p, a_set)
        row = summary(p, member, rng)
        row["set"] = sorted(a_set)
        out["hostile"].append(row)
    rows = out["greedy"] + out["hostile"]
    out["min_ratio_to_random_median"] = min(
        r["rank1_energy_over_a2"]/r["random_same_size_median"] for r in rows)
    out["max_ratio_to_random_median"] = max(
        r["rank1_energy_over_a2"]/r["random_same_size_median"] for r in rows)
    out["open_statement_proved"] = False
    out["r4_target_proved"] = False
    with open("rank1_hostile_verification_20261002.json", "w") as fh:
        json.dump(out, fh, indent=1)
    for key in ("greedy", "hostile"):
        for r in out[key]:
            print(key, r["p"], r["size"], round(r["density"], 4),
                  "E/a^2=%.4f" % r["rank1_energy_over_a2"],
                  "rand_med=%.4f" % r["random_same_size_median"],
                  "1/log=%.3f" % r["target_scale_1_over_log"])
    print(json.dumps({k: out[k] for k in out if not isinstance(out[k], list)},
                     indent=1))


if __name__ == "__main__":
    main()
