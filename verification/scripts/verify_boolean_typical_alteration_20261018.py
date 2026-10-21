"""Finite checks for TA1--TA14; no finite sample certifies target-domain eligibility."""
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path

import numpy as np


def ap_edges(p):
    return sorted({sum(1 << ((x+j*h) % p) for j in range(4))
                   for x in range(p) for h in range(1, p)})


def incidence(p, edges):
    return [[e ^ (1 << v) for e in edges if e & (1 << v)] for v in range(p)]


def degrees(mask, triples):
    return [sum(mask & edge == edge for edge in family) for family in triples]


def altered(mask, edges):
    removed = 0
    for e in edges:
        if mask & e == e:
            removed |= e
    return mask & ~removed


def run():
    counts = Counter()
    maximum_error = 0.0
    geometry, cubes, samples = [], [], []

    def require(ok, label):
        assert ok, label
        counts[label] += 1

    for p in (5, 7, 11, 17, 31, 43):
        edges = ap_edges(p)
        families = incidence(p, edges)
        max_codegree = max_intersection_degree = max_colors = 0
        for family in families:
            codegrees = [sum(bool(e & (1 << v)) for e in family) for v in range(p)]
            max_codegree = max(max_codegree, max(codegrees))
            require(max(codegrees) <= 12, "exact_codegree_bound")
            colors = []
            for i, e in enumerate(family):
                neighbors = [j for j, f in enumerate(family) if j != i and e & f]
                max_intersection_degree = max(max_intersection_degree, len(neighbors))
                require(len(neighbors) <= 33, "exact_intersection_degree_bound")
                forbidden = {colors[j] for j in neighbors if j < i}
                color = next(c for c in range(34) if c not in forbidden)
                colors.append(color)
            max_colors = max(max_colors, 1+max(colors, default=-1))
            require(max_colors <= 34, "exact_greedy_coloring")
            require(len(family) <= 4*(p-1), "exact_incident_count")
        geometry.append({"p": p, "distinct_AP_sets": len(edges),
                         "max_codegree": max_codegree,
                         "max_intersection_degree": max_intersection_degree,
                         "colors_used": max_colors})

    for p in (5, 7, 11):
        edges = ap_edges(p)
        families = incidence(p, edges)
        all_masks = list(range(1 << p))
        out = [altered(m, edges) for m in all_masks]
        deg = [degrees(m, families) for m in all_masks]
        for m in all_masks:
            require(not any(out[m] & e == e for e in edges), "exact_AP_free_output")
            by_degree = sum(1 << v for v in range(p) if m & (1 << v) and deg[m][v] == 0)
            require(by_degree == out[m], "exact_deletion_rule")
            for v in range(p):
                require(deg[m][v] == deg[m ^ (1 << v)][v], "exact_own_coordinate_independence")
            shifted = ((m << 1) & ((1 << p)-1)) | (m >> (p-1))
            expected = ((out[m] << 1) & ((1 << p)-1)) | (out[m] >> (p-1))
            require(out[shifted] == expected, "exact_translation_equivariance")
        cap_results = []
        for cap in (0, 1, 2):
            good = [m for m in all_masks if max(deg[m]) <= cap]
            pairs = 0
            for index, m in enumerate(good):
                for n in good[index:]:
                    require((out[m] ^ out[n]).bit_count()
                            <= (1+3*cap)*(m ^ n).bit_count(), "exact_global_good_endpoint_Lipschitz")
                    pairs += 1
            cap_results.append({"degree_cap": cap, "good_samples": len(good), "pairs": pairs})
        # Exact translation-invariant expectation and independence at t=1/4.
        denominator = 4**p
        masses = [3**(p-m.bit_count()) for m in all_masks]
        means = [Fraction(sum(masses[m] for m in all_masks if out[m] & (1 << v)), denominator)
                 for v in range(p)]
        require(len(set(means)) == 1, "exact_uniform_mean")
        for v in range(p):
            pzero = Fraction(sum(masses[m] for m in all_masks if deg[m][v] == 0), denominator)
            require(means[v] == pzero/4, "exact_mean_completion_independence")
        require(means[0] >= Fraction(1, 4)*(1-Fraction(4*p, 4**3)), "exact_mean_union_bound")
        cubes.append({"p": p, "all_samples": len(all_masks), "good_endpoint_tests": cap_results,
                      "exact_expected_density_at_t_quarter": str(means[0])})

        if p <= 7:
            cap, L = 1, 4
            good = [m for m in all_masks if max(deg[m]) <= cap]
            z = [(v % 3)-1 for v in range(p)]
            f = [sum(z[v] for v in range(p) if out[m] & (1 << v)) for m in all_masks]
            ext = [max(-p, min(p, min(f[n]+L*(m ^ n).bit_count() for n in good))) for m in all_masks]
            for m in all_masks:
                if m in good:
                    require(ext[m] == f[m], "exact_McShane_agreement")
                for v in range(p):
                    require(abs(ext[m]-ext[m ^ (1 << v)]) <= L, "exact_McShane_edge_bound")
            ef = Fraction(sum(masses[m]*f[m] for m in all_masks), denominator)
            ee = Fraction(sum(masses[m]*ext[m] for m in all_masks), denominator)
            bad = Fraction(sum(masses[m] for m in all_masks if m not in good), denominator)
            require(abs(ef-ee) <= 2*p*bad, "exact_extension_mean_error")

            def conditional(prefix, n):
                return Fraction(sum(ext[prefix | (suffix << n)] * 3**(p-n-suffix.bit_count())
                                    for suffix in range(1 << (p-n))), 4**(p-n))

            for n in range(p):
                for prefix in range(1 << n):
                    before = conditional(prefix, n)
                    off = conditional(prefix, n+1)
                    on = conditional(prefix | (1 << n), n+1)
                    delta = on-off
                    require(abs(delta) <= L, "exact_Doob_conditional_Lipschitz")
                    require(off-before == -delta/4 and on-before == 3*delta/4,
                            "exact_Doob_Bernoulli_increment")
                    require(Fraction(3, 16)*delta**2 <= Fraction(1, 4)*L**2,
                            "exact_Doob_conditional_variance")

    # Actual modular samples: delete ALL vertices belonging to any initial AP.
    rng = np.random.default_rng(18102026)
    coefficients = 0
    for p in (127, 257, 521):
        y = np.arange(p)
        for theta in (0.36, 0.45):
            t = p**(-theta)
            R = rng.random(p) < t
            removed = np.zeros(p, dtype=bool)
            initial = 0
            for h in range(1, p):
                starts = y[R & R[(y+h)%p] & R[(y+2*h)%p] & R[(y+3*h)%p]]
                initial += len(starts)
                for j in range(4):
                    removed[(starts+j*h)%p] = True
            A = R & ~removed
            final = sum(int(np.sum(A & A[(y+h)%p] & A[(y+2*h)%p] & A[(y+3*h)%p]))
                        for h in range(1, p))
            require(final == 0, "exact_sample_modular_AP_exclusion")
            require(bool(np.all(~A | R)), "exact_sample_subset")
            a = float(np.mean(A))
            u = A.astype(float)-a
            delta = 0.0
            for start in range(0, p, 32):
                c = np.arange(start, min(start+32, p))
                phase = np.exp(-2j*np.pi*((c[:, None]*y[None, :]**2)%p)/p)
                Q = np.fft.fft(phase*u, axis=1)/p
                delta = max(delta, float(np.max(abs(Q))))
                coefficients += Q.size
                row, col = len(c)-1, (start+19)%p
                direct = np.mean(u*np.exp(-2j*np.pi*((c[row]*y*y+col*y)%p)/p))
                err = float(abs(Q[row, col]-direct))
                maximum_error = max(maximum_error, err)
                require(err < 2e-12, "floating_FFT_direct_check")
            linear = np.fft.fft(u)/p
            require(abs(float(np.sum(abs(linear)**2))-a*(1-a)) < 2e-12, "floating_linear_Parseval")
            samples.append({"p":p, "theta":theta, "initial_size":int(np.sum(R)),
                            "final_size":int(np.sum(A)), "ordered_APs_initial":initial,
                            "ordered_APs_final":final, "density":a, "delta":delta,
                            "delta_over_a_three_halves":delta/a**1.5 if a else None,
                            "original_prescribed_H":math.floor(p*a*a/(48*math.log(p))),
                            "scope":"finite diagnostic, not target-domain or asymptotic certification"})

    return {"checks":sum(counts.values()), "checks_by_kind":dict(sorted(counts.items())),
            "chirp_coefficients_evaluated":coefficients, "maximum_FFT_direct_error":maximum_error,
            "geometry":geometry, "exhaustive_cubes":cubes, "actual_samples":samples,
            "scope":"exact arithmetic and finite-cube checks; numerical phases; asymptotic theorem proved in note"}


if __name__ == "__main__":
    result = json.dumps(run(), indent=2)+"\n"
    (Path(__file__).resolve().parents[1] / "results" / "BOOLEAN_TYPICAL_ALTERATION_VERIFICATION_20261018.json").write_text(result)
    print(result, end="")
