"""Run: python3 verify_parameter_audit_20261002.py. Checks for
PARAMETER_AUDIT_20261002.md: density scaling of the random-alteration B
(stored in candidate_lemmas_verification_20261002.json), the cutoff
4^r >= 8*3^(r+1)*a^(-3) with that density, and the junta allowance
a*r/log r compared with polylog sizes."""
import json
import math


def main():
    data = json.load(open(Path(__file__).resolve().parents[1] / "results" / "candidate_lemmas_verification_20261002.json"))
    rows = []
    for row in data["alteration_balance"]:
        r, a, beta, w = row["r"], row["mean_density"], row["beta"], row["sigma_sd"]
        cutoff_margin = r*math.log(4) - (math.log(8) + (r + 1)*math.log(3) - 3*math.log(a))
        allowance = a*r/math.log(r)
        out = {"r": r, "density": a, "a_times_r_to_3_4": a*r**0.75,
               "a_over_beta_times_sqrt_r": a*math.sqrt(r)/beta,
               "cutoff_log_margin": cutoff_margin,
               "junta_allowance_a_r_over_log_r": allowance,
               "log_r_cubed": math.log(r)**3}
        assert 0.3 < out["a_times_r_to_3_4"] < 1.0
        assert cutoff_margin > 0
        rows.append(out)
        print(out, flush=True)
    with open(Path(__file__).resolve().parents[1] / "results" / "parameter_audit_verification_20261002.json", "w") as fh:
        json.dump({"rows": rows, "target_proved": False}, fh, indent=1)


if __name__ == "__main__":
    main()
