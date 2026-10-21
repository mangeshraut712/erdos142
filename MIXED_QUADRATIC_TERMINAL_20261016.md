# A terminal counting theorem for mixed linear and quadratic windows

16 October 2026. Continuation of the logarithmic-density cycle. Offline. **PROVED partial theorem.**
The target r_4(N)=o(N/log N) remains open. No literature novelty is asserted.

## 1. Statement and exact normalization

Let p>3 be prime. Let Omega be a nonempty intersection of d linear and s
quadratic interval constraints on F_p:

    xi_i x in I_i                       (1<=i<=d, xi_i!=0),
    q_j(x)=c_j x^2+b_j x+e_j in J_j      (1<=j<=s, c_j!=0).

The intervals are circular residue intervals with specified consecutive
integer lifts. Repeated or arithmetically dependent constraints are allowed.
Put r=d+s>=1, k=d+2s, n=|Omega|, w=n/p, K=2+log p. Let A subset Omega
be cyclically 4-AP-free for nonzero differences, and a=|A|/n.

Choose 1<=H with 2H<p. Put eta=(H+1)/p and define the cyclic tent

    f(t)=(H+1-|t|)/(H+1) for the centered lift |t|<=H,
         0 otherwise.

There is a positive number mu, defined explicitly in (M3) below, with
mu>=eta^k, such that

    a <= 3/4 + 6rH/(wp) + sK/(2w sqrt(p))
                 + 1/(2mu sqrt(p)) + 5/(4wp mu).          (M1)

Consequently one may replace mu in the denominators by eta^k. No
independence of coordinate phases is assumed. In particular, consider
any sequence of these windows for which

    r=o(sqrt(log p)),  log(1/w)=o(sqrt(log p)).

Then every AP-free subset satisfies a<=3/4+o(1), uniformly over the
polynomial coefficients and interval positions. The proof supplies
finite error terms and also covers more asymmetric rank/size regimes.

## 2. A positive Fourier weight

Use hat h(t)=E_x h(x)e_p(-tx), with normalized averages. For V={0,...,H},

    f=(1_V * 1_(-V))/eta,
    hat f(t)=|hat 1_V(t)|^2/eta >=0,
    sum_t hat f(t)=f(0)=1, hat f(0)=eta.                  (M2)

Thus the Fourier coefficients form a probability distribution, even
though their index set is all of F_p. There is no Fourier truncation.

For multi-indices l in F_p^d and m,n in F_p^s put

    W(l,m,n)=product_i hat f(l_i) product_j hat f(m_j)hat f(n_j),
    C(m)=sum_j c_j m_j,
    B(l,m)=sum_i xi_i l_i+sum_j b_j m_j,
    N(n)=sum_j c_j n_j,
    mu=sum_(C=0,B=0,N=0) W(l,m,n).                       (M3)

All equations are in F_p. Nonnegative weights sum to 1, and the all-zero
multi-index contributes eta^k. This proves 1>=mu>=eta^k>0.
An alternative formula, useful for exact computation, is

    mu = [E_(t,z) product_i f(xi_i t)
                         product_j f(b_j t+c_j z)]
         [E_y product_j f(c_j y)].                      (M4)

Expanding each f and averaging t,z,y imposes exactly the three conditions
in (M3). The formulas include all arithmetic relations among generators.

## 3. Degree decomposition with an averaged exceptional contribution

For a starting point x and difference h define

    F(x,h)=product_i f(xi_i h)
           product_j f((2c_j x+b_j)h) f(c_j h^2).

This weight is in [0,1] and F(x,0)=1. For a slot i in {0,1,2,3}, put

    D_i(v)=E_h F(v-ih,h).

Fourier expansion gives quadratic and linear coefficients in h

    A_i=N(n)-2i C(m),
    L_v=2v C(m)+B(l,m).                                  (M5)

The modes with C=B=N=0 have constant phase for every v and every i;
their contribution is precisely mu. If C=0 but these conditions fail,
the phase is nonconstant for all v. If C!=0, the phase is constant only
when A_i=0 and v=-B/(2C). Define

    R_i(v)=sum_(C!=0, N-2iC=0, 2vC+B=0) W(l,m,n).

Then

    D_i(v)=mu+R_i(v)+E_i(v),
    R_i(v)>=0, E_v R_i(v)<=1/p, |E_i(v)|<=p^(-1/2).     (M6)

Indeed each multi-index with C!=0 can contribute to R_i at only one
vertex. Its nonnegative weight is included in a total weight at most 1.
Nonconstant linear phases average to zero. Nonconstant quadratic phases
have normalized magnitude p^(-1/2), so their total absolute contribution
is at most p^(-1/2) by (M2). D_i, mu and R_i are real, hence E_i is real.

For completeness, the Gauss bound follows by expanding the square of
sum_h e_p(Ah^2+Bh) and writing the two variables as h and h+t. When
A!=0, the sum over h vanishes for every t!=0, leaving p for the squared
magnitude. This proof applies for every nonzero A, uniformly.

Equation (M6) is the point where treating the generators as independent
would be incorrect. Persistent resonances increase mu; exceptional
resonances have total vertex-average at most 1/p. There may be many
exceptional vertices, and no bound on their number is needed.

## 4. Erosion, wraparound, and the progression count

Shrink both ends of each interval lift by 12H residues; if too short,
replace it by the empty interval. Let Omega_- be the intersection of
these shrunken constraints, w_-=|Omega_-|/p, and b=w-w_-.

For a nonzero linear phase, a removed boundary set of at most 24H
residues has preimage density at most 24H/p. For a quadratic phase,
the removed set is the union of at most two intervals with total size
at most 24H. Each interval indicator has Fourier l1 norm at most K:
the geometric-sum bound |hat 1_I(t)|<=1/[2 min(t,p-t)] and the harmonic
sum prove this. The Gauss estimate therefore gives

    0<=b<=24rH/p+2sK/sqrt(p).                            (M7)

These bounds also apply when a whole short interval is removed.

If F(x,h)>0, choose centered representatives of all its arguments in
[-H,H]. The exact polynomial identity is

    q_j(x+th)=q_j(x)+t(2c_jx+b_j)h+t^2 c_jh^2.

For 0<=t<=3 the signed change is at most 12H; the linear change is
at most 3H. Thus x in Omega_- and F(x,h)>0 imply that all four
vertices are in Omega. This is a statement about the specified integer
lifts, so it does not assume absence of cyclic wraparound elsewhere.

Writing P=1_Omega, let

    T=E_(x,h) F(x,h) product_(j=0)^3 P(x+jh).

Using (M6), positivity of R_0, and the preceding implication gives

    T>=E_x 1_(Omega_-)(x) D_0(x)
      >=w_-(mu-p^(-1/2)).                               (M8)

## 5. Exact hitting argument

Let h_i^ne(v)=E_h 1_(h!=0) F(v-ih,h)
                         product_(j!=i)P(v+(j-i)h),
and h^ne=sum_i h_i^ne. At h=0 the weighted progression contributes
exactly w/p because F(x,0)=1. At every nonzero h its four vertices
are distinct and at least one is a hole in Omega\A. Hence

    E_v (P-1_A)(v) h^ne(v) >= T-w/p.                    (M9)

Since h_i^ne<=D_i, (M6) gives the upper bound

    E_v (P-1_A)(v) h^ne(v)
       <=4(1-a)w(mu+p^(-1/2))+4/p.                     (M10)

Combining (M8)--(M10) yields the stronger finite inequality

    a <= 1-[w_-(mu-p^(-1/2))-(w+4)/p]
                   /[4w(mu+p^(-1/2))].                 (M11)

Subtract 3/4 and use w+w_-<=2w, w+4<=5. It follows that

    a<=3/4+b/(4w)+1/(2mu sqrt(p))+5/(4wp mu).

Substitution of (M7) proves (M1). Bounds with right side above 1
remain valid but supply no contradiction.

## 6. Uniform quantitative terminal regime

For 0<tau<=1, choose H=floor(tau wp/(48r)), assuming tau wp>=48r.
Then H>=1 and 2H<p. Since H+1>tau wp/(48r),

    mu >= mu_0 := (tau w/(48r))^k,
    a <= 3/4+tau/8+sK/(2w sqrt(p))
                    +1/(2mu_0 sqrt(p))+5/(4wp mu_0).   (M12)

An exact sufficient asymptotic regime is

    tau ->0, tau wp/r ->infinity,
    sK/(w sqrt(p))->0,
    sqrt(p) mu_0 ->infinity, wp mu_0 ->infinity.         (M13)

For the rank/size hypotheses in section 1 set tau=1/log p. Write
L=log p and S=log(1/w). Then

    log(1/mu_0)=k[S+log(48r)+log L]=o(L),

because k<=2r=o(sqrt L), S=o(sqrt L), and r log L=o(L).
Every error in (M12) tends to zero and its size hypotheses hold.
This proves the stated terminal theorem for growing mixed factors.

For one quadratic interval there is also a stronger small-host regime.
Here r=s=1, k=2, mu=eta^2 exactly. For p>=67 choose
H=floor(p^(5/6)w^(1/3)); then 1<=H and 2H<p. Equation (M1) gives

    a<=3/4+(13/2)w^(-2/3)p^(-1/6)
             +K/(2w sqrt(p))+(5/4)w^(-5/3)p^(-2/3).     (M14)

Thus p w^4 ->infinity suffices for a<=3/4+o(1). For phase density beta,
|w-beta|<=K/sqrt(p), so beta p^(1/4)->infinity suffices as well.
This improves the size condition of the preceding single-host theorem.

## 7. Regularized first residual on a mixed host

This additional consequence removes first-order boundary bias from the
weighted expansion with the trivial factor; it does not control higher
residual terms. Define h_i as h_i^ne with h=0 restored. If v in Omega_-
and F(v-ih,h)>0, all four phases stay in their intervals: their changes
relative to slot i are (j-i)L+(j^2-i^2)D, of size at most 12H.
Thus h_i(v)=D_i(v) in Omega_-, and 0<=h_i<=D_i everywhere. From (M6),

    E_v P(v)|h_i(v)-mu|
       <=mu b+p^(-1/2)(w+b)+2/p.                        (M15)

To prove this, compare h_i to D_i: the integrated discrepancy is supported
in Omega\Omega_- and is at most (mu+p^(-1/2))b+1/p. The comparison
of D_i to mu on Omega costs at most wp^(-1/2)+1/p. Add the two.

Put u=1_A-aP, so E_p u=0 and |u|<=P. In the expansion of the weighted
4-AP form at aP, the linear residual R_1^F therefore obeys

    |R_1^F|<=4a^3[mu b+p^(-1/2)(w+b)+2/p].             (M16)

In the reachable regime r,S=o(sqrt(log p)), with a>=epsilon/log p and
tau=a^2/log p in (M12), division by a^4 w mu shows that this error
tends to zero uniformly. Indeed b/(aw)<=tau/(2a)+2sK/(aw sqrt p),
log(1/mu_0)=o(log p), and all remaining factors 1/a are O_epsilon(log p).
Also (M8) and T<=w(mu+p^(-1/2))+1/p imply T=(1+o(1))w mu.

The remaining signed counting question concerns R_2^F+R_3^F+R_4^F.
Neither their control nor spectral concentration follows from (M16).

## 8. Proof boundaries

The theorem handles arbitrary dependence among polynomial constraints.
It proves a terminal contradiction for intersections actually produced by
linear or quadratic quarter-arc refinement when their cumulative ledger
satisfies (M13). It does not supply the refinements. In particular it is
not an inverse theorem, and it does not turn a U^3 norm into a quadratic
phase correlation.

Verification is in `verify_log_density_attack_20261016.py`. Exact rational
weights, degree counts and diagonal subtraction are checked separately
from floating spectral identities. The proof above, not the finite tests,
establishes the statements uniformly in p and the ranks.
