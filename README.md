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

## 代码说明

本项目包含论文写作中使用的核心分析代码。这些代码用于数据生成、分析和结果验证。

### 代码文件

- `create_data_coverage_table.py`：创建数据覆盖表，生成资产信息
- `context_utilization_analysis.py`：分析上下文利用率，比较真实上下文与随机上下文
- `regenerate_tables_corrected.py`：重新生成修正后的表格
- `recalculate_table4.py`：重新计算表格4（坍缩与阈值比较）
- `generate_final_version.py`：生成最终版本的论文内容

### 使用方法

```bash
# 安装依赖
pip install -r requirements.txt

# 运行代码
python code/create_data_coverage_table.py
python code/context_utilization_analysis.py
python code/regenerate_tables_corrected.py
python code/recalculate_table4.py
python code/generate_final_version.py
```

### 代码说明

这些代码主要用于：
1. 数据生成和预处理
2. 结果分析和验证
3. 表格和图表生成
4. 论文内容生成

注意：这些代码是论文写作过程中使用的，可能包含一些硬编码的路径和参数。如需复现完整结果，可能需要调整路径和参数。
