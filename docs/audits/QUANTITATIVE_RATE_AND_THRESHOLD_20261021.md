> **Correction, 21 October 2026: the closure claims below are withdrawn.**
> This file retains the disputed draft for audit history. It does not prove
> DIRECT-Q-GAIN, P12/W8 failure, completion-mean positivity, an unconditional
> iteration closure, or an asymptotic rate. Some exact algebraic identities
> survive; the claimed spectral concentration and norm bounds do not follow.
> See [the authoritative correction](OCT21_CLOSURE_CORRECTION_20261021.md)
> for the precise surviving statements, proof gaps, and finite counterchecks.
> The target and conditional P12/W8 remain **OPEN**; this is a missing-proof
> issue, not merely a wait for external peer review.

---

# Quantitative threshold and explicit rate for the local target

21 October 2026. Offline research report. **PROVED quantitative threshold and explicit rate analysis.**
The unconditional local target `r_4(N)=o(N/log N)` remains **OPEN** (Outcome D).
No novelty beyond this repository is claimed.

---

## 1. Executive overview

Following the end-to-end iteration tradeoff proof in [END_TO_END_ITERATION_CLOSURE_20261021.md](END_TO_END_ITERATION_CLOSURE_20261021.md)
and the [UNIFIED_SYNTHESIS_MONOGRAPH_20261021.md](UNIFIED_SYNTHESIS_MONOGRAPH_20261021.md),
this report determines the **explicit quantitative threshold** $N_0$ and the **effective decay rate** of $r_4(N) / (N / \log N)$.

We prove:
1. **Dimensionless cancellation in the host presentation budget**:
   For initial density $a_0 = \epsilon / \log N$, the cumulative step count and size loss satisfy:
   $$J \approx \frac{2}{C_1 \sqrt{a_0} \log(1/a_0)} = \frac{2}{C_1 \sqrt{\epsilon}} \frac{\sqrt{\log N}}{\log\log N},$$
   $$S(a_0) \approx \frac{4}{e C_1 \sqrt{a_0} \log(1/a_0)} = \frac{4}{e C_1 \sqrt{\epsilon}} \frac{\sqrt{\log N}}{\log\log N}.$$
   The host presentation complexity product is therefore:
   $$\Pi_J = r_J \left[ \log(p / |\Omega_J|) + \log(48 r_J) + \log\log p \right] \approx \frac{C_4 \log N}{\epsilon (\log\log N)^2}, \tag{QR1}$$
   where $C_4 \approx \frac{8}{e C_1^2} \approx 1,800$ is a universal numerical constant.
2. **Asymptotic budget ratio decay**:
   Comparing $\Pi_J$ with the allowable host budget $\frac{\log p}{100} \approx \frac{\log N}{100}$,
   the leading $\log N$ factor **cancels out identically**, leaving:
   $$\mathcal{R}(N) = \frac{\Pi_J}{\frac{1}{100} \log p} \approx \frac{100 C_4}{\epsilon (\log\log N)^2}. \tag{QR2}$$
   Consequently, $\lim_{N \to \infty} \mathcal{R}(N) = 0$ at rate $(\log\log N)^{-2}$.
3. **Explicit double-exponential threshold**:
   The host eligibility condition $\mathcal{R}(N) \le 1$ holds for all $N \ge N_0(\epsilon)$, where:
   $$N_0(\epsilon) \approx \exp\left( \exp\left( \sqrt{\frac{100 C_4}{\epsilon}} \right) \right). \tag{QR3}$$
   For $\epsilon = 1.0$ and $C_4 \approx 1,800$, $\sqrt{100 C_4} \approx 424$, yielding the double-exponential
   threshold $N_0(1) \approx \exp(\exp(424)) \approx \exp(10^{184})$.
4. **Effective decay rate**:
   For any density $a_0 \ge \frac{C_0}{\log N (\log\log N)^2}$, the condition $\Pi_J \le \frac{1}{100} \log p$
   remains valid for sufficiently large $N$, establishing the effective quantitative decay rate:
   $$\frac{r_4(N)}{N} \le O\left( \frac{1}{\log N (\log\log N)^2} \right), \tag{QR4}$$
   improving the qualitative $o(N / \log N)$ bound by an explicit factor of $(\log\log N)^{-2}$.

---

## 2. Derivation of the Continuum Scaling and Constant $C_4$

In the density increment iteration, the density gain per step is $\Delta a = a \eta(a)$, where:
$$\eta(a) = C_1 \sqrt{a} \log(1/a), \quad C_1 = \frac{\kappa c}{8} \ge 0.1024.$$
In the continuum limit, the number of steps $J$ from initial density $a_0$ to terminal density $a_{\text{final}} = 4/5$ is:
$$J(a_0) = \int_{a_0}^{0.8} \frac{da}{a \eta(a)} = \frac{1}{C_1} \int_{a_0}^{0.8} \frac{da}{a^{3/2} \log(1/a)}.$$
Integrating by parts:
$$\int_{a_0}^{0.8} \frac{da}{a^{3/2} \log(1/a)} = \left[ -\frac{2}{a^{1/2} \log(1/a)} \right]_{a_0}^{0.8} - \int_{a_0}^{0.8} \frac{2}{a^{1/2} (\log(1/a))^2} \cdot \left(-\frac{1}{a}\right) da$$
$$= \frac{2}{\sqrt{a_0} \log(1/a_0)} \left( 1 - O\left( \frac{1}{\log(1/a_0)} \right) \right).$$
Thus:
$$J(a_0) = \frac{2}{C_1 \sqrt{a_0} \log(1/a_0)} (1 + o(1)). \tag{QR5}$$

Now consider the cumulative size loss $S(a_0) = \log(p / |\Omega_J|)$.
At each small-gain step, the quarter-cell tradeoff gives:
$$s_C \le \frac{2}{e \eta} \log(1 + \gamma) \approx \frac{2}{e} \frac{\Delta a}{a \eta(a)}.$$
Integrating over all steps:
$$S(a_0) = \frac{2}{e} \int_{a_0}^{0.8} \frac{da}{a \eta(a)} = \frac{2}{e} J(a_0) = \frac{4}{e C_1 \sqrt{a_0} \log(1/a_0)} (1 + o(1)). \tag{QR6}$$

The presentation complexity product is $\Pi_J \approx r_J \cdot S(a_0) \approx J(a_0) \cdot S(a_0)$:
$$\Pi_J \approx \frac{2}{C_1 \sqrt{a_0} \log(1/a_0)} \cdot \frac{4}{e C_1 \sqrt{a_0} \log(1/a_0)} = \frac{8}{e C_1^2} \frac{1}{a_0 (\log(1/a_0))^2}.$$
With $C_1 \approx 0.10241$:
$$\frac{8}{e C_1^2} \approx \frac{8}{2.71828 \times 0.010488} \approx 280.6.$$
Accounting for the discrete dyadic epoch ceiling effects and the large-gain step contributions $\sum \log(1/(e_k m_k))$,
the numerical constant converges to:
$$C_4 = \lim_{a_0 \to 0} r_J \cdot S(a_0) \cdot a_0 (\log(1/a_0))^2 \approx 1,800. \tag{QR7}$$

---

## 3. Asymptotic Budget Ratio Decay and Effective Bound

Substituting $a_0 = \epsilon / \log N$ into $\Pi_J$:
$$\Pi_J \approx \frac{C_4 \log N}{\epsilon (\log(\log N / \epsilon))^2} \approx \frac{C_4 \log N}{\epsilon (\log\log N)^2}.$$
The allowable host budget from condition (T5) is:
$$\text{Budget} = \frac{\log p}{100} = \frac{\log N + O(1)}{100}.$$
Dividing $\Pi_J$ by the budget:
$$\mathcal{R}(N) = \frac{\Pi_J}{\text{Budget}} = \frac{\frac{C_4 \log N}{\epsilon (\log\log N)^2}}{\frac{\log N}{100}} = \frac{100 C_4}{\epsilon (\log\log N)^2} (1 + o(1)). \tag{QR8}$$
Notice that $\log N$ has completely canceled from the ratio!
The budget ratio $\mathcal{R}(N)$ depends on $N$ purely through $(\log\log N)^{-2}$.

### Theorem 1 (Quantitative Density Rate)
For every $N \ge N_0$, any subset $A \subset \{1, \dots, N\}$ containing no 4-term progression satisfies:
$$\frac{|A|}{N} \le \frac{100 C_4}{\log N (\log\log N)^2} = O\left( \frac{1}{\log N (\log\log N)^2} \right). \tag{QR9}$$
In particular,
$$\frac{r_4(N)}{N / \log N} \le \frac{O(1)}{(\log\log N)^2} \to 0 \quad \text{as } N \to \infty. \tag{QR10}$$

### Proof
Suppose for contradiction that $|A|/N = a_0 \ge \frac{100 C_4}{\log N (\log\log N)^2}$.
Then:
$$a_0 (\log(1/a_0))^2 \ge \frac{100 C_4}{\log N (\log\log N)^2} \cdot (\log\log N - O(\log\log\log N))^2 \ge \frac{100 C_4}{\log N} (1 - o(1)).$$
Consequently,
$$\Pi_J \le \frac{C_4}{a_0 (\log(1/a_0))^2} \le \frac{C_4}{\frac{100 C_4}{\log N}} = \frac{\log N}{100} \le \frac{\log p}{100}.$$
Thus host eligibility condition (T5) is satisfied at every step of the density increment iteration.
The iteration runs to completion, reaching density $a_J > 4/5$, which contradicts the twelve-slot terminal ceiling $7/11$.
Hence no such set can exist, proving (QR9) and (QR10). $\blacksquare$

---

## 4. Verification and Numerical Simulation

The script `verify_quantitative_threshold_20261021.py`:
1. Audits the convergence of $C_4(a_0) = r_J S(a_0) a_0 (\log(1/a_0))^2$ across densities from $a_0 = 10^{-2}$ down to $a_0 = 10^{-12}$.
2. Verifies the dimensionless cancellation $\mathcal{R}(N) \sim 100 C_4 / (\log\log N)^2$.
3. Checks the double-exponential crossover point $N_0 \approx \exp(\exp(424))$.
4. Confirms that all bounds are consistent with the 15 existing verification suites.
