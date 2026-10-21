<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Referee audit of relative-window geometry and smoothing

Date: 2026-09-06. Scope: `RELATIVE_WINDOWS.md`, Sections 3–7, source lines 45–385, including formulas (1)–(18) and the unnumbered local U3 consequence. Offline mathematical audit; no internet, finite checker, or numerical experiment is used as proof. The source document is unchanged.

## Verdict and explicit domains

**PROVED:** Every numbered formula (1)–(18) survives direct mathematical audit in its intended domain. No substantive false formula was found in these sections. Some domain and interpretation qualifications should be made explicit; the original constants are conservative.

For the positive-density increment statements, explicitly assume `d >= 1`, `0 < a < 1`, and nonempty Omega. For the quantile lemma assume `epsilon > 0` and an integer `1 <= K <= n`. These are the minimal clean domain repairs. The rank-zero geometric formulas themselves are valid, but Section 6's literal choice `K = ceil(256 d 3^d)` is zero at rank zero and does not define its quantile partition. Setting K to at least one, or handling the rank-zero counting alternatives separately, is another possible repair. The factor `a^-3` already requires positive density. The size lower bound dividing by `1-a` must not be evaluated at a=1; the irregularity premise cannot occur there for positive epsilon.

“Retained A-mass” at source lines 226–227 means the **fraction of the original A retained**, namely `|A intersect Omega'|/|A|`, not ambient-normalized mass. State this explicitly.

The conclusions are hereditary geometrically: refined sets are in the same class and restrictions of A remain 4-AP-free. Application of the counting theorem at a later step is **CONDITIONAL** on that later window satisfying the theorem's size and density hypotheses. Geometry alone does not preserve those inequalities.

The document's historical claims about independent review or finite checks are **UNVERIFIED by this audit** and are not used. No novelty claim, asymptotic bound, inverse theorem, or global iteration conclusion follows from this report.

## Notation fixed for this audit

Let p>3 be prime and

    Lambda(F0,F1,F2,F3) = E_(x,t) product_(j=0)^3 Fj(x+jt),
    Fhat(r) = E_x F(x) e_p(-rx).

Every ambient expectation is normalized, while frequency sums are ordinary sums. Let W=1_Omega, B=1_A, n=|Omega|=wp, a=|A|/n, and g=B-aW. Thus g is zero outside Omega and has ambient mean zero.

The endpoint operator is

    (K_B H)(u) = E_v B((2u+v)/3) B((u+2v)/3) H(v).

Its kernel is real and symmetric. Division by 3 is in Z_p. The endpoint parametrization `(x,t) -> (u,v)=(x,x+3t)` is bijective, so `<F,K_B H>_p = Lambda(F,B,B,H)` for real F,H.

## Claim ledger

| Source | Classification | Qualification or proof location below |
|---|---|---|
| (1), relative endpoint expansion | PROVED | A is cyclically 4-AP-free for every nonzero difference; diagonal included |
| (2), Bernoulli baselines | PROVED | a is the fixed sampling parameter, not the realized random density |
| (3), fixed-size correction | PROVED | n>=4, k=an integer, 0<=k<=n |
| (4), coordinate-window definition and unique lifts | PROVED | Nonzero frequencies; integer intervals of diameter <p/3 |
| (5), endpoint-label criterion | PROVED | Full no-wrap proof below |
| (6), positivity/rank/count lower bound | PROVED | Operator includes both endpoint restrictions |
| (7), quadratic form | PROVED | Ambient normalization p^-2 is correct |
| (8), interval count | PROVED | Interval is rectified so cyclic 4-APs correspond to ordinary ones; Section 7's p>3N suffices |
| Label-class rectification after (8) | PROVED | Same frequencies after affine change; does not preserve middle-A factors on restriction |
| Row-box and quantile geometry | PROVED | Integer rounding of row endpoints understood; 1<=K<=n |
| (9), row discrepancy bound | PROVED | Partial cells are charged only once |
| (10), pair discrepancy estimate | PROVED | Symmetry is essential and holds |
| (11), increment/gain-size product | PROVED | epsilon>0, K>=16d3^d/epsilon, K<=n |
| (12), main spatial alternative | PROVED | Main theorem domain and size cutoff |
| (13), Fourier alternative | PROVED | Nonzero coefficient because ghat(0)=0 |
| (14), narrow-arc refinement | PROVED | Semicircle localization proof reconstructed below |
| (15), mixed alternative | PROVED | The proof actually gives the stronger constant 9/16 |
| (16), Fourier algebra norm | PROVED | Pullback by a nonzero frequency preserves that norm |
| Unnumbered local U3 bound | PROVED | Mixed endpoint inequality proved below; no inverse theorem used |
| (17), interval discrepancy constants | PROVED | Balanced 4096-block partition and N>=8192 |
| Plateau support, mass and approximation error | PROVED | p>3N prevents wrap; h=0 is included |
| Smoothed Fourier norm bound | PROVED | Decreasing-summand integral is valid at nonintegral breakpoints |
| (18), density-log Fourier signal | PROVED | Stronger constants are available, stated below |
| Reusing the counting alternatives indefinitely | CONDITIONAL | Every new size/rank cutoff must still hold |
| New asymptotic conclusion or novelty | UNVERIFIED / NOT ESTABLISHED | None is asserted by this audit |

## 1. Exact relative and random-sampling identities

Expanding only the endpoints gives, for arbitrary A subset Omega,

    M = Lambda4(B) - a Lambda(W,B,B,B)
        - a Lambda(B,B,B,W) + a^2 Phi.

Progression reversal `(x,t)->(x+3t,-t)` identifies the two triple terms. For a 4-AP-free set in Z_p, p>3, all nonzero-difference progressions have four distinct points and contribute zero. The diagonal contributes `|A|/p^2=aw/p`. This proves (1), including its normalization.

For random sampling, do not apply the AP-free specialization (1) to the random set. Instead use the general expansion above, or count pointwise. Write R=C-w/p. For t!=0 the four positions are distinct. The two, three and four sampled-point events have Bernoulli probabilities a^2,a^3,a^4; on t=0 the probability is a. Hence the first three expectations in (2) follow. On a nonzero-difference progression the two endpoint factors B-a are independent and centered, so the expectation of their product with the middle indicators is zero. At the diagonal its expectation is

    E[(B-a)^2 B^2] = a(1-a)^2.

This proves the final identity in (2). The realized g need not have mean zero under Bernoulli sampling, precisely as the source states.

For fixed-size sampling, distinct j-point events have probability rho_j=(k)_j/(n)_j. The general endpoint expansion gives the off-diagonal coefficient

    H4 = rho4 - 2a rho3 + a^2 rho2.

For n>=4, after factoring rho2, its numerator is

    (k-2)(k-3) - 2a(k-2)(n-3) + a^2(n-2)(n-3)
      = (1-a)[6(1-a)-an],

using k=an. This proves (3). The identity remains valid for k=0 or 1 because rho2=0; it does not require dividing by rho2. The diagonal term is again a(1-a)^2 w/p. Replacing this off-diagonal fixed-population correction by zero would be unjustified.

## 2. No-wrap geometry, counts and rectification

Each interval has diameter D_j<p/3<p, so every residue has at most one lift in it. Nonzero multiplication by xi_j is a bijection of Z_p and consequently injective on Omega.

For endpoints u,v in Omega, the two middle points are `(2u+v)/3` and `(u+2v)/3`. If, for example, the first middle point lies in Omega, write its jth lift as m_j. Then

    3 m_j - 2 t_j(u) - t_j(v) = 0 mod p.

All three lifts belong to I_j. The absolute value of the left side is at most 3D_j<p, so it is zero as an integer. Thus `t_j(u)=t_j(v) mod 3`. Conversely, equal endpoint residues modulo 3 make both convex averages of the lifts integers in I_j; invertibility of 3 identifies them with the actual middle-point coordinates. This proves (5), simultaneously in every coordinate. Indeed, membership of just one middle point already forces the criterion.

It follows that the kernel of `L_W=P_W K_W P_W` on Omega is one on pairs in a common label class and zero elsewhere. On each nonempty class it is the averaging matrix with normalization 1/p. Thus it has one positive eigenvalue n_l/p per class, and no negative eigenvalues. For real h supported in Omega,

    <h,L_W h>_p = p^-2 sum_l (sum_(x in Omega_l) h(x))^2.

This proves (6)–(7), since

    C = p^-2 sum_l n_l^2 >= p^-2 n^2 / 3^d.

Dependent or repeated coordinate frequencies can reduce the actual number of classes; they do not invalidate the bound.

For a rectified interval of N consecutive integers, write N=3m+r with r in {0,1,2}. Its residue classes have sizes m+1 in r cases and m in 3-r cases. Their square sum is

    r(m+1)^2+(3-r)m^2 = ceil(N^2/3).

This proves (8). The word “rectified” is necessary; the assertion is not about an arbitrary long cyclic interval. The narrow-window hypothesis or the explicit p>3N in Section 7 is sufficient.

For a fixed label class choose x0 in it and set x=x0+3z. Define

    s_j(z) = (t_j(x)-t_j(x0))/3,
    I'_j = [ceil((l_j-t_j(x0))/3), floor((u_j-t_j(x0))/3)].

The label condition makes s_j integral, and `s_j(z)=xi_j z mod p`. These equivalences work in both directions, so the affine pullback of the class is exactly the same-frequency window with intervals I'_j. Their diameters are at most D_j/3. This proves the rectification statement. It does not identify a restricted mixed form with the original negative block, because middle-point membership in A is a separate condition.

## 3. Row boxes and the quantile-discrepancy lemma

Fix y in Omega. Requiring `2y-z` and `2z-y` to belong to Omega is equivalent in coordinate j to

    t_j(z) in I_j
      intersect [2t_j(y)-u_j, 2t_j(y)-l_j]
      intersect [(l_j+t_j(y))/2, (u_j+t_j(y))/2],

with integer rounding of the last interval. Necessity uses the same no-wrap argument: discrepancies such as `2t_j(y)-t_j(z)-t_j(2y-z)` have magnitude at most 2D_j<p. Sufficiency follows by using the displayed integer affine expressions as lifts. Thus each row is an axis-aligned coordinate box intersected with Omega.

For 1<=K<=n, sort the n distinct lifts in each coordinate and cut into K consecutive groups of sizes at most ceil(n/K). Place integer interval boundaries between successive groups. This gives K contiguous bins covering I_j, each of that mass bound. Gaps in the lift set cause no obstruction. Their common refinement has at most K^d nonempty same-frequency windows.

For a row box, at most two bins per coordinate can cross its boundary. Every partial cell lies within the union of these boundary bins, a set of size

    U <= 2d ceil(n/K) <= 4dn/K.

Let d_D=sum_D g for a partition cell D, and P=sum_D max(d_D,0). Since sum_Omega g=0, the total magnitude of negative cell discrepancies is also P.

For the upper bound on a row sum, let E be its intersection with a partial cell D. Then

    sum_E g <= d_D + a|D\E|.

Summing d_D over all full and partial cells charges each cell at most once, and its result is at most P. The remaining term is at most aU. For the lower bound, full cells contribute at least -P, and partial intersections satisfy `sum_E g >= -a|E|`, totaling at least -aU. Therefore

    |sum_z g(z) R_W(y,z)| <= P + 4dan/K.

This proves (9). In particular, no extra P term is needed: the partial-cell accounting in the source is valid.

Symmetry of R_W and B=a+g on Omega imply the exact algebraic identity

    Phi-a^2 C = p^-2 sum_y (B(y)+a) (R_W g)(y).

The nonnegative multiplier B+a has total sum 2an, so (9) gives (10).

Suppose `|Phi-a^2C| >= epsilon a^2C`, epsilon>0, and K>=16d3^d/epsilon. Since C>=w^2/3^d, (10) yields

    P/n >= epsilon a/(2*3^d)-4da/K
         >= epsilon a/(4*3^d).

Set t=epsilon a/(8*3^d). The positive cells with gain less than t have total weighted gain at most t. Therefore at least t of weighted gain remains on cells whose gains are at least t. Among at most K^d cells, some has both

    Delta >= t,        mu Delta >= t/K^d.

This proves (11). Since Delta<=1-a, `mu >= t/[K^d(1-a)]`. Furthermore

    |A intersect Omega'|/|A|
       = mu(a+Delta)/a >= mu Delta/a
       >= epsilon/(8*3^d K^d).

These are genuine one-step size and mass bounds, with no implied later cutoff guarantee.

## 4. Main relative alternatives and semicircle localization

Take K=ceil(256d3^d), d>=1, and n>=max(K,8*3^d a^-3). If the pair-count error exceeds a^2C/16, the preceding lemma with epsilon=1/16 proves (12).

Otherwise

    15a^2C/16 <= Phi <= 17a^2C/16.

If Sigma<7a^3C/8, then U=Sigma-aPhi<-a^3C/16, and `U=<g,K_B W>_p`.

The exact Fourier matrix is

    (K_B W)hat(r)
       = sum_s What(s) Bhat(2r+s) Bhat(-r-2s).

To verify it, write u=2y-z and v=2z-y in the endpoint expression, expand W(v), and collect the y,z frequencies. For each fixed s, both r-indexed arguments of Bhat are bijections. Cauchy–Schwarz and Parseval give

    sum_r |Bhat(2r+s) Bhat(-r-2s)| <= E B^2 = aw.

Consequently `||(K_B W)hat||_1 <= aw A(W)`. If

    eta = max_(r!=0) |ghat(r)|/w,

then ghat(0)=0 implies

    |U| <= a w^2 eta A(W).

It follows that

    eta > a^2 C/[16 w^2 A(W)] >= a^2/[16*3^d A(W)],

proving (13), with a slightly stronger shape-sensitive first bound.

Here is a standalone proof of the conversion used for (14). Let f=B-a on Omega, with relative uniform expectation, and suppose `|E_Omega f e(theta x)|>=eta`. Define

    H(t)=E_Omega f(x) 1_[0,1/2)((theta x-t) mod 1).

This is real, and balance gives H(t+1/2)=-H(t), ignoring boundary parameters of measure zero. Direct integration of the half-circle indicator gives

    |integral_0^1 H(t)e(t)dt| >= eta/pi.

Rotate the coefficient to be real. Since integral_0^1 |cos(2pi t)|dt=2/pi,

    eta/pi <= (2/pi) ||H||_infinity.

Antisymmetry supplies a positive value at least eta/2. Since H has finitely many values away from boundary points, one can choose such a nonboundary translated semicircle. Split it into two disjoint quarter-arcs. Their discrepancies sum to H(t), so one has `mu Delta >= eta/4`. Its Delta is at least eta/4 because mu<=1. For theta=xi/p, its phase points form a consecutive integer interval of diameter at most p/4, strictly below p/3. Intersecting with Omega gives a valid window of rank at most d+1. Combining with (13) proves (14).

In the remaining case Sigma>=7a^3C/8, the size hypothesis gives

    aw/p <= a^4 C/8,

because their ratio is at most 3^d/(a^3 n). Formula (1) then gives

    M <= a^4 C(1/8-7/4+17/16) = -9a^4C/16.

Thus (15) holds with room to spare. This argument does not extract an arithmetic increment from the negative mixed form.

## 5. Fourier algebra norm and the U3 consequence

For a consecutive interval J of m>=1 residues, at a centered nonzero frequency k,

    |1_J hat(k)| <= min(m/p, 1/(2|k|)).

The geometric-sum formula gives the first term and `|sin(pi k/p)|>=2|k|/p` gives the second. Summing the decreasing bound, including the zero coefficient, yields at most 3+log m (indeed a slightly smaller constant suffices). An affine shift changes only Fourier phases; nonzero multiplication permutes frequencies. Products in physical space become Fourier convolutions, whose l1 norm is submultiplicative. Hence

    A(W) <= product_j (3+log |I_j|) <= (3+log p)^d.

Nonemptiness gives A(W)>=1 by Fourier inversion at any point where W=1. This proves (16). The per-coordinate coefficient estimate is understood after the frequency permutation; it need not hold with the same numerical index before that permutation.

For completeness, the mixed endpoint inequality needed for the unnumbered U3 consequence can be proved without a prior audit. For a real function g and arbitrary real B, set

    J(y,z)=g(2y-z)g(2z-y),        b_B=E B^2.

Two applications of Cauchy–Schwarz to `E_(y,z) B(y)B(z)J(y,z)` give

    |Lambda(g,B,B,g)|^4 <= b_B^4 Q,
    Q=E_(y,y',z,z') J(y,z)J(y,z')J(y',z)J(y',z').

Write y'=y+h,z'=z+k, u=2y-z,v=2z-y. The map to u,v has determinant 3, so they are independent uniform variables. With

    F_g(s,t)=E_x g(x)g(x+s)g(x+t)g(x+s+t),

expansion gives `Q=E_(h,k) F_g(2h,-k)F_g(-h,2k)`. Cauchy–Schwarz and the invertibility of 2 yield

    Q <= E_(h,k) F_g(h,k)^2 = ||g||_(U3)^8.

Thus

    |M| <= (aw) ||g||_(U3)^2.

The mixed alternative gives `||g||_(U3)^2 >= a^3w/(2*3^d)`, as stated, or the stronger `9a^3w/(16*3^d)` using the bound actually proved above. This is a norm consequence only.

## 6. Interval discrepancy and smoothing, including boundary cases

Assume Omega=[0,N-1], p>3N, and N>=max(8192,24a^-3). Partition Omega into K0=4096 consecutive blocks with lengths floor(N/K0) or ceil(N/K0). Each length is at least N/8192.

If no block has gain at least tau a, tau=1/256, its A-mass is at most `(1+tau)a` times its length. The total positive block discrepancy is at most tau aN; balance makes the total negative magnitude equal to it. A completed-block prefix therefore has discrepancy in [-tau aN,tau aN]. For a partial final block the discrepancy has magnitude at most its A-mass or a times its length, and hence at most `(1+tau)a ceil(N/K0)`. Since ceil(N/K0)<=2N/K0,

    D <= [tau+2(1+tau)/4096]aN.

Every completion row is an ordinary interval, so its g-sum is a difference of two prefixes and has magnitude at most 2D. The symmetric pair expansion then gives

    |Phi-a^2C| <= 4aND/p^2.

Using `C=ceil(N^2/3)/p^2 >= N^2/(3p^2)` proves

    |Phi-a^2C|/(a^2C)
      <= 12tau+24(1+tau)/4096
       = 6915/131072 < 1/16.

This proves (17). If Sigma<7a^3C/8, the weaker rounded estimate gives U<-a^3C/16<=-a^3w^2/48.

Now set z=a^2N/384 and h=floor(z), M0=N+2h and H=2h+1. Let J=[-h,N-1+h] as a cyclic interval, and

    V(x)=H^-1 sum_(t=-h)^h 1_J(x-t).

Since h<=N/384, the full support lies in [-2h,N-1+2h], whose length is N+4h<p. Thus there is no wrap overlap. For every x in [0,N-1], every x-t belongs to J, so V(x)=1. Elsewhere V is between 0 and 1. This proves V>=W, V=1 on W, and

    E(V-W)=(M0-N)/p=2h/p.

For every endpoint u,

    (K_B 1)(u)<=E_v B((2u+v)/3)=aw.

Positivity and symmetry of K_B, together with |g|<=1, therefore imply

    |Lambda(g,B,B,V-W)|
      <= aw E(V-W)=2awh/p <= a^3w^2/192.

The original negative U remains negative. In fact its magnitude is at least a^3w^2/64, stronger than the source's a^3w^2/96, because 1/48-1/192=1/64.

The Fourier transform of V is the product of the transform of 1_J and the normalized transform of the H-point averaging interval. Thus, for centered k!=0,

    |Vhat(k)| <= min(M0/p,1/(2|k|)) min(1,p/(2H|k|)).

To justify the claimed l1 estimate rigorously, call the displayed decreasing function of |k| F(t). A decreasing nonnegative function satisfies `sum_(k>=1) F(k) <= integral_0^infinity F(t)dt`. Since M0>=H, its breakpoints are A=p/(2M0) and B=p/(2H). Twice the integrals over [0,A], [A,B] and [B,infinity] are respectively

    1,        log(M0/H),        1.

The zero coefficient is M0/p<=1. Hence

    ||Vhat||_1 <= 3+log(M0/H).

This covers noninteger breakpoints, breakpoints below 1, and the finite frequency cutoff by an upper bound; no unjustified discrete-to-continuous equality is being used.

Finally, for every z>=0, `2floor(z)+1>=z`. Therefore H>=z, and for a>0

    M0/H = N/H + 2h/H <= 384/a^2+1 <= 384/a^2+2.

This also includes h=0. Applying the already proved Fourier-matrix estimate with V in place of W gives

    |Lambda(g,B,B,V)| <= a w^2 eta ||Vhat||_1.

It proves (18), and even the stronger constant 64 in place of 96. No function g, density a, or ambient modulus is replaced in this smoothing operation.

## 7. Precise strongest corollaries retained in this audit

The following are the directly proved relative conclusions. They are one-step results, with no novelty or asymptotic claim.

### General narrow-coordinate window

Under the explicit positive-rank/density hypotheses and size cutoff of Section 6, at least one holds:

1. A same-frequency window has `Delta>=a/(128*3^d)` and `mu Delta>=a/(128*3^d K^d)`.
2. A nonzero relative Fourier coefficient has

       eta >= a^2 C/[16w^2 A(W)] >= a^2/[16*3^d A(W)].

   A rank-at-most-d+1 narrow window has both `mu Delta>=eta/4` and `Delta>=eta/4`.
3. `M<=-9a^4 C/16`. Consequently `||g||_(U3)^2>=9a^3 C/(16w)>=9a^3w/(16*3^d)`.

### Initial rectified interval

Let

    delta0=6915/131072,
    L(a)=3+log(384/a^2+2).

Under N>=max(8192,24a^-3) and p>3N, at least one holds:

1. A consecutive block of length at least N/8192 has density gain at least a/256.
2. A nonzero relative Fourier coefficient has

       eta >= a^2 [(1/8-delta0) C/w^2 - 1/192]/L(a)
            >= (7421/393216) a^2/L(a).

   This follows by retaining (17)'s actual discrepancy constant: in the low-Sigma case `U<=-(1/8-delta0)a^3C`, and the same smoothing costs at most a^3w^2/192. It implies the original (18) and the simpler 64-denominator improvement. The quarter-arc conversion gives a rank-at-most-two narrow window with `mu Delta>=eta/4`.
3. `M<=-(75005/131072)a^4C`, since

       1/8-7/4+(1+delta0)=-(5/8-delta0)
                         =-75005/131072.

These constants keep the source's fixed 7/8 triple threshold; no global optimization of that threshold is claimed.

## Remaining obstruction

The interval Fourier loss depends on density rather than ambient length, as a valid explicit inequality. Its consequence still adds a coordinate unless another conversion is proved. The general-window Fourier cost A(W), rank factor 3^d, and size cutoff remain in force at every later application. The mixed alternative still provides no arithmetic density increment. These sections therefore do not prove `r4(N)=o(N/log N)`, do not establish a sufficient global iteration, and do not support an asymptotic or novelty upgrade.
