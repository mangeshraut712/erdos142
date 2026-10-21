<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->

# Erdős r4 completion-driven continuation

Date: 2026-09-07 (Asia/Kolkata). Offline.

STATUS: (E) OPEN — NO NEW THEOREM

13 September correction: the conditional closing claim near the end of this
historical report was incomplete. It omitted corrected mixed statistics near
zero and supplied no terminal step after reaching a=1/2. See
[LOCALIZATION_BRIDGE.md](LOCALIZATION_BRIDGE.md) for the corrected conditional
theorem, a proved terminal window bound, and the still-open uniform coarse
arithmetic energy input. The earlier auxiliary identities remain intact.

The local target `r_4(N)=o(N/log N)` is neither proved nor disproved.
No novelty or publication claim is made for the proved auxiliary statements.

## Referee result for the current checkpoint

The detailed classifications are in:

- `frontier_audit_geometry.md`: relative formulas (1)-(18);
- `frontier_audit_operator.md`: operator/frame formulas (19)-(24);
- `frontier_audit_iteration.md`: conversion and recurrence formulas (25)-(33);
- `frontier_audit_bohr.md`: regular-Bohr geometry and fibers.

The displayed relative counting theorem (12)-(15) is proved for d>=1,
0<a<1 and its stated local-size conditions. The Bernoulli baselines are

    E Phi=a^2(C-w/p)+aw/p,
    E Sigma=a^3(C-w/p)+aw/p.

For exact size k=an they are rho_2(C-w/p)+aw/p and
rho_3(C-w/p)+aw/p, rho_j=(k)_j/(n)_j. Relative ratio (22) requires
d!=0 and q_d>0. The p=31 diameter-14 example is outside the narrow
p/3 class; p=43 repairs it. The 8192 periodic example tests one fixed
partition, is not AP-free, and has a density-one step-two progression.

The audit found an exact correction to `MIXED_INCREMENT.md`: regular
nonzero endpoint rates r_L=r_R=a imply

    Sigma=a Phi+a(1-a)w/p,

not Sigma=a Phi. The negative regular-center budget remains of order
-a^4 C under the checkpoint cutoff.

## New proved auxiliary frontier

`GLOBAL_COMPATIBILITY.md` proves:

1. the exact regular-center subtraction (equations (1)-(4));
2. impossibility of exact r_d=alpha on any active fiber of a proper
   prime-cyclic set, with only the tiny quantitative variance (6);
3. feasible exact regular-center Boolean laws for every fixed overlapping
   4-uniform configuration at sufficiently small density;
4. a fixed-size extension preserving all moments through degree three;
5. sharp endpoint mass/size recurrence bookkeeping.

The finite-law result shows that a contradiction cannot use only a bounded
collection of local one-, two-, three-point moments and represented 4AP
exclusions. A successful global argument must use a configuration growing
with 1/a or global deterministic/arithmetic consistency.

`LOW_SIGMA_SAMPLING.md` proves:

1. a density-weighted empirical approximation of the 3AP-center
   convolution using O(1/a) positive translates rather than the O(1/a^2)
   supplied by the ordinary L2 estimate;
2. a matching Omega(1/a) support obstruction for this approximation in
   the spread-convolution case;
3. a soft multiplicative density increment and an actual convolution
   level-set increment retaining a fixed fraction of A;
4. the exact reason this is not yet an arithmetic increment: the level
   set is A-dependent and need not be a controlled window.

## Exact cubic recurrence

For a guaranteed signal eta_j>=c a_j^2, the existing native conversion
gives

    log N_j >= 2^-j log N_0
      -[2log(128pi)+log(1/(c a_0))](1-2^-j).

The density recurrence a_(j+1)=a_j+k a_j^2 satisfies exactly

    1/a_j-1/a_(j+1)=k/(1+k a_j).

It needs Theta(1/a_0) steps to reach fixed density, whereas the displayed
length guarantee supports only O(log log N_0) steps. At
a_0=epsilon/log N_0 the required count is Theta(log N_0/epsilon).

More generally, if only

    mu_j(a_(j+1)-a_j)>=kappa a_j^2

is known, put r_j=mu_j a_(j+1)/a_j and u_j=1/a_j. Then exactly

    r_j(u_j-u_(j+1))>=kappa,
    log(N_0/N_J)=log(a_J/a_0)+sum log(1/r_j).

The sharp scalar consequence is

    log(N_0/N_J)
      <=log(a_J/a_0)+(1/(e kappa))(1/a_0-1/a_J).

The coefficient 1/e is attained by the scalar path recorded and checked
in `GLOBAL_COMPATIBILITY.md`. At a_0=epsilon/log N_0 the divergent term
is log N_0/(e kappa epsilon), not o(log N_0).

## Exponent, scale, and rank ledgers

| Lane | Gain | Guaranteed localization | Target test |
|---|---:|---:|---|
| high global linear signal | 10% multiplicative | prime loses <=100 | repeatable, O(log log N) total log loss |
| native eta>=c a^2 | additive >=3c a^2/8 | square-root length per step | fails after O(log log N) steps |
| Phi irregularity, fixed d | multiplicative 1+1/(128*3^d) | fixed-rank cell, constant depending on d | closes if encountered alone at fixed d |
| low Sigma | signal a^2/[3^d A(W)] | rank +1, degrading constants | no bounded hybrid potential |
| negative mixed | mixed size a^4 C | arbitrary bounded eigenmode only | no arithmetic localization |
| weighted sampling | O(1/a) translates | A-dependent convolution level set | strong scalar increment, uncontrolled domain |

Regular Bohr translation errors of relative increment radius eta cost
delta=C_reg*r*eta. Making the weighted mixed geometry error O(a^4 w)
requires delta=O(a^3), hence one guaranteed same-rank shrink costs

    r[3log(1/a)+log(C r)]

in logarithmic size. Repeated rank increases still have no proved charge
to a bounded energy or entropy potential.

## Hostile tests

- Z_11 cyclic reuse remains false.
- The affine-spread 3AP-free family defeats universal near-full-mass
  true-progression increments.
- The Z_101 28-point witness has weighted fiber mean 44/189 below 28/101
  and positive fiber deviations on 36 differences; those fibers are not
  hereditary windows.
- The fixed-size local-law construction realizes the regular-center
  table on arbitrary bounded overlapping 4AP hypergraphs.
- The Z_13 difference set keeps exactly flat nonzero Fourier magnitudes.
- A six-point controlled-window family has fixed weighted quadratic-frame
  deficit 5/33 while every normalized atom is O(p^-2).
- The 8192 periodic example has no gain on the fixed consecutive-block
  partition but is outside the AP-free class and has a cheap step-two gain.
- The weighted-sampling identities were checked on both sides of the
  low-cubic hypothesis. The Z_5 set is explicitly labelled outside that
  branch; Z_13 and Z_101 satisfy it.

## One sharpest remaining lemma

**Post-reduction structured localization lemma — OPEN.** Prove that fixed
constants kappa,C>0 exist with the following property. Let Omega be a
controlled narrow window of rank d, let A subset Omega be 4AP-free with
relative density 0<a<=1/2 and above the checkpoint size cutoff, and assume
the already-proved Phi-irregularity increment and high relative linear
signal do not occur. If either

1. the relative cubic/low-Sigma alternative holds, or
2. the regular-center-corrected mixed statistic has the checkpoint-sized
   deficit,

then there is a hereditary controlled window Omega' such that

    density_Omega'(A)>=(1+kappa)a,
    |A intersect Omega'|/|A|>=a^C,
    rank(Omega')<=d+C,

and its radius/coordinate shrink has logarithmic cost at most
C log(1/a) beyond the current window.

This exact conclusion would close the iteration: only O(log(1/a_0))
steps occur; total logarithmic size loss is O((log(1/a_0))^2), rank is
O(log(1/a_0)), and the terminal window remains large when
a_0=epsilon/log N because (log log N)^2=o(log N). The existing terminal
counting criterion then contradicts 4AP-freeness. The lemma is not proved.

## Corrected continuation prompt

Continue offline from `GLOBAL_COMPATIBILITY.md` and
`LOW_SIGMA_SAMPLING.md`. Accept the fixed-pattern regular-center laws and
the correction Sigma=a Phi+a(1-a)w/p. Do not infer structure from negative
mixed mass alone. Prove or refute the Post-reduction structured localization
lemma above. In the low-Sigma case, start from the soft convolution weight
u=1-G/(K a^2), whose multiplicative gain and mass retention are already
proved, and address only its arithmetic localization. In the mixed case,
subtract the exact regular-center value before measuring deviation. Charge
all rank and radius changes, and test the Z_11 wrap, affine-spread family,
Z_101 witness, bounded hypergraph local laws, and a=epsilon/log N.
