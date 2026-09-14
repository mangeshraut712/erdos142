# Contributing

Thank you for considering a contribution to this public research pack.
The author of record is **Mangesh Raut** (`@mangeshraut712`).

This repository is intentionally public. Anyone can clone it. Contribution
rules protect **credit, license integrity, and mathematical honesty**, not
secrecy. See [docs/PRIORITY_AND_ATTRIBUTION.md](docs/PRIORITY_AND_ATTRIBUTION.md).

## Mathematical honesty (non-negotiable)

- Official Erdős problem 142 and the local target `r_4(N) = o(N/log N)`
  remain **open** in this pack. Do not mark them solved.
- Finite Python checks are diagnostics. They are not an asymptotic proof.
- Do not invent a prize amount, DOI, or literature credit. If a bounty
  exists, verify it on [erdosproblems.com](https://www.erdosproblems.com/)
  (problem 142), OEIS, or the published literature, and cite the source.
- Refutations and partial theorems must name the **exact statement** they
  address. Several energy lemmas in this pack were refuted only after the
  size/AP-availability cutoff was dropped; that is not a refutation of the
  cutoff-qualified lemma.

## How to help

Suggested next steps are in [docs/ROADMAP.md](docs/ROADMAP.md) and the
continuation prompts at the ends of the latest audits under
[docs/audits/](docs/audits/). Open an issue before a large write-up so
priority and overlap are visible.

## Development

Python **standard library only**. No third-party packages are required.

```bash
python3 verification/scripts/verify_core.py
python3 verification/scripts/verify_full_group_energy.py
```

Keep new checkers in `verification/scripts/` and captured JSON in
`verification/results/`.

## License of contributions (CLA-lite)

By submitting a contribution (pull request, patch, issue with proposed
text, or other intentional submission) you agree that:

1. You license your contribution under the **Apache License 2.0**, jointly
   with the project, so it can be redistributed with the rest of the Work.
2. You have the right to make that grant (you wrote it, or you have
   permission from the copyright holder).
3. You will **not strip attribution**: copyright headers, `NOTICE`,
   `AUTHORS`, `CITATION.cff`, SPDX identifiers, and author names in
   research notes must remain.
4. You add a DCO sign-off on every commit (below).

This is a short contributor license agreement, not a transfer of your
moral right to be named. Independent write-ups that use this work should
cite the repository; contact the author first if you plan a paper that
relies on unpublished arguments from this pack.

## Developer Certificate of Origin

Each commit must include:

```
Signed-off-by: Your Name <your@email>
```

Use `git commit -s`. That certifies the [Developer Certificate of Origin](https://developercertificate.org/):

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

## Pull requests

- Base against `main`.
- One mathematical claim per PR when possible, with a verifier or an
  explicit statement that the claim is purely analytic.
- Update [docs/PROGRESS.md](docs/PROGRESS.md) if status changes. Never
  upgrade status to "solved" without a complete, peer-checkable proof.
