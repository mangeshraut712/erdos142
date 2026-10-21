# O2: exact quantifiers and a direct weighted cubic estimate

17 October 2026. Offline working note by the tradeoff-review subagent.
The local target and (P12) remain OPEN. The inequalities below are proved
partial results, not a global inverse theorem or a selection theorem.

## 1. Exact negation of DIRECT-Q-GAIN

Fix epsilon>0. Call (p,Omega,A) eligible when it obeys every hypothesis
in (T5)--(T6) of `DIRECT_INCREMENT_TRADEOFF_20261016.md`, including the
actual Boolean and nonzero-difference cyclic 4-AP exclusion assumptions.
Use its specified presentation of Omega when counting r. Put

    a=|A|/|Omega|,
    delta=max_(c,t)!=(0,0) |E_Omega (1_A-a)e_p(-cx^2-tx)|,
    qrel=delta/a^(3/2).

DIRECT-Q-GAIN says

    for every epsilon>0 there exist c>0, p0, and F:(0,4/5]->[1,infinity)
    with lim_(a->0) F(a)=infinity, such that every eligible triple
    with p>=p0 has qrel>=c F(a).

Its exact negation is

    there exists epsilon>0 such that for every c>0, every p0, and
    every such divergent F, there is an eligible (p,Omega,A), p>=p0,
    with qrel<c F(a).

Here F is chosen before the counterexample, and may depend on epsilon
but not on the selected prime, window, or set. Strict inequality is
appropriate because the claimed selection bound is non-strict.
Counterexamples to a single prescribed F, such as loglog(e^2/a), do NOT
by themselves negate the existence of some slower divergent multiplier.

There is an equivalent sequential formulation of failure, useful when
trying to construct an obstruction. For some epsilon>0, at least one
of the following two kinds of eligible sequences exists:

1. a_n->0 and qrel_n remains bounded above;
2. p_n->infinity, inf_n a_n>0, and qrel_n->0.

Proof of the equivalence. Either sequence violates every proposed c,F,p0.
In case 1, p_n->infinity follows from
a_n>=epsilon/(2 log|Omega_n|)>=epsilon/(2 log p_n).
In case 2 use F>=1. Conversely, suppose neither sequence exists. Define

    m(s)=inf {qrel: eligible triple, a<=s},

with inf(empty)=infinity. Absence of sequence 1 gives m(s)->infinity
as s->0. Choose alpha>0 with m(alpha)>=1. Absence of sequence 2 gives
some p0 and b1>0 such that all eligible triples with p>=p0 and
a>=alpha have qrel>=b1; otherwise select p_n>=n and qrel_n<1/n.
Thus b=min(1,b1)>0 is a uniform baseline for the entire p>=p0 class.
Let m0(s) be the same infimum restricted to p>=p0, and set

    c=b/2,
    F(a)=min(a^(-1/4), m0(a)/b),

interpreting min(finite,infinity) as the finite argument. Then F>=1,
F(a)->infinity, and every eligible tail triple obeys
c F(a)<=m0(a)/2<=qrel/2. This supplies DIRECT-Q-GAIN for that epsilon,
contradicting failure. No continuity of the lower envelope is used.

The second alternative cannot silently be omitted: the current statement
quantifies over all densities up to 4/5 on mixed hosts, not just a tending
to zero. This characterization does not establish either alternative.

## 2. Cubic forms from direct quadratic correlations

Work on F_p, p>3, with the exact weight F and probability distribution
lambda(C,beta,N) of (P4) in `WEIGHTED_PAIR_REDUCTION_20261016.md`:

    F(x,h)=sum lambda(C,beta,N)e_p(2Cxh+Nh^2+beta h),
    lambda>=0, sum lambda=1.

Let u be real, supported in Omega, and put

    U=E_p u^2,
    q=max_(c,t) |Q_u(c,t)|,
    Q_u(c,t)=E_p u(y)e_p(-cy^2-ty).

For every three distinct slots i,j,k from {0,1,2,3},

    |E_(x,h) F(x,h)u(x+ih)u(x+jh)u(x+kh)| <= q U.       (C1)

Proof. For each individual frequency (C,beta,N), choose coefficients
gamma_l for l in {i,j,k} satisfying

    sum gamma_l=0, sum l gamma_l=C, sum l^2 gamma_l=N.

The Vandermonde determinant is a product of differences in {1,2,3},
so it is invertible for p>3. Choose theta_l with
sum theta_l=0 and sum l theta_l=beta. Then exactly

    2Cxh+Nh^2+beta h
       =sum_l [gamma_l(x+lh)^2+theta_l(x+lh)].

Define g_l(y)=u(y)e_p(gamma_l y^2+theta_l y). Every Fourier coefficient
of every g_l has magnitude at most q, and every squared L2 norm is U.
Changing variables to the first two occupied slots writes the third as
Av+Bz with A,B nonzero. Fourier expansion gives

    E_(v,z) g_i(v)g_j(z)g_k(Av+Bz)
       =sum_t ghat_i(-At)ghat_j(-Bt)ghat_k(t).

Bounding the last factor by q and using Cauchy-Schwarz and Parseval on
the other two proves qU. Averaging with lambda costs no extra factor.
This proof uses direct global quadratic correlations; it makes no
U^3-to-global-phase inference.

## 3. Proper-host correction and exact budget deficit

Now take u=1_A-a1_Omega, so U=wa(1-a), Q_u(0,0)=0, and q=w delta.
Let b=|Omega\Omega_-|/p, and retain

    beta_boundary=(mu+p^(-1/2))b+1/p.

Each cubic term has one remaining host indicator. Removing it changes
the term by at most beta_boundary: a contributing occupied slot must
lie in the eroded boundary, and |u|<=1 allows the same degree estimate
as (P8). There are four cubic terms, each with prefactor a. Consequently

    |R_3^F| <= 4a qU+4a beta_boundary
             =4w^2 a^2(1-a)delta+4a beta_boundary.       (C2)

This is valid for the ORIGINAL specified weight, including h=0. No
AP exclusion was used; it applies in particular to actual eligible sets.
Under failed concrete selection delta<c a^(3/2)R(a), division by the
desired scale yields

    |R_3^F|/(a^4w mu)
      <=4c(1-a)(w/mu)a^(-1/2)R(a)
        +4[(1+p^(-1/2)/mu)b/(a^3w)+1/(p a^3w mu)].    (C3)

The first term is not small. Even if w/mu is bounded, its displayed
upper bound grows like a^(-1/2)R(a); on general reachable hosts there
is no adequate universal upper bound on w/mu. This is a deficit of
this estimate, not an impossibility theorem about sharper arguments.

For the original choice tau=a^2/log p, the leading upper bound for the
boundary contribution is 2/(a log p), since

    b <= tau w/2+2s(2+log p)/sqrt(p).

At a approximately epsilon/log p, this is only O_epsilon(1), not o(1).
It would be incorrect to claim otherwise. One may instead define a new
weight using tau=a^3/log p. Then the leading boundary term is 2/log p,
and the other terms are o(1) on reachable hosts with
r,S=o(sqrt(log p)), a>=epsilon/log p. Indeed

    log(1/mu0)
       <=2r[S+log(48r)+loglog p+3log(1/a)]=o(log p).

The first- and second-residual proofs also remain valid for this smaller
tau. This change therefore removes the boundary obstacle to (C2), but
does not remove its much larger spectral deficit. It is a variant of the
weighted formulation, not a proof of (P12) for the original fixed weight.
For (C2) alone to give cubic smallness one would need roughly

    delta=o(a^2 mu/w),

far below the failed-selection upper threshold a^(3/2)R(a).

## 4. An exact quartic chirp identity and its limitation

There is a useful full-group diagnostic, independent of the mixed weight.
For real u and p>3, let Lambda_4(u)=E_(x,h) product_(j=0)^3 u(x+jh).
Then

    Lambda_4(u)
      =sum_(c,t) |Q_u(c,t)|^2 |Q_u(3c,3t)|^2
           -U^2+(E_p u^4)/p.                         (C4)

The frequency sum is unnormalized. To prove the identity, expand the
four chirp factors and sum c,t. Orthogonality imposes

    -x0+3x1-3x2+x3=0,
    -x0^2+3x1^2-3x2^2+x3^2=0.

Write x0=x, x1=x+h, x2=x+k; then x3=x-3h+3k and the quadratic equation
is 6(h-k)(2h-k)=0. Its two branches are the 4-AP branch k=2h and the
pairing branch k=h, with their common diagonal counted twice. The two
branch sums give Lambda_4(u) and U^2; their intersection gives E u^4/p.

Therefore positivity gives only Lambda_4(u)>=-U^2+E u^4/p. Meanwhile
Parseval for each c gives sum_(c,t)|Q_u(c,t)|^2=pU, hence

    sum_(c,t)|Q_u(c,t)|^2|Q_u(3c,3t)|^2 <= p q^2 U.    (C5)

A small supremum of the chirp coefficients does not, through these
bounds, control the signed difference from the baseline U^2. At a
logarithmic density the p factor makes (C5) ineffective, while the
lower bound has scale U^2, not a^4w mu. This identity records exactly
the additional quartic covariance that a successful argument would
need to control. It is not a bound for the original weighted R_4^F.

## 5. Verification scope

`verify_o2_cubic_quantifiers_20261017.py` checks the cubic phase absorption,
the direct cubic inequality, the actual positive-tent mixed weight,
proper-host cubic correction, and the quartic identity on small primes.
Finite checks do not test the logarithmic target domain: the domain (T5)
is empty at these small primes. Quantifier equivalence and asymptotic
deficits rest on the proofs above, not finite numerical extrapolation.
