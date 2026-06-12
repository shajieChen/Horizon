---
layout: default
title: "Horizon Summary: 2026-06-13 (ZH)"
date: 2026-06-13
lang: zh
---

> From 41 items, 10 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [霍尔木兹海峡油轮遇袭，三船员丧生，联合国警示冲击扩大](#item-2) ⭐️ 9.0/10
3. [联合国安理会辩论中东政治解决方案，美伊停火脆弱](#item-3) ⭐️ 9.0/10
4. [欧央行货币政策声明及拉加德与武伊契奇问答](#item-4) ⭐️ 9.0/10
5. [以色列再袭泰尔致八人死亡，联合国估黎巴嫩损失超 3.65 亿美元](#item-5) ⭐️ 8.0/10
6. [联合国称乌克兰 5 月平民伤亡人数创四年新高](#item-6) ⭐️ 7.0/10
7. [联合国警告乌克兰战争进入最致命阶段](#item-7) ⭐️ 7.0/10
8. [联合国人权高专：美对古制裁致儿童死亡，须取消](#item-8) ⭐️ 7.0/10
9. [金融稳定理事会发布 AI 负责任采用咨询报告](#item-9) ⭐️ 6.0/10
10. [FSB 宣布举办监管现代化研讨会](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 12, 22:48

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
| Hong Kong Equity Basket | HK | bullish 38/31/31 | neutral 33/33/34 | neutral 33/33/34 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=29677.75; 1d=+0.72%; 5d=+2.24%; 20d=-0.03% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=721.34; 1d=+0.59%; 5d=+2.31%; 20d=+0.22% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29635.95; 1d=+0.64%; 5d=+2.34%; 20d=+0.19% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=6.4%; implied_move=0.2%; put/call OI=1.4076396190455054 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.48; 2Y=4.09; 10Y-2Y=0.39000000000000057 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=34.0; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| NQ=F price trend | close=29677.75; 1d=+0.72%; 5d=+2.24%; 20d=-0.03% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=721.34; 1d=+0.59%; 5d=+2.31%; 20d=+0.22% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29635.95; 1d=+0.64%; 5d=+2.34%; 20d=+0.19% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| META price trend | close=566.98; 1d=-0.26%; 5d=-4.39%; 20d=-8.32% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=390.74; 1d=+0.10%; 5d=-6.22%; 20d=-4.36% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=238.55; 1d=-1.23%; 5d=-3.04%; 20d=-10.73% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=406.43; 1d=+1.82%; 5d=+3.95%; 20d=-8.32% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=359.68; 1d=+0.53%; 5d=-2.34%; 20d=-10.27% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=205.19; 1d=+0.16%; 5d=+0.04%; 20d=-12.86% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| GOOGL options surface | ATM IV=3.8%; implied_move=0.1%; put/call OI=0.5263730587032742 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=7.8%; implied_move=0.3%; put/call OI=0.5744515460355847 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=3.0%; implied_move=0.1%; put/call OI=0.5685272988973629 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=5.0%; implied_move=0.2%; put/call OI=0.3959861873477985 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=5.0%; implied_move=0.2%; put/call OI=0.3269679819527447 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=7.1%; implied_move=0.4%; put/call OI=0.49170956405244953 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| NVDA insider filings | recent Form4 count=561 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.48; 2Y=4.09; 10Y-2Y=0.39000000000000057 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| MSFT insider filings | recent Form4 count=738 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
| META price trend | close=566.98; 1d=-0.26%; 5d=-4.39%; 20d=-8.32% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=390.74; 1d=+0.10%; 5d=-6.22%; 20d=-4.36% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=238.55; 1d=-1.23%; 5d=-3.04%; 20d=-10.73% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 7203.T price trend | close=2775.50; 1d=+1.02%; 5d=-2.61%; 20d=-10.03% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=68000.00; 1d=+7.26%; 5d=+14.38%; 20d=+35.22% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=72620.00; 1d=+1.89%; 5d=-6.98%; 20d=-5.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6472.00; 1d=+1.54%; 5d=-12.85%; 20d=+12.65% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3292.00; 1d=-2.29%; 5d=-7.50%; 20d=-7.94% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.71; 1d=+0.57%; 5d=+2.19%; 20d=+0.71% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=34.0; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.48; 2Y=4.09; 10Y-2Y=0.39000000000000057 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| 7203.T price trend | close=2775.50; 1d=+1.02%; 5d=-2.61%; 20d=-10.03% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=68000.00; 1d=+7.26%; 5d=+14.38%; 20d=+35.22% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=72620.00; 1d=+1.89%; 5d=-6.98%; 20d=-5.91% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 0700.HK price trend | close=463.60; 1d=+1.40%; 5d=+2.29%; 20d=+1.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=26.20; 1d=+1.39%; 5d=-5.76%; 20d=-17.40% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=77.90; 1d=-0.26%; 5d=-2.56%; 20d=-9.10% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=112.60; 1d=+3.40%; 5d=-2.76%; 20d=-13.45% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=22.00; 1d=+0.55%; 5d=+0.82%; 20d=-9.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.49; 1d=-0.30%; 5d=+0.42%; 20d=-9.28% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.48; 2Y=4.09; 10Y-2Y=0.39000000000000057 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=34.0; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 跨层分歧信息有限，后续需补充更多波动与事件市场数据。

**Time stratification**
- 1日：1日篮子收益与5日均线结构偏强
- 1周：有效交易信号不足，使用保守基准分布。
- 1月：有效交易信号不足，使用保守基准分布。

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | medium |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1月 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 0700.HK price trend | close=463.60; 1d=+1.40%; 5d=+2.29%; 20d=+1.91% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=26.20; 1d=+1.39%; 5d=-5.76%; 20d=-17.40% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=77.90; 1d=-0.26%; 5d=-2.56%; 20d=-9.10% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

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

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [Cboe Nasdaq-100 Implied Volatil (^CNIV05) - Yahoo Finance](https://finance.yahoo.com/quote/%5ECNIV05/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Find the latest information on Cboe Nasdaq-100 Implied Volatil (^CNIV05) including data, charts, related news and more from Yahoo Finance

- [Move Index Chart - Barchart.com](https://www.barchart.com/stocks/quotes/$MOVE/interactive-chart)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Customizable interactive chart for Move Index with latest real-time price quote, charts, latest news, technical analysis and opinions.

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [BAMLH0A0HYM2: US High Yield OAS Daily Data - eco3min.fr](https://eco3min.fr/en/credit-spreads-recession-risk-dataset/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：BAMLH0A0HYM2 is the ICE BofA US High Yield Index Option-Adjusted Spread — the daily market-priced premium that below-investment-grade US corporate bonds pay over equivalent-matu...

- [US High Yield Master II Option-Adjusted Spread (Market Dail…](https://ycharts.com/indicators/us_high_yield_master_ii_optionadjusted_spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：View market daily updates and historical trends for US High Yield Master II Option-Adjusted Spread. from United States. Source: Bank of America Merrill Ly…

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [QQQ Options - Live IV, Flow, Greeks & Analysis / ImpliedOptions ...](https://impliedoptions.com/ticker/qqq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Trade QQQ options with real-time implied volatility, IV rank, options flow, and Greeks. Analyze QQQ calls and puts with our free calculator and strategy builder.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Current Values - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index?idx=nk225)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Current Values Nikkei calculates and publishes various types of the indexes such as the "Nikkei Stock Average (Nikkei 225)" which is known as a representative Japanese stock mar...

- [Nikkei Average Volatility (^NKVI.OS) - Yahoo Finance](https://finance.yahoo.com/quote/%5ENKVI.OS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Find the latest information on Nikkei Average Volatility (^NKVI.OS) including data, charts, related news and more from Yahoo Finance

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [EWJ / iShares MSCI Japan ETF Overview / MarketWatch](https://www.marketwatch.com/investing/fund/ewj)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ / A complete iShares MSCI Japan ETF exchange traded fund overview by MarketWatch. View the latest ETF prices and news for better ETF investing.

- [USD/JPY (USDJPY=X) Live Rate, Chart & News - Yahoo Finance](https://finance.yahoo.com/quote/USDJPY=X/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Find the latest USD/JPY (USDJPY=X) currency exchange rate, plus historical data, charts, relevant news and more

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
## [霍尔木兹海峡油轮遇袭，三船员丧生，联合国警示冲击扩大](https://news.un.org/feed/view/en/story/2026/06/1167697) ⭐️ 9.0/10

周三，霍尔木兹海峡附近一艘油轮遭袭，造成三名印度船员死亡，引发联合国警告能源市场、航运和全球供应链风险加剧。 霍尔木兹海峡承载全球约 20%的石油贸易，此次致命袭击加剧了供应中断、能源价格飙升和更广泛经济冲击的担忧，可能影响全球通胀和地缘政治稳定。 三名遇难船员为印度籍，袭击发生于地区军事紧张持续之际；联合国敦促所有船只'高度谨慎'，并呼吁各方避免事态进一步升级。

rss · UN News · Jun 11, 12:00

**背景**: 霍尔木兹海峡是连接波斯湾与阿曼湾的狭窄水道，历史上一直是关键贸易通道，目前承载全球约五分之一的原油贸易和大量液化天然气。2026 年美伊紧张局势，包括军事打击和相互指责，加大了重大供应中断的风险，联合国贸发会议和伍德麦肯兹警告称，长期关闭可能引发数十年来最严重的能源供应冲击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://maritimeducation.com/strait-of-hormuz-geography-navigation-strategic-importance-and-maritime-challenges/">Strait of Hormuz: Geography, Navigation, Strategic Importance, and ...</a></li>
<li><a href="https://unctad.org/publication/strait-hormuz-disruptions-implications-global-trade-and-development">Strait of Hormuz disruptions: Implications for global trade ...</a></li>
<li><a href="https://news.un.org/en/story/2026/05/1167432">Uncertainty continues over safety in the Strait of Hormuz</a></li>

</ul>
</details>

**标签**: `#energy`, `#supply-chain`, `#military-risk`, `#middle-east`, `#commodities`

---

<a id="item-3"></a>
## [联合国安理会辩论中东政治解决方案，美伊停火脆弱](https://news.un.org/feed/view/en/story/2026/06/1167689) ⭐️ 9.0/10

联合国安理会举行了关于推进中东政治解决方案的高级别公开辩论，目前美伊停火脆弱，联合国秘书长警告称局势升级将在全球范围内产生影响。 美伊停火脆弱、联合国辩论凸显两国冲突风险，可能严重威胁全球能源市场、航运安全与国际稳定。 停火协议以伊朗重开霍尔木兹海峡为条件，近期仍发生海军冲突；安理会五个常任理事国拥有否决权，在中东问题上常现分歧。

rss · UN News · Jun 10, 12:00

**背景**: 联合国安理会是联合国维护国际和平的主要机构，五个常任理事国（美、英、法、俄、中）拥有否决权。美伊紧张局势于 2026 年初升级，2026 年 4 月达成脆弱停火，以伊朗保持霍尔木兹海峡开放为条件——该海峡是关键的石油运输咽喉。此外，中东地区还面临加沙和也门等持续冲突，使政治解决更加复杂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://www.bbc.com/news/articles/c626zyywxjno">Trump says US - Iran ceasefire still in place after exchange of fire in...</a></li>
<li><a href="https://www.securitycouncilreport.org/whatsinblue/2026/06/high-level-open-debate-on-advancing-political-solutions-in-the-middle-east.php">High-level Open Debate on Advancing Political Solutions in ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`, `#energy`

---

<a id="item-4"></a>
## [欧央行货币政策声明及拉加德与武伊契奇问答](https://www.ecb.europa.eu//press/press_conference/monetary-policy-statement/2026/html/ecb.is260611~372040d313.en.html) ⭐️ 9.0/10

欧洲央行发布了 2026 年 6 月货币政策声明，并由行长拉加德与管委会成员武伊契奇举行了新闻发布会，沟通了最新利率决议及政策前景的前瞻指引。 该决议直接影响欧元区借贷成本、欧元汇率和全球债市。市场参与者基于前瞻指引重新定价利率预期，影响整个欧元区金融状况。 新闻发布会由行长拉加德和克罗地亚央行行长武伊契奇共同出席，体现了欧央行的沟通策略。前瞻指引为关键利率（包括存款便利利率）的未来路径提供了线索。

rss · ECB Press Releases · Jun 11, 13:00

**背景**: 欧洲央行是欧元的中央银行，负责维护欧元区价格稳定。前瞻指引是央行沟通工具，用于预示货币政策的可能未来走向，帮助锚定市场预期。欧央行的货币政策由管理委员会制定，该委员会包括六名执行董事会成员和 20 个欧元区成员国央行行长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forward_guidance">Forward guidance - Wikipedia</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#currencies`, `#bonds`

---

<a id="item-5"></a>
## [以色列再袭泰尔致八人死亡，联合国估黎巴嫩损失超 3.65 亿美元](https://news.un.org/feed/view/en/story/2026/06/1167685) ⭐️ 8.0/10

尽管停火协议仍在生效，以色列对黎巴嫩南部城市泰尔发动新一轮空袭，造成八人死亡；同时，联合国牵头的快速损失评估于周二发布，估计自最近局势升级以来，贝鲁特和黎巴嫩山的建筑损坏超过 3.65 亿美元。 空袭破坏了 2024 年 11 月达成的脆弱停火协议，增加了全面冲突再起和地区不稳定的风险，而巨大的经济损失凸显了人道主义危机，可能给国际援助和外交调解带来压力。 停火由美国等调解方于 2024 年 11 月 27 日促成，但违规行为持续发生；损失评估由联合国开发计划署与黎巴嫩科研和军事机构共同完成，仅涵盖建筑，实际总损失可能远高于此。

rss · UN News · Jun 9, 12:00

**背景**: 泰尔是黎巴嫩南部历史悠久的腓尼基港口城市，已成为冲突流离失所者的避难所。停火旨在停止自 2023 年 10 月 8 日真主党袭击以色列以来不断升级的敌对行动，冲突于 2024 年 10 月 1 日演变为以色列的地面入侵。联合国损失报告仅量化建筑损毁，但更广泛的经济影响还包括农业、基础设施和流离失所成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tyre,_Lebanon">Tyre, Lebanon - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/2024_Israel–Lebanon_ceasefire_agreement">2024 Israel–Lebanon ceasefire agreement - Wikipedia</a></li>
<li><a href="https://www.undp.org/arab-states/press-releases/rapid-damage-assessment-estimates-over-us365-million-building-damage-across-beirut-and-mount-lebanon">Rapid damage assessment estimates over US$365 Million in building damage across Beirut and Mount Lebanon | United Nations Development Programme</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#military-risk`, `#middle-east`, `#diplomacy`, `#sovereign-risk`

---

<a id="item-6"></a>
## [联合国称乌克兰 5 月平民伤亡人数创四年新高](https://news.un.org/feed/view/en/story/2026/06/1167707) ⭐️ 7.0/10

联合国调查人员周五报告称，乌克兰 5 月份的平民死伤人数达到自全面入侵初期四年来单月最高水平。 这一创纪录的平民伤亡凸显了战争日益加剧的人道代价，可能迫使西方盟友加强对乌克兰的军事支持并对俄罗斯实施更严厉的制裁，同时也将使和平谈判复杂化。 联合国声明强调 5 月伤亡数字超过了 2022 年俄乌战争初期以来的任何月份，但简短的公告未披露具体数字。

rss · UN News · Jun 12, 12:00

**背景**: 联合国乌克兰人权监测团自 2022 年 2 月俄罗斯全面入侵以来系统记录了平民伤亡情况。每月伤亡数字随前线城市战斗强度波动。2026 年 5 月成为四年来伤亡最重月份，表明冲突的人道影响显著升级，可能与军事行动加剧有关。

**标签**: `#russia-ukraine`, `#diplomacy`, `#geopolitics`, `#military-risk`, `#united-nations`

---

<a id="item-7"></a>
## [联合国警告乌克兰战争进入最致命阶段](https://news.un.org/feed/view/en/story/2026/06/1167674) ⭐️ 7.0/10

联合国副秘书长罗斯玛丽·迪卡洛向安理会通报，乌克兰战争已升级至 2022 年入侵以来最致命的阶段，表现为大规模空袭和不断上升的平民伤亡。 这标志着地缘政治风险加剧，可能影响能源市场并促使西方增加军事援助或制裁，同时突显人道主义危机加深，或引发外交行动。 通报强调近几个月来大规模空袭和平民伤亡不断增加，但未提供具体伤亡数字或新的政策措施。

rss · UN News · Jun 8, 12:00

**背景**: 联合国安理会负责维护国际和平与安全。俄罗斯于 2022 年 2 月全面入侵乌克兰，引发二战以来欧洲最大规模冲突，联合国经常就人道主义和安全局势举行通报。

**标签**: `#russia-ukraine`, `#diplomacy`, `#geopolitics`, `#military-risk`

---

<a id="item-8"></a>
## [联合国人权高专：美对古制裁致儿童死亡，须取消](https://news.un.org/feed/view/en/story/2026/06/1167671) ⭐️ 7.0/10

联合国人权事务高级专员沃尔克·蒂尔克警告称，美国对古巴的制裁阻碍了基本药品的获取，导致儿童死亡，并呼吁立即取消制裁。 一位联合国高级官员直接将制裁与儿童死亡联系起来，加大了美国为其封锁进行辩护或放松制裁的压力，可能影响人道主义豁免或更广泛的外交辩论。 蒂尔克将损害与美国 1 月份宣布国家紧急状态（该状态扰乱了燃料供应）联系起来。联合国大会经常谴责该禁运具有域外效力并侵犯主权。

rss · UN News · Jun 8, 12:00

**背景**: 美国对古巴的禁运自 1960 年开始实施，涉及广泛的金融和贸易限制，并以域外方式执行，惩罚与古巴进行交易的第三国实体。联合国大会每年通过决议，要求终止禁运。联合国人权事务高级专员是一个独立机构，负责在全球范围内促进和保护人权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167671">Children are dying as US sanctions push Cuba to the brink, warns UN human rights chief | UN News</a></li>
<li><a href="https://www.ohchr.org/en/press-releases/2026/06/us-sanctions-against-cuba-are-endangering-lives-and-must-be-lifted">U.S. sanctions against Cuba are endangering lives and must be lifted | OHCHR</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_embargo_against_Cuba">United States embargo against Cuba - Wikipedia</a></li>

</ul>
</details>

**标签**: `#sanctions`, `#diplomacy`, `#geopolitics`, `#united-states`, `#cuba`

---

<a id="item-9"></a>
## [金融稳定理事会发布 AI 负责任采用咨询报告](https://www.fsb.org/2026/06/sound-practices-for-responsible-adoption-of-artificial-intelligence-ai-consultation-report/) ⭐️ 6.0/10

金融稳定理事会（FSB）发布了一份咨询报告，概述了金融机构负责任地采用人工智能的稳健做法。 该咨询可能影响全球金融领域的人工智能监管标准，在中期内塑造风险管理框架和跨境协调。 报告面向各类金融机构，提供非约束性的稳健做法；最终规则及各国实施将决定市场影响。

rss · Financial Stability Board News · Jun 10, 08:00

**背景**: 金融稳定理事会是一个监测全球金融体系的国际机构，在 2008 年金融危机后成立。它虽无正式监管权力，但其建议常为国家政策提供指引。该报告针对金融领域日益增长的 AI 采用所引发的偏见和系统性脆弱性等风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Financial_Stability_Board">Financial Stability Board</a></li>
<li><a href="https://www.fsb.org/">Financial Stability Board - Promoting global financial stability through strong financial sector policies</a></li>

</ul>
</details>

**标签**: `#financial-stability`, `#central-bank`, `#macroeconomics`, `#global-markets`

---

<a id="item-10"></a>
## [FSB 宣布举办监管现代化研讨会](https://www.fsb.org/2026/06/fsb-regulatory-and-supervisory-modernisation-symposium/) ⭐️ 6.0/10

金融稳定委员会（FSB）宣布将举办一场研讨会，旨在推动成员在监管与监督框架现代化方面的努力。 此次研讨会表明国际金融监管持续协调，可能影响未来全球金融标准并对市场稳定产生影响。 目前未披露具体议程、参会者或预期成果，研讨会最终影响将取决于后续政策讨论。

rss · Financial Stability Board News · Jun 9, 15:25

**背景**: 金融稳定委员会（FSB）于 2009 年金融危机后成立，负责监测全球金融稳定并协调监管改革。它包括所有 G20 经济体，无正式条约权力，依赖成员合作制定非约束性标准。此前其工作已影响银行监管、衍生品和影子银行等领域政策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Financial_Stability_Board">Financial Stability Board</a></li>
<li><a href="https://www.fsb.org/">Financial Stability Board - Promoting global financial stability ...</a></li>

</ul>
</details>

**标签**: `#financial-stability`, `#global-markets`, `#macroeconomics`, `#diplomacy`

---