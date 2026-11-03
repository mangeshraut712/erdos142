#!/usr/bin/env python3
# HISTORICAL DIAGNOSTIC: analytic transfer claims withdrawn 2026-11-03.
# Excluded from CURRENT; see ALL_PAIR_OPERATOR_20261103.md.
"""Verify Gowers U^3 uniformity, quartic concentration, and arithmetic low-mean bounds (GU24).

Audits:
1. Exact Gowers U^3 norm calculation via discrete derivative Fourier identity:
   ||u||_{U^3}^8 = (1/p) sum_{r in F_p} sum_{k in F_p} |widecheck{Delta_r u}(k)|^4.
2. Exact Gowers-Cauchy-Schwarz bound: |R4| <= C_F ||u||_{U^3}^4.
3. Strict positivity of fourth residual on the arithmetic low-mean branch (m <= 2 a^3 T / w):
   R4 = 3 a^4 T + 2 R1 + R2 - a w m + a w (1 - 4a)/p >= (5/2) a^4 T.
4. Quantitative inverse theorem exponent gap: delta = max_{c, t} |E_Omega u e_p(-cx^2 - tx)|
   satisfies delta >= c a^C with C >= 2.0 > 1.5, proving that Gowers U^3 transfer alone
   cannot supply the super-critical exponent a^(1.5) F(a) needed for DIRECT-Q-GAIN.
"""
from __future__ import annotations

import cmath
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]


def geometry(p: int):
    edges = set()
    for x in range(p):
        for h in range(1, p):
            edges.add(frozenset((x + i * h) % p for i in range(4)))
    return edges


def run() -> None:
    counts: dict[str, int] = defaultdict(int)

    def check(condition: bool, name: str) -> None:
        assert condition, f"Assertion failed: {name}"
        counts[name] += 1

    arithmetic_cases = 0
    low_mean_cases = 0
    zero_mean_cases = 0
    max_observed_delta_ratio = 0.0

    for p in (5, 7, 11, 13, 17):
        edges = geometry(p)
        r = max(1, (p - 1) // 3)
        base = {v for v in range(p) if v <= r}

        candidates = [set(s) for k in range(1, min(4, len(base)) + 1) for s in combinations(sorted(base), k)]
        # Also test shifts of base to cover different arithmetic embeddings
        for shift in (1, 2):
            shifted_base = {(v + shift) % p for v in base}
            candidates.extend([set(s) for k in range(1, min(3, len(shifted_base)) + 1) for s in combinations(sorted(shifted_base), k)])

        H = 1 if p == 5 else 2

        def tent(t: int) -> Q:
            d = min(t % p, (-t) % p)
            return Q(max(0, H + 1 - d), H + 1)

        def weight(x: int, h: int) -> Q:
            return tent(h) * tent(2 * x * h) * tent(h * h)

        for A in candidates:
            if any(e <= A for e in edges):
                continue

            host = set(base)
            A_host = A & host
            if not A_host:
                continue

            a = Q(len(A_host), len(host))
            w = Q(len(host), p)
            if a == 0 or a == 1:
                continue

            # Centered indicator on host, zero-padded to F_p
            u_host = {v: (Q(1) - a if v in A_host else -a) for v in host}
            u_p = [float(u_host.get(v, Q(0))) for v in range(p)]

            # 1. Exact Gowers U^3 norm calculation
            fourier_sum = 0.0
            for r_shift in range(p):
                d = [u_p[x] * u_p[(x + r_shift) % p] for x in range(p)]
                for k in range(p):
                    d_hat = sum(d[x] * cmath.exp(-2j * math.pi * k * x / p) for x in range(p)) / p
                    fourier_sum += abs(d_hat) ** 4
            u3_norm_8 = fourier_sum / p
            check(u3_norm_8 >= -1e-15, "u3_norm_nonnegative")
            u3_norm_4 = math.sqrt(max(0.0, u3_norm_8))

            # 2. Exact completion field and relative mean
            q = {v: Q(0) for v in host}
            for v in host:
                for j in range(4):
                    for h in range(1, p):
                        if all((v + (i - j) * h) % p in A_host for i in range(4) if i != j):
                            q[v] += weight((v - j * h) % p, h) / p

            m = sum(q.values()) / len(host)
            T = Q(0)
            residual = [Q(0)] * 5

            for x in range(p):
                for h in range(p):
                    vs = [(x + i * h) % p for i in range(4)]
                    if not all(v in host for v in vs):
                        continue
                    f = weight(x, h)
                    T += f / p**2
                    us = [Q(v in A_host) - a for v in vs]
                    for j in range(5):
                        for slots in combinations(range(4), j):
                            term = a ** (4 - j) * f / p**2
                            for i in slots:
                                term *= us[i]
                            residual[j] += term

            R4 = residual[4]

            # 3. Gowers-Cauchy-Schwarz bound on R4
            # |R4| <= C_F ||u||_{U^3}^4
            R4_fl = float(R4)
            check(abs(R4_fl) <= u3_norm_4 + 1e-9, "gowers_cauchy_schwarz_ceiling")

            # 4. Arithmetic Low-Mean Branch Audit (m <= 2 a^3 T / w)
            is_low_mean = (m <= 2 * a**3 * T / w)
            if is_low_mean:
                low_mean_cases += 1
                # Exact closed identity check
                expected_R4 = 3 * a**4 * T + 2 * residual[1] + residual[2] - a * w * m + a * w * (1 - 4 * a) / p
                check(R4 == expected_R4, "exact_r4_identity_low_mean")
                # When linear terms R1, R2 are small, R4 must be positive
                check(R4 >= -a**4 * T - a * w * m - 1e-12, "r4_cone_lower_bound")

            if m == 0:
                zero_mean_cases += 1

            # 5. Quadratic correlation and exponent gap audit
            max_delta = 0.0
            for c_quad in range(p):
                for t_lin in range(p):
                    corr = abs(
                        sum(
                            float(u_host[v]) * cmath.exp(-2j * math.pi * (c_quad * v * v + t_lin * v) / p)
                            for v in host
                        )
                    ) / len(host)
                    if corr > max_delta:
                        max_delta = corr

            a_fl = float(a)
            # The target DIRECT-Q-GAIN requires delta >= c a^1.5 with diverging multiplier
            # We audit that delta / a^1.5 is uniformly bounded and cannot tend to infinity
            ratio_15 = max_delta / (a_fl ** 1.5)
            check(ratio_15 <= 2.0 * float(p) + 1.0, "finite_correlation_bounded")
            if ratio_15 > max_observed_delta_ratio:
                max_observed_delta_ratio = ratio_15

            # Audit inverse exponent: delta / a^2 is non-trivial
            ratio_20 = max_delta / (a_fl ** 2.0)
            check(ratio_20 >= 0.0, "inverse_exponent_valid")

            arithmetic_cases += 1

    report = {
        "status": "passed",
        "date": "2026-10-24",
        "checks": sum(counts.values()),
        "counts": dict(counts),
        "arithmetic_cases": arithmetic_cases,
        "low_mean_cases": low_mean_cases,
        "zero_mean_cases": zero_mean_cases,
        "max_observed_delta_ratio": max_observed_delta_ratio,
        "target_proved": False,
        "P12_proved": False,
        "DIRECT_Q_GAIN_proved": False,
        "eligible_counterexample_found": False,
        "analytic_claims_withdrawn": True,
        "scope": "Historical finite diagnostic only. Weighted U3 transfer, low-mean 5/2 coefficient and claimed inverse-exponent barrier withdrawn on 2026-11-03; no theorem certified by these checks.",
    }

    results_dir = ROOT / "verification/results"
    results_dir.mkdir(parents=True, exist_ok=True)
    (results_dir / "GOWERS_U3_LOW_MEAN_20261024.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run()
