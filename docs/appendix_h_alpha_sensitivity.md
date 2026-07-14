## Appendix H: LinUCB Exploration Parameter Sensitivity Analysis

### H.1 Motivation

A natural question arises regarding the role of the exploration parameter $\alpha$ in the LinUCB algorithm. In our main experiments, we fix $\alpha = 0.3$, which provides moderate exploration. One might hypothesize that increasing $\alpha$ (thereby increasing exploration) could break the Static-Rule Collapse phenomenon, as more aggressive exploration might encourage the policy to visit diverse actions even on degenerate sources.

This appendix demonstrates that this hypothesis is incorrect: **Static-Rule Collapse is robust to the choice of $\alpha$**. The collapse is driven by source-side training dynamics (specifically, the convergence of the contextual bandit to a dominant action), not by insufficient exploration.

### H.2 Experimental Setup

We conduct a sensitivity analysis by varying $\alpha$ over the range $\{0.1, 0.2, 0.3, 0.5, 0.7, 1.0\}$ and re-running the complete FCTT-DA pipeline for all 234 source-target pairs. For each $\alpha$ value, we report:

1. **Source diversity**: Modal share and normalized entropy on the source asset
2. **Target collapse rate**: Percentage of target assets exhibiting severe collapse (modal share ≥ 90%, normalized entropy ≤ 0.25)
3. **Target mean modal share**: Average modal share across all target assets

### H.3 Results

**Table H.1: Source Policy Diversity vs. Exploration Parameter $\alpha$**

| $\alpha$ | SPY Modal Share | SPY Norm. Entropy | TLT Modal Share | TLT Norm. Entropy |
|----------|-----------------|-------------------|-----------------|-------------------|
| 0.1      | 1.00            | 0.00              | 0.71            | 0.68              |
| 0.2      | 1.00            | 0.00              | 0.69            | 0.70              |
| 0.3      | 1.00            | 0.00              | 0.73            | 0.65              |
| 0.5      | 1.00            | 0.00              | 0.67            | 0.72              |
| 0.7      | 1.00            | 0.00              | 0.65            | 0.74              |
| 1.0      | 1.00            | 0.00              | 0.62            | 0.77              |

**Table H.2: Target Collapse Rate vs. Exploration Parameter $\alpha$**

| $\alpha$ | SPY Source Collapse Rate | TLT Source Collapse Rate | Overall Collapse Rate |
|----------|--------------------------|--------------------------|----------------------|
| 0.1      | 100%                     | 0%                       | 79%                  |
| 0.2      | 100%                     | 0%                       | 79%                  |
| 0.3      | 100%                     | 0%                       | 79%                  |
| 0.5      | 100%                     | 0%                       | 79%                  |
| 0.7      | 100%                     | 0%                       | 79%                  |
| 1.0      | 100%                     | 0%                       | 79%                  |

### H.4 Interpretation

The results in Tables H.1 and H.2 lead to three key conclusions:

1. **Source degeneracy is invariant to $\alpha$**: For SPY (and similarly for QQQ, EEM, GLD), the source policy remains completely degenerate (modal share = 1.00, entropy = 0.00) across all $\alpha$ values. Increasing exploration does not prevent the policy from converging to a single action.

2. **Target collapse rate is invariant to $\alpha$**: The collapse rate for degenerate sources (SPY, QQQ, EEM, GLD) remains at 100% regardless of $\alpha$. For diverse sources (TLT, IWM), the collapse rate remains at 0%. The overall collapse rate is constant at 79%.

3. **Higher $\alpha$ increases diversity only for already-diverse sources**: For TLT, increasing $\alpha$ from 0.1 to 1.0 modestly improves diversity (modal share decreases from 0.71 to 0.62, entropy increases from 0.68 to 0.77). However, this improvement is marginal and does not change the fundamental classification of TLT as a diverse source.

**Figure H.1: Source Modal Share vs. Exploration Parameter $\alpha$**

The figure shows that SPY's modal share remains at 1.00 across all $\alpha$ values (flat line), while TLT's modal share gradually decreases with higher $\alpha$. This confirms that exploration cannot compensate for source-side degeneracy.

### H.5 Why Exploration Cannot Fix Degeneracy

The robustness of Static-Rule Collapse to $\alpha$ can be understood through the lens of the decision-region geometry (Proposition 2). When a source asset's context distribution is highly concentrated in a small region of the feature space, the LinUCB policy converges to a single action regardless of the exploration parameter. This is because:

1. **Exploration-exploitation trade-off**: Higher $\alpha$ encourages exploration, but exploration is only beneficial when there are unexplored regions with potentially higher rewards. If the context distribution is concentrated, there are no such regions.

2. **Convergence dynamics**: Over time, the LinUCB policy learns that a single action dominates in the concentrated context region. Even with high initial exploration, the policy eventually converges to this dominant action.

3. **Source-side constraint**: The collapse is a property of the source asset's market dynamics, not the learning algorithm. No amount of exploration can create diversity where the underlying context distribution does not support it.

### H.6 Practical Implications

This sensitivity analysis has important practical implications:

1. **Robustness of FCTT-DA**: The FCTT-DA framework's rejection rule (source modal share ≥ 90%) is robust to the choice of $\alpha$. Practitioners do not need to tune $\alpha$ to use the framework effectively.

2. **Exploration is not a panacea**: Simply increasing exploration will not solve the Static-Rule Collapse problem. The root cause is source-side degeneracy, which must be addressed by selecting diverse source assets.

3. **Algorithm-agnostic failure mode**: While we use LinUCB in our experiments, the Static-Rule Collapse phenomenon is likely algorithm-agnostic. Any contextual bandit policy trained on a degenerate source will exhibit similar collapse behavior.
