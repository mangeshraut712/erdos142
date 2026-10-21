"""Finite arithmetic checks for the elementary polynomial-density construction.

AP enumeration/deletion uses exact modular integers. All p^2 chirp
coefficients are evaluated numerically, with direct-sum cross-checks.
No finite example is asserted to belong to the logarithmic target domain.
"""
import json
import math
from pathlib import Path

import numpy as np


def progressions(B):
    p = len(B)
    x = np.arange(p)
    found = []
    for h in range(1, p):
        mask = B & B[(x+h)%p] & B[(x+2*h)%p] & B[(x+3*h)%p]
        found.extend((int(v), h) for v in x[mask])
    return found


def run():
    checks = 0
    max_direct_error = 0.0
    coefficient_count = 0
    cases = []
    theta = 9/20
    rng = np.random.default_rng(18102026)

    def require(condition, message):
        nonlocal checks
        assert condition, message
        checks += 1

    for p in (127, 257, 521, 1031, 2053):
        t = p**(-theta)
        B = rng.random(p) < t
        initial_aps = progressions(B)
        A = B.copy()
        for v, h in initial_aps:
            vertices = (v+np.arange(4)*h) % p
            if np.all(A[vertices]):
                A[v] = False
        final_aps = progressions(A)
        d = int(B.sum()-A.sum())
        a0, a = float(B.mean()), float(A.mean())
        require(not final_aps, "Final set contains a nonzero cyclic 4-AP")
        require(np.all(~A | B), "Deletion added an element")
        require(d <= len(initial_aps), "Deletion count exceeds initial AP count")
        require(a > 0, "Finite sample became empty")
        y = np.arange(p)
        u0, u = B.astype(float)-a0, A.astype(float)-a
        noise = B.astype(float)-t
        max_initial = max_final = max_noise = max_change = 0.0
        witness = None
        for start in range(0, p, 32):
            c = np.arange(start, min(start+32, p))
            phases = np.exp(-2j*np.pi*((c[:, None]*y[None, :]**2)%p)/p)
            Q0 = np.fft.fft(phases*u0[None, :], axis=1)/p
            Q = np.fft.fft(phases*u[None, :], axis=1)/p
            Qn = np.fft.fft(phases*noise[None, :], axis=1)/p
            coefficient_count += 3*len(c)*p
            max_initial = max(max_initial, float(np.max(abs(Q0))))
            max_noise = max(max_noise, float(np.max(abs(Qn))))
            max_change = max(max_change, float(np.max(abs(Q-Q0))))
            row, col = np.unravel_index(np.argmax(abs(Q)), Q.shape)
            if abs(Q[row, col]) > max_final:
                max_final = float(abs(Q[row, col]))
                witness = (int(c[row]), int(col))
            require(float(np.max(abs(Q-Q0))) <= 2*d/p+2e-12,
                    "Per-coefficient deletion stability failed")
            # Two direct-sum checks per chunk, independent of the FFT.
            for row, col in ((0, 0), (len(c)-1, (start+17)%p)):
                direct_phase = np.exp(-2j*np.pi*((c[row]*y*y+col*y)%p)/p)
                direct = np.mean(u*direct_phase)
                error = float(abs(direct-Q[row, col]))
                max_direct_error = max(max_direct_error, error)
                require(error < 2e-12, "FFT/direct chirp mismatch")

        xp = 5*math.log(p)
        Lp = 2*math.sqrt(p*t*xp)+xp
        Zlimit = p*p*t**4*math.log(p)
        require(max_initial <= 2*max_noise+2e-12, "Actual-mean centering bound")
        require(max_final <= max_initial+2*d/p+2e-12, "Final stability bound")
        require(abs(a-t) <= Lp/p+p*t**4*math.log(p)+2e-12,
                "Displayed density error bound")
        concentration_event = max_noise <= Lp/p+2e-12
        ap_count_event = len(initial_aps) <= Zlimit
        require(concentration_event, "Chosen finite sample failed concentration event")
        require(ap_count_event, "Chosen finite sample failed AP-count event")
        require(max_final <= 2*Lp/p+2*p*t**4*math.log(p)+2e-12,
                "Displayed final correlation bound")
        linear_parseval_lower = math.sqrt(a*(1-a)/(p-1))
        require(max_final+2e-12 >= linear_parseval_lower, "Linear Parseval lower bound")
        cases.append({
            "p":p, "theta":theta, "sampling_density":t,
            "initial_size":int(B.sum()), "final_size":int(A.sum()),
            "ordered_nonzero_APs_initial":len(initial_aps),
            "ordered_nonzero_APs_final":len(final_aps), "deleted_vertices":d,
            "a":a, "delta":max_final, "delta_over_a_three_halves":max_final/a**1.5,
            "maximizing_quadratic_linear_coefficients":list(witness),
            "max_centered_coefficient_change":max_change,
            "deterministic_deletion_change_bound":2*d/p,
            "concentration_event_holds":bool(concentration_event),
            "AP_count_event_holds":bool(ap_count_event),
            "original_weight_H":math.floor(p*a*a/(48*math.log(p))),
            "scope":"finite diagnostic; no asymptotic or target-domain certification",
        })
    require(any(c["deleted_vertices"] > 0 for c in cases),
            "At least one case must exercise actual deletion")
    return {"checks":checks, "chirp_coefficients_evaluated":coefficient_count,
            "maximum_FFT_direct_error":max_direct_error, "seed":18102026,
            "scope":"exact modular AP checks; floating all-chirp checks; no asymptotic inference",
            "cases":cases}


if __name__ == "__main__":
    output = json.dumps(run(), indent=2)+"\n"
    Path(__file__).with_name("BOOLEAN_ALTERATION_CHIRP_VERIFICATION_20261018.json").write_text(output)
    print(output, end="")
