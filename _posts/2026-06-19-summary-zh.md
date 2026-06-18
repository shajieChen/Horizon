---
layout: default
title: "Horizon Summary: 2026-06-19 (ZH)"
date: 2026-06-19
lang: zh
---

> From 43 items, 10 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [伊美协议前景下，联合国吁开通霍尔木兹援助通道](#item-2) ⭐️ 9.0/10
3. [美联储发布 FOMC 声明及经济预测](#item-3) ⭐️ 9.0/10
4. [世卫组织和巴西敦促敲定全球大流行病协议](#item-4) ⭐️ 7.0/10
5. [欧洲央行莱恩探讨欧元区经济前景](#item-5) ⭐️ 7.0/10
6. [联合国支持的帮派打击部队在海地开始行动](#item-6) ⭐️ 6.0/10
7. [俄罗斯袭击乌克兰致平民伤亡，文化遗产受损](#item-7) ⭐️ 6.0/10
8. [欧洲央行官员齐波洛内介绍数字欧元最新进展](#item-8) ⭐️ 6.0/10
9. [拉加德关于数字欧元转型的演讲](#item-9) ⭐️ 6.0/10
10. [美联储提议稳定币发行商须建立客户身份识别程序](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 18, 22:56

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
| US Mega Cap Basket | US | bullish 38/31/31 | neutral 33/33/34 | neutral 33/33/34 | high |
| Japan Equity Basket | JP | bullish 38/31/31 | bullish 38/31/31 | bullish 39/30/31 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=30660.75; 1d=+3.28%; 5d=+4.06%; 20d=+4.32% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=30406.19; 1d=+2.48%; 5d=+3.26%; 20d=+3.78% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=740.62; 1d=+2.51%; 5d=+3.28%; 20d=+3.85% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=3.2%; implied_move=0.1%; put/call OI=2.0085277038623897 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=37.5; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| NQ=F price trend | close=30660.75; 1d=+3.28%; 5d=+4.06%; 20d=+4.32% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=30406.19; 1d=+2.48%; 5d=+3.26%; 20d=+3.78% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=740.62; 1d=+2.51%; 5d=+3.28%; 20d=+3.85% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| MSFT price trend | close=379.40; 1d=+0.13%; 5d=-2.80%; 20d=-9.70% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=400.49; 1d=+1.04%; 5d=+0.34%; 20d=-4.02% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=368.03; 1d=+1.17%; 5d=+2.87%; 20d=-5.31% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=577.22; 1d=+1.70%; 5d=+1.64%; 20d=-4.51% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=298.01; 1d=+0.70%; 5d=+0.81%; 20d=-1.40% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=210.69; 1d=+2.95%; 5d=+2.84%; 20d=-5.61% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| NVDA options surface | ATM IV=4.6%; implied_move=0.3%; put/call OI=0.9514358377823172 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=7.1%; implied_move=0.3%; put/call OI=0.6464290444659466 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=8.1%; implied_move=0.3%; put/call OI=0.9373701420108694 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=6.9%; implied_move=0.2%; put/call OI=0.4285838760569438 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=6.0%; implied_move=0.2%; put/call OI=0.8697250515584615 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=9.6%; implied_move=0.4%; put/call OI=0.5202035010070442 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| MSFT insider filings | recent Form4 count=729 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| NVDA insider filings | recent Form4 count=561 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=37.5; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| MSFT price trend | close=379.40; 1d=+0.13%; 5d=-2.80%; 20d=-9.70% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=400.49; 1d=+1.04%; 5d=+0.34%; 20d=-4.02% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=368.03; 1d=+1.17%; 5d=+2.87%; 20d=-5.31% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| EWJ price trend | close=96.26; 1d=+1.92%; 5d=+4.99%; 20d=+6.11% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7189.00; 1d=+4.49%; 5d=+12.79%; 20d=+19.04% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=76080.00; 1d=+4.74%; 5d=+20.00%; 20d=+55.90% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3250.00; 1d=-1.10%; 5d=-3.53%; 20d=-8.55% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77520.00; 1d=+2.54%; 5d=+8.77%; 20d=+0.73% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2793.50; 1d=-0.59%; 5d=+1.67%; 20d=-6.20% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=37.5; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| EWJ price trend | close=96.26; 1d=+1.92%; 5d=+4.99%; 20d=+6.11% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7189.00; 1d=+4.49%; 5d=+12.79%; 20d=+19.04% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=76080.00; 1d=+4.74%; 5d=+20.00%; 20d=+55.90% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 1810.HK price trend | close=24.58; 1d=-3.30%; 5d=-4.88%; 20d=-18.45% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=440.20; 1d=-1.17%; 5d=-3.72%; 20d=-3.30% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=21.28; 1d=-0.28%; 5d=-1.17%; 20d=-9.45% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=104.90; 1d=-1.87%; 5d=-2.33%; 20d=-20.38% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=25.24; 1d=-0.55%; 5d=-5.01%; 20d=-10.24% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=71.80; 1d=-3.49%; 5d=-8.07%; 20d=-13.34% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=37.5; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
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
| 1810.HK price trend | close=24.58; 1d=-3.30%; 5d=-4.88%; 20d=-18.45% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=440.20; 1d=-1.17%; 5d=-3.72%; 20d=-3.30% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=21.28; 1d=-0.28%; 5d=-1.17%; 20d=-9.45% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

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

- [NDAQ Implied Volatility Chart Nasdaq - MarketChameleon.com](https://marketchameleon.com/Overview/NDAQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：View volatility charts for Nasdaq (NDAQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the interactive...

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

- [VIX S&P 500 Volatility and MOVE Treasury Volatility / StreetStats](https://streetstats.finance/markets/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：This page provides current and historical values for key volatility metrics, including the CBOE Volatility Index (VIX) for stock market volatility and the Merrill Lynch Option V...

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX Index / CBOE Volatility (indexcboe: vix) - Investing.com](https://www.investing.com/indices/volatility-s-p-500)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Live VIX Index quote, charts, historical data, analysis and news. View VIX (CBOE volatility index) price, based on real time data from S&P 500 options.

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [BAMLH0A0HYM2: US High Yield OAS Daily Data - eco3min.fr](https://eco3min.fr/en/credit-spreads-recession-risk-dataset/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：BAMLH0A0HYM2 is the ICE BofA US High Yield Index Option-Adjusted Spread — the daily market-priced premium that below-investment-grade US corporate bonds pay over equivalent-matu...

- [ICE BofA Single-B US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A2HYB/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：For more data, go to the source. This data represents the Option-Adjusted Spread (OAS) of the ICE BofA US Corporate B Index, a subset of the ICE BofA US High Yield Master II Ind...

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [QQQ Options - Live IV, Flow, Greeks & Analysis / ImpliedOptions ...](https://impliedoptions.com/ticker/qqq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Trade QQQ options with real-time implied volatility, IV rank, options flow, and Greeks. Analyze QQQ calls and puts with our free calculator and strategy builder.

- [QQQ Options Volatility — NASDAQ:QQQ — TradingView](https://www.tradingview.com/symbols/NASDAQ-QQQ/options-volatility/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Analyze Invesco QQQ Trust, Series 1 puts and calls to craft a reliable strategy and optimize your options trading with implied volatility charts.

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

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

- [USD/JPY — US Dollar to Japanese Yen Live Exchange Rate](https://www.live-rates.com/rates/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：The US Dollar (USD) is the world's primary reserve currency and the most traded currency on the foreign exchange market; the Japanese Yen (JPY) is the currency of Japan and the...

- [Valuta EX - Currency Converter / Real-Time Exchange Rates](https://valuta.exchange/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

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
## [伊美协议前景下，联合国吁开通霍尔木兹援助通道](https://news.un.org/feed/view/en/story/2026/06/1167717) ⭐️ 9.0/10

联合国强调迫切需要开通霍尔木兹海峡援助走廊以防止全球饥饿危机，同时据报道伊朗与美国正敲定和平协议，国际原子能机构(IAEA)表示愿协助核查伊朗核计划。 这可能稳定全球最关键能源咽喉，有望缓解油价波动和化肥供应中断，而美伊和平协议将重塑中东地缘政治和全球能源市场格局。 IAEA 随时准备核查伊朗核计划这一关键症结；但人道协调厅(OCHA)指出，尽管达成协议，黎巴嫩流离失所者返乡仍面临困难。

rss · UN News · Jun 15, 12:00

**背景**: 霍尔木兹海峡是波斯湾唯一海上通道，承载全球约 25%的海运石油、20%的液化天然气及 35%至 40%的化肥运输。近年美伊紧张局势曾引发封锁威胁。IAEA 是联合国下属核监督机构，负责监测核计划并核查国际协议执行情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://unctad.org/publication/strait-hormuz-disruptions-implications-global-trade-and-development">Strait of Hormuz disruptions: Implications for global trade and development | UN Trade and Development (UNCTAD)</a></li>
<li><a href="https://www.thinkbrg.com/insights/publications/dire-straits-the-hidden-supply-chains-of-the-strait-of-hormuz/">Dire Straits: The Hidden Supply Chains of the Strait of Hormuz | Insights | BRG</a></li>
<li><a href="https://en.yna.co.kr/view/AEN20260613003300315">IAEA chief highlights verification role in potential U.S.- Iran nuclear ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#supply-chain`, `#middle-east`

---

<a id="item-3"></a>
## [美联储发布 FOMC 声明及经济预测](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm) ⭐️ 9.0/10

美联储在 6 月 16-17 日会议后发布了 FOMC 声明和更新的经济预测，阐述了委员会对货币政策和经済前景的看法。 声明和预测是金融市场的重要驱动因素，因其暗示利率的可能路径，影响债券收益率、货币价值和股市；任何意外措辞都可能引发显著重新定价。 声明包括联邦基金利率目标区间和前瞻指引，而经济预测摘要展示了委员们对 2028 年之前经济增长、失业率、通胀和适宜政策利率路径的个人预测。

rss · Federal Reserve Press Releases · Jun 17, 18:00

**背景**: 美联储是美国的中央银行，成立于 1913 年，承担促进最大就业和稳定物价的双重使命。联邦公开市场委员会是其货币政策决策机构，每年举行八次会议设定联邦基金利率目标。会后声明和经济预测是引导市场预期的关键沟通工具。联邦基金利率影响整个经济的借贷成本，从抵押贷款到公司债券均受影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Reserve">Federal Reserve</a></li>
<li><a href="https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm">The Federal Reserve Board of Governors in Washington DC.</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#united-states`, `#global-markets`, `#bonds`

---

<a id="item-4"></a>
## [世卫组织和巴西敦促敲定全球大流行病协议](https://news.un.org/feed/view/en/story/2026/06/1167721) ⭐️ 7.0/10

世卫组织与巴西周一发表联合信函，敦促世界各国领导人最终敲定国际《大流行病协议》，以加强全球对未来卫生危机的防范。 敲定该协议将增强全球卫生安全，降低未来大流行病造成严重经济冲击的风险，并释放多边合作信号，从而安抚金融市场和供应链利益相关方。 已获世界卫生大会委员会批准的《世卫组织大流行病协议》仍须正式通过。该协议为国际合作提供框架，但其全面实施有赖各国批准。

rss · UN News · Jun 15, 12:00

**背景**: 《世卫组织大流行病协议》(WHOPA)源于新冠疫情的教训，旨在改进全球在大流行病预防、准备和应对方面的协调。历经多年谈判，成员国于 5 月 19 日在世界卫生大会委员会上批准了草案文本，为正式通过铺平道路。巴西一直是积极的倡导者，反映出全球对具有约束力的卫生安全措施日益增长的推动力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pandemic_Agreement">Pandemic Agreement</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2o4MzQzOURSRXNNcGN1UGpXS01DZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en">Google News - News about Pandemic Agreement - Overview</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#macroeconomics`, `#supply-chain`, `#financial-stability`, `#global-markets`

---

<a id="item-5"></a>
## [欧洲央行莱恩探讨欧元区经济前景](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260616~8076dabd2c.en.pdf) ⭐️ 7.0/10

欧洲央行执行委员会委员菲利普·莱恩于 2026 年 6 月 16 日发表演讲，讨论欧元区经济前景，可能更新了对增长和通胀的评估。 莱恩的言论可能暗示欧洲央行货币政策立场的变化，从而影响市场对利率、欧元和欧洲资产价格的预期。 作为管委会成员，莱恩对通胀驱动因素和增长风险的看法可能预示未来的政策辩论；他的演讲可能包含前瞻性分析，但未宣布具体政策措施。

rss · ECB Press Releases · Jun 16, 13:10

**背景**: 欧洲央行负责制定欧元区货币政策，欧元区目前有 21 个欧盟成员国。作为首席经济学家，菲利普·莱恩在塑造支撑利率决策的经济分析方面发挥关键作用。自 2022 年 7 月以来，欧洲央行激进加息以对抗高通胀，但随着通胀缓和，2024 年开始降息。2026 年初，欧元区面临温和增长和接近目标的通胀，并存在持续的不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/Euro_area">Euro area</a></li>
<li><a href="https://en.wikipedia.org/wiki/Monetary_policy">Monetary policy</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`, `#currency`

---

<a id="item-6"></a>
## [联合国支持的帮派打击部队在海地开始行动](https://news.un.org/feed/view/en/story/2026/06/1167732) ⭐️ 6.0/10

从多国安全支援团演变而来的新型多国安全部队“帮派打击部队”（GSF）已开始在海地打击势力庞大的帮派，这可能成为该国危机的转折点。 若行动成功，可能恢复海地稳定，降低主权风险并重塑加勒比地区的外交格局，但直接市场影响有限。若失败将进一步削弱国际社会在危机干预中的信誉。 GSF 由联合国安理会第 2793 号决议授权，由肯尼亚领导，成员包括加勒比国家、孟加拉国、贝宁和乍得的人员；它与海地警察和武装部队协同行动，计划规模为 5500 人。

rss · UN News · Jun 16, 12:00

**背景**: 自 2018 年以来，海地深陷帮派暴力，帮派控制了首都太子港大部分地区。包括联合国稳定特派团在内的以往国际干预均未能建立持久安全。多国安全支援团于 2023 年获批，2024 年年中首次部署，但成效不足，遂于 2025 年底升级为更强的帮派打击部队。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multinational_Security_Support_Mission_in_Haiti">Multinational Security Support Mission in Haiti</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gang_Suppression_Force">Gang Suppression Force - Wikipedia</a></li>
<li><a href="https://news.un.org/en/story/2024/09/1155151">Security Council renews Haiti mission mandate, calls for more action ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#sovereign-risk`, `#haiti`

---

<a id="item-7"></a>
## [俄罗斯袭击乌克兰致平民伤亡，文化遗产受损](https://news.un.org/feed/view/en/story/2026/06/1167718) ⭐️ 6.0/10

联合国周一报告，俄罗斯军队连夜对基辅、哈尔科夫等地发动袭击，造成数名平民死亡、数十人受伤，并损毁一处文化遗产。 该事件突显了战争中持续的人员伤亡和文化破坏，可能加剧国际谴责并引发人道援助呼吁，但作为常态更新无直接政策变动。 联合国提供了伤亡数字并确认文化遗产受损，但初步报告中未披露具体数字和遗产名称。

rss · UN News · Jun 15, 12:00

**背景**: 自 2022 年 2 月俄罗斯全面入侵以来，已有数千平民伤亡，众多文化遗址遭到破坏或摧毁。联合国一贯谴责针对平民和文化遗产的袭击，认为其可能违反国际人道法，常引发追责和战争罪调查的呼声。

**标签**: `#russia-ukraine`, `#military-risk`, `#diplomacy`, `#geopolitics`

---

<a id="item-8"></a>
## [欧洲央行官员齐波洛内介绍数字欧元最新进展](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260618~da08e71469.en.pdf) ⭐️ 6.0/10

2026 年 6 月 18 日，欧洲央行执行委员会委员皮耶罗·齐波洛内发表演讲，阐述了数字欧元项目的设计进展及其对货币政策和金融稳定的潜在影响。 该演讲表明欧洲央行正加速推进数字欧元，这可能重塑支付体系、影响银行中介业务，并在全球 CBDC 竞赛中提升欧元的国际地位。 数字欧元将不使用区块链或分布式账本技术；截至 2025 年，欧洲央行计划在欧盟 2026 年通过立法后，于 2027 年中开始测试，力争 2029 年首次发行。

rss · ECB Press Releases · Jun 18, 12:00

**背景**: 数字欧元是欧洲央行于 2021 年启动的央行数字货币（CBDC）项目，旨在通过安全、由央行发行的电子支付工具补充现金和银行存款。经过调查阶段后，欧元体系于 2023 年 11 月进入准备阶段，随后推进至设计和测试阶段。CBDC 是国家发行的数字货币，有别于加密货币；全球已有 130 多个国家在探索，引发了关于隐私、金融稳定和银行脱媒的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_euro">Digital euro</a></li>
<li><a href="https://www.ecb.europa.eu/euro/digital_euro/html/index.en.html">Digital euro - European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#currency`, `#financial-stability`, `#europe`, `#macroeconomics`

---

<a id="item-9"></a>
## [拉加德关于数字欧元转型的演讲](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260615~35e6c6c4de.en.html) ⭐️ 6.0/10

欧洲央行行长克里斯蒂娜·拉加德发表了题为《转型中的货币》的演讲，可能讨论了数字欧元项目和央行货币的演变。 该演讲表明欧洲央行继续致力于数字欧元，这可能会重塑欧元区支付系统和货币政策实施，并有可能在 2029 年前发行。 虽然演讲全文未公开，但可能涉及隐私、离线使用等技术细节，或数字欧元发行前所需的立法步骤。

rss · ECB Press Releases · Jun 15, 07:30

**背景**: 欧洲央行于 2021 年 7 月启动数字欧元项目，并于 2023 年 11 月进入准备阶段。截至 2025 年，管理委员会决定推进，目标是在欧盟立法通过后于 2029 年准备就绪。拉加德自 2019 年起担任欧洲央行行长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_euro">Digital euro</a></li>
<li><a href="https://www.ecb.europa.eu/euro/digital_euro/html/index.en.html">Digital euro - European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#digital-currency`, `#europe`, `#macroeconomics`, `#financial-stability`

---

<a id="item-10"></a>
## [美联储提议稳定币发行商须建立客户身份识别程序](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260618a.htm) ⭐️ 6.0/10

美联储正在就一项提案征求公众意见，该提案要求某些支付稳定币发行商建立并维护有效的客户身份识别程序。 这标志着对稳定币更严格的监管，稳定币对加密市场和跨境支付至关重要，可能影响金融稳定、系统性风险以及稳定币的采用。 提案针对“某些支付稳定币发行商”，但未明确具体范围，且仍需根据公众意见进行调整。

rss · Federal Reserve Press Releases · Jun 18, 13:00

**背景**: 稳定币是与法币等稳定资产挂钩的数字资产，广泛用于加密交易和支付。美联储长期担忧其洗钱、消费者保护和金融稳定风险。客户身份识别程序是《银行保密法》下反洗钱和了解客户规则的核心，该提案符合全球加强数字资产监管的趋势。

**标签**: `#central-bank`, `#financial-stability`, `#united-states`, `#global-markets`

---