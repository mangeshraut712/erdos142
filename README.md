<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Erdős problem 142 — research pack

**Status: (E) OPEN — SINGLE FINAL OBSTRUCTION**

Author: [Mangesh Raut](https://github.com/mangeshraut712)
(`mbr63@drexel.edu`). Offline notes from **2026-09-06**, continued
through **2026-09-14**, now a public repository.

This is a working notebook with finite checkers, not a completed
solution. There is no proof of \(r_4(N)=o(N/\log N)\), no proof of
official Erdős #142, no new claimed asymptotic, and no prize claim.

## Problem (as used in these notes)

Let \(r_4(N)\) be the size of the largest subset of \(\{1,\ldots,N\}\)
with no 4-term arithmetic progression. The **local target** of the
increment program here is

\[
r_4(N)=o(N/\log N).
\]

That target is open. The notes repeatedly distinguish it from
**official Erdős problem 142**, which is also open and is **not**
settled by a \(k=4\) little-o bound of this shape even if one were
proved ([docs/audits/MIXED_INCREMENT.md](docs/audits/MIXED_INCREMENT.md)
§10). Official statement:
[docs/literature/OFFICIAL_142.md](docs/literature/OFFICIAL_142.md);
live pages
[erdosproblems.com/142](https://www.erdosproblems.com/142) and
[latex/142](https://www.erdosproblems.com/latex/142).

If a bounty is listed anywhere, verify it on that site, OEIS, or the
literature. Historical prize remarks from the official commentary are
in [OFFICIAL_142.md](docs/literature/OFFICIAL_142.md); this pack does
not claim a live, collectable bounty.

## How far we are

Auxiliary identities (U³ lower bounds, relative-window counting,
signed-operator algebra, a localization bridge) are written and, where
claimed, checked on small cyclic groups. Several proposed closing lemmas
are **refuted** (unrestricted uniform energy; AP-richness as a substitute
for coarse energy; actual-U³ inverse with exponent \(C<2\); mixed mass
as a ready-made increment).

What remains is one sufficient closing input: a **full-cutoff arithmetic
energy theorem** (logarithmic-rank quarter-arc factors with
\(\mathrm{Var}(E(1_A\mid F))\ge\eta a^2\)). That is the “single final
obstruction.” Details, including the full-group \(\mathbb Z_p\) case and
the Freiman-embedded sphere family, are in
**[docs/PROGRESS.md](docs/PROGRESS.md)**. Next steps:
[docs/ROADMAP.md](docs/ROADMAP.md).

## Quickstart (verifiers)

Python 3, **standard library only** (`pyproject.toml` lists no runtime
dependencies). From the repository root:

```bash
python3 verification/scripts/verify_core.py
python3 verification/scripts/verify_phase2.py
python3 verification/scripts/verify_signed.py
python3 verification/scripts/verify_relative.py
python3 verification/scripts/verify_increment.py
python3 verification/scripts/verify_mixed.py
python3 verification/scripts/verify_compat.py
python3 verification/scripts/verify_compatibility.py
python3 verification/scripts/verify_localization.py
python3 verification/scripts/verify_energy_counterexample.py
python3 verification/scripts/verify_ap_richness.py
python3 verification/scripts/verify_endpoint_incidence.py
python3 verification/scripts/verify_full_group_energy.py
```

Most scripts print JSON on stdout. Captured runs live in
`verification/results/`. `verify_full_group_energy.py` also writes
`verification/results/full_group_energy_verification.json`. A passing
script means the finite checks in that file succeeded. It is not a
proof of the local target.

After this layout change (2026-09-14), all thirteen `verify_*.py`
scripts were rerun from the repo root; all exited 0. That does not
change the open status of the mathematics.

## Repository map

```
README.md                 this page
LICENSE, NOTICE           Apache-2.0
CITATION.cff, AUTHORS     citation and author of record
CONTRIBUTING.md           DCO + CLA-lite
CODE_OF_CONDUCT.md, SECURITY.md
docs/PROGRESS.md          proved / refuted / open
docs/ROADMAP.md           contribution ideas
docs/PRIORITY_AND_ATTRIBUTION.md
docs/literature/          external problem page; no invented bounty
docs/audits/              full research trail (markdown)
verification/scripts/     verify_*.py and _probe_terminal.py
verification/results/     captured JSON
pyproject.toml            metadata; stdlib-only
```

Codeowners: [@mangeshraut712](.github/CODEOWNERS).

## Contributing and sponsors

Patches that prove, refute, or correctly weaken the remaining energy
theorem are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md): Apache-2.0
on contributions, DCO sign-off (`git commit -s`), do not strip
attribution, do not mark the problem solved from examples.

Sponsor the author via [GitHub Sponsors](https://github.com/sponsors/mangeshraut712)
or the [GitHub profile](https://github.com/mangeshraut712).

## Citation

```
Mangesh Raut, Erdős problem 142 research pack,
https://github.com/mangeshraut712/erdos142, 2026.
```

Machine-readable: [CITATION.cff](CITATION.cff). A Zenodo DOI is
recommended later; none is registered yet.

## License

Copyright 2026 Mangesh Raut. Licensed under the Apache License 2.0.
SPDX-License-Identifier: Apache-2.0. See [LICENSE](LICENSE) and
[NOTICE](NOTICE).

## Public copies

This repository is public on purpose. Cloning cannot be prevented.
Copyright headers, NOTICE, DCO/CLA-lite, and citation metadata exist so
that reuse keeps the author’s name and does not pretend the mathematics
is finished. They are not a secrecy mechanism.
See [docs/PRIORITY_AND_ATTRIBUTION.md](docs/PRIORITY_AND_ATTRIBUTION.md).
