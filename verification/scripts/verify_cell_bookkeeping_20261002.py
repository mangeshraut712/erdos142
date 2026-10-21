"""Run: python3 verify_cell_bookkeeping_20261002.py. Exact checks for
CELL_BOOKKEEPING_20261002.md: the run lemma, the Cantor small-ball bound,
and the decided/undecided decomposition of an exceptional quarter-arc
character on the box {0,1,2,3}^r (integer arithmetic throughout)."""
from fractions import Fraction
from itertools import product
import json
import math
import random

RHO = Fraction(1, 33)


def signed_frac(q):
    f = q - math.floor(q)
    return f - 1 if f > Fraction(1, 2) else f


def planted_y(r, extra, n_digits, rng):
    """y with a few nonzero base-16 digits among positions 1..r+extra, sign random."""
    den = 16**(r + extra)
    num = 0
    for pos in rng.sample(range(1, r + extra + 1), n_digits):
        num += rng.randrange(1, 16)*16**(r + extra - pos)
    y = Fraction(num, den)
    return -y if rng.random() < 0.5 else y


def check_run_lemma(rng, trials=4000):
    pairs = 0
    for _ in range(trials):
        r = rng.randrange(6, 30)
        y = planted_y(r, 6, rng.randrange(1, 6), rng) if rng.random() < 0.7 else \
            Fraction(rng.randrange(16**(r + 6)), 16**(r + 6))
        z = [signed_frac(y*16**i) for i in range(r)]
        for i in range(r - 1):
            if abs(z[i]) <= RHO and abs(z[i + 1]) <= RHO:
                assert z[i + 1] == 16*z[i]
                pairs += 1
    return pairs


def check_small_ball(g=8):
    """X=sum_{j=1}^g u_j 16^-j, u_j in {0..3}: P(X in interval of length l) <= 2*sqrt(20 l)."""
    vals = sorted(sum(u*16**(g - 1 - j) for j, u in enumerate(us))
                  for us in product(range(4), repeat=g))
    total = len(vals)
    worst = 0.0
    for m in range(0, 2*g + 1):
        for scale in (1, 2, 3, 5, 8, 13):
            width = Fraction(scale, 2**m)
            if width < Fraction(1, 16**g):
                continue
            w_int = width*16**g
            hi = 0
            best = 0
            for lo in range(total):
                while hi < total and vals[hi] - vals[lo] <= w_int:
                    hi += 1
                best = max(best, hi - lo)
            prob = best/total
            bound = 2*math.sqrt(20*float(width))
            assert prob <= bound + 1e-12
            worst = max(worst, prob/bound)
    return worst


def runs_of_good(bad, r):
    """Maximal runs of good indices, each returned as (bottom, top)."""
    out, i = [], 0
    while i < r:
        if i in bad:
            i += 1
            continue
        j = i
        while j + 1 < r and j + 1 not in bad:
            j += 1
        out.append((i, j))
        i = j + 1
    return out


def check_decomposition(rng, r, g, trials, max_digits):
    rows = []
    for _ in range(trials):
        k = rng.randrange(15)
        y = planted_y(r, 4, rng.randrange(1, max_digits + 1), rng)
        z = [signed_frac(y*16**i) for i in range(r)]
        bad = {i for i in range(r) if abs(z[i]) > RHO}
        long_runs = [(lo, hi) for lo, hi in runs_of_good(bad, r) if hi - lo + 1 > g]
        s_prime = set(bad)
        for lo, hi in runs_of_good(bad, r):
            s_prime |= set(range(max(lo, hi - g + 1), hi + 1))
        eps = sum(abs(z[hi]) for _, hi in long_runs)*Fraction(16, 5)/16**g
        alpha = Fraction(rng.randrange(10**6), 10**6)
        lo_end, hi_end = alpha, alpha + Fraction(1, 4)
        phi = Fraction(k, 15) + y
        undecided = 0
        for u in product(range(4), repeat=r):
            X = sum(ui*16**i for i, ui in enumerate(u))
            sigma = sum(u)
            phase = (phi*X) % 1
            assert phase == (Fraction(k*sigma, 15) + sum(ui*zi for ui, zi in zip(u, z))) % 1
            psi = (Fraction(k*sigma, 15) + sum(u[i]*z[i] for i in s_prime)) % 1
            inside = (phase - lo_end) % 1 < Fraction(1, 4)
            d_lo = min((psi - lo_end) % 1, (lo_end - psi) % 1)
            d_hi = min((psi - hi_end) % 1, (hi_end - psi) % 1)
            if min(d_lo, d_hi) <= eps:
                undecided += 1
            else:
                assert inside == ((psi - lo_end) % 1 < Fraction(1, 4))
        mass = undecided/4**r
        if long_runs and eps > 0:
            zmax = max(abs(z[hi]) for _, hi in long_runs)
            ell = 2*eps/zmax
            m = 0
            while m + 1 <= g - 1 and ell <= Fraction(4, 5)*Fraction(16, 16**(m + 1)):
                m += 1
            bound = min(1.0, 2*15*2*4.0**(-m))
        else:
            bound = 0.0
        assert mass <= bound + 1e-12
        rows.append({"r": r, "g": g, "k": k, "bad": sorted(bad), "junta_size": len(s_prime),
                     "undecided_mass": mass, "bound": bound})
    return rows


def main():
    rng = random.Random(20261002)
    pairs = check_run_lemma(rng)
    print("run lemma pairs", pairs, flush=True)
    worst = check_small_ball()
    print("small ball worst ratio", worst, flush=True)
    rows = check_decomposition(rng, r=7, g=2, trials=12, max_digits=3)
    rows += check_decomposition(rng, r=9, g=2, trials=6, max_digits=2)
    for row in rows:
        print(row, flush=True)
    with open(Path(__file__).resolve().parents[1] / "results" / "cell_bookkeeping_verification_20261002.json", "w") as fh:
        json.dump({"run_lemma_pairs_checked": pairs,
                   "small_ball_worst_ratio": worst,
                   "decomposition": rows,
                   "target_proved": False}, fh, indent=1)


if __name__ == "__main__":
    main()
