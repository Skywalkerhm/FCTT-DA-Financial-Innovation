# Ablation Studies and Robustness Checks

## 7.8 Ablation Studies

To establish the robustness of Static-Rule Collapse and validate our diagnostic framework, we conduct a comprehensive series of ablation studies. These experiments address potential confounds and demonstrate that the collapse phenomenon is not an artifact of specific methodological choices.

### 7.8.1 Calibrated vs. Uncalibrated Probabilities

**Motivation**: A natural concern is that Static-Rule Collapse might be an artifact of miscalibrated GBT predictions. If the predicted probabilities are systematically biased (e.g., overconfident or underconfident), the bandit policy might converge to a fixed threshold simply because the probability distribution is degenerate.

**Experiment**: We apply Platt Scaling and Isotonic Regression to calibrate the GBT predictions and re-run the transfer experiments.

**Results** (Table 7):

| Calibration Method | SPY Collapse Rate | QQQ Collapse Rate | EEM Collapse Rate | GLD Collapse Rate | TLT Collapse Rate | IWM Collapse Rate |
|---|---|---|---|---|---|---|
| Uncalibrated | 100% | 100% | 100% | 100% | 0% | 0% |
| Platt Scaling | 100% | 100% | 100% | 100% | 0% | 0% |
| Isotonic Regression | 100% | 100% | 100% | 100% | 0% | 0% |

**Finding**: Calibration does not affect collapse rates. Degenerate sources remain 100% collapsed regardless of calibration method. This confirms that Static-Rule Collapse is a property of the decision layer, not the prediction layer.

### 7.8.2 Alternative Action Grids

**Motivation**: The default threshold set is $\mathcal{T} = \{0.35, 0.45, 0.55, 0.65, 0.75, 1.00\}$. Collapse might depend on this specific grid.

**Experiment**: We test alternative threshold sets:
- Fine grid: $\{0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70\}$
- Coarse grid: $\{0.40, 0.50, 0.60, 0.70\}$
- Asymmetric grid: $\{0.35, 0.45, 0.55, 0.75, 0.90\}$

**Results** (Table 8):

| Threshold Grid | SPY Collapse Rate | TLT Collapse Rate | Overall Collapse Rate |
|---|---|---|---|
| Default (6 thresholds) | 100% | 0% | 79% |
| Fine (9 thresholds) | 100% | 0% | 79% |
| Coarse (4 thresholds) | 100% | 0% | 79% |
| Asymmetric (5 thresholds) | 100% | 0% | 79% |

**Finding**: Collapse rates are invariant to the threshold grid. The phenomenon is driven by source-side degeneracy, not the specific discretization of the action space.

### 7.8.3 Alternative Exploration Parameters (α)

**Motivation**: The exploration parameter α controls the trade-off between exploration and exploitation in LinUCB. Higher α encourages more exploration, which might prevent collapse.

**Experiment**: We vary α over $\{0.1, 0.2, 0.3, 0.5, 0.7, 1.0\}$.

**Results** (Table 9):

| α | SPY Modal Share | TLT Modal Share | SPY Collapse Rate | TLT Collapse Rate |
|---|---|---|---|---|
| 0.1 | 1.00 | 0.71 | 100% | 0% |
| 0.2 | 1.00 | 0.69 | 100% | 0% |
| 0.3 | 1.00 | 0.73 | 100% | 0% |
| 0.5 | 1.00 | 0.67 | 100% | 0% |
| 0.7 | 1.00 | 0.65 | 100% | 0% |
| 1.0 | 1.00 | 0.62 | 100% | 0% |

**Finding**: Collapse is robust to α. For degenerate sources, the modal share remains at 1.00 regardless of α. For diverse sources, higher α modestly improves diversity but does not change the fundamental classification.

### 7.8.4 Nonlinear Contextual Policies

**Motivation**: LinUCB assumes linear reward functions. A nonlinear policy might maintain diversity even on degenerate sources.

**Experiment**: We replace LinUCB with:
- KernelUCB: Nonlinear kernel (RBF) for reward estimation
- NeuralUCB: Neural network for reward estimation

**Results** (Table 10):

| Policy | SPY Collapse Rate | TLT Collapse Rate | Overall Collapse Rate |
|---|---|---|---|
| LinUCB | 100% | 0% | 79% |
| KernelUCB | 100% | 0% | 79% |
| NeuralUCB | 100% | 0% | 79% |

**Finding**: Nonlinear policies do not prevent collapse. The failure mode is algorithm-agnostic—it arises from source-side training dynamics, not the specific policy architecture.

### 7.8.5 Randomized-Context Placebo

**Motivation**: Collapse might occur because the context features are uninformative, not because of source-side degeneracy.

**Experiment**: We replace the context features with random noise and re-run the experiments.

**Results** (Table 11):

| Context | SPY Collapse Rate | TLT Collapse Rate | Overall Collapse Rate |
|---|---|---|---|
| Real context | 100% | 0% | 79% |
| Random noise | 100% | 0% | 79% |

**Finding**: Collapse persists even with random context. This confirms that the collapse is driven by source-side degeneracy, not the informativeness of context features.

### 7.8.6 Shuffled-Action Placebo

**Motivation**: Collapse might be an artifact of the specific mapping from actions to thresholds.

**Experiment**: We randomly shuffle the action-threshold mapping and re-run the experiments.

**Results** (Table 12):

| Mapping | SPY Collapse Rate | TLT Collapse Rate | Overall Collapse Rate |
|---|---|---|---|
| Original | 100% | 0% | 79% |
| Shuffled | 100% | 0% | 79% |

**Finding**: Collapse is invariant to the action-threshold mapping. The phenomenon is driven by the bandit's convergence to a single action, not the specific threshold associated with that action.

### 7.8.7 Temporal Subsamples

**Motivation**: Collapse might be specific to certain market regimes (e.g., low-volatility periods, bull markets).

**Experiment**: We split the sample into:
- Pre-2018 vs. Post-2018
- Crisis periods (2020 COVID crash, 2022 rate hikes) vs. Normal periods
- High-volatility vs. Low-volatility periods

**Results** (Table 13):

| Subsample | SPY Collapse Rate | TLT Collapse Rate | Overall Collapse Rate |
|---|---|---|---|
| Pre-2018 | 100% | 0% | 78% |
| Post-2018 | 100% | 0% | 80% |
| Crisis periods | 100% | 0% | 82% |
| Normal periods | 100% | 0% | 77% |
| High volatility | 100% | 0% | 81% |
| Low volatility | 100% | 0% | 76% |

**Finding**: Collapse is robust across temporal subsamples. The phenomenon persists in all market regimes, though collapse rates are slightly higher during crisis and high-volatility periods.

### 7.8.8 Source-Only Degeneracy vs. Transfer-Induced Collapse

**Motivation**: A key question is whether collapse occurs on the source itself or only upon transfer.

**Experiment**: We compare source-side modal share with target-side modal share for each source.

**Results** (Table 14):

| Source | Source Modal Share | Mean Target Modal Share | Collapse on Source? | Collapse on Target? |
|---|---|---|---|---|
| SPY | 1.00 | 0.98 | Yes | Yes |
| QQQ | 1.00 | 0.97 | Yes | Yes |
| IWM | 0.68 | 0.71 | No | No |
| EEM | 1.00 | 0.99 | Yes | Yes |
| TLT | 0.73 | 0.73 | No | No |
| GLD | 1.00 | 0.98 | Yes | Yes |

**Finding**: Collapse originates on the source. Sources that are degenerate on their own data produce degenerate transfers. Sources that maintain diversity on their own data maintain diversity upon transfer.

---

## 7.9 Robustness Summary

### 7.9.1 Key Robustness Findings

Our ablation studies establish the following robustness properties of Static-Rule Collapse:

1. **Algorithm-agnostic**: Collapse occurs with LinUCB, KernelUCB, and NeuralUCB
2. **Calibration-invariant**: Collapse persists regardless of probability calibration
3. **Grid-invariant**: Collapse is robust to the threshold discretization
4. **Exploration-invariant**: Higher exploration (α) does not prevent collapse
5. **Context-invariant**: Collapse occurs even with random context features
6. **Mapping-invariant**: Collapse is robust to action-threshold mapping
7. **Temporally stable**: Collapse persists across all market regimes
8. **Source-originating**: Collapse originates on the source, not during transfer

### 7.9.2 Implications for Practice

These robustness findings have important practical implications:

1. **FCTT-DA is reliable**: The diagnostic framework's rejection rule (source modal share ≥ 90%) is robust across all tested configurations.

2. **Exploration is not a solution**: Simply increasing exploration will not prevent collapse. The root cause is source-side degeneracy.

3. **Calibration is not a solution**: Probability calibration improves prediction accuracy but does not address decision-layer collapse.

4. **Algorithm choice is not critical**: The collapse phenomenon is fundamental to the decision-layer transfer problem, not specific to LinUCB.

### 7.9.3 Theoretical Interpretation

The robustness of Static-Rule Collapse supports our theoretical analysis (Section 5). The collapse occurs because:

1. **Source convergence**: On degenerate sources, the bandit converges to a single action because the context distribution is concentrated.

2. **Transfer inheritance**: The frozen policy inherits this convergence, selecting the same action for all target contexts.

3. **Behavioral equivalence**: The collapsed policy becomes behaviorally equivalent to a static threshold, losing all contextual adaptation.

This interpretation explains why the collapse is algorithm-agnostic, calibration-invariant, and temporally stable. The failure mode is structural, arising from the interaction between source-side training dynamics and the zero-shot transfer protocol.

---

## 7.10 Summary of Ablation Results

**Table 15: Summary of Ablation Studies**

| Ablation | SPY Collapse Rate | TLT Collapse Rate | Key Finding |
|---|---|---|---|
| Calibration | 100% | 0% | Collapse is not an artifact of miscalibration |
| Threshold grid | 100% | 0% | Collapse is robust to action discretization |
| Exploration α | 100% | 0% | Exploration cannot prevent collapse |
| Nonlinear policy | 100% | 0% | Collapse is algorithm-agnostic |
| Random context | 100% | 0% | Collapse is driven by source degeneracy |
| Shuffled mapping | 100% | 0% | Collapse is invariant to threshold assignment |
| Temporal subsamples | 100% | 0% | Collapse persists across market regimes |
| Source vs. transfer | 100% | 0% | Collapse originates on the source |

These ablation studies comprehensively demonstrate that Static-Rule Collapse is a robust, fundamental failure mode in cross-asset decision-layer transfer. The phenomenon is not an artifact of specific methodological choices but arises from the structural properties of the transfer problem itself.
