# Boolean occupancy and a 2/3 mixed-window terminal bound

17 October 2026. Offline continuation. **PROVED partial theorem.**
The target r_4(N)=o(N/log N), DIRECT-Q-GAIN, and (P12) remain OPEN.
This note improves a terminal constant, not the structural selection step.
No literature novelty is asserted.

## 1. Exact definitions and Boolean expansion

Use the original mixed-window and tent weight of
`MIXED_QUADRATIC_TERMINAL_20261016.md`: p>3 prime, P=1_Omega,
B=1_A with A subset Omega cyclically nonzero-4AP-free, w=|Omega|/p,
a=|A|/|Omega|, u=B-aP, and F(x,h) the progression weight (not a
conditional-expectation factor). All averages below are normalized over
F_p or F_p^2. The conditional factor is the trivial partition, so g=aP,
E_Omega u=0, and exactly

    u^2=(1-2a)u+a(1-a)P,
    U=E_p u^2=wa(1-a).                                  (B1)

For j=0,...,4 define

    M_j=E_(x,h) F(x,h) sum_(|S|=j) product_(i in S)B(x+ih)
                                      product_(i notin S)P(x+ih).

Thus M_0=T and M_4=Lambda_F(B). On a host progression put
K=sum_(i=0)^3 B(x+ih). Its contribution to M_j is F binom(K,j).
Terms off the host vanish. Direct expansion gives

    R_1^F=a^3 M_1-4a^4T,
    R_2^F=a^2 M_2-3a^3 M_1+6a^4T,
    R_3^F=a M_3-2a^2 M_2+3a^3 M_1-4a^4T,
    R_4^F=M_4-a M_3+a^2 M_2-a^3 M_1+a^4T,
    Q=R_3^F+R_4^F=M_4-a^2M_2+2a^3M_1-3a^4T.            (B2)

Proof: expand each u=B-aP. A term containing exactly k copies of B
occurs binom(4-k,j-k) times in the j-residual sum, with coefficient
(-1)^(j-k)a^(4-k). This proves every displayed identity.

For AP-free A, M_4=aw/p exactly: h=0 has F(x,0)=1 and B^4=B,
while every nonzero h contribution vanishes. In particular

    Q=aw/p-a^4T-R_1^F-R_2^F.                            (B3)

This is an identity, not a lower bound from phase failure. It is the
weighted analogue of the older signed-collapse warning. Eliminating
R_4 with AP exclusion does not prove (P12).

The host diagonal in T is w/p. For j>=1 the diagonal in M_j is
binom(4,j)aw/p. The residual diagonals are

    (R_1^F)_diag=0,
    (R_2^F)_diag=6a^2U/p,
    (R_3^F)_diag=4a(1-2a)U/p,
    (R_4^F)_diag=(1-3a+3a^2)U/p.                         (B4)

These follow from E_p u^j=w[a(1-a)^j+(1-a)(-a)^j].

## 2. A Boolean inequality not contained in pair near-positivity

On a nonzero host progression, K is one of 0,1,2,3. Therefore
binom(K,2)<=K pointwise. At h=0 an occupied vertex has K=4,
and binom(4,2)-4=2. Summing with the nonnegative weight F gives

    M_2<=M_1+2aw/p.                                    (B5)

The diagonal is essential. Equality off the diagonal occurs only at
K=0 or K=3, and the exact slack is

    M_1+2aw/p-M_2
      = E_(x,h) 1_(h!=0) F product_i P_i
                                      1_(K in {1,2}).  (B6)

Thus the nonnegative remainder records weighted progressions with
exactly one or two occupied vertices, with coefficient one in both cases.

## 3. Finite 2/3 terminal theorem

Suppose |R_1^F|<=E_1 and R_2^F>=-E_2 for explicit E_1,E_2>=0.
For a>0, (B2) and (B5) imply the exact finite inequality

    2a(3a-2)T
       <=(1-3a)R_1^F/a^3+2aw/p+E_2/a^2
       <=|1-3a|E_1/a^3+2aw/p+E_2/a^2.                 (B7)

Proof: from R_2^F>=-E_2 and M_2<=M_1+2aw/p,
6a^2T+(1-3a)M_1+2aw/p+E_2/a^2>=0. Substitute
M_1=4aT+R_1^F/a^3 and rearrange. No sign of R_1 is assumed.

Since T>=w/p>0, division is legitimate. If a>2/3, (B7) gives

    a<=2/3+|1-3a|E_1/(6a^4T)
             +w/(3pT)+E_2/(6a^3T).                    (B8)

For a<=2/3 the desired terminal ceiling already holds. A positive
lower bound for T may replace T in the error denominators of (B8).

The original proved results supply explicit finite errors. Let
eps=p^(-1/2), b=|Omega\Omega_-|/p, mu the exact persistent baseline,
beta=(mu+eps)b+1/p, and nu_ij as in (P7) of
`WEIGHTED_PAIR_REDUCTION_20261016.md`. One may take

    E_1=4a^3[mu b+eps(w+b)+2/p],
    E_2=a^2[6beta+(6-sum_(i<j)nu_ij)U eps],
    T_lower=(w-b)(mu-eps).                              (B9)

Replacing the middle coefficient by 6 gives a weaker fully explicit
E_2 without computing any nu_ij. The lower bound T_lower is useful
only when positive; the actual T is always positive.

Consider ANY sequence satisfying the original terminal conditions (M13):

    tau->0, tau wp/r->infinity,
    s(2+log p)/(w sqrt(p))->0,
    sqrt(p)mu_0->infinity, wp mu_0->infinity,
    H=floor(tau wp/(48r)), mu_0=(tau w/(48r))^(d+2s).

Then b/w->0 by (M7), mu>=mu_0, and T=(1+o(1))w mu by
(M8) and T<=w(mu+eps)+1/p. If a>2/3, every inverse power of a
in (B8) is bounded. Consequently

    E_1/(a^4T)->0,
    E_2/(a^3T)->0,
    w/(pT)->0.

For example the terms after division are bounded by constant multiples
of b/w, eps/mu, eps b/(w mu), 1/(wp mu), and eps; all vanish.
It follows uniformly over all phase coefficients and interval positions:

    a<=2/3+o(1).                                       (B10)

In particular this holds for r,log(1/w)=o(sqrt(log p)) and for all
reachable windows of DIRECT-Q-GAIN. It improves the previous 3/4+o(1)
terminal ceiling using the newly available pair theorem. Changing a
terminal constant does not supply the missing increment and does not
prove the logarithmic-density target.

## 4. Sharpness of this one-edge argument and a low-density obstruction

The 2/3 constant cannot be improved using only a single Boolean
four-variable law, exclusion of 1111, uniform marginal density, and
nonnegative pair covariance. The following exact abstract law achieves it:

    probability(0000)=1/9;
    probability(each of the four three-one patterns)=2/9.

Every coordinate has mean 2/3, every distinct-coordinate product has
mean 4/9, hence all pair covariances are zero; (B5) is equality.
Its cubic residual sum is -16/81, quartic residual is zero, and
Q=-(2/3)^4. This is an abstract probability law, not an arithmetic
AP-free set and not a counterexample to DIRECT-Q-GAIN or (P12).

More generally, for 0<=a<=1/2 and a bit pattern S with k ones, put

    probability(S)=a^k(1-a)^(4-k)+(-1)^(k+1)a^4.       (B11)

The probabilities are nonnegative: for k=4 they vanish; for k=2
they equal a^2(1-2a); for k=0 they equal (1-a)^4-a^4; the odd-k
entries are nonnegative. Their sum is one by (1-1)^4=0. Every proper
subset moment agrees exactly with independent Bernoulli(a), because
summing the signed perturbation over a remaining coordinate cancels it.
Thus this law satisfies all pointwise Boolean identities, excludes 1111,
has centered moments of orders one through three zero, but R_4=-a^4.

This makes precise why Boolean identities, missing-edge support, and
all lower one-progression moments alone cannot prove (P12). A successful
argument must add quantitative arithmetic information coupling distinct
progressions and must use the actual phase-selection failure. The proof
of (B11) does not realize such a law on F_p and makes no assertion
about global phase correlations.

## 5. Verification and exact remaining task

`verify_boolean_occupancy_20261017.py` checks (B1)--(B8) in exact rational
arithmetic for Boolean patterns and actual finite AP-free sets in full
and proper mixed windows. It also checks the finite error inputs with
floating square roots, exact diagonal formulas, and both abstract laws.
Small-prime terminal error bounds can be vacuous. The asymptotic theorem
is proved by (B7)--(B10), not extrapolated from finite checks.

The unresolved sufficient inequality remains

    R_3^F+R_4^F>=-(1/2)a^4w mu

under the precisely quantified failure of DIRECT-Q-GAIN (or its concrete
threshold). Formula (B3) shows its incompatibility with actual AP-free
sets on eligible hosts once first and second errors are small. Proving
that incompatibility from phase failure remains the missing arithmetic
selection theorem; none of the identities above supplies it.
