"""Run: python3 verify_interval_window_energy_20261002.py. Finite diagnostics.

Rank-one window Omega={0,...,n-1} inside Z_p, p>3n prime. For 4-AP-free A
in Omega, compute the best single-character quarter-arc energy
Var_Omega(E(1_A|F))/a^2 over all nonzero characters and ROTATIONS rotations
per character, and compare with random subsets of Omega of equal size.
Coarse rotations give a lower bound for the true maximum, applied equally
to both sides of the comparison.
"""
import json
import math
import random

SIZES = (1000, 2000, 4000, 8000, 16000)
ROTATIONS = 64
BASELINES = 4


def next_prime(m):
    m += 1
    while any(m % d == 0 for d in range(2, int(m**0.5) + 1)):
        m += 1
    return m


def greedy_4ap_free(n, rng):
    order = list(range(n))
    rng.shuffle(order)
    member = bytearray(n)
    for x in order:
        bad = False
        for h in range(1, (n - 1)//3 + 1):
            for j in range(4):
                s = x - j*h
                if s < 0 or s + 3*h >= n:
                    continue
                if all(member[s + i*h] for i in range(4) if i != j):
                    bad = True
                    break
            if bad:
                break
        if not bad:
            member[x] = 1
    return [x for x in range(n) if member[x]]


def is_4ap_free(a_list):
    s = set(a_list)
    top = max(a_list)
    return not any(x + h in s and x + 2*h in s and x + 3*h in s
                   for x in a_list for h in range(1, (top - x)//3 + 1))


def best_energy(n, p, a_list):
    k = len(a_list)
    a = k/n
    best = 0.0
    for xi in range(1, (p + 1)//2):
        pos_a = [0]*p
        pos_o = [0]*p
        for x in range(n):
            pos_o[(xi*x) % p] = 1
        for x in a_list:
            pos_a[(xi*x) % p] = 1
        pa, po = [0], [0]
        for i in range(p):
            pa.append(pa[-1] + pos_a[i])
            po.append(po[-1] + pos_o[i])

        def cnt(pref, lo, hi):
            lo %= p
            hi_len = hi
            end = lo + hi_len
            if end <= p:
                return pref[end] - pref[lo]
            return pref[p] - pref[lo] + pref[end - p]

        quarter = p // 4
        lengths = (quarter, quarter, quarter, p - 3*quarter)
        for r in range(ROTATIONS):
            start = (r*p) // ROTATIONS
            s = 0.0
            for q in range(4):
                lo = start + q*quarter
                ca = cnt(pa, lo, lengths[q])
                co = cnt(po, lo, lengths[q])
                if co:
                    s += ca*ca/co
            e = s/n - a*a
            if e > best:
                best = e
    return best/(a*a)


def main():
    rng = random.Random(20261002)
    rows = []
    for n in SIZES:
        p = next_prime(3*n)
        a_list = greedy_4ap_free(n, rng)
        assert is_4ap_free(a_list)
        a = len(a_list)/n
        e = best_energy(n, p, a_list)
        base = sorted(best_energy(n, p, sorted(rng.sample(range(n), len(a_list))))
                      for _ in range(BASELINES))
        row = {"n": n, "p": p, "size": len(a_list), "density": a,
               "energy_over_a2": e, "random_median": (base[1] + base[2])/2,
               "random_min": base[0], "random_max": base[-1],
               "one_over_log": 1/math.log(2/a),
               "cutoff_24_over_a3_met": n >= 24/a**3}
        rows.append(row)
        print(row, flush=True)
    out = {"rows": rows, "rotations_per_character": ROTATIONS,
           "target_proved": False}
    with open(Path(__file__).resolve().parents[1] / "results" / "interval_window_energy_verification_20261002.json", "w") as fh:
        json.dump(out, fh, indent=1)


if __name__ == "__main__":
    main()
