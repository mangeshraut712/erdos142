"""Run: python3 verify_junta_residue_20261002.py. Step 1 of
CANDIDATE_LEMMAS_20261002.md section 5: energy of E(1_A | u_S, sigma mod 15)
for |S|=k, computed exactly in count space (log-gamma floats), using the
balanced B stored by verify_symmetric_balance_20261002.py."""
from itertools import product
import json
import math

from verify_symmetric_candidate_20261002 import build_T, log_mult

MOD = 15


def sigma_of(n):
    return n[1] + 2*n[2] + 3*n[3]


def energy(r, T, k):
    """Partition by (counts m of the k fixed coordinates, sigma mod 15)."""
    lg4 = math.log(4)
    rest = r - k
    # P(sigma(n') = s) for n' ~ Mult(rest): coefficients of ((1+x+x^2+x^3)/4)^rest
    coeff = [1.0]
    for _ in range(rest):
        new = [0.0]*(len(coeff) + 3)
        for i, c in enumerate(coeff):
            for j in range(4):
                new[i + j] += c/4
        coeff = new
    res_mass = [0.0]*MOD
    for s, c in enumerate(coeff):
        res_mass[s % MOD] += c
    a = sum(math.exp(log_mult(n) - r*lg4) for n in T)
    total = 0.0
    for m in product(range(k + 1), repeat=4):
        if sum(m) != k:
            continue
        pm = math.exp(log_mult(m) - k*lg4)
        s_m = sigma_of(m)
        hit = [0.0]*MOD
        for n in T:
            rem = tuple(x - y for x, y in zip(n, m))
            if min(rem) >= 0:
                hit[sigma_of(n) % MOD] += math.exp(log_mult(rem) - rest*lg4)
        for c in range(MOD):
            pc = res_mass[(c - s_m) % MOD]
            if pc > 0:
                total += pm*pc*((hit[c]/pc)/a - 1)**2
    return a, total


def main():
    data = json.load(open(Path(__file__).resolve().parents[1] / "results" / "symmetric_balance_verification_20261002.json"))
    results = []
    for row in data["rows"]:
        r, B = row["r"], set(row["B"])
        T = build_T(r, B)
        out = []
        for k in range(0, 7):
            a, e = energy(r, T, k)
            out.append({"k": k, "energy_over_a2": e})
            print(r, out[-1], flush=True)
        assert abs(out[0]["energy_over_a2"] - row["mod15_energy_over_a2"]) < 1e-6
        slope = (out[-1]["energy_over_a2"] - out[0]["energy_over_a2"])/6
        results.append({"r": r, "density": a, "rows": out,
                        "slope_per_coordinate": slope, "slope_times_r": slope*r,
                        "one_over_log": 1/math.log(2/a)})
        print(r, "slope", slope, "slope*r", slope*r, flush=True)
    with open(Path(__file__).resolve().parents[1] / "results" / "junta_residue_verification_20261002.json", "w") as fh:
        json.dump({"results": results, "target_proved": False}, fh, indent=1)


if __name__ == "__main__":
    main()
