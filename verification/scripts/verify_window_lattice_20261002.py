"""Run: python3 verify_window_lattice_20261002.py. Exact finite checks for
WINDOW_LATTICE_MODEL_20261002.md. Integers only; not an asymptotic proof."""
from itertools import product
import json
import random


def is_prime(n):
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for q in small:
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in small:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x*x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def window(p, coords):
    """coords: list of (xi, lo, hi) integer intervals, diameter < p/3."""
    return [x for x in range(p)
            if all(lo <= (xi*x) % p <= hi for xi, lo, hi in coords)]


def aps(p, pts, length):
    s = set(pts)
    out = []
    for x in pts:
        for h in range(1, p):
            if all((x + i*h) % p in s for i in range(1, length)):
                out.append((x, h))
    return out


def lift(p, coords, x):
    return tuple(lo + (((xi*x) % p) - lo) for xi, lo, hi in coords)


def lattice_aps(vecs, length):
    s = set(vecs)
    out = 0
    for u in vecs:
        for v in vecs:
            if v == u:
                continue
            w = tuple(b - a for a, b in zip(u, v))
            if all(tuple(a + i*c for a, c in zip(u, w)) in s for i in range(length)):
                out += 1
    return out


def check_lift(rng, trials):
    """Lemma 1: modular APs in Omega <-> integer APs of the lifts."""
    ok = 0
    for _ in range(trials):
        p = rng.choice([101, 103, 107, 109, 113, 127])
        r = rng.randint(1, 3)
        coords = [(1, 0, rng.randint(10, p//3 - 1))]
        for _ in range(r - 1):
            lo = rng.randint(0, p - 1)
            coords.append((rng.randint(1, p - 1), lo, lo + rng.randint(5, p//3 - 1)))
        coords = [(xi, lo % p, (lo % p) + (hi - lo)) for xi, lo, hi in coords]
        pts = [x for x in range(p) if all(
            0 <= ((xi*x - lo) % p) <= hi - lo for xi, lo, hi in coords)]
        vec = {x: tuple(lo + ((xi*x - lo) % p) for xi, lo, hi in coords) for x in pts}
        assert len(set(vec.values())) == len(pts)
        for length in (3, 4):
            mod = len(aps(p, pts, length))
            lat = lattice_aps(list(vec.values()), length)
            assert mod == lat, (p, coords, length, mod, lat)
        ok += 1
    return ok


def check_threshold():
    """{0,1,2}^r has 3^r points and no 4AP; random convex lattice sets with
    more than 3^r points always contain one (pigeonhole mod 3)."""
    res = {}
    for r in (1, 2, 3):
        cube = list(product(range(3), repeat=r))
        res[r] = {"cube_size": len(cube), "cube_4aps": lattice_aps(cube, 4),
                  "cube_3aps": lattice_aps(cube, 3)}
        assert res[r]["cube_4aps"] == 0 and res[r]["cube_3aps"] > 0
    rng = random.Random(7)
    tested = 0
    for _ in range(300):
        r = rng.randint(1, 3)
        box = [rng.randint(1, 5) for _ in range(r)]
        shear = [[rng.randint(-2, 2) for _ in range(r)] for _ in range(r)]
        pts = []
        for u in product(*[range(-6, 7)]*r):
            y = [sum(shear[i][j]*u[j] for j in range(r)) + u[i] for i in range(r)]
            if all(abs(y[i]) <= box[i] for i in range(r)):
                pts.append(u)
        if len(pts) > 3**r:
            assert lattice_aps(pts, 4) > 0
            tested += 1
    res["random_convex_sets_above_3^r_all_contain_4ap"] = tested
    return res


def digit_window(d):
    """Omega = {sum eps_i 8^i : eps_i in {0,1,2}} as a controlled window of
    rank d+1 in Z_p: one interval for x, one coordinate per digit."""
    D = 8**d
    p = 100*D*D + 1
    while not is_prime(p):
        p += 1
    coords = []
    for j in range(1, d + 1):
        xi = -(-p // 8**j)
        coords.append((xi, 0, (p*37) // 112))
    assert all(hi < p/3 for _, _, hi in coords)
    pts = [x for x in range(D)
           if all((xi*x) % p <= hi for xi, _, hi in coords)]
    expected = sorted(sum(e*8**i for i, e in enumerate(eps))
                      for eps in product(range(3), repeat=d))
    assert pts == expected, d
    s = set(pts)
    four = sum(1 for x in pts for y in pts if x < y and (y - x) % 3 == 0
               and x + (y - x)//3 in s and x + 2*(y - x)//3 in s)
    three = sum(1 for x in pts for y in pts if x < y and (y - x) % 2 == 0
                and (x + y)//2 in s)
    # Integer APs equal modular APs here: all points lie in [0, D) and p > 2D.
    return {"d": d, "rank": d + 1, "p": p, "size": len(pts),
            "size_equals_3^(rank-1)": len(pts) == 3**d,
            "nontrivial_4aps": four, "nontrivial_3aps": three}


def endpoint_supply(rng, trials):
    """Pairs of A-points congruent mod 3 in lattice coordinates give 4APs of
    Omega with A-endpoints; count >= |A|^2/3^r - |A| ordered pairs."""
    worst = None
    for _ in range(trials):
        r = rng.randint(1, 3)
        side = rng.randint(4, 9)
        pts = list(product(range(side), repeat=r))
        a_pts = rng.sample(pts, rng.randint(2, len(pts)//2))
        s = set(pts)
        pairs = 0
        for u in a_pts:
            for v in a_pts:
                if u != v and all((b - a) % 3 == 0 for a, b in zip(u, v)):
                    w = [(b - a)//3 for a, b in zip(u, v)]
                    assert all(tuple(a + i*c for a, c in zip(u, w)) in s for i in range(4))
                    pairs += 1
        bound = len(a_pts)**2/3**r - len(a_pts)
        assert pairs >= bound - 1e-9
        slack = pairs - bound
        worst = slack if worst is None else min(worst, slack)
    return {"trials": trials, "min_pairs_minus_bound": worst}


def main():
    rng = random.Random(20261002)
    out = {
        "lift_isomorphism_trials": check_lift(rng, 40),
        "threshold": check_threshold(),
        "digit_windows": [digit_window(d) for d in (2, 3, 4, 5)],
        "endpoint_supply": endpoint_supply(rng, 200),
        "target_proved": False,
    }
    for w in out["digit_windows"]:
        assert w["size_equals_3^(rank-1)"] and w["nontrivial_4aps"] == 0
        assert w["nontrivial_3aps"] > 0
    with open(Path(__file__).resolve().parents[1] / "results" / "window_lattice_verification_20261002.json", "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
