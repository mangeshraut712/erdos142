# Mod-3 classes alone give no density increment

2 October 2026. **(B) PROPOSED INCREMENT FALSE (as stated).**
This refutes the class-only step proposed at the end of
WINDOW_LATTICE_MODEL_20261002.md section 5. It does not affect the target
r_4(N)=o(N/log N), the window energy lemma, or any earlier theorem.

## 1. Statement refuted

Proposed: every 4-AP-free A of relative density a in a convex lattice set X
(equivalently a controlled window) above the cutoff has a mod-3 class of X
on which its relative density is >=(1+c)a, for a fixed c>0.

## 2. Three-block lemma — PROVED

Let A be a 4-AP-free subset of {0,...,n-1} and let t_1>=2n, t_2-t_1>=2n.
Then U=A union (A+t_1) union (A+t_2) is 4-AP-free.

Proof: let u_0<u_1<u_2<u_3 be a 4-AP in U with difference h. The gaps
between blocks have length >=n. If two consecutive terms share a block then
h<=n-1, so no step can cross a gap and all four terms lie in one block,
giving a 4-AP in a translate of A. Otherwise consecutive terms lie in
strictly increasing blocks, which needs four blocks; there are three.

Choose t_1=1 and t_2=2 mod 3. Each translate permutes the residue counts of
A cyclically, so U has exactly |A| points in every residue class mod 3:
the class densities of U in its hull interval are all equal (up to the
O(1) effect of unequal class sizes). Hence no c>0 works. U also satisfies
any cutoff of the form |hull|>=C/a^3 once A is a large near-extremal
4-AP-free set (Behrend-type sets have density n^(-o(1))).

The block [0,n) carries relative density about 5/3 times that of U: the
increment exists, but on an interval (a slab of the coordinate form), not
on a class. The proposal must therefore allow slabs or general character
cells, which is exactly what the quarter-arc energy lemma already does.

## 3. Exact small cases

For maximum 4-AP-free subsets of {0,...,n-1} (all extremal sets enumerated):

| n | r_4(n) | extremal sets | min over them of best class ratio | min of best interval (length >=n/4) ratio |
|---|---:|---:|---:|---:|
| 12 | 8 | 32 | 9/8 | 9/8 |
| 15 | 10 | 2 | 6/5 | 3/2 |
| 18 | 11 | 100 | 12/11 | 72/55 |
| 21 | 13 | 10 | 15/13 | 35/26 |
| 24 | 14 | 115 | 15/14 | 60/49 |
| 27 | 16 | 8 | 9/8 | 45/32 |
| 30 | 18 | 2 | **1** | 5/4 |

At n=30 an extremal set is exactly balanced mod 3. The interval ratios are
all >1 but are within the sampling fluctuation of a random set of the same
size (about a quarter of 18 points per interval), so they are not evidence
for an interval increment.

The concrete balanced example stored in the JSON: the extremal set
{0,1,2,4,5,7,8,9,14,15,16,18} in [0,20) with shifts 0,43,86 gives 36
points, 12 per class, 4-AP-free, hull density 12/35, and block density
7/4 times the hull density.

## 4. Status

Class-only increments are dead. The remaining hereditary question is the
original one: increments on cells of O(log(2/a)) quarter-arc character
coordinates (which include slabs), i.e. the window energy lemma, still OPEN.

Run `python3 verify_mod3_increment_20261002.py` (about 1 second). Output:
mod3_increment_verification_20261002.json.
