"""Bounded offline Boolean diagnostics; no claim of an asymptotic counterexample.

Exact rational residuals and Boolean witnesses are separate from floating phase
correlations and finite ledger estimates. Historical outputs are never changed.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
import math
import random

import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "BOOLEAN_O2_DIAGNOSTICS_20261017.json"
COUNTS = Counter()
RNG = random.Random(14220261017)


def tent_num(t, p, H):
    t %= p
    return max(0, H + 1 - min(t, p - t))


def ap_edges(p):
    return sorted({tuple(sorted((x + i * h) % p for i in range(4)))
                   for x in range(p) for h in range(1, p)})


def ap_free(A, edges):
    return all(not all(v in A for v in e) for e in edges)


def greedy(host, edges):
    at = {v: [] for v in host}
    for edge in edges:
        if all(v in at for v in edge):
            for v in edge:
                at[v].append(edge)
    order = list(host)
    RNG.shuffle(order)
    A = set()
    for v in order:
        A.add(v)
        if any(all(y in A for y in e) for e in at[v]):
            A.remove(v)
    return A


def geometry(p, N, H, quadratic=False):
    # Full group or initial interval. An optional x^2 quarter interval only
    # establishes the window's shape, not a certified iterative history.
    host = {v for v in range(N)
            if not quadratic or (v*v) % p < (p + 3)//4}
    lin = [(1, 0, N)]
    quad = [(1, 0, 0, 0, (p + 3)//4)] if quadratic else []
    k = 1 + 2 * int(quadratic)
    den = (H + 1)**k
    edges = []
    for x in range(p):
        for h in range(p):
            vertices = tuple((x + i*h) % p for i in range(4))
            if not all(v in host for v in vertices):
                continue
            z = tent_num(h, p, H)
            if quadratic:
                z *= tent_num(2*x*h, p, H)*tent_num(h*h, p, H)
            if z:
                edges.append((h, vertices, z))
    interior = {v for v in host if 12*H <= v < N-12*H
                and (not quadratic or 12*H <= (v*v)%p < (p+3)//4-12*H)}
    # Exact M4: the x^2 derivative variables have invertible coefficients.
    mu = Q(H + 1, p)**k
    return dict(p=p, N=N, H=H, host=host, edges=edges, den=den,
                mu=mu, r=1+int(quadratic), s=int(quadratic), k=k,
                interior=interior, linear=lin, quadratic=quad)


def residuals(g, A):
    p, n, m = g['p'], len(g['host']), len(A)
    raw = [0]*5
    diag = [0]*5
    occupancy = [0]*5
    for h, vertices, z in g['edges']:
        k = sum(v in A for v in vertices)
        occupancy[k] += z
        u = [n*int(v in A)-m for v in vertices]
        poly = [1]
        for v in u:
            poly = [poly[0]*m] + [poly[j]*m+poly[j-1]*v
                                      for j in range(1, len(poly))] + [poly[-1]*v]
        for j, v in enumerate(poly):
            raw[j] += z*v
            if h == 0:
                diag[j] += z*v
    den = p*p*g['den']*n**4
    vals = [Q(z, den) for z in raw]
    diagonal = [Q(z, den) for z in diag]
    a, w = Q(m, n), Q(n, p)
    assert sum(vals) == a*w/p
    assert sum(diagonal) == a*w/p
    assert vals[0] == a**4*Q(sum(occupancy), p*p*g['den'])
    assert diagonal[2] == 6*a*a*w*a*(1-a)/p
    assert diagonal[3] == 4*a*w*a*(1-a)*(1-2*a)/p
    assert diagonal[4] == w*a*(1-a)*(1-3*a+3*a*a)/p
    assert occupancy[4] == m*g['den']
    # Independent occupancy formula, including the all-occupied diagonal.
    qoccupancy = sum(z*(int(k == 4)-3*a**4+2*a**3*k-a*a*Q(k*(k-1),2))
                     for k,z in enumerate(occupancy))/(p*p*g['den'])
    assert vals[3]+vals[4] == qoccupancy
    COUNTS['exact_residual_expansion_diagonals_occupancy'] += 1
    return vals, diagonal, occupancy


def phases(g, A):
    p, n, m = g['p'], len(g['host']), len(A)
    xx = np.arange(p)
    u = np.array([int(v in A)-m/n*int(v in g['host']) for v in range(p)])
    cc = np.arange(p)[:,None]
    chirps = np.exp(-2j*np.pi*((cc*xx[None,:]**2) % p)/p)
    ft = np.fft.fft(chirps*u[None,:], axis=1)/n
    assert abs(ft[0,0]) < 1e-13
    ft[0,0] = 0
    c,t = np.unravel_index(np.argmax(abs(ft)), ft.shape)
    delta = float(abs(ft[c,t]))
    # Fixed-c Parseval: relative support gives sum_t |Q|^2=U/w^2.
    expected = p*(m/n)*(1-m/n)/n
    assert np.max(abs(np.sum(abs(ft)**2, axis=1)-expected)) < 1e-12
    COUNTS['floating_all_quadratic_phase_sweep_and_Parseval'] += 1
    return delta, [int(c),int(t)]


def record(g, A, vals, diag, occ):
    p,n,m = g['p'],len(g['host']),len(A)
    a,w = Q(m,n),Q(n,p)
    delta, maximizing = phases(g,A)
    F = math.log(math.log(math.e**2/float(a)))
    ratio = delta/(float(a)**1.5*F)
    bdry = Q(n-len(g['interior']),p)
    epsp = p**-.5
    U = w*a*(1-a)
    beta = (float(g['mu'])+epsp)*float(bdry)+1/p
    # Uniform conservative P2 bound uses 6-sum nu <=6.
    E2 = 6*float(a*a)*(beta+float(U)*epsp)
    E1 = 4*float(a**3)*(float(g['mu']*bdry)+epsp*float(w+bdry)+2/p)
    main = a**4*w*g['mu']
    budget = g['r']*(math.log(1/float(w))+math.log(48*g['r'])+math.log(math.log(p)))
    prescribed_H = math.floor(float(a*a*w)*p/(48*g['r']*math.log(p)))
    return dict(p=p,N=g['N'],H=g['H'],linear=g['linear'],quadratic=g['quadratic'],
                host=sorted(g['host']),A=sorted(A),a=str(a),w=str(w),mu=str(g['mu']),
                R=list(map(str,vals)),diagonal=list(map(str,diag)),
                off_diagonal=list(map(str,[v-d for v,d in zip(vals,diag)])),
                occupancy_weight_numerators=occ,weight_denominator=g['den'],
                Q=str(vals[3]+vals[4]),main=str(main),
                Q_over_main=float((vals[3]+vals[4])/main),
                R3_over_main=float(vals[3]/main),R4_over_main=float(vals[4]/main),
                phase_delta=delta,maximizing_phase=maximizing,
                concrete_threshold_critical_constant=ratio,
                phase_failure_only_if_c_strictly_above=ratio,
                product_budget_lhs=budget,product_budget_rhs=math.log(p)/100,
                product_budget_passes=budget<=math.log(p)/100,
                prescribed_H=prescribed_H,prescribed_H_valid=prescribed_H>=1,
                boundary=str(bdry),diagonal_over_main=float((a*w/p)/main),
                E1_over_main=E1/float(main),E2_conservative_over_main=E2/float(main),
                epsilon_density_upper_limit=2*float(a)*math.log(n) if n>1 else 0,
                relative_density_at_most_four_fifths=a<=Q(4,5),
                initial_interval_shape=(not g['quadratic'] and 3*g['N']<p<6*g['N']),
                certified_reachable_history=False,
                genuine_P12_counterexample=False)


records = []
best = {}
for p in [7,11,19,29,53,101]:
    global_edges = ap_edges(p)
    for N,quad in [(p,False),((p-1)//4,False),((p-1)//4,True)]:
        if N < 2:
            continue
        for H in sorted({1,max(1,p//8),(p-1)//2}):
            g = geometry(p,N,H,quad)
            if len(g['host']) < 2:
                continue
            host = sorted(g['host'])
            if p <= 11 and not quad:
                candidates = ({host[i] for i in range(len(host)) if mask >> i & 1}
                              for mask in range(1, 2**len(host)-1))
            else:
                candidates = [greedy(host,global_edges) for _ in range(100)]
            seen = set()
            selected = {}
            for A in candidates:
                key = tuple(sorted(A))
                if key in seen or not A or len(A)==len(host) or not ap_free(A,global_edges):
                    continue
                seen.add(key)
                vals,diag,occ = residuals(g,A)
                for field,value in [('R3',vals[3]),('R4',vals[4]),
                                    ('Q',vals[3]+vals[4]),
                                    ('R3_offdiag',vals[3]-diag[3]),
                                    ('R4_offdiag',vals[4]-diag[4])]:
                    if field not in selected or value < selected[field][0]:
                        selected[field] = (value,set(A),vals,diag,occ)
            selected_keys = set()
            for field,(value,A,vals,diag,occ) in selected.items():
                key = tuple(sorted(A))
                if key in selected_keys:
                    continue
                selected_keys.add(key)
                rec = record(g,A,vals,diag,occ)
                rec['selected_for'] = [f for f,z in selected.items() if z[1]==A]
                records.append(rec)

# Direct independent recount of every retained witness, using products instead
# of the coefficient recursion or occupancy identities.
for rec in records:
    p,H,N = rec['p'],rec['H'],rec['N']
    g = geometry(p,N,H,bool(rec['quadratic']))
    A,host = set(rec['A']),set(rec['host'])
    n,m = len(host),len(A)
    den = p*p*g['den']*n**4
    raw = [0]*5
    for h,vs,z in g['edges']:
        un = [n*int(v in A)-m for v in vs]
        for j in range(5):
            raw[j] += z*m**(4-j)*sum(math.prod(un[i] for i in slots)
                                     for slots in combinations(range(4),j))
    assert list(map(str,[Q(v,den) for v in raw])) == rec['R']
    assert ap_free(A,ap_edges(p))
    assert not rec['product_budget_passes']
    assert not rec['prescribed_H_valid']
    COUNTS['independent_exact_saved_witness_recount'] += 1

payload = dict(status="FINITE BOOLEAN OBSTRUCTIONS ONLY; P12 REMAINS OPEN",
               counts=dict(COUNTS),total_checks=sum(COUNTS.values()),
               exact_vs_floating="Residuals, diagonals, occupancy and AP exclusion exact; phase correlations and ledger diagnostics floating.",
               normalization="E_(x,h) is 1/p^2; u=B-aP; all h included; Lambda_F(B)=aw/p.",
               restrictions="Every saved finite host violates T5 and has prescribed H=0. No constant c_epsilon or asymptotic threshold is inferred.",
               records=records)
OUT.write_text(json.dumps(payload,indent=2)+"\n")
print(json.dumps(dict(output=str(OUT),counts=dict(COUNTS),records=len(records)),indent=2))

