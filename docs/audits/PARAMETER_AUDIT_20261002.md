# Parameter audit for the symmetric candidate

2 October 2026. **(D) AUDIT plus a sharpened junta theorem; candidate
still (E) OPEN** (the mixed-factor step is a sketch). Notation as in
SYMMETRIZATION_20261002.md and GENERIC_FACTORS_20261002.md. The window
energy lemma and the target r_4(N)=o(N/log N) remain unproved and
unrefuted.

## 1. Density of the random-alteration B — CORRECTION

The proofs use the random-alteration B of CANDIDATE_LEMMAS section 4. Its
density is a = beta*Theta(1/sqrt r) = Theta(r^(-3/4+eps/2)), not the
r^(-1/2) of the searched B. Measured: a r^(3/4) = 0.45, 0.64, 0.61 at
r=300, 1200, 4800, so log(2/a) = (3/4 - eps/2) log r (1+o(1)), and every
factor size k = C log(2/a) is O(log r) for each fixed C. The cutoff
4^r >= 8*3^(r+1) a^(-3) holds with log-margin 68, 325, 1357.

**Consequence.** The junta bound Y^2 <= 3 a s/r of SYMMETRIZATION section 2
and GENERIC_FACTORS section 1 gives Y^2/a^2 <= 3s/(a r). That allows only
s = o(a r/log r) = o(r^(1/4+eps/2)/log r), and a r/log r is 0.33 to 0.60 at
the sizes above. The statements "Y^2/a^2 = O(s/sqrt r)" and
"s = o(sqrt(r)/log r)" there assumed a of order r^(-1/2) and are corrected
by section 3 below.

## 2. Every threshold, for fixed C and eps

| quantity | order | needed | holds for r >= r_0(C,eps) |
|---|---|---|---|
| mod-15 energy / a^2 | log w / w^(1/2+eps) | o(1/log r) | yes |
| strongly generic energy / a^2 | k^2/(a r^2) = r^(-5/4+o(1)) | o(1/log r) | yes |
| smoothing degree H | r^(M'), M' = O(C) | 4^k r^(-M'/2) -> 0 | yes |
| threshold T | O(C log r log log r) | <= Psi_max = r/4 | yes |
| absorption steps | k + k log_2(sqrt(k) H) = O(C^2 log^2 r) | polylog | yes |
| drift digits g | polylog, depending on C | polylog | yes |
| junta |S'| | steps x (T/delta^2+1)(g+1) = polylog | section 3 allowance | yes |

All constants are uniform for each fixed C. Only r_0 depends on C and eps.

## 3. Sharpened junta theorem — PROVED (density-free)

Since E[f_2 1_V] = E[f_2 P(V|n)] = E[f_2 D_V] exactly (the class part is
orthogonal to f_2), the energy of the junta partition (u_S, sigma mod 15),
with |S|=s, is exactly

    Y^2 = sum_V (E[f_2 D_V])^2 / mu(V),

with no Cauchy–Schwarz. For typical n (|n_d - r/4| <= sqrt(r) log r),

    P(u_S=p | n) / P(u_S=p | class) = 1 + sum_d m_d 4(n_d - E[n_d|c])/r + O(s^2 log^2 r / r),

where m are the digit counts of p; the term is exactly linear when s=1.
Averaging over patterns (m ~ Mult(s,1/4), and sum_d L_(d,c) = 0) gives

    Y^2 = (4s/r^2) sum_c sum_d L_(d,c)^2 / P(c) + O(a^2 s^4 log^4 r / r^2),
    L_(d,c) = E[f_2 n_d 1_c] = P(c) w_c (E[n_d | A, c] - E[n_d | c]).

For the candidate, every mass-carrying count vector of A is a line mode on
a typical line, so |E[n_d|A,c] - r/4| <= sqrt(r) log r (atypical mass
exp(-c log^2 r) << a), and E[n_d|c] = r/4 + O(e^(-cr)). Hence

    Y^2 / a^2 <= 16 s log^2 r / r * (max_c w_c / a)^2 + O(s^4 log^4 r / r^2),

which is o(1/log r) for s = o(sqrt(r) / log^(5/2) r), **independently of
a**. The polylog juntas of CELL_BOOKKEEPING, SYMMETRIZATION section 3 and
MIXED_FACTORS are therefore covered for the random-alteration B.

Checked exactly (verify_linear_junta_20261002.py, balanced B, s=1, where
the linearization is exact):

| r | predicted slope / a^2 | measured / a^2 | max count bias | sqrt(r) log r |
|---|---:|---:|---:|---:|
| 100 | 2.3339e-3 | 2.3339e-3 | 7.7 | 46 |
| 300 | 7.3673e-4 | 7.3673e-4 | 8.2 | 99 |
| 600 | 2.0254e-4 | 2.0254e-4 | 5.8 | 157 |

The count bias of A is O(1) in practice, far inside the sqrt(r) log r used
in the proof, so the true junta energy is about a^2 s/r.

## 4. Status after the audit

Proved, with no numerical input:
- 4-AP-freeness, density and cutoff;
- mod-15 balance (smoothness replaced unimodality);
- junta plus residue for s = o(sqrt(r)/log^(5/2) r);
- factors of exceptional characters;
- strongly generic factors.

Sketch only: mixed factors (MIXED_FACTORS_20261002.md). Its open write-up
points are minorants on cosets and the index check with drift. Constants
are uniform in C (section 2).

## 5. Checks

- `python3 verify_parameter_audit_20261002.py` (about 1 second): the
  density scaling and cutoff margins.
- `python3 verify_linear_junta_20261002.py` (about 9 minutes, dominated
  by enumerating all count vectors at r=600): the section 3 formula against
  the exact energies, and the count-bias bound.

Outputs: parameter_audit_verification_20261002.json,
linear_junta_verification_20261002.json.
