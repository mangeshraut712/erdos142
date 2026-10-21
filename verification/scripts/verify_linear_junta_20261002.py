"""Run: python3 verify_linear_junta_20261002.py. Checks for
PARAMETER_AUDIT_20261002.md section 3: the linearized junta energy
    Y^2 ~ (4s/r^2) sum_c sum_d L_(d,c)^2 / P(c),  L_(d,c) = E[f2 n_d 1_c],
against the exact energy increments of verify_junta_residue_20261002.py
(balanced B), and the bound |E[n_d - r/4 | A, class c]| <= sqrt(r) log r."""
import json
import math

from verify_symmetric_candidate_20261002 import build_T, log_mult

MOD = 15


def main():
    bal = json.load(open(Path(__file__).resolve().parents[1] / "results" / "symmetric_balance_verification_20261002.json"))
    junta = json.load(open(Path(__file__).resolve().parents[1] / "results" / "junta_residue_verification_20261002.json"))
    rows = []
    for res in junta["results"]:
        r = res["r"]
        brow = next(x for x in bal["rows"] if x["r"] == r)
        T = set(build_T(r, set(brow["B"])))
        lg4 = r*math.log(4)
        pc, ac = [0.0]*MOD, [0.0]*MOD
        L = [[0.0]*4 for _ in range(MOD)]
        mean_A = [[0.0]*4 for _ in range(MOD)]
        entries = []
        for n0 in range(r + 1):
            for n1 in range(r + 1 - n0):
                for n2 in range(r + 1 - n0 - n1):
                    n = (n0, n1, n2, r - n0 - n1 - n2)
                    p = math.exp(log_mult(n) - lg4)
                    c = (n[1] + 2*n[2] + 3*n[3]) % MOD
                    pc[c] += p
                    inA = n in T
                    if inA:
                        ac[c] += p
                    entries.append((n, p, c, inA))
        w = [ac[c]/pc[c] for c in range(MOD)]
        a = sum(ac)
        for n, p, c, inA in entries:
            f2 = (1.0 if inA else 0.0) - w[c]
            for d in range(4):
                L[c][d] += p*f2*n[d]
                if inA:
                    mean_A[c][d] += p*(n[d] - r/4)
        slope = 4/r**2*sum(L[c][d]**2/pc[c] for c in range(MOD) for d in range(4))/a**2
        bias = max(abs(mean_A[c][d]/ac[c]) for c in range(MOD) if ac[c] > 0 for d in range(4))
        measured = res["rows"][1]["energy_over_a2"] - res["rows"][0]["energy_over_a2"]
        row = {"r": r, "predicted_slope_over_a2": slope, "measured_s1_over_a2": measured,
               "ratio": measured/slope, "max_count_bias": bias,
               "sqrt_r_log_r": math.sqrt(r)*math.log(r),
               "slope_times_r": slope*r}
        assert bias <= math.sqrt(r)*math.log(r)
        assert 0.5 < row["ratio"] < 2.0
        rows.append(row)
        print(row, flush=True)
    with open(Path(__file__).resolve().parents[1] / "results" / "linear_junta_verification_20261002.json", "w") as fh:
        json.dump({"rows": rows, "target_proved": False}, fh, indent=1)


if __name__ == "__main__":
    main()
