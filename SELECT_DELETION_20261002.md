# SELECT attack: deletion hypergraph degree-discrepancy certificate

2 October 2026. Offline. **PROVED auxiliary dichotomy; SELECT unresolved.**
This is a new derivation in this run, not a repetition of the earlier
constant-fraction hole bound. No claim of literature novelty is made.

## 1. Exact hitting-set certificate, including relative windows

Let p>3 prime, P=1_C the indicator of an arbitrary host C, and let A be
4AP-free. Put D=1_(C\A), b=E_p P, theta=E_p D/b, r=D-theta P. Then
E_p r=0. Define the ordered completion degree

    h_C(v)=sum_(i=0)^3 E_t product_(j!=i) P(v+(j-i)t).

Every nonzero-difference progression in C must hit D. Counting its holes
over the four positions yields

    E_p D h_C >= Lambda4(P)-b/p,
    E_p P h_C =4Lambda4(P),
    E_p r h_C >=(1-4theta)Lambda4(P)-b/p.                 (1)

The second identity is exact by changing variables from v to x=v-it
separately in each slot. The b/p term removes the diagonal. Added points
of A outside C do not affect this argument.

For a relative window Omega, take C=Omega intersect {q(x) in S}. If
mu=|Omega|/p, normalize (1) by mu to get

    E_Omega r h_C >=(1-4theta)Lambda4(1_C)/mu-b/(mu p).    (2)

Thus deletion fraction below 1/4 forces positive degree discrepancy.
This certificate is unconditional and respects the relative window; it
does not yet turn degree discrepancy into a SELECT linear coefficient.

The ordered AP hypergraph also has codegree at most 12: for two distinct
vertices v,w and two distinct positions i,j, the unique progression is
t=(w-v)/(j-i), x=v-it. There are 12 choices (i,j). All denominators are
invertible since p>3. This is an upper codegree bound, not an independence
upper bound or a container theorem.

## 2. Full-group quadratic hosts have an explicit degree law

Let P(x)=1_S(q(x)), q(x)=lambda(x-r0)^2+c, lambda!=0. Write
beta=|S|/p, c_t=E_y 1_S(y)e_p(-ty), K=sum_t |c_t|. Define

    Phi_E(y)=sum_t c_t |c_(3t)|^2 e_p(ty),
    Phi_M(y)=sum_t c_(3t) |c_t|^2 e_p(3ty),
    H(y)=2Phi_E(y)+2Phi_M(y).

For every v!=r0,

    |h_C(v)-H(q(v))|<=4K^3/sqrt(p).                      (3)

Proof: the vertex-completion expansion in slot i has constant-in-t
frequencies satisfying sum_(j!=i)(j-i)k_j=0 and
sum_(j!=i)(j-i)^2 k_j=0. Their kernels are

    i=0: (-3,3,-1)t;  i=1: (1,3,-1)t;
    i=2: (-1,3,1)t;   i=3: (1,-3,3)t.

Substitution gives Phi_E for the two endpoints and Phi_M for the two
middle positions. The assumption v!=r0 ensures a nonzero linear phase
is not incorrectly treated as constant. All other one-variable phases
are nonconstant linear (average zero) or nonzero quadratic (magnitude
p^(-1/2)). Their total Fourier l1 weight is at most K^3 per position.

Both Phi functions are nonnegative and at most beta^2. To see this, let
C_S(z)=E_y 1_S(y)1_S(y+z), which is nonnegative, has mean beta^2 and
Fourier coefficients |c_t|^2. Then

    Phi_E=1_S * [z -> C_S(z/3)],
    Phi_M=1_S * [z -> C_S(3z)],

where convolution is normalized. Hence 0<=Phi_E,Phi_M<=beta^2.
Also

    ||Phihat_E||_1<=beta sum_t |c_(3t)|^2=beta^2,
    ||Phihat_M||_1<=beta sum_t |c_t|^2=beta^2,
    ||Hhat||_1<=4beta^2.                                 (4)

At the exceptional critical vertex r0, both h_C and H(q) lie in [0,4],
so their difference is at most 4. Because |r|<=1, equations (3)-(4)
give

    |E_p r[h_C-H(q)]|<=4K^3/sqrt(p)+4/p.                 (5)

## 3. Quadratic-bias-or-quarter-deletion theorem

Combining (1), (4), (5), and E_p r=0 yields the exact dichotomy

    max_(t!=0) |E_p r(x)e_p(tq(x))|
      >= [(1-4theta)Lambda4(P)-4K^3/sqrt(p)-5/p]_+
                                                      /(4beta^2). (6)

Here [z]_+=max(z,0). The sign of the character can be reversed because
the maximum runs over all nonzero t. This theorem concerns genuine
quadratic correlations of the *centered holes*, rather than just how
many holes must be present.

For an interval S with beta~epsilon/log p, the quadratic-resonance theorem
gives

    Lambda4(P)>=Z_S-K^4/sqrt(p),
    Z_S>=4beta^3/(3pi^4),
    K<=2+log p.

Thus, if theta<=(1-sigma)/4 for fixed sigma>0, eventually

    max_(t!=0)|E_p [D-theta P]e_p(tq)|
       >=sigma beta/(6pi^4).                            (7)

Indeed the errors in (6), including the Gauss error multiplied by sigma,
are eventually at most sigma*(2beta^3/(3pi^4)).

Conversely, if all these centered-hole quadratic coefficients are o(beta),
then theta>=1/4-o(1). This is an asymptotically sharper deletion conclusion
under a specified degree-discrepancy hypothesis; it is not a universal
quarter-deletion theorem.

## 4. Why this does not prove SELECT

SELECT needs a *linear* coefficient at least
a^(5/4)sqrt(log(2/a)). Equations (6)-(7) force a quadratic coefficient.
The uniform quadratic invisibility theorem in
STRUCTURAL_GEOMETRY_20261002.md shows that such a quadratic object can
remain invisible to all permitted linear factors, even on H-windows.
No conversion of (7) into a SELECT coefficient has been proved.

Moreover theta>=1/4 is an unaddressed branch of the dichotomy. The desired
remaining AP-free subset might keep a fixed fraction less than 3/4 of a
quadratic host; neither the old hole count nor (6) excludes it. Replacing
the degree certificate by a generic spectral-expansion claim would assume
the missing theorem.

The codegree bound 12 does not solve this: low pair codegrees can coexist
with large independent sets in general hypergraphs. Any container or
expansion input needs its own quantitative proof for this arithmetic host.

## 5. Relative-window limitations and candidate qualifications

The exact relative certificate (2) and codegree bound apply without error
to C=Omega intersect {q in S}. Uniform relative host AP-richness is proved
in STRUCTURAL_GEOMETRY section 4A. However the full-group degree law (3)
does not transfer by simply inserting W: fixing a vertex gives products
of W at the other three positions, and their Fourier modes may modify the
linear completion resonance. No relative analogue of H(q) alone is used.

At H's endpoint geometry the available host count lower bound is only
of order beta^3 mu^2/3^d. Dividing by the full-group completion bound
would force relative hole fraction only of order mu/3^d, which vanishes.
A uniformly stronger relative discrepancy-to-linear-spectrum theorem is
still needed.

No qualifying AP-free counterexample was found. Full-product few-shell
Freiman constructions remain too sparse; padding the symmetric base-16
window violates H's size requirement; CRT transfer and block replication
need genuine new AP-free dense seeds. Pure quadratic interval hosts have
the required density and linear invisibility but have nonzero 4APs on
every H-window. This check prevents treating them as SELECT refutations.

## 6. Exact next analytic issue

For a host-based attack, the smallest missing conversion exposed here is:
use the arithmetic hitting constraints, beyond the first-degree dual
certificate (1), to force a linear residual coefficient from either the
quadratic-biased-hole branch of (6) or the theta>=1/4 branch, with all
relative-window and intermediate-factor errors. No such conversion has
been established, and these two branches do not independently reduce the
general SELECT theorem to a new proved single inequality.

Checks: verify_select_deletion_20261002.py tests the exact hitting identity,
completion resonance degree law, nonnegative Phi laws and l1 masses,
the quadratic-correlation bound, and codegrees. These finite checks are
supporting evidence, not a proof of SELECT or the r4 target.
