# Positive local laws and Fourier-cap localizers — 12 October 2026

**PROVED auxiliary theorem; SELECT and the local r4 target remain unresolved.**
This is an offline derivation, with no assertion of literature novelty.
It strengthens SELECT_CARDINALITY_RELAXATION_20261002.md by removing both
negative four-variable cylinder probabilities and missing linear-multiplier
Fourier-cap localizers. The construction is still a truncated moment
functional, not a global probability distribution or an AP-free set.

## 1. The strengthened theorem

Let Ω be any n-point subset of Z_p, p>3 prime, n>=200. Choose an integer
4<=k<=n/4, put a=k/n and ρ_j=(k)_j/(n)_j, and assume

    (n-k)(n-k-1) >= 400(k-2)(k-3).                        (1)

There is a real linear functional L on Boolean multilinear polynomials
of degree at most four such that:

(a) L(1)=1 and L(X_S)=ρ_|S| for |S|<=3.
(b) L(X_e)=0 for every distinct nonzero 4AP four-set e in Ω.
(c) L(q²)>=0 for every real polynomial q of degree at most two.
(d) L[(Σ_i X_i-k)X_T]=0 for |T|<=3.
(e) For every pair of disjoint subsets J,K with |J|+|K|<=4,

    L[product_{j in J}X_j product_{l in K}(1-X_l)]>=0.     (2)

Thus every restriction to at most four vertices is a genuine probability
law, with consistency on overlaps. AP four-sets assign probability zero
to the all-one outcome.

(f) Define the real quadratic polynomial

    |c_ξ|²=|n^-1 Σ_{i in Ω}(X_i-a)e_p(-ξi)|².

For every ξ and every real polynomial q of degree at most one,

    L[(τ-|c_ξ|²)q²]>=0 whenever τ>=120a/n.                (3)

The same single L satisfies all these inequalities simultaneously.
Its second moments still give

    L|c_ξ|²=a(1-a)/(n-1)(1-|E_Ω e_p(ξi)|²).              (4)

For H windows and a asymptotic to ε/log p, (1) holds eventually. Moreover
120a/n=o(a^(5/2)log(2/a)), so (3) applies even with the proposed SELECT
failure cap c a^(5/2)log(2/a), for any fixed c>0 eventually. The analogous
comparison holds for the weaker iterated-log target. This is feasibility
of the stated relaxation, not feasibility over actual Boolean sets.

## 2. Average the admissible trades

Retain the old construction of a trade at each AP root e={x_1,...,x_4}:
choose distinct y_1,...,y_4 outside e, uniformly conditioned on the fifteen
other transversals all being non-AP. For σ in {0,1}^4 let e_σ choose x_i
or y_i according to σ_i, and put

    t_e(S)=-Σ_σ(-1)^|σ| 1_{S=e_σ}.

The old proof gives pair codegree <=12, vertex degree <=4(n-1), and at
most n² AP edges. The probability of violating admissibility is at most

    48/(n-7)+144/(n-7)²+96n/(n-7)³+24n²/(n-7)^4 <1/2

for n>=200. Thus conditioning increases any event probability by at most
2. Every trade is balanced at each triple T: Σ_{S containing T}t_e(S)=0.

The change here is to take the exact average

    t(S)=Σ_{AP roots e} E[t_e(S)],
    L(X_S)=ρ_4(1+t(S)) for |S|=4.                        (5)

All expectations are finite uniform averages over admissible choices;
this defines rational moments without a limiting argument. On AP edges,
t=-1 exactly. Triple balancing and hence the cardinality identities remain
exact under averaging.

## 3. Nonnegative local distributions

Fix a NON-AP four-set S. Negative trade contributions use two or four
alternatives. With two alternatives, the root must intersect S in exactly
two points: at most 6*12=72 roots, and at most two ordered placements of
the remaining points. With four alternatives there are at most n² roots
and 24 placements. Consequently

    t(S)>=-A_n,
    A_n=288/[(n-4)(n-5)]
          +48n²/[(n-4)(n-5)(n-6)(n-7)] <1.              (6)

Positive contributions use one or three alternatives. At most 4*12=48
roots contain the selected triple of S, and at most 4*4n=16n roots contain
its selected single point. There are respectively one and six placements.
Hence

    t(S)<=P_n,
    P_n=96/(n-4)+192n/[(n-4)(n-5)(n-6)] <1.              (7)

All counting bounds include the factor 2 for conditioning. The displayed
functions decrease for n>=200, where A_n<.01 and P_n<.5. These facts follow
also by writing their terms as products of n/(n-j) and 1/(n-j), each
nonincreasing. Thus -1<=t(S)<=1 on EVERY four-set, including AP roots.

For a specified four-variable outcome with r ones, the original uniform
k-subset law has probability

    b_r=(k)_r(n-k)_{4-r}/(n)_4.

Only the fourth moment changes, so its new probability is

    b_r+(-1)^(4-r)ρ_4 t(S).                              (8)

Since k<=n/2, b_r>=ρ_4 for all r=0,...,4: compare the factors of
(n-k)_{4-r} with those of (k-r)_{4-r}. Equations (6)-(8) imply (2).
Lower-order probabilities are unchanged. Summing the outcomes gives one,
and marginalizing gives exactly the lower moments, so these are consistent
local laws. This does not assert a joint extension to all n vertices.

## 4. The PSD bound improves to a constant

Let N_P count trades in which a fixed pair P appears in a transversal.
As in the earlier proof,

    Σ_e Pr(P participates in t_e)
       <=12+48n/(n-4)+24n²/[(n-4)(n-5)] <100.            (9)

A participating trade has exactly four transversals containing P.
Therefore the perturbation Δ of the pair-monomial Gram block satisfies

    max_P Σ_Q |Δ_{P,Q}| <= 400ρ_4.                       (10)

Averaging avoids the earlier simultaneous high-probability pair-load bound
and its log n loss. Triple balancing gives ΔU=0 for the pair/vertex
incidence matrix U. On H=ker U*, the original fixed-k pair Gram matrix is
λI with

    λ=ρ_2-2ρ_3+ρ_4
     =ρ_2(n-k)(n-k-1)/[(n-2)(n-3)].

H is orthogonal to the constant and linear cross-blocks. Everything outside
H remains the genuine fixed-k moment matrix. Equation (10) proves full
PSD whenever λ>=400ρ_4, which is exactly (1).

## 5. Fourier caps with every linear-square multiplier

First work with the actual uniform k-subset functional L0. A linear
polynomial can, modulo ΣX_i=k, be written q=b+Q with
Q=Σ_i w_iX_i, real w_i, Σw_i=0. Then

    L0(q²)=b²+ν||w||²,  ν=ρ_1-ρ_2>=a/2.                (11)

Write z_i=(e_p(-ξi)-E_Ωe_p(-ξx))/n. Modulo cardinality, c_ξ=Z=Σz_iX_i.
We have Σz_i=0, ||z||²<=1/n, max|z_i|<=2/n, and
L0|Z|²=ν||z||²<=a/n.

An exact fourth-moment identity for zero-sum z,w is

    L0(|Z|² Q²)=λ[||z||²||w||²+2|Σz_iw_i|²]
                      +κ_4 Σ_i |z_i|²w_i²,
    κ_4=ρ_1-7ρ_2+12ρ_3-6ρ_4.                            (12)

To derive it, expand the four sums and group assignments by equality
partition of the four indices. Terms with a singleton vanish after the
zero-sum relations are imposed. The three pair partitions have coefficient
ρ_2-2ρ_3+ρ_4; the all-equal partition has coefficient κ_4. Equivalently,
Möbius inversion on partitions gives the coefficients 1,-7,12,-6 for the
all-equal contribution. Polarization gives the complex z version.

Use λ<=a² and κ_4<=a+12a³<=2a (a<=1/4); no absolute-value bound on κ_4
is needed. Then

    L0(|Z|²Q²)<=(3a²/n+8a/n²)||w||²
               <=10a/n L0(Q²),                          (13)

where ν>=a/2 and k=an>=4 are used in the last step. The pointwise inequality
(b+Q)²<=2b²+2Q² under the actual fixed-k distribution gives

    L0(|Z|²q²)<=20a/n L0(q²).                            (14)

Only degree-four terms change when passing to L. In ZQ the coefficient
of X_iX_j, i<j, is v_ij=z_iw_j+z_jw_i. Thus

    |(L-L0)(|Z|²q²)|=|v*Δv|
       <=400ρ_4 ||v||²
       <=800a^4/n ||w||²
       <=1600a³/n L0(Q²)
       <=100a/n L0(q²),                                 (15)

using ||v||²<=2||z||²||w||² and a<=1/4. Second moments are unchanged,
so (14)-(15) prove L(|c_ξ|²q²)<=120a/n L(q²), hence (3).
All reductions modulo cardinality multiply ΣX_i-k by polynomials of
degree at most three, covered by (d). They are valid for L, not merely L0.

## 6. Additional pair-literal localizers

If also n-k>=32(k-3), the same L satisfies

    L[m q²]>=0                                            (16)

for every product m of two literals on distinct vertices and every linear
q. Products with one literal also satisfy this, because all the relevant
moments have degree at most three and are unchanged from L0.

For proof, fix a triple T. A trade that contains T has exactly two
transversals containing it. Split AP roots by whether they contain three,
two, one or zero points of T. The sum of participation probabilities is
at most

    12+144/(n-4)+144n/[(n-4)(n-5)]
       +48n²/[(n-4)(n-5)(n-6)] <16,                      (17)

for n>=200. These four terms follow from at most 12, 36, 12n and n² roots,
respectively, and at most 1, 2, 6 and 24 alternative placements, with the
factor 2 for conditioning whenever alternatives are required. Therefore

    Σ_{S containing T}|ρ_4 t(S)| <=32ρ_4.                 (18)

For a fixed literal pair on vertices P, the perturbation of the matrix
L(m X_i X_j), i,j outside P, has off-diagonal entries plus or minus
ρ_4 t(P union {i,j}), and zero diagonal. Triple balancing makes every row
sum zero. Its norm is at most 32ρ_4 by (18). The unchanged constant/linear
cross blocks couple only to the constant vector. On its orthogonal
complement the original conditional matrix has eigenvalue

    (k)_3(n-k)/(n)_4             for two positive literals,
    (k)_2(n-k)_2/(n)_4           for one positive literal,
    k(n-k)_3/(n)_4               for two negative literals.

The smallest is the first when k<=n/4. It is at least 32ρ_4 exactly when
n-k>=32(k-3). The same invariant-subspace argument as before proves (16).
Variables of q belonging to P can first be replaced by their fixed zero
or one values, using Boolean identities after multiplication by m.

Thus, with this additional condition, all literal-product times square
localizers of total degree at most four are valid: zero literals use (c),
one or two literals use this section, and three or four literals use (e).
The extra density restriction still holds eventually at a~ε/log p.

### Products of cap inequalities and literal constraints

For completeness the same L also makes a cap times any two-literal
product nonnegative. Under L0, condition on that literal pattern on P.
The remaining coordinates are a uniform (k-r)-subset of n-2 points.
The conditional mean of Z has absolute value at most 4/n, and its
conditional variance is at most 2a/n. Since k>=4,

    L0(|Z|² m)<=6a/n L0(m).

The fourth-moment perturbation changes this by absolute value at most
8/n² times Σ_{S containing P}|ρ_4 t(S)|, hence at most 3200ρ_4/n².
Every two-literal event has L(m)>=ρ_2, and ρ_4/ρ_2<=a². Since n>=200
and a<=1/4, this error is at most 4a/n L(m). Thus

    L[(τ-|c_ξ|²)m]>=0 for τ>=10a/n.                       (19)

One-literal products are already covered by (3), taking q to be that
literal and reducing its square using Booleanity.

For two caps, positivity of quadratic squares gives
L(|c_ξ|²|c_η|²)>=0 (expand real and imaginary parts into four squares).
Using (4), for τ_ξ,τ_η>=120a/n,

    L[(τ_ξ-|c_ξ|²)(τ_η-|c_η|²)]
      >=τ_ξτ_η-(τ_ξ+τ_η)a/n>=0.                          (20)

These cover all products of cap and literal inequalities of total degree
at most four, with the square multipliers allowed at that degree.

## 7. Precise proof-system consequence

Consider a proposed degree-at-most-four polynomial contradiction composed
of sums of squares, Boolean equalities, cardinality equality with
multipliers of degree at most three, AP quartic equalities with constant
multipliers, Fourier-cap inequalities with sums of squares of linear
multipliers, and nonnegative four-variable cylinder polynomials. Under the additional
condition in section 6, all literal-product localizers of total degree
at most four can also be included.
Applying L makes every equality zero and every nonnegative term
nonnegative. It therefore cannot represent a negative constant. Equations (19)-(20)
allow products of the cap and literal inequalities as well. Thus, under
the section 6 condition, the obstruction applies to the full degree-four
preordering certificate system generated by these inequalities and the
listed equalities. Here "degree-four" refers to the total degree of each
certificate term before Boolean reduction.

This is an obstruction to that specified degree-four certificate system
at the target density. Unlike the earlier theorem, it includes both local
probability nonnegativity and all Fourier-cap localizers available with
linear-square multipliers. It does not rule out higher-degree certificates,
other arithmetic inequalities, or a direct analytic proof of SELECT.
In particular it does not convert moments into a single set realizing
all caps. The global extension problem remains substantive.

## 8. Verification

verify_select_positive_moments_20261012.py independently checks the
fourth-moment identity by exhaustive fixed-size subsets, constructs finite
rational mixtures of admissible trades, checks triple balancing and AP
zeros exactly, checks all distinct cylinder values exactly, certifies PSD
by absolute pair-row bounds, and numerically tests the entire matrix of
linear Fourier-cap multipliers at selected frequencies.

The finite mixtures are explicitly verified certificates; they are not
assumed equal to the exact all-choice averages used in the theorem.
The proof of the all-n assertion is sections 2-5. Computation supplies
checks, not an asymptotic substitute. SELECT, WSELECT, SIGNED, and
r4(N)=o(N/log N) remain unproved in this project.
