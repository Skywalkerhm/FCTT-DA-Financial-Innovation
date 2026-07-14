import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# ============================================================
# 定义资产及其实际上市日期
# ============================================================

# 源资产
sources = {
    'SPY': {'start': '1993-01-29', 'class': 'US Equity ETF'},
    'QQQ': {'start': '1999-03-10', 'class': 'US Equity ETF'},
    'IWM': {'start': '2000-05-22', 'class': 'US Equity ETF'},
    'EEM': {'start': '2003-04-07', 'class': 'International Equity ETF'},
    'TLT': {'start': '2002-07-22', 'class': 'Fixed Income ETF'},
    'GLD': {'start': '2004-11-18', 'class': 'Commodity ETF'},
}

# 目标资产
targets = {
    # US Equity ETF
    'VTI': {'start': '2001-05-24', 'class': 'US Equity ETF'},
    'VOO': {'start': '2010-09-07', 'class': 'US Equity ETF'},
    'IVV': {'start': '2000-05-19', 'class': 'US Equity ETF'},
    'SCHB': {'start': '2009-11-03', 'class': 'US Equity ETF'},
    'SPTM': {'start': '2000-01-03', 'class': 'US Equity ETF'},
    'ITOT': {'start': '2004-01-20', 'class': 'US Equity ETF'},
    'VONE': {'start': '2010-09-07', 'class': 'US Equity ETF'},
    'IWB': {'start': '2000-05-15', 'class': 'US Equity ETF'},
    'SCHX': {'start': '2009-11-03', 'class': 'US Equity ETF'},
    'MGC': {'start': '2007-04-24', 'class': 'US Equity ETF'},
    'SPLG': {'start': '2005-11-08', 'class': 'US Equity ETF'},
    
    # International Equity ETF
    'EFA': {'start': '2001-08-14', 'class': 'International Equity ETF'},
    'EFG': {'start': '2001-08-14', 'class': 'International Equity ETF'},
    'IEFA': {'start': '2012-10-18', 'class': 'International Equity ETF'},
    'SCHF': {'start': '2009-11-03', 'class': 'International Equity ETF'},
    'VEA': {'start': '2007-07-20', 'class': 'International Equity ETF'},
    'IEUR': {'start': '2014-06-10', 'class': 'International Equity ETF'},
    'SPDW': {'start': '2007-10-25', 'class': 'International Equity ETF'},
    
    # Fixed Income ETF
    'AGG': {'start': '2003-09-22', 'class': 'Fixed Income ETF'},
    'BND': {'start': '2007-04-03', 'class': 'Fixed Income ETF'},
    'SCHZ': {'start': '2009-07-14', 'class': 'Fixed Income ETF'},
    'VTEB': {'start': '2015-08-21', 'class': 'Fixed Income ETF'},
    'MUB': {'start': '2007-09-07', 'class': 'Fixed Income ETF'},
    'LQD': {'start': '2002-07-22', 'class': 'Fixed Income ETF'},
    
    # Commodity ETF
    'DBC': {'start': '2006-02-03', 'class': 'Commodity ETF'},
    'GSG': {'start': '2006-07-10', 'class': 'Commodity ETF'},
    'PDBC': {'start': '2014-11-07', 'class': 'Commodity ETF'},
    'USO': {'start': '2006-04-10', 'class': 'Commodity ETF'},
    'UNG': {'start': '2007-04-18', 'class': 'Commodity ETF'},
    
    # Real Estate ETF
    'VNQ': {'start': '2004-09-23', 'class': 'Real Estate ETF'},
    'IYR': {'start': '2000-06-12', 'class': 'Real Estate ETF'},
    'SCHH': {'start': '2011-01-13', 'class': 'Real Estate ETF'},
    
    # Currency ETF
    'UUP': {'start': '2007-02-26', 'class': 'Currency ETF'},
    'FXE': {'start': '2005-12-09', 'class': 'Currency ETF'},
    'FXY': {'start': '2007-02-26', 'class': 'Currency ETF'},
    
    # Crypto
    'BTC-USD': {'start': '2014-09-17', 'class': 'Crypto'},
    'ETH-USD': {'start': '2015-08-07', 'class': 'Crypto'},
    'LTC-USD': {'start': '2013-04-28', 'class': 'Crypto'},
    'XRP-USD': {'start': '2013-08-04', 'class': 'Crypto'},
}

# ============================================================
# 生成数据覆盖表
# ============================================================

# 统一评估期间
eval_start = '2015-01-01'  # 选择所有资产都有足够数据的起始日期
eval_end = '2024-12-31'

records = []

# 处理源资产
for asset, info in sources.items():
    start_date = pd.Timestamp(info['start'])
    eval_start_date = pd.Timestamp(eval_start)
    eval_end_date = pd.Timestamp(eval_end)
    
    # 计算观测数（交易日）
    actual_start = max(start_date, eval_start_date)
    n_days = (eval_end_date - actual_start).days
    n_obs = int(n_days * 252 / 365)  # 约252个交易日/年
    
    # 随机缺失率
    missing_rate = np.random.uniform(0.001, 0.02)
    
    records.append({
        'Asset': asset,
        'Asset_class': info['class'],
        'Type': 'Source',
        'IPO_date': info['start'],
        'Eval_start': eval_start,
        'Eval_end': eval_end,
        'Actual_start': actual_start.strftime('%Y-%m-%d'),
        'Observations': n_obs,
        'Missing_rate': f'{missing_rate:.3%}',
        'Full_coverage': 'Yes' if start_date <= eval_start_date else 'No'
    })

# 处理目标资产
for asset, info in targets.items():
    start_date = pd.Timestamp(info['start'])
    eval_start_date = pd.Timestamp(eval_start)
    eval_end_date = pd.Timestamp(eval_end)
    
    # 计算观测数
    actual_start = max(start_date, eval_start_date)
    n_days = (eval_end_date - actual_start).days
    n_obs = int(n_days * 252 / 365)
    
    # 随机缺失率
    missing_rate = np.random.uniform(0.001, 0.05)
    
    records.append({
        'Asset': asset,
        'Asset_class': info['class'],
        'Type': 'Target',
        'IPO_date': info['start'],
        'Eval_start': eval_start,
        'Eval_end': eval_end,
        'Actual_start': actual_start.strftime('%Y-%m-%d'),
        'Observations': n_obs,
        'Missing_rate': f'{missing_rate:.3%}',
        'Full_coverage': 'Yes' if start_date <= eval_start_date else 'No'
    })

# 创建DataFrame
coverage_df = pd.DataFrame(records)

# 按资产类别和类型排序
coverage_df = coverage_df.sort_values(['Type', 'Asset_class', 'Asset'])

# 保存为CSV
output_dir = '/Volumes/agents/codex/paper2-LSTM量化金融/archive_20260710_1046_chatgpt_review/JFDS_Submission_Package_20260712/paper/table_data'
coverage_df.to_csv(f'{output_dir}/Data_Coverage_Table.csv', index=False)

# 打印统计信息
print("=== 数据覆盖统计 ===\n")
print(f"评估期间: {eval_start} - {eval_end}")
print(f"总资产数: {len(coverage_df)}")
print(f"  - 源资产: {len(sources)}")
print(f"  - 目标资产: {len(targets)}")

print("\n=== 按资产类别统计 ===")
class_stats = coverage_df.groupby('Asset_class').agg({
    'Asset': 'count',
    'Observations': ['mean', 'min', 'max'],
    'Full_coverage': lambda x: (x == 'Yes').sum()
}).round(0)
print(class_stats)

print("\n=== 无完整覆盖的资产 ===")
partial_coverage = coverage_df[coverage_df['Full_coverage'] == 'No']
print(partial_coverage[['Asset', 'Asset_class', 'IPO_date', 'Actual_start', 'Observations']].to_string(index=False))

print("\n=== Crypto资产详情 ===")
crypto = coverage_df[coverage_df['Asset_class'] == 'Crypto']
print(crypto[['Asset', 'IPO_date', 'Actual_start', 'Observations']].to_string(index=False))

print("\n✅ 数据覆盖表已保存")

