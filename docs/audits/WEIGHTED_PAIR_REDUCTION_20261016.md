# Arithmetic near-positivity of the weighted pair residual

16 October 2026, continuation cycle. Offline. **PROVED partial theorem.**
The local target r_4(N)=o(N/log N) remains OPEN. No literature novelty is
asserted. This note uses the tent weight and normalizations of
`MIXED_QUADRATIC_TERMINAL_20261016.md`, independently rederived below.

## 1. The theorem

Let p>3 be prime, and let Omega be a nonempty intersection of d nonzero
linear and s nonconstant quadratic interval constraints over F_p. Write
the generators as xi_l and q_l(x)=c_l x^2+b_l x+e_l, respectively.
Put r=d+s>=1, k=d+2s, w=|Omega|/p. Choose an integer 1<=H with 2H<p,
and let f be the tent of height one and radius H. Define

    F(x,h)=product_l f(xi_l h)
           product_l f((2c_l x+b_l)h)f(c_l h^2).

Use normalized averages over F_p, with all h including zero. For any
real u define U=E_p u^2 and

    J_ij(u)=E_(x,h) F(x,h)u(x+ih)u(x+jh), 0<=i<j<=3.

There are explicit nonnegative numbers Z_ij(u) and nu_ij in [0,1] such that

    |J_ij(u)-Z_ij(u)| <= (1-nu_ij) U/sqrt(p),
    Z_ij(u)>=0.                                        (P1)

In particular J_ij(u)>=-U/sqrt(p). This is an arithmetic near-positivity
theorem, not exact PSD. It is consistent with the p=53 negative-form
witness in the preceding checkpoint.

For a Boolean B=1_A supported in Omega, write P=1_Omega,
`a=|A|/|Omega|`, `u=B-aP`, `U=w a(1-a)`. Let R_2^F be the sum of the six
two-residual terms in the expansion of Lambda_F(B) at aP. Let b be the
density of the eroded boundary Omega\Omega_-, and let mu be the persistent
baseline defined below. Put

    epsilon_p=p^(-1/2),
    beta_boundary=(mu+epsilon_p)b+1/p,
    E_2=a^2[6 beta_boundary+(6-sum_(i<j)nu_ij)U epsilon_p].

Then

    |R_2^F-a^2 sum_(i<j)Z_ij(u)| <= E_2,
    R_2^F >= -E_2.                                     (P2)

AP exclusion is NOT needed for (P1)-(P2). On the reachable logarithmic-
density windows in the current conditional iteration, with H chosen
using tau=a^2/log p, one has

    E_2=o(a^4 w mu), hence R_2^F>=-o(a^4 w mu).          (P3)

Thus the quadratic residual cannot provide cancellation at the required
main-term scale. The unresolved signed cancellation reduces to degrees
three and four. This statement concerns the specified weighted form and
the trivial factor on the current window, not arbitrary old unweighted
factor residuals.

## 2. Positive Fourier weights and their pushforward

Let eta=(H+1)/p. With normalized convolution,

    f=(1_[0,H]*1_[-H,0])/eta,
    fhat(t)=|hat(1_[0,H])(t)|^2/eta>=0,
    sum_t fhat(t)=1.

For multi-indices (l,m,n) in F_p^d x F_p^s x F_p^s assign weight

    W=product fhat(l_i) product fhat(m_j)fhat(n_j).

Define C=sum c_j m_j, B=sum xi_i l_i+sum b_j m_j, N=sum c_j n_j.
To avoid confusing the frequency B with the Boolean indicator, call its
value beta in the pushforward distribution below:

    lambda(C,beta,N)=sum_(indices with these values) W.

This is a nonnegative probability distribution, and

    F(x,h)=sum_(C,beta,N) lambda(C,beta,N)
                      e_p(2Cxh+Nh^2+beta h),
    mu=lambda(0,0,0)>=eta^k.                            (P4)

These are exact identities. All modular resonances are retained. No
coordinate independence or approximation is used.

## 3. Exact pair geometry: squares versus nondegenerate kernels

Fix i<j and put D=j-i, which is nonzero modulo p. Set
v=x+ih and z=x+jh. This is a bijection of F_p^2, with
h=(z-v)/D and x=(jv-iz)/D. A frequency summand in (P4) becomes

    [(N-2jC)v^2+(N-2iC)z^2
       +2((i+j)C-N)vz]/D^2 + beta(z-v)/D.              (P5)

If N=(i+j)C, this is q(z)-q(v), where
`q(y)=(C/D)y^2+(beta/D)y`. For real u its pair contribution is exactly

    |Q_u(C/D,beta/D)|^2,
    Q_u(c,t)=E_y u(y)e_p(-cy^2-ty).                    (P6)

If N!=(i+j)C, the mixed coefficient sigma in (P5) is nonzero. The matrix
with kernel e_p(A v^2+sigma vz+B z^2+alpha v+beta' z), acting by normalized
averaging in z, has operator norm p^(-1/2). To verify the factor of p,
remove its two diagonal unit-modulus multipliers. The remaining transform
is T_sigma h(v)=E_z h(z)e_p(sigma vz). Orthogonality gives

    E_v |T_sigma h(v)|^2=(1/p) E_z |h(z)|^2.

Consequently the absolute pair contribution is at most U/sqrt(p), by
Cauchy-Schwarz. This step uses the nonzero arithmetic mixed coefficient;
it is not an assertion about arbitrary entrywise-positive matrices.

Define explicitly

    nu_ij=sum_(C,beta)lambda(C,beta,(i+j)C),
    Z_ij=sum_(C,beta)lambda(C,beta,(i+j)C)
                          |Q_u(C/D,beta/D)|^2.          (P7)

The separable part is nonnegative; all remaining weights sum to 1-nu_ij.
The triangle inequality on this error proves (P1). The full pair form and
Z_ij are real, so the resulting two-sided scalar bound is valid.

Equivalently, the real symmetric pair kernel has a decomposition into a
positive sum of quadratic-phase rank-one projectors plus a self-adjoint
operator of norm at most (1-nu_ij)/sqrt(p). Thus its Loewner lower bound is
`-(1-nu_ij)p^(-1/2) I`. This follows by symmetrizing the same kernel; it
does not require the original unsymmetrized pair kernel to be self-adjoint.
For complex test vectors the projector phase can be conjugated; the real
quadratic form (P6) is unchanged. In the linear-only case C=N=0 always,
so nu_ij=1 and the full-group pair form is exactly PSD.

## 4. Proper-window correction and all diagonal terms

Restore the other two host indicators in a pair term:

    J_ij^Omega=E_(x,h) F u_i u_j product_(l notin {i,j})P_l.

Here u is zero outside Omega and |u|<=1. If u_i u_j is nonzero but one
of the other host indicators vanishes, then x+ih cannot be in Omega_-.
Indeed the polynomial changes relative to that slot are
`(l-i)L+(l^2-i^2)D_quad`, of magnitude at most 12H on the support of F.
An interior slot would force all four vertices into their interval lifts.
This argument is valid for wrapped circular intervals as well.

Let D_i(v)=E_h F(v-ih,h). The exact degree decomposition from (M6) is

    D_i(v)=mu+R_i(v)+E_i(v),
    R_i>=0, E_p R_i<=1/p, |E_i|<=epsilon_p.

It follows that

    |J_ij^Omega-J_ij|
       <= E_v 1_(Omega\Omega_-)(v)|u(v)|D_i(v)
       <= (mu+epsilon_p)b+1/p=beta_boundary.            (P8)

The choice of one of the two occupied slots only upper bounds the error;
there is no extra factor p or factor w. Sum the six inequalities (P1),
(P8) and multiply by a^2 to obtain (P2).

Every formula above includes h=0. Its contribution to each J_ij and
J_ij^Omega is U/p. Thus the exact diagonal in R_2^F is 6a^2 U/p. If
one uses diagonal-free pair forms, subtract this explicitly. The total
Boolean progression count for an AP-free set is aw/p, not zero.

## 5. Quantitative comparison at the target density

Let S=log(1/w), r=d+s, k=d+2s. Suppose a>=epsilon/log p,
S=o(log p), and

    r[S+log(48r)+loglog p+2log(1/a)]=o(log p).           (P9)

These conditions hold on the reachable windows of both the preceding
product-budget ledger and the improved ledger in
`DIRECT_INCREMENT_TRADEOFF_20261016.md`. Choose
`tau=a^2/log p`, `H=floor(tau wp/(48r))`. For large p, H>=1 and 2H<p,
because wp=exp(log p-o(log p)) and all remaining factors have logarithm
o(log p). Put `mu_0=(tau w/(48r))^k`; then mu>=mu_0=exp(-o(log p)).
The boundary estimate (M7) gives

    b<=a^2 w/(2log p)+2s(2+log p)/sqrt(p).

Using U=w a(1-a), the finite error satisfies

    E_2/(a^4 w mu)
       <=6[b/(a^2w) + b/(a^2w mu sqrt(p))
             +1/(p a^2w mu) +(1-a)/(a mu sqrt(p))].    (P10)

The first term is at most
`1/(2log p)+2s(2+log p)/(a^2w sqrt(p))`. Every other term tends to zero:
w and mu have reciprocals exp(o(log p)), 1/a=O_epsilon(log p), and
s=exp(o(log p)) by (P9). This proves (P3) uniformly in the coefficients.
Equation (P10), rather than an unspecified error, is the finite ledger.

At a=epsilon/log N, with p comparable to N, the improved direct-increment
ledger has r,S=O_epsilon(t^(-1/2)/R(t)+ell(t)^2), t=epsilon/log N,
ell(t)=log(2/t), R(t)=loglog(e^2/t). Its product is o(log p), and
r log(1/a)=o(log p). Thus (P9) holds; there is no polynomial or logarithmic
deficit in this particular quadratic-residual estimate.

## 6. The strictly smaller open signed inequality

For an actual Boolean AP-free set, exact expansion and diagonal subtraction
give

    R_3^F+R_4^F=aw/p-a^4T-R_1^F-R_2^F,
    T=(1+o(1))w mu,
    R_1^F=o(a^4 w mu).

Combining these with (P3) and `p a^3 mu->infinity` yields

    R_3^F+R_4^F <= -(1-o(1))a^4w mu.                  (P11)

The sufficient missing inequality, under failure of the phase selection
threshold of the improved iteration, is now

    R_3^F+R_4^F >= -(1/2)a^4w mu.                     (P12)

It involves only degrees three and four. If proved uniformly on reachable
hosts, it contradicts (P11) and supplies the selection step. It is OPEN.
Neither approximate pair PSD nor mixed-count positivity proves (P12).

The spectral upper bound is also explicit. If
`delta=max_(c,t)!=(0,0)|E_Omega(B-a)e_p(-cx^2-tx)|`, then Q_u=w times
this relative transform and Q_u(0,0)=0. Consequently, with
`Xi=sum nu_ij-6mu>=0`,

    -E_2<=R_2^F<=a^2 w^2 Xi delta^2+E_2.              (P13)

If Xi=0 there is no positive chirp part, and |R_2^F|<=E_2. Otherwise a
large positive R_2 gives the conditional lower bound
`delta^2>=(R_2^F-E_2)_+/(a^2 w^2 Xi)`. No lower bound on mu/w sufficient
to close the iteration is available, so this alone is not selection.

The abstract four-point distribution obtained by removing the fourth
Bernoulli factorial moment while keeping the first three unchanged is
still feasible for small a. It has centered R_1=R_2=R_3=0 and R_4=-a^4.
Thus the new pair bound does not remove the existing abstract quartic
obstruction. That distribution is not an actual arithmetic AP-free set.

## 7. Verification and proof limits

`verify_weighted_pair_20261016.py` independently tests the frequency
substitution, positive-square contribution, normalized matrix norm,
proper-window correction, Boolean diagonals, exact coefficient expansion,
and the old negative witness against the new lower bound. Exact rational
checks are separated from floating Fourier checks. The written proof is
uniform; finite tests are not an asymptotic inverse theorem.

This theorem makes a genuine one-sided improvement to the weighted R_2
estimate. It does not establish an absolute o(a^4w mu) bound, an arbitrary-
factor unweighted bound, a global quadratic inverse theorem, or the local
target. The next obstruction is the signed cubic-plus-quartic inequality
(P12) or an adequate phase correlation by another argument.
