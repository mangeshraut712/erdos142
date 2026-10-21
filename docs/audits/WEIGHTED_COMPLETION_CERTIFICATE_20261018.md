# Weighted completion energy and the exact missing spectral certificate

18 October 2026. Offline working note. **PROVED weighted extension and sufficient certificate; O2, (P12), and the local target remain OPEN.** No literature novelty is asserted. The hole projection itself extends the October 13 and 14 results; it is not a new selection theorem.

## 1. Four weighted channels and exact diagonal subtraction

Use the ORIGINAL weight F, mixed window Omega, and normalizations in `MIXED_QUADRATIC_TERMINAL_20261016.md`. Let P=1_Omega, B=1_A, w=|Omega|/p, 0<a=|A|/|Omega|<1, and u=B-a on Omega. All unmarked one-variable averages in this note are relative averages on Omega; E_p and E_(x,h) retain full-field normalization. Let I={0,1,2,3}. For j in I put

    q_j(v)=P(v) E_h 1_(h!=0) F(v-jh,h)
                          product_(i in I\{j}) B(v+(i-j)h).

These fields are zero-extended outside Omega. They are nonnegative. The three B factors already impose their own host conditions; P(v) imposes the fourth. Restoring h=0 gives exactly q_j+B/p. Actual cyclic AP exclusion gives

    B q_j=0,                 B(q_j+B/p)=B/p.             (W1)

There are FOUR channels here: the original F need not obey F(x,h)=F(x+3h,-h). Therefore endpoint or interior channels cannot be identified by reversal without changing the weight.

Set q=sum_j q_j, m_j=E_Omega q_j, m=sum_j m_j, k=q-m, and U_rel=a(1-a). Then exactly

    w m=M_3-4aw/p.                                      (W2)

Here M_3 has the definition in `BOOLEAN_OCCUPANCY_TERMINAL_20261017.md`. In particular the correction is 4aw/p, not 4a/p, before division by w. All identities remain true when m=0, in which case q=0 on Omega.

## 2. The inherited hole projection and a weighted six-point consequence

Define z=q-m(1-B)/(1-a) on Omega. The old hole projection now reads

    k=-m u/(1-a)+z,
    E_Omega z=0, Bz=0, <u,z>_Omega=0,
    <u,k>_Omega=-am,
    W:=E_Omega k^2=a m^2/(1-a)+E_Omega z^2,
    E_Omega q^2=m^2/(1-a)+E_Omega z^2.                  (W3)

Proof: (W1) says q is supported on the holes, whose relative measure is 1-a. Subtract its mean on those holes. Orthogonality follows because u is constant, equal to -a, on that support. This establishes every equality, including all factors of w. A vector version holds with m replaced by (m_0,...,m_3), giving a PSD remainder in the 4-by-4 covariance matrix; it is the same projection as the earlier two-channel result.

Here is an explicitly weighted arithmetic consequence. In the expansion of q(v)^2, let C(v) be the sum over ordered channel pairs (j,l) and nonzero directions (h,t) for which their occupied triples intersect. Let D(v) be the sum over the disjoint pairs. Retain the weights F(v-jh,h)F(v-lt,t), the six Boolean factors (with repeated factors interpreted Booleanly), and normalization p^-2. Thus q(v)^2=C(v)+D(v) exactly.

For fixed (j,l), an intersection requires

    (i-j)h=(s-l)t

for some i!=j, s!=l in I. Since p>3, each denominator is invertible. Up to changing the sign of h or t, the two possible offset sets are E={1,2,3} and M={-1,1,2}. Their ratio-set sizes are at most 7 for E/E, 8 for E/M, and 6 for M/M. These upper bounds hold for every p>3; modular coincidences only decrease the sizes. Actual AP exclusion removes two E/E ratios, t/h=2 and 1/2, and at least one E/M ratio, t/h=2: their occupied unions contain respectively {1,2,3,4}, {1/2,1,3/2,2}, and {1,2,3,4}, in units of h. For the reversed channel order take reciprocal ratios. All these APs are nondegenerate for p>3.

Thus the numbers of potentially nonzero intersecting ratios are at most 5,7,6 for E/E,E/M,M/M respectively. This is an upper bound, not an assertion that every remaining union is AP-free. For each fixed h and j, summing the second direction over these possibilities costs at most the corresponding number divided by p: its weight and Boolean factors are at most one, while the first summand is retained intact. Each endpoint channel has two endpoint and two interior partners; each interior channel has the converse. Put m_E=m_0+m_3 and m_M=m_1+m_2. Therefore

    0<=E_Omega C<=(24m_E+26m_M)/p<=26m/p,
    E_Omega D>=m^2/(1-a)-26m/p,
    E_Omega D-m^2>=a m^2/(1-a)-26m/p.                 (W4)

This treats each ordered channel pair separately. Disjoint pairs whose six-point union contains a 4-AP also contribute zero automatically. Consequently D counts only actual compatible disjoint six-point configurations. Equation (W4) forces a collective six-point excess whenever p a m/(1-a) is large. It neither localizes that excess to a small phase family nor bounds its sign after a chosen spectral projection. The ratio exclusions extend the previously recorded unweighted overlap geometry; the projection is not being claimed as new.

If m>=c mu a^3 for a fixed c>0, then the collision error relative to the forced excess is at most 26(1-a)/(c p mu a^4), which tends to zero on the current reachable hosts at a>=epsilon/log p. This conclusion is CONDITIONAL on the lower bound for m; none is proved here. The prior degree-six SOS results already contain the underlying hole-energy lower bound. What (W4) adds is its finite collision subtraction for the specified mixed weight and all four anchor channels.

## 3. A direct sufficient quadratic atomic certificate

For each nonconstant quadratic-or-linear phase chi_(c,t)(v)=e_p(cv^2+tv), let

    psi_(c,t)=chi_(c,t)-E_Omega chi_(c,t),
    delta=max_(c,t)!=(0,0) |<u,chi_(c,t)>_Omega|.

Relative phase vectors need not be orthogonal. Suppose m>0 and a FINITE representation has been constructed:

    k=sum_(gamma in Gamma) c_gamma psi_gamma+e,
    L=sum |c_gamma|,       epsilon=||e||_(L2(Omega)).

Complex coefficients and a complex error are allowed; k is real. Direct pairing and Cauchy-Schwarz prove

    a m <= delta L+sqrt(a(1-a)) epsilon.               (W5)

No Gram conditioning, factor refinement, or U^3 inverse theorem is used. In particular, for ANY specified R>0, if

    epsilon <= (m/2) sqrt(a/(1-a)),
    L <= m/(2 sqrt(a) R),                             (W6)

then L>0 and

    delta >= a^(3/2) R.                               (W7)

The positivity of L follows from the first condition and am>0; otherwise (W5) would imply am<=am/2. For a threshold c_epsilon a^(3/2)R(a), replace R by c_epsilon R(a). Thus a uniform divergent R(a), with (W6) on every eligible instance or an alternative successful low-completion branch, is sufficient for the already proved direct-cell iteration. This is a precise OPEN spectral sublemma, not a consequence of (W3) or (W4).

Equivalently, under failure delta<c_epsilon a^(3/2)R(a), every representation with that error tolerance must have

    L>m/[2 c_epsilon sqrt(a) R(a)].                   (W8)

This obstruction is homogeneous in the scale of F: multiplying all completion fields and m by the same constant does not change the required phase conclusion. There is no hidden replacement of relative correlations by full-group coefficients. On the full group the latter equal w times the former only after zero-extending u, as in the earlier notes.

A useful finite Gram version is available. For Gamma of size n, let G be its ACTUAL relative Gram matrix, P_Gamma the relative orthogonal projection, and W_Gamma=||P_Gamma k||_2^2. Assume the nonzero eigenvalues of G are at least lambda_*>0. The Moore-Penrose coefficient representation of P_Gamma k has

    L<=sqrt(n W_Gamma/lambda_*).

Indeed its squared coefficient norm is at most W_Gamma/lambda_*; Cauchy bounds l1 by sqrt(n) times l2. Therefore it suffices that

    ||(I-P_Gamma)k||_2^2 <= a m^2/[4(1-a)],
    n W_Gamma/lambda_* <= m^2/[4 a R^2].              (W9)

Only one phase is ultimately extracted by (W5), so this certificate does not add n constraints to the iterative host. Neither a useful n nor a positive controlled lambda_* is proved here. Singular and dependent phase vectors are allowed via the nonzero spectrum; no unjustified relative Parseval identity is used.

## 4. Low-completion branch and its exact deficit

Let E_1,E_2 be the finite first/pair errors in the existing notes, let U_p=wa(1-a), and beta=(mu+p^-1/2)b+1/p. From the Boolean expansion,

    M_3=4a^3T+3R_1/a+2R_2/a+R_3/a.

The direct cubic estimate already proved on October 17 gives |R_3|<=4a w delta U_p+4a beta. Combining with (W2), R_1>=-E_1, and R_2>=-E_2 yields

    delta >= [4a^3T-wm-3E_1/a-2E_2/a
                         -4beta-4aw/p]_+ /[4w^2a(1-a)].   (W10)

This is a proved conditional branch for actual Boolean AP-free sets. If m<=2a^3T/w and the displayed errors are small compared to a^3T, it gives only a constant times a^2 mu/w. Even in the favorable w/mu=O(1) case, this is smaller than a^(3/2)R(a) by a factor of order sqrt(a)/R(a). General reachable hosts give no lower bound on mu/w adequate to repair it.

There is an additional finite caveat: for the ORIGINAL tau=a^2/log p, beta/(a^3wmu) has leading upper bound 1/(2a log p), so it is not known to vanish at a~epsilon/log p. Choosing a different weight with tau=a^3/log p removes that boundary deficit but not the spectral deficit, exactly as in the October 17 note. We have not changed the weight here.

Thus (W6) plus a successful alternative when m is too small is a sharper explicit remaining task. The automatic hole identity, collision energy, and old cubic bound do not prove either premise and do not prove (P12).

## 5. Verification

`verify_weighted_completion_20261018.py` checks weighted diagonal subtraction, four-channel means, hole projection, collision bounds, and the finite spectral inequality on actual finite AP-free sets in full and proper mixed windows. Rational identities and inequalities use exact integer/Fraction arithmetic; phase decompositions use numerical linear algebra. These are finite consistency checks, not evidence for uniform spectral compression or an asymptotic counterexample.
