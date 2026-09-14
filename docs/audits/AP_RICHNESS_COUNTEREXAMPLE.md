<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Total AP mass and many AP directions do not force relative energy

Date: 2026-09-14. Offline continuation. No claim of literature novelty.

(D) NEW RIGOROUS PARTIAL THEOREM

The new theorem is a counterexample to proposed sufficient AP-richness
conditions, not to r_4(N)=o(N/log N). The full checkpoint rank/size cutoff
is not refuted. The target remains OPEN.

## 1. The theorem

There are deterministic prime-cyclic controlled windows Omega_d and actual
3AP-free subsets A_d, with n_d=|Omega_d| and a_d=|A_d|/n_d, such that

    a_d log p_d -> log 2,
    a_d^3 n_d beta_d -> infinity,

where beta_d=Lambda_4(1_Omega)/(n_d/p_d)^2. Nevertheless, for every fixed
C and fixed equal-arc count b>=2,

    sup_{rank(F)<=C log(2/a_d)} Var_Omega(E(1_A|F))/a_d^2 ->0. (1)

Every factor in (1) uses b shifted equal arcs on each selected character.
All its harmonics are included. For the ambient nonzero-difference AP law,
the effective support grows faster than every fixed power of 1/a_d, and
its entropy divided by log(1/a_d) tends to infinity. These additional
density-only spread tests still do not force the energy conclusion.

All nontrivial ambient APs occur in a small arithmetic progression P_d
disjoint from A_d. A controlled refinement retaining every point of A_d
and a 1-o(1) fraction of Omega_d removes all nontrivial ambient APs.

## 2. Parameters and CRT coordinates

Take integers d>=256 and put

    S=2^d, L=2^ceil(d/2) d^8, Q_0=16L+1, F=d!,
    Q_i=1+Q_0 F i (1<=i<=d), R=product_{i=1}^d Q_i,
    M=Q_0 R.

These moduli are pairwise coprime. Q_i is coprime to Q_0 F. A common
divisor of Q_i and Q_j therefore divides j-i, which divides F, so it is
one. Also R=1 modulo Q_0.

Let p be the least prime greater than 100 M Q_d. By the checkpoint's
prime-existence result,

    100 M Q_d <p<200 M Q_d.                                 (2)

Represent CRT vectors by their unique integer x in [0,M-1]. Let C be the
binary cube with residue x mod Q_0=0 and x mod Q_i in {0,1}, 1<=i<=d.
Let U=C\{0}, so |U|=S-1. Define

    P={Rz:0<=z<=L},   Omega=U disjoint-union P.

The formula for P follows because R=1 mod Q_0 and R=0 mod Q_i, while
Rz<M. Consequently |Omega|=n=S+L.

## 3. Omega is a controlled narrow window — PROVED

The following are all single intervals in linear character coordinates:

1. x lies in [0,M-1].
2. For gamma_0=ceil(p/Q_0), the residue gamma_0 x mod p is at most
   floor(p(L+1/2)/Q_0).
3. For gamma_i=ceil(p/Q_i), i>=1, its residue is at most
   floor(3p/(2Q_i)).
4. Put H_i=LFi+1. For lambda_i=ceil(p(H_i/Q_i+1/Q_0)), its residue is
   at most floor(p[H_i/Q_i+1/(4Q_0)]).

All lower endpoints are zero. These 2d+2 constraints define exactly Omega,
and all interval diameters are below p/3.

Here is the detailed rounding argument. For any rational theta in these
formulas, x ceil(p theta)/p=x theta+e, with 0<=e<M/p<1/(100Q_d).
For the separate residue constraints this error is less than 1/(100Q_i).
It cannot wrap residue Q_i-1 past one, and it is smaller than the half-
residue margins. Conditions 2 and 3 therefore select exactly

    z=x mod Q_0 in {0,...,L},  epsilon_i=x mod Q_i in {0,1}.

For condition 4 the fractional contribution is
H_i epsilon_i/Q_i+z/Q_0, without wrap. Indeed this is below 1/8+1/Q_0.
The exact relation

    H_i/Q_i-L/Q_0=(Q_0-L)/(Q_0 Q_i)>0

shows that the threshold allows epsilon_i=0 with every z<=L, and allows
epsilon_i=1 when z=0. If epsilon_i=1 and z>=1 it exceeds the threshold
by at least 3/(4Q_0). The rounding error is smaller than every stated
margin. Hence z>0 forces all epsilon_i=0, while z=0 permits the whole
binary cube. This is Omega. Each threshold is below p/3, and all
frequencies lie strictly between 0 and p; the first interval is narrow
by (2). Thus the rank is at most r=2d+2.

## 4. Every nontrivial ambient AP lies in P — PROVED

All representatives lie in [0,M-1] and p>2M, so a modular AP has zero
integer second differences. Reduce those equations modulo Q_i, i>=1.
The residues are binary and Q_i>2, forcing each binary coordinate to be
constant along the progression. If any coordinate equals one, every
point must have z=0 and all CRT coordinates coincide. The progression
is then trivial. Therefore every nontrivial three- or four-term AP lies
in P. In particular every subset of U is 3AP-free, hence 4AP-free.

Writing N=L+1, the total ordered ambient 4AP count, including diagonals, is

    Q=ceil(N^2/3)+(S-1),
    Lambda_4(1_Omega)=Q/p^2,   beta=Q/n^2.                  (3)

The first term counts APs in the ordinary N-point progression P; each
of the other S-1 points contributes only its diagonal. The formula for
an interval follows directly from N+2 sum_{e=1}^{floor((N-1)/3)}(N-3e).

## 5. Density and scalar AP richness

Let h=ceil(log_2 p), k=floor(n/h), and a=k/n. For the parameters above,

    L=o(S), n<=2S,  h<=d^3,
    n/(2h)<=k<=S-1                                         (4)

for d>=256. To verify the bounds without a hidden dependence on p:
L/S=2^{-floor(d/2)}d^8 tends to zero and is already below 1/2 at d=256;
the envelope sqrt(2)d^8 2^{-d/2} decreases thereafter.
Also log L<=d: at d=256, 8log d<d/4, and its derivative is at most 1/4
thereafter, while ceil(d/2)log2<=d/2+1/2. Hence log Q_0<=2d and
log Q_i<=d log d+3d. Formula (2) gives

    log p<=3d^2 log d,
    h<=7d^2 log d<=d^3.

We used 1/2<=log2<1; the last inequality holds at 256 and persists by
differentiation. Since n>=2^d>=2d^3, the lower bound on k follows from
flooring. Since h>=d^2/2, n<=2S and S is large, k<=S-1. These prove (4).

Therefore a log p ->log2, since log p/n ->0. Moreover, (3)-(4) imply

    a^3 n beta=a^3 Q/n
      >= L^2/(48h^3 S) >=d^7/48 ->infinity.                 (5)

Thus the proposed scalar AP-richness condition holds by an arbitrarily
large margin, not merely at its endpoint.

## 6. Deterministic subsets invisible to every small factor

Let s=floor(sqrt(d)). As in the preceding counterexample, all factors
using at most s characters and any equal-arc count 2<=b<=d form a finite
family. All shifts are represented by t/(2bp); the number of pairs of a
factor and one of its nonempty cells is at most

    T_d=d(s+1)(2d^2 p^2)^s.                                (6)

Sample only U, independently with probability b_0=k/u, where u=|U|=S-1.
No point of P is sampled. For any cell V, its random count Z_V has mean
b_0 |V intersect U|. For a centered Bernoulli variable, the logarithm of
its exponential moment and its first derivative vanish at zero, and its
second derivative is a tilted Bernoulli variance, at most 1/4. Integrating
twice gives log E exp(t(X-b_0))<=t^2/8. Independence and exponential
Markov, optimized at t=4v/N, give the two-sided tail 2exp(-2v^2/N) for a
sum of N such variables. Consequently

    Pr(|Z_V-b_0|V intersect U||>4d^2 sqrt(|V intersect U|))
       <=2 exp(-32d^4).

Cells disjoint from U have zero discrepancy. Because log p<=d^3,
log T_d<=6d^4 and log(4(u+1))<=d^4. Thus the probability that any cell
fails is below 1/[2(u+1)]. The total sample count is Binomial(u,k/u),
whose mode k has probability at least 1/(u+1). There exists a k-point
subset of U satisfying every discrepancy inequality simultaneously.

Define A_d as the lexicographically first such subset, using the integer
tests

    (u |A_d intersect V|-k |V intersect U|)^2
       <=16d^4 u^2 |V intersect U|                          (7)

for all the finitely many cells. This is a terminating deterministic
integer-search definition, supported by the probability proof. Its
enormous asymptotic output is not claimed to have been generated.

To calculate energy, write on Omega

    1_A-a=(1_A-b_0 1_U)+(b_0 1_U-a)=Z+m_0.

Both terms have mean zero after fixing |A|=k. For any selected factor,
(7) gives ||E(Z|F)||_2^2<=16d^4 d^s/n. Also

    ||m_0||_2^2=a^2(n-u)/u=a^2(L+1)/(S-1).

Conditional expectation is an L2 contraction, and ||v+w||_2^2 is at
most 2||v||_2^2+2||w||_2^2. It follows that

    Var_Omega(E(1_A|F))/a^2
      <=128d^10 d^s/2^d+2(L+1)/(2^d-1) ->0.                (8)

For every fixed C, C log(2/a)<=C log(4d^3)<=s eventually. Every fixed
arc count b is also eventually <=d. Equation (8) therefore proves (1)
uniformly for every factor in the claimed logarithmic-rank family.
This argument counts the factors themselves, including their harmonics,
and does not mistake character count for Fourier-term count.

## 7. Direction distribution and vertex concentration

Use C_h=E_x product_{j=0}^3 W(x+jh). The normalized 4AP average is
Lambda_4(W)=p^{-1} sum_h C_h; it is not the unnormalized sum.
For h!=0, the only active differences are h=Re modulo p with
1<=|e|<=floor(L/3), and

    C_{Re}=(L+1-3|e|)/p.

Let nu(h)=C_h/sum_{t!=0}C_t. Exact arithmetic sums give

    support_eff(nu)
      =[2 sum_{e=1}^{floor(L/3)}(L+1-3e)]^2
       /[2 sum_{e=1}^{floor(L/3)}(L+1-3e)^2]
      =L/2+O(1).                                         (9)

The leading terms are L^2/3 in the first bracket and 2L^3/9 in the
denominator. Alternatively, elementary bounds suffice: for L>=12,
L/24<=support_eff(nu)<=2L/3. The lower bound uses sum c_e>=L^2/12 and
max c_e<=2L; the upper bound is the number of active differences.

Thus H_2(nu)=log L+O(1), and the Shannon entropy lies between H_2(nu)
and log(2L/3), also log L+O(1). Since 1/a<=2d^3 and L grows exponentially
in d, the effective support exceeds every fixed power of 1/a eventually.
However support_eff(nu)/n ->0. All these APs visit P, which has size
L+1=o(n), and A is disjoint from P.

The controlled refinement C obtained by imposing z=0 retains every point
of A and S/n=1-o(1) of the ambient window. It has no nontrivial APs. It is
a same-coordinate refinement: replace the z-coordinate upper endpoint
by floor(p/(2Q_0)). Thus neither retained A-mass nor small *measure*
loss alone preserves AP availability. Its coordinate-width shrink is
large; this is not a counterexample to an additional radius-loss bound.

For these sets Phi=Sigma=k/p^2, because any ambient nontrivial AP has
middle points in P. Hence Phi/(a^2 Lambda_4(W)) tends to zero. The
counterexample is not a stable-Phi mixed instance. It specifically
refutes deriving coarse energy from total AP mass and density-only
direction-spread conditions without further rank or spatial assumptions.

The entropy comparisons used here follow directly from Jensen:
E_nu[-log nu]>=-log E_nu[nu], and
E_nu[log(1/nu)]<=log E_nu[1/nu]=log|support(nu)|.

## 8. Scope, heredity, and remaining lemma

The full old rank/size cutoff fails for every representation in the narrow
window class, not only the displayed rank 2d+2. For any representation
of rank r, label a point by its r integer coordinate lifts modulo 3.
Two different points with the same label have integer convex one-third
and two-third averages inside each coordinate interval. Modulo p these
are the two middle points of their endpoint 4AP, so that AP lies in Omega.
Every point of U lies on no nontrivial ambient AP, hence has a singleton
label class. Thus 3^r>=|U|=S-1. As n/(S-1)->1, neither
n>=256r3^r nor n>=8*3^r*a^-3 can hold.
The construction also does not have global density comparable to
1/log p: |A|/p=a n/p is much smaller. It is not a disproof of r_4(N).

The appropriate hereditary bookkeeping includes AP mass loss. For any
Omega' subset Omega deleting r n points, the total nonzero-difference
mass S_AP=sum_{h!=0}C_h satisfies

    0<=S_AP-S_AP'<=4r n(n-1)/p.                            (10)

Indeed each deleted point, at each of four progression positions, can
belong to at most n-1 nontrivial APs: choose a fixed other position,
which uniquely determines the difference in the prime group. Overcounting
only enlarges this bound. If S_AP'>=(1-epsilon)S_AP, entrywise C'_h<=C_h
also gives

    support_eff(nu') >=(1-epsilon)^2 support_eff(nu).

This is a conditional stability statement. The present same-rank
refinement has S_AP'=0 despite retaining all A-mass, so its premise is
not automatic. For a general window S_AP=w(n beta-1), and C_h<=w implies
support_eff(nu)>=n beta-1 whenever S_AP>0. This explains why total
richness already forces some direction spread, but not the needed
spatial overlap with A.

The full rank/size cutoff does impose spatial participation missing from
this example. In any controlled rank-r window, at most 3^r label classes
exist. Classes of size below an/(2*3^r) contain fewer than an/2 points
in total. Hence at least half of A lies in classes of size at least
an/(2*3^r). Each such point is an endpoint of at least
an/(2*3^r)-1 distinct nontrivial ambient APs, one for every other point
of its class. If n>=8*3^r*a^-3, this is at least 4a^-2-1. This counts
APs in Omega, not APs whose other three points lie in A; no energy
increment follows without that further information.

**ONE REMAINING THEOREM — OPEN:** the uniform coarse arithmetic energy
lemma on the full checkpoint-qualified controlled windows, with the
explicit rank/size cutoff and constants uniform through the corrected
iteration of LOCALIZATION_BRIDGE.md. Total AP mass and polynomial-in-1/a
direction spread cannot replace those hypotheses on their own. The
corrected iteration remains a conditional proof, not an unconditional one.

## 9. Next research prompt

Continue offline from AP_RICHNESS_COUNTEREXAMPLE.md and LOCALIZATION_BRIDGE.md.
Accept that total AP richness can diverge and effective difference support
can exceed every polynomial in 1/a while all nontrivial ambient APs avoid
A. Do not infer energy or heredity from those quantities alone. Attack the
uniform coarse arithmetic energy lemma with its full checkpoint rank/size
cutoff, testing both AP participation of A-occupied points and quantitative
factor complexity. Retain C_h normalization and AP-mass loss under
refinement. Cover the near-regular-center case as well as low Sigma and
corrected mixed deficits. If a uniform energy theorem is obtained, execute
the already-proved atom retention, logarithmic-rank recurrence, terminal
bound, and interval transfer. Otherwise preserve one exact unproved
statement; do not report a solution or literature novelty from this
counterexample or from finite checks.

## 10. Finite verification

Run `python3 verification/scripts/verify_ap_richness.py`. The recorded JSON is
`verification/results/ap_richness_verification.json`. It exhaustively checks the defining
coordinate inequalities on CRT ranges of 955,647 and 4,290,975 integers
for two small geometry instances, verifies that all nontrivial APs are on
the progression component, and checks 140 exact factor-energy/profile
cases. Four rational asymptotic-bound evaluations are also recorded.
The small instances are geometry tests, not instances of the large-d
asymptotic estimates. The deterministic asymptotic A_d are defined by (7)
and proved to exist; their enormous lists were not generated. All test
arithmetic uses integers and fractions. The original target remains OPEN.
