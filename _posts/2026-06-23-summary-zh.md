---
layout: default
title: "Horizon Summary: 2026-06-23 (ZH)"
date: 2026-06-23
lang: zh
---

> From 44 items, 16 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [美联储发布 FOMC 货币政策声明](#item-2) ⭐️ 9.0/10
3. [联合国欢迎黎巴嫩停火；人权专家呼吁追究伊朗责任](#item-3) ⭐️ 8.0/10
4. [IAEA 欢迎美伊停战备忘录，愿提供核核查协助](#item-4) ⭐️ 8.0/10
5. [美联储发布 6 月 FOMC 经济预测](#item-5) ⭐️ 8.0/10
6. [联合国安理会警告乌克兰面临“危险升级循环”](#item-6) ⭐️ 7.0/10
7. [联合国安理会警告苏丹奥贝德面临大规模暴行风险](#item-7) ⭐️ 7.0/10
8. [联合国维护黎巴嫩维和人员行动自由](#item-8) ⭐️ 7.0/10
9. [皮耶罗·奇波洛内：央行货币在国家主权中的角色](#item-9) ⭐️ 7.0/10
10. [欧洲央行工资追踪器显示 2026 年工资压力稳定](#item-10) ⭐️ 7.0/10
11. [欧洲央行莱恩就欧元区经济前景发表讲话](#item-11) ⭐️ 7.0/10
12. [联合国儿基会：加沙停火后仍有 265 名儿童丧生](#item-12) ⭐️ 6.0/10
13. [联合国特使警告利比亚政治窗口收窄 威胁石油稳定](#item-13) ⭐️ 6.0/10
14. [安理会讨论停火下加沙恶化的人道危机](#item-14) ⭐️ 6.0/10
15. [联合国人权高专警告民兵逼近苏丹 El Obeid 恐引发暴行](#item-15) ⭐️ 6.0/10
16. [拉加德出席欧洲议会经济货币听证会](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 22, 22:54

**Trading Analysis**

> 分析方法：digital-oracle multi-signal synthesis  
> 分析范围：QDII 纳斯达克 100 / 海外股票 / 美国股票 / 日本股票 / 香港股票  
> 时间维度：1日 / 1周 / 1月  
> 数据原则：仅使用市场交易数据，不使用新闻观点或分析师观点  
> 可追溯性：结构化 provider 数据 + WebSearch 市场数据引用，参考文章列于报告末尾。  
> 免责声明：本分析仅基于市场数据进行概率估算，不构成投资建议。市场存在不确定性，请独立判断并承担相应风险。

> 数据状态：部分市场数据暂不可用，已采用保守基准概率估计。

### 资产概率总览 (Asset Probability Overview)

| 资产 | 市场 | 1日 | 1周 | 1月 | 数据质量 |
|---|---|---|---|---|---|
| QDII Nasdaq 100 Proxy | US | bullish 38/31/31 | bullish 38/31/31 | bullish 39/30/31 | high |
| US Mega Cap Basket | US | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | high |
| Japan Equity Basket | JP | bullish 38/31/31 | bullish 38/31/31 | bullish 39/30/31 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| ^NDX price trend | close=30347.08; 1d=-0.19%; 5d=+2.40%; 20d=+3.37% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=30576.75; 1d=+1.04%; 5d=+3.08%; 20d=+3.84% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=737.95; 1d=-0.36%; 5d=+2.30%; 20d=+3.28% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=1.6%; implied_move=0.1%; put/call OI=3.979911454817933 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.51; 2Y=4.24; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=34.7; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：1日篮子收益与5日均线结构偏强
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | high |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | high |
| 1月 | 39% | 30% | 31% | bullish | 20日趋势维持上行，1月窗口偏多 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| ^NDX price trend | close=30347.08; 1d=-0.19%; 5d=+2.40%; 20d=+3.37% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=30576.75; 1d=+1.04%; 5d=+3.08%; 20d=+3.84% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=737.95; 1d=-0.36%; 5d=+2.30%; 20d=+3.28% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NVDA price trend | close=208.65; 1d=-0.97%; 5d=+1.69%; 20d=-4.84% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=563.85; 1d=-2.32%; 5d=-0.46%; 20d=-7.08% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=367.34; 1d=-3.18%; 5d=-5.99%; 20d=-12.35% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=405.05; 1d=+1.14%; 5d=-0.34%; 20d=-3.06% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=297.01; 1d=-0.34%; 5d=+2.02%; 20d=-2.62% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=349.68; 1d=-4.99%; 5d=-2.78%; 20d=-9.74% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| TSLA options surface | ATM IV=4.4%; implied_move=0.2%; put/call OI=0.6685747624971103 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=7.2%; implied_move=0.3%; put/call OI=0.49921647638235955 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=6.1%; implied_move=0.2%; put/call OI=0.7997819975904997 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=4.8%; implied_move=0.2%; put/call OI=1.0134706814580032 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=13.5%; implied_move=0.6%; put/call OI=0.9692369430741524 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=5.9%; implied_move=0.2%; put/call OI=0.38753623188405795 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.51; 2Y=4.24; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| AAPL insider filings | recent Form4 count=589 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| NVDA insider filings | recent Form4 count=558 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=34.7; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：有效交易信号不足，使用保守基准分布。
- 1月：有效交易信号不足，使用保守基准分布。

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1月 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| NVDA price trend | close=208.65; 1d=-0.97%; 5d=+1.69%; 20d=-4.84% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=563.85; 1d=-2.32%; 5d=-0.46%; 20d=-7.08% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=367.34; 1d=-3.18%; 5d=-5.99%; 20d=-12.35% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 6758.T price trend | close=3183.00; 1d=+1.37%; 5d=-4.13%; 20d=-11.53% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2741.50; 1d=-1.26%; 5d=-5.55%; 20d=-9.40% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77990.00; 1d=+0.37%; 5d=+3.09%; 20d=-1.10% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=77800.00; 1d=+3.24%; 5d=+6.93%; 20d=+49.10% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7244.00; 1d=+1.87%; 5d=+1.47%; 20d=+2.46% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=96.97; 1d=+0.74%; 5d=+5.16%; 20d=+6.71% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=34.7; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.51; 2Y=4.24; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 跨层分歧信息有限，后续需补充更多波动与事件市场数据。

**Time stratification**
- 1日：1日篮子收益与5日均线结构偏强
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | medium |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | medium |
| 1月 | 39% | 30% | 31% | bullish | 20日趋势维持上行，1月窗口偏多 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 6758.T price trend | close=3183.00; 1d=+1.37%; 5d=-4.13%; 20d=-11.53% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2741.50; 1d=-1.26%; 5d=-5.55%; 20d=-9.40% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77990.00; 1d=+0.37%; 5d=+3.09%; 20d=-1.10% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| EWH price trend | close=21.33; 1d=+0.23%; 5d=-1.48%; 20d=-9.04% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=23.72; 1d=-3.50%; 5d=-9.47%; 20d=-20.03% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=102.90; 1d=-1.91%; 5d=-6.62%; 20d=-18.24% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=33.43; 1d=+0.39%; 5d=-4.56%; 20d=-6.15% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=25.05; 1d=-0.75%; 5d=-5.44%; 20d=-9.34% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=433.00; 1d=-1.64%; 5d=-6.60%; 20d=-1.37% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=34.7; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.51; 2Y=4.24; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 跨层分歧信息有限，后续需补充更多波动与事件市场数据。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：有效交易信号不足，使用保守基准分布。
- 1月：有效交易信号不足，使用保守基准分布。

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1月 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| EWH price trend | close=21.33; 1d=+0.23%; 5d=-1.48%; 20d=-9.04% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=23.72; 1d=-3.50%; 5d=-9.47%; 20d=-20.03% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=102.90; 1d=-1.91%; 5d=-6.62%; 20d=-18.24% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [MOVE Index (MOVE) - MacroMicro](https://en.macromicro.me/charts/35584/us-treasury-move-index)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：The Merrill Lynch Option Volatility Estimate (MOVE) Index reflects the level of volatility in U.S. Treasury futures. The index is considered a proxy for term premiums of U.S. Tr...

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [NDAQ Implied Volatility Chart Nasdaq - MarketChameleon.com](https://marketchameleon.com/Overview/NDAQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：View volatility charts for Nasdaq (NDAQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the interactive...

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days out or more. IV is a forward looking prediction of the likelihood...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [United States - ICE BofA US High Yield Index Option-Adjusted Spread ...](https://tradingeconomics.com/united-states/bofa-merrill-lynch-us-high-yield-option-adjusted-spread-fed-data.html)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：United States - ICE BofA US High Yield Index Option-Adjusted Spread was 2.78% in June of 2026, according to the United States Federal Reserve. Historically, United States - ICE...

- [US - ICE BofA US High Yield Index Option-Adjusted Spread](https://en.macromicro.me/series/78167/us-ice-bofa-us-high-yield-index-option-adjusted-spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：Zoom 6m YTD 1y 3y 5y All All US - ICE BofA US High Yield Index Option-Adjusted Spread 2000 2005 2010 2015 2020 2025 0 5 10 15 20 25

- [QQQ Options - Live IV, Flow, Greeks & Analysis / ImpliedOptions ...](https://impliedoptions.com/ticker/qqq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Trade QQQ options with real-time implied volatility, IV rank, options flow, and Greeks. Analyze QQQ calls and puts with our free calculator and strategy builder.

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [QQQ: Invesco QQQ Trust Option Overview / OptionCharts](https://optioncharts.io/options/QQQ)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View comprehensive QQQ options with our latest charts on volume, open interest, max pain, and implied volatility.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Current Values - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index?idx=nk225)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Current Values Nikkei calculates and publishes various types of the indexes such as the "Nikkei Stock Average (Nikkei 225)" which is known as a representative Japanese stock mar...

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

- [1 USD to JPY - US Dollars to Japanese Yen Exchange Rate - Xe](https://www.xe.com/en/currencyconverter/convert/?Amount=1&From=USD&To=JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest 1 US Dollar to Japanese Yen rate for FREE with the original Universal Currency Converter. Set rate alerts for USD to JPY and learn more about US Dollars and Japan...

- [USD to JPY - US Dollar to Japanese Yen Conversion - Exchange Rates](https://www.exchange-rates.org/converter/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Use the USD to JPY currency converter at Exchange-Rates.org for accurate and up-to-date exchange rates. Easily convert US Dollars to Japanese Yen with real-time data.

- [Live US Dollar to Yens Exchange Rate - $ 1 USD/JPY Today](https://usd.currencyrate.today/jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest and best $1 US Dollar to Yens rate for FREE. USD/JPY - Live exchange rates, banks, historical data & currency charts.

### 数据来源 (Data Sources)
- EdgarProvider
- FearGreedProvider
- USTreasuryProvider
- WebSearchProvider
- YFinanceProvider
- YahooPriceProvider

> *以上分析仅为市场数据概率模型输出，不构成投资建议。*

**标签**: `#trading`, `#qdii`, `#nasdaq100`, `#us-stocks`, `#japan-stocks`, `#hongkong-stocks`

---

<a id="item-2"></a>
## [美联储发布 FOMC 货币政策声明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm) ⭐️ 9.0/10

2026 年 6 月 17 日，美联储发布了最新的联邦公开市场委员会（FOMC）声明，该声明通常会宣布联邦基金利率调整、前瞻指引和经济展望。 FOMC 声明可能通过设定对美国利率的预期而显著影响全球金融市场，波及外汇、债券收益率和股市。 尽管 6 月 17 日声明的具体内容未提供，但 FOMC 声明通常包括联邦基金利率决定、投票详情（包括反对票）及经济状况评估。

rss · Federal Reserve Press Releases · Jun 17, 18:00

**背景**: 联邦储备系统（美联储）是美国的中央银行，成立于 1913 年。联邦公开市场委员会（FOMC）通过调整联邦基金利率来实现充分就业和物价稳定。FOMC 由 7 名理事会成员和 12 家地区联邦储备银行行长中的 5 名投票成员组成，行长们轮流投票。委员会每年召开八次会议，每次会后发布声明，解释政策决定和经济展望。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Reserve">Federal Reserve</a></li>
<li><a href="https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm">Federal Reserve Board - Federal Reserve issues FOMC statement</a></li>
<li><a href="https://www.investing.com/economic-calendar/fomc-statement-398">US Federal Open Market Committee (FOMC) Statement</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#currency`, `#bonds`, `#global-markets`

---

<a id="item-3"></a>
## [联合国欢迎黎巴嫩停火；人权专家呼吁追究伊朗责任](https://news.un.org/feed/view/en/story/2026/06/1167768) ⭐️ 8.0/10

联合国对据报道于 2026 年 6 月 1 日星期五达成的以色列与真主党新停火协议表示欢迎，同时警告称平民仍因持续的不安全局势而逃离。 停火缓解了中东的直接军事紧张局势，降低了能源市场和航运供应链的风险，但鉴于以往的违规行为和持续的区域不稳定，停火能否持久仍不确定；同时，追究伊朗责任的呼吁在更广泛的伊朗战争背景下增加了外交压力。 根据报道的条款，以色列承诺不攻击贝鲁特南郊，真主党誓言不攻击以色列，但平民仍在逃离，联合国警告安全局势持续不稳；此前在 2026 年 3 月，上一次停火在伊朗战争背景下破裂。

rss · UN News · Jun 19, 12:00

**背景**: 真主党是伊朗支持的黎巴嫩什叶派伊斯兰组织，自 1982 年成立以来一直与以色列冲突。2023 年 10 月起跨境交火升级，引发 2024 年黎巴嫩战争。2024 年 11 月的停火屡遭违反，于 2026 年 3 月伊朗最高领袖遇刺后破裂。2026 年 6 月 1 日的新停火旨在停止敌对行动，而联合国驻黎巴嫩临时部队（UNIFIL）自 1978 年起根据历次授权在黎南部开展维和行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Israel–Lebanon_ceasefire">2026 Israel–Lebanon ceasefire - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Interim_Force_in_Lebanon">United Nations Interim Force in Lebanon - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`, `#energy`

---

<a id="item-4"></a>
## [IAEA 欢迎美伊停战备忘录，愿提供核核查协助](https://news.un.org/feed/view/en/story/2026/06/1167748) ⭐️ 8.0/10

国际原子能机构总干事欢迎美伊签署初步备忘录以结束战争，并提议协助伊朗核计划核查工作。 此举可能缓和军事冲突，为重启核协议、解除制裁铺路，并稳定全球石油市场。 该备忘录为初步性文件，具体核查步骤尚未商定；IAEA 的技术参与对双方建立信任至关重要。

rss · UN News · Jun 18, 12:00

**背景**: IAEA 是推动和平利用核能并监督核不扩散的联合国机构。2026 年美伊因伊朗核问题爆发战争，战事耗费巨大，美军截至 5 月已花费近 290 亿美元。IAEA 长期监控伊朗核活动，曾在伊核协议中发挥关键作用，如今其核查职能成为和平协议的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/International_Atomic_Energy_Agency_(IAEA)">International Atomic Energy Agency (IAEA)</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Iran_war">2026 Iran war - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#iran`, `#united-states`, `#energy`

---

<a id="item-5"></a>
## [美联储发布 6 月 FOMC 经济预测](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm) ⭐️ 8.0/10

美联储公布了 6 月 16-17 日 FOMC 会议的经济预测，包括利率预期的‘点阵图’以及对 GDP、失业率和通胀的预测。 这些预测是货币政策预期的关键依据，直接影响利率市场、美元和全球风险资产；任何鹰派或鸽派转向都可能引发市场大幅重定价。 预测包括‘点阵图’，展示各委员对本年度、未来两年及长期联邦基金利率的预期，揭示委员会的政策立场。

rss · Federal Reserve Press Releases · Jun 17, 18:00

**背景**: 联邦公开市场委员会（FOMC）是美国联邦储备系统的货币政策制定机构，每年召开八次会议设定联邦基金利率目标。会后一年四次发布经济预测，包含‘点阵图’（显示每位委员对未来利率路径的评估）以及对 GDP 增长、失业率和通胀的预测。市场密切关注这些预测，以获取未来政策收紧或宽松的信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.federalreserve.gov/monetarypolicy/fomc.htm">The Fed - Federal Open Market Committee</a></li>
<li><a href="https://www.investing.com/economic-calendar/fomc-economic-projections-1061">U.S. Federal Reserve (Fed) Economic Projections</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federal_Open_Market_Committee">Federal Open Market Committee</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#bonds`, `#currencies`, `#global-markets`

---

<a id="item-6"></a>
## [联合国安理会警告乌克兰面临“危险升级循环”](https://news.un.org/feed/view/en/story/2026/06/1167775) ⭐️ 7.0/10

联合国助理秘书长穆罕默德·哈立德·希亚里和人道协调厅危机应对主任埃德姆·沃索努周一在安理会通报，周末乌克兰发生的致命无人机和导弹袭击表明这场四年战争已陷入“危险升级循环”。 安理会的通报突显国际社会对乌克兰局势深化的担忧，可能影响西方军事援助、制裁政策及人道主义应对决策，直接关系到平民的生死存亡。 尽管安理会因俄罗斯否决权而瘫痪，但通报强调成员国的外交和资金决策直接影响平民生存，人道协调厅强调了紧急人道准入和保护的迫切性。

rss · UN News · Jun 22, 12:00

**背景**: 联合国安理会负责维护国际和平，由 15 个成员国组成，五个常任理事国（俄、中、美、英、法）拥有否决权。自 2022 年 2 月俄罗斯全面入侵乌克兰以来，安理会基本陷入僵局，仅能举行听证会。人道协调厅负责协调人道主义响应，乌克兰有数百万流离失所者急需援助。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council">United Nations Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Office_for_the_Coordination_of_Humanitarian_Affairs">UN Office for the Coordination of Humanitarian Affairs</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#russia-ukraine`, `#military-risk`, `#europe`, `#geopolitics`

---

<a id="item-7"></a>
## [联合国安理会警告苏丹奥贝德面临大规模暴行风险](https://news.un.org/feed/view/en/story/2026/06/1167773) ⭐️ 7.0/10

联合国安理会对苏丹快速支援部队在奥贝德周边的大规模军事集结表示震惊，警告该市可能遭到地面进攻，并要求快速支援部队立即停止攻击。 这一警告标志着苏丹冲突升级，可能引发国际外交行动、制裁讨论或人道主义行动，对地区稳定和全球防止暴行的准则产生更广泛影响。 奥贝德是北科尔多凡州首府，曾被快速支援部队围困近两年，直到 2025 年 2 月；该部队有大规模暴行的记录，包括在达尔富尔的种族灭绝，最近经过 18 个月围攻占领了法希尔。

rss · UN News · Jun 20, 12:00

**背景**: 快速支援部队是源自金戈威德民兵的苏丹准军事组织，自 2023 年 4 月起与苏丹军队争夺国家控制权，被指控犯有种族灭绝和族裔清洗，已建立平行政府，依赖金矿和外国支持。奥贝德是北科尔多凡州的战略贸易枢纽，其陷落可能加剧人道危机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167773">Sudan: Security Council warns of mass atrocity risk in El Obeid | UN News</a></li>
<li><a href="https://www.theglobeandmail.com/world/article-mass-atrocities-looming-in-another-sudanese-city-un-says/">Mass atrocities looming in another Sudanese city, UN says - The Globe and Mail</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rapid_Support_Forces_(Sudan)">Rapid Support Forces (Sudan)</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`

---

<a id="item-8"></a>
## [联合国维护黎巴嫩维和人员行动自由](https://news.un.org/feed/view/en/story/2026/06/1167758) ⭐️ 7.0/10

联合国再次要求驻黎巴嫩临时部队（UNIFIL）维和人员在黎巴嫩南部享有不受限制的行动自由，此时正值美伊达成临时协议之后。 这凸显了 UNIFIL 任务可能受阻的风险，可能破坏对安全安排的监督，并在美伊外交接触的关键时刻影响地区稳定。 联合国安理会第 1701 号决议保障联黎部队的无阻碍通行；无法确保这一点将妨碍合规核查和可信报告。据报道，美伊临时协议为谅解备忘录而非正式和平条约，其强制执行力及对真主党的影响存疑。

rss · UN News · Jun 18, 12:00

**背景**: 联黎部队于 1978 年成立，2006 年战争后依据第 1701 号决议得到加强，负责监督以色列与真主党停火并支持黎巴嫩武装部队在南部部署。其行动自由此前曾受挑战，2026 年发生维和人员被拘事件。2026 年黎巴嫩战争加剧紧张，以军在南部采取军事行动并威胁建立永久安全区。2026 年 6 月美伊宣布达成谅解备忘录以结束更大范围敌对，但细节尚未明朗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167758">UN upholds freedom of movement for peacekeepers in Lebanon | UN News</a></li>
<li><a href="https://www.jurist.org/news/2026/06/un-upholds-freedom-of-movement-for-peacekeepers-in-lebanon-amidst-ongoing-regional-hostilities/">UN upholds freedom of movement for peacekeepers in Lebanon amidst ongoing regional hostilities - JURIST - News</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Interim_Force_in_Lebanon">United Nations Interim Force in Lebanon - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#iran`, `#united-states`

---

<a id="item-9"></a>
## [皮耶罗·奇波洛内：央行货币在国家主权中的角色](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260619~53145e5a0b.en.html) ⭐️ 7.0/10

欧洲央行执行委员会委员皮耶罗·奇波洛内发表演讲，强调央行货币对国家主权的重要性，释放了欧洲央行对数字欧元及相关货币基础设施的立场信号。 该演讲突显了欧洲央行致力于将数字欧元作为保护货币主权的工具，以应对私人数字货币和外国央行数字货币的兴起，这可能影响欧元的国际角色和金融稳定。 数字欧元正处于高级准备阶段，可能在 2029 年前发行，2027 年开始测试，但取决于欧盟立法。奇波洛内的演讲很可能涉及隐私、离线功能以及与现金的互补等设计特征。

rss · ECB Press Releases · Jun 19, 10:15

**背景**: 数字欧元是欧洲央行于 2021 年启动的央行数字货币项目。货币主权是指国家对货币和货币政策的排他性控制权。欧洲央行认为，数字欧元将维护央行货币在数字时代的角色，避免依赖私人或外国数字支付系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_euro">Digital euro</a></li>
<li><a href="https://www.ecb.europa.eu/euro/digital_euro/html/index.en.html">Digital euro - European Central Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/Monetary_sovereignty">Monetary sovereignty</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#europe`, `#macroeconomics`, `#financial-stability`, `#digital-currency`

---

<a id="item-10"></a>
## [欧洲央行工资追踪器显示 2026 年工资压力稳定](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260617~79dfc49802.en.html) ⭐️ 7.0/10

欧洲央行最新发布的工资追踪数据显示，2026 年谈判工资增长预计将保持稳定，表明欧元区工资压力持续正常化。 稳定的工资压力意味着劳动力成本驱动的通胀受到控制，这可能降低进一步收紧货币政策的紧迫性，从而可能支撑欧元区债券和股市，同时对欧元构成压力。 欧洲央行工资追踪器涵盖了集体谈判达成的一次性支付（如通胀补偿奖金），比传统指标更精确。数据显示，在经历一段高增长期后，2026 年谈判工资压力正趋于平稳。

rss · ECB Press Releases · Jun 17, 08:00

**背景**: 欧洲央行于 2024 年推出工资追踪器，旨在实时监测后疫情时期通胀飙升和劳动力市场紧张背景下的谈判工资动态。谈判工资是劳动力成本的关键组成部分，也是决策者评估通胀能否回归 2%目标的重要依据。该追踪器补充了欧洲央行谈判工资指标等官方数据，有助于平滑因协议更新不规律造成的波动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://data.ecb.europa.eu/data/datasets/EWT/data-information">ECB Wage Tracker - EWT | ECB Data Portal</a></li>
<li><a href="https://www.ecb.europa.eu/press/blog/date/2024/html/ecbblog20240523~1964e193b7.en.html">Tracking euro area wages in exceptional times</a></li>
<li><a href="https://www.lapost.com/ecb-sees-further-signs-of-easing-wage-pressures">LA Post: ECB sees further signs of easing wage pressures - The Los...</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#bonds`, `#currency`

---

<a id="item-11"></a>
## [欧洲央行莱恩就欧元区经济前景发表讲话](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260616~8076dabd2c.en.pdf) ⭐️ 7.0/10

欧洲央行首席经济学家菲利普·莱恩就欧元区经济前景发表讲话，可能透露央行对增长、通胀和货币政策方向的最新评估。 莱恩的言论可能影响市场对利率决策、债券收益率和欧元汇率的预期，投资者密切关注其讲话中关于政策正常化或经济风险基调的任何变化。 该讲话已在欧洲央行官网发布，但现有摘要未详述具体内容；任何关于降息步伐或通胀前景的信号都可能对市场产生较大影响。

rss · ECB Press Releases · Jun 16, 13:10

**背景**: 菲利普·莱恩自 2019 年起担任欧洲央行首席经济学家，在央行经济分析中发挥关键作用。欧洲央行决策者的定期讲话因能透露未来货币政策线索而备受关注，尤其是在 2024 年中一系列加息后开始降息的背景下。欧元区经济面临增长乏力和服务业通胀顽固的挑战，因此莱恩的评估对判断政策路径至关重要。

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`, `#bonds`

---

<a id="item-12"></a>
## [联合国儿基会：加沙停火后仍有 265 名儿童丧生](https://news.un.org/feed/view/en/story/2026/06/1167760) ⭐️ 6.0/10

联合国儿童基金会报告称，自 2025 年 10 月宣布停火以来，加沙仍有 265 名巴勒斯坦儿童丧生，凸显安全局势恶化。 持续的儿童伤亡表明停火协议脆弱且安全环境依然危险，可能破坏外交进展并使该地区人道主义危机恶化。 联合国儿童基金会的警报使用了‘打个喷嚏都可能被枪杀’的严厉警告，强调儿童面临的普遍威胁；自 2025 年 10 月停火以来，尽管外交努力仍在进行，仍有 265 名儿童丧生。

rss · UN News · Jun 19, 12:00

**背景**: 联合国儿童基金会是联合国下属的儿童救助机构。加沙地带人口超过 200 万，近半数为儿童，常年遭受冲突与封锁。2025 年 10 月以色列与哈马斯达成停火，随后联合国安理会于 2025 年 11 月通过第 2803 号决议，规划过渡治理安排；但零星暴力与不安全状况持续，导致伤亡不断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNICEF">UNICEF</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gaza_Strip">Gaza Strip</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ceasefire_Agreement">Ceasefire Agreement</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#geopolitics`, `#military-risk`, `#diplomacy`

---

<a id="item-13"></a>
## [联合国特使警告利比亚政治窗口收窄 威胁石油稳定](https://news.un.org/feed/view/en/story/2026/06/1167757) ⭐️ 6.0/10

联合国利比亚问题特使警告，尽管政治进程近期重获势头，但采取果断行动的窗口正在缩小，停滞风险可能危及稳定和石油产量。 利比亚的政治不稳定直接影响其近期创十年新高的每日 143 万桶石油产量，停摆可能扰乱全球石油市场并加剧区域安全挑战。 警告中未提及特使姓名，但前任特使巴蒂利曾因僵局辞职；声明暗示国际耐心渐失，选举仍无时间表。

rss · UN News · Jun 18, 12:00

**背景**: 自 2011 年卡扎菲政权被推翻以来，利比亚陷入的黎波里与东部政府之间的分裂，联合国调解多次陷入僵局。作为欧佩克成员国，石油收入对国家运转至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Support_Mission_in_Libya">United Nations Support Mission in Libya - Wikipedia</a></li>
<li><a href="https://businessfront.com/libya-oil-output-hits/">Libya oil output hits 1.4 million bdp, highest in over... - Businessfront</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#middle-east`, `#sovereign-risk`

---

<a id="item-14"></a>
## [安理会讨论停火下加沙恶化的人道危机](https://news.un.org/feed/view/en/story/2026/06/1167750) ⭐️ 6.0/10

应十个非常任理事国请求，联合国安理会就加沙日益恶化的人道局势举行会议。联合国救援负责人汤姆·弗莱彻通报称，自 2025 年 10 月停火以来，已有近 1000 名巴勒斯坦人被杀，大多数加沙人仍流离失所，并称当前进展“只是最低限度”。 此次会议凸显加沙停火的持续脆弱性和冲突升级风险，可能进一步破坏中东稳定并冲击全球能源市场。安理会的关注表明国际担忧，但也反映出因大国否决权而执行和平能力有限。 自 2025 年 10 月以来的停火“有名无实”，暴力仍在持续；会议期间未通过新的具体决议或采取行动。会议由十个非常任理事国发起，突显在常任理事国分歧时他们在推动议题上的作用。

rss · UN News · Jun 18, 12:00

**背景**: 联合国安理会负责维护国际和平与安全，由 15 个成员组成：5 个常任理事国（美、英、法、俄、中）拥有否决权，10 个非常任理事国任期两年。加沙战争始于 2023 年，于 2025 年 10 月达成停火，但违反行为持续。汤姆·弗莱彻自 2024 年起担任联合国主管人道主义事务的副秘书长兼紧急救济协调员，领导人道协调厅。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tom_Fletcher_(diplomat)">Tom Fletcher (diplomat) - Wikipedia</a></li>
<li><a href="https://www.unocha.org/tom-fletcher">Tom Fletcher - OCHA</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-15"></a>
## [联合国人权高专警告民兵逼近苏丹 El Obeid 恐引发暴行](https://news.un.org/feed/view/en/story/2026/06/1167752) ⭐️ 6.0/10

联合国人权事务高级专员 Volker Türk 紧急警告，Rapid Support Forces (RSF) 即将对北科尔多凡州首府 El Obeid 发动攻势，可能导致严重国际罪行，并加剧已灾难性的人道主义危机。 此次警告可能促使联合国安理会采取行动或地区调解，提升国际社会对苏丹内战和潜在暴行的关注，影响区域稳定，但对市场直接冲击有限。 RSF 被指控犯下种族灭绝和战争罪；El Obeid 是战略要地和重要人道主义枢纽，其陷落将加剧流离失所和苦难。

rss · UN News · Jun 18, 12:00

**背景**: 自 2023 年 4 月以来，苏丹军队与准军事组织 Rapid Support Forces (RSF) 之间爆发内战。RSF 源自达尔富尔的金戈威德民兵，被指控犯下包括种族清洗和性暴力在内的大规模暴行，并据称得到阿拉伯联合酋长国的支持。冲突已造成数万人死亡，数百万人流离失所，引发严重人道主义危机。2025 年 RSF 攻占法希尔后，现正逼近 El Obeid。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_High_Commissioner_for_Human_Rights">UN High Commissioner for Human Rights</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rapid_Support_Forces_(Sudan)">Rapid Support Forces (Sudan)</a></li>
<li><a href="https://www.bbc.com/news/articles/cjel2nn22z9o">Sudan war: A simple guide to what is happening</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`

---

<a id="item-16"></a>
## [拉加德出席欧洲议会经济货币听证会](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260622~b060a27b78.en.html) ⭐️ 6.0/10

欧洲央行行长克里斯蒂娜·拉加德出席欧洲议会经济与货币事务委员会的常规听证会，讨论了欧元区的经济前景和货币政策立场。 她的讲话可能预示未来利率调整，影响借贷成本、债券市场和欧元汇率，是投资者和政策制定者的重要事件。 听证会于 2026 年 6 月 22 日举行。市场参与者将仔细分析她对通胀风险、增长预测以及是否偏离此前指引的措辞。

rss · ECB Press Releases · Jun 22, 13:00

**背景**: 欧洲央行是欧元区的中央银行，负责维护价格稳定。经济与货币事务委员会监督欧盟的经济与货币政策，欧洲央行行长定期作证以确保民主问责。如果关键政策基调变化，这些听证会可能引发市场波动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_Parliament_Committee_on_Economic_and_Monetary_Affairs">European Parliament Committee on Economic and Monetary Affairs - Wikipedia</a></li>
<li><a href="https://european-union.europa.eu/institutions-law-budget/institutions-and-bodies/search-all-eu-institutions-and-bodies/european-central-bank-ecb_en">European Central Bank (ECB)</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`, `#financial-stability`

---