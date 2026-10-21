# A large U^3 norm need not give a global finite-field quadratic phase

16 October 2026, continuation cycle. Offline. **PROVED auxiliary
obstruction.** This is not an AP-free Boolean construction and does not
refute DIRECT-Q-GAIN or r_4(N)=o(N/log N).

The exact distinction matters: the required phases are
`e_p(cx^2+rx)` with c,r in F_p. A quadratic phase in an integer lift of
a short interval can have a real coefficient not of this form. The
following elementary construction quantifies that obstruction even on
a rank-one interval window at logarithmic relative density.

## 1. A localized fractional quadratic

Let p>=17 be prime, L=floor(p/8), I={0,...,L}, w=|I|/p, and alpha=sqrt(p).
On F_p, using the representative x in {0,...,p-1}, define

    f(x)=1_I(x) exp(2pi i alpha x^2/p^2),
    Q_f(c,r)=E_x f(x)e_p(-cx^2-rx).

Then, uniformly over all c,r,

    |Q_f(c,r)| <= D_p:=3p^(-1/4)sqrt(1+log p),         (I1)

while

    ||f||_(U^3)=||1_I||_(U^3)>=1/sqrt(32).             (I2)

Both norms and Fourier transforms use normalized full-group averages.

For (I2), every cube whose eight vertices lie in I has an integer affine
lift. Each face relation modulo p has integer magnitude at most 2L<p,
so it holds in the integers. All third differences of the real quadratic
alpha x^2/p^2 then vanish exactly. Thus the alternating product of the
eight phases is one, and the U^3 cube averages of f and 1_I are equal.
Take the cube base and its three positive steps in {0,...,floor(p/32)}.
Their sum is at most 4floor(p/32)<=L. There are more than (p/32)^4 such
cubes, whence `||1_I||_(U^3)^8>=32^(-4)`. This includes degenerate cubes;
the lower bound is independent of their presence asymptotically.

## 2. Linear modes by differencing

For c=0, let S be the unnormalized sum defining p Q_f(0,r), n=L+1.
Expanding |S|^2 by the difference h gives

    |S|^2<=n+2 sum_(h=1)^L min(n,p^2/(4alpha h)).

Indeed the inner sum has linear phase increment 2alpha h/p^2, which
lies between zero and 1/2. A geometric series bounds its magnitude by
the reciprocal of twice that increment, independently of r. Therefore

    |Q_f(0,r)|^2
       <=1/p+(1+log p)/(2sqrt(p)).                     (I3)

This bound covers the mean r=0 as well. There is no omitted zero mode.

## 3. Nonzero quadratic modes by a discrete Sobolev bound

Let Delta f(x)=f(x+1)-f(x), cyclically. The two boundary jumps contribute
2/p to its squared L2 norm. For 0<=x<L, the phase increment has magnitude
at most pi/sqrt(p), since 2L+1<=p/2. Hence

    ||Delta f||_2^2 <= (2+pi^2/8)/p.                   (I4)

With the centered frequency representative tilde t and Parseval,
`|e_p(t)-1|>=4|tilde t|/p` gives

    sum_t tilde t^2 |fhat(t)|^2
       <= (2+pi^2/8)p/16.

Since w<=1/8+1/p, for p>=17 one has

    sum_t (1+tilde t^2/p)|fhat(t)|^2<=1,
    sum_t (1+tilde t^2/p)^(-1)<=1+pi sqrt(p).

The second estimate follows by comparison with the integral of the
decreasing function (1+x^2/p)^(-1) on the positive half-line. Weighted
Cauchy-Schwarz now proves

    sum_t |fhat(t)|<=sqrt(pi+1)p^(1/4).                 (I5)

For c!=0 insert the Fourier series of f into Q_f(c,r). Every inner
normalized Gauss sum has magnitude p^(-1/2), so

    |Q_f(c,r)|<=sqrt(pi+1)p^(-1/4).                    (I6)

Combining (I3) and (I6) proves (I1). All factors of p are explicit.

## 4. A real, centered, bounded residual

There is a real v supported in I such that

    E_I v=0, |v|<=1,
    max_(c,r)|Q_v(c,r)|<=D_p,
    ||v||_(U^3)>=1/(8sqrt(32))                         (I7)

for every sufficiently large p. Here is an existence proof with constants.
Write f=h_1+i h_2. The U^3 triangle inequality implies that at least one
real component h has norm at least 1/(2sqrt(32)). Both components have
chirp correlations bounded by D_p: use
`Q_conjugate(f)(c,r)=conjugate(Q_f(-c,-r))` in their real/imaginary parts.
Put `m=E_I h` and `v=(h-m1_I)/2`. Then |m|<=1, so |v|<=1 and E_I v=0.
Also |m|<=D_p/w and |Q_(1_I)|<=w, proving the chirp bound in (I7).
Finally

    ||v||_(U^3)
       >=1/(4sqrt(32))-D_p/(2w)
       >=1/(8sqrt(32))

once D_p/w<=1/(4sqrt(32)). This is an asymptotic condition, not a claim
that the constants are already effective at the small primes in tests.

For completeness, the norm inequality used here follows from the
eight-linear Gowers Cauchy-Schwarz inequality

    |E_(x,h_1,h_2,h_3) product_(omega in {0,1}^3)
          conjugation^(|omega|) g_omega(x+omega.h)|
       <= product_omega ||g_omega||_(U^3).

One way to verify it is to set x=y_1^0+y_2^0+y_3^0 and
h_i=y_i^1-y_i^0. These induce the same uniform (x,h) distribution.
The summand becomes a box product with the omega-th function evaluated
at (y_1^(omega_1),y_2^(omega_2),y_3^(omega_3)). For coordinate 1, integrate
the two faces separately in y_1^0 and y_1^1, then apply Cauchy-Schwarz in
the other four variables. Expanding the two resulting squares duplicates
each face, with conjugation. Repeat for coordinates 2 and 3. After the
third step the eighth power of the initial absolute average is bounded
by the product, over the eight original functions, of their box cube
averages. For functions of the sum of their coordinates these averages
are their U^3 norms to the eighth power, giving the displayed inequality.
The cube average is nonnegative, for example from the identity
`||g||_(U^3)^8=E_h sum_t |hat(g conjugate(g(.+h)))(t)|^4`.
Expand the cube product of g_1+g_2, apply the displayed inequality to
each of the 2^8 terms, and use the binomial formula. Taking eighth roots
gives the triangle inequality. Thus no inverse theorem is invoked here.

## 5. Explicit relevance and the missing hypothesis

Fix epsilon>0 and put a=epsilon/log p for sufficiently large p. Define
the bounded real weight

    B_weight=a(1_I+v),  u_weight=a v.

It has relative mean a, takes values in [0,2a] subset [0,1], and its
trivial-factor variance is zero. The window I has rank one and satisfies
the product domain (T5) for sufficiently large p. Nonetheless

    ||u_weight||_(U^3)>=a/(8sqrt(32)),
    max_(c,r)|E_I u_weight e_p(-cx^2-rx)|<=a D_p/w.

The latter divided by `a^(3/2)R(a)`, R(a)=loglog(e^2/a), tends to zero,
since its upper bound is a constant depending on epsilon times
`p^(-1/4)log p/R(a)`. Even the weaker fixed multiple of a^(3/2) is not
forced by this U^3 signal in the class of bounded real weights.

This is NOT a Boolean/AP-free counterexample. For sufficiently large p,
|m|<=1/2, so v>=-3/4 and B_weight>=a/4 on the entire interval I.
Its support therefore contains many nontrivial four-term progressions.
It violates exactly the Boolean and AP-exclusion inputs that a successful
selection proof must exploit. A local real quadratic or bracket-quadratic
inverse statement is not refuted by the example. Only the inference to
the specified global finite-field chirps from a bare U^3 signal is blocked.

Finite verification evaluates all global chirps at the stated small
primes, the cube identity, mean subtraction, and the discrete Fourier
estimates. The asymptotic obstruction follows from (I1)-(I7), not from
extrapolating those finite measurements.
