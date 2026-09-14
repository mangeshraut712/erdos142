<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Signed compression and a corrected terminal bridge

Date: 2026-09-13. Offline continuation. The active task's recent turn
metadata identifies gpt-6-astra. No API billing claim is made.

STATUS: (E) OPEN — NO NEW THEOREM

14 September scope note: the size/AP-availability cutoff in equation (8)
is essential to the formulation. The new version omitting it is refuted in
[UNIFORM_ENERGY_COUNTEREXAMPLE.md](UNIFORM_ENERGY_COUNTEREXAMPLE.md). That
construction does not refute equation (8) as written here; this qualified
lemma and the local r4 target remain open.

The local assertion r_4(N)=o(N/log N) is not proved or disproved. The
auxiliary propositions below are proved; novelty is not claimed. They
repair a conditional completion argument and isolate its missing input.

## 1. Corrections to the preceding closing statement

The closing paragraph of FINAL_FRONTIER_REPORT.md is not a complete
conditional implication as written. It requires three repairs:

1. A negative *corrected* mixed statistic is not an exhaustive alternative
   to low Sigma. At the regular center the corrected statistic is zero
   while the ordinary mixed form remains negative. That case must be
   included, not silently discarded.
2. The proposed lemma only applied at a<=1/2. Reaching density 1/2 is not
   the terminal criterion proved in the checkpoint. The conditional
   theorem below requires coverage until density exceeds 4/5.
3. A relative gain kappa>=a^s with s>0 does not yield O(log(1/a_0))
   steps. The logarithmic step count below requires an absolute positive
   kappa, or a separately proved accelerated recurrence.

The earlier statement that the displayed lemma alone would close the
target is withdrawn. This correction does not invalidate the earlier
relative identities, sampling estimate, or mass/size identities.

## 2. Sparse Fourier terms are not a coarse factor

On Z_p, p odd, use normalized Fourier coefficients. For B=1_A of density
a, f=B-a, and G(x)=E_y B(y)B(2x-y), direct Fourier inversion gives

    Ghat(xi)=Bhat(xi/2)^2,
    <f,G>=sum_{xi!=0} fhat(-xi) fhat(xi/2)^2.                (1)

Let R=max_{xi!=0}|fhat(xi)|. If P_L is the exact Fourier projection onto
a set L of nonzero frequencies, then

    |<f,P_L G>|<=|L| R^3.                                   (2)

This follows term by term from (1). If T=<f,G><=-c a^3 and
|<f,G-P_LG>|<=c a^3/2, (2) implies

    |L|>=c a^3/(2R^3).                                     (3)

Thus, conditionally on R<=K a^2, at least c/(2K^3 a^3) Fourier terms
are needed for this particular projection. This is not a lower bound on
the number of generators of a coarse arithmetic factor: many Fourier
terms may belong to one low-complexity frequency system. Nor does this
argument construct a target-regime AP-free family with R<=K a^2.

In a prime cyclic group one nonzero exact character separates every
point. Therefore 'measurable with respect to one character' without a
resolution or atom-count bound is vacuous. The factors below explicitly
specify their cells and number of atoms.

## 3. Signed-correlation compression gives factor energy — PROVED

Let (Omega,mu) be a finite probability space, B an indicator of mean a,
f=B-a, and G a nonnegative function with

    E G=a^2,  G<=K a^2,  <f,G><=-c a^3,

where K>1 and c>0. Let F be a finite partition, G_F=E(G|F), and
b_F=E(B|F). Suppose

    |<f,G-G_F>|<=c a^3/2.                                  (4)

Then

    E(b_F-a)^2 >= [c^2/(4(K-1))] a^2.                     (5)

Proof: conditional expectation preserves means and the bounds on G.
Consequently

    Var(G_F)<=E G_F^2-a^4<=K a^2 E G_F-a^4=(K-1)a^4.

Also <b_F-a,G_F>=<f,G_F><=-c a^3/2, by (4). Subtracting the mean of
G_F and applying Cauchy-Schwarz gives

    c^2 a^6/4 <= E(b_F-a)^2 Var(G_F),

which proves (5). This uses signed-correlation preservation, not uniform
approximation or an L1 approximation of all of G. The earlier positive-
translate support lower bound does not by itself prohibit (4).

## 4. Factor energy gives a useful atom — PROVED

Suppose a partition has at most M nonempty atoms and

    E(b_F-a)^2>=eta a^2,  0<eta<=1.

Then some atom P satisfies both

    density_P(A)>=a(1+eta/2),
    mu(P) density_P(A)/a >= eta a/(2M).                    (6)

The second quantity is the retained A-mass fraction.

Proof: write d_i for atom densities and mu_i for their probabilities.
Since sum mu_i d_i=a,

    sum mu_i d_i(d_i-a)=E(b_F-a)^2>=eta a^2.

Call an atom good if d_i-a>=eta a/2. On the other atoms,
sum mu_i d_i(d_i-a)<=eta a/2 * sum mu_i d_i<=eta a^2/2;
negative contributions only improve this bound. Hence good atoms
contribute at least eta a^2/2. Because d_i-a<=1, their total A-mass is
at least eta a^2/2. At most M atoms share that mass, proving (6).

For the preceding signed-compression proposition, take
eta=min(1,c^2/(4(K-1))). If the factor's atoms are hereditary controlled
windows and M is polynomial in 1/a, (6) is the required geometric gain.
Neither hypothesis on the partition has been established for all sets.

## 5. A direct terminal bound for coordinate windows — PROVED

Let p>3 be prime and Omega be a nonempty proper intersection of d>=1
circular intervals in nonzero character coordinates xi_j x. Put n=|Omega|
and let R be the greatest positive integer with R^d<=p-1. Every cyclic
4AP-free A subset Omega satisfies

    |A|/n <= 3/4 + [3d floor(p/R)]/(4n).                   (7)

The bound can be vacuous for small windows or large rank. Its proof does
not require regular radii or any unproved inverse theorem.

Proof: partition [0,1)^d into R^d half-open boxes of side 1/R. Among the
R^d+1 points (t xi_1/p,...,t xi_d/p) modulo one, 0<=t<=R^d, two lie in
one box. Their index difference q satisfies 1<=q<=R^d<p, and each
centered residue delta_j of q xi_j modulo p obeys
|delta_j|<=floor(p/R).

The map x->x+q is one p-cycle. For a circular interval I, translating
by a centered integer residue delta removes at most |delta| points.
Therefore

    D:=|Omega\(Omega+q)|<=sum_j |delta_j|<=d floor(p/R).

Because Omega is nonempty and proper, D is exactly the number of its
connected runs on the q-cycle. Partition each run into disjoint blocks
of four consecutive points and a remainder of at most three points.
Every full block is a nontrivial cyclic 4AP, so contains at most three
points of A. If r is the total remainder, r<=3D and

    |A|<=3(n-r)/4+r<=3n/4+3D/4.

This proves (7), including wraparound: all blocks are valid cyclic
progressions and q is nonzero.

For d=1, the construction has R=p-1 and floor(p/R)=1, giving the
expected 3n/4+3/4 bound along a rectified interval. For R=1 the same
proof applies, though the numerical estimate is generally uninformative.

## 6. Correct conditional completion, allowing logarithmic added rank

The following is a sufficient unproved hypothesis, not a result.

**Uniform coarse arithmetic energy lemma — OPEN.** There are fixed
0<eta<=1 and C>=1 such that every nontrivial-4AP-free A in a controlled
narrow window Omega with relative density 0<a<=4/5 and

    |Omega|>=max(256d3^d,8*3^d*a^-3)

admits a factor formed by partitioning each of at most
ceil(C log(2/a)) new nonzero character coordinates into four shifted
quarter-circle arcs, and refining Omega by those partitions, such that

    E_Omega [E(B|F)-a]^2 >= eta a^2.                        (8)

Every nonempty atom is a controlled narrow window in the same prime
group; no reset to a smaller modulus is allowed. The claim includes
all alternatives, including corrected mixed statistics near zero.
It must have constants independent of a,p,d and the initial window.

Here is the complete conditional implication of (8).

Let L=log(2/a_0) and kappa=eta/2. Each factor has at most

    M<=4^(C log(2/a)+1)<=4 exp(C log(4)L)

atoms. Equation (6) supplies a successor with relative gain >=kappa,
rank increase <=C L+1, and retained A-mass at least

    r_j>=eta a_j/(2M_j)>=eta a_0/[8 exp(C log(4)L)].          (9)

Thus each step costs at most

    -log r_j <= (1+C log4)L+log(8/eta).

After at most

    J=ceil(log((4/5)/a_0)/log(1+kappa))+1

steps the density exceeds 4/5. Put J=0 if it already exceeds 4/5.
Throughout,

    d_j<=d_0+J(C L+1)=O(L^2),
    log(n_0/n_j)
       =log(a_j/a_0)+sum_{i<j}log(1/r_i)=O(L^2).            (10)

The constants depend only on eta,C and the fixed starting rank. In
particular n_j>=n_0 exp(-C_1 L^2) and d_j<=C_2 L^2 for fixed constants.
The size cutoffs have logarithm O(d_j+log d_j+log(1/a_0))=O(L^2),
whereas log n_j>=log n_0-C_1 L^2. They persist for large n_0 whenever
L=O(log log n_0), so every proposed step remains eligible.

At the terminal stage R_j>= (p-1)^(1/d_j)/2. Since n_0 is comparable
to p, equation (10) gives

    log(n_j R_j/(d_j p))
       >= log(p-1)/(C_2 L^2)-C_1 L^2-O(log L+1) -> infinity

when a_0=epsilon/log N_0 and p is comparable to N_0. Formula (7) then
gives terminal density <=3/4+o(1), contradicting density >4/5.

For the one-time interval transfer, take a prime 3N_0<p<6N_0, using
the prime-existence result already proved in the checkpoint. Embedding
[N_0] gives a starting rank-one narrow window of n_0=N_0 points with
relative density a_0 unchanged. Any modular 4AP inside it has integer
second differences of absolute value <=2(N_0-1)<p, so it lifts to a
nontrivial integer 4AP. Subsequent restrictions stay in the same group.
Since epsilon>0 is arbitrary, (8), if proved, would imply the target.

This supplies terminal counting and a sufficient recurrence. It does
not establish (8), nor show that either the current low-Sigma separator
or the mixed branch has the needed coarse factor. Extra radius loss is
not hidden in (10): actual atom size is controlled by retained mass,
and (7) applies to arbitrary interval widths at the recorded rank.

## 7. Growing local configurations do not yet bypass compatibility

The established local-law theorem applies to every 4-uniform hypergraph
on m vertices whenever am<=1/3. Consequently m=C log(1/a) is still in
its feasible range for every fixed C and small enough a. The same is
true of m=C a^-theta for any fixed theta<1. Counting generators is not
counting vertices: an arithmetic cube with m generators may have 2^m
vertices, and the compatibility condition concerns that larger number.

This prevents a contradiction based solely on those local probability
constraints at logarithmically many vertices. It does not rule out
global PSD, deterministic resampling identities, or larger configurations.

For reference, the conditional endpoint mutual information at the exact
regular center, in natural logarithms, is

    I(a)=(1-2a)log(1-2a)-2(1-a)log(1-a)
        =sum_{k>=2}(2^k-2)a^k/[k(k-1)],  0<a<1/2.

It is of order a^2. The formula follows by substituting the three
nonzero probabilities (a,a,1-2a) into relative entropy against the
independent Bernoulli(a) law and expanding (1-t)log(1-t). Its values
cannot be added across overlapping fibers without another inequality;
the feasible joint laws already disprove any alleged contradiction
derived from such unsupported addition in their size range.

## 8. Status and the single remaining input

Finite checks in verify_localization.py cover 104 coordinate windows,
4,418 actual AP-free subsets, and 152 factor-energy atom cases. The
Z_13 and Z_101 low-cubic fixtures each have a signed-preserving partition
from quarter arcs in coordinates 1 and 3. This partition has 12 cells;
these are dependent harmonics, so it refines the resolution of one phase
rather than finding two independent directions. None of the tested
single-character four-arc partitions with offsets 0 or floor(p/4)
preserved the required half of the negative correlation. This is a
finite resolution diagnostic, not a lower bound on every partition and
not evidence of a uniform asymptotic compression theorem.

The useful new bridge is: signed correlation on a positive bounded
conditional expectation -> relative factor energy -> one polynomial-
mass atom; logarithmic added rank is sufficient for the terminal argument.
The single missing input for this completion route is (8), the uniform
coarse arithmetic energy lemma. It is OPEN, not a theorem obtained by
renaming a negative mixed statistic. All finite checks validate only
the proved bridges and hypotheses of tested instances.
