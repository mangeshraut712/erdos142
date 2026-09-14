# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Mangesh Raut

"""Exact finite checks of one cyclic-progression increment lemma.

These checks are not an asymptotic proof. The algebraic proof and the
obstructions to iteration are recorded in INCREMENT_ATTEMPT.md.
"""

from fractions import Fraction as F
from itertools import product
import json


def spectral_energy(bits):
    """Compute S = E_h (E_x f(x) f(x+h))^2 without Fourier radicals."""
    p, n = len(bits), sum(bits)
    correlations = [
        p * sum(bits[x] * bits[(x + h) % p] for x in range(p)) - n * n
        for h in range(p)
    ]
    return F(sum(c * c for c in correlations), p ** 5)


def best_half_progression(bits):
    """Exhaust all nonzero steps, starts, and both allowed lengths."""
    p, n = len(bits), sum(bits)
    short, long = (p - 1) // 2, (p + 1) // 2
    best_count, best_length, best_start, best_step = 0, short, 0, 1
    for step in range(1, p):
        ordered = [bits[(i * step) % p] for i in range(p)]
        count = sum(ordered[:short])
        for i in range(p):
            if count * best_length > best_count * short:
                best_count, best_length = count, short
                best_start, best_step = i * step % p, step
            # The complement is a progression of the same step and long length.
            if (n - count) * best_length > best_count * long:
                best_count, best_length = n - count, long
                best_start, best_step = (i + short) * step % p, step
            count += ordered[(i + short) % p] - ordered[i]
    points = [(best_start + j * best_step) % p for j in range(best_length)]
    assert len(set(points)) == best_length
    assert sum(bits[x] for x in points) == best_count
    return F(best_count, best_length), best_start, best_step, best_length, points


def is_4ap_free(bits):
    p = len(bits)
    return not any(
        all(bits[(x + j * d) % p] for j in range(4))
        for x in range(p) for d in range(1, p)
    )


def cross_check_computations():
    """Compare optimized computations with direct definitions on tiny groups."""
    checked = 0
    for p in (5, 7):
        for bits in product((0, 1), repeat=p):
            alpha = F(sum(bits), p)
            f = [bit - alpha for bit in bits]
            direct_energy = sum(
                (sum(f[x] * f[(x + h) % p] for x in range(p)) / p) ** 2
                for h in range(p)
            ) / p
            assert spectral_energy(bits) == direct_energy
            direct_max = max(
                F(sum(bits[(x + j * d) % p] for j in range(length)), length)
                for length in ((p - 1) // 2, (p + 1) // 2)
                for d in range(1, p) for x in range(p)
            )
            assert best_half_progression(bits)[0] == direct_max
            checked += 1
    return checked


def check_lemma(bits):
    p, n = len(bits), sum(bits)
    assert p > 3 and all(p % divisor for divisor in range(2, p))
    assert 0 < n < p and all(bit in (0, 1) for bit in bits)
    alpha, b = F(n, p), F(n * (p - n), p * p)
    energy = spectral_energy(bits)
    density, start, step, length, points = best_half_progression(bits)
    gain = density - alpha
    assert length in ((p - 1) // 2, (p + 1) // 2)
    assert energy > 0 and gain > 0
    # Both sides are nonnegative, so squaring removes the sole radical exactly.
    assert gain * gain >= energy / (9 * b), (p, bits, gain, energy, b)
    return {
        "p": p,
        "A": [x for x, bit in enumerate(bits) if bit],
        "alpha": str(alpha),
        "b": str(b),
        "S": str(energy),
        "progression": {"start": start, "step": step, "length": length,
                        "points": points},
        "density": str(density),
        "gain": str(gain),
        "gain_squared": str(gain * gain),
        "required_gain_squared": str(energy / (9 * b)),
    }


def main():
    cross_checked = cross_check_computations()
    groups = (5, 7, 11, 13)
    tested = ap_free_count = large_regime_count = 0
    for p in groups:
        for bits in product((0, 1), repeat=p):
            if sum(bits) in (0, p):
                continue
            check_lemma(bits)
            tested += 1
            if is_4ap_free(bits):
                ap_free_count += 1
                if sum(bits) ** 3 >= 2 * p * p:
                    large_regime_count += 1

    examples = []
    for p, points in ((5, (0, 1)), (7, (0, 1, 3)), (13, (0, 1, 3, 9))):
        bits = [int(x in points) for x in range(p)]
        assert is_4ap_free(bits)
        examples.append(check_lemma(bits))

    # All nonzero pair intersections equal one in the flat-spectrum example.
    flat_bits = [int(x in (0, 1, 3, 9)) for x in range(13)]
    assert all(sum(flat_bits[x] * flat_bits[(x + h) % 13] for x in range(13)) == 1
               for h in range(1, 13))
    assert spectral_energy(flat_bits) == F(108, 28561)

    # A valid increment can fail to preserve 4AP-freeness under cyclic reuse.
    original = [int(x in (6, 8, 9, 10)) for x in range(11)]
    assert is_4ap_free(original)
    reuse_example = check_lemma(original)
    assert reuse_example["progression"]["points"] == [6, 7, 8, 9, 10]
    pulled_back = [original[x] for x in reuse_example["progression"]["points"]]
    assert pulled_back == [1, 0, 1, 1, 1]
    assert not any(all(pulled_back[x + j * d] for j in range(4))
                   for x in range(5) for d in range(1, 5) if x + 3 * d < 5)
    wrapped = [0, 4, 3, 2]
    assert all(pulled_back[x] for x in wrapped)
    assert all((wrapped[i + 1] - wrapped[i]) % 5 == 4 for i in range(3))
    assert not is_4ap_free(pulled_back)

    print(json.dumps({
        "status": "finite increment checks passed; no asymptotic theorem established",
        "groups": groups,
        "nonempty_proper_subsets_checked": tested,
        "independent_direct_definition_cross_checks": cross_checked,
        "empty_full_subsets_excluded": 2 * len(groups),
        "nonempty_proper_4ap_free_subsets": ap_free_count,
        "4ap_free_subsets_with_p_alpha_cubed_at_least_two": large_regime_count,
        "counterexamples_to_increment_lemma": 0,
        "arithmetic": "exact integers and fractions; no floating point",
        "named_4ap_free_examples": examples,
        "cyclic_reuse_counterexample": {
            "original_increment": reuse_example,
            "index_set": [0, 2, 3, 4],
            "new_modulus": 5,
            "wrapped_4ap": wrapped,
            "integer_interval_4ap_free": True,
            "cyclic_4ap_free": False,
        },
        "out_of_scope_examples": [
            "Z_4 and Z_6: not prime groups; canonical atom checks retained",
            "g=(1,1/2,1/2,1/2,1/2): not an indicator; canonical rejection retained",
            "general spectral arrays: need not be spectra of indicators",
        ],
        "external_dependencies": [],
    }, indent=2))


if __name__ == "__main__":
    main()
