"""Run: python3 verify_candidate_lemmas_20261002.py. Checks for
CANDIDATE_LEMMAS_20261002.md: the closed-form line mode, the Fourier decay
bound, the digit lemma, and the random-alteration balance of B.
Finite diagnostics; floats where stated."""
import cmath
import json
import math
import random

from verify_symmetric_candidate_20261002 import lines, log_mult


def mode_on_line(r, alpha, beta):
    lo, hi = max(0, alpha + beta - r), min(alpha, beta)
    R = r - alpha - beta
    n0 = -(-(alpha*beta - R - 1)//(r + 2))
    return min(max(n0, lo), hi)


def check_mode(r):
    for sigma, pts in lines(r):
        alpha = pts[0][0] + pts[0][1]
        beta = pts[0][0] + pts[0][2]
        best = max(log_mult(n) for n in pts)
        n0 = mode_on_line(r, alpha, beta)
        n = (n0, alpha - n0, beta - n0, r - alpha - beta + n0)
        assert abs(log_mult(n) - best) < 1e-9, (r, alpha, beta)
    return True


def dist(x):
    return abs(x - round(x))


def check_fourier_decay(rng, trials):
    """|E e(xi.n(u) + sum z_i u_i)| = prod |phi_i| <= exp(-2 sum ||z_i-gamma||^2),
    gamma = xi_0 - xi_1."""
    worst = 0.0
    for _ in range(trials):
        r = rng.randint(1, 12)
        xi = [rng.random() for _ in range(4)]
        z = [rng.random() for _ in range(r)]
        prod = 1.0
        for zi in z:
            prod *= abs(sum(cmath.exp(2j*math.pi*(xi[j] + j*zi)) for j in range(4)))/4
        gamma = xi[0] - xi[1]
        bound = math.exp(-2*sum(dist(zi - gamma)**2 for zi in z))
        assert prod <= bound + 1e-12
        worst = max(worst, prod/bound)
    return worst


def check_digit_lemma(rng, trials, delta=1/64):
    """If ||16^i x - g|| <= delta and ||16^(i+1) x - g|| <= delta then
    16^i x is within 2 delta/15 of some k/15 and g within 2 delta of it."""
    hits = 0
    for _ in range(trials):
        k = rng.randrange(15)
        y = k/15 + rng.uniform(-delta/8, delta/8)
        g = y + rng.uniform(-delta, delta)
        if dist(16*y - g) > delta or dist(y - g) > delta:
            continue
        hits += 1
        near = min(range(15), key=lambda c: dist(y - c/15))
        assert dist(y - near/15) <= 2*delta/15 + 1e-12
        assert dist(g - near/15) <= 2*delta + 1e-12
    for _ in range(trials):
        y, g = rng.random(), rng.random()
        if dist(y - g) <= delta and dist(16*y - g) <= delta:
            near = min(range(15), key=lambda c: dist(y - c/15))
            assert dist(15*y) <= 2*delta + 1e-12
            assert dist(y - near/15) <= 2*delta/15 + 1e-12
            hits += 1
    return hits


def level_masses_fast(r):
    lg4 = r*math.log(4)
    G = [0.0]*(3*r + 1)
    H = [0.0]*(3*r + 1)
    for alpha in range(r + 1):
        for beta in range(r + 1):
            lo, hi = max(0, alpha + beta - r), min(alpha, beta)
            if lo > hi:
                continue
            sigma = 3*r - 2*alpha - beta
            n0 = mode_on_line(r, alpha, beta)
            G[sigma] += math.exp(log_mult((n0, alpha - n0, beta - n0,
                                          r - alpha - beta + n0)) - lg4)
    for s in range(3*r + 1):
        # total mass of sigma = s: coefficient of x^s in ((1+x+x^2+x^3)/4)^r
        pass
    coeff = [1.0]
    for _ in range(r):
        new = [0.0]*(len(coeff) + 3)
        for i, c in enumerate(coeff):
            for j in range(4):
                new[i + j] += c/4
        coeff = new
    H = coeff
    return G, H


def alteration_B(G, beta_prob, rng, window):
    lo, hi = window
    B = {s for s in range(lo, hi + 1) if rng.random() < beta_prob}
    for x in sorted(B):
        if x not in B:
            continue
        for h in range(1, (hi - lo)//3 + 1):
            if x + 3*h > hi:
                break
            if x + h in B and x + 2*h in B and x + 3*h in B:
                B.discard(x + 3*h)
    return B


def mod_energy(B, G, H, mod=15):
    a = sum(G[s] for s in B)
    tot = [0.0]*mod
    am = [0.0]*mod
    for s, h in enumerate(H):
        tot[s % mod] += h
    for s in B:
        am[s % mod] += G[s]
    return a, sum(t*((x/t)/a - 1)**2 for x, t in zip(am, tot) if t > 0)


def is_4ap_free(B):
    return not any(x + h in B and x + 2*h in B and x + 3*h in B
                   for x in B for h in range(1, (max(B) - x)//3 + 1))


def main():
    rng = random.Random(20261002)
    out = {"mode_formula_exact_r": [r for r in (5, 17, 40, 90) if check_mode(r)],
           "fourier_decay_max_ratio": check_fourier_decay(rng, 3000),
           "digit_lemma_cases": check_digit_lemma(rng, 200000)}
    rows = []
    for r in (300, 1200, 4800):
        G, H = level_masses_fast(r)
        tot = sum(G)
        mu = sum(s*g for s, g in enumerate(G))/tot
        sd = math.sqrt(sum((s - mu)**2*g for s, g in enumerate(G))/tot)
        window = (max(0, int(mu - 6*sd)), min(3*r, int(mu + 6*sd) + 1))
        beta_prob = (12*sd)**(-0.45)
        energies, dens = [], []
        for _ in range(6):
            B = alteration_B(G, beta_prob, rng, window)
            assert is_4ap_free(B)
            a, e = mod_energy(B, G, H)
            energies.append(e)
            dens.append(a)
        rows.append({"r": r, "sigma_sd": sd, "beta": beta_prob,
                     "mean_mod15_energy_over_a2": sum(energies)/len(energies),
                     "max_mod15_energy_over_a2": max(energies),
                     "mean_density": sum(dens)/len(dens),
                     "one_over_log": 1/math.log(2*len(dens)/sum(dens))})
        print(rows[-1], flush=True)
    out["alteration_balance"] = rows
    out["target_proved"] = False
    with open(Path(__file__).resolve().parents[1] / "results" / "candidate_lemmas_verification_20261002.json", "w") as fh:
        json.dump(out, fh, indent=1)
    print({k: v for k, v in out.items() if k != "alteration_balance"})


if __name__ == "__main__":
    main()
