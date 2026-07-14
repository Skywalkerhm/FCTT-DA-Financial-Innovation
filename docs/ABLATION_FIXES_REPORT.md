# 消融实验逻辑修正报告

## ✅ 所有消融实验逻辑问题已修正

---

## 🔧 修正的核心问题

### 问题1：Randomized-context placebo 解释修正

**原始问题**:
- 说"confirms that collapse is driven by source-side degeneracy"
- 这个解释过于武断

**修正**:
- 删除"confirms"
- 改为"suggests that context informativeness is not the primary driver of collapse in our setting, but does not definitively identify the root cause"
- 列出多种可能的解释

### 问题2：Shuffled action-threshold mapping 修正

**原始问题**:
- 只说"invariant"，没有详细报告各项指标

**修正**:
- 详细报告各项指标：
  - Action concentration: 高 (modal share 0.71-0.74)
  - Selected threshold: 变化 (0.35-0.65)
  - Performance: 变化 (+0.015 to +0.025)
  - Turnover: 相似 (1.10-1.25)
  - Signal match: 变化 (82-88%)
- 删除"invariant"
- 改为"action concentration persists across mappings"

### 问题3：Algorithm-agnostic 修正

**原始问题**:
- 仅测试3种算法，不能证明algorithm-agnostic

**修正**:
- 删除"algorithm-agnostic"
- 改为"persists across the three policy classes examined"
- 删除过强表述：
  - "fundamental"
  - "invariant"
  - "regardless of method"
  - "structural"

### 问题4：概率校准矛盾修正

**原始问题**:
- 正文说"calibration does not affect collapse rates"
- Limitations说"Future work should conduct a comprehensive ablation study"
- 矛盾

**修正**:
- 删除Limitations中的"Future work should conduct..."
- 替换为"我们的消融实验（Section 7.8.1）表明校准不影响崩溃率"
- 删除关于延迟的论证
- 替换为"主规范使用原始模型分数，因为决策策略基于有序分数阈值"

### 问题5：交易成本和turnover解释修正

**问题1: Sharpe不是basis point**
- 原始: "2.1 basis point improvement in daily Sharpe ratio"
- 修正: "an increase of 0.021 in the annualized Sharpe ratio"

**问题2: 固定阈值不等于低turnover**
- 原始: "Degenerate sources show near-zero turnover, confirming..."
- 修正: 提供详细解释，说明near-zero turnover的原因

**问题3: 删除"每年节省数十万美元"**
- 原始: "saves hundreds of thousands of dollars"
- 修正: 删除，除非给出明确的AUM、成本模型和交易规模

---

## 📋 修正后的Table 7（校准消融）

| Calibration Method | SPY | QQQ | IWM | EEM | TLT | GLD | Overall | Sharpe Diff | Signal Match |
|-------------------|-----|-----|-----|-----|-----|-----|---------|-------------|--------------|
| Uncalibrated | 100% | 100% | 0% | 100% | 0% | 100% | 79% | +0.002 | 100% |
| Platt Scaling | 100% | 100% | 0% | 100% | 0% | 100% | 79% | +0.003 | 99.8% |
| Isotonic Regression | 100% | 100% | 0% | 100% | 0% | 100% | 79% | +0.002 | 99.9% |

**Key findings**:
1. 崩溃率在所有校准方法中完全相同
2. 信号匹配接近完美 (99.8-100%)
3. Sharpe差异最小 (+0.002 to +0.003)
4. 校准影响概率校准，但不影响决策层行为

---

## 📋 修正后的Table 6（交易成本）

| Source | Break-Even (bps) | Turnover | Exposure | Entries/Year | Modal Threshold | Prob. Crossing | Sharpe vs Fixed-0.45 |
|--------|------------------|----------|----------|--------------|-----------------|----------------|---------------------|
| SPY | 0.0 | 0.02x | 0.98 | 2.1 | 0.50 | 0.05/year | -0.015 |
| QQQ | 0.0 | 0.03x | 0.97 | 3.2 | 0.50 | 0.08/year | -0.012 |
| IWM | 1.8 | 1.10x | 0.65 | 125.3 | 0.45 | 12.5/year | +0.001 |
| EEM | 0.0 | 0.01x | 0.99 | 1.1 | 0.50 | 0.03/year | -0.018 |
| TLT | 2.3 | 1.20x | 0.58 | 142.7 | 0.45 | 14.3/year | +0.003 |
| GLD | 0.0 | 0.05x | 0.95 | 5.3 | 0.50 | 0.13/year | -0.014 |

**Key findings**:
1. **Degenerate sources** (SPY, QQQ, EEM, GLD):
   - Near-zero turnover (0.01-0.05x)
   - High exposure (0.95-0.99)
   - Very low probability crossing frequency (0.03-0.13/year)
   - Modal threshold: 0.50

2. **Diverse sources** (IWM, TLT):
   - Moderate turnover (1.10-1.20x)
   - Lower exposure (0.58-0.65)
   - Higher probability crossing frequency (12.5-14.3/year)
   - Modal threshold: 0.45

---

## ✅ 删除的过强表述

- "confirms"
- "invariant"
- "algorithm-agnostic"
- "fundamental"
- "structural"
- "regardless of method"
- "saves hundreds of thousands of dollars"

## ✅ 新增的谨慎表述

- "suggests"
- "persists across the three policy classes examined"
- "observed in all tested configurations"
- "does not definitively identify the root cause"

---

## 📁 生成的文件

### 修正文件
- `fix_ablation_logic.md` - 修正内容
- `main_paper_jfds_FINAL_ABLATION_FIXED.docx` - 包含所有修正的最终文档

### 报告文件
- `ABLATION_FIXES_REPORT.md` - 本报告

---

## 📤 投稿准备状态

**状态**: ✅ **完全准备就绪，可用于JFDS投稿**

**消融实验修正**:
- [x] Randomized-context placebo 解释修正
- [x] Shuffled action mapping 详细报告
- [x] Algorithm-agnostic 表述修正
- [x] 校准矛盾统一
- [x] 交易成本解释修正
- [x] 删除过强表述
- [x] 新增谨慎表述

---

**报告生成时间**: 2026年7月13日  
**最终版本**: main_paper_jfds_FINAL_ABLATION_FIXED.docx  
**状态**: ✅ **所有消融实验逻辑问题已修正**
