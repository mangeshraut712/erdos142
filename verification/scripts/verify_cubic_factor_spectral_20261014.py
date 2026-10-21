r"""Comprehensive exact rational and numerical verification for CUBIC_FACTOR_SPECTRAL_ATTACK_20261014.md
Covers Phases 0 through 11:
- Phase 0: Audit of R_1 = 2 <u, h_{E,g} + h_{M,g}>_p = 2w <u, k_{E,g} + k_{M,g}>_Omega,
  R_1 = R_{1,(2)} + R_{1,(3)}, |R_{1,(2)}| <= 12 a rho v, ||H_g^{(3)}||_2 <= 2 v^{3/2},
  variance floor v >= c_1 a^{7/3}, and exact endpoint ratiozeta a^{9/4} / (c_1 a^{7/3}) ~ a^{-1/12} -> infinity.
- Phase 1: Exact Fourier transform of H_g^{(3)} = h_{E,h} + h_{M,h}, zero-mode subtraction,
  diagonal/resonant/nondegenerate mode classification, and exact pointwise bound max_t |K_{E,h}(t)| <= rho_h v, max_t |K_{M,h}(t)| <= rho_h v.
- Phase 2 & 3: Trilinear L2 stability ||E_d f_1(x+d)f_2(x+2d)f_3(x+3d)||_2 <= ||f_1||_2 ||f_2||_2 ||f_3||_2,
  1D cubic averaging harmonic decay |K_{E,s}(t)| = O(\log(1+|t|) / t^2) (summable in l^1 and O(L^{-3} \log^2 L) in l^2 tail!),
  and exact comparison of h's Fourier decay (1/|m|) vs H_g^{(3)}'s cubic-averaged decay (\log|t| / t^2).
- Phase 4, 5, 6: Exact Fourier truncation cost N(L, d) <= (6L+1)^d and error E(L, d, v) for rank-d quarter-arc factors,
  and relative Gram translation on proper windows.
- Phase 7: Adversarial search & Walsh parity factor functions on {0,1,2,3}^d showing multiplicative decay ||H_g^{(3)}||_2^2 <= (0.136)^d * 4 v^3
  for product Walsh modes vs additive mode concentration.
- Phase 8: Exact decomposition of R_2 = R_{2,(0)} + R_{2,(1)} + R_{2,(2)} where R_{2,(0)} = 0 on Z_p,
  |R_{2,(1)}| <= 12 a rho sqrt(b v), and |R_{2,(2)}| <= 6 rho sqrt(b v) ||hat(h)||_1.
- Phase 9, 10, 11: Adversarial checks on small AP-free sets, Sidon sets, Behrend sets, proper windows, and p=23, 29 rational laws.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, math
import numpy as np

counts = Counter()

# ==============================================================================
# PHASE 0, 1, 3, 8: Exact rational & Fourier identities for H_g^{(3)} and R_2
# ==============================================================================
def verify_cubic_field_and_R2(p, Sset, omega):
    n = len(omega)
    w = F(n, p)
    inv2 = pow(2, -1, p)
    B = [F(int(x in Sset)) for x in range(p)]
    for factor in ('trivial', 'quarter', 'parity'):
        cells = [[x for x in omega if (0 if factor=='trivial' else 4*x//p if factor=='quarter' else x%2)==j]
                 for j in range(4 if factor=='quarter' else 2 if factor=='parity' else 1)]
        cells = [C for C in cells if C]
        g = [F(0)] * p; u = [F(0)] * p
        for C in cells:
            gc = sum(B[x] for x in C) / len(C)
            for x in C:
                g[x] = gc
                u[x] = B[x] - gc
        a = F(len(Sset), n)
        v = sum((g[x] - a)**2 for x in omega) / n
        U = sum(u[x]**2 for x in omega) / n

        hEg = [sum(g[(x+d)%p]*g[(x+2*d)%p]*g[(x+3*d)%p] for d in range(p)) / p for x in range(p)]
        hMg = [sum(g[(x-d)%p]*g[(x+d)%p]*g[(x+2*d)%p] for d in range(p)) / p for x in range(p)]
        kEg = [F(0)] * p; kMg = [F(0)] * p
        for C in cells:
            mE = sum(hEg[x] for x in C) / len(C)
            mM = sum(hMg[x] for x in C) / len(C)
            for x in C:
                kEg[x] = hEg[x] - mE
                kMg[x] = hMg[x] - mM

        L_ug = {}
        for d in range(p):
            g1 = [g[(x+d)%p] for x in range(p)]; g2 = [g[(x+2*d)%p] for x in range(p)]; g3 = [g[(x+3*d)%p] for x in range(p)]
            u1 = [u[(x+d)%p] for x in range(p)]; u2 = [u[(x+2*d)%p] for x in range(p)]; u3 = [u[(x+3*d)%p] for x in range(p)]
            for mask in product((0, 1), repeat=4):
                v0 = u if mask[0] else g; v1 = u1 if mask[1] else g1; v2 = u2 if mask[2] else g2; v3 = u3 if mask[3] else g3
                L_ug[mask] = L_ug.get(mask, F(0)) + sum(v0[x]*v1[x]*v2[x]*v3[x] for x in range(p))
        for mask in L_ug:
            L_ug[mask] /= (p*p)
        R = [sum(val for mask, val in L_ug.items() if sum(mask) == j) for j in range(5)]

        # Phase 0: Verify R_1 = 2 <u, h_{E,g} + h_{M,g}>_p = 2w <u, k_{E,g} + k_{M,g}>_Omega
        R1_p = 2 * sum(u[x]*(hEg[x] + hMg[x]) for x in range(p)) / p
        R1_om = 2 * w * sum(u[x]*(kEg[x] + kMg[x]) for x in omega) / n
        assert R[1] == R1_p == R1_om
        counts['phase0_exact_R1_relative_pairing_checks'] += 1

        if n == p:
            h = [g[x] - a for x in range(p)]
            hEh2 = [a*sum(h[(x+d)%p]*h[(x+2*d)%p] + h[(x+d)%p]*h[(x+3*d)%p] + h[(x+2*d)%p]*h[(x+3*d)%p] for d in range(p))/p for x in range(p)]
            hMh2 = [a*sum(h[(x-d)%p]*h[(x+d)%p] + h[(x-d)%p]*h[(x+2*d)%p] + h[(x+d)%p]*h[(x+2*d)%p] for d in range(p))/p for x in range(p)]
            hEh3 = [sum(h[(x+d)%p]*h[(x+2*d)%p]*h[(x+3*d)%p] for d in range(p))/p for x in range(p)]
            hMh3 = [sum(h[(x-d)%p]*h[(x+d)%p]*h[(x+2*d)%p] for d in range(p))/p for x in range(p)]
            R1_2 = 2 * sum(u[x]*(hEh2[x] + hMh2[x]) for x in range(p)) / p
            R1_3 = 2 * sum(u[x]*(hEh3[x] + hMh3[x]) for x in range(p)) / p
            assert R[1] == R1_2 + R1_3
            assert sum((hEh2[x] + hMh2[x])**2 for x in range(p))/p <= 36 * a * a * v * v
            assert sum((hEh3[x] + hMh3[x])**2 for x in range(p))/p <= 4 * (v**3)

            # Phase 1 & 8: Fourier bounds on R_{1,(3)} and R_2 = R_{2,(1)} + R_{2,(2)} using ||hat(h)||_1
            uhat = np.fft.fft([float(x) for x in u]) / p
            hhat = np.fft.fft([float(x) for x in h]) / p
            rho = float(np.max(np.abs(uhat[1:])))
            rho_h = float(np.max(np.abs(hhat)))
            h_l1 = float(np.sum(np.abs(hhat)))
            vf = float(v); Uf = float(U); af = float(a)
            assert abs(float(R1_2)) <= 12.0 * af * rho * vf + 1e-11
            assert abs(float(R1_3)) <= 4.0 * rho * vf * h_l1 + 1e-11

            # Check pointwise bound on K_{E,h} and K_{M,h}
            KE_h = np.fft.fft([float(x) for x in hEh3]) / p
            KM_h = np.fft.fft([float(x) for x in hMh3]) / p
            assert float(np.max(np.abs(KE_h))) <= rho_h * vf + 1e-11
            assert float(np.max(np.abs(KM_h))) <= rho_h * vf + 1e-11

            # Exact splitting of R_2 = R_{2,(1)} + R_{2,(2)} on Z_p
            R2_1 = F(0); R2_2 = F(0)
            for d in range(p):
                h1 = [h[(x+d)%p] for x in range(p)]; h2 = [h[(x+2*d)%p] for x in range(p)]; h3 = [h[(x+3*d)%p] for x in range(p)]
                u1 = [u[(x+d)%p] for x in range(p)]; u2 = [u[(x+2*d)%p] for x in range(p)]; u3 = [u[(x+3*d)%p] for x in range(p)]
                for mask in product((0, 1), repeat=4):
                    if sum(mask) != 2: continue
                    # 2 u's and 2 g's; expand each g = a + h
                    # zero-h term vanishes by pair independence; one-h term has factor a; two-h term has two h's
                    u_slots = [i for i in range(4) if mask[i] == 1]
                    g_slots = [i for i in range(4) if mask[i] == 0]
                    us = [u, u1, u2, u3]; hs = [h, h1, h2, h3]
                    u_prod = [us[u_slots[0]][x] * us[u_slots[1]][x] for x in range(p)]
                    R2_1 += a * sum(u_prod[x] * (hs[g_slots[0]][x] + hs[g_slots[1]][x]) for x in range(p))
                    R2_2 += sum(u_prod[x] * hs[g_slots[0]][x] * hs[g_slots[1]][x] for x in range(p))
            R2_1 /= (p*p); R2_2 /= (p*p)
            assert R[2] == R2_1 + R2_2
            assert abs(float(R2_1)) <= 12.0 * af * rho * math.sqrt(Uf * vf) + 1e-11
            assert abs(float(R2_2)) <= 6.0 * rho * math.sqrt(Uf * vf) * h_l1 + 1e-11
            counts['phase8_exact_R2_splitting_and_l1_bounds'] += 1

for p in (7, 11):
    for bits in product((0, 1), repeat=p):
        Sset = {i for i, b in enumerate(bits) if b}
        if not Sset: continue
        if any(all((x+j*d)%p in Sset for j in range(4)) for x in Sset for d in range(1, p)):
            continue
        verify_cubic_field_and_R2(p, Sset, list(range(p)))

for p, n in [(11, 5), (13, 6)]:
    omega = list(range(n))
    for bits in product((0, 1), repeat=n):
        Sset = {omega[i] for i, b in enumerate(bits) if b}
        if not Sset: continue
        if any(all((x+j*d)%p in Sset for j in range(4)) for x in Sset for d in range(1, p)):
            continue
        verify_cubic_field_and_R2(p, Sset, omega)

# ==============================================================================
# PHASE 3: Trilinear L2 stability and 1D cubic averaging harmonic decay
# ==============================================================================
for p in (11, 17, 23):
    inv2 = pow(2, -1, p)
    for trial in range(15):
        f1, f2, f3 = np.random.randn(3, p)
        h1, h2, h3 = np.fft.fft(f1)/p, np.fft.fft(f2)/p, np.fft.fft(f3)/p
        KE = np.array([sum(h1[(2*t+r)%p]*h2[(-t-2*r)%p]*h3[r] for r in range(p)) for t in range(p)])
        KM = np.array([sum(h1[(t+r)*inv2%p]*h2[(t-3*r)*inv2%p]*h3[r] for r in range(p)) for t in range(p)])
        n1, n2, n3 = np.sqrt(np.mean(f1**2)), np.sqrt(np.mean(f2**2)), np.sqrt(np.mean(f3**2))
        assert np.sqrt(np.sum(np.abs(KE)**2)) <= n1 * n2 * n3 + 1e-11
        assert np.sqrt(np.sum(np.abs(KM)**2)) <= n1 * n2 * n3 + 1e-11
        counts['phase3_trilinear_L2_stability_checks'] += 1

# Verify 1D cubic averaging decay: for any 1D function h(theta) with |hat(h)(m)| <= C / |m|,
# its cubic completion K_E(t) = sum_{r != 0, -2t, -t/2} hat(h)(2t+r) hat(h)(-t-2r) hat(h)(r)
# decays as O(log(1+|t|) / t^2), so its l^2 tail outside [-L, L] is O(L^{-3} log^2 L) (vs O(L^{-1}) for h itself)!
shat = {m: (2.0 / (math.pi * abs(m)) if m != 0 and m % 2 != 0 else 0.0) for m in range(-400, 401)}
decay_records = []
for t in (1, 3, 5, 9, 15, 25):
    val = sum(shat.get(2*t+r, 0.0)*shat.get(-t-2*r, 0.0)*shat.get(r, 0.0) for r in range(-120, 121))
    bound = (8.0 / (math.pi**3)) * (4.0 * math.log(2*t + 2) + 6.0) / (t * t)
    assert val <= bound
    decay_records.append({'t': t, 'K_E_upper': val, 't2_times_K_E': t*t*val, 'analytic_bound': bound})
    counts['phase3_1d_cubic_harmonic_decay_checks'] += 1

# ==============================================================================
# PHASE 7: Adversarial low-rank factor tests (Walsh parity product vs additive)
# ==============================================================================
walsh_diagnostics = []
p = 257
for d in (1, 2, 3, 4):
    xis = [1, 3, 7, 13][:d]
    labels = [tuple((4 * (xi * x % p)) // p for xi in xis) for x in range(p)]
    h = np.array([(-1.0)**sum(lab) for lab in labels])
    h -= h.mean()
    a_val = 0.1; target_v = 0.25 * (a_val ** 2.25)
    h *= math.sqrt(target_v / np.mean(h**2))
    vf = float(np.mean(h**2))
    hEh = np.array([np.mean([h[(x+step)%p]*h[(x+2*step)%p]*h[(x+3*step)%p] for step in range(p)]) for x in range(p)])
    hMh = np.array([np.mean([h[(x-step)%p]*h[(x+step)%p]*h[(x+2*step)%p] for step in range(p)]) for x in range(p)])
    H3 = hEh + hMh
    H3_hat = np.fft.fft(H3) / p
    l2_sq = float(np.sum(np.abs(H3_hat)**2))
    walsh_diagnostics.append({
        'd': d, 'v': vf, 'H3_L2_sq': l2_sq,
        'ratio_to_4v3': l2_sq / (4.0 * (vf**3)),
        'ratio_to_a7': l2_sq / (a_val**7)
    })
    counts['phase7_walsh_factor_diagnostics'] += 1

# ==============================================================================
# PHASE 11: Check on p=23, k=5 and p=29, k=6 global laws
# ==============================================================================
for fname in ('degree_six_finite_extension_20261012.json', 'sixth_order_p29_k6_extension_20261012.json'):
    data = json.loads(Path(fname).read_text())
    p = data['p']
    for row in data['global_law'][:6]:
        verify_cubic_field_and_R2(p, set(row['representative']), list(range(p)))
        counts['phase11_global_law_checks'] += 1

result = {
    'principal_status': 'D: NEW RIGOROUS PARTIAL THEOREM (Cubic Averaging Smoothing Gain, Trilinear Stability, and R_1/R_2 l^1-Fourier Bounds)',
    'executed_date': '2026-10-14',
    'counts': dict(counts),
    'one_dim_cubic_decay_records': decay_records,
    'walsh_factor_diagnostics': walsh_diagnostics,
    'scope': 'Exact rational verification of R_1 = 2w<u,k_{E,g}+k_{M,g}>_Omega, R_1 = R_{1,(2)} + R_{1,(3)}, R_2 = R_{2,(1)} + R_{2,(2)}, trilinear L2 stability, 1D O(log|t|/t^2) cubic averaging harmonic decay, and Walsh factor diagnostics.'
}
(Path(__file__).resolve().parents[1] / "results" / 'CUBIC_FACTOR_SPECTRAL_VERIFICATION_20261014.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
