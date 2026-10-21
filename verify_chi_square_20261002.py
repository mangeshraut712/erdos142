"""Run: python3 verify_chi_square_20261002.py. Exact checks for
GENERIC_FACTORS_20261002.md section 1 on the box {0,1,2,3}^r (r=6):
for permutation-symmetric A, f2 = 1_A - E(1_A | sigma mod 15) and a factor
F of random quarter arcs of X(u)=sum u_i 16^i,
    ||E(f2|F)||^2 <= ||E(f2|F v P)||^2
                  <= max_c w_c(1-w_c) * E_n chi^2(Law(V|n) || Law(V|class(n))),
where V runs over cells of F v P."""
from itertools import product
import json
import random

MOD = 15


def energy(f, labels):
    tot, cnt = {}, {}
    for x, lab in zip(f, labels):
        tot[lab] = tot.get(lab, 0.0) + x
        cnt[lab] = cnt.get(lab, 0) + 1
    N = len(f)
    return sum(t*t/cnt[lab] for lab, t in tot.items())/N


def main():
    rng = random.Random(7)
    r = 6
    pts = list(product(range(4), repeat=r))
    N = len(pts)
    counts = [tuple(u.count(d) for d in range(4)) for u in pts]
    sig = [sum(u) % MOD for u in pts]
    X = [sum(ui*16**i for i, ui in enumerate(u)) for u in pts]
    all_n = sorted(set(counts))
    n_size = {n: counts.count(n) for n in all_n}
    c_size = [sig.count(c) for c in range(MOD)]
    worst = 0.0
    for _ in range(60):
        T = {n for n in all_n if rng.random() < rng.choice((0.1, 0.3, 0.6))}
        A = [1.0 if counts[j] in T else 0.0 for j in range(N)]
        w = [0.0]*MOD
        for j in range(N):
            w[sig[j]] += A[j]/c_size[sig[j]]
        f2 = [A[j] - w[sig[j]] for j in range(N)]
        k = rng.randrange(1, 4)
        freqs = [(rng.random(), rng.random()) for _ in range(k)]
        cell = [tuple(int(4*((x*phi + rot) % 1)) for phi, rot in freqs) for x in X]
        refined = [(cell[j], sig[j]) for j in range(N)]
        y_f = energy(f2, cell)
        y_fp = energy(f2, refined)
        assert y_f <= y_fp + 1e-12
        joint_n, joint_c = {}, {}
        for j in range(N):
            joint_n[(refined[j], counts[j])] = joint_n.get((refined[j], counts[j]), 0) + 1
            joint_c[refined[j]] = joint_c.get(refined[j], 0) + 1
        chi = 0.0
        cells_by_class = {}
        for v in joint_c:
            cells_by_class.setdefault(v[1], []).append(v)
        for n in all_n:
            c = (n[1] + 2*n[2] + 3*n[3]) % MOD
            pn = n_size[n]/N
            for v in cells_by_class.get(c, []):
                q = joint_c[v]/c_size[c]
                p = joint_n.get((v, n), 0)/n_size[n]
                chi += pn*(p - q)**2/q
        rhs = max(x*(1 - x) for x in w)*chi
        assert y_fp <= rhs + 1e-12
        if rhs > 0:
            worst = max(worst, y_fp/rhs)
    print("worst ratio", worst)
    with open("chi_square_verification_20261002.json", "w") as fh:
        json.dump({"r": r, "trials": 60, "worst_ratio": worst,
                   "target_proved": False}, fh, indent=1)


if __name__ == "__main__":
    main()
