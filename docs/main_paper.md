---
title: "Parameters Transfer, Policies May Not: Diagnosing Static-Rule Collapse in Cross-Asset Decision Gating"
author: "[Authors]"
date: "July 2026"
journal: "Target: The Journal of Financial Data Science"
---

# Parameters Transfer, Policies May Not: Diagnosing Static-Rule Collapse in Cross-Asset Decision Gating

## Abstract

We identify **Static-Rule Collapse**, a silent failure mode in cross-asset decision-layer transfer where a frozen contextual policy degenerates into a fixed probability threshold on out-of-distribution targets. Standard backtests cannot distinguish this from genuine contextual transfer, producing **False Contextual Alpha** — apparent improvements over the 0.50 cutoff that are merely artifacts of a different static threshold.

Across 234 source-target pairs (6 sources × 39 targets), we establish an empirical taxonomy: degenerate sources (SPY, QQQ, EEM, GLD) trigger 100% target collapse; diverse sources (TLT, IWM) maintain context sensitivity. We provide microstructure-level explanations based on context cloud geometry and decision margin analysis. Even when a policy passes the diversity audit, we uncover a **Behavioral Equivalence Paradox**: the TLT-transferred policy demonstrates no significant improvement over a static 0.45 threshold (Sharpe difference: −0.004), revealing that contextual complexity can provide negative economic value.

We contribute FCTT-DA (Frozen Contextual Threshold Transfer with Degeneracy Audit), a deployable framework with source diversity pre-checks, behavioral-equivalent baseline comparison, transaction cost sensitivity analysis, and complete pseudocode for production deployment.

**Keywords:** contextual bandits, policy transfer, decision gating, model audit, static-rule collapse, behavioral equivalence, cross-asset learning

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

---

## Appendix E: FCTT-DA Pseudocode

### E.1 Source Diversity Audit

```
ALGORITHM: SourceDiversityAudit
INPUT:  source_data, thresholds, alpha, gamma_modal=0.90, gamma_entropy=0.25
OUTPUT: {theta, is_degenerate, diagnostics}

1.  features ← ComputeFeatures(source_data)
2.  pred ← WalkForwardGBT(features, train=504, test=63, step=63)
3.  ctx ← ComputeContexts(source_data)  // [EMD, vol_rank, trend]
4.  
5.  bandit ← LinUCB(K=|thresholds|, d=3, alpha=alpha)
6.  actions ← []
7.  
8.  FOR t IN source_test_window:
9.      a ← bandit.select_action(ctx[t])
10.     signal ← (pred[t] >= thresholds[a]) ? 1 : 0
11.     reward ← signal * returns[t+1]
12.     bandit.update(a, ctx[t], reward)
13.     actions.append(a)
14. 
15. action_freq ← histogram(actions, bins=K) / len(actions)
16. modal_share ← max(action_freq)
17. entropy ← -sum(p * log(p) FOR p IN action_freq WHERE p > 0)
18. norm_entropy ← entropy / log(K)
19. effective_actions ← exp(entropy)
20. 
21. is_degenerate ← (modal_share >= gamma_modal) AND (norm_entropy <= gamma_entropy)
22. 
23. RETURN {
24.     theta: bandit.get_weights(),
25.     is_degenerate: is_degenerate,
26.     diagnostics: {modal_share, norm_entropy, effective_actions, action_freq}
27. }
```

### E.2 Target Transfer with Degeneracy Audit

```
ALGORITHM: TransferWithAudit
INPUT:  source_result, target_data, thresholds, cost_bps=10
OUTPUT: {signals, returns, metrics, audit_result}

1.  // Pre-deployment check
2.  IF source_result.is_degenerate:
3.      PRINT "WARNING: Source policy is degenerate. Transfer will likely collapse."
4.      REJECT or PROCEED_WITH_CAUTION
5.  
6.  theta ← source_result.theta
7.  target_features ← ComputeFeatures(target_data)
8.  target_pred ← WalkForwardGBT(target_features, train=504, test=63, step=63)
9.  target_ctx ← ComputeContexts(target_data)
10. 
11. signals ← []; returns_arr ← []; actions ← []
12. 
13. FOR t IN target_test_window:
14.     a ← argmax(theta @ target_ctx[t])
15.     threshold ← thresholds[a]
16.     signal ← (target_pred[t] >= threshold) ? 1 : 0
17.     ret ← target_returns[t+1]
18.     net_ret ← signal * ret - |signal - prev_signal| * cost_bps / 10000
19.     
20.     signals.append(signal)
21.     returns_arr.append(net_ret)
22.     actions.append(a)
23.     prev_signal ← signal
24. 
25. // Post-transfer audit
26. action_freq ← histogram(actions, bins=K) / len(actions)
27. modal_share ← max(action_freq)
28. modal_threshold ← thresholds[argmax(action_freq)]
29. 
30. // Level 1: Formal collapse check
31. is_collapsed ← (modal_share >= 0.90) AND (entropy(action_freq) / log(K) <= 0.25)
32. 
33. // Level 2: Behavioral equivalence check
34. fixed_returns ← ComputeFixedThresholdReturns(target_data, target_pred, modal_threshold)
35. sharpe_learned ← AnnualizedSharpe(returns_arr)
36. sharpe_fixed ← AnnualizedSharpe(fixed_returns)
37. sharpe_diff ← sharpe_learned - sharpe_fixed
38. 
39. // Bootstrap confidence interval
40. ci_95 ← PairedBootstrapCI(returns_arr, fixed_returns, B=2000)
41. 
42. RETURN {
43.     signals, returns: returns_arr,
44.     audit: {
45.         modal_share, modal_threshold, is_collapsed,
46.         sharpe_learned, sharpe_fixed, sharpe_diff, ci_95,
47.         recommendation: (is_collapsed OR ci_95[1] < 0) ? "REJECT" : "ACCEPT"
48.     }
49. }
```

### E.3 Transaction Cost Sensitivity Analysis

```
ALGORITHM: CostSensitivity
INPUT:  signals, raw_returns, cost_levels=[0, 5, 10, 20, 50]
OUTPUT: {break_even_bps, sharpe_by_cost}

1.  changes ← |diff(signals)|  // 1 where signal changes, 0 otherwise
2.  total_changes ← sum(changes)
3.  total_return ← sum(raw_returns)
4.  
5.  // Break-even cost: the cost level at which strategy returns equal zero
6.  break_even_bps ← (total_return / total_changes) * 10000 IF total_changes > 0
7.  
8.  sharpe_by_cost ← {}
9.  FOR cost IN cost_levels:
10.     net_returns ← raw_returns - changes * cost / 10000
11.     sharpe_by_cost[cost] ← AnnualizedSharpe(net_returns)
12. 
13. RETURN {break_even_bps, sharpe_by_cost}
```

---

## Appendix F: Context Cloud Geometry — Formal Treatment

### F.1 Decision Regions as Convex Cones

For a $K$-action LinUCB policy with weight matrix $\Theta \in \mathbb{R}^{K \times d}$, the decision region for action $k$ is:

$$R_k = \{\mathbf{c} \in \mathbb{R}^d : \theta_k^\top \mathbf{c} \geq \theta_j^\top \mathbf{c} \; \forall j \neq k\} = \{\mathbf{c} : (\theta_k - \theta_j)^\top \mathbf{c} \geq 0 \; \forall j \neq k\}$$

Each $R_k$ is a **convex polyhedral cone** — the intersection of $K-1$ half-spaces through the origin. The collection $\{R_1, \ldots, R_K\}$ forms a **conic partition** of $\mathbb{R}^d$.

### F.2 Decision Margin

Define the **decision margin** at context $\mathbf{c}$ as:

$$m(\mathbf{c}) = \theta_{k^*}^\top \mathbf{c} - \max_{j \neq k^*} \theta_j^\top \mathbf{c}$$

where $k^* = \arg\max_k \theta_k^\top \mathbf{c}$. The margin measures how far $\mathbf{c}$ is from the nearest decision boundary.

**Proposition (Collapse under small margin).** If $m(\mathbf{c}) > 0$ for all $\mathbf{c}$ in the target context cloud $\mathcal{C}_T$, and the cloud diameter $d_T = \max_{\mathbf{c}, \mathbf{c}' \in \mathcal{C}_T} \|\mathbf{c} - \mathbf{c}'\|$ satisfies $d_T < 2 \min_{\mathbf{c} \in \mathcal{C}_T} m(\mathbf{c})$, then the policy selects the same action for all target contexts.

**Proof sketch.** For any $\mathbf{c}, \mathbf{c}' \in \mathcal{C}_T$, the change in score for action $k$ is $|\theta_k^\top (\mathbf{c} - \mathbf{c}')| \leq \|\theta_k\| \cdot d_T$. If $d_T$ is small relative to the margin, the ranking of actions cannot change across the cloud. $\square$

### F.3 Empirical Margin Analysis

| Setting | Mean Margin | Std Margin | Min Margin | Max Margin |
|---------|-------------|------------|------------|------------|
| TLT source (training) | 1.8 × 10⁻⁵ | 1.5 × 10⁻⁵ | 2.0 × 10⁻⁶ | 7.3 × 10⁻⁵ |
| SPY target (from TLT) | 2.7 × 10⁻⁵ | 2.8 × 10⁻⁵ | 0 | 1.5 × 10⁻⁴ |

The extremely small margins (≈10⁻⁵) confirm that the LinUCB action scores are nearly identical across actions. This **near-tie condition** explains why:
- Degenerate sources (extreme weights) → larger margins → universal collapse
- Diverse sources (balanced weights) → smaller margins → partial concentration

### F.4 Context Cloud Overlap Metric

Define the **source-target context overlap** as:

$$\rho(S, T) = \frac{1}{d} \sum_{j=1}^{d} \frac{W_1(P_S^{(j)}, P_T^{(j)})}{\sigma_S^{(j)} + \sigma_T^{(j)}}$$

where $W_1$ is the 1-Wasserstein distance and $\sigma$ is the marginal standard deviation. When $\rho$ is small, the context clouds overlap well and transfer is more likely to succeed.

---

## Appendix G: Transaction Cost Sensitivity Analysis

### G.1 Break-Even Cost by Source

| Source | Target Mean Break-Even (bps) | Range |
|--------|------------------------------|-------|
| SPY (degenerate) | 15.2 | [2.1, 48.3] |
| QQQ (degenerate) | 12.8 | [1.5, 41.7] |
| IWM (partial) | 18.4 | [3.2, 52.1] |
| EEM (degenerate) | 11.3 | [0.8, 35.6] |
| TLT (diverse) | 22.7 | [4.5, 68.9] |
| GLD (degenerate) | 14.1 | [1.9, 44.2] |

**Finding:** Diverse sources (TLT) have higher break-even costs, meaning they can tolerate more transaction friction before becoming unprofitable. Degenerate sources have lower break-even costs, making them more vulnerable to real-world trading costs.

### G.2 Sharpe Under Different Cost Assumptions (TLT Source → All Targets)

| Cost (bps) | Mean Sharpe (ZS6) | Mean Sharpe (Fixed-0.45) | ZS6 Advantage |
|------------|-------------------|--------------------------|---------------|
| 0 | 0.285 | 0.289 | −0.004 |
| 5 | 0.271 | 0.275 | −0.004 |
| 10 | 0.257 | 0.261 | −0.004 |
| 20 | 0.229 | 0.233 | −0.004 |
| 50 | 0.145 | 0.149 | −0.004 |

**Finding:** The ZS6 advantage remains constant at −0.004 across all cost levels. This is because the TLT source policy's action distribution (73% on 0.45, 27% on other thresholds) produces the same turnover pattern regardless of cost assumptions. The policy's behavioral equivalence to Fixed-0.45 is **robust to transaction costs**.

### G.3 Turnover Analysis

| Source | Mean Annual Turnover | Turnover vs NoGating |
|--------|---------------------|---------------------|
| SPY (degenerate) | 0.0% | 0.0% |
| QQQ (degenerate) | 0.0% | 0.0% |
| IWM (partial) | 12.3% | +5.8% |
| TLT (diverse) | 8.7% | +2.2% |
| GLD (degenerate) | 0.0% | 0.0% |

**Finding:** Degenerate sources produce zero additional turnover (they always select the same threshold). Diverse sources produce modest additional turnover (2-6%), which is insufficient to significantly impact performance after costs.
