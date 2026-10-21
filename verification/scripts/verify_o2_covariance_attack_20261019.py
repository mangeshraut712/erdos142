"""Finite support for C19.2, C19.7--10 and C19.14--17; not an asymptotic proof."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import cmath
import json
import math
import random


Q = 101
MASK = frozenset((0, 1, 4, 6, 7, 9, 12, 14, 20, 26, 34, 35, 37, 38,
                  41, 42, 49, 55, 57, 66, 76, 77, 80, 82, 83, 85, 87, 96, 98))
B = F(len(MASK), Q)


@lru_cache(maxsize=None)
def translation_probability(residues):
    return F(sum(all((x-z) % Q in MASK for x in residues) for z in range(Q)), Q)


def weights(H):
    return [(h, F(H+1-abs(h), H+1)) for h in range(-H, H+1)]


def blocks(n, K):
    """Consecutive balanced blocks, with the longer blocks first."""
    small, extra = divmod(n, K)
    sizes = [small+(j < extra) for j in range(K)]
    labels = [j for j, size in enumerate(sizes) for _ in range(size)]
    return sizes, labels


def weighted_count(A, p, H):
    return sum((weight for h, weight in weights(H) for x in range(p)
                if all((x+i*h) % p in A for i in range(4))), F(0))/p**2


def run():
    checks = Counter()
    floating_checks = 0
    maximum_fourier_error = 0.0
    diagnostics = []

    def check(condition, category):
        assert condition, category
        checks[category] += 1

    check(len(MASK) == 29, "mask_size")
    for x in range(Q):
        for h in range(1, Q):
            check(not all((x+i*h) % Q in MASK for i in range(4)), "nonzero_mask_progressions")
        for h in range(Q):
            residues = tuple(sorted({(x+i*h) % Q for i in range(4)}))
            check(translation_probability(residues) == (B if h == 0 else 0),
                  "exact_translation_probabilities")
    rho = F(1, Q*B**3)
    check(rho == F(10201, 24389) < F(9, 20) < F(1, 2), "mask_ratio")
    # Distinct integer vertices can share a residue when q divides h.
    # Thinning is per vertex, so its exponent remains four in that case.
    for h in (Q, -Q, 2*Q, Q+1, Q-1):
        for x in range(Q):
            residues = tuple(sorted({(x+i*h) % Q for i in range(4)}))
            t = B/3
            probability = (t/B)**4*translation_probability(residues)
            check(probability == (t**4/B**3 if h % Q == 0 else 0),
                  "distinct_integer_vertices_same_block")

    # The formula handles H+1 divisible by q as well as the small H<q regime.
    for H in range(1, 1501):
        total = sum((weight for h, weight in weights(H) if h % Q == 0), F(0))
        z = F(H+1, Q)
        r = z - z.numerator//z.denominator
        check(total == z+r*(1-r)/z, "tent_multiple_identity")
        check(total <= z+1, "tent_multiple_bound")
        check(sum((weight for _, weight in weights(H)), F(0)) == H+1, "tent_total_mass")

    # These small fields test exact finite geometry, not the asymptotic density,
    # K=ceil(log(p)^(5/2)), or prescribed H of the existence theorem.
    for p in (53, 101, 149):
        n = p//4
        for K in (1, 2, 5):
            sizes, label = blocks(n, K)
            check(sum(sizes) == n and max(sizes)-min(sizes) <= 1, "balanced_blocks")
            for H in (1, 2, min(5, (n-1)//3)):
                if not (3*H < n and 2*H < p):
                    continue
                for t in (B/2, B/7):
                    total_expected = F(0)
                    crossing_expected = F(0)
                    w, mu = F(n, p), F(H+1, p)
                    for h, weight in weights(H):
                        crossings = 0
                        for x in range(n):
                            vertices = tuple(x+i*h for i in range(4))
                            if not all(0 <= y < n for y in vertices):
                                continue
                            if h == 0:
                                probability = t
                            else:
                                groups = {}
                                for y in vertices:
                                    groups.setdefault(label[y], []).append(y % Q)
                                probability = (t/B)**4
                                for residues in groups.values():
                                    probability *= translation_probability(tuple(sorted(set(residues))))
                                if len(groups) == 1:
                                    expected = t**4/B**3 if h % Q == 0 else F(0)
                                    check(probability == expected, "same_block_expectation")
                                else:
                                    crossings += 1
                                    check(probability <= (t/B)**4, "cross_block_probability")
                                    crossing_expected += weight*probability/p**2
                            total_expected += weight*probability/p**2
                        check(crossings <= 3*K*abs(h), "crossing_count")
                    check(crossing_expected <= (t/B)**4*F(3*K*H, p)*mu,
                          "weighted_crossing_expectation")
                    bound = t*w/p + t**4/B**3*w*(mu/Q+F(1, p)) + t**4/B**4*F(3*K*H, p)*mu
                    check(total_expected <= bound, "full_expectation_bound")
                    diagnostics.append({"p": p, "n": n, "K": K, "H": H, "t": str(t),
                                        "expected_count": str(total_expected), "upper_bound": str(bound)})

    rng = random.Random(20261019)
    for p in (29, 53, 101):
        n = p//4
        P = [int(x < n) for x in range(p)]
        for H in (1, max(1, (n-1)//4)):
            for trial in range(4):
                initial = {x for x in range(n) if rng.randrange(3) == 0}
                A = initial | {0, 1, 2, 3}
                a, w, mu = F(len(A), n), F(n, p), F(H+1, p)
                u = [F(int(x in A))-a*P[x] for x in range(p)]
                check(all(x in A for x in (0, 1, 2, 3)), "forced_nonzero_AP")
                before, after = weighted_count(initial, p, H), weighted_count(A, p, H)
                check(0 <= after-before <= 16*mu/p, "four_vertex_insertion_cost")
                for vertex in range(p):
                    for slot in range(4):
                        incident = sum((weight for h, weight in weights(H)
                                        if ((vertex-slot*h) % p+slot*h) % p == vertex), F(0))/p**2
                        check(incident == mu/p, "anchored_incident_mass")

                bnd = F(n-max(0, n-6*H), p)
                check(bnd <= F(6*H, p), "eroded_boundary_size")
                T = F(0)
                R = [F(0) for _ in range(5)]
                hosted_pairs = {pair: F(0) for pair in combinations(range(4), 2)}
                full_pairs = dict(hosted_pairs)
                for h, weight in weights(H):
                    for x in range(p):
                        v = [(x+i*h) % p for i in range(4)]
                        Ps, us = [P[y] for y in v], [u[y] for y in v]
                        coeff = [F(1)]
                        for Pi, ui in zip(Ps, us):
                            nxt = [F(0)]*(len(coeff)+1)
                            for degree, value in enumerate(coeff):
                                nxt[degree] += value*a*Pi
                                nxt[degree+1] += value*ui
                            coeff = nxt
                        for degree in range(5):
                            R[degree] += weight*coeff[degree]/p**2
                        T += weight*math.prod(Ps)/p**2
                        for pair in full_pairs:
                            value = weight*us[pair[0]]*us[pair[1]]/p**2
                            full_pairs[pair] += value
                            hosted_pairs[pair] += value*math.prod(Ps[j] for j in range(4) if j not in pair)
                check(R[0] == a**4*T, "constant_residual")
                check(sum(R) == after, "exact_residual_expansion")
                check(R[3]+R[4] == after-a**4*T-R[1]-R[2], "cubic_quartic_rearrangement")
                check((w-bnd)*mu <= T <= w*mu, "host_mass_bound")
                check(abs(R[1]) <= 4*a**3*mu*bnd, "linear_boundary_bound")
                check(R[2] >= -6*a**2*mu*bnd, "pair_boundary_bound")
                for pair in full_pairs:
                    check(full_pairs[pair] >= 0, "exact_full_pair_positivity")
                    check(abs(full_pairs[pair]-hosted_pairs[pair]) <= mu*bnd, "individual_pair_boundary")

                # Independent floating Fourier representation, explicitly not
                # an exact numerical certificate for the asymptotic theorem.
                uh = [sum(float(u[x])*cmath.exp(-2j*math.pi*r*x/p) for x in range(p))/p for r in range(p)]
                fh = [sum(float(weight)*cmath.exp(-2j*math.pi*r*h/p) for h, weight in weights(H))/p for r in range(p)]
                for value in fh:
                    assert abs(value.imag) < 1e-12 and value.real >= -1e-12
                    floating_checks += 1
                for pair, exact in full_pairs.items():
                    numeric = sum(fh[((pair[1]-pair[0])*r) % p]*abs(uh[r])**2 for r in range(p))
                    error = abs(numeric-float(exact))
                    maximum_fourier_error = max(maximum_fourier_error, error)
                    assert error < 1e-12
                    floating_checks += 1

    return {"status": "passed; finite supporting identities and diagnostics only",
            "checks": sum(checks.values())+floating_checks,
            "exact_checks": sum(checks.values()), "exact_checks_by_category": dict(checks),
            "floating_fourier_checks": floating_checks,
            "maximum_fourier_error": maximum_fourier_error,
            "mask": sorted(MASK), "rho": str(rho), "finite_expectation_cases": diagnostics,
            "finite_cases_satisfy_asymptotic_prescriptions": False,
            "forced_examples_are_AP_free": False,
            "asymptotic_existence_proved_by_script": False,
            "P12_or_target_proved": False,
            "scope": "Exact modular/Fraction finite checks plus separately labeled floating Fourier checks. The asymptotic auxiliary obstruction is established by the written argument; the constructed final sets contain a nonzero 4-AP and are not P12 counterexamples."}


if __name__ == "__main__":
    output = json.dumps(run(), indent=2)+"\n"
    (Path(__file__).resolve().parents[1] / "results" / "O2_COVARIANCE_ATTACK_VERIFICATION_20261019.json").write_text(output)
    print(output, end="")
