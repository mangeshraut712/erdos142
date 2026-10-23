"""Exact overlapping-AP and consistent local-law checks; no selection theorem."""
from fractions import Fraction as Q
from itertools import combinations, permutations
from collections import Counter
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
counts = Counter()


def check(value, category):
    assert value, category
    counts[category] += 1


def aps(V, p=None):
    result = set()
    for x in V:
        for y in V:
            if x == y:
                continue
            edge = frozenset((x+i*(y-x)) % p if p else x+i*(y-x) for i in range(4))
            if len(edge) == 4 and edge <= V:
                result.add(edge)
    return result


def normalized_pairs(p=None):
    pairs = set()
    for i, k in permutations(range(4), 2):
        for j, l in permutations(range(4), 2):
            r = (i-k)*pow(j-l, -1, p) % p if p else Q(i-k, j-l)
            z = (i-r*j) % p if p else i-r*j
            pairs.add((r, z))
    return pairs


def local_law(V, a):
    V = tuple(V)
    n = len(V)
    law = {frozenset(): 1-n*a+Q(n*(n-1), 2)*a*a}
    law.update({frozenset([v]): a-(n-1)*a*a for v in V})
    law.update({frozenset(S): a*a for S in combinations(V, 2)})
    return law


def run():
    rational_records = []
    histogram = Counter()
    I = set(map(Q, range(4)))
    for r, z in sorted(normalized_pairs()):
        J = {z+r*j for j in range(4)}
        V = I | J
        edges = aps(V)
        allowed = []
        for size in range(len(V)+1):
            for bits in combinations(V, size):
                occupied = frozenset(bits)
                if not any(edge <= occupied for edge in edges):
                    allowed.append(occupied)
        histogram[(len(I & J), len(edges))] += 1
        check(all(not I <= S and not J <= S for S in allowed), 'joint_polytope')
        law = local_law(V, Q(1, 10))
        check(all(S in allowed for S in law), 'joint_polytope')
        rational_records.append(dict(r=str(r), z=str(z), shared=len(I & J),
            vertices=[str(v) for v in sorted(V)], four_APs=len(edges),
            allowed_assignments=len(allowed)))
    check(dict(histogram) == {(2, 2): 28, (2, 3): 20, (3, 2): 4, (4, 1): 2}, 'classification')
    finite_types = {}
    for p in (5, 7, 11, 13, 17, 223):
        direct = {(r, z) for r in range(1, p) for z in range(p)
                  if len(set(range(4)) & {(z+r*j) % p for j in range(4)}) >= 2}
        check(direct == normalized_pairs(p), 'classification')
        hist = Counter()
        for r, z in direct:
            J = {(z+r*j) % p for j in range(4)}
            hist[(len(set(range(4)) & J), len(aps(set(range(4)) | J, p)))] += 1
        finite_types[str(p)] = {str(k): v for k, v in sorted(hist.items())}
        if p == 223:
            check(hist == histogram, 'classification')
    # Check a representative subdomain of every size; permutation symmetry covers the rest.
    for n in range(2, 11):
        V = tuple(range(n))
        for a in (Q(1, 2*(n-1)), Q(1, n-1)):
            law = local_law(V, a)
            check(sum(law.values()) == 1 and min(law.values()) >= 0, 'local_laws')
            for m in range(n+1):
                W = frozenset(range(m))
                marginal = Counter()
                for S, prob in law.items():
                    marginal[S & W] += prob
                wanted = local_law(W, a)
                check(all(marginal[S] == prob for S, prob in wanted.items()), 'local_laws')
            for i in V:
                check(sum(prob for S, prob in law.items() if i in S) == a, 'local_laws')
                for j in V:
                    if i != j:
                        check(sum(prob for S, prob in law.items() if {i, j} <= S) == a*a, 'local_laws')
            if n >= 4:
                r3 = r4 = Q(0)
                for S, prob in law.items():
                    u = [Q(i in S)-a for i in range(4)]
                    r3 += prob*a*sum(u[i]*u[j]*u[k] for i,j,k in combinations(range(4),3))
                    r4 += prob*u[0]*u[1]*u[2]*u[3]
                check(r3 == -4*a**4 and r4 == 3*a**4, 'local_laws')
    # Direct counterexample to using just the two named edge exclusions.
    E, D, occupied = {0,1,2,3}, {0,2,4,6}, {1,2,3,4}
    check(not E <= occupied and not D <= occupied and bool(aps(occupied)), 'cross_edge_witness')
    cases = 0
    low_mean_cases = 0
    phase_records = []
    for p in (5, 7, 11, 13):
        H = 1 if p < 7 else 2
        def tent(t):
            d = min(t % p, (-t) % p)
            return Q(max(0,H+1-d),H+1)
        F = {(x,h): tent(h)*tent(2*x*h)*tent(h*h) for x in range(p) for h in range(p)}
        for host in (set(range(p)), set(range((3*p+3)//4))):
            candidates = [set(S) for n in range(1, min(3,len(host))+1) for S in combinations(sorted(host), n)]
            if p == 11 and len(host) == p:
                candidates.append({0,1,2,4,5,7})
            for A in candidates:
                if aps(A, p) or A == host:
                    continue
                alpha, a, w = Q(len(A),p), Q(len(A),len(host)), Q(len(host),p)
                field = {}
                for v in host:
                    endpoint = {h: int(all((v+i*h)%p in A for i in (1,2,3))) for h in range(1,p)}
                    middle = {h: int(all((v+i*h)%p in A for i in (-1,1,2))) for h in range(1,p)}
                    for h in range(1,p):
                        check(endpoint[h]+middle[2*h % p] <= int((v+2*h)%p in A), 'cross_edge_injection')
                        check(endpoint[h]+endpoint[2*h % p] <= int((v+2*h)%p in A), 'cross_edge_injection')
                    channels = []
                    loss = Q(0)
                    for j in range(4):
                        value = Q(0)
                        for h in range(1,p):
                            bit = int(all((v+(i-j)*h)%p in A for i in range(4) if i != j))
                            weight = F[((v-j*h)%p,h)]
                            value += weight*bit/p
                            loss += (1-weight)*bit/p
                        channels.append(value)
                    q = sum(channels)
                    field[v] = q
                    slack = sum(int((v+2*h)%p in A)-endpoint[h]-middle[2*h % p] for h in range(1,p))/Q(p)
                    check(q == 2*(alpha-Q(v in A,p))-2*slack-loss, 'weighted_slack')
                    check(0 <= q <= 2*alpha, 'degree_bound')
                    check(channels[0] <= alpha/2 and channels[3] <= alpha/2, 'degree_bound')
                    check(v not in A or q == 0, 'hole_support')
                m = sum(field.values())/len(host)
                variance = sum((q-m)**2 for q in field.values())/len(host)
                check(variance <= 2*alpha*m-m*m, 'variance')
                check(m <= 2*alpha*(1-a), 'variance')
                R = [Q(0)]*5
                triples = Q(0)
                T = Q(0)
                for x in range(p):
                    for h in range(p):
                        vs = [(x+i*h)%p for i in range(4)]
                        if not all(v in host for v in vs):
                            continue
                        weight = F[x,h]/p**2
                        T += weight
                        u = [Q(v in A)-a for v in vs]
                        for j in range(5):
                            for slots in combinations(range(4),j):
                                val = weight*a**(4-j)
                                for i in slots: val *= u[i]
                                R[j] += val
                        if h and sum(v in A for v in vs) == 3:
                            triples += weight
                check(sum(R) == a*w/p, 'residual_diagonal')
                check(triples == w*m, 'completion_normalization')
                if m <= 2*a**3*T/w:
                    low_mean_cases += 1
                if len(host) == p and ((len(A) == 3 and sum(r["p"] == p for r in phase_records) < 2) or len(A) == 6):
                    x = np.arange(p)
                    u = np.array([float(Q(v in A)-a) for v in range(p)])
                    delta = max(abs(np.mean(u*np.exp(-2j*np.pi*(c*x*x+t*x)/p)))
                                for c in range(p) for t in range(p) if (c,t)!=(0,0))
                    phase_records.append(dict(p=p,A=sorted(A),H=H,a=str(a),m=str(m),
                        low_mean=bool(m<=2*a**3*T/w),Q_residual=str(R[3]+R[4]),
                        delta_floating=float(delta), eligible=False,
                        reason='T5 fails; chosen H differs from prescribed zero radius.'))
                cases += 1
    result = dict(status='passed', date='2026-10-23', checks=sum(counts.values()),
        counts=dict(counts), arithmetic_cases=cases, low_mean_cases=low_mean_cases, normalized_rational_types=rational_records,
        modular_classification=finite_types, floating_phase_diagnostics=phase_records,
        target_proved=False, P12_proved=False, eligible_counterexample_found=False,
        scope='Exact rational/integer assertions except explicitly labeled floating phase diagnostics. Local laws are not eligible global arithmetic instances.')
    (ROOT/'verification/results/OVERLAP_CONSTRAINTS_20261023.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    run()
