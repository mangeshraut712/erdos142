"""Exact finite checks for AP27; no asymptotic selection claim."""
from fractions import Fraction as Q
from itertools import combinations
from collections import defaultdict
import json
from pathlib import Path


def run():
    counts = defaultdict(int)

    def check(ok, label):
        assert ok, label
        counts[label] += 1

    cases = 0
    for p in (5, 7, 11):
        for host in (set(range(p)), set(range(p - 2))):
            pairs = list(combinations(sorted(host), 2))
            for A_tuple in [s for k in range(1, min(5, len(host)))
                            for s in combinations(sorted(host), k)][::3]:
                A = set(A_tuple)
                a, w = Q(len(A), len(host)), Q(len(host), p)
                U = w * a * (1-a)
                u = {v: Q(v in A)-a for v in host}
                for mode in (0, 1):
                    L = defaultdict(Q)
                    R, Rs = [Q(0)]*5, [Q(0)]*5
                    T, m_mass = Q(0), Q(0)
                    ap_free = True
                    for x in range(p):
                        for h in range(p):
                            vs = [(x+i*h) % p for i in range(4)]
                            if not all(v in host for v in vs):
                                continue
                            F = Q(1) if mode == 0 or h == 0 else Q((x+2*h) % 5, 4)
                            T += F/p**2
                            for j in range(5):
                                for slots in combinations(range(4), j):
                                    val = F*a**(4-j)/p**2
                                    for i in slots:
                                        val *= u[vs[i]]
                                    R[j] += val
                                    if h:
                                        Rs[j] += val
                            if not h:
                                continue
                            occupied = sum(v in A for v in vs)
                            ap_free &= occupied < 4
                            m_mass += F*Q(occupied*(occupied-1)*(occupied-2), 6)/p**2
                            for j in range(4):
                                for i, k in combinations([i for i in range(4) if i != j], 2):
                                    L[vs[j], tuple(sorted((vs[i], vs[k])))] += F/p
                    f = {c: u[c[0]]*u[c[1]] for c in pairs}
                    c2 = {c: Q(set(c) <= A)-a*a for c in pairs}
                    images = []
                    for signal in (f, c2):
                        image = {v: sum((L[v,c]*signal[c] for c in pairs), Q(0)) for v in host}
                        images += [sum(image.values())/p, sum(u[v]*image[v] for v in host)/p]
                        check(sum(t*t for t in image.values()) <= Q(288,p)*sum(t*t for t in signal.values()), 'schur')
                        psi = {v: Q((v*v+3*v) % 7-3, 3) for v in host}
                        adj = {c: sum((L[v,c]*psi[v] for v in host), Q(0)) for c in pairs}
                        check(sum(psi[v]*image[v] for v in host) == sum(adj[c]*signal[c] for c in pairs), 'adjoint')
                    expected = [2*Rs[2]/a**2, 3*Rs[3]/a, 2*(3*Rs[1]+Rs[2])/a**2, (4*Rs[2]+3*Rs[3])/a]
                    full = [2*R[2]/a**2-12*U/p, 3*R[3]/a-12*(1-2*a)*U/p,
                            2*(3*R[1]+R[2])/a**2-12*U/p, (4*R[2]+3*R[3])/a-12*U/p]
                    for actual, rhs, diag in zip(images, expected, full):
                        check(actual == rhs, 'starred_identity')
                        check(actual == diag, 'diagonal_identity')
                    for v in host:
                        check(sum(L[v,c] for c in pairs) <= 12, 'row_bound')
                    for c in pairs:
                        check(sum(L[v,c] for v in host) <= Q(24,p), 'column_bound')
                    for signal in (f,c2):
                        check(sum(signal.values())/len(pairs) == -a*(1-a)/(len(host)-1), 'pair_mean')
                    check(sum(t*t for t in f.values()) == ((p*U)**2-sum(t**4 for t in u.values()))/2, 'pair_norm_uu')
                    occ = len(A)*(len(A)-1)//2
                    check(sum(t*t for t in c2.values()) == occ*(1-a*a)**2+(len(pairs)-occ)*a**4, 'pair_norm_c2')
                    if ap_free:
                        m = m_mass/w
                        check(R[4] == 3*a**4*T+2*R[1]+R[2]-a*w*m+a*w*(1-4*a)/p, 'quartic_identity')
                        if m <= 2*a**3*T/w:
                            check(R[4] >= a**4*T-2*abs(R[1])-max(0,-R[2])+a*w*(1-4*a)/p, 'correct_low_mean_bound')
                    cases += 1
    report = dict(status='passed', date='2026-11-03', checks=sum(counts.values()),
                  counts=dict(counts), cases=cases, target_proved=False, P12_proved=False,
                  scope='Exact Fraction checks of AP27. Arbitrary kernels test algebra only; no eligible asymptotic counterexample or phase gain.')
    path = Path(__file__).resolve().parents[1]/'results/ALL_PAIR_OPERATOR_20261103.json'
    path.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    run()
