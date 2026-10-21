# Localized progression counting in a quadratic interval host

15 October 2026. Offline. **PROVED partial theorem.** This is not a proof of
the local target `r_4(N)=o(N/log N)`. No literature novelty is asserted.

## 1. Statement with finite errors

Let p>3 be prime, let q(x)=c(x-r)^2+b over F_p, with c nonzero, and put

    I={0,...,L-1}, Omega={x:q(x) in I}, w=|Omega|/p, beta=L/p.

A translated residue interval is covered by changing b. Let A be a subset
of Omega with no four-term progression of nonzero difference, and let
a=|A|/|Omega|. Assume Omega is nonempty. All averages below are normalized
by p or p^2, as appropriate. Put K=2+log p (natural logarithm).

Choose an integer H>=1 such that 2H+1<=p and 24H<L. Define

    J={-H,...,H} modulo p, eta=(2H+1)/p,
    beta_0=(L-24H)/p,
    e_2=K^2/sqrt(p), e_3=K^3/sqrt(p).

Then the following explicit inequality holds:

    a <= 1 - [beta_0 eta^2-e_3-(w+4)/p]
                 / [4w(eta^2+e_2)].                         (Q1)

The right side can exceed 1 at small p; no finite-p contradiction is
claimed in that case. Also

    |w-beta| <= K/sqrt(p).                                  (Q2)

In particular, if beta p^(1/6)/(2+log p) tends to infinity, then

    a <= 3/4+o(1).                                         (Q3)

An explicit version is obtained by setting H=ceil(K p^(5/6)). Whenever
24H<L and beta>=2K/sqrt(p),

    a <= 3/4 + 20K/[beta p^(1/6)].                          (Q4)

The hypotheses ensure 2H+1<=p. At beta asymptotic to epsilon/log p,
the error in (Q4) is O_epsilon((log p)^2 p^(-1/6)), tending to zero.
Thus a single quadratic interval host has a terminal bound below 4/5 for
sufficiently large p. This improves the earlier unweighted 53/69 bound.

## 2. Elementary exponential-sum inputs

Use e_p(t)=exp(2 pi i t/p) and hat f(t)=E_x f(x)e_p(-tx).
For an interval V of length l,

    |hat 1_V(t)| <= min(l/p,1/[2 min(t,p-t)])  (t nonzero).

This follows from the geometric sum and sin(pi t/p)>=2t/p for
1<=t<=p/2. Summing gives ||hat 1_V||_1<=2+log p=K. Translation
does not change these absolute values.

For A nonzero in F_p,

    |E_x e_p(Ax^2+Bx)|=p^(-1/2).

To verify this, expand the absolute square of the unnormalized sum,
write the two variables as x and x+t, and sum in x. Only t=0 survives,
giving squared magnitude p. A nonconstant linear phase has average zero.
Every nonzero quadratic form in two variables over F_p can be diagonalized
by an invertible linear change of variables: choose a vector with nonzero
quadratic value (one exists since 2 is invertible), complete the square
in that direction, and repeat on its one-dimensional complement. Its
normalized exponential sum therefore has magnitude p^(-rank/2), at most
p^(-1/2). These arguments prove (Q2) by Fourier expansion of 1_I(q).

## 3. A family of progressions with almost constant vertex degree

For a progression starting at x with difference d, define

    ell(x,d)=2c(x-r)d, D(d)=cd^2,
    F(x,d)=1_J(ell(x,d))1_J(D(d)).

The exact identity is

    q(x+jd)=q(x)+j ell(x,d)+j^2 D(d).                      (Q5)

Let P=1_Omega and

    T=E_(x,d) F(x,d) product_(j=0)^3 P(x+jd).

If q(x) is in I_0={12H,...,L-1-12H} and ell,D belong to J,
use their unique representatives in [-H,H]. For 0<=j<=3 their contribution
has absolute value at most (j+j^2)H<=12H. Thus every q(x+jd) lies in I
as an integer, so there is no modular wraparound in this implication.
Consequently

    T >= E_(x,d) 1_(I_0)(q(x))1_J(ell(x,d))1_J(D(d))
      >= beta_0 eta^2-e_3.                                (Q6)

For the last inequality, expand the three interval indicators. In variables
X=x-r and d the quadratic part of the phase at frequency (s,t,u) is

    c[s X^2+2t Xd+u d^2].

It vanishes identically only at (s,t,u)=(0,0,0). Every other frequency has
exponential average of magnitude at most p^(-1/2). The total absolute
Fourier coefficient weight is at most K^3. This proves (Q6), including
all rank-one quadratic degeneracies.

Let h_F^ne(v) be the sum over positions i=0,1,2,3 of the weighted
completion degrees, with d nonzero:

    h_F^ne(v)=sum_i E_d 1_(d!=0) F(v-id,d)
                         product_(j!=i) P(v+(j-i)d).

For v!=r, discarding the P factors and the exclusion d!=0 gives, in slot i,

    E_d 1_J(2c(v-r)d-2icd^2)1_J(cd^2) <= eta^2+e_2.     (Q7)

Indeed its Fourier phase has quadratic coefficient c(n-2im) and linear
coefficient 2cm(v-r). Both vanish only when m=n=0. Nonconstant linear
phases have zero average; other phases cost at most p^(-1/2).
It follows that

    h_F^ne(v)<=4(eta^2+e_2) for v!=r,
    h_F^ne(r)<=4.                                        (Q8)

The exceptional vertex cannot simply be included in (Q7).

## 4. Hitting argument and the diagonal

Let B=1_A. For d!=0 the four vertices are distinct and every progression
counted by T contains a hole in Omega\A. Counting holes with weight F gives

    E_v (P-B)(v) h_F^ne(v) >= T-w/p.                     (Q9)

The diagonal is exactly w/p: F(x,0)=1 and P(x)^4=P(x).
By (Q8), the left side is at most

    4(1-a)w(eta^2+e_2)+4/p.

Combining this with (Q6) proves (Q1).

To check (Q4), write e=K/sqrt(p), use w>=beta/2, and rearrange (Q1):

    a <= 3/4 +(e+24H/p)/(4w)
               + e_2/(4eta^2)
               + e_3/(4w eta^2)
               + (w+4)/(4wp eta^2).                     (Q10)

For H=ceil(Kp^(5/6)), H<=Kp^(5/6)+1 and eta>=2Kp^(-1/6).
The four terms are bounded respectively by

    12K/(beta p^(1/6)) + K/(2beta sqrt(p)) + 12/(beta p),
    1/(16p^(1/6)),
    K/(8beta p^(1/6)),
    5/(8beta K^2 p^(2/3)).

For p>=5 and beta<=1 their sum is less than
20K/(beta p^(1/6)). This gives an explicit constant and verifies the
asymptotic substitution without unspecified dependence on q, A, or L.

## 5. Finite-pattern extension

Let 4<=m<p and let r_m be any proved upper bound for the size of a
4-AP-free subset of {0,...,m-1}. Put theta=1-r_m/m, R=m(m-1)H,
and assume 2R<L. Use the same F and the product of P(x+jd) for 0<=j<m.
The lower bound for its count is

    T_m >= [(L-2R)/p]eta^2-e_3.

Every nonzero-difference m-progression has at least m-r_m holes: any
integer four-term progression among its occupied indices would give a
nonzero-difference progression in A, because m<p. The m slot degrees
are at most m(eta^2+e_2) off r and at most m at r. The diagonal is w/p.
The same counting argument yields

    1-a >= {theta([(L-2R)/p]eta^2-e_3-w/p)-1/p}
                  / {w(eta^2+e_2)}.                      (Q11)

For fixed m and beta p^(1/6)/K tending to infinity, this gives
a<=r_m/m+o(1). The case m=4, r_m=3 is (Q1). This extension transfers
a finite-pattern occupancy bound; it does not supply a new bound for r_4.

## 6. Limits and next dependency

The progression weights depend on (x,d); they are not a single common
translation of Omega. Thus the theorem does not contradict the failure of
the old translation-packing argument for quadratic windows.

No product-independence claim for several quadratic coordinates is used.
Intersections with existing linear or quadratic constraints need their own
weighted-count and degree analysis. The proof does not show that quadratic
correlation creates an increment with controlled cumulative losses. The
linear spectral packet existence problem is also unchanged.

Independent finite tests are in `verify_residual_field_audit_20261015.py`.
They check (Q5), exact weighted counts, diagonal subtraction, incidence
degrees, and hitting inequalities. Finite tests do not prove (Q3); the
argument above supplies that proof.
