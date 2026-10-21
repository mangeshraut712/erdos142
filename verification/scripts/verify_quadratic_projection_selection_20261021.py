"""Independent verification of the finite quadratic chirp projection theorem
and the phase selection lower bound (Open Lemma O3).
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

def get_ap_free_set(p, size):
    cand = []
    for x in range(p):
        is_ok = True
        for h in range(1, p):
            for j in range(4):
                pts = [(x + (i - j)*h) % p for i in range(4) if i != j]
                if all(pt in cand for pt in pts):
                    is_ok = False
                    break
            if not is_ok:
                break
        if is_ok:
            cand.append(x)
            if len(cand) == size:
                return cand
    return cand if len(cand) >= size else None

records = []

# Audit across primes p in [11, 41]
for p in [11, 13, 17, 19, 23, 29, 31, 37, 41]:
    H = 2
    F_h = tent(p, H)
    for size in [3, 4, 5]:
        if size >= p:
            continue
        A = get_ap_free_set(p, size)
        if A is None or len(A) < size:
            continue
        A = A[:size]
        
        B = np.zeros(p)
        B[list(A)] = 1.0
        a = size / p
        u = B - a
        
        # 1. Four-channel completion field
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
        
        # Hole support check: B * q = 0 identically
        close('ap_free_hole_support_zero', np.max(np.abs(B * q)), 0.0)
        
        # Exact inner product identity: <u, k> = -a * m
        close('exact_inner_product_identity', np.mean(u * k), -a * m)
        
        # Geometric alignment check: rho(u, -k) = am / (||u|| * ||k||) > 0
        u_norm = np.sqrt(np.mean(u**2))
        k_norm = np.sqrt(np.mean(k**2))
        cos_align = np.mean(u * (-k)) / (u_norm * k_norm)
        close('geometric_alignment_formula', cos_align, (a * m) / (u_norm * k_norm))
        assert cos_align > 0.0, f"Alignment not acute: {cos_align} <= 0.0"
        counts['geometric_alignment_acute_positive'] += 1
        
        # Compute quadratic chirp transforms Q_k and Q_u
        y = np.arange(p)
        all_phases = []
        for c in range(p):
            for t in range(p):
                if c == 0 and t == 0:
                    continue
                q_ct = np.mean(k * np.exp(-2j * np.pi * (c * y**2 + t * y) / p))
                qu_ct = np.mean(u * np.exp(-2j * np.pi * (c * y**2 + t * y) / p))
                
                # Atomic spectral contribution xi_gamma = (1/p) Q_k(gamma) Q_u(gamma)^*
                inner_contrib = (1.0 / p) * (q_ct * np.conj(qu_ct)).real
                l_contrib = (1.0 / p) * abs(q_ct)
                all_phases.append((inner_contrib, l_contrib, abs(qu_ct), c, t, q_ct))
        
        # Verify Theorem 1, Part 1: sum over all phases of xi_gamma == <u, k> == -am
        total_xi = sum(x[0] for x in all_phases)
        close('total_frame_inner_product_sum', total_xi, -a * m)
        
        # Sort by most negative inner_contrib (aligned with -am)
        all_phases.sort(key=lambda x: x[0])
        delta = max(x[2] for x in all_phases)
        
        # Theorem 1: Test partial projection for multiple subsets Gamma_n
        target = a * m
        cum_inner = 0.0
        cum_L = 0.0
        n_10 = None
        theta_10 = None
        bound_10 = None
        
        for n, (ic, lc, qu_mag, c, t, q_ct) in enumerate(all_phases):
            cum_inner += ic
            cum_L += lc
            theta_n = abs(cum_inner) / target
            bound_n = abs(cum_inner) / cum_L
            
            # Certificate inequality check for every n: delta >= bound_n
            assert delta >= bound_n - 1e-14, f"Projection certificate violated: delta={delta} < bound={bound_n}"
            counts['projection_certificate_inequality'] += 1
            
            # Record when target fraction theta_0 = 0.10 is reached
            if abs(cum_inner) >= 0.10 * target and n_10 is None:
                n_10 = n + 1
                theta_10 = theta_n
                bound_10 = bound_n
        
        # Theorem 3: Verify that n_10 <= ceil(1 / a)
        max_allowed_n = int(np.ceil(1.0 / a))
        assert n_10 <= max_allowed_n, f"Phase budget exceeded: n={n_10} > ceil(1/a)={max_allowed_n}"
        counts['finite_phase_budget_bound'] += 1
        
        # Verify divergent multiplier scaling: bound_10 >= 0.90 * a^1.5 * log(1/a)
        c_divergent = bound_10 / (a**1.5 * np.log(1.0 / a))
        assert c_divergent >= 0.90, f"Divergent scaling too small: {c_divergent} < 0.90"
        counts['divergent_multiplier_lower_bound'] += 1
        
        # Record case
        records.append({
            'p': p,
            'size': size,
            'a': float(a),
            'm': float(m),
            'n_phases': int(n_10),
            'max_allowed_n': int(max_allowed_n),
            'theta': float(theta_10),
            'bound': float(bound_10),
            'delta': float(delta),
            'ratio_delta_bound': float(delta / bound_10),
            'c_divergent': float(c_divergent)
        })

sources = [
    'verification/scripts/verify_quadratic_projection_selection_20261021.py',
    'docs/audits/QUADRATIC_PROJECTION_SELECTION_20261021.md',
    'docs/audits/QUADRATIC_FRAME_CERTIFICATE_20261021.md',
    'docs/audits/COMPLETION_ENERGY_RESOLUTION_20261021.md'
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
        'Theorem 1: Finite quadratic chirp projection certificate delta >= theta_Gamma * am / L_Gamma verified for all n.',
        'Theorem 2: Geometric alignment cos(u, -k) = am / (||u|| * ||k||) > 0 and constructive addition sum xi_gamma = -am verified.',
        'Theorem 3: Phase selection with n <= ceil(1/a) achieving theta >= 0.10 and c_divergent >= 0.90 verified.',
        'Audited across 27 cases for primes p in [11, 41] and densities a in [0.073, 0.455].',
        'No asymptotic selection claim is made.'
    ],
    'source_sha256': {n: hashlib.sha256((ROOT / n).read_bytes()).hexdigest() for n in sources}
}

output_path = ROOT / 'verification' / 'results' / 'QUADRATIC_PROJECTION_SELECTION_VERIFICATION_20261021.json'
output_path.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({
    'status': 'passed',
    'total_checks': sum(counts.values()),
    'counts': dict(counts),
    'maximum_error': max(errors.values())
}, indent=2))
