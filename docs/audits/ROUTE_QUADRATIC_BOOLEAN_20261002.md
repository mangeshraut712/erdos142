# Quadratic stability and Boolean derivative-spectrum attempt

Date: 2026-10-02. Offline. No internet, no claim about the official problem,
no claimed literature novelty, and no proof of the local r4 target.

## 1. Scope and prior-result boundary

README, PHASE2_AUDIT, SIGNED_RESEARCH, FULL_GROUP_HOSTILE_AUDIT_20260914,
and TARGET_SCALE_ENERGY_BUDGET_20260914 were inspected. The last already
proves the positive pure-quadratic resonance for an interval indicator.
That resonance is an accepted prior input here, not a new result.
The additions below are its vertexwise bound and uniform deletion stability,
and an exact Boolean derivative-spectrum concentration statement.

All averages on Z_p are normalized, p>3 prime; frequency sums are ordinary.
Fourier transform is c_t=E_y g(y)e_p(-ty).

## 2. Pure quadratic host: robust exclusion theorem — PROVED

Let S subset Z_p, g=1_S, beta=|S|/p, K=sum_t |c_t|,
q(x)=lambda(x-r)^2+c with lambda!=0, and B(x)=g(q(x)). Put

    Z_S = sum_t |c_t|^2 |c_{3t}|^2.

For ANY nonconstant-4AP-free A subset Z_p (A need not be inside B), put

    delta = |{x: B(x)=1 and x not in A}|/p.

Then

    Z_S - K^4/sqrt(p) - 5/p
        <= 4 delta [beta^2 + K^3/sqrt(p)].                 (Q1)

Thus if the left side is positive, Q1 gives an explicit lower bound on the
number of host points which must be deleted. Added points outside B do not
invalidate the conclusion.

### Proof, with the vertexwise estimate

The four-fold quadratic expansion is

    sum_{k_0,...,k_3} product_j c_{k_j}
       E_{x,d} e_p(sum_j k_j q(x+jd)).

After translation x-r, its quadratic matrix is zero precisely when
sum k_j=sum j k_j=sum j^2 k_j=0. This has solutions
(k_0,k_1,k_2,k_3)=t(-1,3,-3,1), since the constraint matrix has rank 3
for p>3. The constant phase c sum k_j also vanishes. Realness of g gives
that these terms sum to Z_S. For every remaining matrix, squaring the
normalized Gauss sum and averaging the translated variable gives magnitude
p^(-rank/2), at most p^(-1/2). Consequently

    |Lambda_4(B)-Z_S| <= K^4/sqrt(p).                      (Q2)

Fix a slot i in {0,1,2,3} and a vertex u!=r. Its normalized number of
three-point completions in the host is

    D_i(u)=E_d product_{j!=i} g(q(u+(j-i)d)).

Writing h_j=j-i, a Fourier term is constant in d exactly when

    sum_{j!=i} h_j k_j = sum_{j!=i} h_j^2 k_j =0.         (Q3)

Because u-r!=0, both conditions really are required. The two equations
have rank 2 for p>3. In increasing order of the remaining slots, their
kernel vectors are

    i=0: (-3,3,-1)t;
    i=1: ( 1,3,-1)t;
    i=2: (-1,3, 1)t;
    i=3: ( 1,-3,3)t.

Each vector contains an opposite pair, at either t or 3t. The associated
resonant sum has absolute value at most

    max_t |c_t| * sum_t |c_t|^2 <= beta*beta=beta^2,

using |c_t|<=beta, Parseval sum |c_t|^2=beta, and invertibility of 3.
The remaining one-variable phase is either a nonconstant linear phase
(mean zero), or a nonzero quadratic phase (mean magnitude p^(-1/2)).
The sum of absolute Fourier weights is at most K^3. Hence

    D_i(u) <= beta^2 + K^3/sqrt(p), for every u!=r.        (Q4)

Now every nonzero-d host progression must contain a point in B\A,
since otherwise it would be a nontrivial progression in A. Union-bound
these holes over the four positions. Ordinary holes contribute at most
4 delta [beta^2+K^3/sqrt(p)] to the normalized count by Q4. The possible
single exceptional hole r contributes at most 4/p. The diagonal d=0
contributes (E B)/p<=1/p. Combining these with Q2 proves Q1.

### Interval specialization at beta about epsilon/log p

For S={0,...,L-1}, beta=L/p<=1/2, the elementary geometric-sum formula
and harmonic summation give K<=1+log p. For
0<=t<=floor(1/(12 beta)), both interval coefficients at t and 3t have
magnitude at least 2 beta/pi. These indices are distinct when L>=1 and
p>3. There are at least 1/(12 beta) such indices, and therefore

    Z_S >= 4 beta^3/(3 pi^4).                             (Q5)

For fixed epsilon>0, beta~epsilon/log p implies, eventually,

    K^4/sqrt(p)+5/p <= 2 beta^3/(3 pi^4),
    K^3/sqrt(p) <= beta^2,
    E B <= 2 beta.

Q1 consequently gives

    delta >= beta/(12 pi^4),
    |B\A|/|B| >= 1/(24 pi^4).                            (Q6)

So an AP-free set cannot agree on 1-o(1) of the points of this quadratic
interval host. This is stronger than pointing out one progression, and
explicitly forbids negligible deletion as a repair of the linearly invisible
quadratic example. It does NOT forbid deletion of a fixed or large fraction;
it does NOT cover arbitrary locally quadratic factors; it does NOT prove
a density increment for an arbitrary AP-free set.

## 3. Boolean pair-derivative angular mass — PROVED

Let B=1_A be nontrivial-4AP-free and a=E B. For d!=0 put

    C_d(x)=B(x)B(x+d), theta_d=E C_d,
    w_d(k)=|C_d_hat(k)|^2,
    H_d={k!=0: cos(4 pi k d/p)<0}.

Booleanity gives C_d^2=C_d, hence sum_k w_d(k)=theta_d,
and w_d(0)=theta_d^2. AP exclusion gives the pointwise equation

    C_d(x) C_d(x+2d)=0.

Fourier transform, followed by taking real parts, gives the exact equality

    sum_k w_d(k) cos(4 pi k d/p)=0.                       (B1)

Its zero frequency is theta_d^2, with positive sign. Since every term
outside H_d is nonnegative and every negative cosine has absolute value
at most 1,

    sum_{k in H_d} w_d(k) >= theta_d^2.                  (B2)

A stronger margin version uses z=theta_d/2>0. Let

    J_d={k!=0: cos(4 pi k d/p)<=-theta_d/2}.

Outside J_d, each nonzero cosine is >=-z; on J_d it is >=-1.
B1 therefore implies, on writing W=sum_{J_d} w_d,

    0 >= theta_d^2 - z(theta_d-theta_d^2-W)-W,
    W >= [theta_d^2-z(theta_d-theta_d^2)]/(1-z)
      >= theta_d^2/(2-theta_d).                          (B3)

The intermediate first lower bound is actually slightly stronger. The last
bound follows by discarding the nonnegative z theta_d^2 contribution.
When theta_d=0 both assertions mean zero and require no division.

Average d with normalized E_d over all p values, setting the d=0
contribution to zero. The autocorrelation identity and Parseval give

    E_d theta_d^2 = sum_k |B_hat(k)|^4 >= a^4,
    theta_0=a.

Thus

    (1/p) sum_{d!=0} sum_{H_d} w_d(k) >= a^4-a^2/p,      (B4)
    (1/p) sum_{d!=0} sum_{J_d} w_d(k) >= (a^4-a^2/p)/2.  (B5)

The subtracted a^2/p is essential; the d=0 fiber is not AP-free.
A sharper bound retaining the excluded diagonal is

    (1/p) sum_{d!=0} theta_d^2
       >= (a^2-a/p)^2/(1-1/p),                            (B6)

because (1/p) sum_{d!=0} theta_d=a^2-a/p and Cauchy-Schwarz is taken
over only p-1 values. B4 and B5 may replace their a^4-a^2/p terms by
this B6 bound. Equality holds when all nonzero differences have equal
pair count; the Z_13 set {0,1,3,9} realizes that equality.

This derives a two-variable, phase-sensitive mass obstruction from the
exact polynomial constraints, rather than an unsigned U3 estimate.
At a=epsilon/log p its forced mass is approximately a^4. Total derivative
energy E_d sum_k w_d(k)=E_d theta_d=a^2; the forced fraction is order a^2.

### Exact obstacle to using B4/B5

The selected sets H_d and J_d depend on d. Their frequencies need not lie
in any one small additive span. No justified argument converts this
angular mass into coherent derivative frequencies of a locally quadratic
phase, or a hereditary density increment. Cauchy-Schwarz alone can average
away the arithmetic dependence and supplies no needed complexity bound.
No such conversion is asserted. For the AP-free Z_13 difference set
{0,1,3,9}, every d!=0 has theta_d=1/13 and C_d is a singleton.
Thus every derivative frequency has w_d(k)=1/169, while the original
squared spectrum is exactly |B_hat(k)|^2=3/169 for k!=0. Angular
concentration exists without any preference among derivative frequencies.
This rules out a transfer claiming that the angular selector itself
identifies a preferred original frequency or a concentrated fixed derivative
frequency; it does not disprove a target-density inverse statement.

## 4. Quantitative quadratic localization budget — CONDITIONAL audit

Let correlation rho(a) yield an additive density gain comparable to rho(a)
on a hereditary domain, with per-step logarithmic loss L(a). If the gain
is Delta(a)>=c a^s and L(a)<=C a^(-t)log^D(2/a), the accumulated loss is
bounded by a constant times

    integral_{a0}^{a*} a^(-s-t) log^D(2/a) da,

or by dyadic-epoch summation with the same order. If s+t>1 the dominant
order is a0^(-(s+t-1))log^D(2/a0). At a0=epsilon/log N this is

    O_epsilon((log N)^(s+t-1)(log log N)^D).

For any fixed D, s+t<2 suffices to make this o(log N). At s+t=2,
positive log powers fail this test, while a negative log power can supply
an endpoint saving. This is a sufficient ledger under the stipulated
uniform hereditary premises, not an inverse theorem.

Starting from ||f||U3>=c a^(3/2), an assumed actual-norm inverse bound
rho>=c||f||U3^C supplies only rho>=c' a^(3C/2). Even with t=0 the
strict exponent test requires C<4/3. PHASE2_AUDIT already disproves uniform
actual-norm inverse exponents C<2 in the relevant Boolean AP-free range.
A density-sensitive inverse statement is logically different, and remains
possible but unproved.

If one merely has gain rho=exp(-C a^(-k)), k>0, and no larger gain,
then the number of steps allowed by that guarantee on the initial dyadic
epoch has order a0/rho(a0), namely

    (epsilon/log N) exp(C_epsilon (log N)^k).

This grows faster than log N for every fixed k>0. Such a guarantee cannot
close the needed ledger even with constant cost per step. This is failure
of the guaranteed bound, not a lower bound on actual necessary steps.

Rank R(a)=exp(C sqrt(log(1/a))) is subpolynomial in 1/a. It is cheap with
a gain a^(2-sigma) for any fixed sigma>0: accumulated cost is at most
(log N)^(1-sigma+o(1))=o(log N), when L is R times a polylog. The same
rank with only gain a^2 fails this sufficient test. Saying the rank alone
is harmless omits the number of increments.

## 5. Verification, dependencies, and remaining scope

`python3 verify_route_quadratic_boolean_20261002.py` passed:

- 2,208 quadratic host subsets in Z_5,Z_7,Z_11, checking Q2 and Q4;
- 2,612 AP-free subsets of these hosts (p<=7), checking Q1;
- 765 AP-free Boolean subsets, checking B1, B2, B4, B5;
- 5,304 nonempty derivative fibers, checking B3.

Floating Fourier tolerances are 1e-10. The polynomial-kernel calculations,
Parseval proofs and union bound above are the mathematical proofs; these
finite checks do not establish an asymptotic target. The interval Q6 is
an asymptotic consequence of the explicit symbolic bounds, not a finite
numerical inference.

Dependency classifications:

- prior positive quadratic resonance / Gauss bound: PROVED prior result;
- Q1/Q4 robust vertexwise deletion estimate: PROVED in this note;
- Q6 constant-fraction interval-host deletion: PROVED in this note;
- B1-B5 Boolean derivative angular mass: PROVED in this note;
- finite script execution: COMPUTATIONALLY CHECKED ONLY;
- general coherent quadratic inverse/localization: CONJECTURED, unused;
- power and exponential iteration ledgers: CONDITIONAL on their stated steps.

The next focused attack is to prove that B4/B5, together with AP-free
Booleanity, produces a coherent derivative graph with density-sensitive
correlation and localization loss meeting s+t<2 (or a rigorously quantified
endpoint saving). The present note supplies no proof of that implication.
