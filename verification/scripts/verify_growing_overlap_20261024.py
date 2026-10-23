"""Exact growing-overlap incidence checks; no eligible selection claim."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
import json
import random

ROOT = Path(__file__).resolve().parents[2]
counts = Counter()


def check(ok, key):
    assert ok, key
    counts[key] += 1


def geometry(p):
    triples = set()
    edges = set()
    for x in range(p):
        for h in range(1, p):
            edge = frozenset((x+i*h) % p for i in range(4))
            edges.add(edge)
            triples.update(frozenset(s) for s in combinations(edge, 3))
    return edges, triples


def run():
    ratios = {Q(k-i, j-i) for i,j,k in permutations(range(4), 3)}
    check(ratios == {Q(-2),Q(-1),Q(-1,2),Q(1,3),Q(1,2),Q(2,3),Q(3,2),Q(2),Q(3)}, 'ratio_set')
    for n in range(2, 151):
        for k in range(n+1):
            check(k*(k-2) <= 3*(k*(k-1)*(k-2)//6), 'factorial_moment')
        a = Q(1, n-1)
        check(n*(n-1)*a*a == n*a, 'local_threshold')
        check(n*(n-1)*(a+Q(1,100*n))**2 > n*(a+Q(1,100*n)), 'local_threshold')
    records = []
    _, witness_triples = geometry(17)
    check(frozenset({0,1,4}) not in witness_triples, 'zero_completion_witness')
    for p in (5,7,11,13,17,19,29):
        edges, triples = geometry(p)
        for x,y in combinations(range(p), 2):
            predicted = {(x+(y-x)*r.numerator*pow(r.denominator,-1,p)) % p for r in ratios}
            actual = {next(iter(S-{x,y})) for S in triples if {x,y} <= S}
            check(actual == predicted and len(actual) <= 9, 'pair_codegree')
        check(len(triples) <= 3*Q(p*(p-1),2), 'hypergraph_size')
        # Deterministic independent-set witnesses, not an asymptotic search.
        independent = set()
        for x in range(p):
            if not any(S <= independent|{x} for S in triples):
                independent.add(x)
        records.append({'p':p, 'ambient_triples':len(triples), 'greedy_zero_completion_set':sorted(independent)})
    arithmetic_cases = 0
    zero_mean_cases = 0
    rng = random.Random(142)
    for p in (5,7,11,13,17):
        edges, triples = geometry(p)
        candidates = [set(s) for k in range(1, min(4,p)+1) for s in combinations(range(p), k)]
        if p >= 13:
            candidates = candidates[::11]
        for A in candidates:
            if any(e <= A for e in edges):
                continue
            host = A | {v for v in range(p) if v % 3 != 1}
            if host == A:
                continue
            H = 1 if p == 5 else 2
            def tent(t):
                d = min(t % p, (-t) % p)
                return Q(max(0,H+1-d), H+1)
            def weight(x,h):
                return tent(h)*tent(2*x*h)*tent(h*h)
            q = {v:Q(0) for v in host}
            # Independent anchor definition of q.
            for v in host:
                for j in range(4):
                    for h in range(1,p):
                        if all((v+(i-j)*h)%p in A for i in range(4) if i!=j):
                            q[v] += weight((v-j*h)%p,h)/p
            pairs = list(combinations(sorted(A),2))
            matrix = defaultdict(lambda:Q(0))
            grouped = defaultdict(lambda:Q(0))
            T = Q(0)
            residual = [Q(0)]*5
            a,w = Q(len(A),len(host)), Q(len(host),p)
            for x in range(p):
                for h in range(p):
                    vs = [(x+i*h)%p for i in range(4)]
                    if not all(v in host for v in vs):
                        continue
                    f = weight(x,h)
                    T += f/p**2
                    us = [Q(v in A)-a for v in vs]
                    for j in range(5):
                        for slots in combinations(range(4),j):
                            term = a**(4-j)*f/p**2
                            for i in slots: term *= us[i]
                            residual[j] += term
                    if not h:
                        continue
                    occupied = sorted(v for v in vs if v in A)
                    if len(occupied) != 3:
                        continue
                    v = next(v for v in vs if v not in A)
                    grouped[frozenset(occupied)] += f/p**2
                    for pair in combinations(occupied,2):
                        matrix[v,pair] += f/p
            alpha = a*w
            m = sum(q.values())/len(host)
            check(sum(grouped.values()) == w*m, 'weighted_hypergraph')
            check(all(t <= Q(12,p*p) for t in grouped.values()), 'individual_weight')
            check(sum(residual) == a*w/p, 'full_diagonal')
            check(residual[3]+residual[4] == a*w/p-a**4*T-residual[1]-residual[2], 'full_residual')
            for v in host:
                check(sum(matrix[v,c] for c in pairs) == 3*q[v], 'incidence_rows')
                check(q[v] <= 2*alpha, 'overlap_degree_recheck')
            for c in pairs:
                check(sum(matrix[v,c] for v in host) <= Q(12,p), 'incidence_columns')
            for f in ([Q(1)]*len(pairs), [Q(rng.randrange(-3,4),3) for c in pairs]):
                lhs = sum(sum(matrix[v,c]*f[i] for i,c in enumerate(pairs))**2 for v in host)
                rhs = Q(72,p)*alpha*sum(t*t for t in f)
                check(lhs <= rhs, 'schur_energy')
            check(sum(t*t for t in q.values())/len(host) <= 2*alpha*m, 'weighted_energy')
            check(sum(t*t for t in q.values())/len(host) <= 4*alpha**2*(len(A)-1)/p/w, 'matrix_energy')
            zero_mean_cases += m==0
            arithmetic_cases += 1
    report = dict(status='passed',date='2026-10-24',checks=sum(counts.values()),counts=dict(counts),
                  arithmetic_cases=arithmetic_cases,zero_mean_cases=zero_mean_cases,geometry_records=records,
                  target_proved=False,P12_proved=False,eligible_counterexample_found=False,
                  scope='All assertions use exact arithmetic. Finite positive radii are not the prescribed eligible radii. No phase-selection conclusion.')
    (ROOT/'verification/results/GROWING_OVERLAP_20261024.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    run()
