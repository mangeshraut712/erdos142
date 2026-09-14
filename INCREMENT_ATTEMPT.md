# Erdős 142: one density-increment attempt

Date: 2026-09-06. **STATUS: OPEN — NO NEW ASYMPTOTIC BOUND.**

## User-reported result

This folder claimed auxiliary identities only. `README.md` explicitly leaves
the density-increment mechanism unresolved. Its finite examples are not a
proof of `r_4(N) = o(N/log N)`.

Read before this attempt: `README.md`, `verify_core.py`, `verification.json`,
and `CODEX_TASK.md`. No repo-level `AGENTS.md`, `CODEX.md`, or `codex.md` was
present; the supplied task instructions governed this offline work.

## Locally verified result

Canonical command, run successfully with exit code 0:

```bash
python3 verify_core.py
```

Captured stdout, matching the existing `verification.json`:

```json
{
  "status": "finite auxiliary checks passed; no asymptotic theorem proved",
  "exact_counting_energy_subsets": 2208,
  "nonempty_proper_4ap_free_subsets": 762,
  "exact_four_atom_subsets": 2288,
  "exact_general_even_spectral_arrays": 276,
  "groups_for_counting": [
    5,
    7,
    11
  ],
  "extra_groups_for_degeneracies": [
    4,
    6
  ],
  "spectral_kernel_counterexample": "float check of exact radical formulas, tolerance 1e-12",
  "external_dependencies": []
}
```

The core checks retain all five rejected shortcuts. Their passing status
confirms the recorded counterexamples, not the rejected claims. The kernel
calculation still has the explicitly reported floating-point tolerance;
the exhaustive rational checks are distinct from it.

New command, also exit code 0:

```bash
python3 verify_increment.py > increment_verification.json
```

The new checker uses only Python standard-library integers and `Fraction`:

- It checks the one lemma below on all **10,392 nonempty proper subsets** of
  `Z_5`, `Z_7`, `Z_11`, and `Z_13`; eight empty/full subsets are outside its
  hypotheses. There are **zero counterexamples to this lemma** in that scan.
- It exhausts every nonzero step, every start, and both permitted lengths.
  Squaring a positive gain makes its comparison with the radical bound exact.
- Direct rational definitions independently cross-check the energy calculation
  and progression enumeration on all **160 subsets** of `Z_5` and `Z_7`.
- Of the 10,392 sets, **2,647** are 4AP-free. **None** satisfy
  `p alpha^3 >= 2`; these checks do not exercise that regime of the earlier
  simplified U3 bound.
- The existing `Z_5`, `Z_7`, and flat-spectrum `Z_13` indicator examples are
  checked explicitly. `Z_4` and `Z_6` are outside the prime-group hypothesis;
  the weighted function `g` is outside the indicator hypothesis. Arbitrary
  spectral arrays need not come from indicators. Their original core checks
  remain intact.
- It also verifies the cyclic reuse counterexample below, including both
  integer-interval 4AP-freeness and failure of cyclic 4AP-freeness.

Full numerical witnesses and counts are in
[`increment_verification.json`](increment_verification.json).
The canonical verifier, README, and original captured result were not edited.

## Increment attempt

### The single proposed lemma

Let `p > 3` be prime and let `A` be a nonempty proper subset of `Z_p`. Put

\[
\alpha=|A|/p,\qquad f=1_A-\alpha,\qquad b=\alpha(1-\alpha)>0,
\]

and use the normalized Fourier transform

\[
\widehat f(k)=\frac1p\sum_{x\in\mathbb Z_p} f(x)e^{-2\pi i kx/p},
\qquad W_k=|\widehat f(k)|^2,\qquad S=\sum_k W_k^2.
\]

Then there is a **cyclic arithmetic progression**

\[
P=\{x+jd:0\le j<\ell\}\subset\mathbb Z_p,\qquad d\ne0,
\quad \ell\in\{(p-1)/2,(p+1)/2\},
\]

such that

\[
\boxed{\quad\frac{|A\cap P|}{|P|}\ge
\alpha+\frac13\sqrt{\frac S b}\quad}.
\]

If `A` is 4AP-free for nonzero differences, its pullback to the integer
index interval `[0, ell-1]` is also 4AP-free. No assertion is made that the
pullback is 4AP-free in `Z_ell`.

**Proof status:** complete elementary proof below, independent of the finite
checks. No novelty claim. This is a single-step lemma, not an iterable
density-increment theorem of the strength requested for Erdős 142.

### Proof

1. **Extract a Fourier coefficient from the existing energy.** Parseval and
   balancing give

   \[
   W_0=0,\qquad \sum_k W_k=b,\qquad
   S\le (\max_{k\ne0}W_k)b.
   \]

   Thus some `k != 0` has `W_k >= S/b`. Since `f` is real,
   `W_{-k}=W_k`; these are distinct frequencies because `p` is odd.

2. **Average over a long progression aligned with that coefficient.** Set
   `L=(p-1)/2`, choose `d=k^{-1}` modulo `p`, and define

   \[
   H(x)=\frac1L\sum_{j=0}^{L-1} f(x+jd).
   \]

   This real function has mean zero. Its Fourier transform at a frequency
   `xi` is `fhat(xi) K(xi d)`, where

   \[
   K(a)=\frac1L\sum_{j=0}^{L-1}e^{2\pi i aj/p}.
   \]

   The finite geometric sum gives the exact identity

   \[
   |K(1)|=\frac{\sin(\pi L/p)}{L\sin(\pi/p)}\ge\frac2\pi>\frac12.
   \]

   For completeness, put `theta=pi/p`. Since `0<L theta<pi/2`, concavity
   of sine on `[0,pi/2]` gives `sin(L theta)>=2L theta/pi`, while
   `sin(theta)<=theta`. These establish the displayed inequality.
   Applying Parseval to `H` and retaining the two frequencies `k,-k` gives

   \[
   \mathbb E_x H(x)^2\ge2W_k|K(1)|^2\ge\frac{W_k}{2}.
   \]

   Consequently some `x` has `|H(x)|>=sqrt(W_k/2)`.

3. **Turn either sign into a positive density increment.** If `H(x)>0`,
   take `P={x+jd:0<=j<L}`. Its density gain is `H(x)`.
   If `H(x)<0`, take its complement, which is the progression

   \[
   P=\{x+Ld+jd:0\le j<M\},\qquad M=(p+1)/2.
   \]

   Nonzero `d` traverses all of `Z_p`, so these sets partition the group.
   The total sum of `f` is zero, hence the complementary progression's
   density gain is `-(L/M)H(x)`. Since
   `L/M=(p-1)/(p+1)>=2/3`, in either case the gain is at least

   \[
   \frac23\sqrt{\frac{W_k}{2}}
   =\frac{\sqrt2}{3}\sqrt{W_k}
   \ge\frac13\sqrt{\frac S b}.
   \]

4. **Check the stated preservation property.** The map `j -> x+jd` is
   injective on the chosen index interval because `ell<p`. An ordinary
   nonconstant integer 4AP contained in that interval maps to a 4AP in
   `Z_p` with nonzero difference: its positive index difference is less
   than `p`, and `d` is invertible. Such an AP cannot lie in the pullback
   of a 4AP-free `A`. This proves the interval assertion and completes the
   lemma's proof.

The checker's rational energy is the same `S`: writing
`c_h=E_x f(x)f(x+h)`, Fourier orthogonality gives
`c_h=sum_k W_k exp(2 pi i kh/p)` and `E_h c_h^2=sum_k W_k^2`.
If `n=|A|` and `m_h=|A intersect (A-h)|`, then

\[
S=\frac1{p^5}\sum_h (p m_h-n^2)^2.
\]

Thus neither its energy comparisons nor its counterexamples require
approximating Fourier radicals.

### Existing examples and the new counterexample

These are exact witnesses selected by the exhaustive checker, not evidence
for an asymptotic theorem:

| Group and set | Selected progression, in order | Density gain | Required gain squared `S/(9b)` |
|---|---|---|---|
| `Z_5`, `{0,1}` | `0,1` | `3/5` | `7/675` |
| `Z_7`, `{0,1,3}` | `0,1,2,3` | `9/28` | `2/441` |
| `Z_13`, `{0,1,3,9}` | `1,3,5,7,9,11,0` | `24/91` | `1/507` |

The `Z_13` example still has `W_k=3/169` for every nonzero frequency:
`b=36/169`, `S=108/28561`. The proof uses the inequality
`max W_k>=S/b`, which permits equality and flat spectra; it does not revive
the rejected claim of forced spectral nonflatness. It uses no residual
composition, residual sign transfer, spectral-kernel composition, or
strengthened general `Lambda_4` inequality.

**A new exact obstruction to automatically repeating this step:**

- In `Z_11`, take `A={6,8,9,10}`. It has no nonzero-difference 4AP.
- The allowed progression `P={6,7,8,9,10}` has density `4/5`, exceeding
  `alpha=4/11` by `24/55`. Here `S/(9b)=5/1089`, so this witness satisfies
  the proposed lemma's increment bound.
- Its integer index set is `B={0,2,3,4}` in `[0,4]`, which is 4AP-free as
  an integer set.
- In `Z_5`, however, `0,4,3,2` is a nonzero-difference 4AP in `B`, with
  common difference `4`. Mapping these four indices back gives
  `6,10,9,8`, whose successive differences in `Z_11` are `4,10,10`;
  it is not a 4AP in the original group.

This is a counterexample to automatic cyclic reuse of a valid output, not
to the single-step lemma. It does not rule out every possible choice of
output or every future iteration method. It rules out treating interval
4AP-freeness as sufficient for cyclic 4AP-freeness. **That reuse line stops
here; no repair or second increment lemma is attempted.**

### Quantitative gap relative to the requested iteration

The one-step set is large:

\[
|P|\ge(p-1)/2\ge2p/5,
\qquad \log(p/|P|)\le\log(5/2).
\]

There are nevertheless two separate missing ingredients:

1. **An adequate density-dependent gain has not been obtained.** The
   general bound `S>=b^2/(p-1)` supplies a gain of only
   `sqrt(b/(p-1))/3` through this lemma. This guarantee has order
   `sqrt(alpha/p)` in the sparse regime. At `alpha=epsilon/log p`, it is
   far smaller than any fixed positive power of `alpha`.
   The earlier U3 lower bound does not reverse the verified inequality
   `S^2<=||f||_{U3}^8` to give a lower bound on `S`. Likewise,
   `D/S^2>=S/b^2` provides an upper bound on `S` when the relative defect
   is small. No additional concentration conclusion is established here.
2. **The ambient hypotheses do not automatically persist.** The output
   is an integer interval with a selected subset, not a 4AP-free subset of
   a new prime cyclic group. Its length need not be prime; the explicit
   example shows that even prime length does not resolve the wrap issue.

Accordingly, the constant one-step logarithmic loss does **not** justify
assigning `t=0` to a valid iteration. No repeatable pair of exponents `s,t`
has been obtained, and neither `s+t-1<1` nor an endpoint saving has been
established. The finite examples and the elementary lemma do not supply
the missing deduction of `r_4(N)=o(N/log N)`.

## Mathematical status

**Erdős 142 remains OPEN under the requested status standard.** A full
proof of one elementary cyclic-progression increment lemma is written
above, but the auxiliary estimates have not been converted into the
required iterable mechanism. There is no new asymptotic bound, no proof of
the target little-o statement, and no claim of research novelty.

One increment lemma was considered. Its finite checks passed; automatic
cyclic reuse has an exact counterexample. No public posting, network
research, dependency installation, or change to the canonical verifier was
performed.

## Next verification step

Reproduce the recorded cyclic reuse obstruction by running
`python3 verify_increment.py` and checking the
`cyclic_reuse_counterexample` object: it must report `index_set=[0,2,3,4]`,
`wrapped_4ap=[0,4,3,2]`, `integer_interval_4ap_free=true`, and
`cyclic_4ap_free=false`. This check already passes locally; it is the
concrete independent reproduction check, not a proposed second research
lane.
