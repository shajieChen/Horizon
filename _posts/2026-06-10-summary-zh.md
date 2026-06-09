---
layout: default
title: "Horizon Summary: 2026-06-10 (ZH)"
date: 2026-06-10
lang: zh
---

> From 37 items, 7 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [美以打击伊朗令霍尔木兹海峡成冲突焦点](#item-2) ⭐️ 10.0/10
3. [叙利亚发现未申报化武，含东古塔惨案所用火箭](#item-3) ⭐️ 9.0/10
4. [提尔再遭空袭致八人死亡，联合国称损失达 3.65 亿美元](#item-4) ⭐️ 7.0/10
5. [联合国官员警告：乌克兰战争成为 2022 年以来最致命](#item-5) ⭐️ 7.0/10
6. [联合国人权事务高级专员：美国制裁导致古巴儿童死亡](#item-6) ⭐️ 7.0/10
7. [霍尔木兹危机扰乱全球援助，加剧非洲与阿富汗饥饿](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 9, 22:50

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
| NQ=F price trend | close=29039.00; 1d=-1.41%; 5d=-5.45%; 20d=-1.31% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29084.50; 1d=-1.12%; 5d=-5.14%; 20d=-0.81% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=707.83; 1d=-1.15%; 5d=-5.14%; 20d=-0.77% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=14.7%; implied_move=0.4%; put/call OI=2.0689079843701372 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=33.4; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.53; 2Y=4.13; 10Y-2Y=0.40000000000000036 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| NQ=F price trend | close=29039.00; 1d=-1.41%; 5d=-5.45%; 20d=-1.31% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29084.50; 1d=-1.12%; 5d=-5.14%; 20d=-0.81% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=707.83; 1d=-1.15%; 5d=-5.14%; 20d=-0.77% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| AAPL price trend | close=290.55; 1d=-3.64%; 5d=-7.82%; 20d=-0.73% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=396.68; 1d=-3.00%; 5d=-6.39%; 20d=-10.86% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=403.41; 1d=-2.02%; 5d=-8.59%; 20d=-2.03% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=584.59; 1d=-0.14%; 5d=-2.18%; 20d=-2.38% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=244.19; 1d=-0.42%; 5d=-4.81%; 20d=-9.22% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=208.19; 1d=-0.22%; 5d=-6.46%; 20d=-5.02% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| TSLA options surface | ATM IV=40.4%; implied_move=2.4%; put/call OI=0.6437512644143233 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=32.9%; implied_move=1.9%; put/call OI=0.6153405795463961 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=26.3%; implied_move=1.5%; put/call OI=0.5573015873015873 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=29.7%; implied_move=1.7%; put/call OI=0.7474249689220387 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=26.4%; implied_move=1.5%; put/call OI=0.4931594357199894 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=27.6%; implied_move=1.6%; put/call OI=0.661185574132928 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| NVDA insider filings | recent Form4 count=560 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| AAPL insider filings | recent Form4 count=587 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| CNN Fear & Greed | score=33.4; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| MSFT insider filings | recent Form4 count=738 | 内部人交易节奏可作为估值温度辅助校验信号。 |

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
| AAPL price trend | close=290.55; 1d=-3.64%; 5d=-7.82%; 20d=-0.73% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=396.68; 1d=-3.00%; 5d=-6.39%; 20d=-10.86% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=403.41; 1d=-2.02%; 5d=-8.59%; 20d=-2.03% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 6861.T price trend | close=74770.00; 1d=-0.28%; 5d=-4.56%; 20d=-5.66% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3443.00; 1d=-1.85%; 5d=-6.16%; 20d=-1.18% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=90.95; 1d=-1.09%; 5d=-2.81%; 20d=-1.42% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2830.00; 1d=+0.27%; 5d=-0.49%; 20d=-0.46% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=59920.00; 1d=+8.91%; 5d=+11.56%; 20d=+14.88% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7048.00; 1d=+1.03%; 5d=-18.35%; 20d=+17.72% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.53; 2Y=4.13; 10Y-2Y=0.40000000000000036 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=33.4; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| 6861.T price trend | close=74770.00; 1d=-0.28%; 5d=-4.56%; 20d=-5.66% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3443.00; 1d=-1.85%; 5d=-6.16%; 20d=-1.18% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=90.95; 1d=-1.09%; 5d=-2.81%; 20d=-1.42% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9618.HK price trend | close=114.00; 1d=+0.44%; 5d=-5.08%; 20d=-3.80% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=27.20; 1d=-0.66%; 5d=-8.17%; 20d=-14.20% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=77.20; 1d=+1.25%; 5d=-9.71%; 20d=-8.48% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=453.20; 1d=+1.52%; 5d=-5.90%; 20d=-1.27% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=116.97; 1d=-1.43%; 5d=-10.54%; 20d=-12.55% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=21.59; 1d=-1.19%; 5d=-6.82%; 20d=-11.23% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=33.4; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.53; 2Y=4.13; 10Y-2Y=0.40000000000000036 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 9618.HK price trend | close=114.00; 1d=+0.44%; 5d=-5.08%; 20d=-3.80% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=27.20; 1d=-0.66%; 5d=-8.17%; 20d=-14.20% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=77.20; 1d=+1.25%; 5d=-9.71%; 20d=-8.48% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days or more out. IV is a forward looking prediction of the likelihood...

- [NASDAQ 100 Index Volatility History & Chart Since 1985](https://wallstreetnumbers.com/indexes/ndx/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Get all-time historical data of NASDAQ 100 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [BAMLH0A0HYM2: US High Yield OAS Daily Data - eco3min.fr](https://eco3min.fr/en/credit-spreads-recession-risk-dataset/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：BAMLH0A0HYM2 is the ICE BofA US High Yield Index Option-Adjusted Spread — the daily market-priced premium that below-investment-grade US corporate bonds pay over equivalent-matu...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://alfred.stlouisfed.org/series?seid=BAMLH0A0HYM2)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：Graph and download revisions to economic data for from 2023-06-09 to 2026-06-05 about option-adjusted spread, yield, interest rate, interest, rate, and USA.

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [QQQ Options Volatility — NASDAQ:QQQ — TradingView](https://www.tradingview.com/symbols/NASDAQ-QQQ/options-volatility/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：ATM IV refers to the implied volatility of a contract with a strike price closest to the underlying current price. Track the at-the-money implied volatility for QQQ options acro...

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [iShares MSCI Japan ETF (EWJ) Price, Holdings, & News](https://www.marketbeat.com/stocks/NYSEARCA/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Should You Buy or Sell iShares MSCI Japan ETF Stock? Get The Latest EWJ Stock Price, Constituents List, Holdings Data, and Headlines at MarketBeat.

- [Currency Conversion Calculator / Currency Converter - Forbes Advisor](https://www.forbes.com/advisor/money-transfer/currency-converter/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Use our currency converter to get live exchange rates for over 200 currencies, including cryptocurrencies. Convert major global currencies now.

- [USD/JPY Currency Exchange Rate & News - Google Finance](https://www.google.com/finance/beta/quote/USD-JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：The United States dollar is the official currency of the United States and several other countries. The Coinage Act of 1792 introduced the U.S. dollar at par with the Spanish si...

- [Valuta EX - Currency Converter / Real-Time Exchange Rates](https://valuta.exchange/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

- [Current Values - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index?idx=nk225)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Current Values Nikkei calculates and publishes various types of the indexes such as the "Nikkei Stock Average (Nikkei 225)" which is known as a representative Japanese stock mar...

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
## [美以打击伊朗令霍尔木兹海峡成冲突焦点](https://news.un.org/feed/view/en/story/2026/06/1167648) ⭐️ 10.0/10

2 月 28 日，美国和以色列军队对伊朗发动打击，霍尔木兹海峡即刻成为全球能源运输和军事升级的焦点。 霍尔木兹海峡是全球能源咽喉，承载着 20%的液化天然气和 25%的海运石油运输；任何中断都可能导致油价飙升、供应短缺和中东冲突扩大。 海峡最窄处仅 34 公里，伊朗曾多次威胁封锁，并在过往危机中进行过水雷布设准备。

rss · UN News · Jun 5, 12:00

**背景**: 霍尔木兹海峡连接波斯湾和阿曼湾，是石油资源丰富的海湾地区通往公海的唯一海上通道，每年承载全球五分之一的液化天然气和四分之一的海运石油贸易。数十年来局势时有紧张，伊朗偶有封锁威胁，但 2026 年美以打击将事态升级为全面危机，成为多年来最严重的地缘政治焦点之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://www.britannica.com/place/Strait-of-Hormuz">Strait of Hormuz | Map, Importance, Conflict and Closure, Control, Oil ...</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`, `#united-states`

---

<a id="item-3"></a>
## [叙利亚发现未申报化武，含东古塔惨案所用火箭](https://news.un.org/feed/view/en/story/2026/06/1167652) ⭐️ 9.0/10

联合国化学武器核查人员在叙利亚发现大量未申报的化学武器，其中包括与 2013 年东古塔沙林毒气袭击中使用的相同类型的火箭。 这一发现可能引发联合国安理会采取新行动、对叙利亚实施更多制裁，或导致军事回应，加剧地缘政治紧张，并影响能源市场及避险资产。 该批武库包括用于 2013 年臭名昭著的东古塔袭击的火箭类型，联合国最高裁军官员称此为对国际安全的‘重大发现’。

rss · UN News · Jun 4, 12:00

**背景**: 禁止化学武器组织（OPCW）负责执行《化学武器公约》（CWC），叙利亚在 2013 年东古塔袭击后迫于国际压力加入该公约。尽管叙利亚申报并销毁了其库存，但一直被指控隐藏化学武器。2013 年东古塔袭击使用了装填沙林毒气的火箭，造成数百名平民死亡，并促成美俄达成叙利亚销毁化武的协议。持续调查发现叙利亚内战中多次使用化学武器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Organisation_for_the_Prohibition_of_Chemical_Weapons">Organisation for the Prohibition of Chemical Weapons</a></li>
<li><a href="https://www.opcw.org/">Organisation for the Prohibition of Chemical Weapons</a></li>
<li><a href="https://en.wikipedia.org/wiki/2013_Ghouta_chemical_attack">2013 Ghouta chemical attack</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`, `#sanctions`

---

<a id="item-4"></a>
## [提尔再遭空袭致八人死亡，联合国称损失达 3.65 亿美元](https://news.un.org/feed/view/en/story/2026/06/1167685) ⭐️ 7.0/10

周二，黎巴嫩城市提尔在脆弱的停火期间再遭空袭，造成八人死亡；同日联合国发布评估称，近期冲突升级已对贝鲁特和黎巴嫩山省建筑造成超过 3.65 亿美元损失。 停火协议下暴力依然持续，表明停火可能崩溃，恐将加剧地区不稳定，并恶化黎巴嫩本已严峻的经济和主权风险。 损失评估由联合国开发计划署与黎巴嫩当局协调进行，仅涵盖直接建筑损坏，不含更广泛的经济损失；对提尔的袭击违反了自 2024 年 11 月起生效的停火协议。

rss · UN News · Jun 9, 12:00

**背景**: 2023 年以色列与真主党冲突升级后，2024 年 11 月达成停火，但局势一直脆弱，违规行为频发。2026 年，随着伊朗战争扩大，真主党恢复对以色列的袭击，冲突再度爆发。历史名城提尔位于黎巴嫩南部，多次成为打击目标。联合国损失评估凸显了黎巴嫩所承受的巨大经济代价，该国本就深陷金融危机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167685">Fresh strikes on Tyre kill eight, as UN puts Lebanon ...</a></li>
<li><a href="https://www.undp.org/arab-states/press-releases/rapid-damage-assessment-estimates-over-us365-million-building-damage-across-beirut-and-mount-lebanon">Rapid damage assessment estimates over US$365 Million in ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Lebanon_war">2026 Lebanon war - Wikipedia</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#military-risk`, `#diplomacy`, `#geopolitics`, `#sovereign-risk`

---

<a id="item-5"></a>
## [联合国官员警告：乌克兰战争成为 2022 年以来最致命](https://news.un.org/feed/view/en/story/2026/06/1167674) ⭐️ 7.0/10

在联合国安理会会议上，副秘书长罗斯玛丽·迪卡洛报告称，俄罗斯-乌克兰战争已达到自 2022 年全面入侵以来最致命的地步，空袭范围广泛，平民伤亡不断增加。 此次简报加剧了外交界对冲突升级的警觉，可能促使新的国际制裁、军事援助方案或停火呼吁，同时凸显人道救援系统承受的压力。 迪卡洛指出，近几个月发生了冲突中一些最广泛的空袭，前线两侧平民均受到伤害；安全理事会因俄罗斯的否决权而继续陷入僵局。

rss · UN News · Jun 8, 12:00

**背景**: 联合国安全理事会负责维护国际和平，却因俄罗斯对乌克兰相关决议的否决而屡屡受挫。俄罗斯-乌克兰战争始于 2014 年，2022 年急剧升级，是欧洲自二战以来规模最大的冲突，已造成数万人死亡和严重的难民危机。此次简报正值有报道称俄空袭加剧、人道状况恶化之际。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council">United Nations Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/Russia-Ukraine_war">Russia-Ukraine war</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Department_of_Political_and_Peacebuilding_Affairs">United Nations Department of Political and Peacebuilding Affairs</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#russia-ukraine`, `#military-risk`, `#europe`

---

<a id="item-6"></a>
## [联合国人权事务高级专员：美国制裁导致古巴儿童死亡](https://news.un.org/feed/view/en/story/2026/06/1167671) ⭐️ 7.0/10

联合国人权事务高级专员沃尔克·图尔克周一警告说，美国制裁限制了古巴获取基本药品的渠道，导致儿童死亡，并呼吁立即解除制裁。 这份来自联合国高级官员的高调谴责加剧了对美国放松制裁的外交压力，凸显了经济胁迫的人道主义代价，并可能影响未来的政策辩论。 这一警告是在美国实施数十年全面制裁之后发出的，这些制裁具有域外效力；人道主义豁免被批评为不足以防止药品短缺。

rss · UN News · Jun 8, 12:00

**背景**: 自 1962 年以来，美国一直对古巴实施全面的经济封锁，最初是为了应对冷战紧张局势。该封锁限制贸易、投资和旅行，并对与古巴有业务往来的第三国实施制裁。尽管多年来有所调整，但它仍是现代历史上最持久的贸易禁运之一。联合国人权事务高级专员是联合国负责促进和保护全球人权的最高官员，经常就紧迫的人道主义问题发表声明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_States_embargo_against_Cuba">United States embargo against Cuba - Wikipedia</a></li>
<li><a href="https://www.state.gov/cuba-sanctions">Cuba Sanctions - United States Department of State</a></li>
<li><a href="https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(25)00278-5/fulltext">The health toll of economic sanctions - The Lancet Global Health</a></li>

</ul>
</details>

**标签**: `#sanctions`, `#diplomacy`, `#united-states`, `#cuba`, `#humanitarian`

---

<a id="item-7"></a>
## [霍尔木兹危机扰乱全球援助，加剧非洲与阿富汗饥饿](https://news.un.org/feed/view/en/story/2026/06/1167653) ⭐️ 7.0/10

联合国机构报告称，持续近 100 天的霍尔木兹危机严重阻碍了援助物资的运送，导致非洲饥饿加剧，阿富汗诊所被迫拒收营养不良儿童。 这凸显了地缘政治紧张如何直接扰乱关键的人道主义供应链，加剧脆弱地区的粮食不安全，并可能引发政治不稳定和更多冲突。 危机导致食品价格上涨，增加了援助机构的运营成本，削弱了世界粮食计划署等项目的覆盖范围，南苏丹、索马里和阿富汗受到的影响尤其严重。

rss · UN News · Jun 4, 12:00

**背景**: 霍尔木兹海峡是全球石油和货物运输的关键咽喉。2026 年危机源于伊朗、美国和以色列之间因核谈判破裂及此前的空中冲突而升级的紧张局势。封锁和航运中断不仅影响了能源市场，也阻碍了人道主义物资运输，限制了向本已脆弱地区提供的援助。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167653">From food lines in Somalia to clinics in Afghanistan, Hormuz crisis sends shockwaves through global aid networks | UN News</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis">2026 Strait of Hormuz crisis - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/global-development/2026/apr/29/humanitarian-corridor-strait-of-hormuz-iran-war-hits-vital-aid">Calls for humanitarian corridor through strait of Hormuz as Iran war hits vital aid | Global development | The Guardian</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#supply-chain`, `#commodities`, `#middle-east`, `#food-security`

---