<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Progress report — Erdős 142 pack

**Status: (E) OPEN — SINGLE FINAL OBSTRUCTION.**

Author: Mangesh Raut. Offline notes from 2026-09-06 through 2026-09-14,
now public. Finite Python checks support some algebraic identities; they
are not an asymptotic proof.

This file only records claims already written in [docs/audits/](audits/).
It does not add a proof, a prize amount, or a “solved” claim.

## What the pack is trying to do

The notes work toward a density-increment iteration whose **local
target** is

\[
r_4(N)=o(N/\log N).
\]

That target is neither proved nor disproved here.

**Official Erdős problem 142** is treated as a separate, still-open
statement. The mixed-increment write-up is explicit: even a proof of the
local target would not give an asymptotic formula for all \(r_k(N)\), so
it would not by itself settle official #142
([MIXED_INCREMENT.md](audits/MIXED_INCREMENT.md) §10;
[COMPATIBILITY.md](audits/COMPATIBILITY.md)). Read the official wording
on [erdosproblems.com/142](https://www.erdosproblems.com/142). If a
prize or bounty is attached, verify it there, on OEIS, or in the
literature. This repository records **no** prize amount and **no**
completion.

## How far we are (one paragraph)

Auxiliary counting, U³, signed-operator, and relative-window identities
are proved in the notes and checked on small groups. Several tempting
shortcuts are refuted (cyclic reuse, residual-sign transfer, unrestricted
uniform energy, AP-richness implying coarse energy, actual-U³ inverse
with exponent \(C<2\)). A localization bridge reduces a remaining
increment to a **uniform coarse arithmetic energy** input. That energy
theorem, under the full size/AP-availability cutoff, is the named
closing obstruction. Its full-group case \(\Omega=\mathbb Z_p\) is
settled only in trivial or ineligible regimes; the Freiman-embedded
sphere family is the remaining natural instance. The local target and
official #142 are both still open.

## The single final obstruction

From [ENDPOINT_INCIDENCE_AUDIT.md](audits/ENDPOINT_INCIDENCE_AUDIT.md)
§5, status **(E) OPEN — SINGLE FINAL OBSTRUCTION**:

**Unproved full-cutoff arithmetic energy theorem.** There exist absolute
constants \(\eta>0\) and \(C>0\) such that for every prime \(p>3\), every
checkpoint controlled window \(\Omega\) of rank \(r\) and size \(n\), and
every nonempty 4-AP-free \(A\subset\Omega\) of density \(0<a\le 4/5\)
satisfying the full cutoff

\[
n \ge \max\bigl(256\, r\, 3^r,\; 8\cdot 3^r a^{-3}\bigr),
\]

there is a factor obtained by quantizing at most \(\lceil C\log(2/a)\rceil\)
characters into four equal half-open arcs (rotations allowed), restricted
to \(\Omega\), such that

\[
\mathrm{Var}_\Omega\bigl(E(1_A\mid F)\bigr) \ge \eta a^2.
\]

This is a **sufficient** closing theorem in the existing iteration
bookkeeping ([LOCALIZATION_BRIDGE.md](audits/LOCALIZATION_BRIDGE.md)).
It is not proved. Endpoint-incidence identities (orientation, star
degree \(\le 3\), entropy bounds, middle-pair Gram matrix) do not
supply it.

**Full-group specialization** \(\Omega=\mathbb Z_p\)
([FULL_GROUP_ENERGY_AUDIT.md](audits/FULL_GROUP_ENERGY_AUDIT.md)):
neither a proof nor an eligible counterexample in the nontrivial regime
\(p > 4^{\lceil C\log(2/a)\rceil}\). The remaining concrete instance is
the Freiman-embedded sphere family \(A_d\) of that audit, §8, with
generic \(u\).

A **relaxed** energy hypothesis (rank \(a^{-c}\), \(c<1/2\), or polylog,
at density \(\ge \varepsilon/(2\log n)\)) is proved *sufficient* for the
local target (Theorem 9 there). That weaker hypothesis is also unproved.

## Attempted lanes (what happened)

| Lane | Where | Outcome |
|---|---|---|
| Core U³ / four-atom / spectral identities | [CORE_AUXILIARY_IDENTITIES.md](audits/CORE_AUXILIARY_IDENTITIES.md) | Proved as auxiliary statements; no increment |
| One-step density increment | [INCREMENT_ATTEMPT.md](audits/INCREMENT_ATTEMPT.md) | No new asymptotic; cyclic reuse obstruction |
| Phase 2 inverse | [PHASE2_AUDIT.md](audits/PHASE2_AUDIT.md) | \(\alpha^{3/2}\) lemma verified; actual-U³ \(C<2\) impossible; density-sensitive inverse still open |
| Signed operator / Rayleigh | [SIGNED_RESEARCH.md](audits/SIGNED_RESEARCH.md) | Identities recorded; no sufficient arithmetic increment; universal near-full-mass increment on integer APs disproved (affine-spreading) |
| Relative / controlled windows | [RELATIVE_WINDOWS.md](audits/RELATIVE_WINDOWS.md), frontier audits | Relative counting (12)–(15) proved under stated hypotheses; \(r_4\) open |
| Mixed increment | [MIXED_INCREMENT.md](audits/MIXED_INCREMENT.md) | Regular-center mixed deficit is not itself an increment |
| Compatibility / local laws | [GLOBAL_COMPATIBILITY.md](audits/GLOBAL_COMPATIBILITY.md), [COMPATIBILITY.md](audits/COMPATIBILITY.md) | Bounded local 4-uniform laws cannot force a contradiction; need growing or global arithmetic structure |
| Low-\(\Sigma\) sampling | [LOW_SIGMA_SAMPLING.md](audits/LOW_SIGMA_SAMPLING.md) | Soft increment on an A-dependent level set; not a controlled window |
| Localization bridge | [LOCALIZATION_BRIDGE.md](audits/LOCALIZATION_BRIDGE.md) | Signed compression → factor energy and a terminal window bound proved; uniform arithmetic factor missing |
| Unrestricted uniform energy | [UNIFORM_ENERGY_COUNTEREXAMPLE.md](audits/UNIFORM_ENERGY_COUNTEREXAMPLE.md) | **Refuted** without the cutoff; cutoff-qualified lemma untouched |
| AP richness / density-only entropy | [AP_RICHNESS_COUNTEREXAMPLE.md](audits/AP_RICHNESS_COUNTEREXAMPLE.md) | **Refuted** as a replacement for relative coarse energy |
| Endpoint incidence | [ENDPOINT_INCIDENCE_AUDIT.md](audits/ENDPOINT_INCIDENCE_AUDIT.md) | Conventions and Gram formulas; energy theorem still open |
| Full-group energy | [FULL_GROUP_ENERGY_AUDIT.md](audits/FULL_GROUP_ENERGY_AUDIT.md) | Partial theorems in trivial/ineligible regimes; nontrivial regime open |

## Settled vs open (conservative)

### Proved in the notes (auxiliary; novelty not claimed)

- Exact indicator counting and the mixed Cauchy–Schwarz U³ lower bound,
  including \(\|f\|_{U^3}\ge \alpha^{3/2}/2\) when \(p\alpha^3\ge 2\).
- Four-atom residual description and the spectral defect identities \(D\).
- Phase 2: \(\alpha^{3/2}\) lemma; impossibility of a uniform actual-U³
  correlation bound with \(C<2\) even in the stipulated AP-free density
  regime.
- Relative counting theorem (12)–(15) for \(d\ge 1\), \(0<a<1\), under
  the stated local-size conditions; regular-center correction
  \(\Sigma=a\Phi+a(1-a)w/p\).
- Signed-compression-to-factor-energy bridge and a direct terminal
  window bound (localization write-up).
- Full-group energy: trivial true at the sparse end of its own cutoff;
  interval-supported Behrend/sphere sets, affine images, and random
  thinnings are trivial YES instances; log-rank window form would imply
  \(r_3(N)\le N\exp(-c(\log N)^{1/4})\) via the checkpointed bridge;
  rank \(a^{-c}\) (\(c<1/2\)) at density \(\ge\varepsilon/(2\log n)\)
  already suffices for the local \(r_4\) target *if* that energy
  hypothesis is proved.

### Refuted (named statements only)

- Deterministic two-step residual composition from identical successive
  pairs (\(\mathbb Z_7\), \(\{0,1,3\}\)).
- Passing the forbidden pair-indicator correlation sign to the residual
  alone (\(\mathbb Z_5\), \(\{0,1\}\)).
- Proposed strengthening \(|\Lambda_4(g)|\le U^3(g)^4\).
- Universal near-full-mass true-progression increment on integer
  progressions (affine-spreading family).
- Uniform energy lemma **quantified over every controlled window without
  the size/AP-availability cutoff**.
- “Total AP richness plus density-only direction-support/entropy bounds
  force relative coarse energy.”
- Using only a bounded collection of local one-, two-, three-point
  moments and represented 4-AP exclusions to get a global contradiction.

### Still open

- Official Erdős #142.
- Local target \(r_4(N)=o(N/\log N)\).
- The full-cutoff arithmetic energy theorem (the single obstruction).
- (ENERGY_p) in the nontrivial full-group regime; Freiman-embedded
  sphere family.
- Density-sensitive inverse / increment with iteration-compatible
  exponents (the original unresolved step of 2026-09-06).
- Post-reduction structured localization lemma of
  [FINAL_FRONTIER_REPORT.md](audits/FINAL_FRONTIER_REPORT.md) (later
  corrected: that lemma alone would not close the target without further
  repairs recorded in the localization bridge).

## Finite verification

Checkers are Python 3, standard library only. Latest captured JSON lives
in `verification/results/`. A pass means the finite identities in that
script held on the listed examples. It does **not** mean \(r_4\) or #142
is proved.

See the root README for commands.

## Prize and publication

No prize completion is claimed. No literature novelty is claimed for the
auxiliary statements. No DOI is registered yet
([PRIORITY_AND_ATTRIBUTION.md](PRIORITY_AND_ATTRIBUTION.md)).
