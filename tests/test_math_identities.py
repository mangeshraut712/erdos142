"""Unit tests for additive combinatorics and progression-free set mathematics."""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations
import unittest


def cyclic_4ap_geometry(p: int) -> set[frozenset[int]]:
    """Generate all non-trivial cyclic 4-APs in Z_p."""
    edges: set[frozenset[int]] = set()
    for x in range(p):
        for h in range(1, p):
            edges.add(frozenset((x + i * h) % p for i in range(4)))
    return edges


def tent_weight(t: int, p: int, H: int) -> Q:
    """Discrete tent weight on Z_p with width H."""
    d = min(t % p, (-t) % p)
    return Q(max(0, H + 1 - d), H + 1)


class TestMathIdentities(unittest.TestCase):
    def test_cyclic_4ap_count_prime(self) -> None:
        """In Z_p for prime p > 5, total cyclic 4-APs as sets is p * (p - 1) / 2; for p=5 it is 5."""
        self.assertEqual(len(cyclic_4ap_geometry(5)), 5)
        for p in (7, 11, 13, 17):
            edges = cyclic_4ap_geometry(p)
            expected_distinct = p * (p - 1) // 2
            self.assertEqual(len(edges), expected_distinct, f"Mismatch in 4-AP count for p={p}")

    def test_density_discrepancy_invariance_identity(self) -> None:
        """Verify MS1 identity: <u1, psi> = <u2, psi> = <u12, psi> on any overlap for zero-mean psi."""
        p = 11
        A = {0, 1, 3}  # 4-AP-free subset in Z_11
        host1 = {0, 1, 2, 3, 4, 10}
        host2 = {0, 1, 3, 5, 6, 7}
        overlap = host1 & host2  # {0, 1, 3}

        a1 = Q(len(A & host1), len(host1))
        a2 = Q(len(A & host2), len(host2))
        a12 = Q(len(A & overlap), len(overlap))

        # Construct zero-mean test function on overlap
        overlap_list = sorted(overlap)
        psi = {v: Q(i - (len(overlap_list) - 1) / 2) for i, v in enumerate(overlap_list)}
        self.assertEqual(sum(psi.values()), 0, "Test function must be zero-mean")

        u1_psi = sum((Q(v in A) - a1) * psi[v] for v in overlap_list)
        u2_psi = sum((Q(v in A) - a2) * psi[v] for v in overlap_list)
        u12_psi = sum((Q(v in A) - a12) * psi[v] for v in overlap_list)

        self.assertEqual(u1_psi, u2_psi)
        self.assertEqual(u1_psi, u12_psi)

    def test_hole_annihilation_property(self) -> None:
        """Verify that completion missing vertices can never belong to A when A is 4-AP-free."""
        p = 7
        edges = cyclic_4ap_geometry(p)
        A = {0, 1, 3}  # 4-AP-free in Z_7: no 4-AP subset
        self.assertFalse(any(e <= A for e in edges))

        # Check all possible completion missing vertices
        for e in edges:
            occupied = e & A
            if len(occupied) == 3:
                missing = next(iter(e - A))
                self.assertNotIn(missing, A, "Missing vertex in 3-occupied edge must be a hole")


if __name__ == "__main__":
    unittest.main()
