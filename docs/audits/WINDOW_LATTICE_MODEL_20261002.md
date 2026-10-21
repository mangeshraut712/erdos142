# Controlled windows are convex lattice sets; the 3^r cutoff is sharp

2 October 2026. **(D) NEW RIGOROUS PARTIAL THEOREM (structural).**
The target r_4(N)=o(N/log N) is neither proved nor disproved. The window
energy lemma of AP_RICHNESS_COUNTEREXAMPLE.md section 8 remains OPEN.
Novelty of these elementary lemmas is not claimed.

A controlled window of rank r is
Omega={x in Z_p : xi_j x mod p in I_j, 0<=j<r}, with xi_j nonzero and
each I_j=[b_j,b_j+l_j] an integer interval of diameter l_j<p/3. As in the
checkpoint, one coordinate may be x itself (xi_0=1). Write n=|Omega|.

## 1. The lattice model — PROVED

For x in Omega let y_j(x) be the unique integer in I_j congruent to
xi_j x, and v(x)=(y_0,...,y_(r-1)) in Z^r.

**Lemma 1.** v is injective, and x_0,...,x_(k-1) in Omega form a k-AP in
Z_p (k>=3) iff v(x_0),...,v(x_(k-1)) form a k-AP in Z^r. Nontrivial
progressions correspond to nontrivial ones.

Proof: injectivity uses xi_0 invertible. If x_i=x_0+ih, consecutive lifted
gaps lie in (-p/3,p/3) and are all congruent to xi_j h; two such gaps
differ by less than 2p/3<p, so they are equal. Conversely an integer AP of
lifts gives xi_0 x_i congruent to y_0+i w_0, hence an AP in Z_p. If the
lifted difference is zero, xi_0 h=0, so h=0.

The image is v(Omega)=Gamma intersect B, where B=I_0 x ... x I_(r-1) and
Gamma={y in Z^r : y_j = xi_j x mod p for some x} is a lattice of index
p^(r-1). Choosing a basis Gamma=M Z^r, the map u=M^(-1)v(x) identifies
Omega, together with all its progressions, with X=Z^r intersect K for the
parallelepiped K=M^(-1)B. Character coordinates become linear forms in u,
so quarter-arc cells of coordinate characters are slabs of K.

The binary cube of UNIFORM_ENERGY_COUNTEREXAMPLE.md is X={0,1}^d, and the
window of AP_RICHNESS_COUNTEREXAMPLE.md is a cube joined to a segment.

## 2. Exact 4-AP threshold for convex lattice sets — PROVED

**Lemma 2.** Let K be convex and X=Z^r intersect K.

1. If |X|>3^r, X contains a nontrivial 4-AP.
2. X={0,1,2}^r has |X|=3^r and no nontrivial 4-AP (it does contain 3-APs).

Proof: (1) two points u!=u' agree mod 3; with w=(u'-u)/3 in Z^r, the
points u+w, u+2w are convex combinations in K and lattice points, so
u,u+w,u+2w,u' is a 4-AP in X. (2) a nonconstant coordinate of a 4-AP takes
four distinct values, impossible in {0,1,2}.

Since det M=p^(r-1) is prime to 3, u congruent to u' mod 3 is equivalent
to coordinatewise congruence of the lifts. Thus (1) is the label-class
argument of AP_RICHNESS_COUNTEREXAMPLE.md section 8, now with the matching
lower construction.

## 3. A whole window with no 4-AP — PROVED

For d>=1 put D=8^d, let p be a prime exceeding 100D^2, and
xi_j=ceil(p/8^j). Define Omega by 0<=x<=D-1 and
0<=(xi_j x mod p)<=floor(37p/112), j=1,...,d. Then

    Omega={sum_{i<d} eps_i 8^i : eps_i in {0,1,2}},  n=3^d=3^(r-1),

with rank r=d+1, and Omega has no nontrivial 4-AP in Z_p.

Proof: as in UNIFORM_ENERGY_COUNTEREXAMPLE.md (3), xi_j x/p=x/8^j+e with
0<=e<1/(100D). If lower digits lie in {0,1,2}, their fractional
contribution is at most sum_{i>=2}2/8^i=1/28. Digit v_(j-1) in {0,1,2}
gives fractional part at most 1/4+1/28+e<37/112; v_(j-1)>=3 gives at least
3/8>37/112 and at most 7/8+1/28+e<1, so no wrap. Induction on j gives the
digit description; 37/112<1/3 keeps the window narrow. All points lie in
[0,D), p>2D, so modular APs are integer APs; adding base-8 digits in
{0,1,2} three times creates no carry, so Lemma 2(2) applies digitwise.

**Consequence (sharpness of the cutoff).** Any guarantee that a rank-r
window contains a nontrivial 4-AP must require n>3^(r-1); Lemma 2 shows
n>3^r suffices. In particular A=Omega is 4-AP-free of relative density
one, and any subset of density a<=1/2 is a 4-AP-free set in a window with
no ambient progressions at all. So the 3^r factor in the checkpoint cutoff
n>=8*3^r*a^(-3) cannot be removed or replaced by c*3^r with c<1/3. Whether
the a^(-3) factor can be weakened is not decided here.

## 4. Sharp endpoint supply inside A — PROVED

**Lemma 3.** For any A in X=Z^r intersect K, the number of ordered pairs
(u,u') of distinct A-points with u congruent to u' mod 3 is at least
|A|^2/3^r-|A|, and each such pair is the endpoint pair of a 4-AP of X
(Lemma 2 proof). The bound is attained (equal class sizes).

Under the cutoff n>=8*3^r*a^(-3), with |A|=an, this is at least
|A|(8a^(-2)-1) endpoint pairs, so on average each point of A is an
endpoint of at least 8a^(-2)-1 progressions whose middle points lie in
Omega. If A is 4-AP-free, every one of these progressions has a middle
point in Omega minus A. This averaged statement sharpens the half-of-A
count in AP_RICHNESS_COUNTEREXAMPLE.md section 8 (at least 4a^(-2)-1 for
half of A) and is sharp as a pair count. As noted there, it concerns
middles in Omega, not in A; no energy increment follows yet.

## 5. What changes for the program

1. The window energy lemma is now a statement about 4-AP-free subsets of
   convex lattice sets X in Z^r of size >=8*3^r*a^(-3), with factors given
   by quarter arcs of linear forms mod p. Counterexample searches can be
   run directly on lattice sets, without building primes and CRT windows.
2. The 3^r part of the cutoff is forced (Section 3); constructions that
   evade it, such as the two existing counterexamples, are exactly the
   near-cube cases n<=3^(r-1)-ish.
3. The missing-middle structure of Lemma 3 is the natural input for the
   endpoint-incidence route (ENDPOINT_INCIDENCE_AUDIT.md): each mod-3 class
   of A sends its endpoint pairs to middles in other classes, and
   4-AP-freeness forbids both middles lying in A.

Update: the class-only alternative below is refuted in
MOD3_INCREMENT_20261002.md (three far-apart translates are 4-AP-free and
exactly balanced mod 3); slabs must be allowed.

Next precise step (as first proposed): in the lattice model, decide whether 4-AP-free A of
relative density a in X with |X|>=8*3^r*a^(-3) must have a mod-3 class,
or a slab of one linear form, carrying relative density >=(1+c)a. A
density increment on a mod-3 class is itself a controlled window of the
same rank: it is the image of Z^r intersect (K-c)/3 under u -> 3u+c, which
in Z_p is t -> x_c+3t applied to a rank-r window with intervals shrunk by a
factor 3. That affine map preserves 4-APs, so such an increment would be
hereditary, at a cost of 3^r in size per step.

## 6. Checks

`python3 verify_window_lattice_20261002.py` (about 5 seconds, integers only):
40 random windows with exact equality of modular and lattice 3-AP and 4-AP
counts; {0,1,2}^r for r<=3 has no 4-AP but has 3-APs; 208 random sheared
convex lattice sets with more than 3^r points all contain a 4-AP; the
digit windows for d=2..5 equal {0,1,2}-digit sets of size 3^d at rank d+1
with zero nontrivial 4-APs and positive 3-AP counts; Lemma 3 holds in 200
random trials with minimum slack exactly 0 (attained). Output:
window_lattice_verification_20261002.json.
