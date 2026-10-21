"""Run: python3 verify_symmetric_candidate_20261002.py. Checks for
SYMMETRIC_CANDIDATE_20261002.md: a permutation-symmetric 4-AP-free set in
the box {0,1,2,3}^r. Exact AP checks for small r; float multinomial sums
(log-gamma) for density, cutoff and junta/mod-15 energies at larger r."""
from itertools import product
import json
import math
import random


def greedy_4ap_free(n, rng):
    order = list(range(n))
    rng.shuffle(order)
    member = bytearray(n)
    for x in order:
        ok = True
        for h in range(1, (n - 1)//3 + 1):
            for j in range(4):
                s = x - j*h
                if 0 <= s and s + 3*h < n and all(member[s + i*h] for i in range(4) if i != j):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            member[x] = 1
    return {x for x in range(n) if member[x]}


def log_mult(counts):
    return math.lgamma(sum(counts) + 1) - sum(math.lgamma(c + 1) for c in counts)


def lines(r):
    """Count vectors (n0,n1,n2,n3), grouped by the invariants
    alpha=n0+n1, beta=n0+n2 of the direction d=(-1,1,1,-1)."""
    for alpha in range(r + 1):
        for beta in range(r + 1):
            lo, hi = max(0, alpha + beta - r), min(alpha, beta)
            if lo > hi:
                continue
            pts = [(n0, alpha - n0, beta - n0, r - alpha - beta + n0)
                   for n0 in range(lo, hi + 1)]
            yield 3*r - 2*alpha - beta, pts


def build_T(r, B):
    T = []
    for sigma, pts in lines(r):
        if sigma in B:
            T.append(max(pts, key=log_mult))
    return T


def exact_4ap_free(r, T):
    tset = set(T)
    pts = [u for u in product(range(4), repeat=r)
           if tuple(u.count(j) for j in range(4)) in tset]
    s = set(pts)
    for u in pts:
        for v in pts:
            if u < v and all((b - a) % 3 == 0 for a, b in zip(u, v)):
                w = [(b - a)//3 for a, b in zip(u, v)]
                if tuple(a + c for a, c in zip(u, w)) in s and \
                        tuple(a + 2*c for a, c in zip(u, w)) in s:
                    return False, len(pts)
    return True, len(pts)


def stats(r, T):
    lg4 = r*math.log(4)
    a = sum(math.exp(log_mult(n) - lg4) for n in T)

    def cond(m):
        k = sum(m)
        tot = 0.0
        for n in T:
            rest = tuple(x - y for x, y in zip(n, m))
            if min(rest) >= 0:
                tot += math.exp(log_mult(rest) - (r - k)*math.log(4))
        return tot

    junta = {}
    for k in (1, 2):
        e = 0.0
        for m in product(range(k + 1), repeat=4):
            if sum(m) != k:
                continue
            pm = math.exp(log_mult(m) - k*math.log(4))
            e += pm*(cond(m)/a - 1)**2
        junta[k] = e
    by_res = [0.0]*15
    mass_res = [0.0]*15
    for sigma, pts in lines(r):
        for n in pts:
            mass_res[sigma % 15] += math.exp(log_mult(n) - lg4)
    for n in T:
        sigma = n[1] + 2*n[2] + 3*n[3]
        by_res[sigma % 15] += math.exp(log_mult(n) - lg4)
    mod15 = sum(mr*((br/mr)/a - 1)**2 for br, mr in zip(by_res, mass_res) if mr > 0)
    rank = r + 1
    cutoff_log = r*math.log(4) - (math.log(8) + rank*math.log(3) - 3*math.log(a))
    return {"r": r, "density": a, "sqrt_r_times_density": a*math.sqrt(r),
            "junta1_energy_over_a2": junta[1], "junta2_energy_over_a2": junta[2],
            "mod15_energy_over_a2": mod15,
            "target_scale_1_over_log": 1/math.log(2/a),
            "log_cutoff_margin": cutoff_log}


def main():
    rng = random.Random(20261002)
    out = {"exact_small": [], "large": []}
    for r in (3, 4, 5, 6):
        B = greedy_4ap_free(3*r + 1, rng)
        T = build_T(r, B)
        free, size = exact_4ap_free(r, T)
        assert free
        out["exact_small"].append({"r": r, "B": sorted(B), "points": size, "4ap_free": free})
        print(out["exact_small"][-1], flush=True)
    for r in (50, 100, 200, 300):
        B = greedy_4ap_free(3*r + 1, rng)
        row = stats(r, build_T(r, B))
        row["B_density"] = len(B)/(3*r + 1)
        out["large"].append(row)
        print(row, flush=True)
    # cutoff solver for the asymptotic density profile a ~ c/sqrt(r)
    c = out["large"][-1]["sqrt_r_times_density"]
    r = 1
    while r*math.log(4) < math.log(8) + (r + 1)*math.log(3) + 3*math.log(math.sqrt(r)/c):
        r += 1
    out["first_r_meeting_cutoff_if_a_equals_c_over_sqrt_r"] = r
    out["c_used"] = c
    out["target_proved"] = False
    with open("symmetric_candidate_verification_20261002.json", "w") as fh:
        json.dump(out, fh, indent=1)
    print({k: out[k] for k in ("first_r_meeting_cutoff_if_a_equals_c_over_sqrt_r", "c_used")})


if __name__ == "__main__":
    main()
