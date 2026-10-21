"""Exact finite checks for a 12-slot / 7/11 terminal refinement.

The mathematical proof is supplied separately. This checks its identities,
the finite R_4(12)=8 certificate, and actual AP-free sets in mixed windows
with nonempty eroded interiors. Square-root envelopes alone use floats.
It does not prove phase selection or the logarithmic-density target.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parent
counts = Counter()


def check(label, condition):
    assert condition, label
    counts[label] += 1


def fi(t, p, H):
    return max(0, H + 1 - min(t % p, (-t) % p))


# Exhaustive corroboration of the elementary twelve-slot hole proof.
edges12 = [sum(1 << (x+j*d) for j in range(4))
           for d in range(1, 4) for x in range(12-3*d)]
extremizers = []
for mask in range(1 << 12):
    if any(mask & e == e for e in edges12):
        continue
    check('exact_twelve_slot_cap', mask.bit_count() <= 8)
    if mask.bit_count() == 8:
        extremizers.append([i for i in range(12) if mask >> i & 1])
check('exact_twelve_slot_cap_attained', bool(extremizers))

# Check the three-hole proof's intermediate necessary conditions directly.
for holes in product(range(4), range(4, 8), range(8, 12)):
    a, b, c = holes
    hit_all = all(any((e >> z) & 1 for z in holes) for e in edges12)
    check('exact_three_holes_cannot_hit', not hit_all)
    if b-a <= 4 and c-b <= 4:
        parity_edges = [e for e in edges12
                        if all(((i-next(j for j in range(12) if e >> j & 1)) % 2 == 0)
                               for i in range(12) if e >> i & 1)]
        if all(any((e >> z) & 1 for z in holes) for e in parity_edges):
            check('exact_three_hole_parity_reduction', holes in [(2, 5, 8), (3, 6, 9)])

records = []
configs = [
    (257, 1, 4, 3, [(1, 0, 257)], []),
    (1009, 1, 12, 8, [(1, 0, 1009)], []),
    (1009, 1, 12, 8, [(1, 0, 900)], [(1, 1, 0, 0, 1009)]),
]
for p, H, slots, cap, linear, quadratic in configs:
    d, s = len(linear), len(quadratic)
    den = (H+1)**(d+2*s)
    erosion = slots*(slots-1)*H

    def inside(v, shrink=0):
        return all(shrink <= (xi*v-start) % p < length-shrink
                   for xi, start, length in linear) and all(
                       shrink <= (c*v*v+b*v+e-start) % p < length-shrink
                       for c, b, e, start, length in quadratic)

    Om = {v for v in range(p) if inside(v)}
    interior = {v for v in Om if inside(v, erosion)}
    n, w = len(Om), Q(len(Om), p)
    boundary = Q(n-len(interior), p)
    check('nonempty_eroded_interior', len(interior) > 0)
    first = 0
    for t in range(p):
        lin = math.prod(fi(xi*t, p, H) for xi, _, _ in linear)
        if lin:
            first += lin*sum(math.prod(fi(b*t+c*z, p, H)
                                      for c, b, _, _, _ in quadratic) for z in range(p))
    second = sum(math.prod(fi(c*y, p, H) for c, _, _, _, _ in quadratic)
                 for y in range(p))
    mu = Q(first*second, p**3*den)
    check('exact_independent_baseline', mu == Q(H+1, p)**(d+2*s))
    pairs = list(combinations(range(slots), 2))
    physical = []
    D = [[0]*p for _ in range(slots)]
    for h in range(p):
        lin = math.prod(fi(xi*h, p, H) for xi, _, _ in linear)
        if not lin:
            continue
        for x in range(p):
            weight = lin*math.prod(fi((2*c*x+b)*h, p, H)*fi(c*h*h, p, H)
                                  for c, b, _, _, _ in quadratic)
            if not weight:
                continue
            vertices = tuple((x+i*h) % p for i in range(slots))
            host = all(v in Om for v in vertices)
            physical.append((h, vertices, weight, host))
            for i, v in enumerate(vertices):
                D[i][v] += weight
                if v in interior:
                    check('exact_interior_forces_entire_host', host)
    T = Q(sum(weight for _, _, weight, host in physical if host), p*p*den)
    eps = 1/math.sqrt(p)
    check('floating_T_lower', float(T) + 1e-12 >= float(w-boundary)*(float(mu)-eps))
    check('floating_T_upper', float(T) <= float(w)*(float(mu)+eps)+1/p+1e-12)
    boundary_bound = 2*slots*(slots-1)*(d+s)*H/p+2*s*(2+math.log(p))*eps
    check('floating_boundary_envelope', float(boundary) <= boundary_bound+1e-12)

    ternary = {sum(bit*3**j for j, bit in enumerate(bits))
               for bits in product([0, 1], repeat=5)}
    choices = [set(), {min(Om)}] + [{(x+shift) % p for x in ternary} & Om
                                   for shift in (0, 31, 137)]
    for A in choices:
        check('exact_global_cyclic_APfree', not any(
            (x+2*(y-x)) % p in A and (x+3*(y-x)) % p in A
            for x in A for y in A if y != x))
        occupied = len(A)
        a, U = Q(occupied, n), w*Q(occupied, n)*(1-Q(occupied, n))
        Mraw = [0, 0, 0]
        Jraw, Jhostraw = [0]*len(pairs), [0]*len(pairs)
        Sdiag, Cdiag, slackraw = 0, 0, 0
        for h, vertices, weight, host in physical:
            un = [(n*int(v in A)-occupied) if v in Om else 0 for v in vertices]
            for z, (i, j) in enumerate(pairs):
                q = weight*un[i]*un[j]
                Jraw[z] += q
                if host:
                    Jhostraw[z] += q
                    if not h:
                        Cdiag += q
            if not host:
                continue
            K = sum(v in A for v in vertices)
            if h:
                check('exact_physical_occupancy_cap', K <= cap)
                slackraw += weight*K*(cap-K)
            Mraw[0] += weight
            Mraw[1] += weight*K
            Mraw[2] += weight*math.comb(K, 2)
            if not h:
                Sdiag += weight*sum(un)
        M = [Q(z, p*p*den) for z in Mraw]
        S1 = M[1]-slots*a*T
        C2 = M[2]-(slots-1)*a*M[1]+math.comb(slots, 2)*a*a*T
        J = [Q(z, p*p*den*n*n) for z in Jraw]
        Jh = [Q(z, p*p*den*n*n) for z in Jhostraw]
        check('exact_centered_pair_expansion', C2 == sum(Jh))
        check('exact_single_diagonal_zero', Sdiag == 0)
        check('exact_pair_diagonal', Q(Cdiag, p*p*den*n*n) == len(pairs)*U/p)
        occ_upper = Q(cap-1, 2)*M[1]+Q(slots*(slots-cap), 2)*a*w/p
        check('exact_finite_occupancy_slack', occ_upper-M[2] == Q(slackraw, 2*p*p*den))
        E1 = slots*(float(mu*boundary)+eps*float(w+boundary)+2/p)
        beta = (float(mu)+eps)*float(boundary)+1/p
        E2 = len(pairs)*(beta+float(U)*eps)
        check('floating_single_envelope', abs(float(S1)) <= E1+1e-12)
        for z in range(len(pairs)):
            check('floating_pair_near_positivity', float(J[z]) >= -float(U)*eps-1e-12)
            check('floating_proper_host_pair_error', abs(float(J[z]-Jh[z])) <= beta+1e-12)
        check('floating_centered_pair_envelope', float(C2) >= -E2-1e-12)
        if a:
            coefficient = Q(cap-1, 2)-(slots-1)*a
            lhs = Q(slots, 2)*a*((slots-1)*a-(cap-1))*T
            diagonal = Q(slots*(slots-cap), 2)*a*w/p
            check('exact_finite_terminal_identity_bound',
                  lhs <= coefficient*S1+diagonal+max(Q(0), -C2))
            check('floating_finite_terminal_envelope',
                  float(lhs) <= abs(float(coefficient))*E1+float(diagonal)+E2+1e-12)
    records.append({'p': p, 'H': H, 'slots': slots, 'cap': cap,
                    'linear': linear, 'quadratic': quadratic,
                    'host_size': n, 'interior_size': len(interior),
                    'mu': str(mu), 'T': str(T), 'APfree_cases': len(choices)})

sources = [Path(__file__).name, 'FINITE_PATTERN_TERMINAL_20261018.md',
           'MIXED_QUADRATIC_TERMINAL_20261016.md', 'WEIGHTED_PAIR_REDUCTION_20261016.md']
result = {'date': '2026-10-18', 'offline': True, 'target_proved': False,
          'total_checks': sum(counts.values()), 'counts': dict(counts),
          'R4_12': 8, 'eight_element_witness': extremizers[0], 'cases': records,
          'scope': ['Finite Boolean, occupancy, diagonal and expansion checks are exact rational.',
                    'Square-root error envelope comparisons use floats.',
                    'All physical windows have nonempty eroded interiors.',
                    'These finite tests do not verify an asymptotic phase-selection theorem.'],
          'source_sha256': {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                            for name in sources}}
(ROOT/'FINITE_PATTERN_TERMINAL_VERIFICATION_20261018.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'total_checks': result['total_checks'], 'counts': dict(counts),
                  'cases': records, 'eight_element_witness': extremizers[0]}, indent=2))
