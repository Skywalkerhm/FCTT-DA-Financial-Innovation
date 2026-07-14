# FCTT-DA: Frozen Contextual Threshold Transfer with Degeneracy Audit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 研究概述

本项目包含论文《Parameters Transfer, Policies May Not: Diagnosing Source Static Degeneracy in Cross-Asset Decision Gating》的最终数据和文档。

### 主要发现
- 识别了跨资产决策层迁移中的"Source Static Degeneracy"失败模式
- 提出了FCTT-DA诊断框架
- 在228个源-目标对上进行了实证验证

## 文件结构

```
FCTT-DA-Financial-Innovation/
├── data/                    # 研究数据
│   ├── *.csv              # 表格数据（23个文件）
│   ├── checksums/         # 校验和
│   └── raw/               # 原始数据
├── docs/                    # 文档
│   ├── paper_final.pdf    # 最终论文PDF
│   ├── 4263a944_revised_JFDS_v2.docx  # Word版本
│   └── cover_letter_financial_innovation.docx  # 投稿Cover Letter
├── README.md               # 本文件
└── requirements.txt        # Python依赖包
```

## 数据说明

### 数据来源
- **股票/ETF数据**：Yahoo Finance (2015-2024)
- **加密货币数据**：CoinGecko (2015-2024)
- **数据频率**：日频

### 数据文件
- `Table1_Source_Diversity.csv`：源策略多样性分析
- `Table2_Collapse_by_Source.csv`：各源的坍缩率
- `Table3_TLT_Performance.csv`：TLT性能分析
- `Table4_Collapse_vs_Threshold.csv`：坍缩与阈值比较
- `Table5_Performance_by_Class.csv`：各类别性能
- `Table6_Transaction_Costs.csv`：交易成本分析
- `Table7_Calibration_Ablation.csv`：校准消融实验
- `Table8_Action_Grids.csv`：动作网格分析
- `Table9_Alpha_Sensitivity.csv`：Alpha敏感性分析
- `Table10_Nonlinear_Policies.csv`：非线性策略
- `Table11_Random_Context.csv`：随机上下文
- `Table12_Shuffled_Action.csv`：动作洗牌
- `Table13_Temporal_Subsamples.csv`：时间子样本
- `Table14_Source_vs_Target.csv`：源与目标比较
- `Table15_Robustness_Summary.csv`：稳健性总结
- `Table16_Context_Value.csv`：上下文价值
- `Table17_Regime_Performance.csv`：制度性能
- `Table18_Context_Feature_Importance.csv`：上下文特征重要性
- `Context_Utilization_Analysis.csv`：上下文利用分析
- `Data_Coverage_Table.csv`：数据覆盖表
- `Pair_Level_Data_234.csv`：配对级别数据

## 引用

如果使用本数据，请引用：
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
