"""Run: python3 verify_mod3_increment_20261002.py. Exact checks for
MOD3_INCREMENT_20261002.md. Integers only; finite diagnostics."""
from fractions import Fraction as Q
import json
import random


def has_4ap(s):
    s = set(s)
    top = max(s) if s else 0
    return any(x + h in s and x + 2*h in s and x + 3*h in s
               for x in s for h in range(1, (top - x)//3 + 1))


def extremal_sets(n):
    """All maximum 4-AP-free subsets of {0,...,n-1}."""
    best, found = 0, []

    def grow(chosen, nxt):
        nonlocal best, found
        if len(chosen) + (n - nxt) < best:
            return
        if nxt == n:
            if len(chosen) > best:
                best, found = len(chosen), [tuple(chosen)]
            elif len(chosen) == best:
                found.append(tuple(chosen))
            return
        x = nxt
        if not any(x - h in chosen_set and x - 2*h in chosen_set and x - 3*h in chosen_set
                   for h in range(1, x//3 + 1)):
            chosen.append(x)
            chosen_set.add(x)
            grow(chosen, nxt + 1)
            chosen.pop()
            chosen_set.discard(x)
        grow(chosen, nxt + 1)

    chosen_set = set()
    grow([], 0)
    return best, found


def class_profile(a_set, n):
    """Relative density of A on each residue class mod 3 of {0..n-1},
    divided by the overall density."""
    a = Q(len(a_set), n)
    out = []
    for c in range(3):
        cls = [x for x in range(n) if x % 3 == c]
        out.append(Q(sum(1 for x in a_set if x % 3 == c), len(cls))/a)
    return out


def best_interval(a_set, n, min_len):
    a = Q(len(a_set), n)
    pref = [0]
    s = set(a_set)
    for x in range(n):
        pref.append(pref[-1] + (x in s))
    return max(Q(pref[j] - pref[i], j - i)/a
               for i in range(n) for j in range(i + min_len, n + 1))


def block_union(a_set, diam, shifts):
    return sorted(x + t for t in shifts for x in a_set)


def main():
    out = {}
    # Lemma 1: three far-apart copies of a 4-AP-free set stay 4-AP-free.
    rng = random.Random(1)
    checked = 0
    for _ in range(300):
        n = rng.randint(4, 30)
        a_set = [x for x in range(n) if rng.random() < 0.5]
        if len(a_set) < 2 or has_4ap(a_set):
            continue
        gap = 2*n + rng.randint(1, 5)
        t1 = gap + (1 - gap) % 3
        t2 = t1 + gap + (2 - (t1 + gap)) % 3
        u = block_union(a_set, n, (0, t1, t2))
        assert not has_4ap(u)
        assert len({x % 3 for x in u}) <= 3
        # with four copies an AP across the blocks can appear
        checked += 1
    out["three_block_union_4ap_free_trials"] = checked

    # Exact balance: copies shifted by residues 0,1,2 mod 3.
    best, sets = extremal_sets(20)
    a_set = sets[0]
    n = 20
    gap = 2*n + 1
    shifts = (0, gap + (1 - gap) % 3)
    shifts = shifts + (shifts[1] + gap + (2 - (shifts[1] + gap)) % 3,)
    u = block_union(a_set, n, shifts)
    hull = max(u) + 1
    counts = [sum(1 for x in u if x % 3 == c) for c in range(3)]
    out["balanced_example"] = {
        "base_set": list(a_set), "shifts": list(shifts), "hull": hull,
        "class_counts": counts, "4ap_free": not has_4ap(u),
        "hull_density": str(Q(len(u), hull)),
        "best_block_relative_density": str(Q(len(a_set), n)/Q(len(u), hull)),
    }
    assert not has_4ap(u) and len(set(counts)) == 1

    # Extremal sets for small n: class balance versus interval increments.
    rows = []
    for n in range(12, 31, 3):
        best, sets = extremal_sets(n)
        min_class = min(max(class_profile(s, n)) for s in sets)
        min_interval = min(best_interval(s, n, n//4) for s in sets)
        rows.append({"n": n, "r4": best, "extremal_count": len(sets),
                     "min_over_extremal_of_max_class_ratio": str(min_class),
                     "min_over_extremal_of_best_quarter_interval_ratio": str(min_interval)})
        print(rows[-1])
    out["extremal"] = rows
    out["target_proved"] = False
    with open(Path(__file__).resolve().parents[1] / "results" / "mod3_increment_verification_20261002.json", "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "extremal"}, indent=1))


if __name__ == "__main__":
    main()
