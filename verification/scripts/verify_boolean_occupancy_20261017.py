"""Independent finite checks for Boolean occupancy and the 2/3 terminal bound.

Physical arithmetic is exact rational. Only the previously proved finite
square-root error envelopes use floating arithmetic. No finite check claims
phase selection or an asymptotic AP-free counterexample.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[2]
counts = Counter()


def check(label, condition):
    assert condition, label
    counts[label] += 1


def fi(t, p, H):
    return max(0, H + 1 - min(t % p, (-t) % p))


# Pointwise identities, including all occupancy counts and both density ends.
for a in [Q(j, 17) for j in range(18)] + [Q(1, 2), Q(2, 3)]:
    for bits in product([0, 1], repeat=4):
        u = [Q(b) - a for b in bits]
        for b, z in zip(bits, u):
            check('exact_Boolean_square', z*z == (1-2*a)*z+a*(1-a))
        R = [a**(4-j)*sum((math.prod(u[i] for i in I)
                           for I in combinations(range(4), j)), Q(0))
             for j in range(5)]
        K = sum(bits)
        M = [Q(math.comb(K, j)) if j <= K else Q(0) for j in range(5)]
        check('exact_pointwise_Q',
              R[3]+R[4] == M[4]-a*a*M[2]+2*a**3*M[1]-3*a**4)
        check('exact_pointwise_expansion', sum(R) == math.prod(bits))
        if K <= 3:
            check('exact_missing_edge_occupancy', math.comb(K, 2) <= K)
            check('exact_occupancy_slack', K-math.comb(K, 2) == int(K in [1, 2]))


# Exact abstract law sharpness. These are explicitly not arithmetic examples.
sharp = {(0, 0, 0, 0): Q(1, 9)}
for missing in range(4):
    sharp[tuple(int(i != missing) for i in range(4))] = Q(2, 9)
check('exact_two_thirds_law_mass', sum(sharp.values()) == 1)
for i in range(4):
    check('exact_two_thirds_marginal', sum(q*b[i] for b, q in sharp.items()) == Q(2, 3))
for i, j in combinations(range(4), 2):
    check('exact_two_thirds_pair', sum(q*b[i]*b[j] for b, q in sharp.items()) == Q(4, 9))
a = Q(2, 3)
R3 = sum(q*a*sum(math.prod(b[i]-a for i in I) for I in combinations(range(4), 3))
         for b, q in sharp.items())
R4 = sum(q*math.prod(z-a for z in b) for b, q in sharp.items())
check('exact_two_thirds_residuals', R3 == Q(-16, 81) and R4 == 0)

for a in [Q(j, 38) for j in range(20)]:
    law = {bits: a**sum(bits)*(1-a)**(4-sum(bits))+(-1)**(sum(bits)+1)*a**4
           for bits in product([0, 1], repeat=4)}
    check('exact_lower_moment_law_probability', min(law.values()) >= 0 and sum(law.values()) == 1)
    check('exact_lower_moment_law_AP_exclusion', law[(1, 1, 1, 1)] == 0)
    for k in range(4):
        for I in combinations(range(4), k):
            check('exact_lower_moment_law_moment',
                  sum(q*math.prod(bits[i] for i in I) for bits, q in law.items()) == a**k)
    check('exact_lower_moment_law_quartic',
          sum(q*math.prod(z-a for z in bits) for bits, q in law.items()) == -a**4)


records = []
configs = [
    (7, 2, [(1, 0, 7)], []),
    (11, 3, [(1, 8, 7)], []),
    (11, 3, [(1, 0, 10)], [(1, 1, 0, 0, 8)]),
    (13, 4, [], [(1, 0, 0, 11, 8)]),
    (7, 2, [(1, 2, 3)], []),
]
for p, H, linear, quadratic in configs:
    d, s = len(linear), len(quadratic)
    den = (H+1)**(d+2*s)

    def inside(v, erosion=0):
        return all(erosion <= (xi*v-start) % p < length-erosion
                   for xi, start, length in linear) and all(
                       erosion <= (c*v*v+b*v+e-start) % p < length-erosion
                       for c, b, e, start, length in quadratic)

    Om = [v for v in range(p) if inside(v)]
    n = len(Om)
    assert n > 0
    w = Q(n, p)
    boundary = Q(sum(not inside(v, 12*H) for v in Om), p)
    first = sum(math.prod(fi(xi*t, p, H) for xi, _, _ in linear)*
                math.prod(fi(b*t+c*z, p, H) for c, b, _, _, _ in quadratic)
                for t in range(p) for z in range(p))
    second = sum(math.prod(fi(c*y, p, H) for c, _, _, _, _ in quadratic)
                 for y in range(p))
    mu = Q(first*second, p**3*den)
    edges = []
    for x in range(p):
        for h in range(p):
            vertices = tuple((x+i*h) % p for i in range(4))
            if not all(v in Om for v in vertices):
                continue
            weight = math.prod(fi(xi*h, p, H) for xi, _, _ in linear)*math.prod(
                fi((2*c*x+b)*h, p, H)*fi(c*h*h, p, H)
                for c, b, _, _, _ in quadratic)
            edges.append((h, vertices, weight))
    T = Q(sum(weight for _, _, weight in edges), p*p*den)
    nonzero_edges = {frozenset(vertices) for h, vertices, _ in edges if h}
    cases = 0
    for mask in range(1 << n):
        A = {Om[i] for i in range(n) if mask >> i & 1}
        if any(edge <= A for edge in nonzero_edges):
            continue
        m = len(A)
        a = Q(m, n)
        U = w*a*(1-a)
        Mraw = [0]*5
        Rraw = [0]*5
        diag = [0]*5
        occ_slack = 0
        for h, vertices, weight in edges:
            K = sum(v in A for v in vertices)
            un = [n*int(v in A)-m for v in vertices]
            for j in range(5):
                Mraw[j] += weight*(math.comb(K, j) if j <= K else 0)
                z = weight*m**(4-j)*sum(math.prod(un[i] for i in I)
                                       for I in combinations(range(4), j))
                Rraw[j] += z
                if h == 0:
                    diag[j] += z
            if h and K in [1, 2]:
                occ_slack += weight
        M = [Q(z, p*p*den) for z in Mraw]
        R = [Q(z, p*p*den*n**4) for z in Rraw]
        diagonal = [Q(z, p*p*den*n**4) for z in diag]
        check('exact_host_count', M[0] == T)
        check('exact_APfree_diagonal', M[4] == a*w/p)
        for j in range(5):
            formula = sum((-1)**(j-k)*math.comb(4-k, j-k)*a**(4-k)*M[k]
                          for k in range(j+1))
            check('exact_host_residual_expansion', R[j] == formula)
        check('exact_host_Boolean_square', sum((Q(int(v in A))-a)**2 for v in Om)/p == U)
        check('exact_host_Q_identity', R[3]+R[4] == a*w/p-a**4*T-R[1]-R[2])
        check('exact_host_missing_edge_inequality', M[2] <= M[1]+2*a*w/p)
        check('exact_host_occupancy_slack', M[1]+2*a*w/p-M[2] == Q(occ_slack, p*p*den))
        check('exact_R1_diagonal', diagonal[1] == 0)
        check('exact_R2_diagonal', diagonal[2] == 6*a*a*U/p)
        check('exact_R3_diagonal', diagonal[3] == 4*a*(1-2*a)*U/p)
        check('exact_R4_diagonal', diagonal[4] == (1-3*a+3*a*a)*U/p)
        if a:
            E1, E2 = abs(R[1]), max(Q(0), -R[2])
            rhs = abs(1-3*a)*E1/a**3+2*a*w/p+E2/a**2
            check('exact_finite_terminal_polynomial', 2*a*(3*a-2)*T <= rhs)
            if a > Q(2, 3):
                error = abs(1-3*a)*E1/(6*a**4*T)+w/(3*p*T)+E2/(6*a**3*T)
                check('exact_finite_two_thirds_bound', a <= Q(2, 3)+error)
            eps = 1/math.sqrt(p)
            beta = (float(mu)+eps)*float(boundary)+1/p
            E1f = 4*float(a)**3*(float(mu*boundary)+eps*float(w+boundary)+2/p)
            E2f = float(a)**2*(6*beta+6*float(U)*eps)
            check('floating_first_residual_envelope', float(abs(R[1])) <= E1f+1e-12)
            check('floating_pair_residual_envelope', float(R[2]) >= -E2f-1e-12)
            rhsf = abs(1-3*float(a))*E1f/float(a)**3+2*float(a*w)/p+E2f/float(a)**2
            check('floating_explicit_terminal_envelope', float(2*a*(3*a-2)*T) <= rhsf+1e-12)
        cases += 1
    records.append({'p': p, 'H': H, 'linear': linear, 'quadratic': quadratic,
                    'n': n, 'T': str(T), 'mu': str(mu), 'APfree_cases': cases})

sources = ['docs/audits/BOOLEAN_OCCUPANCY_TERMINAL_20261017.md',
           'verification/scripts/verify_boolean_occupancy_20261017.py',
           'docs/audits/MIXED_QUADRATIC_TERMINAL_20261016.md',
           'docs/audits/WEIGHTED_PAIR_REDUCTION_20261016.md']
result = {
    'date': '2026-10-17', 'offline': True, 'target_proved': False,
    'counts': dict(counts), 'total_checks': sum(counts.values()), 'cases': records,
    'scope': ['Boolean and physical progression identities are exact rational.',
              'Square-root error envelopes use floating arithmetic.',
              'The abstract probability laws are not arithmetic AP-free constructions.',
              'The asymptotic 2/3 terminal bound follows from the proof, not finite extrapolation.',
              'No phase selection or P12 claim is proved.'],
    'source_sha256': {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                      for name in sources},
}
(ROOT/'verification'/'results'/'BOOLEAN_OCCUPANCY_VERIFICATION_20261017.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'total_checks': result['total_checks'], 'counts': dict(counts),
                  'APfree_cases': sum(z['APfree_cases'] for z in records)}, indent=2))
