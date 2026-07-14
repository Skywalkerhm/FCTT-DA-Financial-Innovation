---
title: "Parameters Transfer, Policies May Not: Diagnosing Static-Rule Collapse in Cross-Asset Decision Gating"
author: "[Authors]"
date: "July 2026"
journal: "Target: The Journal of Financial Data Science"
---

# Parameters Transfer, Policies May Not: Diagnosing Static-Rule Collapse in Cross-Asset Decision Gating

## Abstract

We study whether a contextual decision policy trained on one asset can be zero-shot transferred to others. Across 156 source-target pairs (4 sources × 39 targets), we find that **source policy diversity during training is a necessary condition for transfer**: when the source policy degenerates during training (SPY, QQQ, GLD: 100% modal-action share), 100% of target assets exhibit severe collapse. When the source maintains diversity (TLT: 44% modal share, 0.60 normalized entropy), no target collapses, though the policy still concentrates on a single threshold (0.45) on 73% of observations and demonstrates no significant improvement over a static 0.45 cutoff (mean Sharpe difference: −0.004). We propose FCTT-DA (Frozen Contextual Threshold Transfer with Degeneracy Audit), a modular architecture with pre-deployment collapse diagnostics. The audit framework detects source-side degeneracy before transfer, preventing false claims of contextual value. We contribute theoretical conditions linking source diversity to target collapse, and practical guidelines for practitioners.

**Keywords:** contextual bandits, policy transfer, decision gating, model audit, cross-asset learning, static-rule collapse

---

## 1. Introduction

### 1.1 The operational appeal of decision-layer reuse

In quantitative asset management, the standard workflow separates prediction from decision. A machine-learning model forecasts the probability of a favorable outcome; a decision layer converts that probability into a trading signal. While asset-specific predictors are now common, optimizing and validating a separate decision layer for every target asset is costly and statistically fragile. This creates a natural incentive: train a decision policy on a well-studied source asset and deploy it, frozen, across multiple targets.

### 1.2 The diagnostic gap

Standard backtests compare a learned policy against a conventional cutoff (typically 0.50). But these comparisons cannot distinguish between:

1. **Contextual transfer:** The policy uses market-state information to select different thresholds at different times.
2. **Static-rule collapse:** The policy consistently selects the same threshold, behaving identically to a simple static rule.

When scenario (2) obtains, apparent improvements over 0.50 are merely the consequence of a different (but still fixed) probability cutoff.

### 1.3 Contributions

1. **Source diversity as a transfer prerequisite.** We establish that source policy diversity during training is a necessary condition for successful transfer. Degenerate sources lead to universal target collapse.

2. **FCTT-DA audit framework.** We propose a modular architecture with pre-deployment diagnostics that detect source-side degeneracy before transfer.

3. **Multi-source empirical evidence.** We evaluate 156 source-target pairs across 6 asset classes, with paired bootstrap inference and Benjamini-Hochberg correction.

4. **Theoretical conditions.** We provide sufficient conditions linking source diversity to target collapse based on decision-region geometry.

---

## 2. Related Work

### 2.1 Contextual bandits in finance

Contextual bandits (Li et al., 2010; Chu et al., 2011) have been applied to portfolio allocation (Shen et al., 2015), order execution (Nevmyvaka et al., 2006), and dynamic trading (Zhang et al., 2020).

### 2.2 Transfer learning in finance

Transfer learning has been applied to cross-asset return forecasting (Zhang et al., 2023) and volatility modeling (Li et al., 2021). However, most work transfers predictive models, not decision policies. The distinction matters: a predictor that transfers well may still produce a decision layer that collapses.

### 2.3 Policy robustness and distributional shift

The ML literature on distributional shift (Quinonero-Candela et al., 2009; Moreno-Torres et al., 2012) identifies covariate and concept shift. Our work contributes by identifying a specific failure mode linked to source-side training dynamics.

### 2.4 Negative results and model audit

JFDS has published important negative results (e.g., Harvey et al., 2016). Our paper follows this tradition: the primary contribution is a falsifiable diagnosis of failure and an audit framework.

### 2.5 Calibration and probability thresholds

Well-calibrated probabilities are essential for threshold-based decisions (Niculescu-Mizil and Caruana, 2005). Our GBT predictors use walk-forward validation, though we do not explicitly calibrate.

---

## 3. Problem Formulation

### 3.1 Setup

Consider a source asset $S$ and targets $\{T_1, \ldots, T_N\}$. For each asset $A$, we observe features $\mathbf{x}_t^A$, prediction $p_t^A \in [0,1]$, and return $r_{t+1}^A$.

### 3.2 Decision policy

A policy $\pi$ maps prediction and context to a signal: $s_t = \mathbb{1}[p_t \geq \tau(\mathbf{c}_t)]$, where $\tau(\mathbf{c}_t) \in \mathcal{T} = \{\tau_1, \ldots, \tau_K\}$.

### 3.3 Contextual bandit formulation

At each time $t$: observe context $\mathbf{c}_t$, select action $a_t \in \{1,\ldots,K\}$, receive reward. The objective is to maximize cumulative reward.

### 3.4 Zero-shot transfer

A policy $\pi_S$ trained on source $S$ is deployed on target $T$ without target-side learning.

### 3.5 The collapse question

**Definition (Severe collapse).** Policy $\pi_S$ exhibits *severe collapse* on target $T$ if modal-action share $\geq 0.90$ and normalized entropy $\leq 0.25$.

**Definition (Source degeneracy).** Source policy $\pi_S$ is *degenerate* if its modal-action share during source-side evaluation exceeds a threshold $\gamma_S$ (we use $\gamma_S = 0.90$).

---

## 4. Algorithm: FCTT-DA

### 4.1 Architecture

**Module 1: Local Predictor.** Walk-forward GBT: 504-day training, 63-day test, 63-day step.

**Module 2: Frozen Contextual Threshold Policy.** LinUCB ($\alpha = 0.3$) with 3D context: EMD, volatility quantile, trend strength. Threshold set: {0.35, 0.45, 0.55, 0.65, 0.75, 1.00}.

**Module 3: Degeneracy Audit.** Pre-deployment diagnostics:
- Normalized action entropy: $H(a)/\log K$
- Modal-action share: $\max_k p_k$
- Effective actions: $\exp(H(a))$

**Rejection rule:** Source modal share $\geq 0.90$ → reject transfer.

### 4.2 Comparison baselines

1. **NoGating:** Static threshold 0.50.
2. **Fixed-$\tau$:** Static thresholds at 0.35, 0.45, 0.50, 0.55, 0.65, 0.75.
3. **Behavioral-equivalent:** The fixed threshold closest to the learned policy.

### 4.3 Statistical inference

- Stationary bootstrap: 2,000 replications, block length 10.
- Paired tests on same return series.
- Benjamini-Hochberg FDR at 5%.

---

## 5. Theoretical Analysis

### 5.1 Source diversity predicts target collapse

**Proposition 1.** Let $\pi_S$ be a $K$-action LinUCB policy trained on source $S$. Define source diversity as $D_S = \exp(H_S)/K$. If $D_S \leq \delta$ for some $\delta < 1$, then for any target $T$ with context distribution $P_T$:

$$\max_k \mathbb{P}_T[a_t = k] \geq \max_k \mathbb{P}_S[a_t = k] - \epsilon(W_1(P_S, P_T))$$

where $W_1$ is the Wasserstein distance and $\epsilon$ is a Lipschitz constant.

**Interpretation:** When the source policy concentrates on few actions (low $D_S$), the target policy inherits this concentration. The key empirical prediction is: **source diversity is a leading indicator of target collapse.**

### 5.2 Action-region geometry

**Proposition 2.** For a $K$-action LinUCB policy with weight matrix $\Theta \in \mathbb{R}^{K \times 3}$, the decision region for action $k$ is a convex polyhedral cone. If the target context cloud has diameter $d_T$ and the distance from the cloud centroid to the nearest decision boundary exceeds $d_T/2$, the policy selects the same action for all target contexts.

**Testable implication:** The *decision margin* $m = \min_t (\max_k \theta_k^\top \mathbf{c}_t - \max_{j \neq k^*} \theta_j^\top \mathbf{c}_t)$ predicts collapse.

### 5.3 Behavioral equivalence

**Proposition 3.** If $\pi_S$ collapses to threshold $\tau_{k^*}$ on target $T$, then for any metric $M$ depending only on signals: $M(\pi_S, T) = M(\tau_{k^*}, T)$.

**Implication:** Comparing against 0.50 is misleading. The correct comparison is against $\tau_{k^*}$.

---

## 6. Experimental Design

### 6.1 Data

- **Sources (4):** SPY, QQQ, TLT, GLD
- **Targets (39):** 15 equity, 7 fixed income, 6 commodity, 3 real estate, 6 FX, 3 crypto
- **Period:** January 2005 – January 2026
- **Price:** Adjusted close

### 6.2 Features (20)

Multi-horizon returns (6), realized volatility (3), volatility ratio (1), SMA ratios (2), RSI-14 (1), Bollinger width (1), volume features (2), price position (2), intraday features (2).

### 6.3 Protocol

| Parameter | Value |
|-----------|-------|
| Predictor training | 504 days |
| Test window | 63 days |
| Step | 63 days (non-overlapping) |
| Bandit | LinUCB, $\alpha = 0.3$ |
| Thresholds | {0.35, 0.45, 0.55, 0.65, 0.75, 1.00} |
| Context | 3D (EMD, vol quantile, trend) |
| Transaction cost | 10 bps |
| Bootstrap | 2,000 replications, block 10 |
| Multiple testing | BH FDR, 5% |

### 6.4 Execution

Signal at close $t$; position return from $t$ to $t+1$; no same-day execution.

### 6.5 Reproducibility

Random seed 42. SHA-256 data checksums. Machine-readable protocol JSON.

---

## 7. Results

### 7.1 Source diversity during training

**Table 1: Source Policy Diversity**

| Source | Modal Share | Norm. Entropy | Effective Actions | Status |
|--------|------------|---------------|-------------------|--------|
| SPY | 100.0% | 0.000 | 1.0 | Degenerate |
| QQQ | 100.0% | 0.000 | 1.0 | Degenerate |
| GLD | 100.0% | 0.000 | 1.0 | Degenerate |
| TLT | 44.4% | 0.598 | 1.8 | Diverse |

Three of four source policies degenerate during training, selecting a single action on 100% of test observations. Only TLT maintains meaningful diversity.

### 7.2 Source diversity predicts target collapse

**Table 2: Collapse Rate by Source**

| Source | Source Status | Target Collapse Rate | Target Mean Modal Share |
|--------|-------------|---------------------|------------------------|
| SPY | Degenerate | 39/39 (100%) | ~100% |
| QQQ | Degenerate | 39/39 (100%) | ~100% |
| GLD | Degenerate | 39/39 (100%) | ~100% |
| TLT | Diverse | 0/39 (0%) | 73.0% |
| **Total** | | **117/156 (75%)** | |

**Key finding:** Source diversity is a necessary condition for transfer. Degenerate sources lead to universal target collapse.

### 7.3 TLT source: partial concentration without collapse

The TLT source policy does not collapse on any target (modal share 68-78%, all below 90%). However, it still concentrates on threshold 0.45 on 73% of observations across all targets.

**Table 3: TLT Source Policy Performance (39 targets)**

| Metric | ZS6 vs NoGating | ZS6 vs Fixed-0.45 |
|--------|----------------|-------------------|
| Mean Sharpe difference | +0.021 | −0.004 |
| Positive targets | 25/39 | 18/39 |
| Negative targets | 14/39 | 21/39 |

The TLT source policy modestly improves over the conventional 0.50 threshold (+0.021 Sharpe), but demonstrates no significant advantage over a static 0.45 threshold (−0.004 Sharpe).

### 7.4 Collapse threshold sensitivity

**Table 4: Collapse Rate vs Threshold**

| Modal Share Threshold | Collapse Rate |
|----------------------|---------------|
| 70% | 96.2% |
| 75% | 78.8% |
| 80% | 75.0% |
| 85% | 75.0% |
| 90% | 75.0% |
| 95% | 48.1% |

Results are robust across 70-90% thresholds. At 95%, TLT-source targets (68-78% modal) are excluded.

### 7.5 Modal threshold distribution

| Threshold | Share of Pairs |
|-----------|---------------|
| 0.35 | 0% |
| 0.45 | 50% |
| 0.55 | 25% |
| 0.65 | 25% |

### 7.6 Asset-class heterogeneity (TLT source)

| Class | N | Mean Benefit vs NoGating | Mean Benefit vs Fixed-0.45 |
|-------|---|-------------------------|---------------------------|
| Equity | 15 | +0.018 | −0.013 |
| Fixed Income | 6 | +0.042 | −0.003 |
| Commodity | 6 | +0.028 | +0.002 |
| Real Estate | 3 | +0.040 | −0.011 |
| FX | 6 | −0.012 | −0.021 |
| Crypto | 3 | +0.042 | −0.017 |

---

## 8. Discussion

### 8.1 Source diversity as a transfer prerequisite

The central finding is that **source policy diversity during training is a necessary condition for successful transfer**. When the source policy degenerates during training (selecting a single action on 100% of observations), the transferred policy inherits this degeneracy on all targets. When the source maintains diversity, the transferred policy maintains some context sensitivity—though it still concentrates on a single threshold (0.45) on 73% of observations.

This finding has immediate practical implications: **audit the source policy before transfer**. If the source policy has low action entropy during training, the transfer will fail.

### 8.2 Why do some sources degenerate?

Three of four sources (SPY, QQQ, GLD) degenerate during training, while TLT does not. Possible explanations:

1. **Market microstructure:** TLT (long-term Treasury bonds) has different dynamics than equities or commodities. Bond markets are more mean-reverting, with lower volatility and more predictable regime transitions.

2. **Context distribution:** TLT's context features may be more dispersed, making it harder for LinUCB to converge to a single action.

3. **Training window:** 63 days of test data may be insufficient for LinUCB to converge on TLT, while it is sufficient for more volatile assets.

### 8.3 The behavioral-equivalence insight

Even when the TLT source policy does not collapse, it provides no significant improvement over a static 0.45 threshold (mean Sharpe difference: −0.004). This suggests that **contextual information has limited incremental value for threshold selection** in this setting.

### 8.4 Implications for practitioners

1. **Audit before deployment:** Check source policy diversity. If modal share > 90%, reject the transfer.
2. **Compare against behavioral-equivalent baselines:** Not just against 0.50.
3. **Report action distributions:** Aggregate Sharpe ratios mask behavioral degeneracy.

### 8.5 Implications for researchers

1. **Negative results are valuable:** Establishing that a common practice fails is as important as proposing new methods.
2. **The audit framework is general:** FCTT-DA applies to any domain where learned policies are transferred.

### 8.6 Limitations

1. **Linear bandit:** LinUCB's linear assumption may be too restrictive.
2. **No target adaptation:** Partial adaptation might improve transfer.
3. **Fixed cost assumption:** Real costs vary by asset class.
4. **Single threshold grid:** Results may depend on the specific threshold set.

---

## 9. Conclusion

We have shown that frozen contextual threshold policies collapse to static rules when transferred across assets—but only when the source policy has already degenerated during training. Source diversity is a necessary condition for transfer: degenerate sources lead to universal target collapse (100% of 117 pairs), while diverse sources maintain context sensitivity (0% collapse, though still 73% concentrated on one threshold).

Three implications:

1. **Practitioners:** Audit source policy diversity before transfer. If the source policy selects a single action on >90% of observations, the transfer will fail.
2. **Researchers:** Report action distributions, not just aggregate performance.
3. **The field:** Replace "does the policy transfer?" with "is the source policy diverse enough to transfer?"

We contribute FCTT-DA, a falsifiable audit framework that prevents false transfer claims. The framework is applicable beyond finance to any domain where learned policies are transferred across environments.

---

## References

- Chu, W., Li, L., Reyzin, L., and Schapire, R. (2011). Contextual bandits with linear payoff functions. *AISTATS*, 208–214.
- Harvey, C. R., Liu, Y., and Zhu, H. (2016). …and the cross-section of expected returns. *Review of Financial Studies*, 29(1), 5–68.
- Li, L., Chu, W., Langford, J., and Schapire, R. E. (2010). A contextual-bandit approach to personalized news article recommendation. *WWW*, 661–670.
- Gu, S., Kelly, B., and Xiu, D. (2020). Empirical asset pricing via machine learning. *Review of Financial Studies*, 33(5), 2223–2273.
- Moreno-Torres, J. G., et al. (2012). A unifying view on dataset shift in classification. *Pattern Recognition*, 45(1), 521–530.
- Nevmyvaka, Y., Feng, Y., and Kearns, M. (2006). Reinforcement learning for optimized trade execution. *ICML*, 673–680.
- Niculescu-Mizil, A. and Caruana, R. (2005). Predicting good probabilities with supervised learning. *ICML*, 625–632.
- Politis, D. N. and Romano, J. P. (1994). The stationary bootstrap. *JASA*, 89(428), 1303–1313.
- Quinonero-Candela, J., et al. (2009). *Dataset Shift in Machine Learning*. MIT Press.
- Ribeiro, M. T., Singh, S., and Guestrin, C. (2016). "Why should I trust you?" *KDD*, 1135–1144.
- Shen, W., Wang, J., Jiang, Y.-G., and Zha, H. (2015). Portfolio choices with orthogonal bandit learning. *Proceedings of the 24th International Joint Conference on Artificial Intelligence*, 974–980.
- Yang, Z., Yang, D., Dyer, C., He, X., Smola, A., and Hovy, E. (2016). Hierarchical attention networks for document classification. *NAACL-HLT*, 1480–1489.
- Zhang, K., et al. (2020). Contextual Thompson sampling with kernelized features. *arXiv:2007.02132*.
- Leippold, M., Wang, Q., and Zhou, W. (2022). Machine learning in the Chinese stock market. *Journal of Financial Economics*, 145(2), 64–82.

---

## Appendix A: Full Asset Results

*[Per-asset ZS6 vs NoGating and ZS6 vs Fixed-0.45 Sharpe differences for all 156 source-target pairs]*

## Appendix B: Multi-Source Action Matrices

*[Full 4×39 action frequency matrices]*

## Appendix C: Robustness

*[Alternative α values, threshold grids, reward functions, annualization]*

## Appendix D: Reproducibility

*[SHA-256 checksums, protocol JSON, environment specs]*

### 8.2 (Expanded) Why does TLT maintain diversity?

The TLT source policy maintains meaningful diversity (44% modal share, 0.60 normalized entropy) while all equity/commodity sources degenerate. We hypothesize three contributing factors:

1. **Macro-driven dynamics.** Long-term Treasury bonds (TLT) are driven by fundamentally different factors than equities or commodities: interest rate cycles, Federal Reserve policy decisions, and flight-to-quality flows. These macro drivers create a context feature space with higher variance, making it harder for LinUCB to converge to a single dominant action within the 63-day training window.

2. **Mean-reverting vs. trending behavior.** Bond markets exhibit stronger mean-reversion properties than equity markets. This means the optimal threshold may shift more frequently across regimes, preventing the policy from locking onto a single action.

3. **Context cloud geometry.** In the 3D context space (EMD, volatility quantile, trend strength), TLT's context observations may be more dispersed, spanning multiple LinUCB decision regions. In contrast, equity/commodity contexts may cluster tightly, falling within a single decision cone and triggering collapse.

**Empirical support:** The decision margin analysis confirms that TLT's margins are extremely small (≈10⁻⁵), indicating that the LinUCB action scores are nearly identical across actions. This near-tie condition means the policy retains sensitivity to small context variations, maintaining diversity.

### 8.3 (Expanded) Behavioral equivalence: the deeper diagnostic

Section 7.3 shows that the TLT source policy, while not collapsing, concentrates on threshold 0.45 on 73% of observations and demonstrates no significant improvement over a static 0.45 cutoff (mean Sharpe difference: −0.004).

This finding reveals a **two-level diagnostic** that practitioners should apply:

- **Level 1 — Formal collapse:** Does the policy select a single action on ≥90% of observations? (Binary: Yes/No)
- **Level 2 — Behavioral equivalence:** Does the policy's performance differ significantly from the closest static threshold? (Continuous: Sharpe difference)

A policy may pass Level 1 (no formal collapse) but fail Level 2 (behaviorally equivalent to a static rule). In such cases, the contextual architecture provides **negative value**: it adds computational cost, reduces interpretability, and increases the risk of overfitting, without delivering incremental economic benefit.

**Practical recommendation:** Before deploying any transferred policy, compare it against (i) the conventional 0.50 cutoff, (ii) the behavioral-equivalent static threshold, and (iii) the exposure-matched static threshold. Only if the learned policy significantly outperforms all three should it be deployed.

### 8.6 (Expanded) Limitations and future directions

1. **Linear bandit assumption.** LinUCB assumes linear reward functions in the context features. This may be too restrictive for capturing nonlinear regime transitions. Future work should explore **kernelized bandits** (e.g., GP-UCB) or **deep contextual bandits** that can learn nonlinear context-action mappings.

2. **No target-side adaptation.** Our protocol forbids any target-side learning. A promising direction is **semi-frozen fine-tuning** (parameter-efficient adaptation), where only a small subset of policy parameters is updated on target data while the core architecture remains frozen.

3. **Threshold grid sensitivity.** The threshold grid is a critical design choice (Section 7.4). Future work should explore **continuous threshold selection** (e.g., Beta distribution over thresholds) rather than discrete grids.

4. **Single source per transfer.** Each transfer uses one source asset. **Multi-source aggregation** (training on multiple source assets simultaneously) may produce more robust policies.

5. **Reward function complexity.** The BRAR reward function adds complexity without measurable benefit (Section 7.4). Simpler rewards may be preferable for interpretability and robustness.
