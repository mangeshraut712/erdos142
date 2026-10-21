"""Run: python3 verify_vacuity_20261002.py. Exact finite checks of the
integer/cyclic transfer lemmas in VACUITY_OF_FULL_GROUP_OPEN_20261002.md."""
from itertools import combinations
import json


def has_4ap_int(s):
    s = set(s)
    return any(x + h in s and x + 2*h in s and x + 3*h in s
               for x in s for h in range(1, max(s) + 1)) if s else False


def has_4ap_mod(s, p):
    s = set(x % p for x in s)
    return any((x + h) % p in s and (x + 2*h) % p in s and (x + 3*h) % p in s
               for x in s for h in range(1, p))


def r4_int(n):
    best = 0

    def grow(chosen, nxt):
        nonlocal best
        best = max(best, len(chosen))
        if len(chosen) + (n - nxt + 1) <= best:
            return
        for x in range(nxt, n + 1):
            if len(chosen) + (n - x + 1) <= best:
                return
            if not any(x - h in chosen and x - 2*h in chosen and x - 3*h in chosen
                       for h in range(1, x // 3 + 1)):
                chosen.add(x)
                grow(chosen, x + 1)
                chosen.remove(x)

    grow(set(), 1)
    return best


def r4_mod(p):
    for size in range(p, 0, -1):
        for s in combinations(range(p), size):
            if 0 in s and not has_4ap_mod(s, p):
                return size
    return 0


def primes_up_to(m):
    return [q for q in range(2, m + 1) if all(q % d for d in range(2, int(q**0.5) + 1))]


def main():
    out = {}
    cyclic = {p: r4_mod(p) for p in (5, 7, 11, 13, 17)}
    integer = {n: r4_int(n) for n in range(1, 41)}
    out["r4_mod_p"] = cyclic
    out["r4_int"] = integer
    out["cyclic_le_integer"] = all(cyclic[p] <= integer[p] for p in cyclic)

    transfer_ok, sharp = True, []
    for n in range(4, 13):
        free = [s for k in range(1, n + 1) for s in combinations(range(1, n + 1), k)
                if not has_4ap_int(s)]
        for p in primes_up_to(4*n):
            if p <= 3:
                continue
            bad = [s for s in free if has_4ap_mod(s, p)]
            if p > 2*n and bad:
                transfer_ok = False
            if p <= 2*n and p > n and bad and len(sharp) < 5:
                sharp.append({"N": n, "p": p, "set": list(bad[0])})
    out["integer_free_stays_free_mod_p_gt_2N"] = transfer_ok
    out["sharpness_examples_N_lt_p_le_2N"] = sharp
    out["target_proved"] = False
    print(json.dumps(out, indent=1))
    with open("vacuity_verification_20261002.json", "w") as fh:
        json.dump(out, fh, indent=1)
    assert out["cyclic_le_integer"] and transfer_ok and sharp


if __name__ == "__main__":
    main()
