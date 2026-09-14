# Phase 2: hostile audit and exponent reset

Date: 2026-09-06. Offline; no internet, generic inverse theorem, or public posting.

STATUS: (D) α^(3/2) LEMMA VERIFIED — INVERSE STEP STILL OPEN

The alternative density-sensitive inverse step remains open in this work.
There is a stronger negative conclusion about the proposed **actual-norm**
inverse statement: a uniform bound `correlation >= c ||f||U3^C` with `C<2`
is impossible, even for the specified AP-free sets with `p alpha^3 >= 2`,
and even allowing every test function bounded by one. This is a proved
support/normalization obstruction, not an unsuccessful inverse-theorem search.
It does not disprove `correlation >= c alpha^(2-epsilon)`.

## 1. Hostile audit verdict

**(A1) VERIFIED. The α^(3/2) U³ lower bound is correct.**

The mixed inequality was derived independently in two audit lanes and
checked against an explicit complete Cauchy–Schwarz calculation below.
The previous finite checks were rerun; new checks include a set satisfying
the density cutoff, complex conjugations, and deliberately false extensions.
Finite checks support the algebra, not the asymptotic conclusions.

All averages on `G=Z_p` are normalized: `E_x=p^-1 sum_x`. Frequency sums
are ordinary, unnormalized sums. Write

\[
e_p(t)=\exp(2\pi it/p),\qquad
\widehat g(\xi)=\mathbb E_xg(x)e_p(-\xi x).
\]

Orthogonality gives inversion and Parseval:

\[
g(x)=\sum_\xi\widehat g(\xi)e_p(\xi x),\qquad
\mathbb E|g|^2=\sum_\xi|\widehat g(\xi)|^2.
\]

Our conjugation convention is

\[
\|g\|_{U^k}^{2^k}
=\mathbb E_{x,h_1,\ldots,h_k}
 \prod_{\omega\in\{0,1\}^k}\mathcal C^{|\omega|}
 g(x+\omega\cdot h),
\]

where `C` is complex conjugation. In particular, put

\[
F_g(h,k)=\mathbb E_xg(x)\overline{g(x+h)}
                 \overline{g(x+k)}g(x+h+k).
\]

Direct expansion of the square gives

\[
\|g\|_{U^3}^8=\mathbb E_{h,k}|F_g(h,k)|^2.
\tag{1}
\]

## 2. Exact proof, including every normalization

### 2.1 Expansion and diagonal

Let `B=1_A`, `alpha=E B`, `f=B-alpha`, `f_j=f(x+jd)`, and set

\[
T=\mathbb E f_0f_1f_2,\quad
U=\mathbb E f_0f_1f_3,\quad
Q_4=\mathbb E f_0f_1f_2f_3,\quad M=\Lambda(f,B,B,f).
\]

Each of the four one-f terms has mean zero. For `i<j`, the map
`(x,d) -> (x+id,x+jd)` has determinant `j-i`; it is invertible when
2 and 3 are invertible. Each of the six two-f terms therefore equals
`(E f)^2=0`.

The substitution `(x,d)->(x+d,d)` gives the equality of the triples
`012` and `123`. Reversal `(x,d)->(x+3d,-d)` identifies `013` and `023`.
These substitutions are bijections, without any division. Thus

\[
\Lambda_4(B)=\alpha^4+2\alpha T+2\alpha U+Q_4,
\qquad M=2\alpha U+Q_4.
\tag{2}
\]

For AP-free A, every `d!=0` summand in the indicator count is zero.
The `d=0` summands total `|A|`, giving

\[
\Lambda_4(B)=\frac{|A|}{p^2}=\frac\alpha p,
\qquad
\boxed{\frac\alpha p-\alpha^4=M+2\alpha T.}
\tag{3}
\]

No diagonal was subtracted or neglected. Before replacing the count,
the endpoint identity in (3) requires only invertibility of 2: the
potential endpoint pair when 3 is noninvertible occurs on both sides
of (2) and cancels. The assertion that *all* pair terms vanish does
require invertibility of 3 as well.

### 2.2 Complete mixed Cauchy–Schwarz proof

This proof allows arbitrary complex f and B. Let `a_B=E|B|^2`. The change
`y=x+d,z=x+2d`, inverse `x=2y-z,d=z-y`, gives

\[
M=\mathbb E_{y,z}B(y)B(z)K(y,z),\qquad
K(y,z)=f(2y-z)f(2z-y).
\]

First apply Cauchy–Schwarz in y:

\[
|M|^2\le a_B R,\qquad
R=\mathbb E_y\left|\mathbb E_zB(z)K(y,z)\right|^2.
\]

Expand the square, retaining all conjugations:

\[
R=\mathbb E_{z,z'}B(z)\overline{B(z')}C(z,z'),\quad
C(z,z')=\mathbb E_yK(y,z)\overline{K(y,z')}.
\]

A second Cauchy–Schwarz, now in the independent pair `(z,z')`, yields

\[
R^2\le
\bigl(\mathbb E_{z,z'}|B(z)|^2|B(z')|^2\bigr)
\mathbb E_{z,z'}|C(z,z')|^2=a_B^2 Q,
\]

where the nonnegative real number Q is

\[
Q=\mathbb E_{y,y',z,z'}K(y,z)\overline{K(y,z')}
                       \overline{K(y',z)}K(y',z').
\]

Hence `|M|^4 <= a_B^4 Q`. Put `y'=y+h,z'=z+k` and
`a=2y-z,c=2z-y`. The latter map has determinant 3, so a and c remain
independent and uniform. The eight factors are precisely

\[
\begin{aligned}
Q=\mathbb E_{a,c,h,k}&f(a)\overline{f(a-k)}\overline{f(a+2h)}f(a+2h-k)\\
 &\cdot f(c)\overline{f(c+2k)}\overline{f(c-h)}f(c-h+2k)\\
=\mathbb E_{h,k}&F_f(2h,-k)F_f(-h,2k).
\end{aligned}
\]

Cauchy–Schwarz, followed by the two invertible changes of variables
`(h,k)->(2h,-k)` and `(h,k)->(-h,2k)`, proves

\[
Q\le
\left(\mathbb E|F_f(2h,-k)|^2\right)^{1/2}
\left(\mathbb E|F_f(-h,2k)|^2\right)^{1/2}
=\|f\|_{U^3}^8.
\]

Therefore

\[
\boxed{|M|\le\|B\|_2^2\|f\|_{U^3}^2
               =\alpha\|f\|_{U^3}^2\quad(B=1_A).}
\tag{4}
\]

For clarity, the last cube identity expands as

\[
\begin{aligned}
\mathbb E_{h,k}|F_f(h,k)|^2
=\mathbb E_{x,h,k,w}&f_x\bar f_{x+h}\bar f_{x+k}f_{x+h+k}\\
 &\cdot\bar f_{x+w}f_{x+h+w}f_{x+k+w}\bar f_{x+h+k+w}.
\end{aligned}
\]

There are no unnormalized factors hidden in these changes of variables.
Reality, boundedness, balance, and AP-freeness were not used in (4).

### 2.3 Cubic Fourier estimate

Fourier expansion and the x,d orthogonality constraints give

\[
\begin{aligned}
T&=\sum_{r,s,t}\widehat f(r)\widehat f(s)\widehat f(t)
\mathbb E_xe_p((r+s+t)x)\mathbb E_de_p((s+2t)d)\\
 &=\sum_\xi\widehat f(\xi)^2\widehat f(-2\xi).
\end{aligned}
\]

Expanding the U² cube similarly forces all four Fourier frequencies to
coincide, so `||f||U2^4=sum_xi |fhat(xi)|^4`. Consequently

\[
\begin{aligned}
|T|&\le\sum_\xi|\widehat f(\xi)|^2|\widehat f(-2\xi)|\\
&\le\left(\sum_\xi|\widehat f(\xi)|^4\right)^{1/2}
      \left(\sum_\xi|\widehat f(-2\xi)|^2\right)^{1/2}\\
&=\|f\|_{U^2}^2\|f\|_2
=\sqrt{\alpha(1-\alpha)}\,\|f\|_{U^2}^2.
\end{aligned}
\tag{5}
\]

Only the bijection `xi->-2xi` is needed for the general complex-function
inequality. Boolean balance supplies `||f||2^2=alpha(1-alpha)`.

### 2.4 Independent monotonicity proof

Set `D_h f(x)=f(x) conjugate(f(x+h))`. Regrouping the cube gives

\[
\|f\|_{U^3}^8=\mathbb E_h\|D_hf\|_{U^2}^4
\ge\mathbb E_h|\mathbb E_xD_hf(x)|^4
\ge\left(\mathbb E_h|\mathbb E_xD_hf(x)|^2\right)^2
=\|f\|_{U^2}^8.
\tag{6}
\]

The first inequality retains the zero Fourier coefficient; the second
is scalar Cauchy–Schwarz. This proof works for arbitrary complex functions
on every finite abelian group.

### 2.5 Combination and constants

Write `b=alpha(1-alpha)`, `delta=||f||U3`. When `alpha^3>1/p`, (3)-(6) give

\[
\alpha(\alpha^3-p^{-1})\le
\alpha\delta^2+2\alpha\sqrt b\,\|f\|_{U^2}^2
\le\alpha(1+2\sqrt b)\delta^2.
\]

Thus the exact scalar output is

\[
\boxed{\delta^2\ge
\frac{\alpha^3-p^{-1}}{1+2\sqrt{\alpha(1-\alpha)}}.}
\tag{7}
\]

Equivalently, the density-dependent multiplicative constant in
`delta >= c(alpha,p) alpha^(3/2)` is

\[
c(\alpha,p)=
\sqrt{\frac{1-(p\alpha^3)^{-1}}{1+2\sqrt{\alpha(1-\alpha)}}}.
\]

Under `p alpha^3>=2`, this is at least
`[2(1+2 sqrt b)]^(-1/2) >= 1/2`. The constant 1/2 is the sharp output
of separately relaxing to `1-(p alpha^3)^(-1)>=1/2` and `b<=1/4`.
It is **not** asserted to be the optimal constant over actual AP-free
sets: simultaneous equality and prime/cardinality constraints were not
established. In the sparse regime the cutoff-only constant tends to
`1/sqrt(2)`; when also `p alpha^3 -> infinity`, it tends to 1.

### 2.6 Assumptions

| Assertion | Requirements |
|---|---|
| Single-f terms vanish | Mean zero |
| All pair terms vanish | Mean zero; 2 and 3 invertible |
| Cubic terms pair as T,T,U,U | Translation and reversal; identical scalar f |
| Endpoint identity before AP-free count | B=f+alpha, mean zero, 2 invertible |
| Count equals alpha/p | Indicator; no progression with nonzero difference |
| Mixed estimate with factor `||B||2²` | Arbitrary complex f,B; 2 and 3 invertible |
| Cubic estimate with factor `||f||2` | Arbitrary complex f; 2 invertible suffices |
| Variance equals alpha(1-alpha) | Centered indicator |
| U² <= U³ | Arbitrary complex f; any finite abelian group |

Primality is sufficient, not intrinsic. The argument extends to cyclic
groups of order coprime to 6, and to finite abelian groups where multiplication
by 2 and 3 are automorphisms, using no nonzero-difference APs and replacing
p by the group order. In that setting four terms with nonzero difference
are distinct. No hidden independent assumption that f is real is needed;
the specified centered indicator is of course real.

## 3. Best U³ exponent and counting optimization

The best **unconditional exponent proved here** is beta=3/2. No proof
that it is optimal among all uses of the exact identity is claimed.

The separate bounds cannot receive a uniform extra density factor.
First, Cauchy–Schwarz gives, with
`R(t)=E_x |f(x)|² |f(x+t)|²`,

\[
|F_f(h,k)|^2\le R(h+k)R(h-k),\qquad
\delta^8\le(\mathbb E|f|^2)^4=b^4.
\tag{8}
\]

The second inequality uses invertibility of `(h,k)->(h+k,h-k)`.
For the centered singleton, `alpha=1/p` and

\[
M=\alpha^2(1-\alpha)^2,
\qquad
1-\alpha\le\frac{M}{\alpha\delta^2}\le1.
\]

Thus coefficient 1 and density power 1 in (4) are asymptotically sharp,
even among centered AP-free indicators. Also `fhat(xi)=1/p` for nonzero
xi, so equality holds in (5). The singleton is below the density cutoff;
these facts do not rule out improvements exploiting that cutoff and signs.

There is a useful rigorous conditional improvement. If
`T <= -c alpha^3`, then (5) gives

\[
\delta\ge\sqrt c\,\alpha^{5/4}(1-\alpha)^{-1/4}.
\tag{9}
\]

In this branch the same Fourier expression gives a nonzero linear coefficient:

\[
|T|\le\max_{\xi\ne0}|\widehat f(\xi)|\sum_\xi|\widehat f(\xi)|^2,
\quad
\max_{\xi\ne0}|\widehat f(\xi)|
\ge\frac{c\alpha^2}{1-\alpha}.
\tag{10}
\]

This reaches density correlation exponent s=2 conditionally, not s<2.
If `p alpha^3>=2`, the exact identity supplies the following exhaustive
sign dichotomy: either `T<=-alpha^3/8`, or `M<=-alpha^4/4`.
The former implies (9)-(10) with c=1/8; in the latter the mixed term
can dominate while the cubic estimate gives no better exponent.

Booleanity also gives the exact derivative identity
`f²=(1-2alpha)f+b`. If `c(h)=E f(x)f(x+h)`, then

\[
\sum_\xi|\widehat{D_hf}(\xi)|^2
=\mathbb E_xf(x)^2f(x+h)^2
=b^2+(1-2\alpha)^2c(h).
\tag{11}
\]

Averaging h gives b², since `E_h c(h)=0`. This preserves density information
but does not by itself force a quadratic correlation. Positivity/compression
of the endpoint kernel on A recovers the same triple-count identity; no
stronger unconditional exponent was obtained from that rewrite.

## 4. Critical inverse exponent

For a **valid** correlation implication with exponent C, applying the
proved cutoff `delta>=alpha^(3/2)/2` would give s=(3/2)C. Thus

\[
\boxed{C_{\rm critical}=2/(3/2)=4/3.}
\]

This replaces the old alpha^4 starting point. It is an algebraic threshold,
not an existence theorem for such an inverse estimate. Section 6 proves
that the requested uniform power of the *actual norm* cannot meet it.
The density-calibrated alternative remains logically different.

## 5. All derivative Fourier mass retained; actual correlation obtained

For the rest of this section, denote variance by b and write

\[
D_h(\xi)=\widehat{f\,T_hf}(\xi),\qquad
Q(a,r)=\mathbb E_x f(x)e_p(-ax^2-rx),\quad
s_a(r)=|Q(a,r)|^2.
\]

Then `sum_r s_a(r)=b` for every a. Direct Fourier inversion gives

\[
r_a(h):=\sum_r s_a(r)e_p(-rh)
=e_p(ah^2)D_h(-2ah).
\tag{12}
\]

Define the unnormalized additive energy of the nonnegative spectrum by

\[
\mathcal E(s)=\sum_{r_1+r_2=r_3+r_4}
 s(r_1)s(r_2)s(r_3)s(r_4).
\]

Orthogonality says `E(s_a)=E_h |r_a(h)|^4`. For h nonzero, the map
`a->-2ah` covers every frequency once. At h=0, the coefficient is always b.
Thus, with `D_0^*=||f²||U2^4=b^4+(1-2alpha)^4 ||f||U2^4`,

\[
\boxed{\delta^8-\frac{D_0^*}{p}
=\sum_a\left(\mathcal E(s_a)-\frac{b^4}{p}\right).}
\tag{13}
\]

Every term in the sum is nonnegative, because the h=0 contribution to
`E_h|r_a(h)|^4` is b^4/p. This is an exact all-mass reformulation; no
derivative threshold or chosen frequency has been introduced.

It does not force a large individual Q(a,r). If `M_q=max |Q(a,r)|`,
the elementary estimate `E(s_a)<=M_q² b³` sums over p slopes. Applying
it to (13) incurs an explicit ambient factor p, not a density-only gain.

An unconditional finite-p lower bound follows from exact chirp moments:

\[
\sum_{a,r}|Q(a,r)|^2=pb,\qquad
\sum_{a,r}|Q(a,r)|^4=2b^2-\frac{b(1-3b)}p.
\tag{14}
\]

For the second identity, orthogonality imposes equality of the sums and
sums of squares of two pairs. In odd characteristic this says that the
two unordered pairs coincide. Counting the two orderings, subtracting the
all-equal double count, gives `2b²-E f⁴/p`; Booleanity gives
`E f⁴=b(1-3b)`. Therefore

\[
\boxed{M_q^2\ge\frac{2b}{p}-\frac{1-3b}{p^2}.}
\tag{15}
\]

This is ambient-dependent, of scale sqrt(alpha/p) in the sparse regime,
and supplies neither a density-only power nor a finite actual-norm
structured inverse exponent. Equations (9)-(10) provide the better
conditional linear branch. No nilcharacter or nilsequence correlation
theorem is asserted, and none is silently identified with a polynomial phase.

## 6. Exact remaining loss: a genuine obstruction, even in the cutoff regime

**Proposition.** For every fixed `0<C<2` and `c>0`, there are primes p
and cyclic 3-AP-free, hence 4-AP-free, sets A with `p alpha^3>=2` such that

\[
\sup_{\|\Psi\|_\infty\le1}|\mathbb E f\overline\Psi|
<c\|f\|_{U^3}^{C}.
\tag{16}
\]

In particular this rules out the requested actual-norm inverse bound with
`C<4/3`, for bounded polynomial phases, bounded nilcharacters, or any other
class of functions bounded by one. Allowing an unnormalized test function
would change the theorem and must track its amplitude cost.

### 6.1 A short independent proof of the U³ triangle inequality

This supplies the one norm fact used in the construction. U² is an l⁴ norm
of Fourier coefficients, so Minkowski gives its triangle inequality.
For arbitrary complex g,k, expansion and the change `y=x+h` give

\[
\mathbb E_h\|g\,\overline{T_hk}\|_{U^2}^4
=\mathbb E_{u,v}F_g(u,v)\overline{F_k(u,v)}
\le\|g\|_{U^3}^4\|k\|_{U^3}^4.
\]

Expand `(g+k) conjugate(T_h(g+k))` into its four terms. Apply the U²
triangle inequality, then Minkowski in `L_h^4`, and the preceding bound
to the two cross terms. Using the derivative identity gives

\[
\|g+k\|_{U^3}^2
\le\|g\|_{U^3}^2+2\|g\|_{U^3}\|k\|_{U^3}
   +\|k\|_{U^3}^2.
\]

Taking square roots proves the needed triangle inequality without invoking
a generic inverse theorem or generalized von Neumann estimate.

### 6.2 Explicit large AP-free sets in short intervals

Fix `2/3<theta<1`. For every sufficiently large prime p, put

\[
d=\lfloor\sqrt{\log p}\rfloor,\qquad
s=\left\lfloor p^{\theta/d}/2\right\rfloor,\qquad
m=(2s)^d=p^{\theta+o(1)}.
\]

Among vectors `v in {0,...,s-1}^d`, one level set of `sum_i v_i²` has
at least `s^d/[d(s-1)²+1]` elements. Encode this sphere in base 2s:

\[
A=\left\{\sum_{i=0}^{d-1}v_i(2s)^i:\ \sum_i v_i^2=R\right\}
\subset[0,m).
\]

An equation `a+c=2b` has no base-2s carries on either side, because each
digit is at most `2s-2`. Hence its vectors obey `u+w=2v`. Equal squared
norms then give `||u-w||²=0`, so the progression is trivial. Eventually
`2m<p`; any cyclic 3-AP equation among these integers lifts to the same
integer equation. Thus A is cyclic 3-AP-free.

With `lambda=m/p`, `rho=|A|/m`, and `alpha=lambda rho`, the pigeonhole
bound is

\[
\rho\ge\frac{2^{-d}}{d(s-1)^2+1}=p^{-o(1)},\qquad
\lambda=p^{\theta-1+o(1)},\qquad
p\alpha^3=p^{3\theta-2-o(1)}\longrightarrow\infty.
\tag{17}
\]

Thus this family is inside, not below, the requested density regime.

### 6.3 Norm lower bound versus the universal mass ceiling

Let `E(A)` be the unnormalized additive energy. Since `|A+A|<=2m`,
Cauchy–Schwarz on the representation counts gives

\[
\|B\|_{U^2}^4=\frac{E(A)}{p^3}
\ge\frac{|A|^4}{2mp^3}=\frac{\alpha^4}{2\lambda}.
\]

The nonnegative F_B(h,k) is supported on `(A-A)^2`, of relative size
at most `4 lambda²`. Its mean is `||B||U2^4`; its mean square is
`||B||U3^8`. Cauchy–Schwarz restricted to that support proves

\[
\|B\|_{U^3}^8
\ge\frac{\|B\|_{U^2}^8}{4\lambda^2}
\ge\frac{\alpha^8}{16\lambda^4}.
\]

The triangle inequality and the norm of the constant alpha now give

\[
\delta\ge\alpha\bigl((2\lambda)^{-1/2}-1\bigr)
\ge\frac{\alpha}{2\sqrt{2\lambda}}\quad(\lambda\le1/8).
\tag{18}
\]

But every bounded test function satisfies the exact ceiling

\[
|\mathbb E f\overline\Psi|\le\mathbb E|f|
=2\alpha(1-\alpha)\le2\alpha.
\tag{19}
\]

Combining (17)-(19), for every fixed C<2,

\[
\frac{\sup_{\|\Psi\|_\infty\le1}|\mathbb E f\overline\Psi|}{\delta^C}
\le2(2\sqrt2)^C\lambda^{1-C/2}\rho^{1-C}
=p^{-(1-\theta)(1-C/2)+o(1)}\longrightarrow0.
\]

This proves (16). The loss is real: the actual norm scales like a square
root of support fraction, whereas globally normalized correlation is
bounded by the support mass. It occurs before frequency selection,
coherence, integration, or nilsequence approximation.

There is an exact **unstructured benchmark** C=2: (8) and
`Psi=sign(f)` give `|<f,Psi>|=2b>=2 delta²`. Thus 2 is both sufficient
and necessary if every bounded test is allowed. The sign function is
not asserted to be structured. This does **not** prove a structured
inverse theorem with C=2, or identify the smallest achievable structured C.

The direct target `c alpha^(2-epsilon)` survives this obstruction. Indeed,
for these interval-supported examples, the nonzero linear frequency 1
already has correlation at least `alpha(1-2 pi lambda)`: subtracting the
constant changes no nonzero Fourier coefficient, and
`|e_p(-x)-1|<=2 pi m/p` on the support. Concentration is therefore a
case for a density-sensitive argument, not a counterexample to that target.

## 7. Complete exponent ledger

| Step / result | Quantitative statement | Status |
|---|---|---|
| Count deficit | `alpha^4-alpha/p` | Exact |
| Mixed estimate | `|M|<=alpha delta²` | Proved, coefficient/density factor uniformly sharp |
| Cubic estimate | `|T|<=sqrt(b) U2²` | Proved, coefficient sharp |
| U³ starting point | `delta>=alpha^(3/2)/2` in cutoff regime | Proved; beta=3/2 |
| Critical arithmetic | `s=(3/2)C`, so `Ccritical=4/3` | Conditional on a valid inverse theorem |
| Negative cubic branch | `delta ≳ alpha^(5/4)`, linear correlation `≳alpha²` | Conditional; s=2 |
| Full quadratic scan | `M_q²>=2b/p-(1-3b)/p²` | Proved; retains ambient p |
| Actual-norm obstruction | Any uniformly bounded test class requires `C>=2` | Proved even in cutoff regime |
| Unstructured benchmark | `sign(f)` gives `>=2 delta²` | Proved, not a structured result |
| Structured exponent C0 | No ambient-independent exponent established here | Do not relabel necessary C>=2 as an attained theorem |
| Density-sensitive target | Correlation `≳alpha^(2-epsilon)` | Still open in this work |
| Iterable increment and size | No valid `Delta alpha`, `N'/N` obtained | Not proved |

For the explicit family, writing `kappa=1-theta in (0,1/3)`, the ledger is
`alpha=p^(-kappa-o(1))`, `delta>=p^(-kappa/2-o(1))`, correlation ceiling
`p^(-kappa+o(1))`, and `p alpha³=p^(1-3kappa-o(1)) -> infinity`.

## 8. Iteration test

No correlation exponent s<2 was proved, so no actual global density-increment
theorem or full recurrence is asserted. Correlation alone supplies neither
a positive density increment nor an iterable progression length.

For comparison only, in the user's hypothetical model

\[
\alpha_{j+1}\ge\alpha_j+c\alpha_j^s,\qquad
\log(N_j/N_{j+1})\le K\alpha_j^{-t},
\]

with `s>=1,t>=0`, summing via density ranges gives total logarithmic loss
bounded on the scale of `integral_(alpha0)^1 alpha^(-s-t) d alpha`.
Writing `q=s+t-1`, this is `O(alpha0^-q)` for q>0 and
`O(log(1/alpha0))` when q=0. At `alpha0=epsilon/log N`, the q>0 budget
is `O(epsilon^-q (log N)^q)`. It guarantees o(log N) when q<1; at
q=1 an additional saving is needed. This calculation is a conditional
budget, not a lower bound ruling out every possible iteration.

Even an attained universal actual-norm exponent C=2 would yield only
the starting guarantee s=3 from beta=3/2. This would not meet the stated
budget with any nonnegative t. The conditional cubic branch has s=2;
even t=0 sits at the endpoint and gives no little-o guarantee.

Previously verified cyclic-to-interval increments also do not automatically
preserve cyclic AP-freeness on reuse; see `INCREMENT_ATTEMPT.md`. No missing
localization cost is assigned zero here.

## 9. Small finite counterexample tests

Commands:

```text
python3 verify_core.py
python3 verify_phase2.py > phase2_verification.json
```

The canonical verifier passed all 2,208 subsets in Z5,Z7,Z11, its atom
checks, and its 276 general spectral arrays. The Phase 2 verifier checks
all sixteen expansion terms and the three inequalities on those same
2,208 subsets, plus centered singletons in Z13,Z17. It also exhausts
7,776 pairs of real endpoints `f in {-1,0,1}^5` and Boolean middle functions.

A separate exact eligible example is

```text
p=101
A={0,20,22,25,30,32,33,34,37,38,39,48,49,52,53,54,
   58,59,78,79,81,84,88,90,93,94,95,97}
```

It has 28 elements, is 4-AP-free, and has
`p alpha³=21952/10201 > 2`. Its U³ inequality is checked with rational
arithmetic, not just a floating-point Fourier calculation. The report
also records a separately labelled numerical scan of all 10,201 polynomial
quadratics, numerical checks of the exact chirp moment identities to tolerance 1e-10, and the
all-derivative-mass identity residual. The complex mixed-CS identity is
checked separately with tolerance 1e-12.

Deliberate rejected extensions, verified exactly:

* Z3: `f=(1,1,0), B=1` gives `M=2/3`, `U3^8=8/81`, violating the mixed
  bound without the invertibility of 3.
* Z4: `f=(1,1,1,0), B=(1,0,1,1)` gives `M=1/2`, `E B=3/4`,
  `U3^8=41/256`, violating the same general extension.
* Z6: `f=(1,-1/6,-1/2,1/3,-1/2,-1/6)` has `T=5/54`,
  `||f||2²=5/18`, `U2^4=17/648`, so `T²>b U2^4`.
* Z5: `g=(1,1/2,1/2,1/2,1/2)` has `Lambda4(g)=7/50` and
  `U3^8=11/625`; therefore the stronger `|Lambda4(g)|<=U3(g)^4` fails.

The first three are outside the relevant ambient/function hypotheses;
none refutes (7). The centered singleton has the exact formula

\[
\delta^8=\alpha^4-8\alpha^5+28\alpha^6-44\alpha^7+23\alpha^8,
\]

corroborating the mixed sharpness calculation. Finite base-6 sphere and
interval-energy examples independently check the construction's arithmetic;
the asymptotic obstruction is proved in Section 6, not inferred from them.

## 10. Sharpest next sublemma

The next legitimate target must be density-sensitive. A precise unresolved
sublemma for the mixed branch is:

> There exist fixed epsilon>0 and c>0 such that, whenever A is 4-AP-free,
> p alpha³>=2, and T>−alpha³/8 (hence M<=−alpha⁴/4), some bounded
> quadratic object Psi has `|<f,Psi>|>=c alpha^(2-epsilon)`, with explicit
> complexity and localization bounds.

Polynomial quadratics and degree-2 nilcharacters must be distinguished in
any proposed proof. For the complementary cubic branch, (10) reaches only
alpha², so a subcritical improvement or an endpoint-saving iteration is
still required there as well. Solving the displayed sublemma alone would
not complete the program.

For an iteration, the eventual result must additionally state a *positive*
increment `Delta alpha(alpha)` and a preserved domain with size ratio
`N'/N`, and pass the logarithmic-loss calculation above. An unrestricted
actual-U³ inverse exponent below 4/3 is no longer a viable next sublemma.

## Durable checkpoint

Done: complete normalized proof of the alpha^(3/2) lemma; exact/complex
finite audits; sharp separate factors; conditional cubic improvement;
all-mass chirp identity; proof that actual-norm powers C<2 are impossible
even in the stipulated class and regime.

Skipped: network research, generic inverse theorems, BSG/Freiman frequency
selection, external publication, changes to the earlier verifiers.

Remaining: direct density-sensitive structured correlation with s<2 and
an explicitly localized, iterable positive density increment. Neither is
claimed proved. The full r4(N)=o(N/log N) conclusion is not established.
