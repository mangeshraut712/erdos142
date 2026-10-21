#!/usr/bin/env python3
"""Typical count window for MIXED_FACTORS section 7 (exact multinomials).

u uniform on {0,1,2,3}^r, n(u) its count vector. Narrow window
  N_r = { n : |n_d - r/4| <= sqrt(r log r) for all d }.
Claims checked exactly:
  (1) min_{n in N_r} P(n(u)=n) >= r^(-12)       (so dividing costs r^O(1);
      the local CLT exponent is 8 + 3/2 + o(1));
  (2) P(n(u) not in N_r) <= 8 r^(-2) = o(a^2/log r) with a ~ r^(-3/4).
For contrast, the minimum over the wide window |n_d - r/4| <= sqrt(r) log r
is recorded: it decays like exp(-c log^2 r), which e^(-T/2) cannot absorb.
Standard library only.
"""

import json
import math


def log_pmf(counts, r):
    return (math.lgamma(r + 1) - sum(math.lgamma(c + 1) for c in counts)
            - r * math.log(4))


def min_log_pmf(r, half_width):
    centre = r / 4
    lo = max(0, math.ceil(centre - half_width))
    hi = min(r, math.floor(centre + half_width))
    best = 0.0
    for n0 in range(lo, hi + 1):
        for n1 in range(lo, hi + 1):
            rest = r - n0 - n1
            n2_lo = max(lo, rest - hi)
            n2_hi = min(hi, rest - lo)
            for n2 in (n2_lo, n2_hi):
                if n2_lo > n2_hi:
                    continue
                best = min(best, log_pmf((n0, n1, n2, rest - n2), r))
    return best


def binom_tail_two_sided(r, half_width):
    centre = r / 4
    total = 0.0
    for k in range(r + 1):
        if abs(k - centre) > half_width:
            total += math.exp(math.lgamma(r + 1) - math.lgamma(k + 1)
                              - math.lgamma(r - k + 1)
                              + k * math.log(0.25) + (r - k) * math.log(0.75))
    return total


def main():
    rows = []
    for r in (100, 400, 900, 1600):
        narrow = math.sqrt(r * math.log(r))
        wide = math.sqrt(r) * math.log(r)
        min_narrow = min_log_pmf(r, narrow)
        min_wide = min_log_pmf(r, wide)
        atyp = 4 * binom_tail_two_sided(r, narrow)
        row = {
            "r": r,
            "narrow_half_width": narrow,
            "min_log_pmf_narrow_over_log_r": min_narrow / math.log(r),
            "min_log_pmf_wide_over_log_r": min_wide / math.log(r),
            "atypical_mass_union_bound": atyp,
            "bound_8_over_r2": 8 / r ** 2,
            "a_squared_over_log_r": r ** -1.5 / math.log(r),
        }
        assert min_narrow >= -12 * math.log(r), row
        assert atyp <= 8 / r ** 2, row
        assert atyp < row["a_squared_over_log_r"], row
        rows.append(row)
        print(row)
    out = {"rows": rows, "target_proved": False}
    with open(Path(__file__).resolve().parents[1] / "results" / "typical_window_verification_20261002.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
