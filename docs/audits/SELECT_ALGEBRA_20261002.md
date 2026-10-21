# SELECT: exact residual expansion, conditional moments, and main-term positivity

2026-10-02. Offline. SELECT and the local r4 target remain unproved. This
note adds a full-group main-term positivity theorem and exact residual
bounds; it does not promote a conjectured Fourier cancellation inequality
to a theorem. Earlier notes/scripts are preserved.

The user calls quarter conversion sharp; the proved constant 8/pi^2 is a
universal lower bound whose optimality has NOT been established.

Read the full new SELECT directive and CURRENT_STATUS, NEW_RESULTS,
STRUCTURAL_HYPOTHESIS_ATTACK, SOLUTION_LEDGER, PROOF_DEPENDENCIES, AGENTS,
STRUCTURAL_SAMPLING and the prior graph/quadratic notes. This lane addresses
full-group algebra first, as requested. Root handles relative-window cells
and exact downstream threshold weakening.

## 1. Definitions and all sixteen terms

Work on G=Z_p, p>3, with normalized expectations and unnormalized frequency
sums. B=1_A, a=E B, F any partition, g=E(B|F), u=B-g, h=g-a. Put

    v=E h^2, b=E u^2=a(1-a)-v.

Orthogonal conditional expectation gives E u=E h=E uh=0. Define
L(v_0,v_1,v_2,v_3)=E_{x,d} product_j v_j(x+jd).
For I subset {0,1,2,3}, let L_I have u in slots I and g elsewhere. Then

    Lambda_4(B)=R0+R1+R2+R3+R4,                         (A1)

with the complete explicit grouping

    R0=L(g,g,g,g),
    R1=L(u,g,g,g)+L(g,u,g,g)+L(g,g,u,g)+L(g,g,g,u),
    R2=L(u,u,g,g)+L(u,g,u,g)+L(u,g,g,u)
       +L(g,u,u,g)+L(g,u,g,u)+L(g,g,u,u),
    R3=L(u,u,u,g)+L(u,u,g,u)+L(u,g,u,u)+L(g,u,u,u),
    R4=L(u,u,u,u).

For AP-free A, the exact left side is a/p, retaining d=0. No individual
Rj is assumed to have a favorable sign.

The normalized Fourier formula for each of those sixteen terms is

    L(v0,v1,v2,v3)
      =sum_{r,s} v0hat(r+2s) v1hat(-2r-3s)
                  v2hat(r) v3hat(s).                   (A2)

Indeed x-average imposes k0+k1+k2+k3=0 and d-average imposes
k1+2k2+3k3=0; putting k2=r,k3=s gives the displayed parameterization.
No additional conjugations appear for this multilinear convention.
Reality may be used afterward to pair opposite frequencies.

## 2. Exact conditional Bernoulli moments — PROVED

On every F-cell, B has Bernoulli mean g and u=B-g. For all integers k>=1,

    E(u^k|F)=g(1-g)^k+(1-g)(-g)^k.                     (A3)

In particular

    E(u^2|F)=g(1-g),
    E(u^3|F)=g(1-g)(1-2g),
    E(u^4|F)=g(1-g)(1-3g+3g^2).                        (A4)

Pointwise Booleanity is exactly

    u^2=(1-2g)u+g(1-g).                                (A5)

Writing m_j=E h^j, the integrated third and fourth moments are

    E u^3=a-3a^2+2a^3+(-3+6a)v+2m3,
    E u^4=a-4a^2+6a^3-3a^4
            +(-6+18a-18a^2)v+(6-12a)m3-3m4.            (A6)

Since |h|<=1, |m3|,m4<=v. Thus these marginal moment corrections are O(v).
This uses conditional Booleanity fully at one point, but does not provide
cross-position independence along an AP. Conditional orthogonality at x
cannot be substituted for orthogonality at x+d or x+2d.

## 3. New full-group main-term positivity lemma — PROVED

For ANY real g=a+h with E h=0, E h^2=v, one has

    |Lambda_4(g)-a^4| <=4a v^(3/2)+v^2,                (A7)

for a>=0. The statement does not require Booleanity, F-measurability or
nonnegativity of g. Under SELECT's low factor energy v<=zeta a^(9/4),
0<zeta<=1/4, 0<=a<=1,

    Lambda_4(g)>=a^4[1-4zeta^(3/2)a^(3/8)
                         -zeta^2 a^(1/2)]
                >=(7/16)a^4.                          (A8)

Thus the main term's positivity is not an additional missing assumption
on the full group. It is already a consequence of the stated energy bound.

Proof. Expand g=a+h. All one-h and two-h terms vanish. For the latter,
any pair of distinct progression coordinates is uniform and independent:
the map (x,d)->(x+id,x+jd) has determinant j-i!=0 for p>3.
The four surviving cubic terms, each multiplied by a, are bounded by
v^(3/2): the Fourier formula for three distinct coordinates is a one-variable
sum of three h coefficients at invertible multiples of the frequency.
Bound one coefficient by ||h||2=sqrt(v) and the sum of the products of
the other two by v using Cauchy-Schwarz. The four-h term is <=v^2:
split into two pairs, use Cauchy-Schwarz, and use independence within each
pair to identify its squared L2 norm as v^2. This proves A7. Substitution
and a<=1 give 4zeta^(3/2)+zeta^2<=1/2+1/16=9/16, proving A8.
At a~epsilon/log p the error in A7 is actually o(a^4), with relative
orders a^(3/8) and a^(1/2).

## 4. Residual groups: explicit coefficient-aware upper bounds — PROVED

Let rho=max_{k!=0}|uhat(k)|. For b,v>=0, all sixteen terms satisfy

    |R1| <=12a rho v+4sqrt(b)v^(3/2),
    |R2| <=12a rho sqrt(bv)+6bv,
    |R3| <=4a rho b+4sqrt(v)b^(3/2),
    |R4| <=b^2.                                       (A9)

These follow by expanding each g=a+h. In R1, terms with zero or one h
vanish by means/pair independence, leaving twelve a-times cubic uhh
terms and four quartic uhhh terms. In R2 the constant-g terms vanish,
leaving twelve a-times uuh terms and six uuhh terms. R3 has four a-times
uuu terms and four uuuh terms. Every cubic with one u has magnitude at
most rho times the product of the L2 norms of its other two factors, by
its one-variable Fourier formula. Every quartic has magnitude at most
the product of its four L2 norms, by pairwise-coordinate independence
and Cauchy-Schwarz as in A7. This supplies A9 without hidden p factors.

At v<=zeta a^(9/4), b<=a, and rho^2<=c a^(5/2)ell(a), these guarantees
have the following potentially dominant orders:

    R1: a^(31/8) plus a^(9/2)sqrt(ell),
    R2: a^(13/4) plus a^(31/8)sqrt(ell),
    R3: a^(21/8) plus a^(13/4)sqrt(ell),
    R4: a^2.

Several exceed a^4. Therefore the sharp one-point moments and the stated
residual Fourier maximum do not close the expansion using these verified
inequalities. This is an audit of these bounds, not a lower bound on the
best possible AP-specific estimate.

For the trivial factor, h=0 and v=0, the expansion is especially exact:

    Lambda_4(B)=a^4+2a(T_u+S_u)+Q_u,
    |T_u|,|S_u|<=rho b,
    Q_u=Lambda_4(u).                                   (A10)

Consequently controlling the cubic contribution alone by o(a^4) through
its generic Fourier bound requires rho=o(a^2). SELECT failure merely gives
rho=O(a^(5/4)sqrt(ell)), a much larger allowable threshold. It does not
even guarantee smallness of that cubic envelope. Thus a proof must use
actual AP exclusion to improve or reorganize these branches; it cannot
label the SELECT-failure threshold generic Fourier pseudorandomness.

## 5. Sum-before-max experiment

For any mean-zero real u and pair derivative D_d(x)=u(x)u(x+d), averaging
BEFORE maximizing gives

    E_d |D_d_hat(k)|^2
        =sum_t |uhat(t)|^2|uhat(k-t)|^2.                 (A11)

This prior graph identity is used here, not counted as new. Its complete
frequency sum is b^2. Its zero-frequency value is

    E_d |E_x u(x)u(x+d)|^2=sum_t |uhat(t)|^4<=rho^2 b.  (A12)

At SELECT failure, A12 supplies only O(a^(7/2)ell(a)), which is larger
than a^4. Fourth difference moments reproduce the previously derived
codegree eight-factor expression and U3 trace. None of the AP-specific
zeros removes terms from that unsigned expansion without an additional
signed argument. Reversing A12 or replacing derivative mass by original
mass would be invalid.

The two-variable coupling and support cocycle from STRUCTURAL_GRAPH remain
constraints of genuine B, not of every arbitrary positive graph. This lane
did not obtain a stronger amplitude estimate from those constraints.

## 6. Absolute perturbation bounds are the wrong target — REFUTED schema

Suppose a proposed argument derives

    |Lambda_4(B)-Lambda_4(g)|=o(a^4)

solely from Booleanity, low factor energy and residual coefficients below
SELECT's threshold, without using AP-freeness. The prior quadratic Boolean
interval host refutes that implication already with trivial F and g=a:
its density a~1/log p, coefficient maximum O(log p/sqrt p), and zero
factor energy satisfy those premises, but Lambda_4(B)>=c a^3, so its
difference from a^4 is much larger than a^4. This is not an AP-free example.
The lesson is exact: a sufficient perturbation theorem must be a signed
lower bound or must exploit AP exclusion, rather than a generic absolute
norm comparison under the three listed hypotheses.

One possible precise full-group sufficient replacement, now with the main
term A8 proved, would be

    R1+R2+R3+R4 >= -(3/8)a^4                           (A13)

for AP-free B with the low factor energy and small residual coefficients.
Together with A8 this would give Lambda_4(B)>=a^4/16, contradicting a/p
once pa^3>16. A13 is CONJECTURED, not proved. It is a signed sixteen-term
cancellation inequality rather than an absolute perturbation assertion.
It still requires a relative-window replacement for the actual SELECT
quantifiers; root's lane addresses that geometry. No claim of reducing
all of SELECT to A13 alone is made.

## 7. Checks and classifications

`python3 verify_select_algebra_20261002.py` passed:

- 480 B/factor cases in Z5,Z7;
- 7,680 explicitly expanded multilinear terms;
- 3,360 exact rational conditional moment checks;
- 310 low-energy main-term positivity cases;
- coefficient-aware residual bounds A9 with tolerance 1e-10.

A1-A10 and A12 are symbolically PROVED above; A11 is a prior PROVED
identity. A13 is CONJECTURED and not used as an established theorem.
The absolute norm-only schema in section 6 is REFUTED by the existing
quadratic host, not by a new alleged AP-free counterexample. The finite
executions are COMPUTATIONALLY CHECKED ONLY. No asymptotic theorem is
inferred from the enumerations.
