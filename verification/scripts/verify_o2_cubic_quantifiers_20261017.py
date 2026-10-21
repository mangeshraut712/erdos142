"""Finite identity checks only; no asymptotic selection certification."""
import itertools
import json
import math
import numpy as np

rng = np.random.default_rng(17012026)
checks = 0
max_error = 0.0

def check_close(left, right, tol=2e-10):
    global checks, max_error
    err = float(abs(left - right))
    max_error = max(max_error, err)
    assert err <= tol, (left, right, err)
    checks += 1

def check_leq(left, right, tol=2e-10):
    global checks
    assert left <= right + tol, (left, right)
    checks += 1

def solve_mod(mat, vec, p):
    a = [[int(v) % p for v in row] + [int(rhs) % p]
         for row, rhs in zip(mat, vec)]
    for col in range(len(a)):
        pivot = next(j for j in range(col, len(a)) if a[j][col])
        a[col], a[pivot] = a[pivot], a[col]
        scale = pow(a[col][col], -1, p)
        a[col] = [(v * scale) % p for v in a[col]]
        for row in range(len(a)):
            if row != col:
                scale = a[row][col]
                a[row] = [(v - scale * z) % p
                          for v, z in zip(a[row], a[col])]
    return [a[i][-1] for i in range(len(a))]

for p in [5, 7, 11, 17, 29, 43]:
    y = np.arange(p)
    x, h = np.meshgrid(y, y, indexing="ij")
    slots = [(x + j * h) % p for j in range(4)]
    chirps = np.exp(-2j * np.pi * (
        y[:, None, None] * y[None, None, :] ** 2
        + y[None, :, None] * y[None, None, :]) % (2j * np.pi)) if False else None
    # Form phases from reduced integer residues to avoid large angles.
    phase_indices = (y[:, None, None] * y[None, None, :] ** 2
                     + y[None, :, None] * y[None, None, :]) % p
    chirps = np.exp(-2j * np.pi * phase_indices / p)
    for trial in range(6):
        u = rng.uniform(-1, 1, p)
        if trial % 2 == 0:
            u -= np.mean(u)
        U = float(np.mean(u * u))
        Q = np.mean(chirps * u[None, None, :], axis=2)
        q = float(np.max(np.abs(Q)))
        lam4 = float(np.mean(np.prod(np.array([u[v] for v in slots]), axis=0)))
        energy = float(np.sum(abs(Q) ** 2 * abs(Q[(3*y) % p][:, (3*y) % p]) ** 2))
        check_close(lam4, energy - U*U + np.mean(u**4)/p)
        check_leq(energy, p*q*q*U)
        for occupied in itertools.combinations(range(4), 3):
            C, N, beta = [int(z) for z in rng.integers(0, p, 3)]
            coeffs = solve_mod([[1]*3, list(occupied), [j*j for j in occupied]],
                               [0, C, N], p)
            i, j, k = occupied
            theta = [(-beta*pow(j-i, -1, p)) % p,
                     (beta*pow(j-i, -1, p)) % p, 0]
            left = (2*C*x*h + N*h*h + beta*h) % p
            right = sum(c*slots[l]**2+t*slots[l]
                        for l,c,t in zip(occupied,coeffs,theta)) % p
            check_close(np.max(abs(left-right)), 0)
            phase = np.exp(2j*np.pi*left/p)
            value = np.mean(phase*np.prod(np.array([u[slots[l]] for l in occupied]), axis=0))
            check_leq(abs(value), q*U)

    # Original mixed-host geometry and the actual tent weight, rather than
    # a surrogate probability distribution over phases.
    for H in [1, max(1, p//5)]:
        centered = np.minimum(y, p-y)
        tent = np.maximum(0, (H+1-centered)/(H+1))
        F = tent[h] * tent[(2*x*h+h) % p] * tent[(h*h) % p]
        qpoly = (y*y+y) % p
        P = (y <= 3*p//4) & (qpoly <= 4*p//5)
        if not np.any(P):
            continue
        A = P & (rng.uniform(size=p) < .4)
        a = float(np.sum(A)/np.sum(P))
        u = A.astype(float) - a*P
        U = float(np.mean(u*u))
        Q = np.mean(chirps*u[None,None,:],axis=2)
        q = float(np.max(abs(Q)))
        Pminus = ((y >= 12*H) & (y <= 3*p//4-12*H)
                  & (qpoly >= 12*H) & (qpoly <= 4*p//5-12*H))
        b = float(np.mean(P)-np.mean(Pminus))
        fhat = np.fft.fft(tent)/p
        # d=s=1, xi=c=b=1. Persistent conditions force m=n=l=0.
        mu = float(fhat[0].real**3)
        beta_boundary = (mu+1/math.sqrt(p))*b+1/p
        R3 = 0.0
        for occupied in itertools.combinations(range(4),3):
            missing = next(j for j in range(4) if j not in occupied)
            prod = np.prod(np.array([u[slots[j]] for j in occupied]),axis=0)
            full = float(np.mean(F*prod))
            hosted = float(np.mean(F*prod*P[slots[missing]]))
            check_leq(abs(full),q*U)
            check_leq(abs(full-hosted),beta_boundary)
            R3 += a*hosted
        check_leq(abs(R3),4*a*q*U+4*a*beta_boundary)

print(json.dumps({"checks":checks,"maximum_identity_error":max_error,
                  "scope":"finite identities only; primes outside logarithmic target domain"},indent=2))
