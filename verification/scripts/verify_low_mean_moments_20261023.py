"""Exact checks of occupancy feasibility and completion bounds; no closure claim."""
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


def run():
    laws = 0
    # Independently enumerate all rational occupancy distributions on a grid.
    for denominator in range(1, 17):
        for n0 in range(denominator + 1):
            for n1 in range(denominator - n0 + 1):
                for n2 in range(denominator - n0 - n1 + 1):
                    ps = [Q(n0, denominator), Q(n1, denominator),
                          Q(n2, denominator), Q(denominator-n0-n1-n2, denominator)]
                    s1 = sum(k*ps[k] for k in range(4))
                    s2 = sum(Q(k*(k-1), 2)*ps[k] for k in range(4))
                    t = ps[3]
                    check(max(0, (2*s2-s1)/3) <= t <= min(s2/3, 1-s1+s2))
                    check(ps == [1-s1+s2-t, s1-2*s2+3*t, s2-3*t, t])
                    laws += 1
    zero_laws = 0
    for denominator in range(3, 31):
        for numerator in range(1, denominator//3 + 1):
            a = Q(numerator, denominator)
            for t in (Q(0), 2*a**3, 4*a**3):
                ps = [1-4*a+6*a*a-t, 4*a-12*a*a+3*t, 6*a*a-3*t, t]
                check(min(ps) >= 0 and sum(ps) == 1)
                moments = [Q(0)]*5
                for bits in product((0, 1), repeat=4):
                    k = sum(bits)
                    if k == 4:
                        continue
                    prob = ps[k]/len(list(combinations(range(4), k)))
                    for j in range(5):
                        for slots in combinations(range(4), j):
                            value = prob*a**(4-j)
                            for i in slots:
                                value *= bits[i]-a
                            moments[j] += value
                check(moments[1] == moments[2] == 0)
                check(moments[3] == a*t-4*a**4)
                check(moments[4] == 3*a**4-a*t)
                check(moments[3]+moments[4] == -a**4)
                zero_laws += 1
    cases = 0
    zero_mean_cases = 0
    for p, max_size in ((5, 5), (7, 7), (11, 3), (13, 2)):
        for size in range(1, max_size+1):
            for vertices in combinations(range(p), size):
                A = set(vertices)
                if any(all((x+i*h) % p in A for i in range(4))
                       for x in range(p) for h in range(1, p)):
                    continue
                # A proper host and a positive, non-symmetric rational weight.
                host = A | {v for v in range(p) if v % 3 != 1}
                a, w = Q(len(A), len(host)), Q(len(host), p)
                if a == 1:
                    continue
                q = {v: Q(0) for v in host}
                masses = [Q(0)]*4
                full = [Q(0)]*4
                endpoint_triples = 0
                for x in range(p):
                    for h in range(p):
                        vs = [(x+i*h) % p for i in range(4)]
                        if not all(v in host for v in vs):
                            continue
                        weight = Q(1) if h == 0 else Q(1+(x+2*h) % 5, 5)
                        k = sum(v in A for v in vs)
                        for j in range(4):
                            full[j] += weight*len(list(combinations(range(k), j)))/p**2
                        if h == 0:
                            continue
                        check(k <= 3)
                        masses[k] += weight/p**2
                        if all(v in A for v in vs[:3]):
                            endpoint_triples += 1
                        for j, v in enumerate(vs):
                            if all(vs[i] in A for i in range(4) if i != j):
                                q[v] += weight/p
                m = sum(q.values())/len(host)
                t0 = sum(masses)
                s1 = sum(k*masses[k] for k in range(4))
                s2 = sum(Q(k*(k-1), 2)*masses[k] for k in range(4))
                check(w*m == masses[3] == full[3]-4*a*w/p)
                check(max(0, (2*s2-s1)/3) <= w*m <= min(s2/3, t0-s1+s2))
                r1 = a**3*full[1]-4*a**4*full[0]
                r2 = a**2*full[2]-3*a**3*full[1]+6*a**4*full[0]
                lower = (4*a*(3*a-1)*full[0]+(6*a-1)*r1/a**3
                         +2*r2/a**2-8*a*w/p)
                check(lower == 2*s2-s1)
                check(3*w*m >= lower)
                check(all(q[v] == 0 for v in A))
                cap = 4*a*w
                check(all(0 <= value <= cap for value in q.values()))
                variance = sum((value-m)**2 for value in q.values())/len(host)
                z2 = sum((q[v]-m*(v not in A)/(1-a))**2 for v in host)/len(host)
                check(variance == a*m*m/(1-a)+z2)
                check(variance <= cap*m-m*m)
                check(z2 <= cap*m-m*m/(1-a))
                if m == 0:
                    check(endpoint_triples == 0)
                    zero_mean_cases += 1
                cases += 1
    report = dict(status='passed', date='2026-10-23', exact_checks=checks,
                  occupancy_grid_laws=laws, exchangeable_laws=zero_laws,
                  arithmetic_cases=cases, zero_mean_cases=zero_mean_cases,
                  target_proved=False, P12_proved=False,
                  eligible_counterexample_found=False,
                  scope='Exact Fraction checks. Arbitrary bounded weights test universal lemmas only; no T5 or prescribed-radius eligibility claim.')
    (ROOT/'verification/results/LOW_MEAN_MOMENTS_20261023.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    run()
