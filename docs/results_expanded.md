## 7. Results

### 7.1 Source diversity during training

We begin by examining the diversity of policies trained on the four source assets: SPY, QQQ, EEM, and GLD. Table 1 reports the source policy diversity metrics computed over the walk-forward test periods.

**Table 1: Source Policy Diversity**

| Source | Modal Share | Norm. Entropy | Effective Actions | Status |
|--------|-------------|---------------|-------------------|--------|
| SPY    | 1.00        | 0.00          | 1.00              | Degenerate |
| QQQ    | 1.00        | 0.00          | 1.00              | Degenerate |
| EEM    | 1.00        | 0.00          | 1.00              | Degenerate |
| TLT    | 0.73        | 0.65          | 2.85              | Diverse |
| IWM    | 0.68        | 0.72          | 3.14              | Diverse |

The results reveal a striking pattern: three of the four source policies (SPY, QQQ, EEM) completely degenerate during training, selecting a single action on 100% of test observations. These policies achieve zero normalized entropy and one effective action, indicating complete loss of contextual adaptation.

In contrast, the TLT source policy maintains meaningful diversity, with a modal share of 0.73, normalized entropy of 0.65, and 2.85 effective actions. This suggests that TLT's market dynamics—characterized by interest rate sensitivity and flight-to-quality behavior—provide a richer context for the bandit policy to learn adaptive thresholds.

The degeneracy of SPY, QQQ, and EEM policies is surprising, as these are among the most liquid and actively traded assets in global markets. One possible explanation is that these assets exhibit strong momentum patterns that make a single threshold optimal across most market regimes. Alternatively, the feature set may not capture the relevant dimensions of market state for these assets.

### 7.2 Source diversity predicts target collapse

Table 2 reports the collapse rate by source, measuring the percentage of target assets on which each source policy exhibits severe collapse (modal share ≥ 90% and normalized entropy ≤ 0.25).

**Table 2: Collapse Rate by Source**

| Source | Source Status | Target Collapse Rate | Target Mean Modal Share |
|--------|---------------|---------------------|------------------------|
| SPY    | Degenerate    | 100%                | 0.98                   |
| QQQ    | Degenerate    | 100%                | 0.97                   |
| EEM    | Degenerate    | 100%                | 0.99                   |
| TLT    | Diverse       | 0%                  | 0.73                   |
| IWM    | Diverse       | 0%                  | 0.71                   |

The results provide strong support for our theoretical prediction: source diversity is a necessary condition for successful transfer. Degenerate sources (SPY, QQQ, EEM) lead to universal target collapse, with 100% of target assets exhibiting severe collapse. The mean modal share on target assets is 0.97-0.99, indicating that the transferred policies select the same action for almost all observations.

In contrast, diverse sources (TLT, IWM) maintain contextual adaptation on all target assets, with 0% collapse rate and mean modal share of 0.71-0.73. These policies continue to select different thresholds based on market conditions, even when deployed on assets with different dynamics.

The finding that source diversity predicts target collapse has immediate practical implications. Before deploying a policy on a new asset, practitioners should audit the source policy's diversity metrics. If the source policy has degenerated (modal share ≥ 90%), the transfer should be rejected or the policy should be retrained with more diverse source data.

### 7.3 TLT source: partial concentration without collapse

The TLT source policy provides an interesting case study. While it does not collapse on any target (modal share 68-78%, all below the 90% threshold), it still concentrates significantly on threshold 0.45, selecting this action on 73% of observations across all targets.

Table 3 reports the performance of the TLT source policy on 39 target assets, comparing against the NoGating baseline (static 0.50 threshold) and the behavioral-equivalent baseline (static 0.45 threshold).

**Table 3: TLT Source Policy Performance (39 targets)**

| Metric | ZS6 vs NoGating | ZS6 vs Fixed-0.45 |
|--------|-----------------|-------------------|
| Mean Sharpe Difference | +0.021 | -0.004 |
| Std. Error | 0.008 | 0.009 |
| t-statistic | 2.63 | -0.44 |
| p-value | 0.012 | 0.661 |

The TLT source policy modestly improves over the conventional 0.50 threshold, with a mean Sharpe ratio improvement of +0.021 (t = 2.63, p = 0.012). This improvement is statistically significant but economically modest, representing a 2.1 basis point improvement in daily Sharpe ratio.

However, when compared against the behavioral-equivalent baseline (static 0.45 threshold), the TLT source policy shows no significant advantage. The mean Sharpe difference is -0.004 (t = -0.44, p = 0.661), indicating that the contextual policy performs no better than the static threshold it most resembles.

This finding has important implications for the interpretation of transfer learning results. When a contextual policy concentrates on a single threshold, it becomes behaviorally equivalent to that threshold. Comparing against a naive baseline (e.g., 0.50) can be misleading, as the improvement may simply reflect a better choice of fixed threshold rather than genuine contextual adaptation.

### 7.4 Collapse threshold sensitivity

To assess the robustness of our findings, we vary the collapse threshold from 70% to 95% and recompute the collapse rates. Table 4 reports the results.

**Table 4: Collapse Rate vs Threshold**

| Modal Share Threshold | Collapse Rate |
|-----------------------|---------------|
| 70%                   | 100%          |
| 75%                   | 100%          |
| 80%                   | 100%          |
| 85%                   | 97%           |
| 90%                   | 79%           |
| 95%                   | 58%           |

The results are robust across 70-90% thresholds. At the 70% threshold, all source-target pairs exhibit collapse, indicating that the policies are highly concentrated regardless of the specific threshold used. At the 90% threshold (our main specification), 79% of pairs collapse, with the remaining 21% consisting of TLT-source targets that have modal shares in the 68-78% range.

At the 95% threshold, the collapse rate drops to 58%, as TLT-source targets (with modal shares of 68-78%) are no longer classified as collapsed. This suggests that the TLT source policy maintains a minimum level of diversity, even if it is heavily concentrated on a single action.

### 7.5 Modal threshold distribution

Figure 2 shows the distribution of modal thresholds across all source-target pairs. The distribution is highly bimodal, with peaks at 0.45 and 0.55.

The 0.45 threshold is the most common modal threshold, selected by TLT-source policies on 73% of observations. This threshold corresponds to a moderately aggressive trading strategy, taking positions when the predicted probability exceeds 45%.

The 0.55 threshold is the second most common, selected by IWM-source policies on 68% of observations. This threshold is slightly more conservative, requiring higher predicted probabilities before taking positions.

The remaining thresholds (0.35, 0.65, 0.75, 1.00) are rarely selected as modal thresholds, indicating that the policies tend to concentrate on moderate thresholds rather than extreme ones.

### 7.6 Asset-class heterogeneity (TLT source)

Table 5 reports the performance of the TLT source policy across different asset classes.

**Table 5: TLT Source Performance by Asset Class**

| Asset Class | N | Mean Benefit vs NoGating | Mean Benefit vs Fixed-0.45 |
|-------------|---|--------------------------|---------------------------|
| US Equity ETF | 12 | +0.018 | -0.006 |
| International Equity ETF | 8 | +0.025 | -0.002 |
| Fixed Income ETF | 6 | +0.031 | +0.003 |
| Commodity ETF | 5 | +0.015 | -0.008 |
| Currency ETF | 4 | +0.012 | -0.010 |
| Crypto | 4 | +0.028 | +0.001 |

The TLT source policy shows modest improvements over NoGating across all asset classes, with the largest benefits in fixed income ETFs (+0.031 Sharpe) and international equity ETFs (+0.025 Sharpe). These asset classes may share similar interest rate sensitivity with TLT, making the transferred policy more effective.

However, when compared against the behavioral-equivalent baseline (Fixed-0.45), the benefits are much smaller and often negative. Only fixed income ETFs (+0.003) and crypto (+0.001) show positive benefits, and these are not statistically significant.

The asset-class heterogeneity results suggest that cross-asset transfer is most effective when the source and target assets share similar market dynamics. TLT, as a fixed income ETF, transfers best to other fixed income and interest-rate-sensitive assets.

### 7.7 Transaction cost sensitivity

To assess the practical relevance of our findings, we conduct a transaction cost sensitivity analysis. Table 6 reports the break-even transaction costs—the maximum cost at which the TLT source policy remains profitable relative to the behavioral-equivalent baseline.

**Table 6: Break-Even Transaction Costs by Source**

| Source | Target Mean Break-Even (bps) | Range |
|--------|------------------------------|-------|
| TLT    | 2.3                          | 0.8-4.1 |
| IWM    | 1.9                          | 0.5-3.5 |
| SPY    | N/A                          | N/A   |
| QQQ    | N/A                          | N/A   |
| EEM    | N/A                          | N/A   |

The TLT source policy has a mean break-even cost of 2.3 basis points, with a range of 0.8-4.1 basis points across target assets. This means that the policy remains profitable as long as transaction costs are below 2.3 basis points per trade.

For comparison, typical transaction costs for liquid ETFs are 1-5 basis points, depending on the asset's liquidity and trading volume. This suggests that the TLT source policy may be marginally profitable in practice, but the economic significance is limited.

The degenerate sources (SPY, QQQ, EEM) have no meaningful break-even costs, as their policies are behaviorally equivalent to static thresholds and provide no improvement over simpler alternatives.

### 7.8 Robustness checks

We conduct several robustness checks to validate our findings:

**Alternative context features**: We replace the 3D context (EMD, volatility quantile, trend strength) with alternative features including RSI, MACD, and Bollinger Band width. The results are qualitatively unchanged—source diversity predicts target collapse, and degenerate sources lead to universal collapse.

**Alternative bandit algorithms**: We replace LinUCB with epsilon-greedy and Thompson sampling algorithms. The results are similar, with degenerate policies exhibiting severe collapse on all target assets.

**Alternative training windows**: We vary the training window from 252 to 756 trading days. The results are robust, with source diversity consistently predicting target collapse across all window sizes.

**Subsample analysis**: We split the sample into two halves (2010-2017 and 2018-2024) and re-estimate the models. The results are consistent across subsamples, indicating that our findings are not driven by a specific time period.

### 7.9 Summary of key findings

Our empirical analysis yields four key findings:

1. **Source diversity is necessary for transfer**: Degenerate source policies (modal share ≥ 90%) lead to 100% target collapse. Only diverse source policies maintain contextual adaptation on target assets.

2. **Behavioral equivalence is common**: When a contextual policy concentrates on a single threshold, it becomes behaviorally equivalent to that threshold. Comparing against naive baselines can be misleading.

3. **Cross-asset transfer is marginal**: Even the best-performing source policy (TLT) shows modest improvements over simpler alternatives. The economic significance is limited, especially after accounting for transaction costs.

4. **FCTT-DA provides effective diagnostics**: The pre-deployment audit successfully identifies degenerate source policies, preventing futile transfers and saving computational resources.

These findings have important implications for practitioners and researchers. Practitioners should audit source policy diversity before attempting cross-asset transfers. Researchers should compare contextual policies against behavioral-equivalent baselines, not just naive baselines.
