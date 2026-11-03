# All-host-pair lift and audit of the low-mean transfer

3 November 2026. Classification D: rigorous partial theorem. The local
target remains unproved. Authorship of the research pack remains Mangesh Raut.
This note supersedes the unsupported GU24 transfer claims, not the October 21
withdrawal. No literature novelty is asserted.

## 1. Exact setting and the occupied-domain obstruction

Use p>3 prime, a nonempty host Omega, P=1_Omega, A subset Omega,
B=1_A, w=|Omega|/p, 0<a=|A|/|Omega|<1, u=B-aP and U=wa(1-a).
Use the original mixed-host tent F; the identities below in fact hold for
every 0<=F<=1 with F(x,0)=1. Every restricted average retains denominator p
or p^2. Write R_j*=R_j restricted to h!=0, using the definitions in
[LM23](LOW_MEAN_MOMENT_CONE_20261023.md).

The original K has columns only in binom(A,2). Thus B(r)B(s)-a^2P(r)P(s)
equals 1-a^2 on each column and u(r)u(s) equals (1-a)^2. K applied to either
is only a constant multiple of K1=3q. Its range is supported on holes when
A is AP-free. Its bounded-input ceiling does not exclude every possible
rescaled or different-operator proof architecture.

## 2. AP27: a B-independent lift

Let I={0,1,2,3}. Define L on unordered distinct pairs of Omega by

    (Lf)(v) = (1/p) sum_(h!=0,j in I) F(v-jh,h)
                 product_(ell in I) P(v+(ell-j)h)
                 sum_({i,k} subset I\{j}) f({v+(i-j)h,v+(k-j)h}).

L depends on the host and F, but not on B. The original K is NOT merely
its occupied-column restriction: the remaining third vertex must also be
occupied. Define L_B by inserting B(v+(ell-j)h) in each summand, where
ell is the unique fourth slot outside {j,i,k}. Then K is L_B restricted
to occupied columns for AP-free A. L_B on all pairs is NOT zero extension
of K. Its other columns need not vanish.

Set f_uu({r,s})=u(r)u(s), c_2({r,s})=B(r)B(s)-a^2P(r)P(s).
The following identities hold even without AP exclusion:

    E_p L f_uu       = 2R2*/a^2,
    E_p [u L f_uu]   = 3R3*/a,
    E_p L c_2        = 2(3R1*+R2*)/a^2,
    E_p [u L c_2]    = (4R2*+3R3*)/a.                 (AP1)

Proof. Change variables v=x+jh. A pair occurs for two choices of j; a
triple with one distinguished row occurs for three choices. Expand
c_2=a(u_i P_k+P_i u_k)+u_i u_k. Each linear term has multiplicity six
in the mean; each quadratic term has multiplicity four in the u-pairing.
These counts give AP1 directly, with the original weighted host product.

In terms of unstarred residuals the four right sides must respectively
subtract 12U/p, 12(1-2a)U/p, 12U/p, and 12U/p. This follows from
R1_diag=0, R2_diag=6a^2U/p and R3_diag=4a(1-2a)U/p.

Row sums are at most 12: four anchors and three pairs, each direction
average at most one. Column sums are at most 24/p: place the two fixed
vertices into ordered distinct slots (12 choices), then choose either
remaining anchor (2 choices). Each placement determines x,h uniquely.
Weighted Cauchy-Schwarz therefore proves, for counting Euclidean norms,

    ||L||_(2->2)^2 <= 288/p.                          (AP2)

This is an upper bound only. It is weaker in density than the original K
bound, and carries no phase concentration conclusion.

The candidate pair inputs are not exactly centered on distinct host pairs.
If n=|Omega|>1 and k=|A|, their uniform pair means both equal
-a(1-a)/(n-1). Subtract this mean if exact pair centering is required;
then AP1 acquires the corresponding multiple of L1. Their counting norms are

    ||f_uu||_2^2 = ((pU)^2-sum_v u(v)^4)/2,
    ||c_2||_2^2 = binom(k,2)(1-a^2)^2
                  + (binom(n,2)-binom(k,2))a^4.       (AP3)

These follow by expanding the square of sum u^2, and by splitting occupied
and other pairs. The factor here remains the trivial factor g=aP.

## 3. Exact phase form and the missing estimate

With counting complex inner products, <psi,Lf>=<L*psi,f>, where

    <psi,Lf> = (1/p) sum_(x,h!=0) F product P_i
                  sum_j conjugate(psi(x+jh)) sum_({i,k} subset I\{j}) f_ik.

For a fixed ordering (r,s) of a column and slots i!=k, put
h=(s-r)/(k-i), x=r-ih and theta=(j-i)/(k-i). The adjoint is the sum of
the 24 terms F(x,h) product P_i psi((1-theta)r+theta s)/p.
For psi(v)=e_p(cv^2+tv), the phase has cross coefficient
2c theta(1-theta) multiplying rs. For c!=0 this is nonzero since j differs
from i and k. Thus even a single unweighted placement is not a product
of two one-variable chirps. On the full Cartesian domain its matrix is
diagonal unitary factors times e_p(lambda rs), which has rank p by
character orthogonality. This statement about one placement does not
establish the rank of the weighted sum or its restriction to a host.

Failed one-variable selection does not by itself bound this weighted
two-variable expression. A uniform decomposition or arithmetic cancellation
estimate for it is still missing; no automatic diagonalization is used.

## 4. Full residual and low mean

For AP-free A the exact identities give

    R3+R4 = aw/p-a^4T-R1-R2,
    R4 = 3a^4T+2R1+R2-awm+aw(1-4a)/p.               (AP4)

AP1 recovers R3*, but AP4 shows why simply substituting it into the full
residual leaves the original counting obstruction. No signed lower bound
has been obtained. In occupancy moments, R3+R4=M4-a^2M2+2a^3M1-3a^4T;
M3 cancels exactly. Completion mass alone cannot be substituted for this.

A precise corrected low-mean consequence is: if |R1|<=E1, R2>=-E2 and
m<=2a^3T/w, then

    R4 >= a^4T-2E1-E2+aw(1-4a)/p.                 (AP5)

For m=0 replace the leading coefficient 1 by 3. This retains the diagonal
and only needs the one-sided bound for R2. The coefficient 5/2 asserted for
the entire low-mean interval in GU24 does not follow. The LM23 abstract
law with M3=2a^3, R1=R2=0, T=1 gives R4=a^4, demonstrating the exact
algebraic deficit; it is not an eligible arithmetic counterexample.

GU24's arbitrary-kernel Gowers step has no proved uniform multiplier
bound; its finite tests do not prove it. Even assuming such a bound,
one must retain (T/C_F)^(1/4) in a norm lower bound and w in converting
global to relative correlations. The claimed universal inverse exponent
barrier is unsupported. The valid derivative Fourier identity alone
repairs none of these missing steps. No U3 transfer theorem is claimed here.

## 5. Exact remaining task and dependency graph

On the original eligible mixed-host domain
r[log(1/w)+log(48r)+loglog p]<=log p/100, r>=1,
epsilon/(2log|Omega|)<=a<=4/5, define

    delta=max_(c,t)!=(0,0) |E_Omega (B-a)e_p(-cx^2-tx)|.

Prove delta>=c_epsilon a^(3/2)F_epsilon(a), uniformly with
F_epsilon(a)->infinity, or prove under failed adequate selection

    R3+R4 >= -a^4wmu/2.                              (P12)

The low-mean branch m<=2a^3T/w remains open. All original erosion and
weight-loss terms remain in force; AP1 does not bound them.

    AP1 / phase adjoint -> OPEN uniform phase-transfer estimate
    P12 or DIRECT-Q-GAIN -> conditional increment ledger
                         -> reachable terminal contradiction -> local target

Next attempt: analyze the 24 placement expressions with the positive
Fourier expansion of the original F, keeping cross terms and the host
cutoffs. A sufficient estimate must produce a divergent delta/a^(3/2)
on every eligible failure sequence or control the full signed residual.

## 6. Audit and reproducibility

The all-pair identities were independently audited in the preceding session;
the auditor reported 523 rational cases. The checked-in verifier below is
an independently reproducible record, including AP-rich sets, proper hosts,
diagonals, pair means/norms, adjoints, and Schur inequalities. Finite cases
are not eligible asymptotic examples. No external peer review is claimed.

[Verifier](../../verification/scripts/verify_all_pair_operator_20261103.py).
The prior GU24 draft and pre-correction navigation are preserved separately.

The dedicated run passed 46,352 exact assertions on 654 instances over
p=5,7,11, including 76 AP-rich instances. The repository integrity check
and 16 tooling tests passed. The rendered dashboard correction was inspected
in the local browser. These checks do not certify the older inherited
analytic claims; consult each dated correction before using them.

All 39 selected scripts (26 current, 13 legacy) passed in an isolated copy
with Python 3.14.9 and NumPy 2.5.4. The [run manifest](../../history/operator_audit_20261103/verification/summary.json)
records source hashes and timings; adjacent files retain stdout/stderr.
Historical script success does not reinstate withdrawn proof claims.
