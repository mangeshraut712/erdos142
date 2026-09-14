# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Mangesh Raut

"""Adversarial probe of candidate terminal lemmas. Not a proof script."""
from fractions import Fraction as F
from itertools import product
from math import cos, sin, pi
from collections import Counter

REGIME_SET = [0, 20, 22, 25, 30, 32, 33, 34, 37, 38, 39, 48, 49, 52,
              53, 54, 58, 59, 78, 79, 81, 84, 88, 90, 93, 94, 95, 97]


def interval_counts(bits):
    n, m = len(bits), sum(bits)
    prefix = [0]
    mask = 0
    for i, bit in enumerate(bits):
        prefix.append(prefix[-1] + bit)
        mask |= bit << i
    phi = 0
    for y, bit in enumerate(bits):
        if bit:
            lo = max(0, 2 * y - n + 1, (y + 1) // 2)
            hi = min(n - 1, 2 * y, (n - 1 + y) // 2)
            if lo <= hi:
                phi += prefix[hi + 1] - prefix[lo]
    sigma = four = m
    for d in range(1, (n - 1) // 3 + 1):
        triple = mask & (mask >> d) & (mask >> (2 * d))
        sigma += (triple & ((1 << (n - 3 * d)) - 1)).bit_count()
        sigma += (triple >> d).bit_count()
        four += 2 * (triple & (mask >> (3 * d))).bit_count()
    disc = max(abs(n * prefix[i] - m * i) for i in range(n + 1))
    return phi, sigma, four, disc, prefix


def class_stats(bits):
    n = len(bits)
    out = []
    for r in range(3):
        sub = bits[r::3]
        out.append((len(sub), sum(sub), F(sum(sub), len(sub)) if sub else F(0)))
    return out


def max_block_gain(bits, min_len=2):
    n, m = len(bits)
    a = F(m, n)
    best = F(0)
    best_len = 0
    prefix = [0]
    for b in bits:
        prefix.append(prefix[-1] + b)
    for i in range(n):
        for j in range(i + min_len, n + 1):
            L = j - i
            dens = F(prefix[j] - prefix[i], L)
            gain = dens - a
            if gain > best:
                best, best_len = gain, L
    return best, best_len


def fourier_max(bits):
    n, m = len(bits), sum(bits)
    a = m / n
    best = 0.0
    for k in range(1, n):
        re = im = 0.0
        for x, b in enumerate(bits):
            ang = 2 * pi * k * x / n
            v = b - a
            re += v * cos(ang)
            im += v * sin(ang)
        best = max(best, (re * re + im * im) ** 0.5 / n)
    return best


def chirp_max(bits):
    n, m = len(bits), sum(bits)
    a = m / n
    best = 0.0
    for c in range(n):
        for r in range(n):
            if c == 0 and r == 0:
                continue
            re = im = 0.0
            for x, b in enumerate(bits):
                ang = 2 * pi * ((c * x * x + r * x) % n) / n
                v = b - a
                re += v * cos(ang)
                im += v * sin(ang)
            best = max(best, (re * re + im * im) ** 0.5 / n)
    return best


def centers_G(bits):
    """Unnormalized 3-AP centers: G[x] = #{d: both x-d and x+d in A, x-d,x,x+d in range}."""
    n = len(bits)
    G = [0] * n
    for x in range(n):
        for d in range(1, n):
            y, z = x - d, x + d
            if 0 <= y < n and 0 <= z < n and bits[y] and bits[z]:
                G[x] += 1
    return G


def analyze(bits, tag):
    n, m = len(bits), sum(bits)
    if m == 0 or m == n:
        return None
    phi, sigma, four, disc, prefix = interval_counts(bits)
    a = F(m, n)
    c = (n * n + 2) // 3
    Mnum = F(four) - 2 * a * sigma + a * a * phi  # times 1, unnormalized mixed numerator
    # Mixed in Lambda units would divide by p^2; we compare ratios using C~c.
    phi_rel = F(phi) / (a * a * c) if a else None
    sigma_rel = F(sigma) / (a ** 3 * c) if a else None
    classes = class_stats(bits)
    max_class_gain = max(cl[2] - a for cl in classes if cl[0])
    # prefix discrepancy relative
    D = disc
    G = centers_G(bits)
    Gmax = max(G)
    meanG = F(sum(G), n)
    # popular one-sided: among completed window 3APs with d>0, endpoint membership
    left = right = both = none = q = 0
    for x in range(n):
        for d in range(1, (n - 1 - x) // 3 + 1):
            m1, m2, e = x + d, x + 2 * d, x + 3 * d
            if bits[m1] and bits[m2]:
                q += 1
                L, R = bits[x], bits[e]
                left += L and not R
                right += R and not L
                both += L and R
                none += (not L) and (not R)
    return {
        "tag": tag, "n": n, "m": m, "a": str(a),
        "ap_free": four == m,
        "phi_rel": str(phi_rel), "sigma_rel": str(sigma_rel),
        "Mnum": str(Mnum), "disc": D,
        "max_class_gain": str(max_class_gain),
        "class_gain_over_a": str(max_class_gain / a if a else None),
        "Gmax": Gmax, "meanG": str(meanG),
        "Gmax_over_a2n": str(F(Gmax, 1) / (a * a * n) if a else None),
        "fiber_q": q, "fiber_left": left, "fiber_right": right,
        "fiber_both": both, "fiber_none": none,
        "four": four, "phi": phi, "sigma": sigma, "c": c,
    }


def exhaustive_interval(n):
    stats = Counter()
    mixedish = []
    class_linear = 0
    mixed_and_class_tiny = 0
    examples = []
    for bits in product((0, 1), repeat=n):
        rec = analyze(bits, "exh")
        if rec is None:
            continue
        stats["total"] += 1
        if rec["ap_free"]:
            stats["free"] += 1
        else:
            continue
        phi_rel = F(rec["phi_rel"])
        sigma_rel = F(rec["sigma_rel"])
        Mnum = F(rec["Mnum"])
        gain_over_a = F(rec["class_gain_over_a"])
        # mixed-like: Phi within 1/16 of baseline, Sigma >= 7/8, Mnum <= 0
        if abs(phi_rel - 1) <= F(1, 16) and sigma_rel >= F(7, 8) and Mnum <= 0:
            stats["mixedish"] += 1
            if gain_over_a >= F(1, 8):
                class_linear += 1
            else:
                mixed_and_class_tiny += 1
                if len(examples) < 12:
                    examples.append((bits, rec))
        if abs(phi_rel - 1) <= F(1, 16):
            stats["phi_stable"] += 1
        if sigma_rel >= F(7, 8):
            stats["sigma_high"] += 1
        if Mnum <= 0 and rec["ap_free"]:
            stats["M_nonpos"] += 1
    return stats, class_linear, mixed_and_class_tiny, examples


def main():
    print("=== exhaustive 4AP-free intervals ===")
    for n in range(8, 13):
        stats, cl, tiny, examples = exhaustive_interval(n)
        print(n, dict(stats), "class_linear", cl, "mixed_tiny_class", tiny)
        for bits, rec in examples[:3]:
            print("  ex", bits, {k: rec[k] for k in
                  ("a", "phi_rel", "sigma_rel", "Mnum", "class_gain_over_a",
                   "fiber_q", "fiber_left", "fiber_right", "fiber_both", "fiber_none",
                   "Gmax", "Gmax_over_a2n")})

    print("\n=== regime set as cyclic interval of length 101 ===")
    bits = [int(x in REGIME_SET) for x in range(101)]
    rec = analyze(bits, "regime")
    print({k: rec[k] for k in rec if k not in ("tag",)})
    print("class stats", class_stats(bits))
    print("fourier_max", fourier_max(bits))
    print("chirp_max", chirp_max(bits))
    bg, bl = max_block_gain(bits, 4)
    print("max block gain len>=4", bg, "len", bl, "gain/a", bg / F(28, 101))

    print("\n=== affine images of 3AP-free seed in Z_13 ===")
    # 3AP-free: {0,1,3,9} is geometric; also {0,1,4}
    p = 13
    seed = [0, 1, 4]
    for mul in range(1, p):
        for add in range(p):
            A = sorted(((mul * x + add) % p) for x in seed)
            bits = [int(i in A) for i in range(p)]
            rec = analyze(bits, "aff")
            if rec and rec["ap_free"]:
                print("A", A, {k: rec[k] for k in
                      ("phi_rel", "sigma_rel", "Mnum", "class_gain_over_a", "ap_free")})
                break  # one add per mul is enough if pattern similar
        else:
            continue

    print("\n=== 3AP-free Behrend-like small sphere encoded ===")
    # dimension 2, s=3, base 6: points (x,y) with x^2+y^2 = R max sphere in {0,1,2}^2
    pts = {}
    for x, y in product(range(3), repeat=2):
        pts.setdefault(x * x + y * y, []).append(x + y * 6)
    sphere = max(pts.values(), key=len)
    print("sphere", sphere, "len", len(sphere))
    for p in (37, 41, 43):
        bits = [int(i in set(sphere)) for i in range(p)]
        rec = analyze(bits, "sph")
        print("p", p, {k: rec[k] for k in
              ("m", "a", "ap_free", "phi_rel", "sigma_rel", "Mnum",
               "class_gain_over_a", "Gmax_over_a2n")})


if __name__ == "__main__":
    main()
