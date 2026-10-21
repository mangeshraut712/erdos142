<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Official Erdős problem 142

This note records the **official** problem, as numbered and stated on
[erdosproblems.com/142](https://www.erdosproblems.com/142)
([LaTeX page](https://www.erdosproblems.com/latex/142)).
It is not a solution, a new bound, or a claim that anyone can collect a
bounty from this repository.

The live site is the source of truth. Recheck wording, status, citations,
and any prize display there (and in the literature) before relying on
the paraphrase below.

## Statement

Let \(r_k(N)\) be the largest possible size of a subset of
\(\{1,\ldots,N\}\) that does not contain any nontrivial \(k\)-term
arithmetic progression. Prove an asymptotic formula for \(r_k(N)\).

Site labels: `[Er81]`, `[Er97c]`. Additional thanks recorded on the page:
Zach Hunter.

## Status

**OPEN.**

Erdős remarked that the problem is “probably unattackable at present.”
The site commentary also records that an asymptotic formula is still far
out of reach, even for \(k=3\).

## Prize notes (from site commentary; not a live bounty)

The official page comments on **historical offers by Erdős**, not on a
collectable UI attached to this pack:

- In `[Er97c]` Erdős offered \$1000. The site notes that this **seems
  odd**, because he elsewhere offered \$5000 just for (essentially)
  showing \(r_k(N)=o_k(N/\log N)\); see
  [problem 3](https://www.erdosproblems.com/3).
- In `[Er81]` he offered \$10000, stating it is “probably enormously
  difficult.”

This repository does **not** claim a live bounty button, a currently
payable prize, or that anyone can collect those amounts today. If a
bounty is listed anywhere, **verify it** on erdosproblems.com, OEIS, or
the published literature.

## Best known upper bounds (as cited on the page)

The official commentary attributes the best known upper bounds for
\(r_k(N)\) to:

- Kelley–Meka `[KeMe23]` for \(k=3\);
- Green–Tao `[GrTa17]` for \(k=4\);
- Leng–Sah–Sawhney `[LSS24]` for \(k\ge 5\).

Those citations are orientation from the site, not reproductions of the
theorems in this pack.

## Relation to this repository

The **local target** of the increment program here is

\[
r_4(N)=o(N/\log N).
\]

That is a weaker / related \(k=4\) little-o goal, closer in shape to the
[#3](https://www.erdosproblems.com/3)-style bound
\(r_k(N)=o_k(N/\log N)\) than to an asymptotic formula for every
\(r_k(N)\). Even if the local target were proved, it would **not**
settle official #142.

See [docs/PROGRESS.md](../PROGRESS.md) and
[docs/audits/MIXED_INCREMENT.md](../audits/MIXED_INCREMENT.md) §10.
Both official #142 and the local target remain open in this pack.

## Other public work

Some other public projects treat official #142 as a **WALL** (an open
asymptotic problem), for example
[techno-optimist/erdos-frontier-atlas](https://github.com/techno-optimist/erdos-frontier-atlas)
`certificates/erdos-142`. This pack **does not endorse** those
certificates, their scope, or their verification claims; the link is
only a pointer that independent work exists.
