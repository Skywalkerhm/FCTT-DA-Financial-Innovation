
---

## 补充实验（v4 更新）

### Table 1 (Updated): Source Policy Diversity — 6 Sources

| Source | Asset Class | Modal Share | Norm. Entropy | Effective Actions | Status |
|--------|------------|-------------|---------------|-------------------|--------|
| SPY | Equity | 100.0% | 0.000 | 1.0 | Degenerate |
| QQQ | Equity | 100.0% | 0.000 | 1.0 | Degenerate |
| IWM | Equity | 82.5% | 0.258 | 1.3 | Partially degenerate |
| EEM | Equity | 100.0% | 0.000 | 1.0 | Degenerate |
| TLT | Fixed Income | 44.4% | 0.598 | 1.8 | Diverse |
| GLD | Commodity | 100.0% | 0.000 | 1.0 | Degenerate |

### Table 2 (Updated): Collapse Rate by Source — 6 Sources

| Source | Source Status | Targets | Collapsed | Rate | Target Mean Modal |
|--------|-------------|---------|-----------|------|-------------------|
| SPY | Degenerate | 39 | 39 | 100% | ~93% |
| QQQ | Degenerate | 39 | 39 | 100% | ~99% |
| IWM | Partial | 39 | 0 | 0% | 52.8% |
| EEM | Degenerate | 39 | 39 | 100% | ~100% |
| TLT | Diverse | 39 | 0 | 0% | 73.0% |
| GLD | Degenerate | 39 | 39 | 100% | ~100% |
| **Total** | | **234** | **156** | **67%** | |

### Table 5: Threshold Grid Ablation (TLT Source)

| Grid | Thresholds | Modal Share | Norm. Entropy | Status |
|------|-----------|-------------|---------------|--------|
| 4-class | {0.40, 0.50, 0.60, 0.70} | 71.4% | 0.432 | Partially degenerate |
| 5-class | {0.30, 0.45, 0.55, 0.65, 0.80} | 100.0% | 0.000 | Degenerate |
| **6-class** | **{0.35, 0.45, 0.55, 0.65, 0.75, 1.00}** | **44.4%** | **0.598** | **Diverse** |
| 7-class | {0.30, 0.40, 0.45, 0.55, 0.65, 0.75, 0.85} | 100.0% | 0.000 | Degenerate |

**Key finding:** The threshold grid is a critical design choice. Only the 6-class grid maintains source diversity on TLT. Other grids cause degeneracy even on the same source asset.

### Table 6: Reward Function Comparison (TLT Source → SPY Target)

| Reward | Modal Share | Norm. Entropy | Action Distribution |
|--------|-------------|---------------|---------------------|
| BRAR (complex) | 74.2% | 0.370 | [3.0%, 74.2%, 22.7%, 0%, 0%, 0%] |
| Simple (signal × return) | 74.3% | 0.370 | [3.0%, 74.3%, 22.8%, 0%, 0%, 0%] |

**Finding:** The reward function complexity does not affect collapse behavior. BRAR and simple rewards produce virtually identical results.

### Decision Margin Analysis

| Setting | Mean Margin | Median Margin | Range |
|---------|-------------|---------------|-------|
| TLT source (training) | 0.000018 | 0.000010 | [0.000002, 0.000073] |
| SPY target (from TLT) | 0.000027 | 0.000015 | [0.000000, 0.000148] |

**Finding:** Decision margins are extremely small (≈10⁻⁵), confirming Proposition 2. The LinUCB action scores are nearly identical across actions, making the argmax operation sensitive to small context variations. This explains why:
- Degenerate sources (extreme weights) → large margin → universal collapse
- Diverse sources (balanced weights) → small margin → partial concentration

### Updated Summary (6 Sources, 234 Pairs)

| Metric | Value |
|--------|-------|
| Sources | 6 (SPY, QQQ, IWM, EEM, TLT, GLD) |
| Targets | 39 |
| Total pairs | 234 |
| Degenerate sources | 4/6 (SPY, QQQ, EEM, GLD) |
| Diverse sources | 2/6 (TLT, IWM) |
| Collapse rate (degenerate sources) | 156/156 (100%) |
| Collapse rate (diverse sources) | 0/78 (0%) |
| Overall collapse rate | 156/234 (67%) |
