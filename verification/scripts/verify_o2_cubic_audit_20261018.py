"""Proper-host audit with nonzero omitted-indicator corrections.

Finite identities only. These examples are outside the logarithmic target
domain and are not counterexamples to DIRECT-Q-GAIN.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np


def run():
    checks = 0
    max_error = 0.0
    cases = []

    def leq(lhs, rhs):
        nonlocal checks
        assert lhs <= rhs + 2e-12, (lhs, rhs)
        checks += 1

    def equal(lhs, rhs):
        nonlocal checks, max_error
        error = abs(float(lhs) - float(rhs))
        max_error = max(max_error, error)
        assert error < 2e-12, (lhs, rhs, error)
        checks += 1

    for p in (257, 521, 1031):
        y = np.arange(p)
        x, h = np.meshgrid(y, y, indexing="ij")
        slots = [(x + j*h) % p for j in range(4)]
        qpoly = (y*y + y) % p
        linear_lo, linear_hi = -30, 2
        quadratic_lo, quadratic_hi = -p//3, p//3

        def interval(z, lo, hi):
            return ((z-lo) % p) <= hi-lo

        P = interval(y, linear_lo, linear_hi) & interval(
            qpoly, quadratic_lo, quadratic_hi)
        # Exactly {0,1,2}, hence nonzero-difference cyclic 4-AP-free.
        B = (y <= 2)
        assert np.all(P[B])
        a = float(B.sum()/P.sum())
        u = B.astype(float) - a*P
        U = float(np.mean(u*u))
        chirp = np.exp(-2j*np.pi*((y[:, None]*y[None, :]**2) % p)/p)
        Q = np.fft.fft(chirp*u[None, :], axis=1)/p
        q = float(np.max(np.abs(Q)))
        equal(U, float(P.mean())*a*(1-a))
        equal(abs(Q[0, 0]), 0)
        quartic = np.mean(np.prod(np.array([u[v] for v in slots]), axis=0))
        energy = np.sum(abs(Q)**2*abs(Q[(3*y)%p][:, (3*y)%p])**2)
        equal(quartic, energy-U*U+np.mean(u**4)/p)

        H = 1
        tent = np.maximum(0, (H+1-np.minimum(y, p-y))/(H+1))
        F = tent[h]*tent[(2*x*h+h)%p]*tent[(h*h)%p]
        Pminus = interval(y, linear_lo+12*H, linear_hi-12*H) & interval(
            qpoly, quadratic_lo+12*H, quadratic_hi-12*H)
        assert np.any(Pminus), "Audit requires nonempty eroded host"
        assert np.all(P[Pminus])
        b = float(np.mean(P & ~Pminus))
        mu = ((H+1)/p)**3
        boundary = (mu+1/math.sqrt(p))*b+1/p
        corrections = []
        residual = 0.0
        for occupied in itertools.combinations(range(4), 3):
            missing = next(j for j in range(4) if j not in occupied)
            prod = np.prod(np.array([u[slots[j]] for j in occupied]), axis=0)
            full = float(np.mean(F*prod))
            hosted = float(np.mean(F*prod*P[slots[missing]]))
            leq(abs(full), q*U)
            leq(abs(full-hosted), boundary)
            corrections.append(abs(full-hosted))
            residual += a*hosted
        leq(abs(residual), 4*a*q*U+4*a*boundary)
        assert max(corrections) > 1e-12, "Correction must be nonzero"
        checks += 4  # Support, nonempty erosion, erosion subset, nonzero correction.
        cases.append({"p":p, "host_size":int(P.sum()),
                      "eroded_host_size":int(Pminus.sum()),
                      "set_size":int(B.sum()), "a":a,
                      "max_host_correction":max(corrections),
                      "boundary_bound":boundary,
                      "abs_R3":abs(residual),
                      "cubic_bound":4*a*q*U+4*a*boundary})
    return {"checks":checks, "maximum_identity_error":max_error,
            "scope":"finite identities; target domain not asserted",
            "cases":cases}


if __name__ == "__main__":
    result = run()
    rendered = json.dumps(result, indent=2)+"\n"
    (Path(__file__).resolve().parents[1] / "results" / "O2_CUBIC_AUDIT_20261018.json").write_text(rendered)
    print(rendered, end="")
