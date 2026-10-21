# Sixth-order correlation and Fourier structure — 12 October 2026

**(D) NEW RIGOROUS PARTIAL THEOREM.** Offline, no literature novelty claimed.
The unconditional target r_4(N)=o(N/log N) and SELECT remain unresolved.

New results: exact completion-overlap geometry; a sharper localized sixth-
moment constraint; an exact Fourier transform with every diagonal removed;
a quadratic weighted obstruction to using the correlation magnitude alone;
degree-nine/twelve higher-moment certificates; and an exact global extension
at p=29, k=6. The sufficient residual spectral concentration estimate is
identified, but not proved. No asymptotic AP-free counterexample is claimed.

The available skill catalog was checked against this mathematical task.
No available skill supplies a relevant proof workflow; unrelated product,
design, and coding skills were not invoked. The method is independent
algebraic derivation, rational certificates, and focused verification.

## 1. Audit and a necessary distinction

Read the degree-six report, its results and verification JSON, the p=23
certificate, the current status, ledger, dependencies, SELECT attack and
positive-moment theorem. Definitions below retain their normalization.
The canonical extension obstruction and harmonic correction freedom remain
valid. No extension at target density has been constructed or excluded.

For a moment extension L, all first three distinct-coordinate moments are
rho_j=(k)_j/(n)_j. This is an ASSUMPTION of that extension problem. It gives
L(H_v)=m_v rho_3. An arbitrary actual AP-free set does not have these uniform
third moments. For such a set, one must retain the actual completion count.
The a^7 enhancement from the checkpoint cannot simply be asserted for every
actual set by substituting rho_3 for its triple count.

All arguments involving cubic PSD additionally assume the appropriate
Boolean and AP equality multipliers through the degrees used. We explicitly
identify the stronger localizers needed for the odd higher moment below.

## 2. Exact overlap geometry, including relative windows

Let p>7 be prime, v in Omega, and

 D_v={d != 0: v+d,v+2d,v+3d in Omega}, m_v=|D_v|,
 T_d={v+d,v+2d,v+3d}, H_v=sum_{d in D_v} X_{T_d}.

Put R={1,2,3,1/2,3/2,1/3,2/3}, interpreted in F_p. Its seven members
are distinct for p>7. Equality of a coordinate of T_d and T_e is precisely
id=je with i,j in {1,2,3}. Thus

 |T_d intersection T_e| = 3 if e=d;
                         1 if e/d in R minus {1};
                         0 otherwise.                         (1)

In particular there are NO pairs sharing exactly two vertices. Each of
the six nonidentity ratios occurs only once among the nine ratios i/j.
The three remaining ratios i/i all equal one. This proves (1) and also
rules out duplicated triples. For arbitrary D_v define

 q_r(v)=#{d in D_v: rd in D_v}, Q_v=sum_{r in R minus {1}}q_r(v).

The exact ordered-pair counts for intersections 0,1,2,3 are

 m_v^2-m_v-Q_v, Q_v, 0, m_v.                             (2)

For the full group m=p-1, these are m(m-7), 6m, 0, m.
The relative version requires no translation invariance of Omega.

Let M(S)=L(X_S). The COMPLETE expansion is

 L(H_v^2)=m_v rho_3
   + sum_{r in R minus {1}} sum_{d in D_v,rd in D_v} M(T_d union T_rd)
   + sum_{d,e in D_v,e/d notin R} M(T_d union T_e).        (3)

The middle terms are fifth moments; the last terms are sixth moments.
The corresponding fixed-cardinality baseline is

 m_v rho_3 + Q_v rho_5 + (m_v^2-m_v-Q_v)rho_6.            (4)

Consequently, writing Delta_5(v) for the middle sum minus Q_v rho_5
and Delta_6(v) for the last sum minus (m_v^2-m_v-Q_v)rho_6, positivity gives

 Delta_5(v)+Delta_6(v) >= m_v^2 rho_3^2/(1-a)
                  -m_v rho_3-Q_v rho_5
                  -(m_v^2-m_v-Q_v)rho_6.                (5)

This is the exact deficit, retaining the vertex, ratios, and union sets.
Fifth moments cannot be silently replaced by rho_5.

### AP exclusion eliminates two overlap ratios

For r=2 the union contains v+d,v+2d,v+3d,v+4d, an AP.
For r=1/2 the same fact follows after rescaling. Hence these two fifth-
moment classes are zero by degree-five AP multipliers. The four remaining
ratios are 3,1/3,3/2,2/3. Some small primes can make additional unions APs;
we do not need to exclude or ignore those further zeros.

Cubic PSD bounds each remaining union moment in absolute value by rho_3,
since it is the inner product of two triple monomials of squared norm rho_3.
Put Q'_v=q_3+q_(1/3)+q_(3/2)+q_(2/3), so Q'_v<=4m_v. Equations (3) and
the completion-square bound therefore give the sharpened localized result

 sum_{disjoint d,e} M(T_d union T_e)
       >= m_v^2 rho_3^2/(1-a)-(m_v+Q'_v)rho_3
       >= m_v^2 rho_3^2/(1-a)-5m_v rho_3.                (6)

For k>=6, rho_3>=a^3/2. If m_v a^4>=20, then
5rho_3/m_v<=a rho_3^2/2. Divide (6) by the number of disjoint pairs,
which is at most m_v^2; its numerator is positive under these assumptions.
Use 1/(1-a)>=1+a and rho_6<=rho_3^2 to obtain

 average_{disjoint d,e} M(T_d union T_e)
             >=rho_3^2(1+a/2)>=rho_6+a^7/8.             (7)

This improves 36 to 20 and uses AP multipliers as well as cubic PSD.
It holds separately at every eligible vertex satisfying the stated star-
size condition. At least one disjoint pair at each such vertex reaches
the average, but neither a common ratio nor a common additive frequency
across different vertices follows. Equation (5), not only (7), remains
available when fifth moments can be bounded more accurately.

## 3. The exact additive Fourier representation

This section concerns an actual Boolean function B on the FULL Z_p.
Write b(t)=p^-1 sum_x B(x)e_p(-tx), a=b(0), and define

 h(v)=E_d B(v+d)B(v+2d)B(v+3d),
 H(v)=p h(v)-B(v), q(v)=H(v)/p.

Here h includes d=0, whereas H and q omit it. Fourier inversion gives

 K(t):=hat h(t)=sum_r b(2t+r)b(-t-2r)b(r).               (8)

Indeed the three input frequencies alpha,beta,gamma obey
alpha+2beta+3gamma=0 and alpha+beta+gamma=t;
solving gives (alpha,beta,gamma)=(2t+r,-t-2r,r).
Thus

 E_v h(v)^2=sum_t |K(t)|^2.                             (9)

Equivalently, expanding all six factors imposes the THREE linear equations

 alpha_1+2alpha_2+3alpha_3=0,
 alpha_4+2alpha_5+3alpha_6=0,
 sum_{i=1}^6 alpha_i=0.                                (10)

There are no literal quadratic equations on frequencies in (10).
Quadratic phases nevertheless resonate with this system (section 6).
Within |K(t)|^2, terms indexed by equal r are positive squared products;
the cross terms can have either sign in their real parts. Positivity of
the total does not license discarding negative cross terms in a lower bound.

For completely explicit removal of repeated variables, let m=p-1 and

 F_3=E_v E_{d!=0} B(v+d)B(v+2d)B(v+3d),
 F_(5,r)=E_v E_{d!=0} product_{j in {1,2,3,r,2r,3r}}B(v+jd),
 A_6= [p m(m-7)]^-1 sum_v sum_{d,e!=0,e/d notin R}
                     product_{j=1}^3 B(v+jd)B(v+je).

The product for F_(5,r) is over the SET of five distinct residues.
With Lambda_4(B)=E_{v,d} B(v)B(v+d)B(v+2d)B(v+3d), the exact formulas are

 E H^2 = m F_3 + m sum_{r in R minus {1}} F_(5,r) + m(m-7) A_6,
 E H^2 = p^2 sum_t |K(t)|^2 - 2p Lambda_4(B)+a,
 F_3=(p K(0)-a)/m.                                    (11)

These give the requested normalized Fourier representation of A_6 by
substitution and division by m(m-7). They remove d=0, e=0, d=e and every
other repeated-variable ratio exactly. In the AP-free case Lambda_4=a/p,
so the second line is p^2 sum|K|^2-a, and F_(5,2)=F_(5,1/2)=0.

For a pseudo-moment functional the same polynomial identities hold after
applying L. In particular the sixth-order statistic involves L|K(t)|^2,
NOT |L K(t)|^2. Uniform third moments make L H(v)=m rho_3 constant; all
nonzero Fourier coefficients of this expected H vanish even when its
second moment is large. This is one concrete reason not to treat moment
correlation energy as a coefficient of a single realized set.

There is a second exact distinction. Uniform first and second moments
give, on the full group and for every nonzero t,

 L|b(t)|^2=(rho_1-rho_2)/p=a(1-a)/(p-1).

Thus any extension preserving those moments has diffuse EXPECTED linear
Fourier energy, regardless of the new sixth moments. This identity does
not guarantee simultaneous pointwise caps or the existence of an extension.
The two finite global laws below realize it, but not at asymptotic scale.

In a proper window, zero-extend B. This counts the completion triples for
v in Omega correctly, but averaging v outside Omega introduces anchors
not in the window. Restricting back multiplies by 1_Omega and introduces
its Fourier coefficients. Full-group orthogonality and baseline a^3 do
not become relative identities. The exact relative completion pairing
from the previous report remains valid with its zero-extension convention.

## 4. Actual sets: the analytic input and its density loss

For an actual AP-free Boolean set, q>=0 and Bq=0. Let T=E q and V=Var q.
Cauchy on the complement of A gives

 E q^2 >= T^2/(1-a), V>=a T^2/(1-a).                    (12)

This is a deterministic argument, independent of SOS. The crucial missing
input is T, not a freely imposed uniform third moment. On the full group,

 T=a^3+sum_{r!=0} b(r)^2 b(-2r)-a/p.

If rho=max_{r!=0}|b(r)|, Parseval gives

 |T-(a^3-a/p)|<=rho a(1-a).                             (13)

Thus rho<=a^2/4 and pa^2>=4 imply T>=a^3/2, so V>=a^7/4.
If rho>a^2/4, one only obtains a squared coefficient >a^4/16 from this
branch. If rho is smaller, (12) supplies completion variance, not a large
coefficient of B. This dichotomy must not be mislabeled an unconditional
rho>=c a^2 theorem for AP-free four-progressions.

The other branch cannot be closed using an upper bound V=o(a^7) derived
from rho alone for general bounded functions: section 6 disproves such
a general inference. It remains possible that AP exclusion supplies an
additional estimate, but it must be proved.

For residuals u=B-g on the full group, put v=Var g. Because Bq=0,

 |<u,q>| >= aT-sqrt(v V).                              (14)

At the checkpoint energy threshold v<=zeta a^(9/4), T on scale a^3
would require V<=C a^(23/4) to make the error <=aT/2 by this estimate.
The elementary bound 0<=q<=a gives V<=aT, only on scale a^4 when T~a^3;
it does not imply the needed upper bound. The lower bound V>=c a^7 is
compatible with either situation and cannot replace that upper bound.

## 5. Collective energy: an exact sufficient concentration estimate

Here is a precise full-group alternative to one large coefficient.
Let Gamma be a finite set of nonzero characters, Q_Gamma=sum_Gamma |hat q|^2,
and Q_tail=sum_{nonzero outside Gamma}|hat q|^2. Suppose T>0 and

 sqrt(v V)<=aT/4, Q_tail<=aT^2/16.                      (15)

Since ||u||_2^2<=a, the tail pairing has magnitude <=aT/4.
Equation (14) and Cauchy on Gamma then imply

 sum_Gamma |hat u|^2 >= a^2 T^2/(4 Q_Gamma)
                         >= a^2 T^2/(4 V).             (16)

The hypotheses make Q_Gamma positive. This proof also shows why total
completion energy alone is inadequate: it gives no small Gamma with the
required tail, and V appears in a denominator as well as in (15).
On the full group, quarter refinement converts (16) to factor energy with
constant kappa^2=8/pi^2. On a relative window the characters are not
orthogonal; the correct conversion is the previously proved regularized
Gram quantity kappa^2 c*[kappa^2 G+(1-kappa^2)I]^-1 c. A bare sum of
relative squared coefficients is insufficient without controlling G.

There is no proved low character budget for (15). Permitting Gamma to be
all p-1 characters removes the tail but destroys the admissible rank.
This result identifies an exact missing spectral concentration condition;
it does not prove a sufficient replacement for SELECT under its hypotheses.

## 6. A rigorous obstruction to correlation-size-only conversion

The following example is weighted and is NOT AP-free. Its purpose is to
refute a general implication using only sixth-order excess, boundedness,
and small linear Fourier coefficients. It cannot refute SELECT.

Fix beta=1/4, F(theta)=1+2beta cos(2pi theta)+2beta cos(6pi theta).
For primes p tending to infinity put

 M_p=E_x F(x^2/p), f_p(x)=a F(x^2/p)/M_p,
 a=epsilon/log p (or any positive a tending to zero).

F>=0 and F<=2. The elementary quadratic Gauss bound gives
M_p=1+O(p^-1/2), so eventually 0<=f_p<=1 and E f_p=a.
For every nonzero additive frequency,

 |hat f_p(t)| <= a/(M_p sqrt(p)).                       (17)

Proof: the four nonconstant Fourier modes of F are +/-1,+/-3, each with
coefficient beta, and each normalized quadratic Gauss sum has modulus
p^-1/2. The constant mode contributes zero at nonzero t. The Gauss modulus
itself follows by squaring the sum and changing variables to x-y,x+y.

Let h_f(v)=E_d product_{j=1}^3 f_p(v+jd). A term indexed by
(ell_1,ell_2,ell_3) in {0,+/-1,+/-3}^3 has phase

 C v^2+2D vd+A d^2,
 C=ell_1+ell_2+ell_3,
 D=ell_1+2ell_2+3ell_3,
 A=ell_1+4ell_2+9ell_3.

For sufficiently large p the solutions A=0 in this mode set are exactly
(0,0,0), (3,-3,1), (-3,3,-1); all three also have D=0. This follows
by checking ell_3=0,+/-1,+/-3 in A=0. Every other term has A!=0,
so its d-average has modulus p^-1/2. Thus uniformly for every v,

 h_f(v)=(a/M_p)^3[1+2beta^3 cos(2pi v^2/p)]+O(a^3/sqrt(p)).

Summing over v and using Gauss sums again gives

 E_v h_f(v)^2=a^6[1+2beta^6+O(p^-1/2)].                 (18)

All error constants are absolute, since the mode set is fixed. Removing
zero differences and the seven overlap ratios changes the normalized
six-DISTINCT-position product average by O(a^6/p): every product has six
factors bounded by O(a), even when positions coincide before removal.
The denominator also changes by a relative O(1/p). Hence this disjoint
sixth-order average is at least a^6(1+beta^6) for sufficiently large p.
For eventually a<=8beta^6, its excess over a^6 is >=a^7/8.
Replacing a^6 by the fixed-cardinality baseline rho_6 for k=ap integer
only lowers that baseline. One may choose a=floor(epsilon p/log p)/p.

Nevertheless (17) is far below SELECT:

 max_nonzero |hat f_p|^2 / [a^(5/2)log(2/a)]
                <=O(1/[p sqrt(a)log(2/a)]) ->0.         (19)

For every s-character set Gamma, the nonzero Fourier energy is at most
s a^2/(M_p^2 p). Thus even collective energy stays negligible for the
polylogarithmic character budgets in the target substitution.

The example has genuine arithmetic quadratic resonance, not relabeled
unstructured coordinates. Independent Bernoulli occupations with these
probabilities realize its distinct-position moments, but that law has
neither fixed cardinality nor AP exclusion nor uniform third moments.
Those omissions are explicit. It is not a counterexample to the full
sixth-order extension problem. It proves that the magnitude of the sixth-
order signal alone cannot provide the desired linear inverse implication.

## 7. Incidence spectrum of the actual completion hypergraph

Fix v and identify nonzero offsets with F_p*. In the full group the
vertex/triple incidence matrix is I_(x,d)=1_{x/d in {1,2,3}}.
Every vertex and triple has degree three. Every pair of distinct vertices
lies in at most one triple, by (1); the hypergraph is linear. Its Gram is

 I*I =3 Id + sum_{r in R minus {1}} P_r,                 (20)

where (P_r z)(d)=z(rd), up to the immaterial inverse convention.
Multiplicative characters chi diagonalize it, with eigenvalues

 |1+chi(2)+chi(3)|^2.                                  (21)

This follows either from direct substitution or expansion of the square.
In relative windows the incidence matrix is a submatrix and degrees only
decrease. The operator norm remains at most three (Gram norm at most nine).
Its natural eigenvectors are multiplicative characters in the difference
variable; they are not additive characters of the anchor v. Moreover H_v
uses a PRODUCT of three occupations, not a linear incidence sum. No
additive residual energy bound follows from (21) alone. Connected components
in the difference overlap graph are cosets of the subgroup generated by
2 and 3, also not automatically additive low-complexity factors.

## 8. Higher moments, with their required degrees

For an actual AP-free set in any window, H_v>=0 and is supported on its
complement. Let T=E_Omega H. Conditional Jensen gives exactly

 E H^r >= T^r/(1-a)^(r-1), r=2,3,4.                    (22)

The moments themselves, for any moment functional, have the exact expansion

 L(H_v^r)=sum_{(d_1,...,d_r) in D_v^r}
             M(T_(d_1) union ... union T_(d_r)).         (23)

Repeated positions are included once in the union. This requires moments
through degree 3r; six moments do not define the r=3 or r=4 expressions.

For explicit certificates let y=1-X_v and use y^2=y, Hy=H. For t>=0,

 H^3-3t^2 H+2t^3 y=(H-ty)^2(H+2ty),                   (24)
 H^4-4t^3 H+3t^4 y=(H^2-t^2 y)^2+2t^2(H-ty)^2.        (25)

Equation (24) is certified by the degree-nine literal preordering:
H is a sum of positive triple-literal products, so its square multipliers
have degree 3+6=9; the y term needs degree seven. Degree-six PSD alone
cannot certify it. Equation (25) uses PSD squares through degree twelve,
with the corresponding Boolean/AP reductions. Choosing t=L(H)/(1-a)
proves the corresponding L bounds whenever these assumptions hold.
For the uniform-third-moment extension, L(H)=m rho_3. For actual spatial
averaging the mean is the actual T, as in (22).

If the normalized mean is on scale a^3, the forced excess above its r-th
power is on scale (r-1)a^(3r+1) for fixed r: a^7, a^10, a^13.
Higher fixed moments do not by themselves amplify the density exponent.
Taking r on scale 1/a requires growing degree and controls a different,
much smaller baseline; no admissible Fourier budget follows.

## 9. Finite extension mechanism and its enlargement

The p=23,k=5 certificate has 20 four-set orbits, one AP row which is
identically zero on AP-free support, and 59 AP-free five-set orbits.
Its exact positive solution uses 19 independent columns, so the equality
matrix has rank 19. The affine equality solution space has dimension 40;
this is not a claim that the entire nonnegative feasible polytope has
that dimension. Positive support weights have exact margins recorded in
SIXTH_ORDER_VERIFICATION_20261012.json; unselected orbit weights are zero.

A NEW exact extension at p=29,k=6 was constructed by the same all-choice
root-trade formula. There are 235,794 admissible root trades, 33 four-set
orbits and 459 AP-free six-set orbits. Exact rational reconstruction gives
32 positive independent orbit weights, hence rank 32 and affine equality
solution dimension 427. The full weights and representatives are saved in
sixth_order_p29_k6_extension_20261012.json. Independent expansion verifies
normalization, AP exclusion, and every prescribed moment through degree four.
Unlike k=5, the sixth moments are now nonzero on supporting six-sets.

These are global laws, so they satisfy cubic PSD, all AP multipliers,
and all consistent local laws at every degree. The cap tau=120a/n is
larger than a^2 in both examples and hence holds pointwise for every set.
This cap is weak here. Neither example satisfies the large-star condition
m a^4>=20; neither tests the quantitative a^7 theorem's asymptotic range.
The examples demonstrate finite consistency, not feasibility as p grows.
The exact constraints genuinely restricting further extension are positivity
of a global or truncated law with the uniform lower moments, AP multipliers,
and the much smaller target-regime cap. No all-n construction or excluding
dual certificate has been obtained.

## 10. Quantitative ledger and failure of closure

Write ell=log(2/a), t=epsilon/log N. The October 2 ledger proves that a
squared residual coefficient >=c a^lambda ell^q, usable throughout greedy
refinement below its stopping energy, gives leading cumulative rank and
logarithmic size loss O(t^-(lambda-2)/ell(t)^q), with the stated stopping-
energy restrictions. Critical lambda=5/2 needs a positive log gain.
This is a conditional iteration theorem, not a source of coefficients.

| Route | Input/output | Character cost and iteration consequence |
|---|---|---|
| Exact sixth extension | excess >=a^7/8 on each sufficiently large star | No additive coefficient, factor gain, or finite useful rank bound proved |
| Actual completion branch | rho>a^2/4 gives squared coefficient >a^4/16 | Even if available at every residual, lambda=4 gives cumulative O(t^-2), far outside o(sqrt(log N)); availability itself is unproved |
| Complement branch | rho<=a^2/4, pa^2>=4 gives Var q>=a^7/4 | No conversion of cubic-field variance into input Fourier concentration |
| SELECT sought | squared coefficient c a^(5/2)ell | stopping energy zeta a^(9/4); O(a^-1/4/ell) characters per stopping factor, relative density gain of order a^1/4; cumulative O(t^-1/2/ell) |
| Collective lemma | (15) gives E_Gamma(u)>=a^2 T^2/(4V) | |Gamma| characters on full group; relative version needs Gram control; no bound on |Gamma| proved |
| Weighted quadratic diagnostic | excess >=a^7/8 but rho^2<=O(a^2/p) | Refutes unrestricted signal-size conversion; it fails AP exclusion and is not a SELECT counterexample |

For the hypothetical a^4 squared-coefficient branch, reaching energy
zeta a^(9/4) by single-character gains would cost O(a^-7/4) characters
per factor. Relative density gains of order a^1/4 take O(t^-1/4) steps
in the first dyadic density epoch; summing gives O(t^-2) rank and leading
logarithmic size loss. At t=epsilon/log N this is O(epsilon^-2(log N)^2),
whereas the admissible bounds require o(sqrt(log N)). The shortfall in
squared signal relative to SELECT is a^(3/2)/ell ->0.

More generally, a collective factor with gain eta(a)a^2 and added rank
s(a) has the established dyadic sums in SOLUTION_LEDGER.md. With constant
eta, s(a)=O(a^-gamma/ell^D) is sufficient for gamma<1/2, or gamma=1/2
and D>0. These are sufficient budgets, not a proved smallest necessary
budget. No minimal budget follows from the present data. Tail condition
(15) has not supplied even one of these bounds, particularly in proper
windows. At a=epsilon/log N the sixth-order signal is epsilon^7/(log N)^7;
there is no proved amplification to SELECT's squared scale
~epsilon^(5/2) log log N/(log N)^(5/2).

## 11. Adversarial checks and precise remaining problem

Independent derivations checked: intersection ratios and missing two-point
class; AP-forced overlap zeros; Fourier normalization and d=0 subtraction;
pseudoexpectation versus realized Fourier energy; weighted quadratic
resonance classification, including the anchor v=0; Boolean reductions and higher-moment degrees;
finite global-law positivity and fixed cardinality; and target-density
substitution. The verifier tests small primes, both rational global laws,
and numerical Fourier identities. Numerical tests do not establish the
symbolic asymptotic statements. Existing historical records are preserved.

No actual AP-free SELECT-refuting sequence was constructed. The weighted
example and the genuine finite AP-free distributions are separate
categories. There is no new arrow to the unconditional target.

The sharp next issue is whether AP exclusion, Booleanity and low relative
factor energy force a small spectral set for the completion pairing, or
exclude every degree-six correction under the target-regime caps. Total
sixth-order enhancement does not settle either question. In particular a
proof must defeat the explicit quadratic resonance while using the AP-zero
constraint that this diagnostic deliberately lacks.

## Corrected continuation prompt

Continue offline from SIXTH_ORDER_FOURIER_ATTACK_20261012.md and its JSON.
Do not reprove the overlap count or report the weighted quadratic example
as an AP-free counterexample. Keep the uniform-third-moment extension
problem separate from actual sets' completion means. Use the exact deficit
(5), the AP-forced zeros, and Fourier formula (11). Attack one of two precise
remaining routes: (i) prove a relative, Gram-controlled counterpart of
(15)-(16), with a character budget satisfying the October 2 dyadic ledger,
using Boolean AP exclusion to rule out quadratic resonance; or (ii) construct
all-n degree-six harmonic corrections with the actual target cap, or derive
an exact dual certificate against every correction. Audit the p=29,k=6
rational global law as a finite consistency test, not asymptotic evidence.
Track completion mean, variance upper bounds, spectral tails and density
powers separately, including a=epsilon/log N. A large completion variance
alone is not a coefficient theorem. Preserve records, verify new claims,
and return one justified status A-E with another exact remaining lemma if
closure is still absent.
