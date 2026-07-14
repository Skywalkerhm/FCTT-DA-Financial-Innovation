# JFDS 投稿修改指南

## 📊 当前状态总结

| 项目 | 当前值 | JFDS要求 | 状态 |
|------|--------|----------|------|
| 主内容字数 | ~4,500词 | 8,000-12,000词 | ❌ 需扩充 |
| 总字数 | ~5,600词 | - | - |
| 摘要字数 | 196词 | 150-250词 | ✅ 符合 |
| 关键词数量 | 7个 | 4-6个 | ⚠️ 略多 |
| 参考文献数量 | 182条 | ≥30条 | ✅ 符合 |
| 参考文献DOI | 0条 | 建议全部有 | ❌ 需添加 |
| 参考文献格式 | 有前导短横线 | Springer标准 | ❌ 需修正 |
| JEL分类 | ✅ 有 | 需要 | ✅ 符合 |
| 数据可用性声明 | ✅ 有 | 需要 | ✅ 符合 |
| 利益冲突声明 | ✅ 有 | 需要 | ✅ 符合 |
| 致谢(Acknowledgments) | ❌ 无 | 需要 | ❌ 需添加 |
| 作者贡献声明 | ❌ 无 | 建议有 | ❌ 需添加 |
| 行号 | ❌ 无 | 需要 | ❌ 需添加 |

---

## 📝 详细修改指南

### 1. 扩充正文内容（最关键）

**当前主内容**: ~4,500词  
**目标**: 8,000-12,000词  
**需要扩充**: ~3,500-7,500词

#### 已准备的扩充内容文件:

1. **Related Work 章节** (`related_work_expanded.md`)
   - 当前: ~473词
   - 扩充后: ~1,951词
   - 新增子章节: 2.9 Decision gating mechanisms, 2.10 Our contribution in context

2. **Methodology/Problem Formulation 章节** (`methodology_expanded.md`)
   - 当前: ~637词
   - 扩充后: ~1,994词
   - 详细解释了数学公式、算法架构、理论分析

3. **Results 章节** (`results_expanded.md`)
   - 当前: ~211词
   - 扩充后: ~1,813词
   - 添加了详细的表格解读、统计分析、鲁棒性检验

**扩充后预计字数**: 4,500 + 1,478 + 1,357 + 1,602 = ~8,937词 ✅

---

### 2. 修正参考文献格式

**当前格式** (有问题):
```
- Chu, W., Li, L., Reyzin, L., and Schapire, R. (2011). Contextual bandits with linear payoff functions. AISTATS, 208-214.
```

**修正后格式** (Springer标准):
```
Chu, W., Li, L., Reyzin, L., & Schapire, R. (2011). Contextual bandits with linear payoff functions. AISTATS, 208-214. https://doi.org/10.xxxx/xxxxx
```

**修改步骤**:
1. 去掉每条参考文献前的 `- `
2. 将 `, and` 改为 `&`
3. 为每条文献添加DOI (如果可用)

**批量修改方法**:
在Word中使用查找替换:
- 查找: `^- ` (使用通配符)
- 替换为: (空)
- 然后逐条添加DOI

---

### 3. 调整关键词数量

**当前关键词** (7个):
```
Keywords: contextual bandits, policy transfer, decision gating, model audit, static-rule collapse, behavioral equivalence, cross-asset learning
```

**建议修改为** (5-6个):
```
Keywords: contextual bandits, policy transfer, decision gating, static-rule collapse, cross-asset learning
```

或保留6个:
```
Keywords: contextual bandits, policy transfer, decision gating, model audit, static-rule collapse, cross-asset learning
```

**建议删除**: "behavioral equivalence" (可在正文中解释，不必作为关键词)

---

### 4. 添加缺失部分

#### 4.1 致谢 (Acknowledgments)

在 `Conflict of Interest` 之后添加:

```
Acknowledgments

The author感谢[具体感谢对象]。本研究得到了[基金/项目名称]的资助(项目编号: XXXX)。
```

如果无特定感谢对象，可写:
```
Acknowledgments

The author感谢编辑和匿名审稿人的宝贵建议。
```

#### 4.2 作者贡献声明 (Author Contributions)

在致谢之后添加:

```
Author Contributions

Min Huang: 概念化, 方法论, 软件, 验证, 形式分析, 调查, 数据管理, 写作-初稿, 写作-审阅编辑, 可视化, 监督, 项目管理。
```

或英文版本:
```
Author Contributions

Min Huang: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing - original draft, Writing - review & editing, Visualization, Supervision, Project management.
```

---

### 5. 添加行号和页码

#### 5.1 添加行号

在Word中:
1. 布局 → 行号 → 连续
2. 或: 布局 → 行号 → 行号选项 → 添加行号

#### 5.2 添加页码

在Word中:
1. 插入 → 页码 → 页面底端
2. 选择简单数字格式

---

### 6. 检查图表引用

**当前状态**:
- 3张嵌入图片 (image1.png, image2.png, image3.png)
- 13个表格

**需要确认**:
- [ ] 所有图片都有标题和编号
- [ ] 所有表格都有标题和编号
- [ ] 正文中引用了所有图表
- [ ] 图表标题格式一致

---

## 📋 修改清单

### 优先级 1 (必须修改):
- [ ] 扩充正文至8,000+词 (使用扩充文件)
- [ ] 修正参考文献格式 (去掉前导短横线)
- [ ] 为参考文献添加DOI
- [ ] 添加致谢部分
- [ ] 添加作者贡献声明
- [ ] 添加行号

### 优先级 2 (建议修改):
- [ ] 调整关键词至5-6个
- [ ] 添加页码
- [ ] 检查所有图表引用
- [ ] 统一图表标题格式

### 优先级 3 (可选优化):
- [ ] 检查数学公式格式
- [ ] 验证交叉引用
- [ ] 检查脚注格式
- [ ] 最终校对

---

## 📁 扩充内容文件位置

所有扩充内容文件位于:
```
/Volumes/agents/codex/paper2-LSTM量化金融/archive_20260710_1046_chatgpt_review/JFDS_Submission_Package_20260712/paper/
```

文件列表:
1. `related_work_expanded.md` - Related Work章节扩充内容 (1,951词)
2. `methodology_expanded.md` - Methodology章节扩充内容 (1,994词)
3. `results_expanded.md` - Results章节扩充内容 (1,813词)
4. `JFDS_Modification_Guide.md` - 本修改指南

---

## 🎯 预计修改后状态

| 项目 | 修改后预计值 | JFDS要求 | 状态 |
|------|-------------|----------|------|
| 主内容字数 | ~8,900词 | 8,000-12,000词 | ✅ 符合 |
| 关键词数量 | 5-6个 | 4-6个 | ✅ 符合 |
| 参考文献格式 | Springer标准 | Springer标准 | ✅ 符合 |
| 参考文献DOI | 全部有 | 建议全部有 | ✅ 符合 |
| 致谢 | ✅ 有 | 需要 | ✅ 符合 |
| 作者贡献声明 | ✅ 有 | 建议有 | ✅ 符合 |
| 行号 | ✅ 有 | 需要 | ✅ 符合 |

**预计合规率**: 95%+

---

## 💡 修改建议

1. **先扩充正文**: 使用提供的扩充文件替换相应章节
2. **再修正格式**: 批量修正参考文献格式
3. **后添加内容**: 添加致谢、作者贡献等部分
4. **最后检查**: 通读全文，确保一致性

---

## ⚠️ 注意事项

1. **保留原始文件**: 修改前备份 `main_paper_jfds_ready.docx`
2. **分步修改**: 每完成一步保存一个版本
3. **检查交叉引用**: 修改后检查所有图表、公式、参考文献的交叉引用
4. **最终校对**: 完成所有修改后进行全文校对

---

*本指南生成时间: 2026年7月12日*
*基于对 `main_paper_jfds_ready.docx` 的分析*
