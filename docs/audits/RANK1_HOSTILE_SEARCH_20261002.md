# Rank-one energy of 4-AP-free sets: hostile finite search

2 October 2026. Offline. **(E) OPEN — ONE EXACT OBSTRUCTION (unchanged).**

No proof or counterexample to the target-scale statement (OPEN) of
TARGET_SCALE_ENERGY_BUDGET_20260914.md section 7 is obtained. No bound for
r_4(N) is claimed. These are finite diagnostics, not asymptotic evidence.

## 1. Question tested

(OPEN) asks for a rotated-quarter factor of rank <= K log^2(2/a) with
Var(E(B|F)) >= c a^2/log(2/a). Rank one is the cheapest such factor; by
(8) of that report its best energy is >= (4/pi^2) max|fhat|^2. The test:
do actual 4-AP-free sets carry more rank-one energy than random sets of
the same size, i.e. does AP-freeness leave any detectable linear trace?

Cells are exactly `cells` of verify_full_group_hostile_20260914.py: every
nonzero xi and all 8p rotations t/(8p). The maximiser is found with cyclic
prefix counts and its energy recomputed in exact rationals with `energy`.

## 2. Constructions

- Greedy: random order, add x unless it completes a 4-AP. p=211, 401
  (six seeds each), p=797 (two seeds). Densities 0.14-0.22.
- Hostile: from a greedy set, 150 swap moves preserving size and
  4-AP-freeness, accepting a move iff best rank-one energy does not rise.
  p=101, 151, 211. The final sets are stored in the JSON.
- Baseline: median best rank-one energy of 8 uniformly random sets of the
  same size (not AP-free).

Every reported set passes an exhaustive 4-AP check.

## 3. Results (E = best rank-one energy)

| p | |A| | a | E/a^2 (AP-free) | E/a^2 (random median) | 1/log(2/a) |
|---|---:|---:|---:|---:|---:|
| 211 greedy (6) | 44-47 | 0.21-0.22 | 0.26-0.38 | 0.28-0.32 | 0.45 |
| 401 greedy (6) | 66-70 | 0.16-0.17 | 0.19-0.29 | 0.21-0.24 | 0.41 |
| 797 greedy (2) | 111-113 | 0.14 | 0.153 | 0.156-0.165 | 0.38 |
| 101 hostile | 25 | 0.25 | 0.308 | 0.467 | 0.48 |
| 151 hostile | 34 | 0.23 | 0.263 | 0.400 | 0.46 |
| 211 hostile | 43 | 0.20 | 0.225 | 0.339 | 0.44 |

Over all 17 sets the ratio to the random median lies in [0.656, 1.324].

## 4. Reading

1. Greedy 4-AP-free sets are indistinguishable from random sets at rank
   one. E|A|/a^2 averages about 14, 16, 17 at |A| about 45, 69, 112: the slow
   logarithmic growth expected of the maximum of about 8p^2 noisy
   chi-squared statistics, not a fixed fraction of a^2.
2. Hostile search drives AP-free sets strictly BELOW the random baseline
   (0.66 times at p=101). AP-freeness and rank-one uniformity coexist
   easily at these sizes.
3. If this noise scaling persisted, rank-one energy would be
   O(a^2 log p/|A|) = o(a^2/log(2/a)) whenever a p >> log p log(2/a).
   So rank one cannot be the mechanism behind (OPEN): any proof must use
   the higher rank allowed, or input beyond linear Fourier coefficients.
   This agrees with section 5 of the target-scale report (4-AP counts are
   quadratic, not linear) and is not a refutation: small p cannot see the
   asymptotic regime, and greedy sets need not be extremal.

See VACUITY_OF_FULL_GROUP_OPEN_20261002.md: at large p, (OPEN) is vacuous
unless the target fails, so full-group searches like this one can only
probe pre-asymptotic behaviour.

## 5. Status and next step

(OPEN) stays unproved and unrefuted. Rank one is now ruled out as a
standalone route at the finite level. The next finite check is rank two
(pairs of characters, 16 cells) on the stored hostile sets, compared with
the noise baseline for 16 cells: if those also stay at noise, the
polylogarithmic-rank requirement is doing essential work.

Run `python3 verify_rank1_hostile_search_20261002.py` (about 7.5 minutes,
standard library only). Output: rank1_hostile_verification_20261002.json.
