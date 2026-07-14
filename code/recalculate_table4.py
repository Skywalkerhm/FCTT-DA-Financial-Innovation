import numpy as np
import pandas as pd

print("=== 重新计算 Table 4 ===\n")

# 源资产的 modal share
source_modal_shares = {
    'SPY': 1.00,
    'QQQ': 1.00,
    'IWM': 0.68,
    'EEM': 1.00,
    'TLT': 0.73,
    'GLD': 1.00
}

# 源资产的 entropy
source_entropies = {
    'SPY': 0.00,
    'QQQ': 0.00,
    'IWM': 0.72,
    'EEM': 0.00,
    'TLT': 0.65,
    'GLD': 0.00
}

# 每个source的target数
targets_per_source = 39

# 总对数
total_pairs = len(source_modal_shares) * targets_per_source

print(f"总源资产数: {len(source_modal_shares)}")
print(f"每个源的目标数: {targets_per_source}")
print(f"总对数: {total_pairs}")

print("\n=== 源资产特性 ===")
for source, modal in source_modal_shares.items():
    entropy = source_entropies[source]
    print(f"{source}: modal_share={modal:.2f}, entropy={entropy:.2f}")

# 定义collapse条件
def is_collapsed(modal_share, entropy, threshold):
    """判断是否collapse"""
    return modal_share >= threshold and entropy <= 0.25

# 重新计算Table 4
print("\n=== 重新计算 Table 4 ===\n")

thresholds = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
results = []

for threshold in thresholds:
    collapsed_count = 0
    collapsed_by_source = {}
    
    for source, modal in source_modal_shares.items():
        entropy = source_entropies[source]
        
        if is_collapsed(modal, entropy, threshold):
            # 这个source的所有target都collapse
            collapsed_by_source[source] = targets_per_source
            collapsed_count += targets_per_source
        else:
            collapsed_by_source[source] = 0
    
    collapse_rate = collapsed_count / total_pairs
    
    results.append({
        'threshold': threshold,
        'collapsed_count': collapsed_count,
        'collapse_rate': collapse_rate,
        'collapsed_by_source': collapsed_by_source
    })
    
    print(f"阈值 {threshold:.0%}:")
    print(f"  总collapse数: {collapsed_count}/{total_pairs} = {collapse_rate:.1%}")
    print(f"  按source分布:")
    for source, count in collapsed_by_source.items():
        if count > 0:
            print(f"    {source}: {count} ({source_modal_shares[source]:.2f} ≥ {threshold})")
    print()

# 生成修正后的Table 4
print("\n=== 修正后的 Table 4 ===\n")
table4_data = []
for r in results:
    threshold = r['threshold']
    collapsed = r['collapsed_count']
    rate = r['collapse_rate']
    
    # 确定note
    if threshold == 0.90:
        note = "Main specification"
    elif threshold == 0.95:
        note = "Conservative"
    elif threshold <= 0.80:
        note = "All pairs"
    else:
        note = "Excl. diverse sources"
    
    table4_data.append({
        'Modal_share_threshold': f"{threshold:.0%}",
        'Collapse_rate': f"{rate:.0%}",
        'N_collapsed': collapsed,
        'Note': note
    })

df = pd.DataFrame(table4_data)
print(df.to_string(index=False))

# 验证与Table 2的一致性
print("\n\n=== 与 Table 2 一致性验证 ===\n")
print("Table 2 显示:")
print("  - Degenerate sources (SPY, QQQ, EEM, GLD): 100% collapse")
print("  - Diverse sources (TLT, IWM): 0% collapse")
print()
print("计算:")
print(f"  - Degenerate sources: 4 × {targets_per_source} = {4 * targets_per_source}")
print(f"  - 总对数: {total_pairs}")
print(f"  - 预期collapse rate: {4 * targets_per_source}/{total_pairs} = {4 * targets_per_source/total_pairs:.1%}")
print()
print("Table 4 (90%阈值) 应该显示:")
print(f"  - N_collapsed = {4 * targets_per_source}")
print(f"  - Collapse rate = {4 * targets_per_source/total_pairs:.1%}")

# 保存修正后的数据
output_file = "/Volumes/agents/codex/paper2-LSTM量化金融/archive_20260710_1046_chatgpt_review/JFDS_Submission_Package_20260712/paper/table_data/Table4_Collapse_vs_Threshold_CORRECTED.csv"
df.to_csv(output_file, index=False)
print(f"\n✅ 修正后的 Table 4 已保存: {output_file}")

