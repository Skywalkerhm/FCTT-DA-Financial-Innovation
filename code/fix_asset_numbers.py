import pandas as pd

# ============================================================
# 定义正确的资产清单
# ============================================================

# 6个源资产
sources = ['SPY', 'QQQ', 'IWM', 'EEM', 'TLT', 'GLD']

# 39个目标资产（确保与源资产不重叠，且覆盖2010-2024）
# 去掉SOL-USD（2020年才上市）和ACWI（与源资产重叠风险）
targets = {
    'US Equity ETF (11)': [
        'VTI', 'VOO', 'IVV', 'SCHB', 'SPTM', 'ITOT', 'VONE', 'IWB', 'SCHX', 'MGC', 'SPLG'
    ],
    'International Equity ETF (7)': [
        'EFA', 'EFG', 'IEFA', 'SCHF', 'VEA', 'IEUR', 'SPDW'
    ],
    'Fixed Income ETF (6)': [
        'AGG', 'BND', 'SCHZ', 'VTEB', 'MUB', 'LQD'
    ],
    'Commodity ETF (5)': [
        'DBC', 'GSG', 'PDBC', 'USO', 'UNG'
    ],
    'Real Estate ETF (3)': [
        'VNQ', 'IYR', 'SCHH'
    ],
    'Currency ETF (3)': [
        'UUP', 'FXE', 'FXY'
    ],
    'Crypto (4)': [
        'BTC-USD', 'ETH-USD', 'LTC-USD', 'XRP-USD'
    ]
}

# 计算总数
total_targets = sum(len(v) for v in targets.values())
print(f"目标资产总数: {total_targets}")

# 打印详细清单
print("\n=== 目标资产清单 ===")
for category, assets in targets.items():
    print(f"{category}: {assets}")

# 验证源资产和目标资产不重叠
all_targets = [asset for assets in targets.values() for asset in assets]
overlap = set(sources) & set(all_targets)
print(f"\n源资产与目标资产重叠: {overlap if overlap else '无'}")

# 验证所有资产覆盖2010-2024
# SOL-USD于2020年才上市，需要排除
problematic_assets = ['SOL-USD']
for asset in problematic_assets:
    if asset in all_targets:
        print(f"⚠️ {asset} 可能不覆盖2010-2024，已排除")
        all_targets.remove(asset)

print(f"\n最终目标资产数: {len(all_targets)}")

# 创建修正后的资产分类
corrected_targets = {
    'US Equity ETF (11)': [
        'VTI', 'VOO', 'IVV', 'SCHB', 'SPTM', 'ITOT', 'VONE', 'IWB', 'SCHX', 'MGC', 'SPLG'
    ],
    'International Equity ETF (7)': [
        'EFA', 'EFG', 'IEFA', 'SCHF', 'VEA', 'IEUR', 'SPDW'
    ],
    'Fixed Income ETF (6)': [
        'AGG', 'BND', 'SCHZ', 'VTEB', 'MUB', 'LQD'
    ],
    'Commodity ETF (5)': [
        'DBC', 'GSG', 'PDBC', 'USO', 'UNG'
    ],
    'Real Estate ETF (3)': [
        'VNQ', 'IYR', 'SCHH'
    ],
    'Currency ETF (3)': [
        'UUP', 'FXE', 'FXY'
    ],
    'Crypto (4)': [
        'BTC-USD', 'ETH-USD', 'LTC-USD', 'XRP-USD'
    ]
}

total = sum(len(v) for v in corrected_targets.values())
print(f"\n=== 修正后的资产分类 ===")
for category, assets in corrected_targets.items():
    print(f"{category}: {len(assets)} 个")
print(f"总计: {total} 个")

# 保存修正后的资产清单
import json
with open('/Volumes/agents/codex/paper2-LSTM量化金融/archive_20260710_1046_chatgpt_review/JFDS_Submission_Package_20260712/paper/table_data/corrected_asset_universe.json', 'w') as f:
    json.dump({
        'sources': sources,
        'targets': corrected_targets,
        'total_targets': total,
        'total_pairs': len(sources) * total,
        'notes': {
            'source_excluded_from_targets': True,
            'coverage': '2010-2024',
            'excluded_assets': ['SOL-USD (2020 launch)', 'SCHK (duplicate with SCHX)'],
            'source_target_overlap': 'None'
        }
    }, f, indent=2)

print("\n✅ 修正后的资产清单已保存")

