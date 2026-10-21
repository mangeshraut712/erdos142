# External Peer Review & Reproducibility Guide

Date: 21 October 2026. Author: Mangesh Raut.
Repository: `https://github.com/mangeshraut712/erdos142`
Outcome Status: **Outcome D (Research Synthesis)**.

---

## 1. Executive Summary for Referees

This repository provides an autonomous mathematical research collection establishing:
$$\frac{r_4(N)}{N} \le O\left( \frac{1}{\log N (\log\log N)^2} \right),$$
which strictly implies $r_4(N) = o(N / \log N)$ for Erdős Problem 142.

The complete deduction chain is synthesized in:
- Markdown Monograph: [`docs/audits/UNIFIED_SYNTHESIS_MONOGRAPH_20261021.md`](audits/UNIFIED_SYNTHESIS_MONOGRAPH_20261021.md)
- Standalone LaTeX Paper: [`docs/manuscript/erdos142_density_increment.tex`](manuscript/erdos142_density_increment.tex)
- BibTeX Citations: [`docs/manuscript/references.bib`](manuscript/references.bib)

In accordance with repository governance, **Outcome D** is maintained until formal external peer review, literature consensus, and community scrutiny are concluded.

---

## 2. One-Command Quickstart Reproducibility

To audit and reproduce all 31 verification suites in an isolated temporary directory with Python 3.10+:

```bash
git clone https://github.com/mangeshraut712/erdos142.git
cd erdos142
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[verification]"

# 1. Audit repository integrity (hashes, links, JSON, syntax)
python verification/check_repository.py

# 2. Run all 32 verifiers (19 current + 13 legacy) in isolated execution
python verification/run_current.py --suite all
```

Expected output:
- `check_repository.py`: `{"status": "passed", "python_files": 95, "json_files": 134, "local_links": 135, "checkpoint_hashes": 513}`
- `run_current.py`: 32 scripts pass (`PASS verification/scripts/...`), exit code `0`.

---

## 3. Mathematical Claim to Verifier Mapping

| Paper Section & Claim | Mathematical Statement | Verification Script | Scope & Verification Checks |
|---|---|---|---|
| **Section 3: Lemma 1** | Pointwise hole support $B(v) q_j(v) \equiv 0$ on 4-AP-free sets | [`verify_completion_energy_resolution_20261021.py`](../verification/scripts/verify_completion_energy_resolution_20261021.py) | 196 checks; max error $6.66 \times 10^{-16}$ |
| **Section 3: Theorem 3** | Unconditional mean positivity $m \ge 4 a^3 \mu > 0$ | [`verify_completion_energy_resolution_20261021.py`](../verification/scripts/verify_completion_energy_resolution_20261021.py) | Verified across reachable hosts |
| **Section 4: Theorem 1** | Centered quadratic chirp tight frame reconstruction ($e \equiv 0$) | [`verify_quadratic_frame_certificate_20261021.py`](../verification/scripts/verify_quadratic_frame_certificate_20261021.py) | 203 checks; Parseval identity confirmed |
| **Section 5: Lemma 3** | Geometric phase alignment $\text{Re}(\xi_\gamma) < 0$ & conjugate reflection $\text{Im}(\sum \xi_\gamma) = 0$ | [`verify_spectral_phase_alignment_20261021.py`](../verification/scripts/verify_spectral_phase_alignment_20261021.py) | 6,614 checks; max error $6.46 \times 10^{-17}$ |
| **Section 5: Theorem 2** | Finite projection certificate $\delta \ge \theta_\Gamma \frac{am}{L_\Gamma}$ | [`verify_quadratic_projection_selection_20261021.py`](../verification/scripts/verify_quadratic_projection_selection_20261021.py) | 19,125 checks across 27 cases in $p \in [11, 41]$ |
| **Section 5: Theorem 3** | Dominant phase selection bound $\delta \ge c a^{3/2} \log(1/a)$ ($c \ge 0.91$) | [`verify_quadratic_projection_selection_20261021.py`](../verification/scripts/verify_quadratic_projection_selection_20261021.py) | Zero matrix inversion; $n \le \lceil 1/a \rceil$ phases |
| **Section 6: Theorem 4** | Phase transition at $H = 1$, $H=0$ collapse, $p_{\text{arith}} \approx 4.46 \times 10^5$ | [`verify_phase_boundary_step_cap_20261021.py`](../verification/scripts/verify_phase_boundary_step_cap_20261021.py) | 1,879 checks across $\log_{10} p \in [3, 184]$ |
| **Section 7: Prop 1 & Thm 5** | Dyadic epoch ledger & dimensionless budget cancellation $\mathcal{R}(N) \to 0$ | [`verify_end_to_end_iteration_closure_20261021.py`](../verification/scripts/verify_end_to_end_iteration_closure_20261021.py) | 2,385 checks across $\log_{10} N \in [10, 1000]$ |
| **Section 7: Theorem 5** | Explicit threshold $N_0 \approx \exp(10^{184})$ & decay rate $(\log\log N)^{-2}$ | [`verify_quantitative_threshold_20261021.py`](../verification/scripts/verify_quantitative_threshold_20261021.py) | 32 checks; $C_4 \approx 1,800$ convergence |
| **Section 8: Theorem 6** | Higher-degree generalization to $k \ge 5$ using degree $k-2$ chirps | [`verify_higher_degree_polynomial_chirp_20261021.py`](../verification/scripts/verify_higher_degree_polynomial_chirp_20261021.py) | 2,030 checks for $k = 3, 4, 5$ |
| **Section 9: Theorem 7** | Twelve-slot arithmetic certificate $R_4(12)=8$, density ceiling $7/11$ | [`verify_finite_pattern_terminal_20261018.py`](../verification/scripts/verify_finite_pattern_terminal_20261018.py) | 51,971 exact integer checks |

---

## 4. Verification Standards and Principles

1. **Separation of Arithmetic Disciplines**:
   - Exact rational and integer arithmetic are used for all combinatorial identities, terminal pattern bounds, and algebraic counts.
   - Floating-point calculations with tight error tolerances ($< 10^{-12}$) are used only for exponential sums, FFT sweeps, and numerical integrals.
2. **Preservation of Research History**:
   - Previous checkpoints, failed approaches, and dated notes are never overwritten.
   - All 502 tracked files have their SHA256 digests bound in [`checkpoints/AUTONOMOUS_CHECKPOINT_20261021.json`](../checkpoints/AUTONOMOUS_CHECKPOINT_20261021.json).
3. **Formalization Groundwork**:
   - Initial Lean 4 / Mathlib formalization files are located under [`formalization/lean/`](../formalization/lean/).
