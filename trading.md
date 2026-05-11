# Trading Market Analysis Plugin

## 概述

Horizon 的 `asset_watchlist` 模式现已优先采用 **digital-oracle Skill 方法论**：

- 仅使用交易数据（价格、期权、收益率曲线、事件市场、波动与信用利差等）
- 每个资产篮子至少 3 个独立信号层交叉验证
- 分层输出 Data Summary / Analysis / Probability Estimates / Conclusion
- 输出继续兼容 Horizon 的 Markdown 与每日邮件

> 免责声明：本模块仅提供概率分析，不构成投资建议。

---

## 方法论

Trading Analysis 采用 digital-oracle 的核心原则：

1. Trading data only
2. 至少 3 个独立市场信号
3. 多时间窗口分层（1日 / 1周 / 1月）
4. provider 并行调用，单点失败不影响整体
5. 结构化输出，不以新闻观点或分析师观点作为交易依据

---

## 安装与回退

由于上游 `komako-workshop/digital-oracle` 仓库当前不是可直接 `pip install` 的标准发布包，Horizon 采用 vendor 方案：

- full package 路径：`src/vendor/digital_oracle_full/digital_oracle/`
- bridge：`src/market/digital_oracle_bridge.py`

运行时逻辑：

1. 优先尝试导入完整 `digital_oracle` 包（已安装或 vendored）。
2. 若不可用，自动回退到 `src/vendor/digital_oracle/providers.py` minimal provider。
3. 回退时会在 Missing Evidence 明确写入：
   - `digital-oracle full provider package unavailable; using minimal Horizon fallback provider.`

---

## 资产范围与代理限制

`asset_watchlist` 默认范围：

- QDII Nasdaq 100 Proxy
- US Mega Cap Basket
- Japan Equity Basket
- Hong Kong Equity Basket
- 用户自定义海外股票篮子（按配置 symbols）

QDII 纳斯达克 100 使用 `QQQ / ^NDX / NQ=F` 代理底层市场，**不包含**中国场内 QDII 折溢价、T+1、外汇管制等本地结构因素。

---

## Provider 体系（14 个）与用途

1. PolymarketProvider：事件概率市场
2. KalshiProvider：受监管事件概率市场
3. YahooPriceProvider：股票/ETF/指数/外汇/商品价格历史
4. DeribitProvider：加密衍生品 term structure/IV
5. USTreasuryProvider：收益率曲线、利率背景
6. WebSearchProvider：VIX/MOVE/HY OAS 等补充交易指标
7. CftcCotProvider：期货持仓结构
8. CoinGeckoProvider：加密现货与市值结构
9. EdgarProvider：SEC 内部人交易与披露
10. BisProvider：政策利率/信用缺口
11. WorldBankProvider：宏观长期指标
12. YFinanceProvider：美股期权链、IV、put/call、max pain
13. FearGreedProvider：风险偏好综合指数
14. CMEFedWatchProvider：联邦基金利率路径概率

---

## 输出结构

日报 Trading Analysis 包含：

- 分析方法说明（digital-oracle multi-signal synthesis）
- Asset Probability Overview（6 列窄表，QQ 邮箱兼容）
- Digital Oracle Signal Layers
  - Layer 1: Price Trend
  - Layer 2: Options / Volatility
  - Layer 3: Risk Appetite / Macro
- Analysis
  - Resonance signals
  - Key divergences
  - Time stratification
- Probability Estimates（1日 / 1周 / 1月）
- Signals to Monitor
- Conclusion
- Data Sources
- Missing Evidence（若有）

---

## 概率含义（1日 / 1周 / 1月）

- `up_probability`：上涨概率
- `down_probability`：下跌概率
- `neutral_probability`：震荡/中性概率
- `expected_bias`：bullish / bearish / neutral
- `confidence`：由信号覆盖与冲突程度决定

若信号冲突或不足，系统会降低置信度并在 Missing Evidence 中说明。

---

## Missing Evidence 含义

Missing Evidence 表示：

- 某 provider 调用失败
- 某资产关键信号缺失（如期权链不可用）
- 信号层覆盖不足（<3 层）
- 运行时触发 fallback

其目的是让日报结果可诊断、可回退、可审计。

---

## 免责声明

本模块输出为市场数据驱动的概率估计，不构成投资建议。市场存在不可预测风险，使用者需独立判断并承担相应风险。
