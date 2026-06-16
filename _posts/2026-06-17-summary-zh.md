---
layout: default
title: "Horizon Summary: 2026-06-17 (ZH)"
date: 2026-06-17
lang: zh
---

> From 41 items, 10 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [联合国秘书长称美伊和平协议是‘关键一步’](#item-2) ⭐️ 10.0/10
3. [以色列袭击黎巴嫩医院，冲突加剧人道危机](#item-3) ⭐️ 9.0/10
4. [联合国：乌克兰 5 月平民伤亡创四年新高](#item-4) ⭐️ 9.0/10
5. [欧洲央行公布 2026 年 6 月货币政策决议](#item-5) ⭐️ 9.0/10
6. [拉加德谈货币转型 或涉数字欧元](#item-6) ⭐️ 8.0/10
7. [欧洲央行首席经济学家连恩就欧元区经济前景发表演讲](#item-7) ⭐️ 7.0/10
8. [海地新多国部队启动打击帮派行动](#item-8) ⭐️ 6.0/10
9. [欧央行埃尔德森荷兰采访谈政策前景](#item-9) ⭐️ 6.0/10
10. [FSB 发布 AI 负责任采用良好实践咨询报告](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 16, 22:54

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
| QDII Nasdaq 100 Proxy | US | neutral 33/33/34 | bullish 38/31/31 | bullish 39/30/31 | high |
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
| ^NDX price trend | close=29968.13; 1d=-1.89%; 5d=+3.04%; 20d=+3.36% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=30353.75; 1d=-0.67%; 5d=+4.25%; 20d=+4.32% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=729.86; 1d=-1.90%; 5d=+3.11%; 20d=+3.40% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=2.4%; implied_move=0.1%; put/call OI=1.8455362095323133 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=39.2; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.43; 2Y=4.05; 10Y-2Y=0.3799999999999999 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | high |
| 1月 | 39% | 30% | 31% | bullish | 20日趋势维持上行，1月窗口偏多 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| ^NDX price trend | close=29968.13; 1d=-1.89%; 5d=+3.04%; 20d=+3.36% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=30353.75; 1d=-0.67%; 5d=+4.25%; 20d=+4.32% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=729.86; 1d=-1.90%; 5d=+3.11%; 20d=+3.40% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| TSLA price trend | close=404.66; 1d=-1.58%; 5d=+2.01%; 20d=-1.30% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=393.83; 1d=-1.48%; 5d=-2.37%; 20d=-6.81% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=246.00; 1d=-0.01%; 5d=+0.74%; 20d=-7.12% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=373.25; 1d=+1.06%; 5d=+2.47%; 20d=-5.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=600.21; 1d=+1.13%; 5d=+2.77%; 20d=-1.71% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=207.41; 1d=-2.37%; 5d=-0.37%; 20d=-6.60% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| AMZN options surface | ATM IV=25.7%; implied_move=1.5%; put/call OI=0.39085936121404624 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=17.0%; implied_move=1.0%; put/call OI=0.6368193016736047 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=25.7%; implied_move=1.5%; put/call OI=0.35068864173341785 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=24.8%; implied_move=1.4%; put/call OI=0.4864121087031304 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=28.1%; implied_move=1.6%; put/call OI=0.9821726245601037 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=27.7%; implied_move=1.6%; put/call OI=0.7590690662395175 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=39.2; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| AAPL insider filings | recent Form4 count=587 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.43; 2Y=4.05; 10Y-2Y=0.3799999999999999 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| NVDA insider filings | recent Form4 count=561 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
| TSLA price trend | close=404.66; 1d=-1.58%; 5d=+2.01%; 20d=-1.30% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=393.83; 1d=-1.48%; 5d=-2.37%; 20d=-6.81% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=246.00; 1d=-0.01%; 5d=+0.74%; 20d=-7.12% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 6758.T price trend | close=3275.00; 1d=-1.36%; 5d=-4.88%; 20d=-11.96% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=70860.00; 1d=-2.61%; 5d=+18.26%; 20d=+50.25% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7102.00; 1d=-0.52%; 5d=+0.77%; 20d=+32.48% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=94.12; 1d=+0.06%; 5d=+4.05%; 20d=+4.08% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=75500.00; 1d=-0.20%; 5d=+0.98%; 20d=+0.67% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2847.50; 1d=-1.89%; 5d=+0.62%; 20d=-3.70% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.43; 2Y=4.05; 10Y-2Y=0.3799999999999999 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=39.2; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 6758.T price trend | close=3275.00; 1d=-1.36%; 5d=-4.88%; 20d=-11.96% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=70860.00; 1d=-2.61%; 5d=+18.26%; 20d=+50.25% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7102.00; 1d=-0.52%; 5d=+0.77%; 20d=+32.48% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| KWEB price trend | close=25.88; 1d=-2.78%; 5d=-1.22%; 20d=-7.77% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=34.56; 1d=-1.57%; 5d=+0.37%; 20d=-3.71% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=25.66; 1d=-2.28%; 5d=-5.66%; 20d=-16.31% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=111.60; 1d=-0.80%; 5d=-2.11%; 20d=-11.78% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=75.30; 1d=-3.77%; 5d=-2.46%; 20d=-8.34% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=21.73; 1d=-0.64%; 5d=+2.28%; 20d=-7.88% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=39.2; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.43; 2Y=4.05; 10Y-2Y=0.3799999999999999 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| KWEB price trend | close=25.88; 1d=-2.78%; 5d=-1.22%; 20d=-7.77% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=34.56; 1d=-1.57%; 5d=+0.37%; 20d=-3.71% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=25.66; 1d=-2.28%; 5d=-5.66%; 20d=-16.31% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [Move Index Chart - Barchart.com](https://www.barchart.com/stocks/quotes/$MOVE/interactive-chart)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Customizable interactive chart for Move Index with latest real-time price quote, charts, latest news, technical analysis and opinions.

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

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
  - 摘要：Graph and download economic data for CBOE Volatility Index: VIX (VIXCLS) from 1990-01-02 to 2026-06-15 about VIX, volatility, stock market, and USA.

- [Nasdaq-100 Volatility Index (VOLQ)](https://www.nasdaq.com/market-activity/index/volq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Find the latest information on Nasdaq-100 Volatility Index (VOLQ), including data, charts, related news, and more from Nasdaq.com

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Volatility Term Structure chart plots the at-the-money implied volatility across expirations, which are an invaluable tool in determining options strategies based on anticipated...

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [QQQ: Invesco QQQ Trust Option Overview / OptionCharts](https://optioncharts.io/options/QQQ)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View comprehensive QQQ options with our latest charts on volume, open interest, max pain, and implied volatility.

- [Invesco QQQ (QQQ) - Implied Volatility (Mean) (30-Day) - AlphaQuery](https://www.alphaquery.com/stock/QQQ/volatility-option-statistics/30-day/iv-mean)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Implied Volatility (Mean): The forecasted future volatility of the security over the selected time frame, derived from the average of the put and call implied volatilities for o...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://alfred.stlouisfed.org/series?seid=BAMLH0A0HYM2)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：Graph and download revisions to economic data for from 2023-06-19 to 2026-06-15 about option-adjusted spread, yield, interest rate, interest, rate, and USA.

- [USD/JPY Currency Exchange Rate & News - Google Finance](https://www.google.com/finance/beta/quote/USD-JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：USD/JPY spikes lower on US-Iran deal and consolidates ahead of BoJ and FOMC decisions Profile The United States dollar is the official currency of the United States and several...

- [Valuta EX - Currency Converter / Real-Time Exchange Rates](https://valuta.exchange/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

- [Live US Dollar to Yens Exchange Rate - $ 1 USD/JPY Today](https://usd.currencyrate.today/jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest and best $1 US Dollar to Yens rate for FREE. USD/JPY - Live exchange rates, banks, historical data & currency charts.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Current Values - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index?idx=nk225)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Current Values Nikkei calculates and publishes various types of the indexes such as the "Nikkei Stock Average (Nikkei 225)" which is known as a representative Japanese stock mar...

- [Index Information - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index/profile?idx=nk225vi)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：The Nikkei Stock Average Volatility Index are calculated by using prices of Nikkei 225 futures and Nikkei 225 options on the Osaka Exchange (OSE). In the calculation, taking nea...

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

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
## [联合国秘书长称美伊和平协议是‘关键一步’](https://news.un.org/feed/view/en/story/2026/06/1167716) ⭐️ 10.0/10

联合国秘书长安东尼奥·古特雷斯欢迎美伊之间的新和平协议，称其为结束冲突的“关键一步”，同时联合国强调急需开辟穿越霍尔木兹海峡的援助走廊，以防止全球饥饿危机。 该协议标志着重大外交缓和，可能降低军事风险，为解除制裁铺路，稳定全球能源市场，并重塑中东地缘政治，直接影响石油进口国和地区安全。 尽管协议宣布，仍有相互矛盾的报道，且人道主义挑战持续，黎巴嫩的流离失所者仍难以返回家园，凸显即便外交取得进展，区域不稳定依然存在。

rss · UN News · Jun 14, 12:00

**背景**: 霍尔木兹海峡是关键的能源咽喉，全球大量石油经此运输，使其成为价格波动的引爆点。美国退出 2015 年伊核协议（JCPOA）并重新实施制裁后，美伊紧张局势升级；而人道主义走廊是联合国在冲突期间用于运送援助的非军事区。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz - Wikipedia</a></li>
<li><a href="https://www.ebsco.com/research-starters/law/us-sanctions-against-iran">U . S . sanctions against Iran | Law | Research... | EBSCO Research</a></li>
<li><a href="https://en.wikipedia.org/wiki/Humanitarian_corridor">Humanitarian corridor - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#energy`, `#sanctions`

---

<a id="item-3"></a>
## [以色列袭击黎巴嫩医院，冲突加剧人道危机](https://news.un.org/feed/view/en/story/2026/06/1167714) ⭐️ 9.0/10

随着与真主党的敌对行动升级，以色列空袭直接击中黎巴嫩的多家医院，进一步瘫痪该国医疗系统，加剧人道主义紧急状况。 袭击医院违反国际人道法，可能引发国际谴责、联合国安理会行动和制裁讨论。同时，此举也可能导致地区动荡扩大，并因中东紧张局势影响能源市场。 2026 年 3 月开始的黎巴嫩战争已导致以色列入侵黎部分地区。对医疗设施的袭击使本已崩溃的基本服务雪上加霜。

rss · UN News · Jun 12, 12:00

**背景**: 真主党是黎巴嫩什叶派伊斯兰政治和军事组织，与以色列的冲突长达数十年。2023-2024 年战争及停火后，冲突于 2026 年 3 月再次爆发，以色列入侵黎巴嫩。黎巴嫩政府近期试图解除真主党武装，但该组织仍拥有强大军事能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Lebanon_war">2026 Lebanon war - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah–Israel_conflict">Hezbollah–Israel conflict - Wikipedia</a></li>

</ul>
</details>

**标签**: `#military-risk`, `#middle-east`, `#diplomacy`, `#geopolitics`

---

<a id="item-4"></a>
## [联合国：乌克兰 5 月平民伤亡创四年新高](https://news.un.org/feed/view/en/story/2026/06/1167707) ⭐️ 9.0/10

联合国人权观察员报告，乌克兰 5 月平民伤亡人数为 2022 年 4 月以来最高，表明冲突急剧升级。 创纪录的伤亡人数表明战斗加剧，可能引发新的外交压力、制裁讨论和对乌军援增加，同时加剧地缘政治风险和人道主义担忧。 联合国乌克兰人权监测团核实了伤亡情况，并指出袭击影响了居民区和关键基础设施，但最初报告未披露具体数字。

rss · UN News · Jun 12, 12:00

**背景**: 联合国乌克兰人权监测团自 2014 年冲突开始以来一直记录平民伤亡。2022 年 2 月俄罗斯全面入侵后，伤亡人数激增，最高峰为 2022 年 4 月。此后数字有所波动，但 2026 年 5 月的数字是自那以来最高的，标志着重大升级。该监测团目前由丹妮尔·贝尔领导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.government.nl/ministries/ministry-of-foreign-affairs/news/2024/12/11/war-in-ukraine-8-million-for-un-human-rights-monitoring-mission">War in Ukraine : €8 million for UN Human Rights Monitoring Mission</a></li>
<li><a href="https://en.wikipedia.org/wiki/Casualties_of_the_Russo-Ukrainian_war">Casualties of the Russo-Ukrainian war - Wikipedia</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#military-risk`, `#diplomacy`, `#geopolitics`, `#humanitarian`

---

<a id="item-5"></a>
## [欧洲央行公布 2026 年 6 月货币政策决议](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html) ⭐️ 9.0/10

欧洲央行于 2026 年 6 月 11 日公布最新货币政策决议，在通胀和增长动态变化背景下，详细说明了其关键利率立场和前瞻性指引。 鉴于欧元区在国际贸易和金融中的核心地位，欧洲央行的决策直接影响欧元汇率、欧洲债券收益率和全球风险偏好。 决议涵盖主要再融资利率、存款便利利率和边际贷款便利利率，市场仔细审视政策声明以寻找未来举措和通胀前景的信号。

rss · ECB Press Releases · Jun 11, 12:15

**背景**: 欧洲央行是欧元区的中央银行，负责维持价格稳定。其管理委员会大约每六周举行一次会议制定货币政策，其决策对全球市场至关重要，因为欧元是第二大交易货币，且欧元区是主要经济体。

**标签**: `#central-bank`, `#macroeconomics`, `#currency`, `#bonds`, `#europe`

---

<a id="item-6"></a>
## [拉加德谈货币转型 或涉数字欧元](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260615~35e6c6c4de.en.html) ⭐️ 8.0/10

欧洲央行行长克里斯蒂娜·拉加德发表题为‘转型中的货币’的演讲，阐述了货币的演变，并暗示数字货币和货币政策可能的新进展。 此次演讲可能预示着欧洲央行在数字欧元方面的下一步行动，并可能影响对央行数字货币及欧元区货币主权的预期。 虽然全文尚未公开，但该演讲可能涉及潜在数字欧元的设计、时间表及监管问题，以及对金融稳定的影响。

rss · ECB Press Releases · Jun 15, 07:30

**背景**: 欧洲央行自 2020 年起一直探索数字欧元，反映了全球对央行数字货币的广泛关注。拉加德一贯强调欧洲需适应数字支付趋势，同时保护隐私与货币主权。

**标签**: `#central-bank`, `#macroeconomics`, `#currency`, `#europe`, `#financial-stability`

---

<a id="item-7"></a>
## [欧洲央行首席经济学家连恩就欧元区经济前景发表演讲](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260616~8076dabd2c.en.pdf) ⭐️ 7.0/10

2026 年 6 月 16 日，欧洲央行首席经济学家菲利普·R·莱恩就欧元区经济前景发表演讲，可能涉及增长、通胀及货币政策影响。 作为欧洲央行首席经济学家，莱恩的评估可能影响市场对利率、欧元及欧洲资产的预期，从而指引货币政策方向。 演讲于 2026 年 6 月 16 日在欧洲央行网站以 PDF 形式发布。未宣布即时政策变化，但演讲可能透露欧洲央行对近期地缘政治不确定性的反应。

rss · ECB Press Releases · Jun 16, 13:10

**背景**: 菲利普·R·莱恩自 2019 年起担任欧洲央行执行委员会成员兼首席经济学家。欧洲央行负责制定欧元区关键利率，目标是通胀率低于但接近 2%。欧洲央行 2026 年 3 月的预测显示增长具有韧性，但因中东战争不确定性加剧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Philip_R._Lane">Philip R. Lane - Wikipedia</a></li>
<li><a href="https://www.ecb.europa.eu/ecb/decisions/html/cvlane.en.html">Philip R. Lane - European Central Bank</a></li>
<li><a href="https://www.ecb.europa.eu/press/projections/html/ecb.projections202603_ecbstaff~ebe291cd3d.en.html">ECB staff macroeconomic projections for the euro area, March 2026</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`, `#currency`

---

<a id="item-8"></a>
## [海地新多国部队启动打击帮派行动](https://news.un.org/feed/view/en/story/2026/06/1167732) ⭐️ 6.0/10

一支联合国授权的多国安全支助团已在海地展开行动，直接打击控制了太子港大部分地区的强大帮派。 这可能是海地长期安全危机的转折点，一旦成功或将减少暴力和流离失所，失败则可能加剧动荡并削弱外国干预的公信力。 这支由肯尼亚牵头的部队并非联合国维和部队，而是支援海地警方的‘支助团’；其交战规则和时间表尚不明朗，且历史干预成效参差不齐。

rss · UN News · Jun 16, 12:00

**背景**: 自 2017 年联合国海地稳定特派团结束以来，海地帮派暴力不断升级，帮派现控制首都约 80%区域，导致大量平民流离失所。在海地多次请求后，联合国安理会于 2023 年批准了这支多国部队。批评者指出，以往外国干预常侧重短期维稳，而非建设持久制度，致使海地极易重陷暴力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2024/05/1149831">Haiti : Multinational mission and the ‘inexorable... | UN News</a></li>
<li><a href="https://www.dw.com/en/un-security-council-approves-haiti-multinational-force/a-66985438">UN Security Council approves Haiti multinational force</a></li>
<li><a href="https://www.rescue.org/article/haitis-gang-violence-crisis-what-know-and-how-help">Haiti's gang violence crisis: What to know and how to help</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#military-risk`, `#sovereign-risk`, `#united-states`

---

<a id="item-9"></a>
## [欧央行埃尔德森荷兰采访谈政策前景](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260610~439aa97519.en.html) ⭐️ 6.0/10

欧央行执委兼监事会副主席弗兰克·埃尔德森接受荷兰《财经日报》采访，重点讨论了欧元区货币政策前景与金融稳定。 采访可能预示欧央行政策调整，影响利率预期和银行监管情绪；若偏离当前立场，可能冲击金融市场和欧元区经济状况。 采访内容尚未公开，但可能涉及通胀走势、经济增长和金融系统风险；鉴于埃尔德森的监管职责，预计会就银行监管和风险管理发表评论。

rss · ECB Press Releases · Jun 10, 14:00

**背景**: 弗兰克·埃尔德森自 2020 年起任欧央行执委，负责法律事务并兼任监事会副主席。欧央行每半年发布《金融稳定评估》以评估系统性风险。央行通过前瞻性指引塑造市场对未来货币政策的预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Frank_Elderson">Frank Elderson - Wikipedia</a></li>
<li><a href="https://www.ecb.europa.eu/press/financial-stability-publications/fsr/html/index.en.html">Financial Stability Review - European Central Bank</a></li>
<li><a href="https://www.publicnow.com/view/CE02421D8CB89061028A18B20E6F1D3FFE24AD1C">ECB - European Central Bank (via Public) / Financial ...</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#financial-stability`, `#europe`

---

<a id="item-10"></a>
## [FSB 发布 AI 负责任采用良好实践咨询报告](https://www.fsb.org/2026/06/sound-practices-for-responsible-adoption-of-artificial-intelligence-ai-consultation-report/) ⭐️ 6.0/10

金融稳定委员会（FSB）发布了一份咨询报告，为各类金融机构负责任地采用人工智能提出了良好实践建议。 由于 FSB 制定全球金融监管标准，这些良好实践可能会统一各司法管辖区的人工智能治理，降低操作风险，并塑造金融领域人工智能的未来监管格局。 该报告是一份咨询文件，邀请利益相关方反馈；适用于所有金融机构，包括银行、保险公司和资产管理公司，但不具备约束力。

rss · Financial Stability Board News · Jun 10, 08:00

**背景**: FSB 是一个国际机构，负责监督全球金融体系并提出建议。它成立于 2008 年金融危机后，包括 G20 经济体，制定的非约束性标准通常会影响力各国监管。其先前工作包括加密资产和运营韧性方面的指导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Financial_Stability_Board">Financial Stability Board</a></li>
<li><a href="https://www.fsb.org/">Financial Stability Board - Promoting global financial ...</a></li>

</ul>
</details>

**标签**: `#financial-stability`, `#central-bank`, `#global-markets`, `#macroeconomics`

---