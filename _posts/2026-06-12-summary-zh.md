---
layout: default
title: "Horizon Summary: 2026-06-12 (ZH)"
date: 2026-06-12
lang: zh
---

> From 39 items, 9 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [霍尔木兹海峡袭击致三名海员死亡 联合国警告影响扩大](#item-2) ⭐️ 10.0/10
3. [美以打击伊朗，霍尔木兹海峡告急](#item-3) ⭐️ 10.0/10
4. [联合国警告乌克兰战争达 2022 年来最致命阶段](#item-4) ⭐️ 9.0/10
5. [欧洲央行公布 2026 年 6 月货币政策决议](#item-5) ⭐️ 9.0/10
6. [安理会中东辩论，美伊停火脆弱维系](#item-6) ⭐️ 7.0/10
7. [Fresh strikes on Tyre kill eight, as UN puts Lebanon destruction bill at $365 million, and rising](#item-7) ⭐️ 7.0/10
8. [联合国人权高专：美制裁致古巴儿童死亡](#item-8) ⭐️ 7.0/10
9. [欧央行埃尔德松谈政策与稳定](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 11, 22:51

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
| QDII Nasdaq 100 Proxy | US | bullish 38/31/31 | neutral 33/33/34 | neutral 33/33/34 | high |
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
| QQQ price trend | close=717.12; 1d=+3.38%; 5d=-3.17%; 20d=+0.34% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29446.18; 1d=+3.29%; 5d=-3.16%; 20d=+0.27% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29539.00; 1d=+3.45%; 5d=-3.11%; 20d=+0.20% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=17.0%; implied_move=0.4%; put/call OI=1.2275924540731946 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.45; 2Y=4.05; 10Y-2Y=0.40000000000000036 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=29.7; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：1日篮子收益与5日均线结构偏强
- 1周：有效交易信号不足，使用保守基准分布。
- 1月：有效交易信号不足，使用保守基准分布。

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | high |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1月 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| QQQ price trend | close=717.12; 1d=+3.38%; 5d=-3.17%; 20d=+0.34% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29446.18; 1d=+3.29%; 5d=-3.16%; 20d=+0.27% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29539.00; 1d=+3.45%; 5d=-3.11%; 20d=+0.20% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| AAPL price trend | close=295.63; 1d=+1.39%; 5d=-5.01%; 20d=-1.08% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=241.51; 1d=+1.47%; 5d=-4.84%; 20d=-10.59% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=204.87; 1d=+2.22%; 5d=-6.31%; 20d=-9.18% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=568.43; 1d=-0.45%; 5d=-9.42%; 20d=-7.82% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=390.34; 1d=-1.77%; 5d=-8.81%; 20d=-3.46% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=399.15; 1d=+4.60%; 5d=-4.61%; 20d=-10.36% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| TSLA options surface | ATM IV=57.1%; implied_move=3.4%; put/call OI=0.6008633932752261 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=31.9%; implied_move=1.8%; put/call OI=0.5259939585906639 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=34.7%; implied_move=2.0%; put/call OI=0.5937099106612135 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=31.2%; implied_move=1.8%; put/call OI=0.3825504381106621 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=31.0%; implied_move=1.8%; put/call OI=0.47250061109753116 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=21.5%; implied_move=1.2%; put/call OI=0.47430794145691757 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.45; 2Y=4.05; 10Y-2Y=0.40000000000000036 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=29.7; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| MSFT insider filings | recent Form4 count=727 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| AAPL insider filings | recent Form4 count=587 | 内部人交易节奏可作为估值温度辅助校验信号。 |

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
| AAPL price trend | close=295.63; 1d=+1.39%; 5d=-5.01%; 20d=-1.08% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=241.51; 1d=+1.47%; 5d=-4.84%; 20d=-10.59% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=204.87; 1d=+2.22%; 5d=-6.31%; 20d=-9.18% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 7203.T price trend | close=2747.50; 1d=-2.36%; 5d=-3.21%; 20d=-8.66% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=63400.00; 1d=+2.54%; 5d=-0.41%; 20d=+23.83% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.18; 1d=+3.24%; 5d=-2.07%; 20d=-0.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3369.00; 1d=-0.47%; 5d=-4.83%; 20d=-2.18% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6374.00; 1d=-1.35%; 5d=-13.60%; 20d=+10.47% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=71270.00; 1d=-2.22%; 5d=-10.96%; 20d=-7.81% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.45; 2Y=4.05; 10Y-2Y=0.40000000000000036 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=29.7; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| 7203.T price trend | close=2747.50; 1d=-2.36%; 5d=-3.21%; 20d=-8.66% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=63400.00; 1d=+2.54%; 5d=-0.41%; 20d=+23.83% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.18; 1d=+3.24%; 5d=-2.07%; 20d=-0.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 0700.HK price trend | close=457.20; 1d=-1.80%; 5d=-0.39%; 20d=-0.02% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=108.90; 1d=-2.94%; 5d=-5.30%; 20d=-15.05% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=78.10; 1d=-1.14%; 5d=-0.64%; 20d=-10.84% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=34.91; 1d=+0.46%; 5d=-1.58%; 20d=-8.76% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=25.84; 1d=-1.82%; 5d=-8.95%; 20d=-18.74% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.57; 1d=+0.49%; 5d=-2.06%; 20d=-13.14% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=29.7; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.45; 2Y=4.05; 10Y-2Y=0.40000000000000036 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 0700.HK price trend | close=457.20; 1d=-1.80%; 5d=-0.39%; 20d=-0.02% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=108.90; 1d=-2.94%; 5d=-5.30%; 20d=-15.05% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=78.10; 1d=-1.14%; 5d=-0.64%; 20d=-10.84% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [VIX S&P 500 Volatility and MOVE Treasury Volatility / StreetStats](https://streetstats.finance/markets/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：At its current level the index sits near its long-term average, suggesting a balanced outlook for bond market volatility. See the charts and tables below for the latest VIX and...

- [Move Index Chart - Barchart.com](https://www.barchart.com/stocks/quotes/$MOVE/interactive-chart)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Customizable interactive chart for Move Index with latest real-time price quote, charts, latest news, technical analysis and opinions.

- [MOVE Index Charts and Quotes — TradingView](https://www.tradingview.com/symbols/TVC-MOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：MOVE INDEX Setup for Top in World stock markets The chart is the Move index it is reaching an area which I consider High level of Complacency I say this as of this writing The 1...

- [NASDAQ 100 Index Volatility History & Chart Since 1985](https://wallstreetnumbers.com/indexes/ndx/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Get all-time historical data of NASDAQ 100 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days out or more. IV is a forward looking prediction of the likelihood...

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [CBOE Volatility Index: VIX (VIXCLS) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/VIXCLS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Graph and download economic data for CBOE Volatility Index: VIX (VIXCLS) from 1990-01-02 to 2026-06-10 about VIX, volatility, stock market, and USA.

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

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://alfred.stlouisfed.org/series?seid=BAMLH0A0HYM2)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：Graph and download revisions to economic data for from 2023-06-12 to 2026-06-10 about option-adjusted spread, yield, interest rate, interest, rate, and USA.

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [iShares MSCI Japan ETF (EWJ) Price, Holdings, & News](https://www.marketbeat.com/stocks/NYSEARCA/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Should You Buy or Sell iShares MSCI Japan ETF Stock? Get The Latest EWJ Stock Price, Constituents List, Holdings Data, and Headlines at MarketBeat.

- [USD/JPY (JPY=X) Live Rate, Chart & News - Yahoo Finance](https://finance.yahoo.com/quote/JPY=X/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Find the latest USD/JPY currency exchange rate, historical data, charts, and relevant news for informed trading and investing.

- [Live US Dollar to Yens Exchange Rate - $ 1 USD/JPY Today](https://usd.currencyrate.today/jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest and best $1 US Dollar to Yens rate for FREE. USD/JPY - Live exchange rates, banks, historical data & currency charts.

- [USD/JPY Currency Exchange Rate & News - Google Finance](https://www.google.com/finance/beta/quote/USD-JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：USD/JPY Forecast: The BOJ Can't Save the Yen and JGBs Forever Profile The United States dollar is the official currency of the United States and several other countries.

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
## [霍尔木兹海峡袭击致三名海员死亡 联合国警告影响扩大](https://news.un.org/feed/view/en/story/2026/06/1167697) ⭐️ 10.0/10

周三，一艘油轮在霍尔木兹海峡附近遭袭，导致三名印度籍海员死亡。联合国警告称，此次袭击可能给全球能源运输、粮食安全和供应链带来更广泛的影响。 霍尔木兹海峡承载着全球约 20%的石油贸易，这次致命袭击威胁能源安全、燃料价格和供应链稳定，可能引发外交升级、保险成本上升以及大宗商品、股票和货币市场的重新定价。 遇难船员为印度籍，袭击发生在一艘油轮上。联合国明确将此次袭击与全球粮食和能源系统风险加剧联系起来。

rss · UN News · Jun 11, 12:00

**背景**: 霍尔木兹海峡是位于伊朗与阿曼之间的狭窄水道，连接波斯湾与阿曼湾，是全球最重要的海运咽喉之一，每天约有全球五分之一的原油和大量液化天然气通过。因其战略地位，该地区长期是地缘政治紧张和航运袭击的焦点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://worldhistoryjournal.com/2026/04/20/strait-of-hormuz/">The Strategic Importance of the Strait of Hormuz: a ...</a></li>
<li><a href="https://maritimeducation.com/strait-of-hormuz-geography-navigation-strategic-importance-and-maritime-challenges/">Strait of Hormuz: Geography, Navigation, Strategic Importance ...</a></li>
<li><a href="https://www.defencejournal.com/2026/04/03/historical-and-strategic-significance-of-the-strait-of-hormuz-in-global-trade/">Historical and Strategic Significance of the Strait of Hormuz ...</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#military-risk`, `#energy`, `#supply-chain`, `#middle-east`

---

<a id="item-3"></a>
## [美以打击伊朗，霍尔木兹海峡告急](https://news.un.org/feed/view/en/story/2026/06/1167648) ⭐️ 10.0/10

2026 年 2 月 28 日，美以联军对伊朗发动打击，立即使仅 34 公里宽的霍尔木兹海峡成为关键地缘政治引爆点，威胁全球能源运输。 这场危机危及全球约 20%的液化天然气和 25%的海运石油贸易，可能导致严重供应中断、油价飙升以及主要大国间的军事对抗升级。 霍尔木兹海峡连接波斯湾和阿曼湾，以往冲突中从未长时间关闭，但伊朗曾准备布雷；2026 年危机已使其成为主要战区。

rss · UN News · Jun 5, 12:00

**背景**: 霍尔木兹海峡是波斯湾唯一出海通道，承载全球四分之一海运石油和五分之一液化天然气贸易。伊朗位于海峡北岸，阿曼和阿联酋位于南岸。伊朗虽多次威胁封锁，但在 2026 年伊朗战争前从未出现持续中断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://www.strausscenter.org/strait-of-hormuz-geography/">Strait of Hormuz - Geography - Strauss Center</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`, `#global-markets`

---

<a id="item-4"></a>
## [联合国警告乌克兰战争达 2022 年来最致命阶段](https://news.un.org/feed/view/en/story/2026/06/1167674) ⭐️ 9.0/10

联合国安理会获悉，乌克兰战争已进入自 2022 年俄罗斯全面入侵以来最致命的阶段，空袭规模空前，平民伤亡不断攀升。 联合国政治事务负责人的警告表明人道主义危机正在加深，可能加大国际社会对停火谈判、新制裁或军事援助决策的压力。 负责政治事务的副秘书长罗斯玛丽·迪卡洛进行了通报，指出近几个月出现了冲突中规模最大的一些空袭。

rss · UN News · Jun 8, 12:00

**背景**: 联合国安理会是维护国际和平与安全的首要机构。俄罗斯于 2022 年 2 月全面入侵乌克兰，导致旷日持久的战争。安理会已就该冲突举行多次会议，但行动协议常因俄罗斯的否决权而受阻。

**标签**: `#russia-ukraine`, `#diplomacy`, `#military-risk`, `#geopolitics`, `#europe`

---

<a id="item-5"></a>
## [欧洲央行公布 2026 年 6 月货币政策决议](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html) ⭐️ 9.0/10

2026 年 6 月 11 日，欧洲央行公布了其最新的货币政策决议，设定了关键利率并更新了前瞻性指引。 这些决议直接影响欧元汇率、欧洲债券收益率和股市，并可能产生全球溢出效应。 主要再融资利率、存款便利利率和边际贷款便利利率的具体调整，以及前瞻性指引的措辞，将引导市场预期。

rss · ECB Press Releases · Jun 11, 12:15

**背景**: 欧洲央行是欧元区 20 个成员国的中央银行，负责维持价格稳定。其管理委员会制定货币政策。前瞻性指引是一种沟通工具，用于影响市场对未来利率的预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forward_guidance">Forward guidance</a></li>
<li><a href="https://en.wikipedia.org/wiki/Monetary_policy">Monetary policy</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#currencies`, `#bonds`, `#europe`, `#macroeconomics`

---

<a id="item-6"></a>
## [安理会中东辩论，美伊停火脆弱维系](https://news.un.org/feed/view/en/story/2026/06/1167689) ⭐️ 7.0/10

联合国安理会就推进中东政治解决方案举行高级别辩论，联合国秘书长警告称，当前升级正跨越国界和大陆产生影响，而美伊之间脆弱的停火协议在最新危机爆发近四个月后仍在维持。 此次辩论表明在冲突可能扩大的担忧下，外交努力正在加强，可能影响能源市场、制裁政策及地缘政治格局，尤其在美伊停火脆弱且安理会肩负维护国际和平职责的背景下。 辩论于周三（可能是 2026 年 7 月初）举行，联合国秘书长强调全球外溢效应；美伊停火原为 2026 年 4 月由巴基斯坦调解的两周协议，后经延长，但仍脆弱，此前已有违反停火事件发生。

rss · UN News · Jun 10, 12:00

**背景**: 最近一次中东危机于 2026 年 2 月升级，美国与以色列对伊朗发动袭击，引发冲突，伊朗关闭霍尔木兹海峡并攻击美军基地。2026 年 4 月，由巴基斯坦调解达成两周停火，但局势依然紧张。负责国际和平与安全的联合国安理会在中东问题上常因大国对立而僵持，常任理事国屡次使用否决权。此次高级别辩论凸显全球对冲突外溢效应的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire">2026 Iran war ceasefire - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Middle_East_crisis">Middle East crisis</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#united-states`, `#iran`

---

<a id="item-7"></a>
## [Fresh strikes on Tyre kill eight, as UN puts Lebanon destruction bill at $365 million, and rising](https://news.un.org/feed/view/en/story/2026/06/1167685) ⭐️ 7.0/10

Fresh Israeli strikes on Tyre killed eight people and a UN assessment put Lebanon's building damage at over $365 million, highlighting the failure of the ceasefire to halt violence.

rss · UN News · Jun 9, 12:00

**标签**: `#military-risk`, `#middle-east`, `#ceasefire`, `#geopolitics`, `#diplomacy`

---

<a id="item-8"></a>
## [联合国人权高专：美制裁致古巴儿童死亡](https://news.un.org/feed/view/en/story/2026/06/1167671) ⭐️ 7.0/10

联合国人权事务高级专员福尔克尔·蒂尔克发出严厉警告，指出美国的制裁导致古巴药品匮乏、儿童死亡，并呼吁立即解除制裁。 联合国人权事务高级专员的高调谴责可能加大国际社会对美国的外交压力，并影响关于制裁导致人道主义后果的持续辩论，进而可能影响美国政策。 美国对古巴的封锁自 1960 年开始实施，近年来进一步收紧，包括将古巴列为“支持恐怖主义国家”，加剧了该国的药品和燃料短缺。

rss · UN News · Jun 8, 12:00

**背景**: 美国自 1960 年起对古巴实施全面的经济、商业和金融封锁。联合国人权事务高级专员是联合国负责人权事务的主要官员，其职责是促进和保护所有人权。福尔克尔·蒂尔克自 2022 年 10 月起担任此职。美国的制裁对古巴医疗系统的影响一直受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_States_embargo_against_Cuba">United States embargo against Cuba - Wikipedia</a></li>
<li><a href="https://www.ohchr.org/en/press-releases/2025/11/enforcement-and-recent-strengthening-us-sanctions-deepen-hardships-cuban">Enforcement and recent strengthening of U.S. sanctions deepen ...</a></li>

</ul>
</details>

**标签**: `#sanctions`, `#diplomacy`, `#united-states`, `#cuba`

---

<a id="item-9"></a>
## [欧央行埃尔德松谈政策与稳定](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260610~439aa97519.en.html) ⭐️ 6.0/10

欧央行执委弗兰克·埃尔德松接受《金融日报》采访，讨论了欧元区的货币政策与金融稳定。 埃尔德松的言论可能为欧央行下一步政策提供早期信号，从而影响利率预期与市场情绪。 摘要未详述采访具体内容，但埃尔德松通常涉及监管、法律事务与系统性风险等议题。

rss · ECB Press Releases · Jun 10, 14:00

**背景**: 弗兰克·埃尔德松是欧央行执委会成员兼监事会副主席，负责法律事务与金融稳定。他的公开讲话常被解读为欧央行对通胀与增长立场的风向标。

**标签**: `#central-bank`, `#europe`, `#macroeconomics`, `#financial-stability`, `#global-markets`

---