# Labeled derivative frequency graph and cocycle attack

2026-10-02. Offline continuation. No proof or refutation of H. All earlier
files preserved. This note records new identities and falsifications of
specific compression/cocycle shortcuts, not a counterexample to H.

Read CURRENT_STATUS, NEW_RESULTS, SOLUTION_LEDGER, PROOF_DEPENDENCIES,
AGENTS, and the prior quadratic/Boolean route note. H refers to the exact
narrow-coordinate-window hypothesis in NEW_RESULTS section 1. The chain
H=>target is not re-proved here.

## 1. Exact two-variable transform — PROVED

For any Boolean B on Z_p, let

    b(k)=E_x B(x)e_p(-kx), W(k)=|b(k)|^2, alpha=E B,
    C_d(x)=B(x)B(x+d),
    F(d,k)=E_x C_d(x)e_p(-kx), w(d,k)=|F(d,k)|^2.

The d-Fourier transform is the rank-one product tensor

    E_d F(d,k)e_p(-td)=b(k-t)b(t).                       (G1)

Proof: substitute y=x+d, so the phase is -(k-t)x-ty, and the two
averages factor. There is no AP-free assumption or exceptional difference.
Consequently

    F(d,k)=sum_t b(k-t)b(t)e_p(td),
    R(k):=E_d w(d,k)=sum_t W(k-t)W(t)=(W*W)(k).          (G2)

Here convolution is an unnormalized frequency sum. In particular

    sum_k R(k)=alpha^2,
    R(0)=sum_k W(k)^2,
    sum_k R(k)^2=sum_{k,t,u}W(t)W(k-t)W(u)W(k-u).        (G3)

These are the exact graph right degrees and their second moment, not merely
bounds on independent fibers. For rho=max_{k!=0}|b(k)|, k!=0 gives

    R(k)<=2alpha^2 W(k)+rho^2 alpha(1-alpha)
         <=(alpha+alpha^2)rho^2.                        (G4)

The two terms with t=0 or t=k give the first summand, and every remaining
W factor is <=rho^2. Thus tiny original Fourier maximum makes every
nonzero right degree small, even though AP exclusion forces negative
angular edge mass. A frequency set Gamma of cardinality m captures at most
m(alpha+alpha^2)rho^2 derivative mass. This is an upper bound, not a
reverse implication asserting original-spectrum concentration.

If rho<=alpha^2 and m=O(alpha^(-1/2)/log(2/alpha)), G4 gives

    sum_{k in Gamma,k!=0}R(k)
       =O(alpha^(9/2)/log(2/alpha))=o(alpha^4).           (G4a)

Consequently, within that low-original-spectrum branch, selecting the
allowed number of single derivative frequencies cannot retain the forced
order-alpha^4 angular mass. This does not exclude compression into a span
with many elements, or recovery through a more complicated factor.

For completeness, exact graph codegrees are

    M(k,l)=E_d w(d,k)w(d,l)
      =sum_{t,u,r} b(k-t)b(t) conjugate[b(k-t-r)b(t+r)]
                   *b(l-u)b(u) conjugate[b(l-u+r)b(u-r)]. (G4b)

This is obtained by imposing t-tprime+u-uprime=0, parameterized by
tprime=t+r,uprime=u-r. It is a PSD Gram matrix of nonnegative row vectors.
Its total sum and diagonal sum are

    sum_{k,l} M(k,l)=E_d theta_d^2=sum_k W(k)^2,
    sum_k M(k,k)=E_d sum_k |F(d,k)|^4=||B||U3^8.        (G4c)

Thus the simplest codegree/trace statistic is exactly the existing U3
quantity; it does not automatically improve its inverse dependencies.

### The signed two-dimensional coupling

Fourier inversion in k gives the exact identity

    E_d sum_k w(d,k)e_p(2kd)=Lambda_4(B).                 (G5)

Indeed the frequency sum pairs x with x+2d. Applying G1 instead gives

    Lambda_4(B)=sum_{k,t} b(k-t)b(t)
                          conjugate[b(-k-t)b(t+2k)].     (G6)

This displays the shared coupling between d-frequencies t and t+2k. It
is not an arbitrary bipartite graph. For AP-free B, its value is alpha/p.
The k=0 part is R(0)>=alpha^4, so the remaining signed sum is negative
by at least alpha^4-alpha/p when that is positive. Taking magnitudes or
retaining only graph degrees loses this phase interference.

## 2. Abstract angular graph obstruction — PROVED, not a Boolean example

The prior derivative theorem states for d!=0, theta_d=E C_d,

    sum_k w(d,k)=theta_d, w(d,0)=theta_d^2,
    sum_k w(d,k)cos(4pi kd/p)=0.

Those three fiber facts, including positivity and the exact angular zero,
do NOT force compression into few right vertices. Here is an explicit
positive graph satisfying all of them. Fix p>3 and 1/p<=theta<=1/4. Put

    D=2theta(1-p theta)/[p(p-3)],
    C=(theta-theta^2+D)/(p-1),
    w(d,0)=theta^2,
    w(d,k)=C+D cos(4pi kd/p), d,k!=0.                    (G7)

Use sum_{k!=0}cos=-1 and sum_{k!=0}cos^2=p/2-1. Substitution gives row
mass theta and angular sum zero exactly. Since D<=0,

    C+D=theta(1-3theta)/(p-3)>=0,

so all weights are nonnegative. For every k!=0 the nonzero-d right degree
is exactly the same:

    (1/p)sum_{d!=0}w(d,k)=[(p-1)C-D]/p.                (G8)

Moreover C-D=O(theta/p) uniformly for p>=5, theta<=1/4. Thus any m
nonzero right vertices capture O(m theta/p). Taking theta about alpha^2,
alpha=epsilon/log p and m=O(alpha^-1/2/log(2/alpha)) captures o(alpha^4),
although the angular theorem forces mass at least (1-1/p)theta^2 about
alpha^4. Even m=p^o(1) is insufficient. The same obstruction applies to
fixed bounded-coefficient additive spans of the allowed number of
characters, which have only exp(O(s))=p^o(1) elements.

This graph has NOT been realized as a Boolean derivative spectrum. In
particular G1/G6 and the shared pointwise Boolean constraints are additional
conditions not enforced by G7. Its role is precise: graph positivity,
left degrees, angular exclusion, and uniform averaging alone cannot prove
H. Random sampling or popularity based only on those statistics cannot
succeed; additional phase/cocycle structure must be used.

## 3. Exact Boolean triangle cocycle — PROVED

For all x,d,e,

    C_d(x)C_e(x+d)=B(x)B(x+d)B(x+d+e)
                  =B(x+d)C_{d+e}(x).                   (G9)

Unlike a unit-modulus multiplicative derivative, this is a support-weighted
cocycle. The middle B factor cannot be divided out on its zero set.
Let T_{d,e}(x)=B(x)B(x+d)B(x+d+e), tau=E T. Its average over all d,e is
exactly alpha^3, by the bijection (x,d,e) to the three vertices. Thus the
average support of a consistency comparison is alpha times smaller than
average pair support alpha^2.

### A quantitative local consistency implication

Choose any frequencies k_d,k_e,k_{d+e} and unit constants z_d,z_e,z_{d+e}.
Set psi_h(x)=z_h e_p(k_h x), and

    E_h=E_x C_h(x)|psi_h(x)-1|^2.

On triangle support, all three relevant pair indicators are 1. The product
Psi(x)=psi_d(x)psi_e(x+d)conjugate(psi_{d+e}(x)) therefore obeys

    E_x T(x)|Psi(x)-1|^2 <=3(E_d+E_e+E_{d+e}),           (G10)

by telescoping the three unit factors and Cauchy-Schwarz. Notice that the
E_e term is invariant under the needed translation of x.
Taking real parts gives

    Re E_x T(x)Psi(x)>=tau-(3/2)(E_d+E_e+E_{d+e}).       (G11)

If additionally all nonzero Fourier coefficients of T have magnitude
<=kappa tau, with kappa<1, and

    (3/2)(E_d+E_e+E_{d+e})<(1-kappa)tau,

then (G11) forces k_d+k_e-k_{d+e}=0. This is an exact conditional cocycle
criterion. Its extra hypothesis concerns triangle support, not the full
ambient group. No such pseudorandomness or small-error condition is supplied
by the angular mass theorem.

For phases chosen to align a coefficient, the pair error is

    E_h=2(theta_h-|F(h,k_h)|).

Thus this local theorem requires nearly saturated pair coefficients, with
deficits small relative to the triple support. Forced angular squared mass
does not guarantee saturation. At the logarithmic-density scale the
average triangle/pair ratio is alpha about 1/log p, so even a relative
pair error of order 1 is much too large for this particular criterion.

## 4. Saturation alone fails to force additive frequency selection — REFUTED

Take p=13 and A={0,1,3,9}. It is genuinely cyclically 4-AP-free, and every
nonzero difference occurs in exactly one ordered pair. Hence C_d is a
singleton for every d!=0. For every frequency k,

    |F(d,k)|=theta_d=1/13.

All frequencies are saturated. Choosing k_d=d^2 mod 13, and setting
z_d=e_p(-k_d x_d) where x_d is the unique pair-start, gives E_d=0 for all
nonzero d. Nevertheless on the occupied triangle x=0,d=1,e=2,

    k_1+k_2-k_3=1+4-9=9 mod 13 !=0.

The triangle support is the singleton {0}, so every triangle Fourier
coefficient is itself saturated. It violates precisely the extra
pseudorandomness premise in G11. There are 24 such occupied nonadditive
triangles for this selection. Therefore even actual AP-free Boolean sets
with perfectly saturated derivative coefficients do not force the selected
frequencies to be additive without a support/phase uniqueness input.
This finite example does not test H at its asymptotic density/geometry.

Repair attempted: use G11 with support pseudorandomness. Exact remaining
failure of that repair: no theorem forces triangle Fourier flatness or a
useful alternative increment, and angular mass supplies no small pair
errors. The repaired statement is proved conditionally, not assumed true.

## 5. Quadratic drift and expanded linear budget

For a genuine complex quadratic unit phase phi=e_p(lambda x^2+mu x),
phi(x+d)conjugate(phi(x)) is linear with frequency 2lambda d. In contrast,
the Boolean pairs C_d are real nonnegative and have G9's support cocycle.
One cannot replace them by unit-phase derivatives without proving the
normalization and error estimates. G1 explicitly shows how frequency drift
is coupled by the original spectrum rather than independent fibers.

The pure quadratic interval host from the previous note remains linearly
invisible even with the expanded H character allowance. Briefly, its
original Fourier maximum is O(log p/sqrt p). The proved quarter-factor
cutoff gives, for s added characters and harmonic cutoff m,

    energy <=(4m-3)^s O(log^2 p/p)+48s/m.

Take beta about 1/log p, s=O(sqrt(log p)/log log p), and
m=ceil(48s/(tau beta^2)) with tau tending to zero, say 1/log log p.
Then log m=O(log log p), so (4m-3)^s=exp(O(sqrt(log p)))=p^o(1).
Both terms are o(beta^2), uniformly over all such full-group factors.
Thus the enlarged budget does not linearly discretize this quadratic
Boolean family to relative constant energy. This is not a counterexample
to H: the family contains many APs. The previous constant-fraction deletion
theorem is the currently proved AP-free exclusion, and does not exclude
large deletions which might change the quadratic signal.

## 6. Relative-window normalization and exact gap

For H, B=1_A is extended by zero to Z_p and its full-group density is
alpha=a w, where w=|Omega|/p. Equations G1-G11 stay valid with alpha;
they do not magically use relative a. At the extreme permitted size
w=exp(-sqrt(log p)), alpha can be a exp(-sqrt(log p)). The averaged
negative angular mass is then of size alpha^4=a^4w^4. Replacing alpha by
a would be a normalization error. A relative/window-weighted analogue
with quantified boundary and overlap is needed before this full-group
information can establish H throughout its actual domain class.

No proof or eligible counterexample to H was obtained by the graph,
double-transform, saturation/cocycle, or quadratic-drift attacks. The exact
new distinction is that fiber angular statistics admit completely diffuse
positive graphs, while true derivatives have the product tensor G1 and
the support cocycle G9. One must exploit those two additional coupled
conditions, together with relative geometry, rather than the angular
statistics alone.

## 7. Verification and classifications

`python3 verify_structural_graph_20261002.py` passed on 2,208 Boolean subsets
in Z5,Z7,Z11 (765 AP-free), checking G1-G6 and the abstract graph equations, and 47,904 pointwise G9
instances. It also checks the genuine Z13 saturation counterexample.
Fourier checks use tolerance 1e-10. Symbolic proofs above establish the
identities; finite computation is supplementary, not asymptotic proof.

PROVED: G1-G11 as stated, diffuse abstract graph construction, expanded-budget
invisibility of the existing quadratic interval family.
REFUTED: saturated selected Boolean pair frequencies must be additive on
occupied triangles without an additional triangle-support hypothesis.
CONDITIONAL: G11's cocycle conclusion under its explicit error and Fourier
pseudorandomness hypotheses.
COMPUTATIONALLY CHECKED ONLY: the listed finite test executions.
CONJECTURED: H; neither its proof nor a counterexample follows from this note.
