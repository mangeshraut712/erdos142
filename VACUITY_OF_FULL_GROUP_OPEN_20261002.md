# The full-group (OPEN) statement is equivalent to its own non-vacuity

2 October 2026. **(D) NEW RIGOROUS PARTIAL THEOREM (structural).**
The target r_4(N)=o(N/log N) is neither proved nor disproved.
Novelty of the elementary lemmas is not claimed.

(OPEN) below is the statement of TARGET_SCALE_ENERGY_BUDGET_20260914.md,
section 7: for every epsilon>0 there are c_eps, K_eps, p_eps such that
every 4-AP-free A in Z_p, p>=p_eps prime, with eps/log p<=a<=4/5, admits a
rotated-quarter factor of rank <=ceil(K_eps log^2(2/a)) and
Var(E(B|F))>=c_eps a^2/log(2/a). (T) denotes r_4(N)=o(N/log N).

## 1. Transfer lemmas — PROVED

**Lemma 1 (cyclic to integer).** If A in Z_p (p>3) is 4-AP-free, then
A, read as a subset of {0,...,p-1}, has no integer 4-AP. Hence
|A|<=r_4(p).

Proof: an integer 4-AP in {0,...,p-1} has difference 0<|h|<=(p-1)/3, so
h is nonzero mod p and the same four points form a 4-AP in Z_p.

**Lemma 2 (integer to cyclic).** If A in {1,...,N} has no integer 4-AP and
p>2N is prime, then A is 4-AP-free in Z_p.

Proof: let x_0,...,x_3 in A form a 4-AP in Z_p with difference h!=0.
The integer gaps d_i=x_(i+1)-x_i lie in [-(N-1),N-1] and are all congruent
to h mod p. Since |d_i-d_j|<=2N-2<p, they are equal to one integer d, and
d!=0 because h!=0. So the x_i form an integer 4-AP, a contradiction.

The hypothesis p>2N is sharp in general: {1,2,4,5} has no integer 4-AP but
contains 2,5,1,4 mod 7 (difference 3). See the JSON for further examples.

## 2. Consequences — PROVED

**Theorem A.** (T) implies (OPEN). Indeed, given eps, (T) and Lemma 1 give
p_eps beyond which r_4(p)<eps p/log p, so no A satisfies the hypotheses of
(OPEN): the statement holds vacuously.

**Theorem B.** If (T) fails, the hypotheses of (OPEN) are met infinitely
often. Indeed there are eps>0 and infinitely many N with
r_4(N)>=eps N/log N. Take a prime p in (2N,4N] (Bertrand). By Lemma 2 an
extremal set is 4-AP-free in Z_p with density
>=eps N/(p log N)>=(eps/4)/log p, and density <=1/2<4/5.

Together: **(OPEN) has non-vacuous content exactly when (T) is false**
(up to the factor 4 in epsilon). This is the usual shape of a
proof-by-contradiction input, so (OPEN) is not useless; but it changes
what kinds of work on it can succeed.

**Corollary C (refutation is as hard as the target).** Any infinite
family of eligible counterexamples to (OPEN) at density >=eps/log p
contradicts (T) via Lemma 1, i.e. disproves the Erdős-type bound itself.
Constructive or computer searches for full-group counterexamples at the
target density cannot succeed unless (T) is false. Finite searches at
small p (e.g. RANK1_HOSTILE_SEARCH_20261002.md) only probe pre-asymptotic
behaviour.

**Corollary D (unconditional vacuous range).** Green–Tao give
r_4(N)<=C_0 N (log N)^(-c_0) for absolute c_0>0. By Lemma 1, (OPEN) holds
vacuously for densities a>C_0(log p)^(-c_0). The only non-vacuous band is

    eps/log p <= a <= C_0 (log p)^(-c_0),

which is non-empty because c_0<1 in the published bound.

**Corollary E (sparse full-group theorem is out of range).** The proved
ENERGY range a<=p^(-1/4) of FULL_GROUP_HOSTILE_AUDIT_20260914.md lies
entirely below eps/log p for large p, so it contributes nothing to (OPEN).

## 3. What this means for the program

1. Full-group (OPEN) is a consequence of the target, so its proof is only
   useful as the input to an argument by contradiction, and only together
   with the still-missing hereditary extension.
2. The only object where counterexamples can exist without disproving the
   target is the hereditary / controlled-window version, where the relative
   density inside a window can be large while the global density is not.
   Counterexample effort should go there (as UNIFORM_ENERGY_COUNTEREXAMPLE.md
   and AP_RICHNESS_COUNTEREXAMPLE.md already did), not to Z_p at density
   eps/log p.
3. Proof effort on (OPEN) may assume a <= C_0(log p)^(-c_0), i.e. it may use
   that A is already polylogarithmically sparse.

## 4. Literature status (checked online, 2 October 2026)

- r_4(N) << N(log N)^(-c): Green–Tao, *New bounds for Szemerédi's theorem
  III* (arXiv:1705.01703), described there as the limit of their methods.
- k>=5: Leng–Sah–Sawhney, r_k(N) << N exp(-(log log N)^(c_k))
  (arXiv:2402.17995); their introduction still cites Green–Tao as the
  best bound for k=4.
- erdosproblems.com/142 lists the problem as OPEN; o(N/log N) for r_k is the
  separate $5000 question referenced there as problem 3.

No published bound gives r_4(N)=o(N/log N), so (T) remains open in the
literature as well as here.

## 5. Checks

`python3 verify_vacuity_20261002.py` (about 2 minutes, standard library):
exact r_4(N) for N<=40 (agrees with OEIS A003003), exact cyclic maxima for
p<=17 with r_4(Z_p)<=r_4(p), exhaustive confirmation of Lemma 2 for every
4-AP-free subset of [1,N], N<=12, and every prime p in (2N,4N], plus
wrap-around examples for N<p<=2N. Output: vacuity_verification_20261002.json.
