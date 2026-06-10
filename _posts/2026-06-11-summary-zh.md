---
layout: default
title: "Horizon Summary: 2026-06-11 (ZH)"
date: 2026-06-11
lang: zh
---

> From 37 items, 8 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [美以打击使霍尔木兹海峡成全球冲突热点](#item-2) ⭐️ 10.0/10
3. [联合国安理会辩论中东问题，美伊停火脆弱](#item-3) ⭐️ 7.0/10
4. [提尔新空袭致 8 人死亡，联合国评估黎巴嫩损失超 3.65 亿美元](#item-4) ⭐️ 7.0/10
5. [联合国警告乌克兰战争达 2022 年以来最致命阶段](#item-5) ⭐️ 7.0/10
6. [无人机袭击破坏苏丹关键援助路线](#item-6) ⭐️ 6.0/10
7. [联合国人权负责人：美国制裁正导致古巴儿童死亡](#item-7) ⭐️ 6.0/10
8. [联合国发起 3.315 亿美元黎巴嫩危机援助呼吁](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 10, 22:53

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
| QQQ price trend | close=693.69; 1d=-2.00%; 5d=-6.79%; 20d=-1.92% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=28508.03; 1d=-1.98%; 5d=-6.75%; 20d=-1.92% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=28445.50; 1d=-2.31%; 5d=-7.14%; 20d=-2.48% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=17.7%; implied_move=0.5%; put/call OI=1.3193297237481723 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=27.5; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.55; 2Y=4.13; 10Y-2Y=0.41999999999999993 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| QQQ price trend | close=693.69; 1d=-2.00%; 5d=-6.79%; 20d=-1.92% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=28508.03; 1d=-1.98%; 5d=-6.75%; 20d=-1.92% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=28445.50; 1d=-2.31%; 5d=-7.14%; 20d=-2.48% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| AMZN price trend | close=238.00; 1d=-2.53%; 5d=-4.81%; 20d=-10.47% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=381.59; 1d=-3.80%; 5d=-9.94%; 20d=-11.96% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=291.58; 1d=+0.35%; 5d=-6.02%; 20d=-1.09% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=200.42; 1d=-3.73%; 5d=-6.56%; 20d=-9.12% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=570.98; 1d=-2.33%; 5d=-8.35%; 20d=-5.31% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=397.36; 1d=-1.50%; 5d=-7.02%; 20d=-2.34% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| AMZN options surface | ATM IV=6.6%; implied_move=0.3%; put/call OI=0.6187338791073231 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=9.6%; implied_move=0.4%; put/call OI=0.7161707337625965 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=9.1%; implied_move=0.3%; put/call OI=0.7110457536157181 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=16.9%; implied_move=0.6%; put/call OI=0.6618456828203898 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=7.6%; implied_move=0.3%; put/call OI=0.3389201364823799 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=6.4%; implied_move=0.3%; put/call OI=0.5690060022872301 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| NVDA insider filings | recent Form4 count=561 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| MSFT insider filings | recent Form4 count=727 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| AAPL insider filings | recent Form4 count=587 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.55; 2Y=4.13; 10Y-2Y=0.41999999999999993 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| AMZN price trend | close=238.00; 1d=-2.53%; 5d=-4.81%; 20d=-10.47% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=381.59; 1d=-3.80%; 5d=-9.94%; 20d=-11.96% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=291.58; 1d=+0.35%; 5d=-6.02%; 20d=-1.09% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| EWJ price trend | close=89.29; 1d=-1.83%; 5d=-4.95%; 20d=-3.01% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=61830.00; 1d=+3.19%; 5d=+1.53%; 20d=+20.43% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6461.00; 1d=-8.33%; 5d=-22.30%; 20d=+7.47% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=72890.00; 1d=-2.51%; 5d=-9.60%; 20d=-8.25% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3385.00; 1d=-1.68%; 5d=-6.47%; 20d=-7.51% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2814.00; 1d=-0.57%; 5d=-2.33%; 20d=-4.27% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=27.5; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.55; 2Y=4.13; 10Y-2Y=0.41999999999999993 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| EWJ price trend | close=89.29; 1d=-1.83%; 5d=-4.95%; 20d=-3.01% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=61830.00; 1d=+3.19%; 5d=+1.53%; 20d=+20.43% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6461.00; 1d=-8.33%; 5d=-22.30%; 20d=+7.47% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 1810.HK price trend | close=26.32; 1d=-3.24%; 5d=-7.91%; 20d=-16.34% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.44; 1d=+0.92%; 5d=-2.87%; 20d=-9.30% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=113.50; 1d=-2.97%; 5d=-10.25%; 20d=-14.76% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=465.60; 1d=+2.74%; 5d=-0.17%; 20d=+3.02% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=34.75; 1d=+0.17%; 5d=-2.22%; 20d=-6.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=79.00; 1d=+2.33%; 5d=-1.74%; 20d=-6.12% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.55; 2Y=4.13; 10Y-2Y=0.41999999999999993 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=27.5; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
| 1810.HK price trend | close=26.32; 1d=-3.24%; 5d=-7.91%; 20d=-16.34% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.44; 1d=+0.92%; 5d=-2.87%; 20d=-9.30% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=113.50; 1d=-2.97%; 5d=-10.25%; 20d=-14.76% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

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

- [Move Index Chart - Barchart.com](https://www.barchart.com/stocks/quotes/$MOVE/interactive-chart)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Customizable interactive chart for Move Index with latest real-time price quote, charts, latest news, technical analysis and opinions.

- [VIX S&P 500 Volatility and MOVE Treasury Volatility / StreetStats](https://streetstats.finance/markets/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：At its current level, the gauge sits near its long‐run average, pointing to a balanced outlook for fixed‐income volatility. See the charts and tables below for the latest VIX an...

- [MOVE Index (MOVE) - MacroMicro](https://en.macromicro.me/charts/35584/us-treasury-move-index)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：The Merrill Lynch Option Volatility Estimate (MOVE) Index reflects the level of volatility in U.S. Treasury futures. The index is considered a proxy for term premiums of U.S. Tr...

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [QQQ: Invesco QQQ Trust Option Overview / OptionCharts](https://optioncharts.io/options/QQQ)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View comprehensive QQQ options with our latest charts on volume, open interest, max pain, and implied volatility.

- [CBOE Volatility Index: VIX (VIXCLS) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/VIXCLS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Graph and download economic data for CBOE Volatility Index: VIX (VIXCLS) from 1990-01-02 to 2026-06-09 about VIX, volatility, stock market, and USA.

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://alfred.stlouisfed.org/series?seid=BAMLH0A0HYM2)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：Graph and download revisions to economic data for from 2023-06-12 to 2026-06-08 about option-adjusted spread, yield, interest rate, interest, rate, and USA.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

- [Current Values - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index?idx=nk225)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Current Values Nikkei calculates and publishes various types of the indexes such as the "Nikkei Stock Average (Nikkei 225)" which is known as a representative Japanese stock mar...

- [USD/JPY (JPY=X) Live Rate, Chart & News - Yahoo Finance](https://finance.yahoo.com/quote/JPY=X/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Find the latest USD/JPY currency exchange rate, historical data, charts, and relevant news for informed trading and investing.

- [USD JPY / US Dollar to Yen Live Rate - Investing.com](https://www.investing.com/currencies/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get real time data on the USD/JPY pair including the live rate, as well as our currency converter, analysis, news, historical data and more.

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
## [美以打击使霍尔木兹海峡成全球冲突热点](https://news.un.org/feed/view/en/story/2026/06/1167648) ⭐️ 10.0/10

2 月 28 日，美国和以色列军队对伊朗发动打击，使霍尔木兹海峡一夜之间成为全球冲突热点，威胁到关键能源运输航道的稳定。 霍尔木兹海峡是全球最重要的石油和液化天然气运输咽喉之一；任何中断都可能引发严重的能源价格飙升和供应短缺，影响全球市场和经济稳定。 该海峡最窄处仅 34 公里宽，每年承担全球 20%的液化天然气和 25%的海运石油贸易。军事升级立即增加了航运、保险成本以及欧亚能源依赖型经济体的风险。

rss · UN News · Jun 5, 12:00

**背景**: 霍尔木兹海峡位于伊朗和阿曼之间，是从波斯湾到公海的唯一海上通道。它对全球能源供应至关重要，大量石油和天然气经此运输。历史上伊朗曾在冲突中威胁关闭海峡，2026 年的伊朗战争将其变成了活跃的军事冲突热点，可能造成比过去油轮战等危机更严重的干扰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://www.strausscenter.org/strait-of-hormuz-geography/">Strait of Hormuz - Geography - Strauss Center</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#military-risk`, `#energy`, `#commodities`, `#middle-east`

---

<a id="item-3"></a>
## [联合国安理会辩论中东问题，美伊停火脆弱](https://news.un.org/feed/view/en/story/2026/06/1167689) ⭐️ 7.0/10

联合国安理会就推进中东政治解决方案举行高级别辩论，同时美伊之间的脆弱停火仍在维持，联合国秘书长警告称局势升级会在全球产生连锁反应。 这场辩论凸显了美伊停火的脆弱性以及全球能源市场面临的高风险，因为进一步升级可能扰乱霍尔木兹海峡的石油运输，并引发新的制裁或军事行动。 值得注意的是，据报道停火协议草案包括延长 60 天，允许伊朗自由出售石油，以换取美国解除制裁，但该协议仍未获批。

rss · UN News · Jun 10, 12:00

**背景**: 联合国安理会五个常任理事国（中国、法国、俄罗斯、英国、美国）对实质性决议拥有否决权。当前的美伊停火是在 2026 年初数月的军事升级之后达成的，包括美国对伊朗目标的打击以及霍尔木兹海峡石油运输中断，该海峡是全球能源供应的关键瓶颈。这些紧张局势已影响油价并促使国际外交干预。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://main.un.org/securitycouncil/en/content/voting-system">Voting System | Security Council - United Nations</a></li>
<li><a href="https://www.theguardian.com/world/2026/may/23/trump-ceasefire-iran-strait-of-hormuz">Trump claims peace deal with Iran ‘largely negotiated... | The Guardian</a></li>
<li><a href="https://www.imf.org/en/blogs/articles/2026/03/30/how-the-war-in-the-middle-east-is-affecting-energy-trade-and-finance">How the War in the Middle East Is Affecting Energy, Trade, and ... - IMF</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#iran`, `#united-states`

---

<a id="item-4"></a>
## [提尔新空袭致 8 人死亡，联合国评估黎巴嫩损失超 3.65 亿美元](https://news.un.org/feed/view/en/story/2026/06/1167685) ⭐️ 7.0/10

黎巴嫩提尔市遭受的新空袭造成 8 人死亡，与此同时，联合国周二发布的一份评估报告显示，自最新一轮升级以来，贝鲁特和黎巴嫩山地区的建筑损坏已超过 3.65 亿美元。 尽管存在停火协议，但持续不断的暴力和巨大损失凸显了外交努力的脆弱性，以及爆发更广泛地区冲突的风险，这可能会破坏能源市场和地区稳定。 该评估由联合国开发计划署牵头，并得到联合国安全保障部及黎巴嫩武装部队的核实，采用卫星图像；2024 年 11 月达成的 60 天停火协议未能阻止敌对行动，双方均威胁进行报复。

rss · UN News · Jun 9, 12:00

**背景**: 自 2023 年 10 月以来，以色列与真主党之间的敌对行动在黎巴嫩造成广泛破坏。2024 年 11 月达成的停火协议曾短暂平息战事，但违反行为持续发生。联合国的评估为重建规划提供了关键数据，并凸显了人道主义后果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167685">Fresh strikes on Tyre kill eight, as UN puts Lebanon ... | UN News</a></li>
<li><a href="https://www.undp.org/arab-states/publications/building-level-damage-assessment-beirut-and-mount-lebanon">Building -Level Damage Assessment : Beirut and Mount Lebanon</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah–Israel_conflict_(2023–present)">Hezbollah–Israel conflict (2023–present) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#geopolitics`, `#military-risk`, `#diplomacy`

---

<a id="item-5"></a>
## [联合国警告乌克兰战争达 2022 年以来最致命阶段](https://news.un.org/feed/view/en/story/2026/06/1167674) ⭐️ 7.0/10

联合国副秘书长迪卡洛周一向安理会表示，由于大规模空袭和平民伤亡增加，乌克兰战争进入了自 2022 年俄罗斯全面入侵以来最致命的阶段。 冲突急剧升级加剧了地缘政治紧张，增加了进一步制裁和军事升级的风险，并可能扰乱全球能源和大宗商品市场，促使大国作出政策反应。 这一警告是在安理会会议上发出的，当时敌对行动正在加剧，迪卡洛强调大规模空袭是造成人道主义后果恶化的关键因素。

rss · UN News · Jun 8, 12:00

**背景**: 俄罗斯于 2022 年 2 月对乌克兰发动全面入侵，引发二战以来欧洲最大规模的武装冲突。联合国安理会虽多次开会，但因俄罗斯拥有否决权而分歧严重。冲突时有升级，包括密集的城市炮击和基础设施袭击，但当前阶段标志着局势显著恶化。

**标签**: `#russia-ukraine`, `#geopolitics`, `#military-risk`, `#energy`, `#commodities`

---

<a id="item-6"></a>
## [无人机袭击破坏苏丹关键援助路线](https://news.un.org/feed/view/en/story/2026/06/1167688) ⭐️ 6.0/10

联合国周二报告称，针对苏丹桥梁、道路和民用基础设施的无人机袭击不断升级，正在阻碍人道主义援助进入，并将平民置于进一步的危险之中。 这些袭击可能加剧苏丹的人道主义危机，并可能加大国际社会对交战各方的压力，从而影响外交努力和地区稳定。 联合国的警告强调，关键援助路线的损坏限制了向脆弱人群运送基本物资，但未立即提供具体的伤亡或损失数字。

rss · UN News · Jun 9, 12:00

**背景**: 自 2023 年 4 月以来，苏丹一直陷入苏丹武装部队与快速支援部队之间的冲突，造成大规模流离失所和严重的人道主义危机。双方在战斗中均使用了无人机，但对桥梁和道路等民用基础设施的袭击代表了一种升级，直接阻碍了援助物资的运送。联合国及人道主义组织一再警告通行条件恶化及饥荒风险。

**标签**: `#geopolitics`, `#military-risk`, `#middle-east`, `#humanitarian`, `#sudan`

---

<a id="item-7"></a>
## [联合国人权负责人：美国制裁正导致古巴儿童死亡](https://news.un.org/feed/view/en/story/2026/06/1167671) ⭐️ 6.0/10

联合国人权事务高级专员沃尔克·蒂尔克发出严厉警告，称美国制裁通过阻断基本药品获取，正在导致古巴儿童死亡，并呼吁立即解除封锁。 联合国高级官员的这一表态显著加大了对美国古巴政策的外交压力，可能强化国际社会对制裁人道主义后果的关注，影响多边论坛上的相关辩论。 该警告首次明确在联合国人权事务负责人层级将美国制裁与儿童死亡联系起来，但并不意味政策会立即改变；美国对古巴的封锁已持续超过六十年。

rss · UN News · Jun 8, 12:00

**背景**: 美国对古巴的禁运始于 1960 年，是现代史上持续时间最长的贸易封锁之一。它限制了对古巴的贸易、金融交易和商品出口，包括药品和医疗设备。沃尔克·蒂尔克是奥地利外交官，自 2022 年 10 月起担任联合国人权事务高级专员。联合国大会曾多次谴责该禁运的域外影响和对人道主义的伤害。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_States_embargo_against_Cuba">United States embargo against Cuba - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/03/26/world/americas/cubas-health-system-us-oil-blockade.html">Cuban Patients Are Dying Because of U.S. Blockade, Doctors Say</a></li>

</ul>
</details>

**标签**: `#sanctions`, `#diplomacy`, `#united-states`, `#cuba`

---

<a id="item-8"></a>
## [联合国发起 3.315 亿美元黎巴嫩危机援助呼吁](https://news.un.org/feed/view/en/story/2026/06/1167659) ⭐️ 6.0/10

联合国驻黎巴嫩机构周五追加发起 3.315 亿美元的援助呼吁，以帮助因真主党武装与以色列部队持续冲突（已进入第三个月）而受影响的 140 万民众。 这凸显人道主义局势持续恶化，表明地区不稳定长期化，可能加大外交压力并影响捐助方资金分配，同时在流离失所和经济压力下加剧黎巴嫩的主权风险。 呼吁目标覆盖 140 万人，但具体资金机制和响应计划尚不明朗。黎巴嫩政府近期已着手解除真主党武装，但进展不确定。

rss · UN News · Jun 5, 12:00

**背景**: 真主党是黎巴嫩什叶派伊斯兰政治和军事组织，被多国列为恐怖实体。与以色列的冲突于 2023 年 10 月再起，2024 年升级为全面战争，后达成停火。2026 年，黎巴嫩政府禁止其军事部门并批准解除武装计划。联合国人道主义呼吁是为危机紧急需求协调募资的机制，此次 3.315 亿美元是对以往筹资的补充。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sana.sy/en/international/2321436/">UN launches $331.5 million humanitarian appeal for Lebanon response</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#military-risk`, `#geopolitics`, `#sovereign-risk`, `#humanitarian`

---