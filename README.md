# FCTT-DA: Frozen Contextual Threshold Transfer with Degeneracy Audit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 研究概述

本项目包含论文《Parameters Transfer, Policies May Not: Diagnosing Source Static Degeneracy in Cross-Asset Decision Gating》的完整代码和数据。

### 主要发现
- 识别了跨资产决策层迁移中的"Source Static Degeneracy"失败模式
- 提出了FCTT-DA诊断框架
- 在228个源-目标对上进行了实证验证

## 快速开始

### 环境要求
```bash
Python 3.8+
pandas >= 1.3.0
numpy >= 1.21.0
scikit-learn >= 1.0.0
matplotlib >= 3.4.0
```

### 安装
```bash
git clone https://github.com/Skywalkerhm/FCTT-DA-Financial-Innovation.git
cd FCTT-DA-Financial-Innovation
pip install -r requirements.txt
```

### 数据说明

#### 数据来源
- **股票/ETF数据**：Yahoo Finance (2015-2024)
- **加密货币数据**：CoinGecko (2015-2024)
- **数据频率**：日频

#### 数据结构
```
data/
├── raw/           # 原始数据
├── processed/     # 处理后的数据
└── checksums/     # SHA-256校验和
```

## 代码结构

```
code/
├── data_collection/       # 数据收集脚本
├── preprocessing/         # 数据预处理
├── models/                # 模型实现
├── analysis/              # 分析脚本
└── visualization/         # 可视化代码
```

## 复现指南

详细复现步骤请参考：[docs/replication_guide.md](docs/replication_guide.md)

## 引用

如果使用本代码或数据，请引用：
```bibtex
@article{huang2026fctt,
  title={Parameters Transfer, Policies May Not: Diagnosing Source Static Degeneracy in Cross-Asset Decision Gating},
  author={Huang, Min and Liu, Mingyan and Li, Xiaoer},
  journal={Financial Innovation},
  year={2026}
}
```

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 联系方式

- **Min Huang**：minhuang1@link.cuhk.edu.cn
- **项目主页**：https://github.com/Skywalkerhm/FCTT-DA-Financial-Innovation

## 致谢

感谢Yahoo Finance和CoinGecko提供数据支持。
