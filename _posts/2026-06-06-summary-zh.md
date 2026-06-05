---
layout: default
title: "Horizon Summary: 2026-06-06 (ZH)"
date: 2026-06-06
lang: zh
---

> From 41 items, 12 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [联合国促克制 美伊交火 伊朗袭邻国](#item-2) ⭐️ 10.0/10
3. [叙利亚发现未申报化武，含古塔袭击所用火箭](#item-3) ⭐️ 9.0/10
4. [以色列-真主党冲突升级，联合国安理会召开紧急会议](#item-4) ⭐️ 9.0/10
5. [霍尔木兹危机扰乱联合国援助，加剧非洲与阿富汗饥荒](#item-5) ⭐️ 7.0/10
6. [WMO 确认厄尔尼诺形成，警告极端天气](#item-6) ⭐️ 7.0/10
7. [欧洲央行施纳贝尔：从货币基金到稳定币的教训](#item-7) ⭐️ 7.0/10
8. [欧洲央行副行长谈欧元区经济与政策立场](#item-8) ⭐️ 7.0/10
9. [联合国呼吁追加 3.315 亿援黎](#item-9) ⭐️ 6.0/10
10. [联合国：以色列停火期间仍袭击加沙警察](#item-10) ⭐️ 6.0/10
11. [联合国谴责俄罗斯对乌克兰的新一轮袭击](#item-11) ⭐️ 6.0/10
12. [欧洲央行发布 2026 年 4 月消费者预期调查](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 5, 22:56

**Trading Analysis**

> 分析方法：digital-oracle multi-signal synthesis  
> 分析范围：QDII 纳斯达克 100 / 海外股票 / 美国股票 / 日本股票 / 香港股票  
> 时间维度：1日 / 1周 / 1月  
> 数据原则：仅使用市场交易数据，不使用新闻观点或分析师观点  
> 可追溯性：结构化 provider 数据 + WebSearch 市场数据引用，参考文章列于报告末尾。  
> 免责声明：本分析仅基于市场数据进行概率估算，不构成投资建议。市场存在不确定性，请独立判断并承担相应风险。

### 资产概率总览 (Asset Probability Overview)

| 资产 | 市场 | 1日 | 1周 | 1月 | 数据质量 |
|---|---|---|---|---|---|
| QDII Nasdaq 100 Proxy | US | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | high |
| US Mega Cap Basket | US | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | high |
| Japan Equity Basket | JP | neutral 33/33/34 | bullish 38/31/31 | bullish 39/30/31 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| ^NDX price trend | close=28957.60; 1d=-4.77%; 5d=-4.53%; 20d=+1.38% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=705.06; 1d=-4.80%; 5d=-4.50%; 20d=+1.46% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=28829.25; 1d=-5.44%; 5d=-5.18%; 20d=+0.51% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=8.1%; implied_move=0.3%; put/call OI=2.826744908021768 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.55; 2Y=4.17; 10Y-2Y=0.3799999999999999 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=42.1; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| ^NDX price trend | close=28957.60; 1d=-4.77%; 5d=-4.53%; 20d=+1.38% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=705.06; 1d=-4.80%; 5d=-4.50%; 20d=+1.46% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=28829.25; 1d=-5.44%; 5d=-5.18%; 20d=+0.51% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| TSLA price trend | close=391.00; 1d=-6.56%; 5d=-10.28%; 20d=-5.05% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=246.03; 1d=-3.06%; 5d=-9.09%; 20d=-9.27% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=205.10; 1d=-6.20%; 5d=-2.75%; 20d=-2.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=416.67; 1d=-2.66%; 5d=-7.46%; 20d=-0.76% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=593.00; 1d=-5.51%; 5d=-6.25%; 20d=-3.86% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=368.53; 1d=-0.98%; 5d=-3.11%; 20d=-7.40% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| NVDA options surface | ATM IV=5.4%; implied_move=0.2%; put/call OI=0.7515216948850699 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=7.6%; implied_move=0.3%; put/call OI=0.37879698319190874 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=3.4%; implied_move=0.1%; put/call OI=0.4201459339486945 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=11.2%; implied_move=0.4%; put/call OI=0.45711837595570787 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=11.1%; implied_move=0.5%; put/call OI=0.4989197762979777 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=7.8%; implied_move=0.3%; put/call OI=0.7221303917868557 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=42.1; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| NVDA insider filings | recent Form4 count=560 | 内部人交易节奏可作为估值温度辅助校验信号。 |
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
| TSLA price trend | close=391.00; 1d=-6.56%; 5d=-10.28%; 20d=-5.05% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=246.03; 1d=-3.06%; 5d=-9.09%; 20d=-9.27% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=205.10; 1d=-6.20%; 5d=-2.75%; 20d=-2.91% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 6861.T price trend | close=78070.00; 1d=-2.46%; 5d=-2.55%; 20d=-7.25% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3559.00; 1d=+0.54%; 5d=+3.34%; 20d=+14.29% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=59450.00; 1d=-6.61%; 5d=+13.41%; 20d=+13.35% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=90.72; 1d=-3.62%; 5d=-2.41%; 20d=-0.30% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2850.00; 1d=+0.41%; 5d=-6.31%; 20d=-2.16% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7426.00; 1d=+0.66%; 5d=-0.87%; 20d=+21.12% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.55; 2Y=4.17; 10Y-2Y=0.3799999999999999 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=42.1; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 跨层分歧信息有限，后续需补充更多波动与事件市场数据。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | medium |
| 1月 | 39% | 30% | 31% | bullish | 20日趋势维持上行，1月窗口偏多 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 6861.T price trend | close=78070.00; 1d=-2.46%; 5d=-2.55%; 20d=-7.25% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3559.00; 1d=+0.54%; 5d=+3.34%; 20d=+14.29% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=59450.00; 1d=-6.61%; 5d=+13.41%; 20d=+13.35% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| EWH price trend | close=21.82; 1d=-3.11%; 5d=-5.58%; 20d=-10.35% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.38; 1d=-2.76%; 5d=-1.31%; 20d=-10.64% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=34.75; 1d=-2.03%; 5d=-0.86%; 20d=-6.56% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=27.80; 1d=-2.04%; 5d=-0.86%; 20d=-10.67% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=115.80; 1d=+0.70%; 5d=+2.03%; 20d=-2.69% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=453.20; 1d=-1.26%; 5d=+6.09%; 20d=-3.96% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.55; 2Y=4.17; 10Y-2Y=0.3799999999999999 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=42.1; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
| EWH price trend | close=21.82; 1d=-3.11%; 5d=-5.58%; 20d=-10.35% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.38; 1d=-2.76%; 5d=-1.31%; 20d=-10.64% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=34.75; 1d=-2.03%; 5d=-0.86%; 20d=-6.56% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days or more out. IV is a forward looking prediction of the likelihood...

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [NASDAQ 100 Index Volatility History & Chart Since 1985](https://wallstreetnumbers.com/indexes/ndx/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Get all-time historical data of NASDAQ 100 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Move Index Chart - Barchart.com](https://www.barchart.com/stocks/quotes/$MOVE/interactive-chart)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Customizable interactive chart for Move Index with latest real-time price quote, charts, latest news, technical analysis and opinions.

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [CBOE Volatility Index: VIX (VIXCLS) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/VIXCLS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Graph and download economic data for CBOE Volatility Index: VIX (VIXCLS) from 1990-01-02 to 2026-06-03 about VIX, volatility, stock market, and USA.

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [QQQ Options Chain — Open Interest, Implied Volatility, Max Pain & Gamma ...](https://whalequant.io/en/stocks/QQQ/options-analytics)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Explore the live QQQ options chain with strikes, open interest, volume, implied volatility (IV), max pain levels, gamma exposure, dealer positioning and options flow analysis. P...

- [Cboe Global Indices: VIX Index Dashboard](https://www.cboe.com/us/indices/dashboard/vix/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX Index VIX Index Dashboard, VIX Dashboard

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [U.S. High Yield Bond Spread (1996-2026) - Macrotrends](https://www.macrotrends.net/3229/us-high-yield-bond-spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：U.S. High Yield Bond Spread: 2.95% as of June 1, 2026. Units: Percent Frequency: Daily, Close Release: ICE BofA Indices Source: Ice Data Indices, LLC

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Index Information - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index/profile?idx=nk225vi)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：The Nikkei Stock Average Volatility Index are calculated by using prices of Nikkei 225 futures and Nikkei 225 options on the Osaka Exchange (OSE). In the calculation, taking nea...

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

- [Valuta EX - Currency Converter / Real-Time Exchange Rates](https://valuta.exchange/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

- [USD JPY / US Dollar to Yen Live Rate - Investing.com](https://www.investing.com/currencies/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get real time data on the USD/JPY pair including the live rate, as well as our currency converter, analysis, news, historical data and more.

- [USD JPY Exchange Rate, Live USD to JPY Forex Rate at Forex Rates](https://www.forexrates.net/fx-rates/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：USD JPY Exchange Rate This is the live USD JPY rate forex data page, displaying the FX price for the USD/JPY. The FX rate self-updates every few seconds. Compare exchange rates...

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
## [联合国促克制 美伊交火 伊朗袭邻国](https://news.un.org/feed/view/en/story/2026/06/1167639) ⭐️ 10.0/10

周二，联合国秘书长安东尼奥·古特雷斯对据报道的美伊之间夜间交火以及伊朗袭击科威特和巴林的事件表示震惊。 美伊直接军事交火及伊朗对海湾国家的攻击扩大，可能导致更大规模的地区战争，威胁全球能源供应，并引发市场严重重新定价和避险资产流动。 联合国秘书长呼吁克制；报道表明伊朗直接以科威特和巴林为目标，将冲突从美伊双边紧张扩大至更广泛的海湾阿拉伯国家。

rss · UN News · Jun 3, 12:00

**背景**: 自 2026 年初美以联合打击伊朗及核谈判破裂以来，美伊紧张局势持续升级。伊朗此前报复主要针对美国目标，但最新对科威特和巴林的袭击标志着危险扩张。海湾地区是全球石油运输要道，局势升级对国际市场和安全的威胁更大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167639">World News in Brief: UN urges restraint as Gulf tensions rise, fear and ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Iran_war">2026 Iran war - Wikipedia</a></li>
<li><a href="https://www.msn.com/en-us/politics/international-relations/iran-launches-missile-attacks-on-bahrain-and-kuwait/ar-AA24HpPO">Iran launches missile attacks on Bahrain and Kuwait - MSN</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`

---

<a id="item-3"></a>
## [叙利亚发现未申报化武，含古塔袭击所用火箭](https://news.un.org/feed/view/en/story/2026/06/1167652) ⭐️ 9.0/10

联合国化武检查员在叙利亚发现大量未申报的化学武器，其中包括与 2013 年古塔袭击中使用的相同类型的火箭。联合国裁军高官称此为“重大发现”。 这一违规行为可能引发新的外交危机，导致安理会对叙政权实施制裁或军事行动。它也动摇了国际防扩散规范，并可能刺激对避险资产的需求。 该发现是在禁化武组织核查叙利亚申报完整性的任务下进行的；叙利亚此前声称所有化武已于 2014 年移除。这些火箭与在古塔释放沙林毒气、造成逾 1400 人死亡的火箭是同一型号。

rss · UN News · Jun 4, 12:00

**背景**: 2013 年 8 月，古塔遭受沙林袭击，造成逾 1400 人死亡，普遍认为是阿萨德军队所为，几乎招致西方军事打击。叙利亚随后加入《化学武器公约》，在禁化武组织-联合国联合特派团监督下于 2014 年销毁了已申报的武库。但外界始终怀疑其有未申报化武，此次发现证实叙利亚隐瞒了武器，违反了国际义务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167652">Undeclared chemical weapons found in Syria, including type ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ghouta_chemical_attack">Ghouta chemical attack - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OPCW-UN_Joint_Mission_in_Syria">OPCW-UN Joint Mission in Syria</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#sanctions`, `#middle-east`

---

<a id="item-4"></a>
## [以色列-真主党冲突升级，联合国安理会召开紧急会议](https://news.un.org/feed/view/en/story/2026/06/1167618) ⭐️ 9.0/10

应法国请求，联合国安理会于周一召开紧急会议，讨论以色列与黎巴嫩真主党之间不断升级的暴力冲突，这给正在进行的美伊和谈蒙上阴影。 冲突升级可能破坏脆弱的美伊和谈，重新点燃更广泛的地区冲突并扰乱全球能源市场，同时也考验联合国执行停火的能力。 会议是在以色列警告将打击贝鲁特南郊，且与停火协议相关的美伊谈判状况不明之际召开的。

rss · UN News · Jun 1, 12:00

**背景**: 真主党是黎巴嫩受伊朗支持的强大什叶派民兵和政治党派，被多国列为恐怖组织。自 2023 年 10 月以来，该组织与以色列持续交战，包括 2024 年的战争后曾达成停火。美国和伊朗自 2025 年起进行谈判，包括在伊斯兰堡的多轮会谈，旨在延长停火并防止更广泛战争，但近期冲突加剧，谈判陷入僵局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/06/03/us-iran-war-escalates-peace-talks-stalemate-.html">U.S., Iran intensify attacks as ceasefire frays, peace talks ... Second round in Islamabad: Who are the main US-Iran ... U.S. And Iran Fail to Agree on Peace Deal After 21 Hours of ... US and Iran show little progress in talks after week of clashes Where peace talks between the US and Iran currently stand US conducts 'self-defense' strikes in Iran - ABC News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#middle-east`, `#diplomacy`, `#military-risk`, `#energy`

---

<a id="item-5"></a>
## [霍尔木兹危机扰乱联合国援助，加剧非洲与阿富汗饥荒](https://news.un.org/feed/view/en/story/2026/06/1167653) ⭐️ 7.0/10

霍尔木兹海峡危机持续近 100 天后，联合国机构报告援助供应链中断，导致索马里饥荒加剧，而阿富汗的诊所因物资短缺被迫拒收营养不良儿童。 这场人道主义冲击标志着供应链的长期中断，可能引发大范围粮食不安全，促使紧急外交干预，并影响石油和谷物等大宗商品市场，对弱势群体造成严重后果。 这场危机已进入第三个月，尤其严重影响了索马里和阿富汗的援助行动；联合国机构警告，若霍尔木兹海峡持续阻塞，援助缺口将进一步恶化，可能导致拯救生命的项目被迫进一步缩减。

rss · UN News · Jun 4, 12:00

**背景**: 霍尔木兹海峡是全球关键的海上咽喉，每日约有 20%的世界石油和大量液化天然气经此运输。该海峡的任何航运中断都可能立即冲击全球能源和大宗商品供应链。联合国世界粮食计划署（WFP）是全球最大的人道主义组织，依赖稳定的航线向冲突和贫困地区运送粮食。长期封锁不仅会推高能源价格，还会延误或阻止关键援助物资的运输，从而加剧脆弱地区的饥荒。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://worldhistoryjournal.com/2026/04/20/strait-of-hormuz/">The Strategic Importance of the Strait of Hormuz: a historical ...</a></li>
<li><a href="https://maritimeducation.com/strait-of-hormuz-geography-navigation-strategic-importance-and-maritime-challenges/">Strait of Hormuz: Geography, Navigation, Strategic Importance, and ...</a></li>
<li><a href="https://www.un.org/en/our-work/deliver-humanitarian-aid">Deliver Humanitarian Aid | United Nations</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#supply-chain`, `#commodities`, `#middle-east`, `#global-markets`

---

<a id="item-6"></a>
## [WMO 确认厄尔尼诺形成，警告极端天气](https://news.un.org/feed/view/en/story/2026/06/1167620) ⭐️ 7.0/10

联合国世界气象组织确认厄尔尼诺现象已经开始，太平洋变暖模式将带来几乎全球范围的高温与极端天气，并敦促各国加强预警系统。 这一确认预示全球农业、能源市场和供应链可能受扰，通胀压力上升，进而影响央行政策，波及大宗商品价格与金融市场。 世界气象组织警告称“几乎所有地方”都将出现高于平均的气温，并呼吁加强预警系统以管控风险；具体经济影响取决于厄尔尼诺的强度和持续时间。

rss · UN News · Jun 2, 12:00

**背景**: 厄尔尼诺是一种自然气候模式，与热带中东太平洋海温升高有关，属于厄尔尼诺-南方涛动（ENSO）的一部分。它通常每两到七年发生一次，会改变全球天气，导致部分地区干旱、另一些地区洪涝。历史上，厄尔尼诺曾导致重大经济损失，影响农业、能源需求和渔业。世界气象组织是联合国专门机构，负责监测和协调各国气象与气候数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://journalistsresource.org/environment/el-nino-economic-devastation-climate-change/">El Niño: Economic devastation and how it intersects with climate change</a></li>
<li><a href="https://www.wri.org/insights/super-el-nino-impacts-explained">3 Possible Impacts from the Super El Niño | World Resources Institute</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_Meteorological_Organization">World Meteorological Organization</a></li>

</ul>
</details>

**标签**: `#macroeconomics`, `#commodities`, `#energy`, `#supply-chain`, `#global-markets`

---

<a id="item-7"></a>
## [欧洲央行施纳贝尔：从货币基金到稳定币的教训](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260601~38dffe5ec5.en.html) ⭐️ 7.0/10

伊莎贝尔·施纳贝尔发表讲话，从货币市场基金和稳定币中为央行总结教训，强调了对金融稳定和监管的影响。 该讲话暗示了欧洲央行在数字货币和稳定币监管方面可能的未来政策方向，正值全球对稳定币影响货币主权和金融稳定担忧加剧之际，可能影响欧盟监管框架和市场预期。 讲话可能讨论了运行风险、储备资产质量以及稳定币发行方无法获得央行流动性等风险，并类比了货币市场基金改革。未提出具体政策宣布。

rss · ECB Press Releases · Jun 1, 00:10

**背景**: 货币市场基金投资于短期债务工具并维持稳定净值，但在危机中曾遭遇挤兑，引发改革。稳定币是与法币挂钩的数字资产，通常持有短期工具作为储备，引发类似的稳定性担忧。伊莎贝尔·施纳贝尔是欧洲央行执行委员会委员，对货币政策和监管具有影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stablecoin">Stablecoin - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isabel_Schnabel">Isabel Schnabel - Wikipedia</a></li>
<li><a href="https://www.federalreserve.gov/econres/notes/feds-notes/banks-in-the-age-of-stablecoins-implications-for-deposits-credit-and-financial-intermediation-20251217.html">The Fed - Banks in the Age of Stablecoins: Some Possible Implications for Deposits, Credit, and Financial Intermediation</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#global-markets`, `#europe`, `#macroeconomics`

---

<a id="item-8"></a>
## [欧洲央行副行长谈欧元区经济与政策立场](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260531~f648dbde70.en.html) ⭐️ 7.0/10

2026 年 5 月 31 日，欧洲央行副行长路易斯·德金多斯在《拓展报》的采访中讨论了欧元区的经济挑战、通胀趋势以及依赖数据的货币政策立场。 其言论为利率决策提供前瞻性指引，在经济增长疲软和地缘不确定性的背景下，影响欧元汇率、债券收益率和市场预期。 此次采访在欧央行 2026 年 3 月维持利率不变的决定之后进行，当时预测 GDP 增长 0.8%，并重申逐次会议、依赖数据的决策方式。

rss · ECB Press Releases · May 31, 14:00

**背景**: 欧洲央行是欧元区的中央银行，负责维持价格稳定。受俄乌冲突和贸易紧张局势影响，欧元区经济增长乏力，通胀逐步回落。自 2024 年以来，欧洲央行已多次降息，但近期暂停，强调依赖数据的策略。德金多斯作为副行长，在政策沟通中发挥重要作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260319~3057739775.en.html">Monetary policy decisions - European Central Bank</a></li>
<li><a href="https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-europe.html">Our economic outlook for the euro area | Vanguard</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`

---

<a id="item-9"></a>
## [联合国呼吁追加 3.315 亿援黎](https://news.un.org/feed/view/en/story/2026/06/1167659) ⭐️ 6.0/10

联合国呼吁追加 3.315 亿美元，以援助黎巴嫩境内 140 万受难民众，此时真主党与以色列军队的冲突已持续三个月，人道主义需求不断加剧。 这一呼吁凸显了以色列-真主党冲突的严重人道后果，可能促使国际社会加大斡旋力度以达成停火，并加剧地区不稳定，对能源市场和安全产生影响。 这笔资金旨在援助 140 万人，但真主党在部分地区的控制以及黎巴嫩政府正在进行的解除武装行动，可能使人道主义准入复杂化。

rss · UN News · Jun 5, 12:00

**背景**: 真主党是黎巴嫩受伊朗支持的什叶派武装组织和政党。自 2023 年 10 月以来，与以色列的跨境交火不断升级，2024 年爆发全面战争，虽经斡旋达成停火，但冲突仍在持续。黎巴嫩政府在美国支持之下，正积极推进真主党解除武装，但该进程充满争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://www.cfr.org/backgrounders/what-hezbollah">What Is Hezbollah? - Council on Foreign Relations</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#geopolitics`, `#military-risk`, `#diplomacy`, `#humanitarian`

---

<a id="item-10"></a>
## [联合国：以色列停火期间仍袭击加沙警察](https://news.un.org/feed/view/en/story/2026/06/1167631) ⭐️ 6.0/10

联合国人权高专办报告称，尽管名义上的停火已持续数月，以色列无人机和空袭仍在继续袭击加沙警察和其他巴勒斯坦人。 持续的袭击破坏了加沙脆弱的稳定和重建努力，警察部队对安全和援助分配至关重要，这可能加剧紧张局势并引发国际谴责。 人权高专办指出，警察部队正被系统性攻击，这违反了国际人道法。尽管 2025 年 1 月达成停火协议，以色列军队仍持续打击警察目标。

rss · UN News · Jun 3, 12:00

**背景**: 2025 年 1 月以色列与哈马斯之间的停火协议旨在停止敌对行动并促进人质释放和人道主义援助，但停火一直脆弱且时有违反。联合国人权高专办是负责促进和保护人权的联合国部门，负责监测和报告冲突地区的侵犯行为。加沙警察部队在维持公共秩序和促进重建及人道主义物资运送方面发挥关键作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/January_2025_Gaza_war_ceasefire">January 2025 Gaza war ceasefire - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OHCHR">OHCHR</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`

---

<a id="item-11"></a>
## [联合国谴责俄罗斯对乌克兰的新一轮袭击](https://news.un.org/feed/view/en/story/2026/06/1167622) ⭐️ 6.0/10

联合国驻乌克兰人道主义协调员报告称，俄罗斯夜间对三个主要城市发动袭击，造成数名平民死亡、数十人受伤，并摧毁或损坏了住宅、医院和商店。 持续袭击平民区加剧了人道主义危机，可能引发进一步的外交谴责或制裁，并影响与冲突相关的国际支持和市场风险认知。 袭击在夜间进行，波及三个未具名的乌克兰城市，医院和商店等民用基础设施直接受损；联合国人道主义协调员的声明未提供具体伤亡数字，仅表述为“数人死亡”和“数十人受伤”。

rss · UN News · Jun 2, 12:00

**背景**: 联合国人道主义协调员由紧急救济协调员任命，负责人道主义国家工作队并协调人道主义行动。在乌克兰，该官员监测平民伤害并倡导根据国际人道法保护平民。自 2022 年全面入侵以来，俄罗斯对城市地区的袭击多次遭到联合国谴责。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Humanitarian_Coordinator">Humanitarian Coordinator - Wikipedia</a></li>
<li><a href="https://interagencystandingcommittee.org/humanitarian-leadership-strengthening-section/leadership-humanitarian-action-handbook-humanitarian-coordinators">LEADERSHIP IN HUMANITARIAN ACTION: Handbook for Humanitarian ...</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#military-risk`, `#diplomacy`, `#europe`

---

<a id="item-12"></a>
## [欧洲央行发布 2026 年 4 月消费者预期调查](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260601~bf8026bfc2.en.html) ⭐️ 6.0/10

欧洲央行发布了 2026 年 4 月消费者预期调查结果，提供了欧元区家庭对通胀和经济增长看法的最新数据。 该调查是欧洲央行政策制定者评估通胀预期锚定情况的重要依据；持续的变动可能预示中期物价稳定风险的变化，并影响未来的利率决策。 尽管不是高影响力的市场事件，但调查中通胀预期指数的持续变化可能影响欧洲央行的中期政策立场。

rss · ECB Press Releases · Jun 1, 08:00

**背景**: 欧洲央行消费者预期调查于 2020 年启动，每月收集欧元区家庭对通胀、收入、消费和劳动力市场的详细预期。它提供了前瞻性的经济情绪指标，补充了欧洲央行的专业预测者调查等其他调查。监测消费者预期至关重要，因为脱锚的通胀预期可能导致自我实现的工资-物价螺旋上涨，使货币政策复杂化。

**标签**: `#central-bank`, `#macroeconomics`, `#europe`

---