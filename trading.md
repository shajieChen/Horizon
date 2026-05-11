# Trading Market Analysis Plugin

## 概述 (Overview)

Horizon 内置 Trading Analysis 插件，在每日日报中提供固定资产池的市场概率分析。  
该模块默认开启（`trading.enabled = true`），不依赖外部新闻事件触发，每天至少生成一次分析报告。

**重要免责声明**：本模块仅提供基于市场数据的概率分析，不构成投资建议。

---

## 默认开启 (Default On)

`TradingConfig.enabled` 默认为 `true`。若 `data/config.json` 中缺少 `trading` 字段，系统会自动使用默认配置启动，不影响邮件、Webhook 及正常日报流程。

---

## 运行模式 (Modes)

### `asset_watchlist`（默认）

- 不依赖新闻关键词触发
- 每日自动生成固定资产池的 1D/1W/1M 概率分析
- 即使当天无新闻命中，日报顶部仍会插入 Trading Watchlist 条目

### `event_driven`（兼容旧版）

- 基于新闻关键词触发，分析 macro_rates、crypto_cycle 等事件类型
- 设置 `trading.mode = "event_driven"` 启用

---

## 资产分析范围 (Asset Scope)

`asset_watchlist` 模式仅分析以下固定资产类别，**不再默认输出** crypto / commodity / geopolitical 分析：

| 类别标识 | 说明 |
|---|---|
| `qdii_nasdaq100` | QDII 纳斯达克 100（使用 QQQ / ^NDX / NQ=F 作代理） |
| `overseas_stock` | 海外股票 |
| `us_stock` | 美国股票（默认含 AAPL / MSFT / NVDA / GOOGL / META / AMZN / TSLA） |
| `japan_stock` | 日本股票（默认含 7203.T / 6758.T / 9984.T / 8035.T / 6861.T） |
| `hongkong_stock` | 香港股票（默认含 0700.HK / 9988.HK / 3690.HK / 1810.HK / 9618.HK） |

---

## QDII Nasdaq 100 代理限制

QDII 纳斯达克 100 分析使用 QQQ / ^NDX / NQ=F 作为底层指数代理。  
**注意**：此分析不涵盖国内 QDII 基金的折溢价，不反映 T+1 赎回规则及外汇管制影响。

---

## 概率含义 (Horizon Probability)

每个资产输出三个时间维度的方向概率：

| 字段 | 说明 |
|---|---|
| `up_probability` | 上涨概率（%） |
| `down_probability` | 下跌概率（%） |
| `neutral_probability` | 中性/横盘概率（%） |
| `expected_bias` | 预期偏向：bullish / bearish / neutral |
| `confidence` | 置信度：low / medium（取决于有效信号数量） |
| `basis` | 分析依据（来自哪些价格/技术信号） |
| `invalidation` | 反证条件（何种情况下概率估算失效） |

三个概率之和约等于 100%。当真实数据不足时：
- 使用保守基准分布（up=33 / down=33 / neutral=34）
- `confidence = low`
- `data_quality = low`
- 在 Missing Evidence 中说明缺少真实数据

---

## 数据源 (Data Sources)

| Provider | 说明 | 依赖 |
|---|---|---|
| `yahoo_price` | 通过 yfinance 获取 30 日价格历史，计算 1D/5D/20D 回报、MA 位置、实现波动率 | yfinance (optional) |
| `yfinance` | 获取美国股票期权链，输出 ATM IV / implied move | yfinance (optional) |
| `fear_greed` | US 市场情绪代理指标 | 无 |
| `treasury` | 美国利率环境代理 | 无 |

---

## yfinance 可选依赖

`yfinance` 为可选依赖：

```bash
# 安装含 trading 支持的版本
pip install -e '.[trading]'
```

若未安装 yfinance：
- `yahoo_price` 回退为桩数据（stub）
- `yfinance` 返回 "N/A" 信号
- **程序不会崩溃**，分析继续运行，Missing Evidence 中记录提示

---

## 失败容忍策略 (Failure Tolerance)

- 每个 provider 调用独立封装在 `try/except` 中
- 单个 symbol 获取失败不会中断整体分析
- 日本 / 香港股票期权不支持时记录为 Missing Evidence，不报错
- 信号数量不足时，使用 `confidence = low` 保守输出，明确说明数据不足
- Provider 错误写入 `errors` 字段，并在日报中的"信息缺口"部分展示

---

## 配置示例 (Configuration)

```json
{
  "trading": {
    "enabled": true,
    "mode": "asset_watchlist",
    "min_ai_score": 0.0,
    "max_items_per_run": 20,
    "default_horizons": ["1d", "1w", "1m"],
    "asset_scope": [
      "qdii_nasdaq100", "overseas_stock", "us_stock", "japan_stock", "hongkong_stock"
    ],
    "watch_assets": [
      {
        "name": "QDII Nasdaq 100 Proxy",
        "category": "qdii_nasdaq100",
        "symbols": ["QQQ", "^NDX", "NQ=F"],
        "market": "US",
        "analysis_proxy": true
      },
      {
        "name": "US Mega Cap Basket",
        "category": "us_stock",
        "symbols": ["AAPL", "MSFT", "NVDA", "GOOGL", "META", "AMZN", "TSLA"],
        "market": "US"
      }
    ],
    "enabled_providers": ["yahoo_price", "yfinance", "fear_greed", "treasury"]
  }
}
```

---

## 输出字段

每个分析结果写入：

- `item.metadata["trading_analysis"]`：完整结构化分析（含 `asset_views`）
- `item.metadata["forecast"]`：与 DailySummarizer 兼容的预测结构

日报中渲染的内容：

- 资产概率总览表（1D / 1W / 1M）
- 每个资产的详细分析（概率 + 依据 + 反证条件）
- 信息缺口（Missing Evidence）
- 免责声明

---

## 免责声明

本模块提供的所有分析结果均基于市场历史数据的统计概率模型，**不构成投资建议**。  
市场存在不可预测的不确定性，概率估算不代表未来实际走势。使用者需独立判断并承担相应风险。

