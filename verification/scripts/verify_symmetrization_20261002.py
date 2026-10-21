"""Run: python3 verify_symmetrization_20261002.py. Checks for
SYMMETRIZATION_20261002.md.

Part A (exact, small box): for permutation-symmetric A, P = sigma mod 15,
f2 = 1_A - E(1_A|P) and any factor F with cells V,
    Y^2 = ||E(f2|F)||^2 = sum_V c_V E[f2 D_V],  D_V(u) = P(V|n(u)) - P(V|P(u)),
    Y^2 <= sum_V (E[|f2| |D_V|])^2 / mu(V).
Factors: quarter arcs of random real frequencies of X(u)=sum u_i 16^i.

Part B (count space, r=100): for F = (u_S, sigma mod 15), the right side
of the inequality versus the exact energy increment Y^2 measured by
verify_junta_residue_20261002.py, using the stored balanced B."""
from itertools import product
import json
import math
import random

from verify_symmetric_candidate_20261002 import build_T, log_mult

MOD = 15


def part_a(rng, r=6, trials=40):
    pts = list(product(range(4), repeat=r))
    N = len(pts)
    counts = [tuple(u.count(d) for d in range(4)) for u in pts]
    sig = [sum(u) % MOD for u in pts]
    X = [sum(ui*16**i for i, ui in enumerate(u)) for u in pts]
    all_n = sorted(set(counts))
    worst = 0.0
    for _ in range(trials):
        T = {n for n in all_n if rng.random() < 0.3}
        A = [1.0 if counts[j] in T else 0.0 for j in range(N)]
        cls_sum, cls_cnt = [0.0]*MOD, [0]*MOD
        for j in range(N):
            cls_sum[sig[j]] += A[j]
            cls_cnt[sig[j]] += 1
        f2 = [A[j] - cls_sum[sig[j]]/cls_cnt[sig[j]] for j in range(N)]
        k = rng.randrange(1, 4)
        freqs = [(rng.random(), rng.random()) for _ in range(k)]
        cell = [tuple(int(4*((x*phi + rot) % 1)) for phi, rot in freqs) for x in X]
        cells = {}
        for j in range(N):
            cells.setdefault(cell[j], []).append(j)
        n_tot, n_cell = {}, {}
        p_tot, p_cell = [0]*MOD, {}
        for j in range(N):
            n_tot[counts[j]] = n_tot.get(counts[j], 0) + 1
            n_cell[(cell[j], counts[j])] = n_cell.get((cell[j], counts[j]), 0) + 1
            p_cell[(cell[j], sig[j])] = p_cell.get((cell[j], sig[j]), 0) + 1
        y2 = ident = rhs = 0.0
        for v, members in cells.items():
            mu = len(members)/N
            c_v = sum(f2[j] for j in members)/len(members)
            y2 += mu*c_v*c_v
            e_fd = e_abs = 0.0
            for j in range(N):
                d = n_cell.get((v, counts[j]), 0)/n_tot[counts[j]] - \
                    p_cell.get((v, sig[j]), 0)/cls_cnt[sig[j]]
                e_fd += f2[j]*d/N
                e_abs += abs(f2[j])*abs(d)/N
            ident += c_v*e_fd
            rhs += e_abs*e_abs/mu
        assert abs(y2 - ident) < 1e-12
        assert y2 <= rhs + 1e-12
        if rhs > 0:
            worst = max(worst, y2/rhs)
    return worst


def part_b(r=100, s_max=4):
    data = json.load(open(Path(__file__).resolve().parents[1] / "results" / "symmetric_balance_verification_20261002.json"))
    row = next(x for x in data["rows"] if x["r"] == r)
    T = set(build_T(r, set(row["B"])))
    lg4 = r*math.log(4)
    ns = [(n0, n1, n2, r - n0 - n1 - n2) for n0 in range(r + 1)
          for n1 in range(r + 1 - n0) for n2 in range(r + 1 - n0 - n1)]
    pn = [math.exp(log_mult(n) - lg4) for n in ns]
    sg = [(n[1] + 2*n[2] + 3*n[3]) % MOD for n in ns]
    pc = [0.0]*MOD
    ac = [0.0]*MOD
    for n, p, c in zip(ns, pn, sg):
        pc[c] += p
        if n in T:
            ac[c] += p
    a = sum(ac)
    f2 = [(1.0 if n in T else 0.0) - ac[c]/pc[c] for n, c in zip(ns, sg)]
    junta = json.load(open(Path(__file__).resolve().parents[1] / "results" / "junta_residue_verification_20261002.json"))
    jrows = next(x for x in junta["results"] if x["r"] == r)["rows"]
    out = []
    for s in range(1, s_max + 1):
        rhs = 0.0
        rho2 = 0.0
        for m in product(range(s + 1), repeat=4):
            if sum(m) != s:
                continue
            n_pat = math.exp(log_mult(m))
            # probability of one fixed pattern with digit counts m, given n
            pp = []
            for n in ns:
                if min(x - y for x, y in zip(n, m)) < 0:
                    pp.append(0.0)
                else:
                    pp.append(math.exp(sum(math.lgamma(x + 1) - math.lgamma(x - y + 1)
                                           for x, y in zip(n, m))
                                       - (math.lgamma(r + 1) - math.lgamma(r - s + 1))))
            pclass = [0.0]*MOD
            for p, c, q in zip(pn, sg, pp):
                pclass[c] += p*q
            rho2 += n_pat*4.0**(-s)*sum(p*(q*4**s - 1)**2 for p, q in zip(pn, pp))
            for c in range(MOD):
                mu = pclass[c]
                if mu <= 0:
                    continue
                avg = mu/pc[c]
                e_abs = sum(p*abs(f)*abs(q - avg)
                            for p, f, q, cc in zip(pn, f2, pp, sg) if cc == c)
                rhs += n_pat*e_abs*e_abs/mu
        y2 = (jrows[s]["energy_over_a2"] - jrows[0]["energy_over_a2"])*a*a
        assert y2 <= rhs*(1 + 1e-9)
        assert abs(rho2 - 3*s/r) < 0.2*3*s/r
        out.append({"s": s, "Y2_over_a2": y2/a**2, "rhs_over_a2": rhs/a**2,
                    "mean_rho2": rho2, "three_s_over_r": 3*s/r})
        print(out[-1], flush=True)
    return a, out


def main():
    rng = random.Random(20261002)
    worst = part_a(rng)
    print("part A worst Y^2/rhs", worst, flush=True)
    a, rows = part_b()
    with open(Path(__file__).resolve().parents[1] / "results" / "symmetrization_verification_20261002.json", "w") as fh:
        json.dump({"part_a_worst_ratio": worst, "part_b_r": 100, "density": a,
                   "part_b": rows, "target_proved": False}, fh, indent=1)


if __name__ == "__main__":
    main()
