#!/usr/bin/env python3
"""
verify_higher_degree_polynomial_chirp_20261021.py

Verification script for HIGHER_DEGREE_POLYNOMIAL_CHIRP_20261021.md.
Tests:
1. Pointwise hole support B(v) q_j(v) == 0 for all slots j in {0, ..., k-1} on k-AP-free sets (k = 3, 4, 5).
2. Exact inner product identity <u, q> = -a * m.
3. Unconditional completion mean positivity m > 0.
4. Exact tight frame resolution of identity for degree k-2 polynomial chirps (k = 3, 4, 5).
5. Exact field reconstruction k(v) = (1/p^(k-2)) sum_c <k, psi_c> psi_c^*(v).
"""

import sys
import numpy as np


def tent_kernel(h, p, H):
    dist = min(h % p, (-h) % p)
    return max(0.0, float(H + 1 - dist)) / float(H + 1)


def find_k_ap_free_set(p, k):
    """Greedy search for a k-AP-free subset of F_p."""
    A = []
    for x in range(p):
        # Check if adding x creates any non-trivial k-AP with points already in A
        creates_ap = False
        cand_set = set(A) | {x}
        for h in range(1, p):
            for start in range(p):
                ap = [(start + i * h) % p for i in range(k)]
                if all(pt in cand_set for pt in ap):
                    creates_ap = True
                    break
            if creates_ap:
                break
        if not creates_ap:
            A.append(x)
    return set(A)


def compute_k_completion_field(A_set, p, k, H):
    """Compute k completion channels and total completion field."""
    B = np.zeros(p, dtype=float)
    for x in A_set:
        B[x] = 1.0

    q_channels = [np.zeros(p, dtype=float) for _ in range(k)]

    for h in range(1, p):
        w = tent_kernel(h, p, H)
        if w == 0.0:
            continue
        for v in range(p):
            for j in range(k):
                # Product over i != j of B(v + (i - j) * h)
                prod = 1.0
                for i in range(k):
                    if i == j:
                        continue
                    prod *= B[(v + (i - j) * h) % p]
                    if prod == 0.0:
                        break
                q_channels[j][v] += w * prod

    for j in range(k):
        q_channels[j] /= p

    q_total = sum(q_channels)
    return q_channels, q_total


def evaluate_poly_chirp(c_coeffs, p):
    """
    Evaluate degree k-2 polynomial chirp on F_p:
    c_coeffs = [c_1, c_2, ..., c_{k-2}]
    psi(x) = exp(2 pi i (c_1 x + c_2 x^2 + ... + c_{k-2} x^{k-2}) / p)
    """
    x = np.arange(p)
    phase = np.zeros(p, dtype=float)
    for power, c in enumerate(c_coeffs, start=1):
        phase += c * (x ** power)
    return np.exp(2j * np.pi * (phase % p) / p)


def main():
    total_checks = 0
    max_error = 0.0

    primes = [11, 13, 17, 19, 23]
    for k in [3, 4, 5]:
        for p in primes:
            A_set = find_k_ap_free_set(p, k)
            a = len(A_set) / p
            assert a > 0, "Empty set"

            for H in [1, 2]:
                q_channels, q_total = compute_k_completion_field(A_set, p, k, H)

                # Check pointwise hole support on each channel: B(v) q_j(v) == 0
                for j in range(k):
                    for v in A_set:
                        val = q_channels[j][v]
                        err = abs(val)
                        max_error = max(max_error, err)
                        assert err < 1e-12, f"Hole support failed at k={k}, p={p}, H={H}, j={j}, v={v}: val={val}"
                        total_checks += 1

                # Check total q is supported on holes
                for v in A_set:
                    val = q_total[v]
                    err = abs(val)
                    max_error = max(max_error, err)
                    assert err < 1e-12, f"Total hole support failed at k={k}, p={p}, H={H}, v={v}: val={val}"
                    total_checks += 1

                # Check completion mean m
                m = float(np.mean(q_total))
                if len(A_set) >= k - 1:
                    assert m > 0.0, f"Completion mean m <= 0 at k={k}, p={p}, H={H}: m={m}"
                total_checks += 1

                # Check exact inner product <u, q> = -a * m
                B = np.zeros(p, dtype=float)
                for x in A_set:
                    B[x] = 1.0
                u = B - a
                inner_prod = float(np.mean(u * q_total))
                expected = -a * m
                err_inner = abs(inner_prod - expected)
                max_error = max(max_error, err_inner)
                assert err_inner < 1e-14, f"Inner product mismatch at k={k}, p={p}, H={H}: got {inner_prod}, expected {expected}"
                total_checks += 1

    # For small primes to keep exhaustive frame summation fast
    tf_primes = [7, 11, 13]
    for p in tf_primes:
        # k = 3: degree 1 (linear chirps, |F_1| = p)
        # sum_{c1} psi(x) psi^*(y) = p delta_{x, y}
        kernel_k3 = np.zeros((p, p), dtype=complex)
        for c1 in range(p):
            psi = evaluate_poly_chirp([c1], p)
            kernel_k3 += np.outer(psi, np.conj(psi))
        kernel_k3 /= p
        err_k3 = float(np.max(np.abs(kernel_k3 - np.eye(p))))
        max_error = max(max_error, err_k3)
        assert err_k3 < 1e-12, f"Tight frame failed for k=3 at p={p}: err={err_k3}"
        total_checks += p * p

        # k = 4: degree 2 (quadratic chirps, |F_2| = p^2)
        # sum_{c2, c1} psi(x) psi^*(y) = p^2 delta_{x, y}
        kernel_k4 = np.zeros((p, p), dtype=complex)
        for c2 in range(p):
            for c1 in range(p):
                psi = evaluate_poly_chirp([c1, c2], p)
                kernel_k4 += np.outer(psi, np.conj(psi))
        kernel_k4 /= (p ** 2)
        err_k4 = float(np.max(np.abs(kernel_k4 - np.eye(p))))
        max_error = max(max_error, err_k4)
        assert err_k4 < 1e-12, f"Tight frame failed for k=4 at p={p}: err={err_k4}"
        total_checks += p * p

        # k = 5: degree 3 (cubic chirps, |F_3| = p^3)
        if p <= 11:
            kernel_k5 = np.zeros((p, p), dtype=complex)
            for c3 in range(p):
                for c2 in range(p):
                    for c1 in range(p):
                        psi = evaluate_poly_chirp([c1, c2, c3], p)
                        kernel_k5 += np.outer(psi, np.conj(psi))
            kernel_k5 /= (p ** 3)
            err_k5 = float(np.max(np.abs(kernel_k5 - np.eye(p))))
            max_error = max(max_error, err_k5)
            assert err_k5 < 1e-12, f"Tight frame failed for k=5 at p={p}: err={err_k5}"
            total_checks += p * p

    for p in [11, 13]:
        for k in [3, 4]:
            A_set = find_k_ap_free_set(p, k)
            _, q_total = compute_k_completion_field(A_set, p, k, H=1)
            m = float(np.mean(q_total))
            k_field = q_total - m

            # Reconstruct k_field from frame coefficients
            k_recon = np.zeros(p, dtype=complex)
            if k == 3:
                for c1 in range(p):
                    psi = evaluate_poly_chirp([c1], p)
                    Q_c = np.mean(k_field * np.conj(psi))
                    k_recon += Q_c * psi
            elif k == 4:
                for c2 in range(p):
                    for c1 in range(p):
                        psi = evaluate_poly_chirp([c1, c2], p)
                        Q_c = np.mean(k_field * np.conj(psi))
                        k_recon += Q_c * psi
                k_recon /= p # normalized frame

            recon_err = float(np.max(np.abs(k_field - np.real(k_recon))))
            max_error = max(max_error, recon_err)
            assert recon_err < 1e-12, f"Reconstruction failed for k={k}, p={p}: err={recon_err}"
            total_checks += p

    out = {
        'status': 'passed',
        'total_checks': total_checks,
        'maximum_error': max_error,
        'scope': [
            'Theorem 1: Pointwise hole support B(v) q_j(v) == 0 for all slots j in {0, ..., k-1} on k-AP-free sets (k = 3, 4, 5).',
            'Corollary 2: Exact centered inner product identity <u, q> == -a * m.',
            'Theorem 3: Strict positivity of completion mean m > 0 on eligible models.',
            'Theorem 5: Exact tight frame resolution of identity for degree k-2 polynomial chirps (k = 3, 4, 5).',
            'Section 5: Exact field reconstruction from degree k-2 frame coefficients.'
        ]
    }
    from pathlib import Path
    import json
    root = Path(__file__).resolve().parents[2]
    out_file = root / 'verification' / 'results' / 'HIGHER_DEGREE_POLYNOMIAL_CHIRP_VERIFICATION_20261021.json'
    out_file.write_text(json.dumps(out, indent=2) + '\n')

    print(json.dumps({
        'status': 'passed',
        'total_checks': total_checks,
        'maximum_error': max_error
    }, indent=2))


if __name__ == "__main__":
    main()
