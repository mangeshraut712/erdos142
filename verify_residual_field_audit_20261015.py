"""Independent, deterministic finite audit; never an asymptotic proof.

Exact integer/Fraction checks and floating Fourier checks are reported separately.
No dependency on the legacy verifier implementations. Writes only the new JSON.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math

import numpy as np

ROOT = Path(__file__).resolve().parent
counts = Counter()
errors = Counter()
rng = np.random.default_rng(14220261015)

for prime in (7, 11, 13, 17, 29, 31, 37, 53, 101, 257, 1009, 10007, 100003):
    assert prime > 3 and all(prime % d for d in range(2, math.isqrt(prime)+1))
    counts['exact_prime_inputs'] += 1


def close(label, lhs, rhs, tol=3e-10):
    err = float(np.max(np.abs(np.asarray(lhs) - np.asarray(rhs))))
    errors[label] = max(errors[label], err)
    assert err < tol, (label, err)
    counts[label] += 1


def ap_free(A, p):
    return not any(all((x + j*d) % p in A for j in range(4))
                   for x in A for d in range(1, p))


# Independent integer tuple enumeration, including translated modular intervals.
for p in (7, 11, 17, 29, 37):
    for L in range(1, (p + 3)//4 + 1):
        for start in (0, p - 2):
            I = [(start + x) % p for x in range(L)]
            z = sum((z1-z2-3*(z4-z3)) % p == 0
                    for z1, z2, z3, z4 in product(I, repeat=4))
            M = (L-1)//3
            formula = L*L + 2*sum((L-u)*(L-3*u) for u in range(1, M+1))
            assert z == formula
            phi_m, phi_e = [], []
            for y in I:
                pm = sum((z1-z2-3*(y-z3)) % p == 0
                         for z1, z2, z3 in product(I, repeat=3))
                pe = sum((y-z3-3*(z1-z2)) % p == 0
                         for z1, z2, z3 in product(I, repeat=3))
                phi_m.append(pm); phi_e.append(pe)
            r = L - 3*M
            assert F(max(phi_m)) == F(L*L, 3) + F(r*(3-r), 3)
            assert F(max(phi_e)) <= F(11*L*L, 36) + F(2*L, 3) + F(1, 3)
            assert F(max(2*(a+b) for a, b in zip(phi_m, phi_e))) <= F(23*L*L, 18)+F(4*L, 3)+2
            counts['exact_interval_tuple_cases'] += 1


# Conditional-centering synthesis and relative/full-group normalization.
packet_records = []
for p, omega in [(7, list(range(7))), (11, list(range(11))),
                 (11, list(range(6))), (13, [0, 1, 2, 4, 5, 8, 9])]:
    n = len(omega); w = n/p
    E = np.exp(2j*np.pi*np.outer(np.arange(p), np.arange(p))/p)
    examples = [set(omega[i] for i in ids)
                for k in range(1, min(5, n)+1)
                for ids in combinations(range(n), k)]
    for A in examples:
        if not ap_free(A, p):
            continue
        B = np.array([int(x in A) for x in range(p)])
        qe = np.array([sum(B[(x+d)%p]*B[(x+2*d)%p]*B[(x+3*d)%p]
                           for d in range(1, p)) for x in range(p)])
        qm = np.array([sum(B[(x-d)%p]*B[(x+d)%p]*B[(x+2*d)%p]
                           for d in range(1, p)) for x in range(p)])
        assert not np.any(B*qe) and not np.any(B*qm)
        counts['exact_actual_APfree_completion_support'] += 1
        for labels in ([0]*n, [4*x//p for x in omega]):
            cells = [[x for x, lab in zip(omega, labels) if lab == z]
                     for z in sorted(set(labels))]
            g = np.zeros(p)
            for C in cells:
                g[C] = sum(int(B[x]) for x in C)/len(C)
            u = B-g; a = len(A)/n
            c = np.fft.fft(u)/n  # exactly uhat/w
            for lam in [(1, 0), (0, 1), (1, 1)]:
                q = (lam[0]*qe+lam[1]*qm)/p
                phi = np.zeros(p)
                phi[omega] = (g[omega] >= a/2)*q[omega]
                S = float(np.dot(g[omega], phi[omega])/n)
                fhat = np.fft.fft(phi)/p
                close('floating_relative_pairing', np.vdot(c[1:], fhat[1:]), -S)
                assert np.max(np.abs(fhat)) <= 2*w*S/a+3e-12
                centered_phi = phi[omega].copy()
                psi = E[:, omega].copy()
                for C in cells:
                    pos = [omega.index(x) for x in C]
                    centered_phi[pos] -= np.mean(phi[C])
                    psi[:, pos] -= np.mean(E[:, C], axis=1)[:, None]
                close('floating_conditional_synthesis', fhat[1:] @ psi[1:], centered_phi)
                if S <= 1e-13:
                    continue
                terms = np.conj(c[1:])*fhat[1:]
                order = np.argsort(-np.abs(terms))
                for s in sorted(set([1, min(3, p-1), p-1])):
                    ix = order[:s]+1
                    theta = min(1.0, abs(np.vdot(c[ix], fhat[ix]))/S)
                    assert np.sum(np.abs(c[ix]))+1e-11 >= theta*a/(2*w)
                    assert np.sum(np.abs(c[ix])**2)+1e-11 >= theta**2*a*a/(4*s*w*w)
                    assert np.max(np.abs(c[ix])**2)+1e-11 >= theta**2*a*a/(4*s*s*w*w)
                    counts['floating_packet_implication'] += 1
                if len(packet_records) < 5:
                    packet_records.append({'p': p, 'omega': omega, 'A': sorted(A),
                                           'lambda': lam, 'S': S})


# Exponents: test exact symbolic rational arithmetic, not fitted floating curves.
assert F(2)-2*F(-1, 4) == F(5, 2)
assert F(2)-F(2, 3)*F(-3, 4) == F(5, 2)
assert -F(2, 3)*F(-5, 2)-F(2, 3) == 1
assert F(1, 3)*F(-5, 2)-F(2, 3) == -F(3, 2)
counts['exact_exponent_identities'] = 4

# Full-group conditional Gram is <= I, and generally not I.
p = 11
E = np.exp(2j*np.pi*np.outer(np.arange(1, p), np.arange(p))/p)
psi = E.copy()
for label in range(4):
    C = [x for x in range(p) if 4*x//p == label]
    psi[:, C] -= E[:, C].mean(axis=1)[:, None]
G = psi.conj() @ psi.T/p
assert np.linalg.eigvalsh(G).min() > -1e-12
assert np.linalg.eigvalsh(np.eye(p-1)-G).min() > -1e-12
assert np.linalg.norm(G-np.eye(p-1)) > 0.1
counts['floating_conditional_Gram_order'] = 1


# Actual sparse Boolean examples; exact support tests plus floating spectra.
# This is outside the logarithmic-density admissibility regime.
def sparse_ap_free(A, p):
    return not any((2*y-x) % p in A and (3*y-2*x) % p in A
                   for x in A for y in A if x != y)


sparse_records = []
for p in (1009, 10007, 100003):
    for attempt in range(100):
        A = set(np.flatnonzero(rng.random(p) < p**(-0.6)).tolist())
        if not A or not sparse_ap_free(A, p):
            continue
        qe = np.zeros(p, dtype=np.int64)
        qm = np.zeros(p, dtype=np.int64)
        inv2 = pow(2, -1, p)
        for x in A:
            for y in A:
                if x == y:
                    continue
                if (2*y-x) % p in A:
                    qe[(2*x-y) % p] += 1
                if ((3*y-x)*inv2) % p in A:
                    qm[((x+y)*inv2) % p] += 1
        if qe.sum() == 0:
            continue
        break
    else:
        raise AssertionError(('no seeded sparse example', p))
    B = np.zeros(p); B[list(A)] = 1
    assert np.all(qe[list(A)] == 0) and np.all(qm[list(A)] == 0)
    a = len(A)/p
    uhat = np.fft.fft(B-a)/p
    qhat = np.fft.fft((qe+qm)/p)/p
    S = a*int((qe+qm).sum())/(p*p)
    close('floating_sparse_full_pairing', np.vdot(uhat[1:], qhat[1:]), -S)
    s = max(1, math.ceil(a**(-0.25)/math.log(2/a)))
    terms = np.abs(np.conj(uhat[1:])*qhat[1:])
    any_packet_upper = float(np.sum(np.sort(terms)[-s:])/S)
    rho = float(np.max(np.abs(uhat[1:])))
    assert any_packet_upper <= s*rho/a+1e-10
    sparse_records.append({'p': p, 'A': sorted(A), 'density': a,
                           'variance_trivial_factor': 0,
                           'endpoint_triple_count': int(qe.sum()),
                           'middle_triple_count': int(qm.sum()),
                           'packet_size': s,
                           'upper_bound_any_packet_capture_fraction': any_packet_upper,
                           'positivity_cap_upper_bound': s*rho/a,
                           'rho_squared': rho*rho,
                           'rho_squared_over_a_5_2_ell': rho*rho/(a**2.5*math.log(2/a)),
                           'admissible_target_density_claimed': False})
    counts['exact_sparse_actual_APfree_examples'] += 1


# Weighted progression family: exact integer counts and double-counting.
weighted_records = []
for p, L, H in [(31, 29, 1), (53, 40, 1), (101, 60, 2), (257, 100, 3)]:
    J = set(x % p for x in range(-H, H+1))
    eta = F(len(J), p)
    for c0, root, offset in [(1, 0, 0), (2, 3, 1), (p-1, p-2, p//3)]:
        q = [(c0*(x-root)**2+offset) % p for x in range(p)]
        Omega = {x for x in range(p) if q[x] < L}
        w = F(len(Omega), p)
        T, lower, nonzero = 0, 0, 0
        deg = [0]*p
        ignore = [[0]*p for _ in range(4)]
        actual_edges = []
        for x in range(p):
            for d in range(p):
                ell = 2*c0*(x-root)*d % p
                D = c0*d*d % p
                if ell not in J or D not in J:
                    continue
                vertices = [(x+j*d) % p for j in range(4)]
                assert all(q[vertices[j]] == (q[x]+j*ell+j*j*D)%p for j in range(4))
                for i, vtx in enumerate(vertices):
                    ignore[i][vtx] += 1
                if 12*H <= q[x] < L-12*H:
                    assert all(vtx in Omega for vtx in vertices)
                    lower += 1
                if not all(vtx in Omega for vtx in vertices):
                    continue
                T += 1
                if d:
                    nonzero += 1
                    actual_edges.append(vertices)
                    for vtx in vertices:
                        deg[vtx] += 1
        assert T >= lower
        assert T-nonzero == len(Omega)
        assert sum(deg) == 4*nonzero
        counts['exact_weighted_count_and_diagonal'] += 1
        K = 2+math.log(p)
        lo = F(L-24*H, p)*eta**2
        assert abs(float(F(lower, p*p)-lo)) <= K**3/math.sqrt(p)+1e-12
        for vtx in range(p):
            for i in range(4):
                if vtx != root:
                    assert abs(ignore[i][vtx]/p-float(eta**2)) <= K*K/math.sqrt(p)+1e-12
                else:
                    assert ignore[i][vtx] <= p
        counts['floating_Gauss_error_envelopes'] += 1
        for trial in range(4):
            order = list(Omega)
            rng.shuffle(order)
            A = set()
            for vtx in order:
                candidate = A | {vtx}
                if ap_free(candidate, p):
                    A = candidate
            holes = Omega-A
            hit = sum(deg[x] for x in holes)
            assert hit >= nonzero
            # Direct edge hole enumeration independently checks degree accumulation.
            assert hit == sum(sum(vtx in holes for vtx in edge) for edge in actual_edges)
            bound = 1-(float(lo)-K**3/math.sqrt(p)-(float(w)+4)/p)/(4*float(w)*(float(eta**2)+K*K/math.sqrt(p)))
            assert len(A)/len(Omega) <= bound+1e-12
            counts['exact_weighted_APfree_hitting'] += 1
        weighted_records.append({'p': p, 'L': L, 'H': H, 'c': c0,
                                 'root': root, 'offset': offset,
                                 'host_size': len(Omega), 'weighted_count_numerator': T,
                                 'interior_count_numerator': lower,
                                 'nonzero_weighted_count_numerator': nonzero,
                                 'max_degree_numerator': max(deg)})


# An independent m=5 incidence test of the finite-pattern extension.
# r_4(5)=4: all five contain a 4-AP, and {0,1,2,4} supplies the lower bound.
p, L, H, m, r_m = 101, 80, 1, 5, 4
q = [((x-7)**2+9) % p for x in range(p)]
Omega = {x for x in range(p) if q[x] < L}
J = {p-1, 0, 1}
edges = []
for x in range(p):
    for d in range(1, p):
        if 2*(x-7)*d % p not in J or d*d % p not in J:
            continue
        vertices = [(x+j*d) % p for j in range(m)]
        if all(v in Omega for v in vertices):
            edges.append(vertices)
assert edges, 'finite-pattern incidence test must contain nonzero progressions'
for trial in range(5):
    order = list(Omega); rng.shuffle(order)
    A = set()
    for x in order:
        if sparse_ap_free(A | {x}, p):
            A.add(x)
    assert all(sum(x in A for x in edge) <= r_m for edge in edges)
    assert sum(sum(x not in A for x in edge) for edge in edges) >= (m-r_m)*len(edges)
    counts['exact_finite_pattern_incidence'] += 1


# Small-host witness against an unqualified finite-p terminal density <4/5.
small_host = {'p': 7, 'q': 'x^2', 'I': [0], 'Omega': [0], 'A': [0],
              'relative_density': '1',
              'scope': 'Not a counterexample to the asymptotic theorem or r4 target.'}
assert ap_free({0}, 7)
assert [x for x in range(7) if x*x % 7 == 0] == [0]

legacy = ROOT/'history'/'audit_20261015_residual_field'
reruns = {}
for name in ['RESIDUAL_FIELD_AMPLIFICATION', 'QUADRATIC_TO_LINEAR_TRANSFER']:
    path = legacy/f'rerun_{name}_VERIFICATION_20261014.json'
    if path.exists():
        reruns[name] = json.loads(path.read_text())['counts']

output = {
    'date': '2026-10-15',
    'principal_status': 'D: NEW RIGOROUS PARTIAL THEOREM',
    'unconditional_r4_target': 'OPEN',
    'new_theorem': 'Localized weighted progressions give a<=3/4+o(1) in a single quadratic interval host under the stated size condition.',
    'asymptotic_evidence': 'Mathematical proof in QUADRATIC_LOCALIZATION_20261015.md; finite checks are not an asymptotic proof.',
    'counts': dict(counts),
    'max_floating_errors': dict(errors),
    'weighted_records': weighted_records,
    'sparse_records': sparse_records,
    'packet_examples': packet_records,
    'small_host_witness': small_host,
    'legacy_verifiers_rerun': reruns,
    'verification_limits': [
        'Weighted Gauss envelopes can be vacuous at tested small primes.',
        'No exhaustive large-prime or eligible-target-regime search.',
        'No proof of spectral packet existence.',
        'No re-audit of the full October 2 conditional iteration in this script.',
        'No pseudo-moment evaluation is classified as an actual Boolean set.'
    ],
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT/'RESIDUAL_FIELD_AUDIT_VERIFICATION_20261015.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps({'status': output['principal_status'], 'target': 'OPEN',
                  'counts': dict(counts), 'max_floating_errors': dict(errors)}, indent=2))
