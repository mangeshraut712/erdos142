# Global regular-center compatibility: exact frontier

Date: 2026-09-07 (Asia/Kolkata). Offline continuation of the 6 September
checkpoint. Originals are preserved. The target is the local assertion
`r_4(N)=o(N/log N)`, not an asymptotic formula for all r_k.

STATUS: (E) OPEN — NO NEW THEOREM

Auxiliary propositions below are proved, but no research novelty, new
asymptotic bound, or closing density increment is claimed. The four
`frontier_audit_*.md` files contain the referee audits of the relative-window
checkpoint. One audit agent later hit a usage limit; its saved report and
returned calculations remain available. No paid API research runner was
started by this continuation.

## 1. Exact regular-center subtraction — PROVED

Let p>3 be prime, Omega nonempty, W=1_Omega, w=|Omega|/p,
A subset Omega, B=1_A, a=|A|/|Omega|, g=B-aW. All spatial and difference
averages in this section are normalized by p. Suppose A has no nontrivial
cyclic 4AP. For d!=0 put

    q_d = E_x W_0 B_1 B_2 W_3,
    t_L,d = E_x B_0 B_1 B_2 W_3,
    t_R,d = E_x W_0 B_1 B_2 B_3.

For active d define r_L,d=t_L,d/q_d and r_R,d=t_R,d/q_d. The endpoints
are exclusive conditional on the middle-pair event, so their joint table
is (P11,P10,P01,P00)=(0,r_L,r_R,1-r_L-r_R).

Let Phi=Lambda(W,B,B,W), Sigma=Lambda(B,B,B,W)=Lambda(W,B,B,B),
M=Lambda(g,B,B,g), and Q=Phi-aw/p. If Q>0 put mu(d)=q_d/(pQ) for d!=0.
The exact formula, with the exceptional diagonal separated, is

    M = aw(1-a)^2/p + Q[a^2-a E_mu(r_L+r_R)].                 (1)

Indeed, for d!=0 the endpoint product expands to
q_d[a^2-a(r_L+r_R)] because its joint term is zero. At d=0 the product
g B B g equals B(1-a)^2, whose spatial mean is aw(1-a)^2.
Also q_0=t_L,0=t_R,0=aw. Averaging these identities proves (1).

The exact conditional regular-center value is therefore

    M_reg = aw(1-a)^2/p-a^2 Q
          = -a^2 Phi + aw[(1-a)^2+a^2]/p.                    (2)

Subtracting gives

    M-M_reg = -a Q E_mu[(r_L-a)+(r_R-a)]
            = -2a[ Sigma-a Phi-a(1-a)w/p ].                 (3)

Thus subtracting the regular center removes the joint-exclusion budget,
but leaves an averaged cubic deviation. It does not itself detect the
variance of the fiber deviations or arithmetic alignment.

**Correction to the relative discussion in MIXED_INCREMENT.md.** Exact
r_L=r_R=a on nonzero fibers implies

    Sigma = a Phi+a(1-a)w/p,                                (4)

not Sigma=a Phi. The simultaneous equalities r_L=r_R=a,
Phi=a^2 C, Sigma=a^3 C omit this positive diagonal correction. Their
asymptotic interpretation is reasonable, but their exact conjunction is
FALSE for 0<a<1. The qualitative negative-budget conclusion survives:
if Phi=a^2 C and aw/p<=a^4 C/8, then (2) gives M_reg<=-7a^4 C/8.

## 2. Prime-cyclic exact equality is impossible — PROVED

In the full cyclic group write n=|A| with 1<=n<p, alpha=n/p, and

    k_d = |A intersect (A-d)|,
    ell_d = #{x: x,x+d,x+2d in A}.

For k_d>0, r_d=ell_d/k_d. Equality r_d=alpha would imply
p ell_d=n k_d. As gcd(n,p)=1, this would force p to divide k_d, impossible
when 0<k_d<=n<p. Therefore no active fiber of any proper nonempty prime
cyclic set has r_d exactly equal to its global density. AP-freeness is
not needed for this statement.

Consequently the proposed realization of **exact** global r_d=alpha on
an infinite prime-cyclic family is FALSE, not merely OPEN. The relevant
question is quantitative approximation, and the elementary gap is tiny:

    |r_d-alpha| = |p ell_d-n k_d|/(p k_d) >= 1/(p k_d).       (5)

For n>=2 define H=#{d!=0:k_d>0}, total Q_num=n(n-1), and

    V = sum_{d!=0} [k_d/(n(n-1))] (r_d-alpha)^2.

Then

    V = [p^2 n(n-1)]^{-1} sum_active (p ell_d-n k_d)^2/k_d
      >= H^2/[p^2 n^2(n-1)^2]
      >= 1/[p^2(n-1)^2].                                   (6)

Proof: every integer numerator in (5) is nonzero. Cauchy gives
sum_active 1/k_d >= H^2/sum k_d. Also sum_{d!=0}k_d=n(n-1).
For d!=0, k_d=n would make A invariant under a generator of Z_p, contrary
to 0<n<p. Thus k_d<=n-1 and H>=n. These facts prove (6).

At alpha=epsilon/log p, the last bound is only of order
(log p)^2/(epsilon^2 p^4). It is not the required density-power variance
bound, and no localization follows from it. This is not a successful
regular-center incompatibility theorem at the target scale.

In the same normalization, with T=Lambda_3(B)-alpha^3 and
Q_star=alpha^2-alpha/p, the exact mean relation is

    T-alpha(1-alpha)/p = Q_star(E_mu r_d-alpha).              (7)

It follows by adding the triple diagonal alpha/p to the nonzero triple
count Q_star E_mu r_d. Again, removing the center returns a cubic mean.

## 3. Overlapping finite configurations admit exact local laws — PROVED

The following proposition strengthens a single four-bit example. It is
still a statement about finite probability distributions, not an actual
set satisfying every cyclic exclusion.

**Proposition.** Let H be any 4-uniform hypergraph on m vertices. If
0<a<=1/(3m), there exists a joint Boolean law (X_v) such that, for every
S subset of the vertices,

    E product_{v in S} X_v = a^{|S|} if S contains no edge of H,
                           0 otherwise.                    (8)

In particular all marginals on at most three coordinates are independent
Bernoulli(a), every specified four-edge is absent almost surely, and an
edge's endpoints conditional on its two middle coordinates have
probabilities (0,a,a,1-2a). Arbitrary overlaps among the edges are allowed.

**Complete proof.** Call S independent if it contains no edge. Define
F(S)=a^{|S|} for independent S and F(S)=0 otherwise. Give the exact occupied
set T probability

    P(T) = sum_{U subset V\T} (-1)^{|U|} F(T union U).        (9)

If T is not independent, every summand is zero. If T is independent,

    P(T)/a^{|T|}
       = 1 + sum_{nonempty U, T union U independent} (-a)^{|U|}
       >= 1-sum_{k=1}^m binom(m,k)a^k
       >= 1-sum_{k=1}^infinity (ma)^k
       >= 1/2.

Here ma<=1/3. Hence every probability is nonnegative. For any S,
sum_{T containing S}P(T)=F(S): in (9), the coefficient of F(R) in this
sum is sum_{S subset T subset R}(-1)^{|R\T|}, equal to one for R=S and
zero otherwise. Taking S empty proves normalization, and the general
identity proves (8). If S is an edge, its product has expectation zero
and is nonnegative, so the exclusion holds almost surely. The conditional
endpoint assertions follow from the two-/three-point moments a^2,a^3
and the four-edge moment zero. This completes the proof.

The construction is consistent on overlapping subsets: restrictions have
the same prescribed occupancy moments, which uniquely determine each
finite Boolean law by (9). This is consistency of these local marginals,
not existence of a full law after the allowed scope becomes too large.

An explicit check uses the 4x4 integer grid, with all 10 four-term lines
(four horizontal, four vertical, two diagonal) forbidden. At a=1/64,
the integer Mobius transform checks all 65,536 assignments. It also checks
that a six-point union of two three-point rows containing no forbidden
edge has occupancy probability a^6. Thus this result is not obtained
merely by allowing at most three occupied coordinates in the entire grid.

**Precise limitation.** No contradiction can follow solely from the
finite joint-probability constraints that (8) satisfies. In particular,
the one-/two-/three-point data and all represented 4AP exclusions on a
fixed pattern do not contradict the regular-center model at small a.
This does NOT rule out a global incompatibility theorem, a pattern whose
size grows with 1/a, a global moment-matrix constraint, exact fixed-size
identities summed over all p points, or relations obtained by independently
resampling spatial variables conditional on one deterministic set.
Those additional constraints must be proved and included, not inferred
from a local probability table. This is not a claim about all SOS methods.

For comparison, the simpler hypergraph-independent law supported on at
most three occupied vertices has exact-set probabilities

    |T|=3: a^3;
    |T|=2: a^2-(m-2)a^3;
    |T|=1: a-(m-1)a^2+binom(m-1,2)a^3;
    |T|=0: 1-ma+binom(m,2)a^2-binom(m,3)a^3.

For m>=4 and 0<a<=1/(m-2), these are nonnegative. The singleton
polynomial has nonpositive discriminant; the empty probability decreases
on this interval, and at a=1/(m-2), writing r=m-2, it equals
(r-1)(r-2)/(3r^2)>=0. It has all three-point product marginals, but kills
every larger occupied subset; (8) avoids that unnecessary restriction.

## 3A. Fixed-size local marginals and a limited global extension — PROVED

There is a version of (8) that matches the exact fixed-size random model.
Let the full ground set have P vertices, intended size k, alpha=k/P, and
let H be any 4-uniform hypergraph on a distinguished m-vertex set V.
Assume alpha*m<=1/3. Put rho_j=(k)_j/(P)_j (zero if j>k), and prescribe

    F(S)=rho_{|S|} for independent S subset V, zero otherwise.

The same Mobius formula (9) defines a probability law. Indeed, for an
independent T of size t<=k,

    rho_{t+j}/rho_t=(k-t)_j/(P-t)_j <= alpha^j.

Thus the preceding geometric-series estimate proves P(T)>=rho_t/2;
for t>k every summand vanishes. Normalization and moment reconstruction
are unchanged. Every represented edge is absent. All one-, two-, and
three-coordinate occupied moments are exactly rho_1,rho_2,rho_3.
Conditional endpoint rates on a represented edge are consequently

    rho_3/rho_2=(k-2)/(P-2)
       =alpha-2(1-alpha)/(P-2),                              (8a)

when k>=3. Thus all such rates are within O(1/P) of the center while
every represented forbidden joint is zero.

If m<=k<=P-m, this local law even extends to a random subset of the whole
ground set having **exactly k points**: first choose its occupied set T
inside V using the law, then choose uniformly k-|T| points outside V.
All choices are possible under these size conditions. The full random
set has the exact fixed-size one-/two-/three-point occupied moments.
To see this, take r specified inside and s specified outside vertices
with r+s<=3. Its occupied probability is the expectation of

    1_{R subset T} (k-|T|)_s/(P-m)_s.

The numerator, as a Boolean polynomial in the inside coordinates, has
degree at most r+s. Its expectation therefore agrees with the uniform
k-subset law, because all inside moments of that degree agree. Under
that law the displayed occupied probability is rho_{r+s}.

**Scope:** this extension avoids the forbidden edges represented inside
V, not all arithmetic progressions on the full P-point ground set. Nor
does it identify averaging over this random ensemble with spatial
averaging over one deterministic set. Its purpose is to show that exact
cardinality plus a bounded pattern's exclusions and low-order marginals
are still insufficient. Any proof using the other p-point exclusions or
deterministic resampling relations needs those additional constraints.

## 4. Conditional covariance does not violate positivity — PROVED

At the exact regular center the endpoint covariance matrix is

    [[a(1-a), -a^2], [-a^2, a(1-a)]].

Its eigenvalues are a and a(1-2a). Both are nonnegative when 0<=a<=1/2.
Its determinant is a^2(1-2a), and the trace of its kth power is
a^k+[a(1-2a)]^k. Therefore a local covariance/Schur-positivity argument
does not contradict this table. A statistic subtracting this entire
baseline vanishes on the model by definition. The required resource is
a quantitatively useful global restriction on its realization.

## 5. Exact optimized endpoint bookkeeping — PROVED

Let a_j be increasing relative densities, mu_j the retained domain
fraction, and r_j=mu_j a_{j+1}/a_j the retained A-mass fraction. Assume
0<r_j<=1 and the joint gain-size guarantee

    mu_j(a_{j+1}-a_j)>=kappa a_j^2,                           (10)

with fixed kappa>0. Write u_j=1/a_j and delta_j=u_j-u_{j+1}. Exactly,

    r_j delta_j=mu_j(a_{j+1}-a_j)/a_j^2>=kappa,
    log(N_0/N_J)=log(a_J/a_0)+sum_j log(1/r_j).               (11)

Since log t<=t/e for all t>0 (maximize log(t)/t),

    log(N_0/N_J)
      <=log(a_J/a_0)+[1/(e kappa)](1/a_0-1/a_J).             (12)

The coefficient 1/e is sharp for this scalar information: choose
delta_j=e kappa, r_j=e^{-1},
a_{j+1}=a_j/(1-e kappa a_j), and
mu_j=e^{-1}(1-e kappa a_j), while denominators are positive. Then (10)
and every bound leading to (12) are equalities. This is an admissible
numerical path, not a constructed sequence of sets or windows.

At a_0=epsilon/log N_0, this path costs
log N_0/(e kappa epsilon)+O(log log N_0) to reach a fixed density.
Thus the joint inequality alone cannot guarantee o(log N_0) cost.
With rank-dependent kappa_j, the valid bound is instead

    log(N_0/N_J)<=log(a_J/a_0)+sum_j delta_j/(e kappa_j);       (13)

one cannot replace kappa_j by an initial fixed constant.

This does NOT say all alpha^2 increments are insufficient. If one had
the additional mass guarantee r_j>=exp(-K a_j), together with
a_{j+1}>=a_j+kappa a_j^2 and densities <=1, then

    log(a_{j+1}/a_j)>=log(1+kappa a_j)
       >= kappa a_j/(1+kappa).

Summing gives sum a_j <=(1+kappa)/kappa log(a_J/a_0), hence

    log(N_0/N_J)
       <=[1+K(1+kappa)/kappa]log(a_J/a_0).                   (14)

This is O(log log N_0) at the target starting density. The conditional
calculation is PROVED; the needed hereditary arithmetic mass-retention
theorem is OPEN. The earlier affine-spreading construction already makes
its universal true-integer-progression version FALSE.

## 6. What the referee audit establishes

The relative-window theorem (12)-(15) is PROVED with d>=1, 0<a<1,
and its stated local-size and Fourier-algebra-norm hypotheses. The mixed
constant actually supplied by its proof is 9/16. The interval smoothing
constant 96 can be improved to 64 without changing the exponent. These
constant improvements do not repair iteration.

The exact random baselines distinguish Bernoulli parameter a from an
exact-size sample. In particular, with R=C-w/p, Bernoulli expectations
are E Phi=a^2 R+aw/p and E Sigma=a^3 R+aw/p. For fixed size k=an they
are rho_2 R+aw/p and rho_3 R+aw/p, rho_j=(k)_j/(n)_j. Both are PROVED
by counting distinct positions. The operator, frame, high-signal, clipping,
and geometric identities are detailed in the four saved audit files.

Important scope corrections:

- Relative equation (22)'s ratio requires d!=0 and q_d>0.
- The p=31 interval counterexample of diameter 14 is outside the narrow
  p/3 class; the same example at p=43 is inside it.
- High-signal prime-first reduction concerns the globally balanced cyclic
  signal, not an arbitrary window-relative coefficient.
- Small deletion preserves AP availability only relative to that
  availability; absolute smallness is insufficient when it is tiny.
- The large-interval no_coarse_gain flag checks a fixed partition. Its
  even-number example has a density-one step-two progression and is not
  AP-free. It is not a universal cheap-increment obstruction.
- MIXED_INCREMENT.md treats a guaranteed eigenmode lower bound of order
  a^5 as though it were an upper bound and refers to Bohr conversion of
  an arbitrary eigenmode. Neither inference is supplied by the checkpoint.
  The correct conclusion is that the available bounded-mode guarantee
  is too weak and gives no arithmetic domain; it is not a universal upper
  bound on what every spectral argument can obtain.
- An intersection (A-d) intersect (A-2d) is not generally a controlled
  bounded-rank window. This does not mean it can never be such a window:
  accidental examples and high-complexity representations are possible.

## 7. Verification and live frontier

Run `python3 verify_compatibility.py`. The captured output is
`compatibility_verification.json`. It checks 21 local laws, every occupancy
moment on the 16-point grid, 2,179 proper prime-group subsets with active
fibers, 219 relative-center identities, and exact scalar recurrences.
It includes the Z_101 28-point set, whose weighted fiber variance is
17181266911/1389540232080. It also checks the small-window spectral family
from frontier_audit_operator.md. All these new checks use exact integers
and rational arithmetic. They corroborate the proofs; they are not an
asymptotic proof or evidence that the model is globally realizable.

No closing increment has been obtained. A useful next theorem must use
global arithmetic compatibility beyond the feasible finite laws, or change
the cubic cost/mass tradeoff. Positivity of a local table, another identity,
or a variance gap with p in its denominator cannot be substituted for that
theorem. The research continuation has not proved or disproved the target.
