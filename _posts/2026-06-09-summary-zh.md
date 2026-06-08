---
layout: default
title: "Horizon Summary: 2026-06-09 (ZH)"
date: 2026-06-09
lang: zh
---

> From 38 items, 7 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [美以空袭伊朗，霍尔木兹海峡成为全球冲突热点](#item-2) ⭐️ 10.0/10
3. [联合国在叙利亚发现未申报化武，关联 2013 年古塔袭击](#item-3) ⭐️ 9.0/10
4. [联合国安理会警告乌克兰人道主义伤亡恶化](#item-4) ⭐️ 7.0/10
5. [联合国人权高专：美国制裁致古巴儿童死亡](#item-5) ⭐️ 7.0/10
6. [联合国为黎巴嫩危机追加 3.315 亿美元援助呼吁](#item-6) ⭐️ 6.0/10
7. [欧洲央行报告 2025 年欧元国际角色温和上升](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 8, 22:49

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
| QDII Nasdaq 100 Proxy | US | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | high |
| US Mega Cap Basket | US | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | high |
| Japan Equity Basket | JP | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| QQQ price trend | close=716.07; 1d=+1.56%; 5d=-3.59%; 20d=+0.68% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29414.26; 1d=+1.58%; 5d=-3.60%; 20d=+0.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29369.50; 1d=+1.18%; 5d=-3.92%; 20d=+0.13% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=1.9%; implied_move=0.1%; put/call OI=1.3332686922960497 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.56; 2Y=4.15; 10Y-2Y=0.40999999999999925 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=40.1; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| QQQ price trend | close=716.07; 1d=+1.56%; 5d=-3.59%; 20d=+0.68% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29414.26; 1d=+1.58%; 5d=-3.60%; 20d=+0.61% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29369.50; 1d=+1.18%; 5d=-3.92%; 20d=+0.13% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| GOOGL price trend | close=363.31; 1d=-1.42%; 5d=-3.47%; 20d=-9.35% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=208.64; 1d=+1.73%; 5d=-6.90%; 20d=-2.94% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=411.74; 1d=-1.18%; 5d=-10.59%; 20d=-0.60% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=408.95; 1d=+4.59%; 5d=-1.67%; 20d=-4.53% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=245.22; 1d=-0.33%; 5d=-6.14%; 20d=-10.07% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=585.39; 1d=-1.28%; 5d=-2.51%; 20d=-3.98% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| AAPL options surface | ATM IV=5.9%; implied_move=0.3%; put/call OI=0.4170731304045899 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=3.7%; implied_move=0.1%; put/call OI=0.8882147578212385 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=5.8%; implied_move=0.3%; put/call OI=0.3502470603946607 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=6.9%; implied_move=0.2%; put/call OI=0.7898972228296524 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=7.3%; implied_move=0.3%; put/call OI=0.5393078512396694 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=12.1%; implied_move=0.6%; put/call OI=0.6331103187148476 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.56; 2Y=4.15; 10Y-2Y=0.40999999999999925 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=40.1; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| AAPL insider filings | recent Form4 count=587 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| MSFT insider filings | recent Form4 count=726 | 内部人交易节奏可作为估值温度辅助校验信号。 |

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
| GOOGL price trend | close=363.31; 1d=-1.42%; 5d=-3.47%; 20d=-9.35% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=208.64; 1d=+1.73%; 5d=-6.90%; 20d=-2.94% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=411.74; 1d=-1.18%; 5d=-10.59%; 20d=-0.60% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 6758.T price trend | close=3508.00; 1d=-1.43%; 5d=-0.96%; 20d=+4.03% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=91.95; 1d=+1.36%; 5d=-1.05%; 20d=-0.29% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2822.50; 1d=-0.96%; 5d=-2.86%; 20d=-1.66% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=74980.00; 1d=-3.96%; 5d=-6.53%; 20d=-8.89% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=55020.00; 1d=-7.45%; 5d=+3.69%; 20d=+5.65% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6976.00; 1d=-6.06%; 5d=-18.32%; 20d=+21.47% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.56; 2Y=4.15; 10Y-2Y=0.40999999999999925 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=40.1; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 6758.T price trend | close=3508.00; 1d=-1.43%; 5d=-0.96%; 20d=+4.03% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=91.95; 1d=+1.36%; 5d=-1.05%; 20d=-0.29% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2822.50; 1d=-0.96%; 5d=-2.86%; 20d=-1.66% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 0700.HK price trend | close=446.40; 1d=-1.50%; 5d=+2.39%; 20d=-4.20% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=34.68; 1d=-0.20%; 5d=-1.87%; 20d=-6.87% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=118.80; 1d=-2.94%; 5d=-3.26%; 20d=-14.53% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=27.38; 1d=-1.51%; 5d=-4.67%; 20d=-13.57% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=21.85; 1d=+0.14%; 5d=-5.04%; 20d=-10.01% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=76.25; 1d=-4.63%; 5d=-2.56%; 20d=-9.28% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=40.1; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.56; 2Y=4.15; 10Y-2Y=0.40999999999999925 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| 0700.HK price trend | close=446.40; 1d=-1.50%; 5d=+2.39%; 20d=-4.20% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=34.68; 1d=-0.20%; 5d=-1.87%; 20d=-6.87% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=118.80; 1d=-2.94%; 5d=-3.26%; 20d=-14.53% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [NASDAQ 100 Index Volatility History & Chart Since 1985](https://wallstreetnumbers.com/indexes/ndx/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Get all-time historical data of NASDAQ 100 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Volatility Term Structure chart plots the at-the-money implied volatility across expirations, which are an invaluable tool in determining options strategies based on anticipated...

- [Nasdaq-100 Volatility Index (VOLQ)](https://www.nasdaq.com/market-activity/index/volq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Find the latest information on Nasdaq-100 Volatility Index (VOLQ), including data, charts, related news, and more from Nasdaq.com

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [Move Index Chart - Barchart.com](https://www.barchart.com/stocks/quotes/$MOVE/interactive-chart)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Customizable interactive chart for Move Index with latest real-time price quote, charts, latest news, technical analysis and opinions.

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [QQQ Options - Live IV, Flow, Greeks & Analysis / ImpliedOptions ...](https://impliedoptions.com/ticker/qqq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Trade QQQ options with real-time implied volatility, IV rank, options flow, and Greeks. Analyze QQQ calls and puts with our free calculator and strategy builder.

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [BAMLH0A0HYM2: US High Yield OAS Daily Data - eco3min.fr](https://eco3min.fr/en/credit-spreads-recession-risk-dataset/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：BAMLH0A0HYM2 is the ICE BofA US High Yield Index Option-Adjusted Spread — the daily market-priced premium that below-investment-grade US corporate bonds pay over equivalent-matu...

- [USD/JPY Currency Exchange Rate & News - Google Finance](https://www.google.com/finance/beta/quote/USD-JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：The United States dollar is the official currency of the United States and several other countries. The Coinage Act of 1792 introduced the U.S. dollar at par with the Spanish si...

- [Valuta EX - Currency Converter / Real-Time Exchange Rates](https://valuta.exchange/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

- [Currency Conversion Calculator / Currency Converter - Forbes Advisor](https://www.forbes.com/advisor/money-transfer/currency-converter/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Use our currency converter to get live exchange rates for over 200 currencies, including cryptocurrencies. Convert major global currencies now.

- [iShares MSCI Japan ETF (EWJ) Price, Holdings, & News](https://www.marketbeat.com/stocks/NYSEARCA/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Should You Buy or Sell iShares MSCI Japan ETF Stock? Get The Latest EWJ Stock Price, Constituents List, Holdings Data, and Headlines at MarketBeat.

- [EWJ / iShares MSCI Japan ETF Overview / MarketWatch](https://www.marketwatch.com/investing/fund/ewj)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ / A complete iShares MSCI Japan ETF exchange traded fund overview by MarketWatch. View the latest ETF prices and news for better ETF investing.

- [EWJ ETF Stock Price & Overview](https://stockanalysis.com/etf/ewj/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Get a real-time stock price for the EWJ ETF (iShares MSCI Japan ETF) with an overview of various metrics and statistics.

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
## [美以空袭伊朗，霍尔木兹海峡成为全球冲突热点](https://news.un.org/feed/view/en/story/2026/06/1167648) ⭐️ 10.0/10

2026 年 2 月 28 日，美国和以色列对伊朗发动军事打击，引发严重地缘政治危机，一举将霍尔木兹海峡变为全球冲突热点。 霍尔木兹海峡是全球石油和液化天然气运输的关键咽喉要道，超过 20%的全球石油运输经过该海峡。打击行动可能中断能源供应，引发市场立即重新定价，并威胁依赖进口地区的粮食安全。 伊朗以导弹袭击以色列和美国盟友阿拉伯国家作为回应，并实际关闭了海峡，扰乱了全球 20%的石油供应。自 4 月 7 日起，双方开始了为期两周的有条件停火，但危机依然严重。

rss · UN News · Jun 5, 12:00

**背景**: 霍尔木兹海峡是连接波斯湾与阿曼湾的狭窄水道，对中东主要产油国的石油和液化天然气出口至关重要。长期以来，它一直是地区紧张局势中的战略热点。美国和以色列一直反对伊朗的核计划和地区影响力，最终导致此次军事升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Iran_war">2026 Iran war - Wikipedia</a></li>
<li><a href="https://www.iea.org/about/oil-security-and-emergency-response/strait-of-hormuz">Strait of Hormuz - About - IEA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Economic_impact_of_the_2026_Iran_war">Economic impact of the 2026 Iran war - Wikipedia</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`, `#iran`

---

<a id="item-3"></a>
## [联合国在叙利亚发现未申报化武，关联 2013 年古塔袭击](https://news.un.org/feed/view/en/story/2026/06/1167652) ⭐️ 9.0/10

联合国化学武器核查人员在叙利亚发现大量未申报的化学武器，其中包括与 2013 年古塔化学攻击所用同类型的火箭弹。联合国裁军事务高级官员称此为‘重大发现’。 这一发现表明叙利亚未遵守《化学武器公约》，可能引发联合国安理会行动、新制裁或军事回应，加剧地缘政治紧张，影响区域稳定和能源市场。 此事引发对叙利亚申报完整性的严重关切，2017 年汗谢洪等袭击早已暗示存在未披露库存。禁化武组织（OPCW）长期质疑叙利亚未完全履约。

rss · UN News · Jun 4, 12:00

**背景**: 2013 年 8 月，叙利亚古塔地区遭遇沙林毒气袭击，造成数百人死亡，引发国际谴责。叙利亚随后加入《化学武器公约》，在禁化武组织与联合国联合监督下，于 2014 年销毁了所有申报的化武。但 2017 年和 2018 年的化武袭击表明可能仍有未申报武器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167652">Undeclared chemical weapons found in Syria, including type ... - UN News</a></li>
<li><a href="https://en.wikipedia.org/wiki/2013_Ghouta_chemical_attack">2013 Ghouta chemical attack</a></li>
<li><a href="https://www.opcw.org/media-centre/featured-topics/opcw-and-syria">Syria and the OPCW</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`, `#sanctions`

---

<a id="item-4"></a>
## [联合国安理会警告乌克兰人道主义伤亡恶化](https://news.un.org/feed/view/en/story/2026/06/1167674) ⭐️ 7.0/10

联合国政治事务副秘书长罗斯玛丽·迪卡洛在安理会通报称，乌克兰战争已达到自 2022 年全面入侵以来最致命的程度，大规模空袭导致平民伤亡不断攀升。 人道主义危机加剧预示着冲突可能进一步升级，或将扰乱全球能源和粮食市场，并可能引发国际社会采取更多外交措施或调整制裁。 通报指出，近几个月发生了冲突以来最广泛的空袭，前线两侧均出现伤亡，但未公布具体数字或宣布新政策措施。

rss · UN News · Jun 8, 12:00

**背景**: 联合国安理会负责维护国际和平与安全。政治事务副秘书长目前由 2018 年任命的罗斯玛丽·迪卡洛担任，她领导政治和建设和平事务部，定期向安理会通报冲突情况。俄罗斯于 2022 年 2 月开始全面入侵乌克兰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council">United Nations Security Council - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Department_of_Political_and_Peacebuilding_Affairs">United Nations Department of Political and Peacebuilding Affairs</a></li>
<li><a href="https://main.un.org/securitycouncil/en">Homepage | Security Council</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#russia-ukraine`, `#military-risk`, `#europe`

---

<a id="item-5"></a>
## [联合国人权高专：美国制裁致古巴儿童死亡](https://news.un.org/feed/view/en/story/2026/06/1167671) ⭐️ 7.0/10

联合国人权事务高级专员福尔克尔·蒂尔克警告，美国制裁导致古巴药品严重短缺，儿童因此死亡，并敦促美国立即解除封锁。 联合国人权事务最高官员的这一严厉警告显著加大了国际社会对美国重新考虑古巴封锁的压力，可能影响外交讨论和政策审议，同时突显全球对制裁人道主义后果日益增长的担忧。 该声明直接将美国持续近 60 年的封锁与儿童死亡率联系起来，强调医生无法获取必需药品。始于 1962 年的美国禁运是全球最全面、持续时间最长的贸易制裁之一。

rss · UN News · Jun 8, 12:00

**背景**: 美国对古巴的禁运自 1960 年起逐步实施，并于 1962 年正式确立，广泛限制了两国间的贸易、金融交易和旅行。古巴实行国家资助的全民医疗体系，严重依赖进口医疗物资，易受贸易限制影响。福尔克尔·蒂尔克自 2022 年 10 月起担任联合国人权事务高级专员，该职务负责就全球人权侵犯问题发表意见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_States_embargo_against_Cuba">United States embargo against Cuba - Wikipedia</a></li>
<li><a href="https://www.ohchr.org/en/about-us/high-commissioner/volker-turk">Volker Türk | OHCHR</a></li>
<li><a href="https://en.wikipedia.org/wiki/Healthcare_in_Cuba">Healthcare in Cuba - Wikipedia</a></li>

</ul>
</details>

**标签**: `#sanctions`, `#diplomacy`, `#united-states`, `#geopolitics`

---

<a id="item-6"></a>
## [联合国为黎巴嫩危机追加 3.315 亿美元援助呼吁](https://news.un.org/feed/view/en/story/2026/06/1167659) ⭐️ 6.0/10

联合国驻黎巴嫩机构呼吁额外筹集 3.315 亿美元，以帮助因真主党与以色列军队之间冲突升级而受影响的 140 万人，冲突已持续三个月。 该呼吁凸显了严重的人道主义压力和地区动荡风险，对能源市场以及黎巴嫩已违约的主权债务产生影响。 新的 3.315 亿美元要求是在现有人道主义资金基础上追加的，因为三个月前爆发致命暴力以来需求激增；真主党被许多国家列为恐怖组织，自 2026 年 3 月起被黎巴嫩政府禁止。

rss · UN News · Jun 5, 12:00

**背景**: 黎巴嫩自 2019 年以来深陷经济危机，于 2020 年 3 月首次主权债务违约。真主党是伊朗支持的什叶派伊斯兰军事和政治组织，在黎巴嫩拥有强大军力，与以色列的冲突时有升级。当前冲突始于 2026 年的一次致命事件，导致大面积流离失所和破坏。联合国已在黎巴嫩开展人道主义行动，但需求已超出资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah - Wikipedia</a></li>
<li><a href="https://www.euromesco.net/news/lebanon-announces-first-ever-default-on-countrys-sovereign-debt/">Lebanon announces first ever default on country’s sovereign debt ...</a></li>
<li><a href="https://www.cfr.org/backgrounders/what-hezbollah">What Is Hezbollah ? | Council on Foreign Relations</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#middle-east`, `#military-risk`, `#sovereign-risk`

---

<a id="item-7"></a>
## [欧洲央行报告 2025 年欧元国际角色温和上升](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260602~f941e87516.en.html) ⭐️ 6.0/10

欧洲央行年度报告显示，欧元在国际储备、外汇交易和债务发行中的份额在 2025 年略有上升，扭转了 2024 年的小幅下滑。 欧元国际角色的增强可能巩固其全球储备货币地位，减轻对美元的依赖，并影响欧元区借贷成本和汇率稳定。 欧元在全球官方储备中的份额微升至约 20%，国际债务证券中的份额保持稳定；但欧元在跨境支付中的使用仍远落后于美元。

rss · ECB Press Releases · Jun 2, 08:00

**背景**: 欧洲央行自 2015 年起发布欧元国际角色年度评估。全球金融体系由美元主导，欧元是第二大货币。地缘政治变化、贸易格局和央行储备多元化影响欧元地位。欧元份额在欧债危机和负利率期间曾下降，但自疫情以来逐步回升。

**标签**: `#central-bank`, `#macroeconomics`, `#currency`, `#global-markets`, `#europe`

---