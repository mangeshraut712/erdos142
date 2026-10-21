# Symmetrization: step 1 proved, step 2 reduced to the uniform measure

2 October 2026. **(D) NEW RIGOROUS THEOREMS; candidate still (E) OPEN.**
Continues CANDIDATE_LEMMAS_20261002.md section 5 and CELL_BOOKKEEPING_20261002.md.
Notation: box {0,1,2,3}^r with uniform measure, n(u) the count vector,
P the partition by sigma mod 15. A is any permutation-invariant set
(the candidate is one) of density a, with f_2 = 1_A - E(1_A|P). The window
energy lemma and the target r_4(N)=o(N/log N) remain unproved and
unrefuted.

## 1. Symmetrization identity — PROVED

Let F be any factor with cells V, c_V = E(f_2|V) and Y^2 = ||E(f_2|F)||^2.
Put

    D_V(u) = P(V | n(u)) - P(V | P(u)).

Then

    Y^2 = sum_V c_V E[f_2 D_V],      Y^2 <= sum_V (E[|f_2| |D_V|])^2 / mu(V).

Proof. Y^2 = <f_2, h> with h = sum_V c_V 1_V. Since f_2 is
permutation-invariant, <f_2,h> = <f_2, E(h|n)>, and E(h|n) = sum_V c_V
P(V|n). Because E(f_2|P)=0 and P is coarser than n, <f_2, E(h|P)> = 0;
subtract it. The inequality follows by Cauchy–Schwarz, using
sum_V mu(V) c_V^2 = Y^2.

**Meaning.** A and B enter only through |f_2|. Everything else is about the
**uniform** measure: how much the probability of each cell, given the count
vector, differs from its probability given sigma mod 15.

## 2. Step 1 (junta plus residue) — PROVED for |S| = o(sqrt(r)/log r)

Take F = (u_S, sigma mod 15) with |S| = s, and for a pattern p on S put
rho_p(n) = P(u_S=p | n) / P(u_S=p | sigma class) - 1. For V=(p,c),
D_V = 1_c P(p|c) rho_p, so Cauchy–Schwarz in n within the class c gives
(E|f_2||D_V|)^2/mu(V) <= E[f_2^2 | c] P(p|c) E[1_c rho_p^2]. Since
f_2^2 <= |f_2| <= 1_A + w, we have E[f_2^2|c] <= 2w_c, so

    Y^2 <= 2 max_c w_c * E_p E_n[rho_p(n)^2] * (1+o(1)).

Here o(1) covers P(u_S=p | class) = 4^(-s)(1 + O(theta^(r-s))) with
theta<1 (the digit sum mod 15 equidistributes exponentially fast).

By factorial moments of the multinomial, using
(x)_m^2 = sum_j C(m,j)^2 j! (x)_(2m-j) and E prod_d (n_d)_(b_d) =
(r)_(|b|) 4^(-|b|):

    E_n[(4^s P(u_S=p|n) - 1)^2] = (4 sum_d m_d^2 - s^2)/r + O(s^4/r^2),

where m are the digit counts of p. Averaged over p this is
3s/r (1+O(s/r)). Hence

    Y^2 <= 6 (max_c w_c) s / r (1+o(1)),   so   Y^2/a^2 = O(s/(a r)) = O(s/sqrt r)

(max_c w_c = a(1+o(1)) for the balanced B). At r=100 and s=1 this bound
is 6/(a r) = 0.94 in units of a^2, above both the exact section 1 bound
(0.057) and the measured energy (0.0023).

This is o(1/log(2/a)) whenever s = o(sqrt(r)/log r), and in particular for
every polylog-size junta. It holds for every permutation-invariant A,
with no randomness in B. Together with the mod-15 balance (CANDIDATE_LEMMAS
section 4, now fully proved since level smoothness replaced the
unimodality input) this proves step 1, and it explains the linear growth in s measured in CANDIDATE_LEMMAS
section 5.

**Correction (PARAMETER_AUDIT_20261002.md).** The random-alteration B has
a = Theta(r^(-3/4+eps/2)), so the bound above allows only s = o(a r/log r).
PARAMETER_AUDIT section 3 replaces it with the density-free bound
Y^2/a^2 <= 16 s log^2 r/r + O(s^4 log^4 r/r^2), valid for
s = o(sqrt(r)/log^(5/2) r).

## 3. Exceptional factors — PROVED (no assumption beyond section 4 balance)

CELL_BOOKKEEPING section 5 assumed a uniform relative bound on every fine
cell; an L^2 bound suffices. Let G = (u_(S'), sigma mod 15) and let U be
the (G-measurable) undecided set, so every cell of F differs from a union
of G-cells only inside U. Then V \ U is G-measurable, and

    Y_F^2 = <E(f_2|G), sum_V c_V 1_(V\U)> + sum_V c_V E[f_2 1_(V∩U)]
          <= Y_G Y_F + E[(1_A + w) 1_U],

so Y_F <= Y_G + (E[(1_A+w)1_U])^(1/2). E[1_A 1_U] <= E[w 1_U] + Y_G mu(U)^(1/2),
and mu(U) = r^(-M). With |S'| = polylog(r), section 2 gives Y_F^2 =
o(a^2/log(2/a)). **Every factor built from O(log r) exceptional
quarter-arc characters has energy o(a^2/log(2/a)) on the candidate**
(given the balanced B).

## 4. What remains: a statement about the uniform measure only — OPEN

By section 1, the candidate refutes the window energy lemma (base-16
realization, full cutoff) if, for every factor F of at most C log(2/a)
quarter-arc characters,

    sum_V (E[|f_2| |D_V|])^2 / mu(V) = o(a^2 / log(2/a)).

A sufficient condition is the **count-vector equidistribution property**:
the mu-weighted mean of tau_V^2 is o(1/log r), where tau_V is the relative
deviation sup over typical n of |P(V|n)/P(V|class(n)) - 1|. Atypical n
(|n_d - r/4| > sqrt(r) log r) have mass r^(-omega(1)) and are absorbed
separately by Cauchy–Schwarz in n.

This involves neither A nor B. Juntas satisfy it (tau^2 about s/r) and
exceptional characters reduce to juntas. The open case is factors
containing generic characters: the phases phi_j X(u) of a uniform
arrangement with fixed counts n must be jointly equidistributed at scale
4^(-k), relative to their distribution given only sigma mod 15. The
Fourier route meets the (log H)^k = r^(Theta(log log r)) coefficient mass
recorded in CELL_BOOKKEEPING section 6, so a different method is needed:
for example a swap coupling between count vectors n and n' with the same
sigma mod 15, controlling the influence of one random digit change on
arc cells.

## 5. Checks

`python3 verify_symmetrization_20261002.py` (about 30 seconds).

- **Part A** (exact, r=6, 4096 points): over 40 random symmetric A and
  factors of 1 to 3 random quarter-arc characters, it asserts that the
  identity holds to 1e-12 and that the inequality holds (worst ratio
  Y^2/rhs 0.17).
- **Part B** (count space, r=100, balanced B), for s=1 to 4:

  | s | measured Y^2/a^2 | bound/a^2 | mean rho^2 | 3s/r |
  |---|---:|---:|---:|---:|
  | 1 | 0.0023 | 0.057 | 0.0300 | 0.03 |
  | 2 | 0.0049 | 0.115 | 0.0612 | 0.06 |
  | 3 | 0.0076 | 0.176 | 0.0937 | 0.09 |
  | 4 | 0.0106 | 0.235 | 0.1275 | 0.12 |

  The bound from section 1 is computed exactly and asserted to dominate
  the measured energy, and the mean of rho^2 is asserted to be within 20%
  of 3s/r.

Output: symmetrization_verification_20261002.json.
