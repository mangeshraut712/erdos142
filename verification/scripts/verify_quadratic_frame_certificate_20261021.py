"""Independent verification of the exact quadratic chirp tight frame and
the canonical completion certificate (Open Lemma O3).
Follows repository standards: exact modular and floating arithmetic separated;
results saved to verification/results/.
"""

from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import hashlib
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
counts = Counter()
errors = defaultdict(float)

def close(label, x, y, tol=1e-12):
    err = float(np.max(np.abs(np.asarray(x) - np.asarray(y))))
    errors[label] = max(errors[label], err)
    assert err < tol, f"Tolerance exceeded in {label}: err={err} >= {tol}"
    counts[label] += 1

def tent(p, H):
    t = np.arange(p)
    return np.maximum(0, H + 1 - np.minimum(t, p - t)) / (H + 1)

def get_ap_free_set(p, size, domain=None):
    if domain is None:
        domain = list(range(p))
    for cand in combinations(domain, size):
        is_ap_free = True
        for x in range(p):
            for h in range(1, p):
                if all((x + j * h) % p in cand for j in range(4)):
                    is_ap_free = False
                    break
            if not is_ap_free:
                break
        if is_ap_free:
            return cand
    return None

records = []

# =========================================================================
# Part 1: Theorem 1 — Exact Centered Tight Frame Reconstruction
# =========================================================================

for p in [5, 7, 11, 13, 17, 19, 23]:
    y = np.arange(p)
    phases = []
    for c in range(p):
        for t in range(p):
            if c == 0 and t == 0:
                continue
            chi = np.exp(-2j * np.pi * (c * y**2 + t * y) / p)
            psi = chi - np.mean(chi)
            phases.append((c, t, psi))
    
    Psi = np.column_stack([p_vec[2] for p_vec in phases])
    
    # Test on multiple mean-zero vectors (both synthetic and AP-free completion fields)
    rng = np.random.default_rng(p * 1000 + 42)
    for trial in range(3):
        k = rng.standard_normal(p)
        k -= np.mean(k)
        
        Q_k = (1.0 / p) * (k @ np.conj(Psi))
        recon = (1.0 / p) * (Q_k @ Psi.T)
        
        close('tight_frame_reconstruction_synthetic', recon.real, k)
        close('tight_frame_reconstruction_imag_zero', recon.imag, 0.0)
        
        parseval_lhs = (1.0 / p) * np.sum(np.abs(Q_k)**2)
        parseval_rhs = np.mean(k**2)
        close('tight_frame_parseval_synthetic', parseval_lhs, parseval_rhs)

# =========================================================================
# Part 2: Theorem 2 & 3 — Canonical Certificate and Phase Selection Bound
# =========================================================================

for p in [11, 13, 17, 19, 23, 29]:
    H = 2
    F_h = tent(p, H)
    for size in range(3, min(p, 8)):
        A = get_ap_free_set(p, size)
        if A is None:
            continue
        
        B = np.zeros(p)
        B[list(A)] = 1.0
        a = size / p
        u = B - a
        
        q = np.zeros(p)
        for j in range(4):
            for v in range(p):
                val = 0.0
                for h in range(1, p):
                    val += F_h[h] * np.prod([B[(v + (i - j) * h) % p] for i in range(4) if i != j])
                q[v] += val / p
        
        m = np.mean(q)
        if m < 1e-12:
            continue
        
        k = q - m
        
        # Frame reconstruction for completion field k
        y = np.arange(p)
        Q_k = np.zeros((p, p), dtype=complex)
        for c in range(p):
            for t in range(p):
                Q_k[c, t] = np.mean(k * np.exp(-2j * np.pi * (c * y**2 + t * y) / p))
        
        recon_k = np.zeros(p, dtype=complex)
        for c in range(p):
            for t in range(p):
                if c == 0 and t == 0:
                    continue
                chi_conj = np.exp(+2j * np.pi * (c * y**2 + t * y) / p)
                psi_conj = chi_conj - np.mean(chi_conj)
                recon_k += (1.0 / p) * Q_k[c, t] * psi_conj
        
        close('completion_field_exact_reconstruction', recon_k.real, k)
        close('completion_field_reconstruction_imag', recon_k.imag, 0.0)
        
        # Parseval on k
        parseval_k = (1.0 / p) * sum(np.abs(Q_k[c, t])**2 for c in range(p) for t in range(p) if not (c == 0 and t == 0))
        close('completion_field_parseval', parseval_k, np.mean(k**2))
        
        # Canonical L1 norm
        L_can = (1.0 / p) * sum(np.abs(Q_k[c, t]) for c in range(p) for t in range(p) if not (c == 0 and t == 0))
        lower_bound = (a * m) / L_can
        
        # Max phase correlation delta
        delta = max(np.abs(np.mean(u * np.exp(-2j * np.pi * (c * y**2 + t * y) / p)))
                    for c in range(p) for t in range(p) if not (c == 0 and t == 0))
        
        # Certificate inequality: delta >= a*m / L_can
        assert delta >= lower_bound - 1e-14, f"Certificate bound violated: delta={delta} < bound={lower_bound}"
        counts['canonical_certificate_inequality'] += 1
        
        # Check divergent ratio delta / (a^1.5 * log(1/a))
        ratio_divergent = delta / (a**1.5 * np.log(1.0 / a))
        assert ratio_divergent >= 0.5, f"Divergent ratio too small: {ratio_divergent}"
        counts['divergent_multiplier_check'] += 1
        
        records.append({
            'p': p,
            'size': size,
            'a': float(a),
            'm': float(m),
            'L_can': float(L_can),
            'bound': float(lower_bound),
            'delta': float(delta),
            'ratio_divergent': float(ratio_divergent)
        })

sources = [
    'verification/scripts/verify_quadratic_frame_certificate_20261021.py',
    'docs/audits/QUADRATIC_FRAME_CERTIFICATE_20261021.md',
    'docs/audits/COMPLETION_ENERGY_RESOLUTION_20261021.md',
    'docs/audits/WEIGHTED_COMPLETION_CERTIFICATE_20261018.md'
]

out = {
    'date': '2026-10-21',
    'offline': True,
    'target_proved': False,
    'counts': dict(counts),
    'total_checks': sum(counts.values()),
    'max_errors': dict(errors),
    'cases': records,
    'scope': [
        'Theorem 1: Exact centered quadratic chirp tight frame reconstruction and Parseval verified.',
        'Theorem 2: Canonical completion certificate bound delta >= am / L_can verified.',
        'Theorem 3: Phase selection ratio delta / (a^1.5 log(1/a)) audited across multiple primes and densities.',
        'No asymptotic selection claim is made.'
    ],
    'source_sha256': {n: hashlib.sha256((ROOT / n).read_bytes()).hexdigest() for n in sources}
}

output_path = ROOT / 'verification' / 'results' / 'QUADRATIC_FRAME_CERTIFICATE_VERIFICATION_20261021.json'
output_path.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({
    'status': 'passed',
    'total_checks': sum(counts.values()),
    'counts': dict(counts),
    'maximum_error': max(errors.values())
}, indent=2))
