# Cell bookkeeping for the symmetric candidate

2 October 2026. **(D) NEW RIGOROUS REDUCTIONS; candidate still (E) OPEN.**
Step 2 of CANDIDATE_LEMMAS_20261002.md section 5. Notation as there: box
{0,1,2,3}^r in the base-16 window, X(u)=sum u_i 16^i, sigma(u)=sum u_i,
A={u: n(u) in T} of density a (of order r^(-1/2)), f=1_A-a. A quarter-arc
character with frequency phi in R/Z cuts the box by phi*X(u) mod 1 into
four arcs of length 1/4. The window energy lemma and the target
r_4(N)=o(N/log N) remain unproved and unrefuted.

Result: factors built only from **exceptional** characters (mod-15 class
plus few-digit perturbation) reduce exactly to step 1 with polylog juntas,
with no small-cell loss. Factors containing **generic** characters still
need a combination lemma (section 6), and the obvious regularization
iteration provably overshoots.

## 1. Splitting off the mod-15 part — PROVED

Let f_1=E(f | sigma mod 15) and f_2=f-f_1=1_A-E(1_A | sigma mod 15), so
|f_2|<=1. For any factor F,

    ||E(f|F)||^2 <= 2||f_1||^2 + 2||E(f_2|F)||^2,

and ||f_1||^2 is the mod-15 energy, o(a^2/log(2/a)) by
CANDIDATE_LEMMAS section 4 (now fully proved; level smoothness replaced
the unimodality input).

## 2. No small-cell loss — PROVED

Let F have cells V. Suppose each V satisfies
|E(f_2 1_V)| <= eta*a*mu(V) + e_V. Then with Y=||E(f_2|F)||,

    Y^2 = sum_V E(f_2 1_V) E(f_2|V) <= eta*a*sum_V mu(V)|E(f_2|V)| + sum_V e_V
        <= eta*a*Y + sum_V e_V        (Cauchy-Schwarz, |E(f_2|V)|<=1),

so Y^2 <= 2 eta^2 a^2 + 2 sum_V e_V. Small cells only enter through
sum_V e_V. **Consequence:** step 1 needs only uniform relative error
eta=o((log r)^(-1/2)), not o(1/log r), since the energy is quadratic in eta.

## 3. Exact phase identity and the run lemma — PROVED

Write phi=k/15+y. Since 16=1 mod 15, X(u)=sigma(u) mod 15, so exactly

    phi*X(u) = k*sigma(u)/15 + sum_i u_i z_i  (mod 1),
    z_i = signed representative of 16^i y mod 1 in (-1/2,1/2].

Call i bad if |z_i|>rho=1/33, and let S be the bad indices. **Run lemma:**
if i and i+1 are good then z_(i+1)=16 z_i exactly (16 z_i-z_(i+1) is an
integer of modulus at most 17 rho<1). So on a maximal good run with top
index b, z_(b-j)=16^(-j) z_b: the drift decays geometrically downward
from the top of each run.

Relation to section 3 of CANDIDATE_LEMMAS: if fewer than L' indices are
bad for (phi, gamma) at level delta, then with rho=2delta/15 at most
2L'+1 indices are bad for y. So "exceptional" (fewer than L=2L'+2 bad
indices for some k) and "decayed" (every gamma has at least L' bad
indices, Fourier coefficient <=(r+1)^2 exp(-2L' delta^2)) cover all phi.

## 4. Cantor small-ball bound — PROVED

Let X_g=sum_{j=1}^g u_j 16^(-j) with u_j uniform in {0,1,2,3}. Level-m
cylinders have length 16^(-m)/5 and gaps of 4*16^(-m)/5, so an interval
of length l<=4*16^(-m)/5 meets at most two of them:
P(X_g in J) <= 2*4^(-m) <= 2 sqrt(20 l) for l >= 16^(-g). Checked exactly
for g=8 over many interval lengths (worst ratio to the bound 0.248).

## 5. Factors of exceptional characters — PROVED (modulo step 1)

Let phi have bad set S with |S|<L, take g>=1, and let S' be S together
with the top g indices of every good run (|S'|<=L(g+1)+g). Put

    psi(u) = k sigma/15 + sum_{i in S'} u_i z_i,
    eps    = (16/5) 16^(-g) sum_{long runs} |z_b|,

the sum over runs of length >g. Then |phi X - psi| <= eps (mod 1), so for
any arc Q, membership of u in {phi X in Q} is determined by
(sigma mod 15, u_(S')) except on U={psi within eps of an endpoint of Q}.
U is itself (sigma mod 15, u_(S'))-measurable. Splitting by the digit sum
of the g-block of the run maximizing |z_b| (15 classes) and applying
section 4 to that block,

    mu(U) <= 2 endpoints * 15 * 2 * 4^(-m),  m >= g-1-log_16(#runs)-O(1).

For a factor of k exceptional characters take S' as the union (size
<=k(L(g+1)+g)) and U as the union of the bad sets. Every cell V is then a
union of (sigma mod 15, u_(S'))-cells W up to U. If step 1 gives
|E(1_A|W)-E(1_A|sigma class)| <= eta*a on all W, then

    |E(f_2 1_V)| <= eta*a*mu(V) + 3a*mu(U ∩ V),

using E(1_A|W)<=2a on the W composing U. Section 2 gives

    ||E(f_2|F)||^2 <= 2eta^2 a^2 + 6a*mu(U) <= 2eta^2 a^2 + 360 k a 4^(-m).

With g = C log r, k = O(log r) and L = polylog(r): 4^(-m) = r^(-C'),
|S'| = polylog(r), and the energy is o(a^2/log(2/a)) provided eta =
o((log r)^(-1/2)). The number of cells never enters.

Checked exactly: the phase identity, and "decided implies correct
membership", on every point of the box for 12 planted frequencies at r=7
and 6 at r=9 (g=2), about 1.8 million points in total. Undecided mass was
at most 0.019 with juntas of size 3 to 7. The constant 60 makes the
displayed bound vacuous at these sizes, so the mass bound is asymptotic
only.

Update: SYMMETRIZATION_20261002.md section 3 removes the step-1
assumption (an L^2 bound on the fine partition suffices), so this case is
now proved outright.

## 6. What remains: generic characters and combinations — OPEN

1. **Aliasing in Beurling–Selberg.** For a decayed phi, sandwiching the
   arc by degree-H polynomials needs every multiple h*phi with 0<|h|<=H to
   be decayed or to sum to small total mass. A generic phi can have
   exceptional multiples (phi near (k/15+y)/h + l/h); these terms have
   coefficient O(1/H) each, so the requirement is
   #{|h|<=H : h phi exceptional} = o(H/polylog r). Not proved.
   Partial: RATIONAL_CLASSES_20261002.md gives the orbit form of the
   decay and disposes of small odd denominators not dividing 15h.
2. **Mixed factors.** For a factor with exceptional and generic
   characters, condition on the exceptional fine partition W first. Then
   f_2 1_W is count-symmetric on the coordinates outside S', and section
   2 of CANDIDATE_LEMMAS applies to combinations sum m_j phi_j of the
   generic characters if each has at least L_gen >> |S'| bad indices
   outside S'.
3. **The tower obstruction.** If some combination of generic characters is
   exceptional, the natural move is to declare it exceptional, enlarge S'
   and repeat. Each round needs L_(j+1) >= 2g*sum_(i<=j) L_i, so after
   k = C log r rounds L_k >= (2g)^k = r^(Omega(log log r)) > r. **The naive
   regularization fails at k of order log r.** A proof needs a structural
   bound on exceptional combinations (for example, that the frequencies
   sum m_j phi_j that are exceptional lie in a set of bounded rank), not
   iteration.

If items 1 to 3 and step 1 (now with eta=o((log r)^(-1/2))) hold, A
refutes the window energy lemma with the full cutoff in the base-16
realization. The target r_4(N)=o(N/log N) would not be refuted.

## 7. Checks

`python3 verify_cell_bookkeeping_20261002.py` (about 65 seconds):
- 33,232 exact instances of the run lemma (rational arithmetic);
- the small-ball bound for g=8 over interval lengths 2^(-m) times
  {1,2,3,5,8,13};
- the exact phase identity and decided/undecided decomposition on full
  boxes, as above.

Output: cell_bookkeeping_verification_20261002.json.
