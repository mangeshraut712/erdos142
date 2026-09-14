# Relative windows and the cubic-branch iteration

Date: 2026-09-06. Offline continuation of SIGNED_RESEARCH.md.

STATUS: (C) NEW RIGOROUS PARTIAL RESULT

The new result is a relative counting decomposition on an explicitly
hereditary class of linear-coordinate windows, with a quantified density
increment for pair-count irregularity. There is also a repeatable
constant-cost reduction for large relative linear Fourier signals.
Neither result closes the low-signal cubic case or the relative signed
mixed case. The target r_4(N)=o(N/log N) is not proved or disproved.
No claim of novelty relative to literature is made; this was an offline
derivation and audit. Idle time during interruption was not research time.

## 1. Executive verdict

The exact relative identity can be turned into a controlled three-way
statement. A window-count irregularity produces a real, quantified
same-rank increment; a weighted triple deficit produces a relative linear
signal with explicit window cost; otherwise the negative mixed form
survives, with the diagonal bounded explicitly.

The missing step is now narrower: the low-signal alternative costs rank,
and the negative mixed alternative still lacks an arithmetic increment.
These are not technical cleanup. The exact iteration below fails to
establish the ultimate bound unless they are improved.

## 2. What was attacked

Independent lanes treated:

1. exact window counts, random baselines, and local quadratic spectra;
2. normalized window operators, fibers, geometric refinements, and
   terminal counting;
3. optimized single-frequency conversion, safe reembedding, convolution
   clipping/smoothing, and the full cubic recurrence.

The main derivation combined the geometric refinement with an interval
prefix-discrepancy argument, and removed the ambient logarithm from the
interval Fourier estimate by an explicitly bounded smoothing step.
Promising statements were independently reviewed and checked against
exact finite counts. The previous U³ lemma was not reproved.

## 3. Definitions and exact relative baseline

Let p>3 be prime. All ambient averages are p^-1 sums and frequency sums
are unnormalized. Let Omega be nonempty, W=1_Omega, n=|Omega|=wp,
A subset Omega, B=1_A, a=|A|/n, and g=B-aW. Set

\[
C=\Lambda_4(W),\quad
\Phi=\Lambda(W,B,B,W),\quad
\Sigma=\Lambda(B,B,B,W)=\Lambda(W,B,B,B),\quad
\mathcal M=\Lambda(g,B,B,g).
\]

For 4-AP-free A, the accepted endpoint expansion reads

\[
\boxed{\mathcal M=aw/p-2a\Sigma+a^2\Phi.}\tag{1}
\]

The diagonal is aw/p, not a/p. The shape-dependent reference values
are a²C and a³C, not powers of the global density alone.

For independent Bernoulli selection with fixed parameter a inside Omega,
write R=C-w/p. Distinct positions are independent for d!=0, giving

\[
\mathbb E\Phi=a^2R+aw/p,\quad
\mathbb E\Sigma=a^3R+aw/p,\quad
\mathbb E\Lambda_4(B)=a^4R+aw/p,\quad
\mathbb E\mathcal M=a(1-a)^2w/p.\tag{2}
\]

Here g is balanced only in expectation. For exact size k=an, let
rho_j=(k)_j/(n)_j. Uniform fixed-size sampling instead gives, for n>=4,

\[
\mathbb E\Phi=\rho_2R+aw/p,\quad
\mathbb E\Sigma=\rho_3R+aw/p,
\]
\[
\mathbb E\mathcal M=H_4R+a(1-a)^2w/p,\quad
H_4=\rho_4-2a\rho_3+a^2\rho_2
=\frac{\rho_2(1-a)[6(1-a)-an]}{(n-2)(n-3)}.\tag{3}
\]

These follow by assigning rho_j to j distinct sampled points. Their
finite-population correction must not be silently replaced by zero.

## 4. The controlled window class and exact geometry — PROVED

Fix nonzero frequencies xi_1,...,xi_d. For each coordinate choose a
consecutive integer interval I_j=[l_j,u_j] with diameter u_j-l_j<p/3.
Define

\[
\Omega=\{x\in\mathbb Z_p:\text{the residue }\xi_jx
\text{ has an integer lift }t_j(x)\in I_j\text{ for every }j\}.
\tag{4}
\]

The lift is unique. These are intersections of shifted narrow linear
Bohr-coordinate intervals. No regular-radius assumption is needed.
Their parameters are d, the frequencies, the endpoints of I_j, and n.

For u,v in Omega, both middle points of the endpoint progression belong
to Omega if and only if

\[
(t_1(u),\ldots,t_d(u))\equiv
(t_1(v),\ldots,t_d(v))\pmod3.\tag{5}
\]

Proof: if a middle point lies in Omega, its coordinate equation modulo p
has discrepancy at most three times the coordinate diameter, hence less
than p. It is an integer equality. The two endpoint lifts must have the
same residue modulo3. Conversely, equal residues make their two convex
averages integers inside I_j. Invertibility of3 identifies them with the
actual middle coordinates in Z_p. This holds simultaneously in all d
coordinates.

Let Omega_l be the nonempty label classes from (5), of sizes n_l. There
are at most3^d. The normalized endpoint window operator
L_W=P_WK_WP_W therefore has a kernel equal to one exactly inside these
blocks and zero between them. Consequently

\[
\boxed{L_W\succeq0,\quad\operatorname{rank}L_W\le3^d,\quad
C=\sum_l(n_l/p)^2\ge w^2/3^d.}\tag{6}
\]

Its nonzero eigenvalues are n_l/p. For a real h supported on Omega,

\[
\langle h,L_Wh\rangle_p
=p^{-2}\sum_l\left(\sum_{x\in\Omega_l}h(x)\right)^2.\tag{7}
\]

For an N-point rectified interval, the classes are the three ordinary
residue classes modulo3, and

\[
\boxed{C=\lceil N^2/3\rceil/p^2.}\tag{8}
\]

Each label class can itself be rectified by x=x_0+3z, with x_0 in that
class, into a window of the same rank whose lifted coordinate diameters
are at most one third as large. This is a geometric assertion, not
permission to reuse a negative block: its middle A-values may lie in
other label classes and would be discarded on restriction.

## 5. Pair-count irregularity forces a controlled increment — PROVED

Define the middle-point completion kernel

\[
R_W(y,z)=W(2y-z)W(2z-y),\qquad y,z\in\Omega.
\]

Each row is the intersection of d coordinate intervals in z. In coordinate
j the allowed lift of z lies in the intersection of I_j with
`[2t_j(y)-u_j,2t_j(y)-l_j]` and
`[(l_j+t_j(y))/2,(u_j+t_j(y))/2]`. The no-wrap argument is the same
as in Section4.

Choose an integer K<=n. Partition each coordinate interval into K
contiguous quantile bins under uniform counting on Omega. Nonzero
frequencies are injective, so no coordinate ties prevent bins of mass at
most ceil(n/K). Their common refinement has at most K^d nonempty cells.
Every cell is another window of the form (4), with the same frequencies
and narrower intervals.

Let

\[
P=\sum_j\max\{|A\cap\Omega_j|-a|\Omega_j|,0\}.
\]

The total negative cell discrepancy is also P. A row box meets at most
two boundary bins per coordinate. Since n>=K, their union has size at most
2d ceil(n/K)<=4dn/K. Full cells contribute discrepancy between -P and P.
For a partial cell E subset D,

\[
\sum_Eg=\sum_Dg-|A\cap(D\setminus E)|+a|D\setminus E|
\le\sum_Dg+a|D\setminus E|.
\]

This uses the positive discrepancy of the partial cell only once.
The analogous lower bound is -a|E|. Therefore every row satisfies

\[
\left|\sum_{z\in\Omega}g(z)R_W(y,z)\right|
\le P+4dan/K.\tag{9}
\]

Symmetry and B=aW+g give

\[
\Phi-a^2C=p^{-2}\sum_{y\in\Omega}(B(y)+a)(R_Wg)(y).
\]

As sum(B+a)=2an, (9) proves

\[
\boxed{|\Phi-a^2C|\le2aw^2(P/n+4da/K).}\tag{10}
\]

If
`|Phi-a²C|>=epsilon a²C` and `K>=16d3^d/epsilon`, (6) and (10) imply
`P/n>=epsilon a/(4·3^d)`. Discard positive-density-gain cells with gain
less than epsilon a/(8·3^d). Their total weighted gain is at most that
threshold. At least the same weighted gain remains on at most K^d cells.
Some remaining cell thus satisfies both

\[
\boxed{\Delta a\ge\frac{\epsilon a}{8\cdot3^d},\qquad
\mu\Delta a\ge\frac{\epsilon a}{8\cdot3^dK^d},}
\tag{11}
\]

where mu=|Omega'|/|Omega|. In particular its size is at least
`mu>=epsilon a/[8·3^d K^d(1-a)]`, and its retained A-mass is at least
`epsilon/(8·3^d K^d)`. This is a genuine multiplicative density increment,
with a proved size bound. It does not assert that an arbitrary tiny
high-density cell is useful.

## 6. Main relative counting theorem — PROVED

Let Omega be (4), let A be 4-AP-free, and put

\[
K=\lceil256d3^d\rceil,\qquad
n\ge\max\{K,8\cdot3^d a^{-3}\},\qquad
\mathcal A(W)=\sum_\xi|\widehat W(\xi)|.
\]

Then at least one of the following holds:

**I. Same-rank spatial increment.** A same-frequency refined window has

\[
\Delta a\ge a/(128\cdot3^d),\qquad
\mu\Delta a\ge a/(128\cdot3^dK^d).
\tag{12}
\]

**II. Relative linear signal.** For some nonzero xi,

\[
\boxed{|\mathbb E_\Omega(B-a)e_p(-\xi x)|
\ge\frac{a^2}{16\cdot3^d\mathcal A(W)}.}\tag{13}
\]

It yields a refined narrow window of rank at most d+1 with

\[
\mu\Delta a\ge\frac{a^2}{64\cdot3^d\mathcal A(W)},\qquad
\Delta a\ge\frac{a^2}{64\cdot3^d\mathcal A(W)}.
\tag{14}
\]

**III. Signed relative mixed signal.**

\[
\boxed{\mathcal M\le-\tfrac12a^4C.}\tag{15}
\]

Proof: if `|Phi-a²C|>a²C/16`, use (11). Otherwise
`15a²C/16<=Phi<=17a²C/16`.

If Sigma<7a³C/8, set U=Sigma-aPhi. Then U<-a³C/16. Also
`U=<g,K_BW>_p`. The exact Fourier matrix of K_B and Cauchy–Schwarz give

\[
\begin{aligned}
\|\widehat{K_BW}\|_1
&\le\sum_s|\widehat W(s)|
       \sum_r|\widehat B(2r+s)||\widehat B(-r-2s)|\\
&\le aw\mathcal A(W).
\end{aligned}
\]

Writing eta=max|ghat|/w and using ghat(0)=0 gives
`|U|<=a w² eta A(W)`. Equation(6) now proves (13).
The audited semicircle conversion gives a relative atom with mu Delta>=eta/2.
Split it into two quarter-arcs. One has mu Delta>=eta/4. Its added lifted
coordinate has diameter at most p/4, hence below p/3, proving (14) and
heredity of the window class.

If instead Sigma>=7a³C/8, the size hypothesis and (6) imply
`aw/p<=a⁴C/8`. Inserting this, the lower Sigma bound, and the upper Phi
bound into (1) gives
`M<=a⁴C(1/8-7/4+17/16)=-9a⁴C/16`, stronger than (15).

For completeness, the available Fourier norm bound is explicit:

\[
1\le\mathcal A(W)\le
\prod_{j=1}^d(3+\log|I_j|)\le(3+\log p)^d.
\tag{16}
\]

Each coordinate interval has Fourier coefficient bounded by
`min(|I_j|/p,1/(2|xi|))` at centered nonzero frequency; summing gives
`3+log|I_j|`. Products become Fourier convolutions, whose l1 norm is at
most the product of the l1 norms. This is a bound, not a claim that the
cost is small in an iteration.

The mixed alternative supplies the correctly scaled local U³ consequence

\[
\|g\|_{U^3}^2\ge a^3w/(2\cdot3^d),
\]

by the already audited endpoint inequality. This is not a new inverse
theorem and is not counted as solving the mixed branch.

## 7. Sharper interval version: no ambient logarithm — PROVED

Let Omega=[0,N-1], p>3N, and
`N>=max(8192,24a^-3)`. Partition into4096 nearly equal consecutive blocks.
Either a block of length at least N/8192 has density at least
`a+a/256`, or let D=max_t |sum_(x<t)g(x)|. Absence of that increment gives

\[
D\le[\tau+2(1+\tau)/4096]aN,\qquad\tau=1/256.
\]

Completed blocks have total positive and negative discrepancy at most
tau aN; within a block use its total A-mass and its length. Each row of
R_W is one ordinary interval, so |R_Wg|<=2D. Consequently

\[
|\Phi-a^2C|\le4aND/p^2,
\quad
\frac{|\Phi-a^2C|}{a^2C}
\le12\tau+24(1+\tau)/4096
=6915/131072<1/16.
\tag{17}
\]

The same relative dichotomy applies. In its low-Sigma case,
`U=Lambda(g,B,B,W)<=-a³w²/48`.

Set h=floor(a²N/384) and use the plateau test function

\[
V(x)=\frac1{2h+1}\sum_{t=-h}^{h}
1_{[-h,N-1+h]}(x-t).
\]

This changes the test function only: g, a, and the ambient remain unchanged.
One has V>=W, V=1 on W, and E(V-W)=2h/p. Row sums of K_B are at most
aw, hence

\[
|\Lambda(g,B,B,V-W)|\le2awh/p\le a^3w^2/192.
\]

In particular the magnitude with V remains at least a³w²/96.
Writing M=N+2h and H=2h+1, Fourier coefficient bounds give

\[
|\widehat V(k)|\le
\min(M/p,1/(2|k|))\min(1,p/(2H|k|)).
\]

Integrate this decreasing bound between its breakpoints p/(2M) and p/(2H).
The two tails each contribute at most1 after accounting for the two
frequency signs, and the middle range contributes log(M/H). Including
frequency0 proves `||Vhat||1<=3+log(M/H)`.
For z=a²N/384, `2 floor(z)+1>=z`, so
`M/H<=384/a²+2`, including h=0. Thus the interval linear alternative is

\[
\boxed{\eta\ge
\frac{a^2}{96[3+\log(384/a^2+2)]}.}\tag{18}
\]

This is an endpoint exponent with a density logarithm. It is an actual
relative improvement over a log N window loss, not a subendpoint theorem.

## 8. Relative operators, baselines, and fibers

On ambient-normalized L² use `K_Omega=P_WK_BP_W`. It has

\[
\operatorname{tr}K_\Omega=aw,\quad
\|K_\Omega\|_{HS}^2=\Phi,\quad
\|K_\Omega\|_{op}\le aw.
\]

On `L²(Omega,E_Omega)` use `mathcal K=K_Omega/w`, giving

\[
\operatorname{tr}\mathcal K=a,\quad
\|\mathcal K\|_{HS}^2=\Phi/w^2\le a^2,\quad
\|\mathcal K\|_{op}\le a,
\quad\langle g,\mathcal Kg\rangle_\Omega=\mathcal M/w^2.
\tag{19}
\]

Let rho=mathcal K1. The centered compression has trace
`a-Phi/w²` and squared HS norm
`Phi/w²-2||rho||²+(Phi/w²)²`. These follow by subtracting the constant
block and its row/column blocks. The signed spectral extraction from the
checkpoint applies with gamma=-M/w² and variance a(1-a); bounded
normalization yields only order `a^5 3^(-2d)` under (15), without an
arithmetic description.

For independent Bernoulli selection, the correct operator baseline is

\[
\mathbb E K_\Omega=a^2L_W+a(1-a)P_W/p.\tag{20}
\]

Operator centering does not center its quadratic form against the dependent
random g. For Z equal to the operator minus (20),
`E<g,Zg>=a(1-a)(1-2a)w/p`. The exactly centered off-diagonal version is

\[
Z_{off}=K_\Omega-P_B/p-a^2(L_W-P_W/p),
\quad\mathbb EZ_{off}=0,\quad\mathbb E\langle g,Z_{off}g\rangle=0.
\tag{21}
\]

The last equality uses independence of the four distinct progression
positions, not an assumption that g is independent of the operator.

Relative fibers have unequal marginals. Define

\[
q_d=\mathbb E W_0B_1B_2W_3,\quad
t_{L,d}=\mathbb E B_0B_1B_2W_3,\quad
t_{R,d}=\mathbb E W_0B_1B_2B_3.
\]

Only t_L(d)=t_R(-d) holds in general. Conditioned on the event in q_d,
the endpoint law for nonzero d has probabilities
`0,r_L,r_R,1-r_L-r_R`. Thus

\[
m_d=1_{d=0}aw-a(t_{L,d}+t_{R,d})+a^2q_d,
\qquad m_d/q_d=a^2-a(r_L+r_R).\tag{22}
\]

Negativity forces only r_L+r_R>a, not2a. Window regularity does not
algebraically supply the missing second a. For p=19, Omega=[0,4],
A={0,1,2}, d=1, the marginals are exactly1 and0.

## 9. Relative quadratic spectra and failed simplifications

Put alpha=aw, v=E g²=aw(1-a), and
`Q_h(c,r)=E_x h(x)e_p(-cx²-rx)`. The exact all-chirp identity is

\[
\boxed{\mathcal M=
\sum_{c,r}|Q_g(c,r)|^2|Q_B(3c,3r)|^2
-a^2w^2(1-a)+aw(1-a)^2/p.}\tag{23}
\]

Fourier orthogonality imposes
`x-x'+3(y-y')=0` and `x²-x'²+3(y²-y'²)=0` with factor p^-2.
The case y=y' contributes alpha v. Otherwise division by y-y' forces
`x=2y'-y,x'=2y-y'`; this is the off-diagonal mixed form. Its missing
diagonal is alpha(1-a)²/p. This proof uses that Z_p is a field.

On the subspace of h supported on Omega with sum zero on every label
class from Section4, (7) and the same calculation give

\[
\boxed{\sum_q|Q_h(q)|^2|Q_W(3q)|^2
=(w-1/p)\|h\|_2^2.}\tag{24}
\]

This is an exact weighted local quadratic isometry, not an inverse theorem.
It retains the window baseline instead of replacing it by a scalar norm.

Unweighted full-chirp entropy cannot detect structure. For every nonzero
complex h, exact second/fourth moments give

\[
\sum_q|Q_h(q)|^2=p\|h\|_2^2,\quad
\sum_q|Q_h(q)|^4=2\|h\|_2^4-\mathbb E|h|^4/p.
\]

The fourth identity follows because equal sums and sums of squares of two
pairs force equal unordered pairs; subtract the all-equal double count.
For `nu(q)=|Q_h(q)|²/(p||h||2²)`, its collision probability lies in
`[p^-2,2p^-2]`. Therefore its Renyi-2 and Shannon entropies are always
between `2 log p-log2` and `2 log p`, including for a pure quadratic phase.
Conditional or derivative spectra are not excluded by this observation.

The following proposed shortcuts are FALSE:

* **Global quadratic-Rayleigh positivity after localization.** For
  p=19, Omega=[0,4], A={1,2,3}, q(x)=3(x-1)(x-3),
  `<W e(q),K_B W e(q)>=[3-4cos(pi/19)]/19²<0`.
  Here the relative mixed form is exactly -12/(25·19²).
* **Generic negative spectrum after localization.** For Omega=[0,5],
  A={0,3}, p>18, `K_Omega=P_A/p`; its centered compression is PSD.
* **Dropping weighted pair corrections.** On Omega=[0,14], A={3,6,11},
  p=31, a=1/5, the endpoint one-g term vanishes but
  `Lambda(g,g,W,W)+Lambda(g,W,g,W)=-1/(5p²)<0`.

All these are exact algebraic counterexamples, not disproofs of the
target asymptotic regime. Localized quadratic phases can genuinely see
negative spectrum; a general density-sensitive extraction remains open.

## 10. A repeatable high-linear-signal reduction — PROVED

For sufficiently large prime p, if a cyclic 4-AP-free A of density alpha
satisfies

\[
\max_{\xi\ne0}|\widehat f(\xi)|\ge3\alpha/4,
\]

then there is a smaller prime q and a cyclic 4-AP-free A' with

\[
\boxed{p/100<q<p/50,\qquad\alpha'>11\alpha/10.}\tag{25}
\]

Choose the new prime first: take q between floor(p/100) and twice that
integer, using the elementary prime-existence proof already recorded in
SIGNED_RESEARCH.md. Let L=(q-1)/2 and rho=L/p<1/100. Every nonboundary
phase arc of width rho contains exactly L points of Z_p and is an
L-term cyclic progression.

Let F(t) be the density of A on that arc. Then F>=0, mean F=alpha, and
`|Fhat(1)|=|fhat(xi)| sinc(pi rho)`. A bounded nonnegative function of
mean alpha and cap D obeys

\[
|\widehat F(1)|\le(D/\pi)\sin(\pi\alpha/D).\tag{26}
\]

Proof: orient the cosine toward its first coefficient, choose its top
arc E of length alpha/D, and put lambda=cos(pi alpha/D). Pointwise
`(F-D1_E)(cos-lambda)<=0`; the lambda term integrates to zero. This
proves (26). The bound increases with D, since sin t-t cos t>0 on(0,pi).

If every arc had density at most12alpha/5, it would follow that
`(3/4)sinc(pi/100)<=sinc(5pi/12)`. This is false. Elementary bounds
pi<22/7, pi>31/10, sin x>=x-x³/6, and
sin75°=(sqrt6+sqrt2)/4 give respectively

\[
(3/4)\operatorname{sinc}(\pi/100)>17997/24000
>2319/3100>\operatorname{sinc}(5\pi/12).
\]

For pi>31/10 one may use the inscribed regular12-gon:
`pi>3(sqrt6-sqrt2)>3(2449/1000-1415/1000)>31/10`.
The upper radical bounds sqrt6<49/20, sqrt2<283/200 prove the displayed
upper sinc bound. The rational comparison is verified by cross multiplication.

Thus one progression has density>12alpha/5. Pull it back to [0,L-1]
and embed directly in Z_q, where q=2L+1. No new wrapped AP appears,
because a second difference has absolute value<=2(L-1)<q. The resulting
density exceeds `(6/5)(1-1/q)alpha>=11alpha/10` for q>=12.
If alpha>=5/12, the required arc density exceeds1, so the initial
high-signal hypothesis is impossible instead.

All such reductions have s=1,t=0. Their number, even interleaved with
other density-increasing cyclic steps, is at most
`1+log(1/alpha_0)/log(11/10)`. Their total log scale loss is at most
that number times log100. At alpha_0=epsilon/log p_0 this is O(log log p_0),
and the modulus remains p_0 divided by a fixed power of log p_0.
The cutoff and fixed size thresholds persist for sufficiently large p_0.

The same construction works for every fixed relative-signal threshold
greater than2/pi. It does not apply to the coefficient c alpha² forced
by the general cubic branch.

## 11. Optimized low-signal cubic conversion and exact recurrence

For an interval, let
`eta=|E_[N] f e(theta x)|`, `beta=|E_[N] e(theta x)|`.
Choose positive integers q,L with qL<=N, and put `rho=4pi L||q theta||`.
Partition residue chains into blocks of lengths L through2L-1.
Approximating the phase by a block constant costs at most2alpha rho.
If m_P are block means and M=max m_P, positivity of M-m_P gives

\[
\left|\sum_P\mu_Pm_Pz_P\right|
\le M\left(1+\left|\sum_P\mu_Pz_P\right|\right)
\le M(1+\beta+\rho).
\]

Thus one block has gain at least

\[
\boxed{\frac{\eta-2\alpha\rho}{1+\beta+\rho}.}\tag{27}
\]

This retains the actual Diophantine parameter. For exact theta=b/q with
q|N, a whole residue chain has length N/q and gain at least eta.
For general theta, optimizing the available Dirichlet guarantee gives
the checkpoint bound

\[
\Delta\alpha\ge3\eta/8,\quad
N'\ge(128\pi)^{-1}\sqrt{\eta N/\alpha}.
\tag{28}
\]

For the small case `N<(128pi)² alpha/eta`, its length lower bound is
below1; a singleton from A has gain `1-alpha>=3eta/8`, since
`eta<=2alpha(1-alpha)`. Thus (28) has a singleton fallback there.
This is a guaranteed bound, not a universal optimality assertion. For
eta_j>=c alpha_j², put L_j=log N_j and C_0=log(128pi). Since alpha_j
increases, its exact unrolling gives

\[
\boxed{L_j\ge2^{-j}L_0-
[2C_0+\log(1/(c\alpha_0))](1-2^{-j}).}\tag{29}
\]

This guarantee supports only O(log log N) successive steps. The allowed
worst-case density recurrence
`alpha_(j+1)=alpha_j+(3c/8)alpha_j²` takes Theta(1/alpha_0) steps to
reach fixed density. At epsilon/log N that is Theta(log N), while during
O(log log N) steps the relative density change is only
O(log log N/log N). No logarithmic improvement in constants removes this
mismatch.

There is no proved bound forcing the cubic branch to stop: the 3-AP-free
subcase is hereditary under progression pullback and safe reembedding.
When its cutoff holds it has T=alpha/p-alpha³ and M>0.

## 12. Further cubic routes: proved separators, missing smoothing

Let G(x)=(B*B)(2x), so G>=0, E G=alpha² and T=<f,G>=-tau. If S is a
self-adjoint positive mean-preserving arithmetic average satisfying
`|<f,SG-G>|<=tau/2`, then

\[
\boxed{\max Sf\ge\frac{\tau}{2(\|G\|_\infty-\alpha^2)}.}\tag{30}
\]

Indeed, for H=Sf<=Delta and E H=0,
`-<H,G>=<Delta-H,G>-Delta alpha²<=Delta(||G||infinity-alpha²)`.
Self-adjointness supplies the required negative correlation. A spread
convolution with ||G||infinity<=K alpha² would therefore give gain
order alpha, if sufficiently cheap arithmetic smoothing existed.

Clipping provides an exact complementary statement. Choose K>1 as a
separate clipping parameter, unrelated to the quantile-bin constant. Put
R=max|fhat|, v=E(G-alpha²)²=sum|fhat|⁴<=R²b, and
`G_K=min(G,K alpha²)`. The inequality `(u-c)_+<=u²/(4c)` gives

\[
\mathbb E(G-K\alpha^2)_+\le\frac{v}{4(K-1)\alpha^2}.
\]

Since f>=-alpha,
`<f,G_K><=T+alpha E(G-Kalpha²)_+`.
Thus T<=-c alpha³ and R²b<=2c(K-1)alpha⁴ imply
`<f,G_K><=-(c/2)alpha³`. Either a coefficient of order alpha^(3/2)
already exists, or a bounded normalized separator has correlation of order
alpha. Neither statement supplies bounded arithmetic complexity or cheap
smoothing of the separator.

Two hostile tests identify missing assumptions:

* A convolution peak plus Booleanity and cutoff does not imply (25).
  Quadratic residues in Z_29 have alpha=14/29, G(0)=alpha, and
  R=(sqrt29+1)/58<3alpha/4. They contain1,5,9,13 and so are not AP-free.
  This diagnoses the relaxed inference, not an AP-free theorem.
* Cheap smoothing of a spread convolution is false on other ambient
  groups. For a prime q=3 mod4, the paraboloid
  `{(x,y,x²+y²)}` in F_q³ is 3-AP-free and has alpha=1/q,
  R=alpha², T=-bR, and G=alpha²-alpha²f. Its autocorrelation is b at0,
  zero when the spatial shift is nonzero, and -alpha² on nonzero vertical
  shifts. Hence the paired approximation in (30), for S=mu*, forces
  mu(0)>=1/2. A uniform averaging progression has at most two points.
  This example is not prime cyclic and has |G|alpha³=1; it is not a
  counterexample to the stipulated target class.

For completeness, the paraboloid claims follow directly. A midpoint
equation forces u²+v²=0; -1 is nonsquare, so the AP is trivial. Completing
two quadratic squares gives Fourier coefficients
`-q^-2 e_q((u²+v²)/(4t))` for t!=0 and zero at the other nonzero
frequencies. The quadratic Gauss square is -q: its modulus is sqrt q by
the change (x,y)->(x-y,x+y), while complex conjugation negates it.
This gives the Fourier formula and `G=alpha²-alpha²f`. Translating the
graph gives q common points for a nonzero spatial shift, none for a purely
vertical nonzero shift, and q² at zero, proving the correlation claims.

## 13. Scale, rank, and hybrid iteration ledger

| Alternative | Proven gain/signal | Domain cost | Repeatability |
|---|---|---|---|
| Phi irregularity | Delta>=a/(128·3^d) | same rank; mu Delta>=a/(128·3^dK^d) | yes on narrow windows |
| Low Sigma | eta>=a²/(16·3^d A(W)) | narrow quarter-cell adds one frequency; mu Delta>=eta/4 | yes geometrically; costs deteriorate |
| Interval low Sigma | eta>=a²/[96(3+log(384/a²+2))] | initial ambient log removed | later rank costs remain |
| Relative mixed | -M>=a⁴C/2 | bounded eigenmode only order a^5·3^(-2d), unstructured | no increment proved |
| High relative linear signal | cyclic alpha'>1.1alpha | prime shrinks by at most100 | fully repeatable |
| Generic native linear conversion | Delta>=3eta/8 | N'>=const sqrt(eta N/alpha) | loses half log N guarantee |
| Clipped convolution separator | correlation order alpha, or R order alpha^(3/2) | smoothing complexity unbounded | conditional only |

At a fixed rank d, let beta_d=1/(128·3^d),
`kappa_d=1/(128·3^dK^d)`. Every Phi-irregularity step has
`a'>=(1+beta_d)a` and retained A-mass at least kappa_d. Exact telescoping
therefore bounds all such fixed-rank steps by

\[
\log(n_0/n_k)\le
\left[1+\frac{\log(1/\kappa_d)}{\log(1+\beta_d)}\right]
\log(1/a_0).\tag{31}
\]

There is also a terminal counting criterion on the same class. Removing
each point of Omega\A destroys at most n APs for each of four possible
positions, because that point and one other position determine the step.
Thus

\[
\Lambda_4(A)\ge w^2[3^{-d}-4(1-a)].\tag{32}
\]

If `a>=1-1/(8·3^d)` and `n>2·3^d`, this exceeds the diagonal aw/p,
contradicting AP-freeness. In the asymptotic density regime, pure same-rank
irregularity steps can therefore be iterated to a contradiction: (31)
keeps n at least its initial value times a fixed power of a_0, which
remains above the theorem's size cutoff when a_0=epsilon/log N.
The one-step size hypothesis alone is not a bootstrap at arbitrary finite N.
The unresolved alternatives prevent this from being a proof for every set.

Low-Sigma steps increase rank. Their constants contain3^d and A(W),
and the theorem's size cutoff contains3^d a^-3. These cannot be held
constant through a hybrid recurrence. No proved potential bounds their
total number or compensates for that growth. The relative mixed steps
do not yet have gain or scale parameters at all.

There is an exact hereditary obstruction to charging these rank increases
to depleted 3-AP scarcity. If A is cyclic3AP-free, then on every refined
window Sigma=aw/p. Under the theorem's size hypothesis,
`Sigma/(a³C)<=3^d/(a²n)<=a/8`. Thus the low-Sigma condition remains
strong after restriction. This does not prove infinitely many steps
occur, but supplies no diminishing scarcity budget.

The guaranteed rank-dependent numbers themselves permit stalling. Even
optimistically put A(W)=1 and choose

\[
\mu_d=1-a_d/(64\cdot3^d),\qquad a_{d+1}=a_d/\mu_d.
\]

Then `mu_d(a_(d+1)-a_d)=a_d²/(64·3^d)` and all A-mass is retained, but
`1/a_(d+1)=1/a_d-1/(64·3^d)`. The total reciprocal-density improvement
is bounded. This is an admissible numerical model of the current bounds,
not a constructed sequence of actual windows.

One must also retain the actual AP availability beta_W=C/w². If a
refinement discards a fraction r of the window, the same hole-counting
argument as (32) proves

\[
C'\ge C-4rw^2,\qquad
\boxed{\beta_{W'}\ge(\beta_W-4r)/(1-r)^2.}\tag{33}
\]

Hence tiny measure loss cannot itself divide the actual baseline by3 at
each rank increase. Replacing every baseline by3^-d can be wasteful.
However (33) does not control A(W) or quantile refinement complexity, so
it does not yet provide the missing hybrid potential.

## 14. Full alpha=epsilon/log N test and transfer

* High-signal cyclic reductions cost O(log log N) in logarithmic scale.
* At fixed rank, Phi-irregularity steps cost O_d(log log N), including
  a valid terminal counting argument.
* Even an ideal reusable constant-rank alpha² signal with the sharp
  joint relation mu Delta>=c alpha² yields only O(1/alpha_0)
  logarithmic loss. At epsilon/log N this is O(epsilon^-1 log N),
  not o(log N). The actual low-Sigma bounds carry extra rank/log factors.
* The exact native recurrence (29) fails before the required number of
  low-signal cubic steps. This is failure of the proved guarantee, not a
  theorem ruling out every possible stronger linear method.
* The signed mixed alternative supplies no iterable increment.

One-time transfer from [N] to a prime group is already proved in the
checkpoint: choose2N<p<4N for sufficiently large N; second differences
of four representatives have magnitude below p and therefore cannot
create new wrapped APs. This loses only a fixed density factor.
The new high-signal prime-first step proves its own safe repeated transfer.
The narrow-window refinements remain inside the original prime group,
preserving cyclic AP-freeness, so they require no repeated interval
padding. A final contradiction on them would follow from (32).

No complete hybrid recurrence currently covers all alternatives. Thus the
ultimate target remains open despite the relative counting theorem.

## 15. Adversarial audit and finite verification

Run `python3 verify_relative.py > relative_verification.json`.
The captured passing results include:

* all32,766 subsets of intervals of lengths1 through14, with exact
  Phi/Sigma/AP counts, prefix-discrepancy bounds, and fixed-size models;
* all4,096 subsets of a12-point rank-two window in Z_101, checking the
  label baseline, quantile row bound, Phi stability, and cell geometry;
* 220 additional seeded windows of ranks1 through3;
* exact localized negative-Rayleigh and positive-semidefinite examples;
* separately numerical all-chirp/Fourier moment identities, tolerance1e-12;
* stable periodic-density examples of lengths8192 through65536,
  explicitly labelled as not AP-free;
* exact rational checks of the interval constants and prime-first margin.

The large-K hypotheses of the general increment theorem are not exercised
by the tiny exhaustive windows; those tests audit its constituent exact
geometry and discrepancy identities. The theorem is proved above, not
inferred from finite data. The eligible Z_101 mixed-branch witness remains
a diagnostic input; it does not satisfy the much larger window theorem's
local-size threshold and is not misreported as an iteration instance.

Independent proof reviews checked the quantile partial-cell bound without
an erroneous extra2P, the simultaneous gain-and-size cell choice, the
plateau h=0 case, all operator normalizations, and the fixed-size versus
Bernoulli distinction. No internet was used.

## 16. Sharpest remaining sublemma and next prompt

The unresolved relative theorem must improve at least one of:

1. the low-Sigma increment, with enough quantitative gain or rank control
   to beat the endpoint budget; or
2. the negative relative mixed alternative (15), converting it to an
   arithmetic increment with explicit costs.

The weighted local quadratic transform (24), after separately handling
label imbalances, is a concrete candidate representation. Its isometry
does not itself select a large coefficient. The clipped cubic separator
in Section12 is another candidate, but cheap arithmetic smoothing is a
separate unproved theorem, not an automatic consequence of boundedness.

Next research prompt:

> Continue offline from RELATIVE_WINDOWS.md. Accept the controlled-window
> theorem (12)-(15), the interval smoothing refinement (18), and the
> repeatable high-signal prime-first reduction (25). Work on the terminal
> low-signal cubic or stable-Phi negative-mixed alternatives. Retain the
> exact window-weighted quadratic frame and local variance/boundary terms.
> Prove either an increment above the endpoint or a quantified rank/scale
> saving that closes the hybrid recurrence. Do not drop the3^d factor,
> hold a growing rank fixed, identify an eigenvector with a phase, or infer
> smoothing from clipping alone. Test against the narrow-window examples,
> the affine-spread 3-AP-free family, and the outside-class paraboloid
> smoothing obstruction with its hypotheses clearly separated.

Durable checkpoint: relative counting and window heredity are proved;
high-signal linear steps are cheaply repeatable; low-signal cubic and
negative mixed extraction remain unclosed. No ultimate solution claimed.
