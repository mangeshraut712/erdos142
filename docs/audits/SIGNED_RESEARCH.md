<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Signed mixed branch, localization, and endpoint bookkeeping

Date: 2026-09-06. Offline continuation of PHASE2_AUDIT.md.

STATUS: (D) OPEN

No proof or disproof of r_4(N)=o(N/log N) is established. The audited
alpha^(3/2) lemma is accepted as the checkpoint, not counted as new work.
This continuation proves signed operator/fiber identities, rules out two
tempting spectral/conditional shortcuts, and develops exact localization
bookkeeping. None forces a density-sensitive arithmetic correlation above
the alpha² endpoint from the stipulated signed hypotheses.

## 1. Executive verdict and retained information

The retained information is the **negative sign**, the two middle indicator
factors, the pointwise absence of completed progressions, and the fraction
of A's mass retained under restriction. No generic actual-U³ inverse theorem
is invoked.

Two main findings guide the next attempt:

* Every polynomial quadratic phase has a nonnegative Rayleigh quotient for
  the exact endpoint operator. A negative eigenvector cannot simply be
  identified with a quadratic phase. Negative spectrum alone is present
  for every proper set with at least two elements, even without AP-freeness.
* An alpha² increment would overcome the iteration endpoint if it retained
  all but O(alpha^u) of the set's mass, for some u>0. However, hostile review
  disproved the proposed universal integer-progression version. Affinely
  spread 3-AP-free sets give the counterexample in Section 9. The valid
  conditional bookkeeping is preserved separately from its false premise.

All claims below are labelled PROVED, CONDITIONAL, or FALSE as appropriate.
Auxiliary identities and conversions are not classified as a major
breakthrough or as a new asymptotic bound.

## 2. Exact signed Fourier representation — PROVED

Use E_x=p^-1 sum_x, fhat(xi)=E_x f(x)e_p(-xi x), B=1_A,
f=B-alpha, and b=alpha(1-alpha). Frequency sums are unnormalized.
Fourier expansion retains the two constraints

\[
\xi_0+\xi_1+\xi_2+\xi_3=0,\qquad
\xi_1+2\xi_2+3\xi_3=0.
\]

Consequently

\[
\begin{aligned}
M&=\sum_{\xi_0+\xi_1+\xi_2+\xi_3=0\atop
               \xi_1+2\xi_2+3\xi_3=0}
 \widehat f(\xi_0)\widehat B(\xi_1)
 \widehat B(\xi_2)\widehat f(\xi_3)\\
 &=\boxed{\sum_{r,s}\widehat f(r)\widehat B(s-2r)
                         \widehat B(r-2s)\widehat f(s).}
\tag{1}
\end{aligned}
\]

Indeed, choosing r=xi_0 and s=xi_3 forces xi_1=s-2r and xi_2=r-2s.
No phases or signs have been discarded. Reality also gives the equivalent
Hermitian expression

\[
M=\sum_{r,s}\overline{\widehat f(r)}\widehat f(s)
      \widehat B(2r+s)\widehat B(-r-2s).
\tag{2}
\]

The diagonal r=s contributes
`sum_r |fhat(r)|² |Bhat(3r)|² >= 0`. Thus negative M requires a negative
real total from the off-diagonal terms. This is signed interference, not
by itself a large coefficient or an additive-energy theorem. Replacing
the products by their magnitudes loses this information.

There is also an exact representation retaining all polynomial-quadratic
Fourier weights. Define `Q_g(a,r)=E_x g(x)e_p(-ax²-rx)`. Then

\[
\boxed{M=\sum_{a,r}|Q_f(a,r)|^2|Q_B(3a,3r)|^2
              -\alpha b+\frac{\alpha(1-\alpha)^2}{p}.}
\tag{2a}
\]

To prove it, expand the four Fourier factors in the positive sum.
Orthogonality imposes
`x-x'+3(y-y')=0` and `x²-x'²+3(y²-y'²)=0`, with overall factor p^-2.
The case y=y' forces x=x' and contributes alpha b. If y!=y', dividing
the second constraint using the first gives x+x'=y+y', hence
`x=2y'-y,x'=2y-y'`. Those terms are precisely the off-diagonal part of
M in middle-point coordinates. Its omitted diagonal is
`E_y B(y)f(y)²/p=alpha(1-alpha)²/p`. This proves (2a).

Negative M is therefore a deficit in this positive quadratic-spectrum
overlap relative to alpha b. Since alpha b has scale alpha² while the
stipulated deficit has scale alpha⁴, the identity alone has not forced
a large individual Q_f. It is not an inverse theorem.

## 3. Exact endpoint operator — PROVED

Let the inner product be `<g,h>=E_u conjugate(g(u))h(u)`. Define

\[
K(u,v)=B((2u+v)/3)B((u+2v)/3),\qquad
(Kg)(u)=\mathbb E_vK(u,v)g(v).
\]

Changing variables from `(x,d)` to `(u,v)=(x,x+3d)` gives
`M=<f,Kf>`. The normalized matrix has entries K(u,v)/p. Since the middle
points swap when u,v swap, K is real self-adjoint. The following identities
are exact:

\[
\operatorname{tr}K=\alpha,\quad
\|K\|_{HS}^2=\alpha^2,\quad
r(u):=(K1)(u)=\mathbb E_yB(y)B(2y-u),
\quad0\le r\le\alpha,\quad\mathbb Er=\alpha^2.
\tag{3}
\]

For the trace, K(u,u)=B(u). For the HS norm use K²=K entrywise and the
bijection `y=(2u+v)/3,z=(u+2v)/3`, inverse `u=2y-z,v=2z-y`.
It gives E_uv K(u,v)=alpha². The row formula follows by choosing y as
the first middle point. Cauchy–Schwarz with the nonnegative row weights
proves `||K||op<=alpha`: its square is bounded by
`E_u r(u) E_v K(u,v)|g(v)|² <= alpha² ||g||2²`.

In the orthonormal character basis,

\[
\boxed{\langle e_r,Ke_s\rangle
=\widehat B(2r+s)\widehat B(-r-2s)},\qquad
\widehat r(\xi)=\widehat B(2\xi)\widehat B(-\xi).
\tag{4}
\]

This follows by substituting u=2y-z,v=2z-y in
`E_uv K(u,v)e_p(sv-ru)`. In particular every linear character has
nonnegative Rayleigh quotient `|Bhat(3r)|²`.

Let P_A be multiplication by B. AP-freeness gives the stronger identity

\[
\boxed{P_AKP_A=p^{-1}P_A.}
\tag{5}
\]

For u,v in A, an off-diagonal nonzero kernel entry would complete the
nontrivial progression `u,(2u+v)/3,(u+2v)/3,v`. The only remaining matrix
entries are the diagonal entries B(u)/p. In particular every nonzero
function supported on A has positive K-Rayleigh quotient.

For mean-zero compression, write `Q=I-|1><1|` and `H=QKQ`. Then

\[
H=K-|1\rangle\langle r|-|r\rangle\langle1|
       +\alpha^2|1\rangle\langle1|,
\]

\[
\operatorname{tr}H=b,\qquad
\|H\|_{HS}^2=\alpha^2-2\|r\|_2^2+\alpha^4\le\alpha^2,
\qquad \langle f,Hf\rangle=M.
\tag{6}
\]

The HS formula also follows by writing K in blocks for
`span{1} direct_sum 1-perp`: the upper-left block is alpha² and the
off-diagonal vector is r-alpha². Subtract their squared HS contributions.
Furthermore `<B,K1>=Lambda_3(B)=alpha³+T`, so `<1,Kf>=T`.
The compression of K to the orthonormal pair `1,f/sqrt(b)` is exactly

\[
\begin{pmatrix}\alpha^2&T/\sqrt b\\T/\sqrt b&M/b\end{pmatrix}.
\tag{7}
\]

### Quantitative negative spectrum — PROVED, not arithmetic structure

Put gamma=-M>0. In a real orthonormal eigenbasis of H,

\[
\sum_{\lambda_j<0}|\lambda_j||\langle f,\phi_j\rangle|^2\ge\gamma.
\]

Since `||H||op<=alpha`, it follows that

\[
\|P_-f\|_2^2\ge\gamma/\alpha,
\qquad \lambda_{\min}(H)\le-\gamma/b.
\tag{8}
\]

Set tau=gamma/(2b). Negative modes above -tau contribute at most
tau||f||2²=gamma/2. Cauchy–Schwarz on the remaining modes gives

\[
\gamma/2\le
\left(\sum\lambda_j^2\right)^{1/2}
\left(\sum_{\lambda_j\le-\tau}|\langle f,\phi_j\rangle|^4\right)^{1/2}.
\]

The first factor is at most alpha. Also the sum of the squared overlaps
is at most b. Hence some eigenmode obeys

\[
\boxed{\lambda_j\le-\frac\gamma{2b},\qquad
|\langle f,\phi_j\rangle|\ge\frac\gamma{2\alpha\sqrt b}.}
\tag{9}
\]

For gamma>=c_0 alpha⁴ this is an eigenvalue of magnitude at least
`c_0 alpha³/[2(1-alpha)]` and L²-normalized overlap at least
`c_0 alpha^(5/2)/[2 sqrt(1-alpha)]`. This is not a bounded-phase correlation.
The eigenvalue equation only supplies

\[
\|\phi_j\|_\infty\le
\frac{\sqrt\alpha(1+\alpha)}{|\lambda_j|}.
\]

Indeed, for mean-zero phi, `H phi=K phi-<r,phi>1`,
`|K phi(u)|<=sqrt(r(u))<=sqrt(alpha)`, and
`|<r,phi>|<=||r||2<=alpha^(3/2)`. Rescaling to a bounded test therefore
gives only the guaranteed overlap

\[
\frac{\gamma^2}{4\alpha^{3/2}b^{3/2}(1+\alpha)}
\ge\frac{c_0^2\alpha^5}{4(1-\alpha)^{3/2}(1+\alpha)}.
\tag{10}
\]

No arithmetic description of this bounded function has been established.
The exponent 5 records this particular normalization route; it is not a
lower bound on the performance of every possible spectral argument.

### Quadratic-eigenmode shortcut — FALSE

For every polynomial quadratic q(x)=ax²+bx+c,

\[
q(2z-y)-q(2y-z)=3q(z)-3q(y).
\]

Applying the same middle-point substitution proves

\[
\boxed{\langle e_p(q),K e_p(q)\rangle
=|\mathbb E_xB(x)e_p(3q(x))|^2\ge0.}
\tag{11}
\]

Thus no negative K-eigenvector is a polynomial quadratic phase. This does
not prevent correlation with a phase: its positive and negative spectral
components can cancel. No statement here identifies a nilcharacter with a
polynomial phase.

### Negative spectrum as an AP-free signature — FALSE

In fact H has a negative eigenvalue for every proper A with 2<=|A|<p.
From 0<=r<=alpha and E r=alpha²,

\[
\|H\|_{HS}^2\ge\alpha^2-2\alpha^3+\alpha^4=b^2=(\operatorname{tr}H)^2.
\]

Equality would force r(u) in {0,alpha}. For u in A the summand y=u makes
r(u)>0, so equality would imply `2A-u=A` for every u in A. Two distinct
u,v then make A invariant under nonzero translation u-v, impossible for a
proper subset of Z_p. Thus the inequality is strict. A positive semidefinite
matrix has sum(lambda²)<=sum(lambda)², giving a contradiction. Signed M
adds **quantitative overlap with f**, not the mere existence of negativity.

## 4. Physical and conditional endpoint analysis — PROVED

Let

\[
q_d=\mathbb E_xB(x+d)B(x+2d)=\alpha^2+c_d,
\quad c_d=\mathbb E_xf(x)f(x+d),
\]

\[
t_d=\mathbb E_xB(x)B(x+d)B(x+2d)
    =\mathbb E_xB(x+d)B(x+2d)B(x+3d).
\]

The second equality is translation of x. Expanding the two endpoints,
and using AP-freeness for d!=0, gives

\[
\boxed{m_d=1_{d=0}\alpha-2\alpha t_d+\alpha^2q_d,\qquad
m_0=\alpha(1-\alpha)^2.}
\tag{12}
\]

In particular, if S=Lambda_3(B), the complete physical form is

\[
\boxed{M=\alpha/p-2\alpha S+\alpha^4.}
\tag{13}
\]

For d!=0, condition on
`S_d={x:B(x+d)B(x+2d)=1}` when q_d>0. Both endpoint marginals are
`r_d=t_d/q_d`. The forbidden product makes their joint probability zero.
Thus their complete binary distribution is

| Endpoints | Conditional probability |
|---|---:|
| (1,1) | 0 |
| (1,0) | r_d |
| (0,1) | r_d |
| (0,0) | 1-2r_d |

Consequently 0<=r_d<=1/2 and

\[
\boxed{m_d/q_d=\alpha^2-2\alpha r_d
=-r_d^2+(r_d-\alpha)^2.}
\tag{14}
\]

Negativity needs r_d>alpha/2, not r_d>alpha. The negative covariance can
therefore coexist with marginal densities below alpha.

### Popular negative fibers, with the diagonal retained — PROVED

Write

\[
Q_*:=\frac1p\sum_{d\ne0}q_d=\alpha^2-\alpha/p,
\qquad \mu(d)=q_d/(pQ_*),
\quad
\zeta=\frac{(1-\alpha)^2+c_0\alpha^2}{pQ_*}.
\]

Negative M implies Q_*>0. The exact identity

\[
M=\frac{\alpha(1-\alpha)^2}{p}
   +Q_*\bigl(\alpha^2-2\alpha\mathbb E_\mu r_d\bigr)
\]

and M<=-c_0 alpha⁴ give

\[
\boxed{\mathbb E_\mu r_d\ge[(1+c_0)\alpha+\zeta]/2.}
\tag{15}
\]

For `D={d!=0:q_d>0,r_d>=alpha/2}`, bounding r by alpha/2 outside D
and by 1/2 inside D yields

\[
\boxed{\mu(D)\ge\frac{c_0\alpha+\zeta}{1-\alpha}.}
\]

Moreover,

\[
0\le\mathbb E B(x)(1-B(x-d))(1-B(x+d))=\alpha-2q_d+t_d,
\]

and t_d<=q_d/2 imply q_d<=2alpha/3. Hence

\[
\boxed{|D|\ge\frac32\left(
\frac{c_0p\alpha^2}{1-\alpha}+\frac{1-\alpha}{\alpha}\right).}
\tag{16}
\]

This follows by `|D|>=3pQ_*mu(D)/(2alpha)` and substitution; an integer
ceiling is understood. For fibers with a uniform negative magnitude, set
`tau=(1+c_0/2)alpha/2`. The same calculation gives

\[
\mu\{r_d\ge\tau\}\ge
\frac{(c_0/2)\alpha+\zeta}{1-(1+c_0/2)\alpha},
\qquad m_d/q_d\le-(c_0/2)\alpha^2.
\tag{17}
\]

The denominators are positive whenever the hypothesis is feasible:
(15) and r_d<=1/2 imply
`p alpha²[1-(1+c_0)alpha]>=1-alpha`.

These are popularity statements, not arithmetic structure of D. Even an
increment on S_d would not be an iterable progression increment: S_d is
contained in a translate of A, hence is itself 4-AP-free and contains no
ordinary progression of length four.

### False fiber inferences and exact counterexamples

On Z_7, A={0,1,2,4}, every nonzero d has q_d=2/7,t_d=1/7,
r_d=1/2<alpha=4/7, but M=-108/2401. Thus negative M need not mean
an increased endpoint marginal. This example is below the cutoff.

The eligible Z_101 example has weighted nonzero-d endpoint marginal
`44/189 < 28/101=alpha`, yet M/alpha⁴=-9055/21952<-1/4. Thus failure
of an *averaged* conditional density increment occurs inside the cutoff.
This does not assert that every individual fiber has marginal below alpha.

On Z_13, A={7,8,10,11,12}, d=1 gives
`m_d=-55/2197<0` but unconditional endpoint correlation
`c_(3d)=1/169>0`. The conditioned sign cannot be transferred to the
unconditioned pair correlation.

## 5. Negative cubic branch — PROVED endpoint, no saving

Write `fhat(xi)=r_xi exp(i theta_xi)` and use reality. Exactly,

\[
T=\sum_{\xi\ne0}r_\xi^2r_{2\xi}
                  \cos(2\theta_\xi-\theta_{2\xi}).
\]

If T=-tau<0 and `w_xi=r_xi²/b`, then

\[
\mathbb E_w[-r_{2\xi}\cos(2\theta_\xi-\theta_{2\xi})]=\tau/b.
\]

Some phase edge therefore has the bracket at least tau/b. In particular

\[
\max_{\xi\ne0}|\widehat f(\xi)|\ge\tau/b
\ge c\alpha^2/(1-\alpha)\quad(T\le-c\alpha^3).
\tag{18}
\]

There is a phase-aware weighted statement. Set `R=max r_xi`,
`gamma=tau/b`, and let E consist of edges with the bracket at least gamma/2.
Bounding the bracket by R on E and gamma/2 outside it gives
`w(E)>=gamma/(2R-gamma)>=gamma/(2R)`.

No orbit-length assumption is used. There is no necessary phase conflict
around a multiplication-by-minus-two cycle: setting every nonzero phase
to pi makes every cubic summand negative, for every orbit length.

### A proposed saving from signed orbit algebra alone — FALSE

For sufficiently large primes p set the formal density parameter
`alpha=2p^(-1/3)`, `b=alpha(1-alpha)`, and
`r=sqrt(b/(p-1))`. Take Fourier data a_0=0 and a_xi=-r for xi!=0.
They have mean zero, Hermitian symmetry, variance b, and

\[
T=-(p-1)r^3=-br,\quad \max|a_\xi|=r,\quad p\alpha^3=8,
\]

\[
-T\sim\alpha^3/(2\sqrt2),\qquad
\max|a_\xi|\sim\alpha^2/(2\sqrt2).
\]

Thus neither alpha^(2-epsilon) nor alpha² log(1/alpha) follows from
these signed spectral constraints. The limitation is explicit: inverse
Fourier transform gives f(0)=-(p-1)r and f(x)=r otherwise, so these
data are unbounded and are not Boolean/AP-free indicators. They do not
disprove the desired special-set theorem. A successful orbit argument
must use additional realizability information.

The flat-spectrum example A={0,1,3,9} in Z_13 is correctly 3-AP-free:
its twelve ordered nonzero differences are distinct. It has
T=-12/2197 but p alpha³=64/169<2, so it is an out-of-cutoff diagnostic.

## 6. Concentration regularization — PROVED

Work now with true integer progressions in [N]; their index pullbacks
preserve integer 4-AP-freeness. For a restriction P define

\[
\lambda=|P|/N,\quad \kappa=|A\cap P|/|A|,
\quad\alpha'=|A\cap P|/|P|.
\]

Counting the same intersection in two ways gives

\[
\boxed{\lambda=\kappa\alpha/\alpha',\qquad
\log(N_0/N_k)=\log(\alpha_k/\alpha_0)
                 +\sum_{j<k}\log(1/\kappa_j).}
\tag{19}
\]

Whenever a true progression retains at least half the current A-mass and
doubles its density, restrict to it and pull back to its index interval.
There are at most log_2(1/alpha_0) such steps. Equation (19) implies

\[
\boxed{N_k\ge\alpha_0^2N_0.}
\tag{20}
\]

At termination, every nonempty integer progression P satisfies

\[
\boxed{\kappa(P)<\max\{1/2,2|P|/N_k\}.}
\tag{21}
\]

Otherwise both selection conditions hold. In particular any progression
of length at least N_k/4 has density below twice the current density.
At alpha_0=epsilon/log N, the logarithmic scale cost is at most
`2 log(log N/epsilon)=O(log log N)` for fixed epsilon.

This removes concentration retaining a substantial fraction of the mass.
It does not rule out many smaller concentrated components or prove a
stronger inverse theorem on the terminal set.

For any finite arithmetic partition, with cell weights mu_j and densities
alpha_j, its conditional variance v satisfies another useful exact fact:

\[
\boxed{\max_j\alpha_j\ge\alpha+v/\alpha,
\quad v=\sum_j\mu_j(\alpha_j-\alpha)^2.}
\tag{22}
\]

Indeed, `alpha²+v=sum mu_j alpha_j² <= (max alpha_j)alpha`.
Negative M has not been shown to force sufficient v on a partition of
controlled arithmetic complexity.

## 7. Sharp Fourier-to-Bohr-atom conversion — PROVED

Let Omega be any finite subset of the integers with uniform measure,
`f=1_A-alpha` relative to Omega, and
`|E_Omega f(x)e(theta x)|>=eta>0`. There is a translated semicircle atom

\[
P=\{x\in\Omega:(\theta x-t)\bmod1\in[0,1/2)\}
\]

with relative size mu and positive density gain Delta such that

\[
\boxed{\mu\Delta\ge\eta/2,\qquad
\Delta\ge\eta/2,\qquad
\mu\ge\eta/[2(1-\alpha)].}
\tag{23}
\]

This is a shifted rank-one Bohr atom of radius 1/4, intersected with Omega,
not a claimed long integer progression.

Proof: define
`H(t)=E_Omega f(x) 1_[0,1/2)((theta x-t) mod1)`.
It is real and H(t+1/2)=-H(t), apart from irrelevant boundary parameters.
Integration shows

\[
\left|\int_0^1H(t)e(t)dt\right|
=|\mathbb E_\Omega f(x)e(\theta x)|/\pi\ge\eta/\pi.
\]

Rotate this Fourier coefficient to be real. Since the integral of
`|cos(2pi t)|` is 2/pi,
`eta/pi <= (2/pi)||H||infinity`. Antisymmetry supplies a positive value
at least eta/2. At that value H(t)=mu Delta. Finally Delta<=1-alpha.
The constant 1/2 is sharp for Omega={0,1}, A={0}, theta=1/2.

### Joint gain/size amortization — CONDITIONAL

Suppose a reusable theorem supplied eta>=c alpha^r, 0<c<=1,r>1,
relative to every resulting atom. Then mu Delta >=(c/2)alpha^r and

\[
\log(1/\mu)\le\frac{2\Delta}{c\alpha^r}
                  \mu\log(1/\mu)
\le\frac{2\Delta}{ec\alpha^r}.
\]

In a starting-density band [a,2a), internal steps have total Delta at
most a. One crossing step has mu>=(c/2)a^r, since Delta<=1. Therefore
that band's scale loss is at most

\[
\left[2/(ec)+\log(2/c)+r/(e(r-1))\right]a^{1-r}.
\]

Here `log(1/a)<=a^(1-r)/(e(r-1))`. Summing dyadic bands gives

\[
\boxed{\sum_j\log(1/\mu_j)\le K(c,r)\alpha_0^{1-r},\quad
K(c,r)=\frac{2/(ec)+\log(2/c)+r/[e(r-1)]}{1-2^{1-r}}.}
\tag{24}
\]

The number of new frequencies is also O(alpha_0^(1-r)), by counting
steps in each band using Delta>=c alpha^r/2. Thus r<2 passes the scale
test, while r=2 is still the endpoint. No reusable signal theorem on
these intersections of atoms, or final AP contradiction inside them, is
proved. Their growing rank cannot be omitted.

## 8. Interval-native progression conversion — PROVED, too costly

If `|E_[N](1_A-alpha)e(theta x)|>=eta` and
`N>=(128pi)² alpha/eta`, there is a true integer progression P with

\[
\boxed{|P|\ge\frac1{128\pi}\sqrt{\frac{\eta N}{\alpha}},\qquad
\operatorname{dens}_P(A)\ge\alpha+3\eta/8,}
\tag{25}
\]

whose step is at most sqrt(alpha N/eta).

Proof: set Q=floor(sqrt(alpha N/eta)),
L=floor(eta Q/(32pi alpha)). Pigeonhole the Q+1 points
0,theta,...,Qtheta into Q circular bins to obtain 1<=q<=Q with
`||q theta||<=1/Q`. Partition each residue chain modulo q into blocks
of lengths between L and 2L-1. Each chain is long enough: its length is
at least floor(N/Q), whereas `N/Q>=eta Q/alpha>=32pi L`.
On a block, chordal phase oscillation is at most `4pi L/Q<=eta/(8alpha)`.
Replacing the phase by a block constant costs at most
`eta/(8alpha) E|f|<=eta/4`. If m_P is the block mean, then
`sum_P (|P|/N)|m_P|>=3eta/4`. Their weighted signed sum is zero;
some block therefore has mean at least 3eta/8. The hypothesis ensures
both floors lose at most a factor 2, giving the stated length.

The actual logarithmic scale loss is

\[
\boxed{\log(N/|P|)\le\tfrac12\log N+
        \tfrac12\log(\alpha/\eta)+\log(128\pi).}
\tag{26}
\]

The term (1/2)log N cannot be called t=0. When eta is alpha^r,
the guaranteed recurrence has length only a constant times
`alpha^((r-1)/2) sqrt(N)` per step.

The square-root loss is real for generic single-phase flattening. Let
theta=(sqrt(5)-1)/2. If m is nearest to q theta, its conjugate root
theta'=(-sqrt(5)-1)/2 gives
`(q theta-m)(q theta'-m)=m²+qm-q²`, a nonzero integer. Also
`|q theta'-m|<=sqrt(5)q+1/2<3q`, so `||q theta||>=1/(3q)`.
If all phases on an L-term step-q progression fit in an arc of length
rho<=1/4, lift them into that arc. Consecutive lifted differences must
be the same representative of q theta, so `(L-1)||q theta||<=rho`.
Together with `(L-1)q<=N-1`, this gives

\[
\boxed{L\le1+\sqrt{3\rho(N-1)}.}
\tag{27}
\]

This obstructs this conversion method, not every possible direct increment.

## 9. Mass-retaining endpoint proposal — FALSE; conditional budget preserved

The following was proposed as a sufficient sublemma. **It is false.** Its
conditional implication is correct, but the counterexample below defeats
the premise. It must not be reused as an established or viable universal
increment theorem.

> There are fixed c,C,u,K>0 and N_0 such that every integer 4-AP-free
> A subset [N] with 0<alpha<=4/5, N>=max(N_0,alpha^(-K)), satisfying
> the terminal concentration condition (21), admits a true integer
> progression P with density alpha'>=alpha+c alpha² and mass retention
> kappa>=exp(-C alpha^u).

Here is the complete conditional calculation that motivated the proposal;
the subsequent counterexample does not invalidate this implication.

Alternate concentration steps from Section 6 with the hypothetical steps.
Density is increasing. All concentration steps together double density
at most log_2(1/alpha_0) times, so their total log mass loss is at most
log(1/alpha_0). In a dyadic band [a,2a), the hypothetical steps have
at most `1/(ca)+1` starting points, and each costs at most `C(2a)^u`
in log mass. Summing bands and then using (19) gives total log length loss

\[
R(\alpha_0)=
\begin{cases}
O(\log(1/\alpha_0)+\alpha_0^{u-1}),&0<u<1,\\
O(\log(1/\alpha_0)),&u\ge1.
\end{cases}
\tag{28}
\]

All implied constants depend only on the fixed sublemma constants. For
alpha_0>=epsilon/log N with N the initial length and fixed epsilon>0,
this is o(log N).
Thus all intermediate lengths remain `N exp(-o(log N))`, which eventually
exceeds both the fixed threshold N_0 and alpha_0^(-K). Since alpha only
increases, the sublemma's length condition persists.

The increments cannot continue indefinitely below 4/5: their number is
finite, bounded by dyadic summation of O(1/alpha_0). Hence eventually
alpha>4/5 while the interval length tends to infinity. But partitioning
an integer interval into disjoint blocks of length four shows any 4-AP-free
set has size at most `3 floor(N/4)+(N mod4)<=3N/4+3/4`. Its density is
less than 4/5 for N>15. This is the required contradiction.

This is a complete conditional implication. The premise, however, is false.

### Counterexample to the proposed premise — PROVED

There are cyclic 3-AP-free sets A_0 subset Z_p with alpha->0 and
alpha=p^(-o(1)). For a self-contained construction put
`d=floor(sqrt(log p))`, `s=floor((p/4)^(1/d)/2)`, choose the largest
sphere `sum_i v_i²=R` in `{0,...,s-1}^d`, and encode it in base 2s.
It lies in `[0,(2s)^d)` with `(2s)^d<=p/4`. No carries occur in a 3AP
equation; equal norms force its three vectors to coincide. Cyclic equations
lift to integer ones because the containing interval has length at most p/4.
Its cardinality n satisfies

\[
\frac{s^d}{d(s-1)^2+1}\le n\le s^d\le\frac{p}{4\,2^d}.
\]

Since `s>=(p/4)^(1/d)/4` for large p, `log(p/n)=O(sqrt(log p))`,
while the upper bound makes alpha=n/p tend to zero. In particular
`p>=alpha^(-K)` for every fixed K eventually, and `p alpha³->infinity`.

Choose a uniformly random affine image A=aA_0+b, with a!=0, and represent
it in the integer interval [1,p]. For `X_x=1_A(x)-alpha`, affine
two-transitivity gives the following moments. Explicitly, for distinct
x,y and any distinct u,v in A_0 there is a unique affine map sending
u,v to x,y. Thus `Pr(x,y in A)=n(n-1)/(p(p-1))`, while each single
membership probability is alpha. Subtraction gives

\[
\mathbb EX_x=0,\quad \mathbb EX_x^2=\alpha(1-\alpha),\quad
\mathbb EX_xX_y=-\alpha(1-\alpha)/(p-1)\quad(x\ne y).
\]

Thus every fixed L-point block has sum variance

\[
\mathbb E\left|\sum X_x\right|^2
=\alpha(1-\alpha)\frac{L(p-L)}{p-1}\le\alpha L.
\tag{28a}
\]

Set `h=1+ceil(log_2 p)`, `Q=ceil(4/alpha)`. Fix an integer step q<=Q
and one residue chain modulo q in [1,p], of length L. Pad its variables
with zeros to the next power of two. Every prefix is the union of at most
h dyadic blocks, so Cauchy–Schwarz gives

\[
\max_{\text{prefix}}\left|\sum X_x\right|^2
\le h\sum_{\text{all dyadic blocks}}\left|\sum X_x\right|^2.
\]

At each tree level, (28a) bounds the expectation of the block-square sum
by alpha L. There are at most h levels. Every segment is a difference
of two prefixes, hence the expected maximal segment-square is at most
`4h² alpha L`. Summing over residue chains and then steps bounds the
maximum discrepancy D_Q over all these progressions by

\[
\mathbb E D_Q^2\le4h^2\alpha pQ\le20h^2p.
\]

Therefore some affine image satisfies `D_Q<=sqrt(20) h sqrt(p)`.
If a true integer progression retains half the mass of this A, its length
L is at least alpha p/2. Eventually L>=2 and its step is at most
`(p-1)/(L-1)<=4/alpha`. It is among the progressions just controlled, so

\[
\boxed{|\operatorname{dens}_P(A)-\alpha|
\le\frac{2\sqrt{20}\,h}{\alpha\sqrt p}
=o(\alpha^R)\quad\text{for every fixed }R>0.}
\tag{28b}
\]

These A are terminal under the concentration rule: every half-mass
progression has density less than 2alpha. For any proposed fixed C,u>0,
`exp(-C alpha^u)>=1/2` eventually, so any progression meeting the proposed
retention requirement falls under (28b). Its gain is smaller than c alpha²
for every fixed c>0 eventually. All polynomial length thresholds in the
proposal hold. This proves that the proposed sublemma is false, even for
sets satisfying the original cyclic density cutoff.

The examples lie in Branch I:
`T=alpha/p-alpha³<=-alpha³/2` eventually. Their mixed form is
`M=alpha/p-2alpha²/p+alpha⁴>0` for alpha<1/2. Thus this does not refute
a mass-retention theorem restricted only to Branch II. Nor does it refute
the ultimate problem: `alpha log p -> 0`, since alpha<=1/(4·2^d).
A version explicitly restricted to
the logarithmic density regime would be a different, unproved claim.

The obstruction is to **true integer progressions retaining much of the
mass**. A cyclic progression with an arbitrary invertible step can undo
the affine scrambling; it cannot be silently substituted for the true
integer progression required by the failed iterative lemma.

## 10. Exponent ledger and increment parameters

| Statement | Gain / signal | Scale or normalization cost | Conclusion |
|---|---|---|---|
| Signed mixed | -M>=c_0 alpha⁴ | Exact | Input |
| Negative eigenvalue | magnitude >=c alpha³ | L² operator | Not a quadratic object |
| Eigenmode overlap | >=c alpha^(5/2) | L²-normalized | Not bounded correlation |
| Bounded eigenmode route | >=c alpha^5 | No arithmetic complexity bound | Insufficient |
| Popular signed fibers | weighted mass >=c alpha; number >=c p alpha² | S_d irregular and AP-free | No density gain over alpha |
| Negative cubic | eta>=c alpha² | Global linear Fourier signal | Endpoint only |
| Bohr atom | Delta>=eta/2; mu Delta>=eta/2 | Rank +1; radius 1/4; previous ambient intersection | Repeatability missing |
| Hypothetical eta>=c alpha^r atoms | s=r | Amortized O(alpha_0^(1-r)); rank same order | r<2 passes, r=2 endpoint |
| Native progression from eta | Delta>=3eta/8 | N'/N>=(128pi)^(-1)sqrt(eta/(alpha N)) | Contains (1/2)log N loss |
| Concentration doubling | alpha'>=2alpha | kappa>=1/2; global N_final>=alpha_0²N | Cheap regularization only |
| Proposed universal mass-retaining step | s=2 | kappa>=exp(-C alpha^u), u>0 | Budget (28) passes, but premise is FALSE by (28b) |

For a separate power-model increment `Delta>=c alpha^s` and
`log(N/N')<=C alpha^-t`, q=s+t-1 remains the criterion. The present
cubic signal with a reusable constant-cost conversion would only give
s=2,t=0,q=1. The genuine native conversion has an ambient log N term,
so it has no justified fixed t in that model. Equation (28) instead uses
the exact gain/mass relation and is a demonstrably stronger conditional
iteration scheme.

## 11. Full iteration test at alpha=epsilon/log N

* Concentration regularization alone: loss <=2 log(log N/epsilon)=o(log N),
  but no contradiction on its terminal set.
* Repeatable Bohr atom signal alpha²: even the improved joint estimate
  gives O(alpha_0^-1)=O(epsilon^-1 log N), not o(log N). The repeatable
  signal premise is itself missing.
* Native progression conversion at eta~alpha²: each guaranteed length is
  only a constant times sqrt(alpha N); repeatedly applying this guarantee
  approximately halves log N. It does not provide the required budget.
* Proposed near-full mass retention: equation (28) would be o(log N),
  but the universal integer-progression premise is false by (28b).
* Actual result: no proved repeatable signed-branch increment passes the
  test. Neither a proof nor a counterexample to the ultimate target follows.

## 12. Adversarial finite checks

Commands run:

```text
python3 verification/scripts/verify_core.py
python3 verification/scripts/verify_signed.py > verification/results/signed_verification.json
```

The canonical verifier passed its 2,208 subset tests and retained all
previous counterexamples. The signed verifier independently checks:

* all 10,400 subsets of Z5,Z7,Z11,Z13;
* 2,647 nonempty 4-AP-free subsets, including 244 satisfying M<=-alpha⁴/4;
* the exact strict HS criterion for 10,356 proper sets of size at least two;
* exact fiber identities, diagonal, AP-free compression, popularity bounds;
* 7,028 translated-semicircle localization cases, with exact rational
  gain/size products and numerical Fourier tolerance 1e-12;
* 1,012 finite concentration-regularization runs and exact telescoping;
* 2,150 exact relative-window identities for A subset Omega in Z5,Z7;
* exact affine-image covariance/discrepancy checks over 42 images in Z7
  and 156 images in Z13; these support, but do not replace, the asymptotic
  affine-spreading proof;
* numerical signed Fourier and quadratic Rayleigh identities, tolerance
  1e-10, including all polynomial quadratics for the small named examples;
* an independently calculated small symmetric-matrix spectrum (Jacobi
  rotations), explicitly numerical and separate from the exact proofs.

The eligible example from Phase 2 has p=101, |A|=28,
`p alpha³=21952/10201>2`, 204 ordered 3APs including the diagonal,
`T/alpha³=-337/5488>-1/8`, and `M/alpha⁴=-9055/21952<-1/4`.
It is genuinely in the mixed branch. Its popular set D has 78 differences;
the exact lower bound in (16), with c_0=1/4, is 32451/4088.

For p=7,A={0,1,2,4}, the numerical minimum eigenvalues are approximately
-0.223079 for K and -0.216156 for H; their negativity already follows
exactly from M=-108/2401 and b=12/49. Every polynomial quadratic still
has the nonnegative Rayleigh quotient (11).

Small exhaustive cases cover empty/full sets, singletons, dense sets near
one half, intervals, flat spectra, and missing conditional atoms. The
concentrated-support family remains governed by the accepted Phase 2 proof;
it is not rerun or claimed excluded by small finite tests. The scalar
orbit obstruction explicitly identifies its failed Boolean/bounded
hypotheses. No conclusion depends on assuming a large order of -2.

## 13. Transfer between Z_p and integer intervals — PROVED limits

One-time transfer of a completed cyclic upper bound is valid. If
`p>2(N-1)`, any four representatives in [N] forming a cyclic progression
satisfy two second-difference congruences whose absolute values are less
than p. They are therefore zero as integers. Thus an integer 4-AP-free
set stays cyclic 4-AP-free under this embedding.

For completeness, a prime with `2N<p<4N` exists for all sufficiently large
N by the following elementary argument, with no cited prime-distribution
theorem. Let P(m) be the product of primes <=m. Induction gives P(m)<=4^m.
For odd m=2k+1, primes in (k+1,2k+1] divide binomial(2k+1,k), which is
at most 2^(2k); multiply by P(k+1)<=4^(k+1). Even m>2 is composite,
so reduce to m-1. The small bases are immediate.

If there were no prime in (n,2n), then

\[
\frac{4^n}{2n+1}\le {2n\choose n}
\le(2n)^{\sqrt{2n}}4^{2n/3}.
\]

For the upper bound, each prime <=sqrt(2n) contributes a power at most
2n: in its factorial valuation, each power contributes 0 or 1. Larger
primes appear at most once. Primes in (2n/3,n] have valuation zero;
the rest contribute at most P(floor(2n/3)). The assumed empty interval
(n,2n) removes the remaining primes. The inequality is impossible for
sufficiently large n because its logarithm has a positive linear term
on the left versus O(sqrt(n)log n) on the right. Take n=2N.

Consequently a cyclic o(p/log p) theorem would imply the target on [N].
If |A|>=epsilon N/log N, its cyclic density for such p is at least
epsilon/(4 log p), so the fixed-epsilon formulation also transfers.

Repeated reembedding is a separate problem. An interval density a becomes
alpha=aN/p<a/2 for p>2N. This erases an additive alpha² gain. Moreover,
for nonzero cyclic frequency xi,

\[
\widehat{(B-\alpha)}_{\mathbb Z_p}(\xi)
=\frac Np\left[
\mathbb E_{[N]}(B-a)e_p(-\xi x)
+a\mathbb E_{[N]}e_p(-\xi x)\right].
\tag{29}
\]

The interval cutoff can supply the entire coefficient. A cyclic-balanced
signal does not automatically become an interval-balanced signal.
For a general local ambient W, expanding B=alpha 1_W+g produces weighted
single and pair terms that do not vanish merely from E_W g=0. A usable
relative counting identity with quantified errors is still missing.

## 14. Sharpest remaining sublemma

The remaining target must permit arithmetic localizations beyond the
false half-mass integer-progression mechanism. A repeatable relative
Bohr/progression signal alpha^(2-epsilon), with all rank/radius and
terminal-counting costs controlled, remains unproved. So does a
mixed-branch-only mass-retention statement, which would still leave
Branch I unresolved.

Here is the exact relative identity that a localized argument must retain.
Let W=1_Omega, w=|Omega|/p, A subset Omega, a=|A|/|Omega|, and
g=B-aW. Define

\[
\Phi_W=\Lambda(W,B,B,W),\qquad
\Sigma_W=\Lambda(B,B,B,W)=\Lambda(W,B,B,B).
\]

Reversal gives the equality defining Sigma_W. Expanding the endpoints
and retaining the AP-free diagonal gives the exact formula

\[
\boxed{\Lambda(g,B,B,g)=aw/p-2a\Sigma_W+a^2\Phi_W.}
\tag{30}
\]

The needed sublemma must control these window-dependent quantities, or
turn their failure of expected behavior into a positive density increment.
Neither Phi_W nor Sigma_W may be replaced by a global density power:
relative balancing does not make the weighted pair and triple terms vanish.
The quadratic Rayleigh formula (11) likewise must not be assumed unchanged
after restricting both endpoints to W.

The signed arithmetic input still to exploit is (2) together with (5):
off-diagonal Fourier interference plus exact exclusion of A-to-A edges.
The needed output is a positive density gain on an arithmetic domain that
retains almost all mass, or a genuinely stronger correlation with a
controlled reusable domain. The present spectral level sets and S_d
fibers do not meet that requirement.

## 15. Next research prompt

> Work offline from SIGNED_RESEARCH.md. Accept all audited identities and
> the new affine-spreading counterexample to Section 9. Do not revive a
> universal near-full-mass increment on true integer progressions. Starting
> from the relative identity (30), investigate controlled Bohr/window
> ambients while retaining Phi_W, Sigma_W, the diagonal, and discarded
> mass. Derive a repeatable positive increment from signed mixed
> interference, or an alpha^(2-epsilon) relative signal with explicit rank,
> radius, and terminal-counting bounds. Treat the cubic branch separately:
> the affine-spreading counterexamples lie there. Test every proposed
> localization theorem on that family and on the p=101 mixed witness.
> Neither negative eigenvalue existence nor polynomial-phase identification
> is an acceptable structural step. Prove the full iteration or isolate
> the exact unsatisfied quantitative premise.

## Durable checkpoint

Done: exact signed Fourier/operator/fiber analysis, popular negative fibers,
quadratic Rayleigh obstruction, generic-negative-spectrum diagnosis,
phase-aware cubic endpoint analysis, concentration regularization, sharp
semicircle gain-size conversion, native progression cost, the conditional
mass-retention budget and its counterexample, exact relative-window
identity, and elementary interval transfer.

Skipped: internet and literature lookup, generic inverse machinery, public
posting, claims of novelty, or relabelling auxiliary diagnostics as a
solution. Earlier proof and verification files are preserved.

Remaining: derive a sufficient density-sensitive arithmetic increment from
the signed hypotheses. The status remains OPEN.
