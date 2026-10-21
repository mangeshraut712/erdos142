"""Finite diagnostics for the new attack; no structural input is proved here."""
import cmath
import itertools
import json
import math
from pathlib import Path
import random

rng = random.Random(14220261002)
counts = {"variable_energy_trajectories": 0, "exact_window_label_counts": 0,
          "quadratic_resonance_kernels": 0, "adversarial_cases": 0}

# Check arbitrary overshooting trajectories against the dyadic envelopes.
for t, beta, gamma, C, D, overshoot in itertools.product(
    [.005, .02, .1], [0, .25], [.1, .25, .5], [0, 1], [0, 1, 3], [1, 4, 20]
):
    eta = lambda a: .125 * a**beta / math.log(2/a)**C
    rank = lambda a: math.ceil(a**(-gamma) / math.log(2/a)**D)
    Dt, St = 1.0, math.log(1/t)
    e = t
    while e <= .8:
        hi = min(2*e, .8)
        m = eta(e)
        R = math.ceil(e**(-gamma)/math.log(2/hi)**D)
        M = 1 + 4*math.log(2)/m
        Dt += M*R
        St += M*(math.log(2/(m*e)) + math.log(4)*R)
        e *= 2
    a, actual_rank, actual_loss = t, 1, 0.0
    while a <= .8:
        s = rank(a)
        ap = min(1.0, a*(1+overshoot*eta(a)/2))
        # Log retained mass; avoids exponentiating enormous 4^s.
        log_r = math.log(eta(a)*a/2) - s*math.log(4)
        actual_loss += math.log(ap/a) - log_r
        actual_rank += s
        a = ap
    assert actual_rank <= Dt + 1e-8
    assert actual_loss <= St + 1e-8
    counts["variable_energy_trajectories"] += 1

# Independently verify the exact integer endpoint-label identity.
for p in [5, 7, 11, 13, 17]:
    for _ in range(45):
        d = rng.randint(1, 3)
        chars = [rng.randrange(1, p) for _ in range(d)]
        starts = [rng.randrange(p) for _ in range(d)]
        lengths = [rng.randint(1, p//3) for _ in range(d)]
        omega = [x for x in range(p) if all(
            (xi*x-start)%p < length
            for xi,start,length in zip(chars,starts,lengths))]
        labels = {}
        for x in omega:
            key = tuple((start+(xi*x-start)%p)%3
                        for xi,start in zip(chars,starts))
            labels[key] = labels.get(key, 0) + 1
        U = set(omega)
        raw = sum(all((x+j*h)%p in U for j in range(4))
                  for x in range(p) for h in range(p))
        assert raw == sum(v*v for v in labels.values())
        counts["exact_window_label_counts"] += 1

# All zero quadratic matrices have exactly the claimed one-parameter kernel.
for p in [5,7,11]:
    kernel = {tuple((t*c)%p for c in [1,-3,3,-1]) for t in range(p)}
    actual = set()
    for ts in itertools.product(range(p), repeat=4):
        if all(sum((j**power)*ts[j] for j in range(4))%p == 0
               for power in [0,1,2]):
            actual.add(ts)
        counts["quadratic_resonance_kernels"] += 1
    assert actual == kernel

# Representative finite adversarial sets. Classification is computed,
# never presumed from the informal family name. This is not asymptotic evidence.
p = 257
omega = list(range(65))
assert 64 < p/3 and len(omega) >= p*math.exp(-math.sqrt(math.log(p)))
families = {
    "random Boolean": {x for x in omega if rng.random()<.2},
    "quadratic Boolean interval": {x for x in omega if x*x%p<32},
    "3AP-free ternary digits": {sum(v*3**j for j,v in enumerate(vs))
        for vs in itertools.product([0,1],repeat=3)},
    "sparse cube": {sum(v*4**j for j,v in enumerate(vs))
        for vs in itertools.product([0,1],repeat=3)},
    "progression plus cube": {i+10*j+30*k for i in range(4)
        for j,k in itertools.product([0,1],repeat=2)},
    "concentrated interval": set(range(21)),
    "separated pieces": {0,1,3,4,60,61,63,64},
    "tensor seed": {i+10*j for i,j in itertools.product([0,1,3,4],repeat=2)},
}
adversarial = []
for name, A in families.items():
    assert A and A.issubset(omega)
    a = len(A)/len(omega)
    u = {x: float(x in A)-a for x in omega}
    nonzero4 = sum(all((x+j*h)%p in A for j in range(4))
                   for x in A for h in range(1,p))
    nonzero3 = sum(all((x+j*h)%p in A for j in range(3))
                   for x in A for h in range(1,p))
    maxcorr2, maxgain = 0.0, 0.0
    # All nonzero characters, and all unlabelled quarter-rotation states.
    for xi in range(1,p):
        corr = sum(u[x]*cmath.exp(-2j*math.pi*(xi*x%p)/p)
                   for x in omega)/len(omega)
        maxcorr2 = max(maxcorr2, abs(corr)**2)
        residues = [xi*x%p for x in omega]
        for j in range(p):
            sums, sizes = [0.0]*4, [0]*4
            for x,r in zip(omega,residues):
                # Rotation theta=(j+1/2)/(4p), exact cell labels via integers.
                slot = ((8*r-2*j-1)%(8*p))//(2*p)
                sums[slot] += u[x]
                sizes[slot] += 1
            gain = sum(z*z/n for z,n in zip(sums,sizes) if n)/len(omega)
            maxgain = max(maxgain,gain)
    assert maxgain+1e-10 >= (8/math.pi**2)*maxcorr2
    assert maxgain <= a*(1-a)+1e-10
    adversarial.append({"family":name,"p":p,"window_size":len(omega),
        "relative_density":a,"nonzero_ordered_4APs":nonzero4,
        "nonzero_ordered_3APs":nonzero3,"max_relative_coefficient_squared":maxcorr2,
        "best_one_character_quarter_energy":maxgain,
        "coefficient_squared_over_greedy_scale":maxcorr2/(a**2.5*math.log(2/a))})
    counts["adversarial_cases"] += 1

result = {"status":"finite supporting checks passed; H and greedy selection unproved",
          "checks":counts,"adversarial_examples":adversarial,
          "arithmetic":"integer label/kernel counts; floating energy diagnostics tolerance 1e-10",
          "external_dependencies":[]}
Path(__file__).with_name('structural_attack_verification_20261002.json').write_text(
    json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
