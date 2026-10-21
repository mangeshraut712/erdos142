"""Run: python3 verify_symmetric_balance_20261002.py. Chooses the 4-AP-free
digit-sum set B of SYMMETRIC_CANDIDATE_20261002.md to balance A-mass
across residues of sigma mod 15, the only symmetric character class of
the base-16 realization. Float multinomial sums; finite diagnostics."""
import json
import math
import random

from verify_symmetric_candidate_20261002 import lines, log_mult, stats, build_T

MOD = 15


def level_masses(r):
    lg4 = r*math.log(4)
    G = [0.0]*(3*r + 1)
    H = [0.0]*(3*r + 1)
    for sigma, pts in lines(r):
        masses = [math.exp(log_mult(n) - lg4) for n in pts]
        G[sigma] += max(masses)
        H[sigma] += sum(masses)
    return G, H


def mod_energy(B, G, H):
    a = sum(G[s] for s in B)
    tot_c = [0.0]*MOD
    a_c = [0.0]*MOD
    for s, h in enumerate(H):
        tot_c[s % MOD] += h
    for s in B:
        a_c[s % MOD] += G[s]
    return a, sum(t*((x/t)/a - 1)**2 for x, t in zip(a_c, tot_c) if t > 0)


def creates_4ap(B, x):
    for h in range(1, len(B) + 3*max(B | {x}) + 1):
        if h > 3*(max(B | {x}) + 1):
            break
        for j in range(4):
            s = x - j*h
            if all((s + i*h) in B for i in range(4) if i != j):
                return True
    return False


def balanced_B(G, H, rng, restarts, steps):
    n = len(G)
    best = None
    for _ in range(restarts):
        B = set()
        order = sorted(range(n), key=lambda s: -G[s]*(1 + 0.3*rng.random()))
        for s in order:
            if G[s] > 1e-12 and not creates_4ap(B, s):
                B.add(s)
        a, e = mod_energy(B, G, H)
        for _ in range(steps):
            out = rng.choice(sorted(B))
            B.discard(out)
            cand = [s for s in range(n) if s not in B and s != out and G[s] > 1e-9
                    and not creates_4ap(B, s)]
            if not cand:
                B.add(out)
                continue
            new = rng.choice(cand)
            B.add(new)
            a2, e2 = mod_energy(B, G, H)
            if e2 <= e and a2 >= 0.9*a:
                a, e = a2, e2
            else:
                B.discard(new)
                B.add(out)
        if best is None or e < best[1]:
            best = (sorted(B), e, a)
    return best


def main():
    rng = random.Random(20261002)
    rows = []
    for r in (100, 300, 600):
        G, H = level_masses(r)
        B, e, a = balanced_B(G, H, rng, restarts=4, steps=400)
        assert not any(creates_4ap(set(B) - {x}, x) for x in B)
        row = {"r": r, "density": a, "mod15_energy_over_a2": e,
               "target_scale_1_over_log": 1/math.log(2/a), "B": B}
        if r <= 300:
            full = stats(r, build_T(r, set(B)))
            row.update({k: full[k] for k in ("junta1_energy_over_a2",
                        "junta2_energy_over_a2", "log_cutoff_margin")})
            assert abs(full["mod15_energy_over_a2"] - e) < 1e-6
        rows.append(row)
        print({k: v for k, v in row.items() if k != "B"}, flush=True)
    with open("symmetric_balance_verification_20261002.json", "w") as fh:
        json.dump({"rows": rows, "target_proved": False}, fh, indent=1)


if __name__ == "__main__":
    main()
