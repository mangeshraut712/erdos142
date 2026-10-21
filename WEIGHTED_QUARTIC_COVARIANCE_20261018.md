# Exact shifted-chirp covariance for the original weighted quartic residual

18 October 2026. Offline. **PROVED algebraic partial theorem.**
The local target, DIRECT-Q-GAIN, and (P12) remain OPEN. This extends the
unweighted chirp branch identity to the original mixed tent weight. It
removes the pairing baseline exactly, but does not control the remaining
covariance. No novelty beyond this repository is asserted.

## 1. Definitions and theorem

Let p>3 be prime and let F(x,h) be the original nonnegative tent weight
from `WEIGHTED_PAIR_REDUCTION_20261016.md`, with its exact probability
measure lambda(C,beta,N):

    F(x,h)=sum lambda(C,beta,N)e_p(2Cxh+Nh^2+beta h),
    lambda>=0, sum lambda=1.

For a real function u on F_p put

    Q_u(c,t)=E_y u(y)e_p(-cy^2-ty),
    U=E_y u(y)^2, M4=E_y u(y)^4,
    m_s=E_y u(y)^2 e_p(sy^2)=Q_(u^2)(-s,0),
    D_s(c,t)=Q_u(c,t) conjugate(Q_u(c+s,t))-m_s/p.

All E averages are normalized; all sums over chirp indices (c,t) below
are UNNORMALIZED. Let

    s=(N-3C)/2, gamma=(N-5C)/2,
    phi_(C,beta,N)(c,t)=(3c+gamma,3t-beta),

with arithmetic in F_p. Define the nonnegative real energy

    E_F(u)=sum_(C,beta,N) lambda(C,beta,N)
              sum_(c,t) |D_s(c,t)-D_s(phi(c,t))|^2.       (W1)

For every such real u, exactly

    sum_t D_s(c,t)=0 for every c,s,
    sum_(c,t)|D_s(c,t)|^2=U^2-M4/p for every s,           (W2)

    Lambda_F(u)=E_(x,h)F(x,h)product_(j=0)^3 u(x+jh)
       =M4/p+sum lambda sum D_s(c,t)conjugate(D_s(phi(c,t)))
       =U^2-(1/2)E_F(u).                               (W3)

The averaged covariance in (W3) is real. No AP exclusion or mean-zero
assumption is needed. When u=B-aP, this Lambda_F(u) is precisely R_4^F;
there is no omitted host correction because u already vanishes outside
Omega and the quartic term has no remaining P slot.

## 2. Proof by exact arithmetic branches

Fix one (C,beta,N), and abbreviate s,gamma as above. Set

    g0(y)=u(y),
    g1(y)=u(y)e_p(gamma y^2-beta y),
    g2(y)=u(y)e_p((4C-N)y^2+beta y),
    g3(y)=u(y)e_p(sy^2).

The sum of their quadratic coefficients is zero, the slot-weighted sum
is C, and the squared-slot-weighted sum is N. Their linear coefficients
sum to zero and have slot-weighted sum beta. Consequently

    product_j gj(x+jh)
      =product_j u(x+jh)e_p(2Cxh+Nh^2+beta h).           (W4)

For arbitrary four functions gj, summing

    sum_(c,t) Q_g0(c,t)Q_g1(-3c,-3t)
                          Q_g2(3c,3t)Q_g3(-c,-t)

imposes the two exact equations

    -x0+3x1-3x2+x3=0,
    -x0^2+3x1^2-3x2^2+x3^2=0.

Write x0=x, x1=x+h, x2=x+k. Then x3=x-3h+3k and the second equation
reduces to 6(h-k)(2h-k)=0. Since p>3, the branches are k=2h (the 4-AP)
and k=h (x0=x3, x1=x2). Their intersection is the common diagonal.
The four Fourier normalizations and two orthogonality sums give p^-2
on each branch. The pairing contribution is

    [E_y g0(y)g3(y)] [E_y g1(y)g2(y)]=|m_s|^2,

and the intersection is M4/p: all four modulation coefficients sum
to zero on the diagonal.

Write D_s^raw(c,t)=Q_u(c,t)conjugate(Q_u(c+s,t)). Since u is real,
Q_u(-c,-t)=conjugate(Q_u(c,t)). Substitution of the gj into the Fourier
sum therefore gives exactly

    sum D_s^raw(c,t)conjugate(D_s^raw(phi(c,t)))
      =E_(x,h) e_p(2Cxh+Nh^2+beta h)product_j u(x+jh)
          +|m_s|^2-M4/p.                              (W5)

For each c, orthogonality in t gives sum_t D_s^raw(c,t)=m_s.
The affine map phi is a permutation of F_p^2 and sends every t-row
bijectively to another row. Subtracting m_s/p from every entry cancels
exactly |m_s|^2 in (W5); this proves the covariance formula in (W3)
after averaging with lambda. No square-root or host-size loss occurs.

For the norm in (W2), expand
sum_(c,t)|Q_u(c,t)|^2|Q_u(c+s,t)|^2. Orthogonality gives equality of
both the sums and the sums of squares of two pairs of field elements.
The unordered pairs coincide, producing two branches: the direct
pairing contributes U^2 and the swapped pairing contributes |m_s|^2.
Their intersection contributes M4/p. Thus the raw norm is
U^2+|m_s|^2-M4/p. Centering subtracts |m_s|^2, proving (W2).

Finally every phi is a permutation, so its two D_s norms agree. Expand
the squared difference in (W1):

    E_F(u)=2(U^2-M4/p)-2 Re(sum lambda sum D_s conjugate(D_s o phi)).

The covariance average is real because (W5) averages to the real
physical weighted count. This yields the energy formula in (W3).

## 3. Exact Boolean correction and diagonal

On the proper window use P=1_Omega, B=1_A, g=aP, u=B-aP,
a=|A|/|Omega| and w=|Omega|/p. Then

    u^2=(1-2a)u+a(1-a)P,
    U=wa(1-a),
    M4=wa(1-a)(1-3a+3a^2),
    m_s=(1-2a)Q_u(-s,0)+a(1-a)Q_P(-s,0).              (W6)

In particular m_0=U, not a or a^2. The proper-host transform Q_P is
retained explicitly; replacing it by a full-group constant is invalid.
The h=0 contribution in R_4^F is M4/p, exactly as in (W3).

Combining with the literal cubic residual, without altering its weight,

    Q=R_3^F+R_4^F=R_3^F+U^2-(1/2)E_F(u).              (W7)

Hence (P12) is exactly equivalent to the following energy upper bound:

    E_F(u) <= 2U^2+2R_3^F+a^4w mu.                    (W8)

This equivalence is valid at finite p. It preserves the cubic term; a
bound on R_4 alone cannot silently discard it. W8 is a sharper explicit
spectral formulation of the OPEN sublemma, not an established estimate.

For an actual AP-free set, the exact Boolean expansion instead gives

    E_F(u)=2U^2+2R_3^F+2a^4T+2R_1^F+2R_2^F-2aw/p.    (W9)

The full Boolean count has diagonal aw/p, whereas the quartic residual
has diagonal M4/p. These are distinct quantities. On reachable hosts
the existing estimates make (W9) incompatible with (W8). Proving W8
from the specified failed phase selection, without merely substituting
(W9), remains the structural problem.

## 4. What the phase cap does and does not control

If delta=max_(c,t)!=(0,0)|E_Omega(B-a)e_p(-cx^2-tx)|, then
max|Q_u|=w delta, since Q_u(0,0)=0. Thus

    |D_s(c,t)| <= w^2 delta^2+|m_s|/p,
    sum_(c,t)|D_s|^2=U^2-M4/p.                         (W10)

Even small individual entries can distribute this fixed energy over
many indices. Neither (W10) nor positive lambda implies an upper bound
of the precision a^4w mu needed in (W8). The direct cubic estimate is

    |R_3^F| <=4w^2a^2(1-a)delta+4a beta_boundary,
    beta_boundary=(mu+p^-1/2)b+1/p.

At the target failed cap delta<c_epsilon a^(3/2)R(a), its spectral
upper bound divided by a^4w mu is
4c_epsilon(1-a)(w/mu)a^-1/2 R(a), which is not controlled to be small.
For the original tau=a^2/log p even its boundary envelope is only
O_epsilon(1) at a approximately epsilon/log p. These deficits are not
repaired by the exact algebra in W3.

A universal consequence of W2 and Cauchy-Schwarz is

    0<=E_F(u)<=4(U^2-M4/p),
    -U^2+2M4/p <= R_4^F <= U^2.                        (W11)

This is at the U^2 scale, approximately w^2a^2 for small a, rather
than a^4w mu. The nonnegative energy in W1 is subtracted in W7; it
therefore supplies an upper orientation, not the desired lower bound.
The sign of a quadratic form cannot be inferred from positive tent
Fourier coefficients after this four-slot branch operation.

## 5. Independent checks and remaining task

`verify_weighted_quartic_covariance_20261018.py` checks the branch
factorization and coefficient absorption exactly modulo p, then all
modewise and averaged Fourier identities for real fields, constants,
point masses, and Boolean residuals on proper windows. It checks repeated
quadratic constraints and linear-only cases. Fourier comparisons are
floating arithmetic and are labelled separately. These small primes do
not meet the asymptotic target domain.

Independent symbolic review confirmed the signs, p factors, diagonal,
row centering, and universal norm. This is not a proof of (W8), phase
selection, or r_4(N)=o(N/log N). The next attack must couple the affine
chirp-index covariance in W1 to actual Boolean/AP-free arithmetic under
the adequate phase cap, or obtain selection by a different argument.
