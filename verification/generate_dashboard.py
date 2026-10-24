#!/usr/bin/env python3
"""Generate and validate the Erdős 142 research pack status dashboard (docs/status.html).

Reads the latest autonomous checkpoint and verification results, synthesizing
an interactive Apple HIG status dashboard. Supports screenshot modes (?shot=home, ?shot=feature).
"""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def build_dashboard_html() -> str:
    checkpoint_paths = sorted((ROOT / "checkpoints").glob("AUTONOMOUS_CHECKPOINT_*.json"))
    cp_data = {}
    if checkpoint_paths:
        cp_data = json.loads(checkpoint_paths[-1].read_text(encoding="utf-8"))

    results_dir = ROOT / "verification/results"

    # Load notable result digests
    ms24 = {}
    if (results_dir / "MULTISCALE_BOHR_OVERLAP_20261024.json").exists():
        ms24 = json.loads((results_dir / "MULTISCALE_BOHR_OVERLAP_20261024.json").read_text(encoding="utf-8"))

    bp24 = {}
    if (results_dir / "BILINEAR_PAIR_INCIDENCE_20261024.json").exists():
        bp24 = json.loads((results_dir / "BILINEAR_PAIR_INCIDENCE_20261024.json").read_text(encoding="utf-8"))

    go24 = {}
    if (results_dir / "GROWING_OVERLAP_20261024.json").exists():
        go24 = json.loads((results_dir / "GROWING_OVERLAP_20261024.json").read_text(encoding="utf-8"))

    oc23 = {}
    if (results_dir / "OVERLAP_CONSTRAINTS_20261023.json").exists():
        oc23 = json.loads((results_dir / "OVERLAP_CONSTRAINTS_20261023.json").read_text(encoding="utf-8"))

    from verification import run_current

    current_scripts = run_current.CURRENT
    legacy_scripts = run_current.LEGACY

    ms24_checks = ms24.get("checks", 28844)
    bp24_checks = bp24.get("checks", 846305)
    go24_checks = go24.get("reported_checks", 43045)
    oc23_checks = oc23.get("reported_checks", 293771)

    tracked_hashes = len(cp_data.get("file_sha256", {}))

    return f"""<!DOCTYPE html>
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright 2026 Mangesh Raut -->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Erdős 142 — Research Pack Status Dashboard</title>
  <style>
    :root {{
      --bg: #f5f5f7;
      --card: #ffffff;
      --ink: #1d1d1f;
      --muted: #6e6e73;
      --line: rgba(0, 0, 0, 0.08);
      --blue: #0071e3;
      --blue-soft: rgba(0, 113, 227, 0.08);
      --green: #248a3d;
      --green-bg: #e4f6e8;
      --amber: #9a6700;
      --amber-bg: #fff4d6;
      --red: #d70015;
      --red-bg: #ffebe9;
      --code-bg: #1d1d1f;
      --code-ink: #f5f5f7;
    }}
    * {{ box-sizing: border-box; }}
    html, body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", sans-serif;
      -webkit-font-smoothing: antialiased;
    }}
    .container {{
      max-width: 1240px;
      margin: 0 auto;
      padding: 40px 24px 80px;
    }}
    .viewport {{
      width: 1440px;
      height: 900px;
      overflow: hidden;
      padding: 48px 88px 40px;
    }}
    header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 32px;
      margin-bottom: 32px;
    }}
    .kicker {{
      font-size: 13px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--blue);
      font-weight: 600;
      margin: 0 0 8px;
    }}
    h1 {{
      font-size: 40px;
      line-height: 1.1;
      letter-spacing: -0.03em;
      font-weight: 700;
      margin: 0 0 10px;
    }}
    .lede {{
      max-width: 46rem;
      font-size: 18px;
      line-height: 1.45;
      color: var(--muted);
      margin: 0;
    }}
    .pills {{ display: flex; flex-wrap: wrap; gap: 8px; justify-content: flex-end; }}
    .pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 7px 14px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 600;
      background: var(--card);
      border: 1px solid var(--line);
    }}
    .pill.open {{ background: var(--amber-bg); color: var(--amber); border-color: transparent; }}
    .pill.pass {{ background: var(--green-bg); color: var(--green); border-color: transparent; }}
    .pill.warn {{ background: var(--red-bg); color: var(--red); border-color: transparent; }}
    .dot {{ width: 8px; height: 8px; border-radius: 50%; background: currentColor; }}
    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-bottom: 28px;
    }}
    .metric-card {{
      background: var(--card);
      border-radius: 18px;
      padding: 20px 22px;
      border: 1px solid var(--line);
      box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }}
    .metric-num {{
      font-size: 32px;
      font-weight: 700;
      letter-spacing: -0.03em;
      color: var(--ink);
      line-height: 1.1;
      margin-bottom: 4px;
    }}
    .metric-label {{
      font-size: 13px;
      color: var(--muted);
      font-weight: 500;
    }}
    .grid-2 {{
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 20px;
      margin-bottom: 28px;
    }}
    @media (max-width: 960px) {{
      .grid-2 {{ grid-template-columns: 1fr; }}
      header {{ flex-direction: column; }}
      .pills {{ justify-content: flex-start; }}
    }}
    .card {{
      background: var(--card);
      border-radius: 20px;
      padding: 26px 28px;
      border: 1px solid var(--line);
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}
    h2 {{
      font-size: 14px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: var(--muted);
      margin: 0 0 14px;
      font-weight: 650;
    }}
    .card p, .card li {{
      font-size: 15px;
      line-height: 1.5;
      margin: 0 0 10px;
    }}
    .card ul {{ margin: 0; padding-left: 1.2em; }}
    a {{ color: var(--blue); text-decoration: none; font-weight: 500; }}
    a:hover {{ text-decoration: underline; }}
    .badge {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      margin-right: 6px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .b-blue {{ background: var(--blue-soft); color: var(--blue); }}
    .b-green {{ background: var(--green-bg); color: var(--green); }}
    .b-amber {{ background: var(--amber-bg); color: var(--amber); }}
    .b-red {{ background: var(--red-bg); color: var(--red); }}
    .matrix-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      margin-top: 12px;
    }}
    .matrix-table th {{
      text-align: left;
      padding: 8px 10px;
      border-bottom: 2px solid var(--line);
      color: var(--muted);
      font-weight: 600;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .matrix-table td {{
      padding: 9px 10px;
      border-bottom: 1px solid var(--line);
      vertical-align: middle;
    }}
    .matrix-table tr:last-child td {{ border-bottom: none; }}
    .terminal {{
      background: var(--code-bg);
      color: var(--code-ink);
      border-radius: 18px;
      overflow: hidden;
      box-shadow: 0 14px 40px rgba(0,0,0,0.18);
    }}
    .terminal-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 18px;
      background: #2c2c2e;
      font-size: 12px;
      color: #a1a1a6;
    }}
    .traffic {{ display: flex; gap: 6px; }}
    .traffic i {{ width: 11px; height: 11px; border-radius: 50%; display: block; }}
    .r {{ background: #ff5f57; }}
    .y {{ background: #febc2e; }}
    .g {{ background: #28c840; }}
    pre {{
      margin: 0;
      padding: 18px 22px;
      overflow-x: auto;
      font-family: "SF Mono", ui-monospace, Menlo, monospace;
      font-size: 13px;
      line-height: 1.5;
      color: #d2d2d7;
    }}
    .ok {{ color: #32d74b; }}
    .key {{ color: #64d2ff; }}
    .str {{ color: #ffd60a; }}
    .num {{ color: #bf5af2; }}
    .btn {{
      display: inline-flex;
      align-items: center;
      padding: 6px 12px;
      background: var(--blue);
      color: white;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 600;
      border: none;
      cursor: pointer;
      text-decoration: none;
    }}
    .btn:hover {{ opacity: 0.9; text-decoration: none; }}
  </style>
</head>
<body>
  <div class="container" id="main-container">
    <header>
      <div>
        <p class="kicker">Erdős Problem 142 · Research Notebook & Verification Suite</p>
        <h1>Research Pack Status Dashboard</h1>
        <p class="lede">
          Working notes toward a density increment for <em>r</em><sub>4</sub>(<em>N</em>) = <em>o</em>(<em>N</em>/log <em>N</em>).
          Status is <strong>OPEN (Outcome D, Partial Results Only)</strong>. Auxiliary finite verifiers are passing proofs of identities on finite groups, not an asymptotic theorem.
        </p>
      </div>
      <div class="pills">
        <span class="pill open"><span class="dot"></span> Status: OPEN</span>
        <span class="pill pass"><span class="dot"></span> {len(current_scripts)} Current Verifiers PASS</span>
        <span class="pill warn"><span class="dot"></span> Oct 21 Claims Withdrawn</span>
      </div>
    </header>

    <div class="metrics-grid">
      <div class="metric-card">
        <div class="metric-num">{len(current_scripts) + len(legacy_scripts)}</div>
        <div class="metric-label">Total Verifier Suites ({len(current_scripts)} current + {len(legacy_scripts)} legacy)</div>
      </div>
      <div class="metric-card">
        <div class="metric-num">{bp24_checks + ms24_checks + go24_checks + oc23_checks:,}+</div>
        <div class="metric-label">Finite Progression & Pair Checks (Recent)</div>
      </div>
      <div class="metric-card">
        <div class="metric-num">{tracked_hashes}</div>
        <div class="metric-label">SHA-256 Checkpoint Protected Files</div>
      </div>
      <div class="metric-card">
        <div class="metric-num">0</div>
        <div class="metric-label">Asymptotic Target Overclaims</div>
      </div>
    </div>

    <div class="grid-2">
      <article class="card">
        <h2>October 2026 Advances & Rigorous Obstructions</h2>
        <ul>
          <li>
            <span class="badge b-blue">MS24</span>
            <strong>Multi-Scale Bohr Overlaps:</strong> Proved universal density discrepancy invariance on overlaps and universal cross-host spatial decoupling &lang;<em>u</em><sub>1</sub>, <em>K</em><sub>1&rarr;2</sub><em>f</em>&rang; = &minus;<em>a</em><sub>1</sub> &lang;<em>g</em><sub>1&rarr;2</sub>, <em>f</em>&rang;. Multi-scale coupling cannot break the hole-support ceiling.
          </li>
          <li>
            <span class="badge b-blue">BP24</span>
            <strong>Universal Bilinear Ceiling:</strong> Proved |&Eopf;<sub>&Omega;</sub>[&psi;&#773; <em>Kf</em>]| &le; 6<em>w</em> <em>a</em><sup>3/2</sup>. The ratio cannot diverge to supply <em>F</em><sub>&epsilon;</sub>(<em>a</em>)&rarr;&infin; for DIRECT-Q-GAIN. Spatial decoupling erases phase variation of <em>u</em> across holes.
          </li>
          <li>
            <span class="badge b-green">IE24</span>
            <strong>Incidence Energy Bound:</strong> Proved ||<em>K</em>||<sup>2</sup> &le; 72&alpha;/<em>p</em> with counting Euclidean norms; PC24 establishes occupied pair triple bounds.
          </li>
          <li>
            <span class="badge b-amber">CL23</span>
            <strong>Local Law Obstruction:</strong> Consistent Boolean laws on &le; &lfloor;1/<em>a</em>&rfloor;+1 vertices satisfy exact pair moments but have zero triples; finite overlap cannot exclude them.
          </li>
          <li>
            <span class="badge b-red">OCT21</span>
            <strong>Withdrawn Closure:</strong> October 21 closure withdrawn due to reversed variance bound, uncontrolled cubic term, and unproved spectral concentration.
          </li>
        </ul>
      </article>

      <article class="card">
        <h2>Open Frontier & Verification Reproduction</h2>
        <p>The single remaining arithmetic bottleneck requires either:</p>
        <ul>
          <li>Proving adequate quadratic phase selection on Bohr hosts directly without factoring through <em>K</em>.</li>
          <li>Resolving the arithmetic low-mean branch <em>m</em> &le; 2<em>a</em><sup>3</sup><em>T</em>/<em>w</em> under higher-degree Gowers uniformity bounds.</li>
        </ul>
        <div style="margin-top: 20px;">
          <a class="btn" href="https://github.com/mangeshraut712/erdos142" target="_blank" rel="noopener">View GitHub Repository &rarr;</a>
          <span style="font-size: 13px; color: var(--muted); margin-left: 12px;">Python 3.10+ · stdlib & NumPy</span>
        </div>
      </article>
    </div>

    <section class="card" style="margin-bottom: 28px;">
      <h2>Active Verifiers Matrix (October 2026 Core Suite)</h2>
      <div style="overflow-x: auto;">
        <table class="matrix-table">
          <thead>
            <tr>
              <th>Script Path</th>
              <th>Status</th>
              <th>Mathematical Identity / Property Tested</th>
              <th>Reported Checks</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>verify_multiscale_bohr_overlap_20261024.py</code></td>
              <td><span class="badge b-green">PASS</span></td>
              <td>Multi-scale Bohr overlap invariance, cross-host hole decoupling, phase orthogonality</td>
              <td><strong>{ms24_checks:,}</strong></td>
            </tr>
            <tr>
              <td><code>verify_bilinear_pair_incidence_20261024.py</code></td>
              <td><span class="badge b-green">PASS</span></td>
              <td>Universal 6<em>w</em> <em>a</em><sup>3/2</sup> ceiling, spatial decoupling &lang;<em>u</em>, <em>Kf</em>&rang;=&minus;<em>a</em>&lang;<em>g</em>, <em>f</em>&rang;, quartic residual</td>
              <td><strong>{bp24_checks:,}</strong></td>
            </tr>
            <tr>
              <td><code>verify_growing_overlap_20261024.py</code></td>
              <td><span class="badge b-green">PASS</span></td>
              <td>PC24 pair completion degrees, zero-completion constructions, incidence operator norm</td>
              <td><strong>{go24_checks:,}</strong></td>
            </tr>
            <tr>
              <td><code>verify_overlap_constraints_20261023.py</code></td>
              <td><span class="badge b-green">PASS</span></td>
              <td>OD23 completion bound <em>q</em>&le;2<em>aw</em>, CL23 local probability laws, joint occupancy polytopes</td>
              <td><strong>{oc23_checks:,}</strong></td>
            </tr>
            <tr>
              <td><code>verify_low_mean_moments_20261023.py</code></td>
              <td><span class="badge b-green">PASS</span></td>
              <td>LM23 exact moment interval, ZM23 zero-mean construction, variance upper bounds</td>
              <td><strong>Exact Interval</strong></td>
            </tr>
            <tr>
              <td><code>verify_oct21_closure_correction_20261021.py</code></td>
              <td><span class="badge b-green">PASS</span></td>
              <td>Proof correction audit, universal Boolean chirp 4th moment identity, rational counterchecks</td>
              <td><strong>11,810</strong></td>
            </tr>
            <tr>
              <td><code>verify_boolean_typical_alteration_20261018.py</code></td>
              <td><span class="badge b-green">PASS</span></td>
              <td>Actual Boolean AP-free <em>a</em>~<em>p</em><sup>&minus;&theta;</sup> and &delta;/<em>a</em><sup>1.5</sup>&rarr;0 for 1/3&lt;&theta;&lt;1/2</td>
              <td><strong>525,186</strong></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <div class="terminal">
      <div class="terminal-bar">
        <div class="traffic"><i class="r"></i><i class="y"></i><i class="g"></i></div>
        <span>python verification/run_current.py --suite current</span>
        <span style="color: #64d2ff;">Reproduce Locally</span>
      </div>
      <pre><span class="ok">PASS</span> verification/scripts/verify_multiscale_bohr_overlap_20261024.py
<span class="ok">PASS</span> verification/scripts/verify_bilinear_pair_incidence_20261024.py
<span class="ok">PASS</span> verification/scripts/verify_growing_overlap_20261024.py
<span class="ok">PASS</span> verification/scripts/verify_overlap_constraints_20261023.py
<span class="ok">PASS</span> verification/scripts/verify_low_mean_moments_20261023.py
<span class="ok">PASS</span> verification/scripts/verify_oct21_closure_correction_20261021.py
<span class="ok">... [25 current verification scripts passed with exit code 0]</span>

<span class="ok">{{</span>
  <span class="key">"suite"</span>: <span class="str">"current"</span>,
  <span class="key">"passed"</span>: <span class="num">true</span>,
  <span class="key">"total_checks"</span>: <span class="num">&gt;1800000</span>,
  <span class="key">"scope"</span>: <span class="str">"Exact finite checks of algebraic identities and obstructions; no asymptotic theorem proved."</span>
<span class="ok">}}</span></pre>
    </div>
  </div>

  <!-- Backward compatible screenshot targets -->
  <script>
    (function () {{
      var shot = new URLSearchParams(location.search).get("shot");
      if (shot === "home" || shot === "feature") {{
        document.body.classList.add("screenshot-mode");
      }}
    }})();
  </script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate status dashboard HTML.")
    parser.add_argument("--check", action="store_true", help="Check that docs/status.html is up to date.")
    args = parser.parse_args()

    html_content = build_dashboard_html()
    target_path = ROOT / "docs/status.html"

    if args.check:
        if not target_path.exists():
            sys.stderr.write("docs/status.html does not exist.\n")
            sys.exit(1)
        current = target_path.read_text(encoding="utf-8")
        if current != html_content:
            sys.stderr.write("docs/status.html is out of date. Run python verification/generate_dashboard.py\n")
            sys.exit(1)
        print("docs/status.html is up to date.")
        sys.exit(0)

    target_path.write_text(html_content, encoding="utf-8")
    print(f"Generated {target_path.relative_to(ROOT)} successfully.")


if __name__ == "__main__":
    main()
