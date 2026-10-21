"""Run: python3 verify_level_smoothness_20261002.py. Checks for
CANDIDATE_LEMMAS_20261002.md section 4 (smoothness replaces unimodality):
on the window I = [mu-6w, mu+6w] of the level-mass profile G,
    max_s |G(s+1)/G(s) - 1|  and  V(G on I)/G(I)  are O(log r / sqrt r),
and |G_c - G(I)/15| <= V for every residue c mod 15."""
import json
import math

from verify_candidate_lemmas_20261002 import level_masses_fast

MOD = 15
RS = (100, 300, 1200, 2400)


def main():
    rows = []
    for r in RS:
        G, _ = level_masses_fast(r)
        tot = sum(G)
        mu = sum(s*g for s, g in enumerate(G))/tot
        w = math.sqrt(sum((s - mu)**2*g for s, g in enumerate(G))/tot)
        lo, hi = max(0, int(mu - 6*w)), min(3*r, int(mu + 6*w) + 1)
        GI = sum(G[lo:hi + 1])
        ratio = max(abs(G[s + 1]/G[s] - 1) for s in range(lo, hi))
        V = sum(abs(G[s + 1] - G[s]) for s in range(lo, hi))
        dev = max(abs(sum(G[s] for s in range(lo, hi + 1) if s % MOD == c) - GI/MOD)
                  for c in range(MOD))
        assert dev <= V + 1e-15
        scale = math.log(r)/math.sqrt(r)
        row = {"r": r, "w": w, "max_ratio_dev": ratio, "V_over_GI": V/GI,
               "max_class_dev_over_GI": dev/GI, "log_r_over_sqrt_r": scale,
               "max_ratio_dev_over_scale": ratio/scale}
        rows.append(row)
        print(row, flush=True)
    assert all(x["max_ratio_dev_over_scale"] < 3 for x in rows)
    assert rows[-1]["V_over_GI"] < rows[0]["V_over_GI"]
    with open(Path(__file__).resolve().parents[1] / "results" / "level_smoothness_verification_20261002.json", "w") as fh:
        json.dump({"rows": rows, "target_proved": False}, fh, indent=1)


if __name__ == "__main__":
    main()
