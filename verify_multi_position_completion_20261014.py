"""Exact verification for multi-position (endpoint + interior) completion algebra,
2x2 cell projection, cross-overlap geometry, and degree-six matrix SOS."""
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import itertools, json, math
import numpy as np

counts = Counter()
strict_improvements = []
window_rescues = []

def check_case(p, S, omega):
    B = np.array([int(x in S) for x in range(p)])
    HE = np.array([sum(int(B[(x+d)%p]*B[(x+2*d)%p]*B[(x+3*d)%p]) for d in range(1,p)) for x in range(p)])
    HM = np.array([sum(int(B[(x-d)%p]*B[(x+d)%p]*B[(x+2*d)%p]) for d in range(1,p)) for x in range(p)])
    assert not np.any(B * HE) and not np.any(B * HM)
    qE = [F(int(x), p) for x in HE]
    qM = [F(int(x), p) for x in HM]
    hE = [qE[x] + F(int(B[x]), p) for x in range(p)]
    hM = [qM[x] + F(int(B[x]), p) for x in range(p)]
    assert all(B[x]*hE[x] == F(int(B[x]), p) and B[x]*hM[x] == F(int(B[x]), p) for x in range(p))

    # Full-group Fourier identities and exact duality with T and S in Lambda_4(B)
    b = np.fft.fft(B) / p
    inv2 = pow(2, -1, p)
    KE = np.array([sum(b[(2*t+r)%p]*b[(-t-2*r)%p]*b[r] for r in range(p)) for t in range(p)])
    KM = np.array([sum(b[(t+r)*inv2%p]*b[(t-3*r)*inv2%p]*b[r] for r in range(p)) for t in range(p)])
    assert np.max(np.abs(np.fft.fft([float(x) for x in hE])/p - KE)) < 1e-11
    assert np.max(np.abs(np.fft.fft([float(x) for x in hM])/p - KM)) < 1e-11
    a_full = F(int(B.sum()), p)
    T_fourier = sum(b[r]*b[r]*b[(-2*r)%p] for r in range(1, p)).real
    S_fourier = sum(b[r]*b[(2*r)%p]*b[(-3*r)%p] for r in range(1, p)).real
    assert abs(float(sum(qE)/p) - (float(a_full**3 - a_full/p) + T_fourier)) < 1e-11
    assert abs(float(sum(qM)/p) - (float(a_full**3 - a_full/p) + S_fourier)) < 1e-11
    if S and (not np.any(HE) or not np.any(HM)):
        bound = max(F(0), (a_full*a_full - F(1, p))/(1 - a_full))
        assert max(abs(b[1:])) + 1e-11 >= float(bound)
        counts['qE_or_qM_zero_Fourier_branch'] += 1
    counts['exact_fourier_dual_channel_checks'] += 1

    n = len(omega)
    for factor in ('trivial', 'quarter', 'parity'):
        cells = [[x for x in omega if (0 if factor=='trivial' else 4*x//p if factor=='quarter' else x%2)==j]
                 for j in range(4 if factor=='quarter' else 2 if factor=='parity' else 1)]
        cells = [C for C in cells if C]
        u = {}; kE = {}; kM = {}; zE = {}; zM = {}
        SE = F(0); SM = F(0); JE = F(0); JM = F(0); JEM = F(0)
        for C in cells:
            g = F(sum(int(B[x]) for x in C), len(C))
            TE = sum(qE[x] for x in C) / len(C)
            TM = sum(qM[x] for x in C) / len(C)
            aE = TE / (1 - g) if g != 1 else F(0)
            aM = TM / (1 - g) if g != 1 else F(0)
            for x in C:
                u[x] = F(int(B[x])) - g
                kE[x] = qE[x] - TE
                kM[x] = qM[x] - TM
                zE[x] = kE[x] + aE * u[x]
                zM[x] = kM[x] + aM * u[x]
            assert sum(zE[x] for x in C) == 0 and sum(zM[x] for x in C) == 0
            assert all(B[x]*zE[x] == 0 and B[x]*zM[x] == 0 for x in C)
            assert sum(u[x]*zE[x] for x in C) == 0 and sum(u[x]*zM[x] for x in C) == 0
            SE += len(C) * g * TE
            SM += len(C) * g * TM
            JE += len(C) * g * TE * aE
            JM += len(C) * g * TM * aM
            JEM += len(C) * g * TE * aM
            counts['exact_joint_cell_identities'] += 1

        SE /= n; SM /= n; JE /= n; JM /= n; JEM /= n
        U = sum(u[x]**2 for x in omega) / n
        WE = sum(kE[x]**2 for x in omega) / n
        WM = sum(kM[x]**2 for x in omega) / n
        WEM = sum(kE[x]*kM[x] for x in omega) / n
        ZE = sum(zE[x]**2 for x in omega) / n
        ZM = sum(zM[x]**2 for x in omega) / n
        ZEM = sum(zE[x]*zM[x] for x in omega) / n

        assert sum(u[x]*kE[x] for x in omega)/n == -SE
        assert sum(u[x]*kM[x] for x in omega)/n == -SM
        assert WE == JE + ZE and WM == JM + ZM and WEM == JEM + ZEM
        assert ZE >= 0 and ZM >= 0 and ZE * ZM >= ZEM * ZEM
        assert (U*JE - SE*SE) >= 0 and (U*JM - SM*SM) >= 0
        assert (U*JE - SE*SE)*(U*JM - SM*SM) >= (U*JEM - SE*SM)**2
        assert (U*WE - SE*SE)*(U*WM - SM*SM) >= (U*WEM - SE*SM)**2

        if U > 0:
            ovE = (SE*SE)/(U*WE) if WE > 0 else F(0)
            ovM = (SM*SM)/(U*WM) if WM > 0 else F(0)
            det = WE*WM - WEM*WEM
            if det > 0:
                ov2 = (SE*SE*WM - 2*SE*SM*WEM + SM*SM*WE) / (U * det)
            else:
                ov2 = max(ovE, ovM)
            assert ov2 >= max(ovE, ovM)
            if ov2 > ovE:
                counts['strict_two_channel_overlap_improvements'] += 1
                if len(strict_improvements) < 5:
                    strict_improvements.append({
                        'p': p, 'window_size': n, 'factor': factor, 'set': sorted(S),
                        'endpoint_overlap_sq': float(ovE), 'interior_overlap_sq': float(ovM),
                        'joint_overlap_sq': float(ov2)
                    })
        counts['exact_2x2_loewner_checks'] += 1

        # Relative Gram spectral projection check for linear combinations
        uv = np.array([float(u[x]) for x in omega])
        kEv = np.array([float(kE[x]) for x in omega])
        kMv = np.array([float(kM[x]) for x in omega])
        for freqs in ((1,), (1, 2, 3)):
            M = np.exp(2j * np.pi * np.outer(omega, freqs) / p)
            for C in cells:
                ids = [omega.index(x) for x in C]
                M[ids] -= M[ids].mean(axis=0)
            P = M @ np.linalg.pinv(M, rcond=1e-12)
            pu = P @ uv
            gain = float(np.vdot(pu, pu).real / n)
            for lamE, lamM in ((1.0, 0.0), (0.0, 1.0), (0.5, 0.5), (1.0, -0.5)):
                kv = lamE * kEv + lamM * kMv
                pk = P @ kv
                tail = np.linalg.norm(kv - pk) / math.sqrt(n)
                energy = float(np.vdot(pk, pk).real / n)
                S_lam = lamE * float(SE) + lamM * float(SM)
                if energy > 1e-20:
                    lower = max(0.0, abs(S_lam) - math.sqrt(float(U)) * tail)**2 / energy
                    assert gain + 1e-10 >= lower
                counts['relative_gram_joint_projection_checks'] += 1
    counts['set_window_cases_checked'] += 1

for p in (7, 11):
    for bits in itertools.product((0, 1), repeat=p):
        S = {i for i, b in enumerate(bits) if b}
        if any(all((x+j*d)%p in S for j in range(4)) for x in S for d in range(1, p)):
            continue
        check_case(p, S, list(range(p)))

# Also check p=13 trivial factor overlap improvements
p = 13
for bits in itertools.product((0, 1), repeat=p):
    S = {i for i, b in enumerate(bits) if b}
    if not S or len(S) == p: continue
    if any(all((x+j*d)%p in S for j in range(4)) for x in S for d in range(1, p)):
        continue
    B = [int(x in S) for x in range(p)]
    qE = [F(sum(B[(x+d)%p]*B[(x+2*d)%p]*B[(x+3*d)%p] for d in range(1,p)), p) for x in range(p)]
    qM = [F(sum(B[(x-d)%p]*B[(x+d)%p]*B[(x+2*d)%p] for d in range(1,p)), p) for x in range(p)]
    a = F(len(S), p); U = a*(1-a)
    TE = sum(qE)/p; TM = sum(qM)/p
    SE = a*TE; SM = a*TM
    WE = sum((qE[x]-TE)**2 for x in range(p))/p
    WM = sum((qM[x]-TM)**2 for x in range(p))/p
    WEM = sum((qE[x]-TE)*(qM[x]-TM) for x in range(p))/p
    ovE = (SE*SE)/(U*WE) if WE > 0 else F(0)
    ovM = (SM*SM)/(U*WM) if WM > 0 else F(0)
    det = WE*WM - WEM*WEM
    ov2 = (SE*SE*WM - 2*SE*SM*WEM + SM*SM*WE)/(U*det) if det > 0 else max(ovE, ovM)
    assert ov2 >= max(ovE, ovM)
    if ov2 > ovE:
        counts['p13_trivial_factor_strict_improvements'] += 1

# Proper-window diagnostics and rescues
cube = {sum(b[j]*3**j for j in range(3)) for b in itertools.product((0, 1), repeat=3)}
prodset = {x + 16*y for x in (0, 1, 4) for y in (0, 1, 4)}
for name, p, n, S in [
    ('three_point', 101, 25, {0, 1, 3}),
    ('ternary_cube', 59, 14, cube),
    ('digit_product', 277, 69, prodset),
    ('z11_3', 11, 3, {0, 1, 2}),
]:
    omega = list(range(n))
    check_case(p, S, omega)
    B = [int(x in S) for x in range(p)]
    sum_HE = sum(sum(B[(x+d)%p]*B[(x+2*d)%p]*B[(x+3*d)%p] for d in range(1,p)) for x in omega)
    sum_HM = sum(sum(B[(x-d)%p]*B[(x+d)%p]*B[(x+2*d)%p] for d in range(1,p)) for x in omega)
    window_rescues.append({
        'name': name, 'p': p, 'window_size': n,
        'endpoint_completions_in_window': sum_HE,
        'interior_completions_in_window': sum_HM,
        'rescued_by_interior_channel': (sum_HE == 0 and sum_HM > 0)
    })

# Verify interior and cross-overlap geometry and AP-forced zeros for p > 7
for p in (11, 13, 17, 23, 29, 41):
    RM = {i * pow(j, -1, p) % p for i in (-1, 1, 2) for j in (-1, 1, 2)}
    REM = {i * pow(j, -1, p) % p for i in (1, 2, 3) for j in (-1, 1, 2)}
    assert len(RM) == 6 and len(REM) == 8
    for d in range(1, p):
        Ed = {d % p, (2*d) % p, (3*d) % p}
        Md = {(-d) % p, d % p, (2*d) % p}
        for e in range(1, p):
            Me = {(-e) % p, e % p, (2*e) % p}
            r = e * pow(d, -1, p) % p
            assert len(Md & Me) == (3 if r == 1 else 2 if r == (-1)%p else 1 if r in RM else 0)
            assert len(Ed & Me) == (2 if r == 1 else 1 if r in REM else 0)
            if r == 2:
                U = Ed | Me
                assert len(U) == 5
                assert all((j*d) % p in U for j in (1, 2, 3, 4))
            counts['exact_overlap_pair_classifications'] += 1

# Verify degree-six joint completion SOS polynomial identity on all AP-free sets of Z_7, Z_11
for p in (7, 11):
    for bits in itertools.product((0, 1), repeat=p):
        S = {i for i, b in enumerate(bits) if b}
        if any(all((x+j*d)%p in S for j in range(4)) for x in S for d in range(1, p)):
            continue
        B = [int(x in S) for x in range(p)]
        HE = [sum(B[(v+d)%p]*B[(v+2*d)%p]*B[(v+3*d)%p] for d in range(1,p)) for v in range(p)]
        HM = [sum(B[(v-d)%p]*B[(v+d)%p]*B[(v+2*d)%p] for d in range(1,p)) for v in range(p)]
        for v in range(p):
            for alpha, beta, s in ((F(1), F(1), F(1,2)), (F(2), F(-1), F(3,4))):
                Hcomb = alpha * HE[v] + beta * HM[v]
                lhs = Hcomb**2 - 2*s*Hcomb + s*s*(1 - B[v])
                rhs = (Hcomb - s*(1 - B[v]))**2 - 2*s*B[v]*Hcomb
                assert lhs == rhs and lhs >= 0
                counts['exact_joint_degree_six_sos_checks'] += 1

result = {
    'status': 'passed; exact two-channel completion theorem verified; SELECT and target unresolved',
    'executed_date': '2026-10-14',
    'counts': dict(counts),
    'window_rescues': window_rescues,
    'sample_strict_improvements': strict_improvements,
    'scope': 'Exact integer/Fraction verification for 2x2 cell covariance, Loewner order, overlap geometry, and degree-six SOS; 1e-10 tolerance for Fourier and Moore-Penrose Gram projections.'
}
Path('MULTI_POSITION_COMPLETION_VERIFICATION_20261014.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
