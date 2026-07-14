# 公式丢失清单

## 📋 8处公式丢失的详细清单

---

### 1. 段落63: 预测概率

**当前位置**: Section 3.1 Setup

**原文**:
> "The prediction  represents the model's estimate of the probability that asset  will experience a positive return over the next period."

**问题**: "prediction"和"asset"后的空格，公式丢失

**应修复为**:
> "The prediction $p_t^A$ represents the model's estimate of the probability that asset $A$ will experience a positive return over the next period."

**需要的公式**:
- $p_t^A$: 资产A在时间t的预测概率
- $A$: 资产标识

---

### 2. 段落79: LinUCB设计矩阵

**当前位置**: Section 3.3 Contextual Bandit Formulation

**原文**:
> "where  is the design matrix for action , and  is an exploration parameter. We set  based on preliminary experiments."

**问题**: "where"、"action"、"set"后的空格，公式丢失

**应修复为**:
> "where $\mathbf{A}_k$ is the design matrix for action $k$, and $\alpha$ is an exploration parameter. We set $\alpha = 0.3$ based on preliminary experiments."

**需要的公式**:
- $\mathbf{A}_k$: 动作k的设计矩阵
- $k$: 动作索引
- $\alpha$: 探索参数
- $\alpha = 0.3$: 具体值

---

### 3. 段落87: Modal-Action Share公式

**当前位置**: Section 4.1 Architecture (Module 3: Degeneracy Audit)

**原文**:
> "Modal-Action Share: , where  is the empirical frequency of action ..."

**问题**: 冒号后和"where"后的空格，公式丢失

**应修复为**:
> "Modal-Action Share: $\max_k \hat{p}_k$, where $\hat{p}_k = \frac{1}{T}\sum_{t=1}^{T} \mathbb{1}[a_t = k]$ is the empirical frequency of action $k$."

**需要的公式**:
- $\max_k \hat{p}_k$: 模态动作份额
- $\hat{p}_k$: 动作k的经验频率
- $T$: 总时间步数
- $\mathbb{1}[a_t = k]$: 指示函数
- $k$: 动作索引

---

### 4. 段落88: Normalized Entropy公式

**当前位置**: Section 4.1 Architecture (Module 3: Degeneracy Audit)

**原文**:
> "Normalized Entropy: , where  is the entropy of the action distribution."

**问题**: 冒号后和"where"后的空格，公式丢失

**应修复为**:
> "Normalized Entropy: $H(\hat{\mathbf{p}})/\log K$, where $H(\hat{\mathbf{p}}) = -\sum_k \hat{p}_k \log \hat{p}_k$ is the entropy of the action distribution."

**需要的公式**:
- $H(\hat{\mathbf{p}})/\log K$: 归一化熵
- $H(\hat{\mathbf{p}})$: 熵
- $\hat{p}_k$: 动作k的概率
- $K$: 动作总数

---

### 5. 段落93: Behavioral Equivalence定义

**当前位置**: Section 5.3 Behavioral Equivalence

**原文**:
> "where  is the set of all observed contexts on target . Behavioral equivalence is a stronger condition than severe collapse."

**问题**: "where"和"target"后的空格，公式丢失

**应修复为**:
> "where $\mathcal{C}_T$ is the set of all observed contexts on target $T$. Behavioral equivalence is a stronger condition than severe collapse."

**需要的公式**:
- $\mathcal{C}_T$: 目标T上所有观测到的上下文集合
- $T$: 目标资产

---

### 6. 段落139: Signal sequence定义

**当前位置**: Section 5.3 Behavioral Equivalence (Corollary)

**原文**:
> "If  for all , then the signal sequence is  for every ."

**问题**: "If"、"all"、"is"、"every"后的空格，公式丢失

**应修复为**:
> "If $\pi(x) = k^*$ for all $x \in \mathcal{X}$, then the signal sequence is $s_t = \mathbb{1}[p_t \geq \tau_{k^*}]$ for every $t$."

**需要的公式**:
- $\pi(x) = k^*$: 策略选择动作k*
- $x \in \mathcal{X}$: 上下文空间
- $s_t$: 时间t的信号
- $p_t$: 时间t的预测概率
- $\tau_{k^*}$: 动作k*对应的阈值
- $t$: 时间索引

---

### 7. 段落144: Returns match定义

**当前位置**: Section 5.3 Behavioral Equivalence (Corollary 3.1)

**原文**:
> "Returns match:  for all ."

**问题**: 冒号后和"all"后的空格，公式丢失

**应修复为**:
> "Returns match: $r_t(\pi) = r_t(\tau_{k^*})$ for all $t$."

**需要的公式**:
- $r_t(\pi)$: 策略π在时间t的收益
- $r_t(\tau_{k^*})$: 静态阈值τ_{k*}在时间t的收益
- $t$: 时间索引

---

### 8. 段落236: Reward定义

**当前位置**: Section 6.3 Protocol

**原文**:
> "Reward:  where  is the trading signal and  is the next-day return."

**问题**: 冒号后和两个"where"后的空格，公式丢失

**应修复为**:
> "Reward: $r_t = s_t \cdot r_{t+1}$, where $s_t$ is the trading signal and $r_{t+1}$ is the next-day return."

**需要的公式**:
- $r_t$: 时间t的奖励
- $s_t$: 时间t的交易信号
- $r_{t+1}$: 下一日收益

---

## 📊 汇总

| 序号 | 段落 | 位置 | 缺失的公式 | 优先级 |
|------|------|------|------------|--------|
| 1 | 63 | Section 3.1 | $p_t^A$, $A$ | 高 |
| 2 | 79 | Section 3.3 | $\mathbf{A}_k$, $k$, $\alpha$, $\alpha=0.3$ | 高 |
| 3 | 87 | Section 4.1 | $\max_k \hat{p}_k$, $\hat{p}_k$, $T$, $k$ | 高 |
| 4 | 88 | Section 4.1 | $H(\hat{\mathbf{p}})/\log K$, $H(\hat{\mathbf{p}})$, $\hat{p}_k$, $K$ | 高 |
| 5 | 93 | Section 5.3 | $\mathcal{C}_T$, $T$ | 中 |
| 6 | 139 | Section 5.3 | $\pi(x)=k^*$, $x$, $s_t$, $p_t$, $\tau_{k^*}$, $t$ | 中 |
| 7 | 144 | Section 5.3 | $r_t(\pi)$, $r_t(\tau_{k^*})$, $t$ | 中 |
| 8 | 236 | Section 6.3 | $r_t$, $s_t$, $r_{t+1}$ | 高 |

---

## 🔧 修复步骤

### 步骤1: 在Word中打开文档
打开 `FCTT_DA_formula_symbol_reviewed.docx`

### 步骤2: 定位丢失的公式
按段落号找到上述8处位置

### 步骤3: 插入公式
1. 将光标放在空格位置
2. 使用Word公式编辑器插入公式
3. 输入对应的LaTeX代码或使用公式面板

### 步骤4: 验证
1. 检查公式是否正确显示
2. 导出PDF验证
3. 确保公式可搜索、可复制

---

## 📝 LaTeX代码参考

### 公式1: $p_t^A$
```latex
p_t^A
```

### 公式2: $\mathbf{A}_k$
```latex
\mathbf{A}_k
```

### 公式3: $\max_k \hat{p}_k$
```latex
\max_k \hat{p}_k
```

### 公式4: $H(\hat{\mathbf{p}})/\log K$
```latex
H(\hat{\mathbf{p}})/\log K
```

### 公式5: $\mathcal{C}_T$
```latex
\mathcal{C}_T
```

### 公式6: $s_t = \mathbb{1}[p_t \geq \tau_{k^*}]$
```latex
s_t = \mathbb{1}[p_t \geq \tau_{k^*}]
```

### 公式7: $r_t(\pi) = r_t(\tau_{k^*})$
```latex
r_t(\pi) = r_t(\tau_{k^*})
```

### 公式8: $r_t = s_t \cdot r_{t+1}$
```latex
r_t = s_t \cdot r_{t+1}
```

---

**清单生成时间**: 2026年7月13日  
**状态**: ✅ **清单完整，可按此修复**
