## 2. Related Work

### 2.1 Contextual bandits in finance

Contextual bandits (Li et al., 2010; Chu et al., 2011) have emerged as a powerful framework for sequential decision-making under uncertainty, with applications spanning portfolio allocation (Shen et al., 2015), order execution (Nevmyvaka et al., 2006), and dynamic trading (Zhang et al., 2020). The key advantage of contextual bandits over traditional supervised learning is their ability to balance exploration and exploitation by incorporating contextual information—market state features, volatility regimes, and cross-asset correlations—into the decision process.

In portfolio management, contextual bandits have been used to dynamically adjust asset allocations based on changing market conditions. Shen et al. (2015) demonstrate that bandit-based allocation strategies can outperform static mean-variance portfolios by adapting to regime shifts. Similarly, Nevmyvaka et al. (2006) apply bandit algorithms to optimal execution, showing significant reductions in market impact costs. More recently, Zhang et al. (2020) extend contextual bandits to high-frequency trading, incorporating limit order book dynamics as contextual features.

However, the existing literature has largely focused on single-asset or single-strategy applications. The question of whether contextual bandit policies trained on one asset can be effectively transferred to other assets—what we term "cross-asset policy transfer"—remains largely unexplored. Our work addresses this gap by identifying a fundamental failure mode in such transfers.

### 2.2 Transfer learning in finance

Transfer learning has been applied to cross-asset return forecasting (Zhang et al., 2023) and volatility modeling (Li et al., 2021). The underlying premise is that financial markets share common patterns—momentum, mean-reversion, volatility clustering—that can be learned from one asset and applied to others. Gu, Kelly, and Xiu (2020) demonstrate that return prediction models trained on broad cross-sections of stocks can improve individual asset forecasts, while Leippold, Wang, and Zhou (2022) extend this finding to Chinese markets.

In the deep learning era, transfer learning has become increasingly sophisticated. Pre-trained language models have been adapted for financial sentiment analysis (Araci, 2019), while convolutional neural networks trained on technical charts have been transferred across different markets (Sezer et al., 2020). Reinforcement learning policies have also been transferred across related tasks in robotics (Tobin et al., 2017) and game playing (Vinyals et al., 2019), though applications in finance remain limited.

However, most work transfers predictive models, not decision policies. The distinction matters: a predictor that transfers well may still produce a decision layer that collapses. Our work addresses this gap by focusing specifically on the transfer of decision policies—the layer that maps predictions to actions—rather than the underlying predictions themselves.

### 2.3 Policy robustness and distributional shift

The machine learning literature on distributional shift (Quinonero-Candela et al., 2009; Moreno-Torres et al., 2012) identifies two primary forms: covariate shift, where the input distribution changes, and concept shift, where the relationship between inputs and outputs changes. In financial applications, both forms are prevalent due to non-stationary market dynamics.

Robust optimization techniques have been proposed to address distributional shift. Ben-Tal et al. (2009) develop robust optimization frameworks that perform well under worst-case scenarios. In reinforcement learning, domain randomization (Tobin et al., 2017) and adversarial training (Pinto et al., 2017) have been used to improve policy robustness. However, these approaches typically assume that the shift is gradual or bounded, which may not hold in financial markets where regime changes can be abrupt.

Our work contributes by identifying a specific failure mode linked to source-side training dynamics. We show that policies trained on "degenerate" sources—assets where the contextual bandit converges to a static rule—will inevitably collapse when transferred to new assets, regardless of the transfer method employed. This finding has important implications for the deployment of machine learning policies in production trading systems.

### 2.4 Negative results and model audit

JFDS has published important negative results (e.g., Harvey et al., 2016), contributing to the scientific integrity of financial research. Our paper follows this tradition: the primary contribution is a falsifiable diagnosis of failure and an audit framework that can be applied before deployment.

The importance of negative results in finance cannot be overstated. Harvey, Liu, and Zhu (2016) document the "factor zoo" problem, showing that many published factors fail out-of-sample replication. McLean and Pontiff (2016) demonstrate that post-publication factor returns decay by 58%, suggesting data-mining biases in the original studies. Our work contributes to this literature by documenting a failure mode that, by definition, cannot be detected by standard backtests—the policy appears to work on the source asset but fails silently on target assets.

Model audit frameworks have gained importance in regulated industries. Barocas and Selbst (2016) discuss the legal implications of algorithmic decision-making, while Doshi-Velez and Kim (2017) propose standards for interpretable machine learning. In finance, regulatory requirements such as SR 11-7 (Federal Reserve, 2011) mandate model risk management. Our FCTT-DA framework provides a practical tool for auditing cross-asset policy transfers before deployment.

### 2.5 Calibration and probability thresholds

Well-calibrated probabilities are essential for threshold-based decisions (Niculescu-Mizil and Caruana, 2005). A classifier is well-calibrated if, among all instances predicted with probability p, approximately a fraction p actually belong to the positive class. In financial applications, calibration is particularly important because trading decisions often hinge on probability thresholds—for example, buying when the predicted probability of an upward move exceeds 60%.

Our GBT predictors use walk-forward validation, though we do not explicitly calibrate. This is a common practice in quantitative finance, where computational efficiency often takes precedence over perfect calibration. However, we acknowledge that calibration errors could contribute to the observed collapse phenomenon. Future work could explore whether explicit calibration improves cross-asset transfer performance.

The choice of threshold is itself a critical decision. Traditional approaches use fixed thresholds (e.g., 0.50), while more sophisticated methods adapt thresholds based on market conditions (López de Prado, 2018). Our work shows that the contextual bandit's ability to select adaptive thresholds is precisely what degenerates during cross-asset transfer, leading to collapse.

### 2.6 Model interpretability and explanation

The growing complexity of machine learning models has spurred research on interpretability. LIME (Ribeiro et al., 2016) and SHAP (Lundberg and Lee, 2017) provide local explanations for individual predictions, while attention mechanisms (Vaswani et al., 2017) offer insights into which features drive model decisions. In finance, explainability is not merely desirable—it is often a regulatory requirement under frameworks such as the EU's General Data Protection Regulation (GDPR).

Interpretability methods have been applied to financial models with mixed results. Guidotti et al. (2018) survey methods for explaining black-box models in finance, noting that post-hoc explanations may not faithfully represent the model's decision process. Our work contributes to this literature by providing a structural explanation for why certain policies fail: the failure mode is not in the prediction accuracy but in the decision-layer degeneration.

The concept of "behavioral equivalence" that we introduce provides a new lens for understanding policy failure. Two policies are behaviorally equivalent if they produce identical actions across all possible inputs, regardless of their internal representations. This concept allows us to detect when a complex contextual policy has degenerated into a simple static rule—a form of interpretability that emerges naturally from the analysis rather than being imposed externally.

### 2.7 Cross-asset transfer in quantitative finance

Cross-asset transfer has been explored in several contexts. Gu, Kelly, and Xiu (2020) demonstrate that return prediction models trained on broad cross-sections can improve individual asset forecasts. Leippold, Wang, and Zhou (2022) extend this to Chinese markets, showing that transfer learning can mitigate data limitations in emerging markets. However, these studies focus on predictive transfer, not decision-layer transfer.

In portfolio construction, the concept of "style factors" (Fama and French, 1993) represents a form of cross-asset knowledge transfer. Momentum, value, and size factors are estimated from broad cross-sections and applied to individual assets. More recently, machine learning approaches have been used to learn factor models that transfer across assets (Kelly et al., 2019; Feng et al., 2020). Our work addresses a fundamentally different question: even when predictions transfer well, does the decision policy transfer?

The distinction between predictive transfer and decision-layer transfer is crucial. A prediction model that achieves high accuracy on multiple assets does not guarantee that the same decision threshold will be optimal across assets. Different assets may have different base rates, volatility profiles, and market microstructures, requiring asset-specific decision policies. Our work formalizes this intuition and provides diagnostic tools to detect when decision-layer transfer fails.

### 2.8 Negative results in financial economics

The tradition of publishing negative results in finance dates back at least to Fama and French (1993), who documented the failure of the Capital Asset Pricing Model (CAPM) to explain the cross-section of expected returns. This seminal work opened the door to alternative asset pricing models and sparked decades of research on risk factors.

More recently, Harvey, Liu, and Zhu (2016) catalog the "factor zoo" and demonstrate that many published factors fail replication. Their analysis suggests that multiple testing biases and data-mining have inflated the apparent significance of many trading strategies. McLean and Pontiff (2016) provide complementary evidence, showing that post-publication factor returns decay by 58%, consistent with data-mining and market learning effects.

Our paper contributes to this tradition by documenting a failure mode that, by definition, cannot be detected by standard backtests. When a contextual bandit policy collapses to a static rule during cross-asset transfer, the transferred policy may still outperform a naive baseline on the target asset. Standard backtests would conclude that the transfer "works," even though the policy has lost its contextual adaptation capability. This silent failure mode has important implications for the deployment of machine learning policies in production trading systems.

### 2.9 Decision gating mechanisms

Decision gating—the process of converting predictions into actions—has received relatively little attention in the financial machine learning literature. Most work focuses on improving prediction accuracy, assuming that better predictions naturally lead to better decisions. However, the mapping from predictions to actions is itself a critical component of the trading system.

In reinforcement learning, the concept of a "policy" explicitly models this mapping. Contextual bandits represent a special case where the policy maps contextual features to actions without considering long-term consequences. The quality of the policy depends not only on the accuracy of the underlying predictions but also on the appropriateness of the decision threshold.

Our work highlights the importance of auditing decision gating mechanisms before deployment. We show that a policy trained on one asset may degenerate when transferred to another, even if the underlying predictions remain accurate. This finding suggests that the decision layer should be treated as a first-class component of the trading system, subject to the same rigorous testing and validation as the prediction model.

### 2.10 Our contribution in context

Our work makes several novel contributions to the literature on cross-asset policy transfer. First, we formally define "Static-Rule Collapse" as a failure mode where a contextual bandit policy degenerates into a fixed probability threshold. Second, we provide sufficient conditions linking source diversity to target collapse, establishing that source policy diversity is a necessary condition for successful transfer. Third, we propose the FCTT-DA framework as a practical diagnostic tool for auditing cross-asset transfers before deployment.

Our empirical analysis spans 234 source-target pairs across six asset classes, providing the most comprehensive study of cross-asset policy transfer to date. The results demonstrate that degenerate sources (SPY, QQQ, EEM, GLD) trigger 100% target collapse, while diverse sources (TLT, IWM) maintain contextual adaptation. This finding has immediate practical implications for quantitative trading firms seeking to deploy machine learning policies across multiple assets.

Finally, our work contributes to the growing literature on negative results in financial machine learning. By documenting a failure mode that cannot be detected by standard backtests, we highlight the importance of developing new diagnostic tools for evaluating machine learning policies. The FCTT-DA framework represents a step in this direction, providing a practical and deployable solution for auditing cross-asset policy transfers.
