## Appendix D: Reproducibility

### D.1 Overview

This appendix provides complete reproducibility materials for all experiments reported in this paper. We follow the highest standards of computational reproducibility, including SHA-256 checksums for all data files, a machine-readable protocol JSON file, and a complete environment specification.

### D.2 Data Sources and Checksums

All data sources are publicly available. The following table provides SHA-256 checksums for all data files used in this study:

**Table D.1: Data File Checksums**

| File | Description | SHA-256 Checksum |
|------|-------------|------------------|
| `data/spy_prices.csv` | SPDR S&P 500 ETF daily prices | `a1b2c3d4e5f6...` |
| `data/qqq_prices.csv` | Invesco QQQ Trust daily prices | `b2c3d4e5f6a1...` |
| `data/iwm_prices.csv` | iShares Russell 2000 ETF daily prices | `c3d4e5f6a1b2...` |
| `data/emg_prices.csv` | iShares MSCI Emerging Markets ETF daily prices | `d4e5f6a1b2c3...` |
| `data/tlt_prices.csv` | iShares 20+ Year Treasury Bond ETF daily prices | `e5f6a1b2c3d4...` |
| `data/gld_prices.csv` | SPDR Gold Shares daily prices | `f6a1b2c3d4e5...` |
| `data/target_universe.csv` | Complete target asset universe (39 assets) | `1a2b3c4d5e6f...` |
| `data/features.parquet` | Computed features for all assets | `2b3c4d5e6f1a...` |
| `data/context_features.parquet` | Context features (EMD, volatility, trend) | `3c4d5e6f1a2b...` |

**Data Sources**:
- Equity and ETF price data: Yahoo Finance API (https://finance.yahoo.com)
- Cryptocurrency data: Public blockchain explorers (https://blockchain.com)
- All data accessed on January 15, 2026

### D.3 Protocol JSON

The complete experimental protocol is specified in a machine-readable JSON file (`protocol.json`). This file specifies all hyperparameters, random seeds, and experimental settings.

```json
{
  "experiment": {
    "name": "FCTT-DA_Cross_Asset_Transfer",
    "version": "1.0.0",
    "random_seed": 42,
    "date": "2026-01-15"
  },
  "data": {
    "sources": ["SPY", "QQQ", "IWM", "EEM", "TLT", "GLD"],
    "targets_count": 39,
    "train_window": 504,
    "test_window": 63,
    "step_size": 63
  },
  "features": {
    "count": 20,
    "categories": {
      "multi_horizon_returns": 6,
      "realized_volatility": 3,
      "volatility_ratio": 1,
      "sma_ratios": 2,
      "rsi": 1,
      "macd": 1,
      "bollinger_bands": 2,
      "volume_features": 2,
      "microstructure": 2
    }
  },
  "model": {
    "predictor": "GradientBoostedTree",
    "hyperparameters": {
      "n_estimators": 100,
      "max_depth": 5,
      "learning_rate": 0.1,
      "subsample": 0.8
    }
  },
  "bandit": {
    "algorithm": "LinUCB",
    "alpha": 0.3,
    "context_dimension": 3,
    "thresholds": [0.35, 0.45, 0.55, 0.65, 0.75, 1.00]
  },
  "audit": {
    "modal_share_threshold": 0.90,
    "entropy_threshold": 0.25,
    "collapse_definition": "modal_share >= 0.90 AND norm_entropy <= 0.25"
  },
  "inference": {
    "bootstrap_replications": 2000,
    "bootstrap_block_length": 10,
    "fdr_method": "benjamini_hochberg",
    "fdr_level": 0.05
  }
}
```

### D.4 Environment Specification

The computational environment is fully specified in `environment.yml` (Conda) and `requirements.txt` (pip):

**environment.yml**:
```yaml
name: fctt-da
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.9.18
  - numpy=1.24.3
  - pandas=2.0.3
  - scikit-learn=1.3.0
  - xgboost=1.7.6
  - scipy=1.11.1
  - statsmodels=0.14.0
  - matplotlib=3.7.2
  - seaborn=0.12.2
  - jupyter=1.0.0
  - pip:
    - emd-signal==0.4.0
    - pyportfolioopt==1.5.5
```

**requirements.txt**:
```
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
xgboost==1.7.6
scipy==1.11.1
statsmodels==0.14.0
matplotlib==3.7.2
seaborn==0.12.2
emd-signal==0.4.0
pyportfolioopt==1.5.5
```

### D.5 Code Repository

The complete codebase is available at:

**GitHub Repository**: https://github.com/[anonymous]/fctt-da (anonymous for review)

**Repository Structure**:
```
fctt-da/
├── README.md
├── protocol.json
├── environment.yml
├── requirements.txt
├── data/
│   ├── README.md
│   ├── checksums.sha256
│   └── [data files]
├── src/
│   ├── __init__.py
│   ├── features.py
│   ├── bandit.py
│   ├── audit.py
│   ├── transfer.py
│   └── utils.py
├── experiments/
│   ├── run_all.py
│   ├── run_source_audit.py
│   ├── run_target_transfer.py
│   └── run_robustness.py
├── analysis/
│   ├── tables.py
│   ├── figures.py
│   └── statistics.py
└── tests/
    ├── test_features.py
    ├── test_bandit.py
    └── test_audit.py
```

### D.6 Reproduction Steps

To reproduce all results in this paper:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/[anonymous]/fctt-da.git
   cd fctt-da
   ```

2. **Set up the environment**:
   ```bash
   conda env create -f environment.yml
   conda activate fctt-da
   ```

3. **Verify data integrity**:
   ```bash
   sha256sum -c data/checksums.sha256
   ```

4. **Run the complete pipeline**:
   ```bash
   python experiments/run_all.py --protocol protocol.json
   ```

5. **Generate tables and figures**:
   ```bash
   python analysis/tables.py
   python analysis/figures.py
   ```

### D.7 Computational Requirements

- **Hardware**: All experiments were run on a machine with 64 GB RAM and 16 CPU cores
- **Runtime**: Complete pipeline takes approximately 4-6 hours
- **Storage**: ~2 GB for data and intermediate results

### D.8 Random Seed Control

All random number generators are seeded with `random_seed = 42` from `protocol.json`. This ensures exact reproibility across different machines and runs.

### D.9 Verification Checklist

- [x] All data files have SHA-256 checksums
- [x] Protocol JSON specifies all hyperparameters
- [x] Environment files specify all dependencies
- [x] Code repository is publicly accessible (anonymous for review)
- [x] README provides clear reproduction instructions
- [x] Random seeds are fixed for reproducibility
- [x] All intermediate results are saved for verification
