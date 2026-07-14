# Method Details Supplement

## 6.1 Data (Expanded)

### 6.1.1 Asset Universe

**Source Assets (6)**:
- SPY: SPDR S&P 500 ETF Trust
- QQQ: Invesco QQQ Trust
- IWM: iShares Russell 2000 ETF
- EEM: iShares MSCI Emerging Markets ETF
- TLT: iShares 20+ Year Treasury Bond ETF
- GLD: SPDR Gold Shares

**Target Assets (39)**:
- US Equity ETFs (12): VTI, VOO, IVV, SCHB, SPTM, ITOT, VONE, IWB, SCHX, MGC, SPLG, SCHK
- International Equity ETFs (8): EFA, EFG, IEFA, SCHF, VEA, IEUR, SPDW, ACWI
- Fixed Income ETFs (6): AGG, BND, SCHZ, VTEB, MUB, LQD
- Commodity ETFs (5): DBC, GSG, PDBC, USO, UNG
- Real Estate ETFs (3): VNQ, IYR, SCHH
- Currency ETFs (3): UUP, FXE, FXY
- Crypto Assets (3): BTC-USD, ETH-USD, SOL-USD

### 6.1.2 Data Sources and Access

- **Equity/ETF Data**: Yahoo Finance API (https://finance.yahoo.com)
- **Cryptocurrency Data**: Public blockchain explorers (https://blockchain.com)
- **Access Date**: January 15, 2026
- **Data Period**: January 1, 2010 – December 31, 2024
- **Frequency**: Daily (close-to-close returns)

### 6.1.3 Data Processing

**Price Adjustments**:
- All prices are adjusted for stock splits and dividends
- We use Adjusted Close prices for return computation

**Missing Values**:
- Forward-fill missing values (up to 5 consecutive days)
- Drop assets with >10% missing values in any rolling window

**Liquidity Filter**:
- Minimum average daily volume: 1 million shares (for ETFs)
- No volume filter for crypto assets

**Calendar Alignment**:
- US trading days are used as the reference calendar
- Crypto prices are mapped to the nearest US trading day
- Non-trading days are excluded from analysis

---

## 6.2 Features (Expanded)

### 6.2.1 Feature Definitions

We compute 20 technical and fundamental features for each asset:

**Multi-Horizon Returns (6)**:
- Return over past 1, 5, 10, 21, 63, 252 trading days
- Formula: $r_t^{(h)} = \frac{P_t}{P_{t-h}} - 1$

**Realized Volatility (3)**:
- 21-day, 63-day, 252-day realized volatility
- Formula: $\sigma_t^{(h)} = \sqrt{\frac{252}{h} \sum_{i=1}^{h} r_{t-i+1}^2}$

**Volatility Ratio (1)**:
- Ratio of short-term to long-term volatility
- Formula: $vr_t = \frac{\sigma_t^{(21)}}{\sigma_t^{(252)}}$

**SMA Ratios (2)**:
- Price relative to 50-day and 200-day SMA
- Formula: $sma_t^{(n)} = \frac{P_t}{\frac{1}{n}\sum_{i=0}^{n-1} P_{t-i}}$

**RSI (1)**:
- 14-day Relative Strength Index
- Formula: $rsi_t = 100 - \frac{100}{1 + \frac{\text{avg gain}_{14}}{\text{avg loss}_{14}}}$

**MACD (1)**:
- Moving Average Convergence Divergence
- Formula: $macd_t = ema_{12}(P_t) - ema_{26}(P_t)$

**Bollinger Bands (2)**:
- Distance from upper and lower Bollinger Bands (20-day, 2 std)
- Formula: $bb_t^{upper} = \frac{P_t - (SMA_{20} + 2\sigma_{20})}{2\sigma_{20}}$

**Volume Features (2)**:
- Volume relative to 20-day average
- Volume volatility (20-day)

**Microstructure Features (2)**:
- High-low range relative to close
- Close-to-close vs. high-low volatility ratio

### 6.2.2 Feature Standardization

All features are standardized using rolling z-scores:

$z_t = \frac{x_t - \mu_t^{(252)}}{\sigma_t^{(252)}}$

where $\mu_t^{(252)}$ and $\sigma_t^{(252)}$ are the rolling mean and standard deviation over the past 252 trading days.

**Look-Ahead Prevention**:
- All features use only past data (no future information)
- Standardization uses expanding window for first 252 days

### 6.2.3 Context Features for LinUCB

The 3 context features for the bandit are:

1. **EMD Trend**: First intrinsic mode function of the price series
   - Computed using Empirical Mode Decomposition
   - Captures short-term momentum
   
2. **Volatility Quantile**: Current volatility relative to historical distribution
   - Computed as percentile rank over 252-day rolling window
   - Identifies high/low volatility regimes

3. **Trend Strength**: Consistency of recent price movements
   - Computed as ratio of directional movement to total movement
   - Distinguishes trending from mean-reverting markets

---

## 6.3 Protocol (Expanded)

### 6.3.1 Walk-Forward Validation

**Training Window**: 504 trading days (~2 years)
**Test Window**: 63 trading days (~1 quarter)
**Step Size**: 63 days

**Procedure**:
1. Train GBT on features from day $t-504$ to $t-1$
2. Generate predictions for day $t$ to $t+62$
3. Step forward 63 days and repeat

### 6.3.2 GBT Predictor

**Algorithm**: XGBoost (Gradient Boosted Trees)

**Hyperparameters**:
- n_estimators: 100
- max_depth: 5
- learning_rate: 0.1
- subsample: 0.8
- colsample_bytree: 0.8
- min_child_weight: 5
- random_state: 42

**Label Definition**:
- Binary classification: 1 if next-day excess return > 0, else 0
- Excess return: $r_{t+1} - r_f$ where $r_f$ is the 1-month T-bill rate

**Prediction Output**:
- Probability of positive excess return: $\hat{p}_t \in [0, 1]$

### 6.3.3 LinUCB Bandit

**Algorithm**: LinUCB with disjoint linear models

**Initialization**:
- $A_k = I_d$ (identity matrix) for each action $k$
- $b_k = 0$ (zero vector) for each action $k$

**Action Selection**:
$a_t = \arg\max_k \left( \theta_k^\top c_t + \alpha \sqrt{c_t^\top A_k^{-1} c_t} \right)$

where $\theta_k = A_k^{-1} b_k$

**Update Rule**:
$A_k \leftarrow A_k + c_t c_t^\top$
$b_k \leftarrow b_k + r_t c_t$

**Reward Definition**:
$r_t = s_t \cdot r_{t+1}$

where $s_t \in \{0, 1\}$ is the trading signal and $r_{t+1}$ is the next-day return

### 6.3.4 Source Policy Training

**Training Procedure**:
1. Train LinUCB on source asset using walk-forward windows
2. Collect actions from all test windows
3. Compute diversity metrics (modal share, entropy)

**Policy Freezing**:
- After training, freeze the entire bandit state ($A_k$, $b_k$)
- No further learning on target assets

### 6.3.5 Transfer Evaluation

**Zero-Shot Transfer**:
1. Apply frozen source policy to target asset
2. Generate signals for all target test windows
3. Compute performance metrics

**Baselines**:
- NoGating: Static threshold at 0.50
- Fixed-$\tau$: Static thresholds at 0.35, 0.45, 0.55, 0.65, 0.75
- Behavioral-equivalent: Fixed threshold closest to learned policy

---

## 6.4 Execution (Expanded)

### 6.4.1 Computational Environment

- **Hardware**: 64 GB RAM, 16 CPU cores
- **OS**: macOS 13.0
- **Python**: 3.9.18
- **Runtime**: ~4-6 hours for complete pipeline

### 6.4.2 Random Seed Control

All random number generators are seeded with `random_seed = 42`:
- NumPy: `np.random.seed(42)`
- XGBoost: `random_state=42`
- Bootstrap: Fixed seed for reproducibility

### 6.4.3 Memory Management

- Process one source-target pair at a time
- Save intermediate results to disk
- Clear memory between pairs

---

## 6.5 Reproducibility (Expanded)

### 6.5.1 Code Repository

Complete code available at: [anonymous repository]

**Structure**:
```
fctt-da/
├── src/           # Source code
├── scripts/       # Experiment scripts
├── data/          # Data files
├── results/       # Output results
└── docs/          # Documentation
```

### 6.5.2 Data Checksums

SHA-256 checksums provided for all data files:
```bash
sha256sum -c data/checksums.sha256
```

### 6.5.3 Environment Specification

Complete environment specified in:
- `environment.yml` (Conda)
- `requirements.txt` (pip)

### 6.5.4 Protocol JSON

Machine-readable protocol in `protocol.json`:
- All hyperparameters
- Random seeds
- Data specifications
- Output settings

### 6.5.5 Reproduction Steps

```bash
# 1. Clone repository
git clone [anonymous URL]
cd fctt-da

# 2. Set up environment
conda env create -f environment.yml
conda activate fctt-da

# 3. Verify data
sha256sum -c data/checksums.sha256

# 4. Run experiments
make reproduce
```

---

## A. Additional Experimental Details

### A.1 Bootstrap Inference

**Method**: Stationary Bootstrap (Politis and Romano, 1994)

**Parameters**:
- Replications: 2,000
- Mean block length: 10 periods
- Confidence level: 95%

**Procedure**:
1. Generate 2,000 bootstrap samples
2. Compute test statistic for each sample
3. Construct confidence interval using percentile method
4. Compute p-value as proportion of bootstrap samples with statistic ≤ 0

### A.2 False Discovery Rate Control

**Method**: Benjamini-Hochberg (1995)

**Procedure**:
1. Sort p-values in ascending order
2. For each p-value $p_{(i)}$, compute adjusted threshold: $\frac{i}{m} \cdot \alpha$
3. Reject hypotheses where $p_{(i)} \leq \frac{i}{m} \cdot \alpha$

**Parameters**:
- $\alpha = 0.05$ (FDR level)
- $m$ = number of tests (234 source-target pairs)

### A.3 Transaction Cost Analysis

**Cost Range**: 1-10 basis points per trade

**Break-Even Calculation**:
- Maximum cost at which strategy remains profitable
- Computed for each source-target pair

**Turnover Calculation**:
- Annual turnover = (number of trades × 2) / (total observations / 252)
- Reported as multiple of portfolio value
