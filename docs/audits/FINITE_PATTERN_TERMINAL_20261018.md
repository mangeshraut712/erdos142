# A twelve-slot mixed-window terminal ceiling of 7/11

18 October 2026. Offline continuation. **PROVED partial theorem.**
The target r_4(N)=o(N/log N), DIRECT-Q-GAIN, and (P12) remain OPEN.
This extends the pair argument to several overlapping four-term
progressions inside one fixed longer progression. It improves a terminal
constant and supplies no structural phase-selection step. No literature
novelty is asserted.

## 1. Setup and the general finite-pattern theorem

Keep the mixed-window definitions, tent f, nonnegative progression weight
F(x,h), persistent baseline mu, and normalizations of
`MIXED_QUADRATIC_TERMINAL_20261016.md` and
`WEIGHTED_PAIR_REDUCTION_20261016.md`. Thus r=d+s>=1, p>3 is prime,
1<=H and 2H<p, Omega is nonempty, P=1_Omega, w=|Omega|/p,
A subset Omega is cyclically nonzero-4AP-free, B=1_A,
a=|A|/|Omega|, and u=B-aP. In particular

    E_p u=0,       U=E_p u^2=wa(1-a).

Fix an integer m with 4<=m<p. Suppose every four-term-AP-free subset
of {0,...,m-1} has at most R elements, with 1<=R<m. Here the finite
integer progressions use positive differences; their images in F_p have
nonzero differences because p>m. The constants m and R are fixed in
the asymptotic statement below.

For P_i=P(x+ih), B_i=B(x+ih), define

    T_m=E_(x,h) F product_(i=0)^(m-1) P_i,
    M_1=E_(x,h) F sum_i B_i product_(j!=i)P_j,
    M_2=E_(x,h) F sum_(i<j) B_i B_j product_(l!=i,j)P_l,
    S_1=M_1-ma T_m,
    C_2=M_2-(m-1)a M_1+binom(m,2)a^2 T_m.             (F1)

The letter C_2 here denotes the sum of centered pair terms in an
m-slot auxiliary count; it is not the original degree-two residual of
the four-slot expansion. Likewise T_m need not equal the original T.

Erode each defining interval by m(m-1)H residues at each end, using
its specified consecutive lift and making the result empty if too
short. Let Omega_-^(m) be the resulting intersection and put
b_m=|Omega\Omega_-^(m)|/p, eps=p^(-1/2), K_p=2+log p. Then

    b_m<=2m(m-1)rH/p+2sK_p eps,                       (F2)
    (w-b_m)(mu-eps)<=T_m<=w(mu+eps)+1/p,
    T_m>=w/p>0.                                      (F3)

For every 0<=i<j<m let nu_ij be the nonnegative Fourier weight of the
resonant plane N=(i+j)C, exactly as in (P7) of the pair theorem. Define

    D_m=mu b_m+eps(w+b_m)+2/p,
    beta_m=(mu+eps)b_m+1/p,
    E_1=m D_m,
    E_2=binom(m,2)beta_m
                   +(binom(m,2)-sum_(i<j)nu_ij)U eps. (F4)

One may replace the last coefficient by binom(m,2) for a weaker fully
explicit E_2. Then

    |S_1|<=E_1,            C_2>=-E_2.                 (F5)

For a>0 the finite terminal inequality is

    (ma/2)[(m-1)a-(R-1)]T_m
      <=[(R-1)/2-(m-1)a]S_1
                         +m(m-R)aw/(2p)+E_2
      <=| (R-1)/2-(m-1)a | E_1
                         +m(m-R)aw/(2p)+E_2.          (F6)

Equivalently, after dividing by the positive m(m-1)a T_m/2,

    a <= (R-1)/(m-1)
       +2| (R-1)/2-(m-1)a | E_1/[m(m-1)aT_m]
       +(m-R)w/[(m-1)pT_m]
       +2E_2/[m(m-1)aT_m].                            (F7)

This holds for every a>0, although it is useful only when the errors
are small. The a=0 case requires no division or terminal argument.

## 2. Why the original arithmetic estimates extend

On the support of F, put L=(2cx+b)h and D=ch^2 for a quadratic
generator. Their centered lifts have magnitude at most H. Relative to
slot i, the change at slot j is

    q(x+jh)-q(x+ih)=(j-i)L+(j^2-i^2)D.

For 0<=i,j<m the sum of the coefficient magnitudes is at most
(m-1)+(m-1)^2=m(m-1). The linear changes are at most (m-1)H.
Consequently, an interior slot and F>0 force all m vertices into
the host, with no additional restriction on wrapped interval positions.
The same boundary-preimage argument as (M7) proves (F2).

The exact degree decomposition

    D_i(v)=E_h F(v-ih,h)=mu+R_i(v)+E_i(v),
    R_i>=0, E_v R_i<=1/p, |E_i|<=eps

holds for every slot i: its Fourier coefficients are still
N-2iC and 2vC+beta. Its proof never required i<=3. Applying it at an
interior vertex gives the lower bound in (F3); dropping all host
indicators except P_0 gives its upper bound. The diagonal h=0 gives
T_m>=w/p. Comparing the host incidence degree to D_i exactly as in
(M15), now using b_m, bounds its distance from mu in weighted L1
by D_m. Since E_p u=0 and |u|<=P, summing this comparison proves
the first inequality of (F5).

For a pair i<j<m, put D_slot=j-i. This is nonzero in F_p. The
bijective substitution v=x+ih, z=x+jh gives exactly the phase

    [(N-2jC)v^2+(N-2iC)z^2
       +2((i+j)C-N)vz]/D_slot^2 + beta(z-v)/D_slot.

On N=(i+j)C this is q(z)-q(v), giving a nonnegative square.
All other modes have a nonzero mixed coefficient and operator norm
p^(-1/2). The original full-group estimate therefore remains

    J_ij(u)>=-(1-nu_ij)U eps.

Restoring the other m-2 host indicators changes the pair form by at
most beta_m. Indeed a pair contribution lost through any of these
indicators must have its occupied anchor slot in
Omega\Omega_-^(m); the same single-anchor estimate as (P8) applies.
There is no extra multiplicative factor m-2. Summing over the
binom(m,2) pairs proves the second inequality of (F5).

Every average includes h=0. The exact diagonals are

    (T_m)_diag=w/p,
    (M_1)_diag=maw/p,
    (M_2)_diag=binom(m,2)aw/p,
    (S_1)_diag=0,
    (C_2)_diag=binom(m,2)U/p.                         (F8)

## 3. Boolean occupancy and the finite inequality

On a host progression put K=sum_i B_i. When h!=0, AP exclusion
implies K<=R, because a four-term progression in the occupied index
set would map to a nonzero four-term progression in A. Hence

    binom(K,2)<=(R-1)K/2.

On the diagonal an occupied point has K=m. Keeping this contribution
exactly yields

    M_2<=(R-1)M_1/2+m(m-R)aw/(2p).                   (F9)

The exact nonnegative slack is

    (R-1)M_1/2+m(m-R)aw/(2p)-M_2
      =(1/2)E_(x,h) 1_(h!=0) F product_i P_i K(R-K). (F10)

Combine (F9) with C_2>=-E_2 and substitute M_1=maT_m+S_1.
The coefficient of T_m is

    (ma/2)[(R-1)-(m-1)a].

Rearrangement proves (F6), with no sign assumption on S_1. Division
gives (F7). At m=4,R=3, S_1=R_1^F/a^3 and C_2=R_2^F/a^2,
so this recovers the preceding 2/3 argument with exactly its diagonal.

## 4. An elementary twelve-point certificate

Every four-term-AP-free subset of {0,...,11} has at most eight elements.
Here is a direct proof, independent of the finite enumeration.

Suppose there were at most three holes. The disjoint four-term
progressions {0,1,2,3}, {4,5,6,7}, and {8,9,10,11} require exactly
three holes, one in each block. Call them a_0,b_0,c_0. Avoiding four
consecutive occupied positions requires

    b_0-a_0<=4,              c_0-b_0<=4.              (F11)

Both parity classes must contain a hole. With three holes, one parity
class has exactly one. In the six-term even sequence
0,2,4,6,8,10, a unique hole hitting all three consecutive four-term
subprogressions must be 4 or 6. For the odd sequence it must be 5 or 7.
Thus b_0 is the unique hole of its parity, and a_0,c_0 have opposite
parity.

If b_0=4, then c_0>=9 and the second inequality in (F11) fails.
If b_0=7, then a_0<=2 and the first fails. If b_0=5, parity and
(F11) force (a_0,c_0)=(2,8). If b_0=6 they force (3,9).
In either remaining case a_0 and c_0 have the same residue modulo
3, so the three holes cannot hit all three disjoint progressions

    {0,3,6,9},    {1,4,7,10},    {2,5,8,11}.

This contradiction proves the upper bound eight.

It is attained by {0,1,2,4,5,7,8,9}. Its holes are {3,6,10,11}.
They hit every difference-one progression, every difference-two
progression (the six starts 0 through 5), and every difference-three
progression (the three starts 0 through 2). These exhaust the possible
positive differences. Thus the exact finite maximum is R_4(12)=8.

In particular (F6) becomes

    6a(11a-7)T_12
       <=(7/2-11a)S_1+24aw/p+E_2.                   (F12)

For a>0 the resulting finite ceiling is

    a<=7/11+|7/2-11a|E_1/(66aT_12)
                +4w/(11pT_12)+E_2/(66aT_12),        (F13)

where E_1=12D_12 and E_2 is (F4) with binom(12,2)=66.
No assertion of sharpness of the 7/11 ceiling for arithmetic sets,
or even for all abstract twelve-variable laws, is made.

## 5. Compatibility with the original terminal regime

Use exactly the previous H and baseline lower bound:

    H=floor(tau wp/(48r)),
    mu_0=(tau w/(48r))^(d+2s),       mu>=mu_0.

Assume (M13), namely tau->0, tau wp/r->infinity,
s(2+log p)/(w sqrt(p))->0, sqrt(p)mu_0->infinity,
and wp mu_0->infinity. For any fixed m, (F2) gives

    b_m/w<=m(m-1)tau/24+2sK_p/(w sqrt(p))->0.         (F14)

For m=12 its first term is (11/2)tau. No change in H or the
persistent baseline is needed. Equations (F3) now imply

    T_m=(1+o(1))w mu.

After division by T_m, the errors E_1 and E_2 are bounded by constants
depending only on m times sums of

    b_m/w, eps/mu, eps b_m/(w mu), 1/(wp mu).

All tend to zero under (M13), using U<=w. Also w/(pT_m)->0,
since p mu>=wp mu>=wp mu_0->infinity. If a exceeds the positive
ceiling (R-1)/(m-1), its reciprocal in (F7) is bounded. Otherwise
the desired ceiling already holds. For the stated m=12,R=8 this proves

    a<=7/11+o(1),                                    (F15)

uniformly over all phase coefficients, dependence among constraints,
and interval positions satisfying (M13). In particular it applies to
the same reachable windows as the previous 2/3 theorem. It improves
that terminal constant by 1/33. It does not alter the missing
phase-correlation threshold, density increment, or inequality (P12).

## 6. Verification and limitations

`verify_finite_pattern_terminal_20261018.py` writes
`FINITE_PATTERN_TERMINAL_VERIFICATION_20261018.json`. Its 51,971 checks
include exhaustive corroboration of R_4(12)=8 over all 4,096 masks,
the 64 possible three-hole block patterns, exact rational expansions,
occupancy slack and diagonals, and fifteen actual cyclic AP-free
subsets in three finite host configurations.

All three hosts have nonempty eroded interiors: a four-slot full
linear host at p=257 (233 interior vertices), a twelve-slot full
linear host at p=1009 (745), and a twelve-slot proper mixed host at
p=1009 (900 host vertices and 486 interior vertices). The mixed
case checks anchor erosion, proper-host pair corrections, and the
explicit finite error formulas. The older October 17 verifier's
listed configurations all had empty eroded interiors; this extension
adds coverage without changing that historical artifact.

Physical arithmetic and the finite combinatorial certificate use
exact integers and rational numbers. Only square-root error-envelope
comparisons use floating arithmetic. With H=1 the generic finite
error envelopes can be vacuous even though the interior is nonempty.
Consequently the asymptotic conclusion rests on the displayed proof,
not finite numerical extrapolation. No phase-selection claim or
asymptotic arithmetic counterexample is obtained.
