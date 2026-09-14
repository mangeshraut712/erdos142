<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Roadmap / contribution ideas

The problem is open. Useful work is a proof or a cutoff-eligible
counterexample of the remaining energy theorem, or a clearly weaker
hypothesis that still closes the iteration ledger.

Do not open a PR that only restates a refuted lemma without the cutoff.

## Highest leverage (named in the latest audits)

1. **Full-cutoff arithmetic energy theorem**
   ([ENDPOINT_INCIDENCE_AUDIT.md](audits/ENDPOINT_INCIDENCE_AUDIT.md) §5).
   Prove it, or give a deterministic family that meets the entire cutoff
   and drives factor energy to \(o(a^2)\). Star entropy and the middle-pair
   Gram matrix are already recorded; they are not the theorem.

2. **Freiman-embedded sphere family** \(A_d=\phi(\mathrm{shell})\)
   ([FULL_GROUP_ENERGY_AUDIT.md](audits/FULL_GROUP_ENERGY_AUDIT.md) §8, §12).
   Bound \(\sup_F \mathrm{Var}(E(1_A\mid F))/a^2\) over quarter-arc factors
   of rank \(\le C\log(2/a)\) either below by an absolute \(\eta\) for all
   generic \(u\), or show it tends to \(0\) for some \(u\). Union bounds
   over factors are not available; the argument has to be structural.

3. **Relaxed energy (Theorem 9)** in the same full-group audit: rank
   \(a^{-1/3}\) (or polylog), density \(a\ge\varepsilon/(2\log n)\), full
   cutoff, energy \(\eta a^2\), using 4-AP-freeness essentially. This is
   enough for the local \(r_4\) target if proved. It is not a proof of
   official #142.

## Secondary lanes (still open, already constrained)

- Arithmetic localization of the low-\(\Sigma\) convolution level set
  ([LOW_SIGMA_SAMPLING.md](audits/LOW_SIGMA_SAMPLING.md)): multiplicative
  gain is proved; the domain is not a controlled window.
- After alternatives I–II, hereditary-window alignment of \(r_d-a\) with
  \(s+t<2\) ([MIXED_INCREMENT.md](audits/MIXED_INCREMENT.md) §11). Do not
  extract increment from mixed mass alone.
- Density-sensitive inverse with iteration-compatible exponents (original
  2026-09-06 unresolved step). The actual-U³ \(C<2\) route is closed.

## Tests every new claim should survive

The notes already use these as hostile tests. A proposed increment or
energy statement should say what it does on:

- \(\mathbb Z_{11}\) cyclic reuse
- affine-spread 3-AP-free family
- \(\mathbb Z_{101}\) 28-point diagnostic (often ineligible for cutoffs)
- bounded overlapping 4-AP hypergraph local laws
- unrestricted vs cutoff-qualified energy (the logarithmic-density
  digit-window family)
- AP-rich ambient progressions that miss \(A\)
- \(a=\varepsilon/\log N\)

## Housekeeping (welcome, lower mathematical priority)

- Archive a tagged snapshot on Zenodo once the author wants a DOI
  (do not invent a DOI).
- Add a verifier only when a new finite identity is actually used.
- Keep Python stdlib-only.

## Status rule

The pack stays **OPEN** unless a complete, peer-checkable proof of the
claimed statement is written. Finite JSON is not that proof. Official
#142 is not the same as the local \(r_4\) target.
