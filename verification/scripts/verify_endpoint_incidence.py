# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Mangesh Raut

"""Exact finite diagnostics; run: python3 verify_endpoint_incidence.py."""
from collections import Counter
from fractions import Fraction
import json


def check(p, omega, x):
    shifts = [h for h in range(1, p)
              if all((x + j*h) % p in omega for j in range(4))]
    edges = [frozenset((x+j*h) % p for j in (1, 2, 3)) for h in shifts]
    assert len(set(edges)) == len(edges)
    degrees = Counter(y for e in edges for y in e)
    assert all(len(e) == 3 and x not in e for e in edges)
    assert max(degrees.values(), default=0) <= 3
    matching = []
    for e in edges:
        if all(not e & f for f in matching):
            matching.append(e)
    assert 7*len(matching) >= len(edges)
    vertices = sorted(set().union(*edges)) if edges else []
    counts = Counter()
    for mask in range(1 << len(vertices)):
        occupied = {y for i, y in enumerate(vertices) if mask >> i & 1}
        if all(not e <= occupied for e in edges):
            counts[len(occupied)] += 1
    for a in (Fraction(1, 4), Fraction(1, 2)):
        prob = sum(c*a**k*(1-a)**(len(vertices)-k) for k, c in counts.items())
        assert (1-a**3)**len(edges) <= prob
        assert prob <= (1-a**3)**len(matching)
    return len(edges)


def gram_check(p, omega):
    cols = [(u, v, (2*u-v) % p, (2*v-u) % p)
            for u in omega for v in omega if u != v
            and (2*u-v) % p in omega and (2*v-u) % p in omega]
    inv3 = pow(3, -1, p)
    cases = 0
    candidates = [set(), set(omega), {y for y in omega if y % 2 == 0}]
    greedy = set()
    for y in sorted(omega):
        candidate = greedy | {y}
        if not any({(z+j*h) % p for j in range(4)} <= candidate
                   for z in candidate for h in range(1, p)):
            greedy = candidate
    candidates.append(greedy)
    for a_set in candidates:
        selected = [(s, t) for u, v, s, t in cols if u in a_set and v in a_set]
        for y in omega:
            t_y = sum(all((y+j*h) % p in omega for j in range(4))
                      and (y+h) % p in a_set and (y+2*h) % p in a_set
                      for h in range(1, p))
            for z in omega:
                actual = sum(y in (s, t) and z in (s, t) for s, t in selected)
                expected = 2*t_y if y == z else 2*int(
                    (2*y+z)*inv3 % p in a_set and (y+2*z)*inv3 % p in a_set)
                assert actual == expected
                if a_set == greedy and y != z and y in a_set and z in a_set:
                    assert actual == 0
                cases += 1
        # With a_set=omega the weighted formula is the ambient formula.
    return cases


def main():
    stars = matrix_entries = 0
    for p in (5, 7, 11, 13):
        for omega in (set(range(p)), set(range(p//2+1))):
            for x in sorted({min(omega), max(omega), sorted(omega)[len(omega)//2]}):
                check(p, omega, x)
                stars += 1
            matrix_entries += gram_check(p, omega)
    print(json.dumps({"status": "passed", "exact_star_cases": stars,
                      "exact_gram_entries": matrix_entries,
                      "target_proved": False}, indent=2))


if __name__ == "__main__":
    main()
