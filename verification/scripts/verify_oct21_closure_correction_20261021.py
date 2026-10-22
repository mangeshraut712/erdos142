#!/usr/bin/env python3
"""Finite diagnoses of overclaims in the October 21 closure attempt.

Exact Fraction/modular checks are separated from numerical chirp checks.
These examples fail T5 and the original H prescription. They refute broad
auxiliary assertions, not the eligible DIRECT-Q-GAIN or P12 statements.
"""
from collections import Counter
from fractions import Fraction
from math import floor, log, prod
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def run():
    counts = Counter()
    exact_records = []
    numerical_records = []
    fourth_moment_records = []

    def exact_check(condition, label):
        assert condition, label
        counts['exact_' + label] += 1

    def build(p, points, H):
        A = frozenset(points)
        a = Fraction(len(A), p)
        B = [int(x in A) for x in range(p)]
        for x in range(p):
            for h in range(1, p):
                exact_check(not all((x+i*h) % p in A for i in range(4)),
                            'nonzero_AP_exclusion')
        q = []
        for v in range(p):
            value = Fraction(0)
            for j in range(4):
                for h in range(1, p):
                    weight = Fraction(max(0, H+1-min(h, p-h)), H+1)
                    value += weight * prod(B[(v+(i-j)*h) % p] for i in range(4) if i != j) / p
            q.append(value)
            exact_check(B[v] * value == 0, 'pointwise_hole_support')
        m = sum(q) / p
        exact_check(m > 0, 'positive_mean_in_test_case')
        u = [Fraction(b) - a for b in B]
        k = [v-m for v in q]
        inner = sum(v*t for v, t in zip(u, k))/p
        u2 = sum(v*v for v in u)/p
        k2 = sum(v*v for v in k)/p
        z = [v + m*t/(1-a) for v, t in zip(k, u)]
        z2 = sum(v*v for v in z)/p
        exact_check(sum(k) == 0, 'centered_completion')
        exact_check(inner == -a*m, 'inner_product_identity')
        exact_check(u2 == a*(1-a), 'indicator_variance')
        exact_check(sum(v*t for v, t in zip(u, z)) == 0, 'orthogonal_residual')
        exact_check(k2 == a*m*m/(1-a)+z2, 'variance_decomposition')
        # Full-group presentation r=1: even this minimal T5 budget fails.
        L = log(p)
        prescribed_H = floor(float(a*a) * p / (48*L))
        t5_left = log(48)+log(L)
        t5_right = L/100
        assert prescribed_H == 0 and H > 0 and t5_left > t5_right
        counts['floating_eligibility_diagnoses'] += 1
        record = {
            'p': p, 'A': sorted(A), 'tested_H': H, 'a': str(a), 'm': str(m),
            'norm_k_squared': str(k2), 'projection_lower_bound_squared': str(a*m*m/(1-a)),
            'orthogonal_residual_squared': str(z2), 'correlation_squared': str(inner*inner/(u2*k2)),
            'original_prescribed_H': prescribed_H,
            'T5_minimal_rank_left': t5_left, 'T5_right': t5_right,
            'satisfies_T5': False, 'uses_original_prescribed_weight': False,
            'eligible_target_domain_counterexample': False,
        }
        exact_records.append(record)
        return a, m, u, k, k2, record

    a, m, u, k, k2, rec = build(11, [0, 1, 2], 2)
    exact_check(m == Fraction(8, 363), 'p11_mean_value')
    exact_check(k2 == Fraction(32, 14641), 'p11_variance_value')
    lower = a*m*m/(1-a)
    exact_check(lower == Fraction(8, 43923), 'p11_projection_value')
    exact_check(k2/lower == 12, 'p11_reversed_bound_counterexample')
    rec['actual_over_purported_upper_bound_squared'] = '12'

    a, m, u, k, k2, rec = build(5, [0, 1, 2], 1)
    u2 = sum(v*v for v in u)/5
    inner = sum(v*t for v, t in zip(u, k))/5
    corr2 = inner*inner/(u2*k2)
    exact_check(corr2 == 1, 'p5_correlation_value')
    exact_check((1-a)**2 == Fraction(4, 25), 'p5_claimed_correlation_bound')
    exact_check(corr2 > (1-a)**2, 'p5_correlation_bound_counterexample')
    rec['purported_correlation_upper_bound_squared'] = '4/25'

    # The first case already occurs in the published 27-case sample; QP3
    # allows theta0=1/4, while that verifier only tested theta0=0.10.
    for p, A, target in [
        (13, [0, 1, 2, 4, 5], 0.25),
        (101, [0, 1, 2, 4, 5, 7, 8, 9, 14, 15, 16, 18, 25, 26, 28], 0.10),
    ]:
        a, m, u, k, k2, _ = build(p, A, 2)
        x = np.arange(p)
        ku = np.asarray([float(v) for v in k])
        uu = np.asarray([float(v) for v in u])
        phases = []
        parseval = 0.0
        for c in range(p):
            modulation = np.exp(-2j*np.pi*((c*x*x) % p)/p)
            qk = np.fft.fft(ku*modulation)/p
            qu = np.fft.fft(uu*modulation)/p
            for t in range(p):
                if c == 0 and t == 0:
                    continue
                xi = qk[t]*np.conj(qu[t])/p
                parseval += abs(qk[t])**2/p
                phases.append((xi, c, t))
        spectral_error = abs(sum(v[0] for v in phases)+float(a*m))
        parseval_error = abs(parseval-float(k2))
        assert spectral_error < 1e-12 and parseval_error < 1e-12
        counts['floating_full_frame_and_inner_product'] += 2
        phases.sort(key=lambda row: (row[0].real, row[1], row[2]))
        budget = (p+len(A)-1)//len(A)
        partial = 0j
        capture_complex = []
        capture_real = []
        direct_error = 0.0
        for xi, c, t in phases[:budget]:
            chi = np.exp(-2j*np.pi*((c*x*x+t*x) % p)/p)
            direct_xi = np.mean(ku*chi)*np.conj(np.mean(uu*chi))/p
            direct_error = max(direct_error, abs(xi-direct_xi))
            partial += xi
            capture_complex.append(abs(partial)/float(a*m))
            capture_real.append(abs(partial.real)/float(a*m))
        # Large margins distinguish these diagnoses from rounding artifacts.
        assert direct_error < 1e-12
        assert max(capture_complex) < target-0.05
        assert max(capture_real) < target-0.05
        counts['floating_phase_budget_diagnoses'] += 3
        numerical_records.append({
            'p': p, 'A': A, 'tested_H': 2, 'phase_budget_ceil_inverse_a': budget,
            'claimed_capture_target': target,
            'max_complex_capture_over_allowed_prefixes': max(capture_complex),
            'max_real_capture_over_allowed_prefixes': max(capture_real),
            'complex_capture_at_budget': capture_complex[-1],
            'real_capture_at_budget': capture_real[-1],
            'spectral_inner_product_error': spectral_error,
            'frame_parseval_error': parseval_error,
            'selected_phase_direct_DFT_error': direct_error,
            'scope': 'Numerical countercheck of the broad finite phase-budget claim; not an eligible asymptotic counterexample.'
        })

    # Quadratic-parabola orthogonality converts the full fourth moment to
    # the number of ordered equal-sum/equal-square pairs divided by p^2.
    # Test arbitrary Boolean sets, including AP-rich sets; no AP exclusion
    # is used for this identity. Direct solution classification also checks
    # the unordered-pair characterization underlying the closed formula.
    for p in (5, 7, 11, 13):
        subsets = [set(), {0}, {0, 1}, {0, 1, 2, 3}, set(range(p)),
                   set(range(1, p, 2)), {x*x % p for x in range(p)}]
        for A in subsets:
            n = len(A)
            alpha = Fraction(n, p)
            solution_count = 0
            for x0 in A:
                for x1 in A:
                    for x2 in A:
                        for x3 in A:
                            if ((x0+x1-x2-x3) % p == 0
                                    and (x0*x0+x1*x1-x2*x2-x3*x3) % p == 0):
                                solution_count += 1
                                exact_check(sorted((x0, x1)) == sorted((x2, x3)),
                                            'fourth_moment_equal_pair_classification')
            exact_check(solution_count == 2*n*n-n, 'fourth_moment_solution_count')
            full_moment = Fraction(solution_count, p*p)
            exact_check(full_moment == 2*alpha*alpha-alpha/p,
                        'universal_boolean_fourth_moment')
            nonzero_moment = full_moment-alpha**4
            exact_check(nonzero_moment == 2*alpha*alpha-alpha/p-alpha**4,
                        'nonzero_boolean_fourth_moment')
            has_nonzero_AP = any(all((x+i*h) % p in A for i in range(4))
                                 for x in A for h in range(1, p))
            fourth_moment_records.append({
                'p': p, 'A': sorted(A), 'size': n,
                'contains_nonzero_4AP': has_nonzero_AP,
                'equal_sum_equal_square_ordered_solutions': solution_count,
                'closed_solution_count_2n_squared_minus_n': 2*n*n-n,
                'full_fourth_moment': str(full_moment),
                'nonzero_fourth_moment': str(nonzero_moment),
                'arithmetic': 'Exact integer solution enumeration and Fraction normalization.'
            })
    exact_check(any(r['contains_nonzero_4AP'] for r in fourth_moment_records),
                'fourth_moment_includes_AP_rich_examples')

    return {
        'status': 'passed', 'date': '2026-10-21', 'checks': sum(counts.values()),
        'counts': dict(counts), 'exact_case_records': exact_records,
        'floating_phase_budget_records': numerical_records,
        'universal_boolean_fourth_moment_records': fourth_moment_records,
        'target_proved': False, 'DIRECT_Q_GAIN_proved': False, 'P12_refuted': False,
        'eligible_asymptotic_counterexample_found': False,
        'scope': [
            'Exact modular enumeration verifies AP exclusion for these finite sets.',
            'Fraction arithmetic verifies completion fields, orthogonal variance decomposition, and counterexamples to reversed variance and correlation bounds.',
            'Separately labeled floating calculations diagnose broad finite phase-budget overclaims with large numerical margins.',
            'Exact finite solution enumeration supports the universal Boolean fourth-moment identity; AP exclusion is not needed for that identity.',
            'All examples fail T5 and use H greater than the prescribed zero radius; they do not refute an eligible asymptotic statement.',
            'No finite test here proves an asymptotic selection theorem or closes the research target.'
        ]
    }


if __name__ == '__main__':
    report = run()
    out = ROOT/'verification/results/OCT21_CLOSURE_CORRECTION_VERIFICATION_20261021.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
