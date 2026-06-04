---
layout: default
title: "Horizon Summary: 2026-06-05 (ZH)"
date: 2026-06-05
lang: zh
---

> From 42 items, 15 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [联合国秘书长对美伊交火及伊朗袭击科威特巴林震惊](#item-2) ⭐️ 10.0/10
3. [叙利亚发现未申报化学武器，含古塔袭击同型火箭](#item-3) ⭐️ 9.0/10
4. [联合国安理会就黎巴嫩蓝线紧张局势召开会议](#item-4) ⭐️ 8.0/10
5. [欧洲央行副行长德金多斯接受《拓展报》专访](#item-5) ⭐️ 8.0/10
6. [联合国维和人员在黎南部遭迫击炮袭击身亡](#item-6) ⭐️ 7.0/10
7. [联合国人权高专办：加沙警察在停火下遭系统性袭击](#item-7) ⭐️ 7.0/10
8. [以色列威胁打击真主党，贝鲁特家庭逃离](#item-8) ⭐️ 7.0/10
9. [FSB 全会警示全球金融稳定新风险](#item-9) ⭐️ 7.0/10
10. [联合国大会选举孟加拉国拉赫曼为下届主席](#item-10) ⭐️ 6.0/10
11. [世卫组织证实黎巴嫩提尔市医院遭袭](#item-11) ⭐️ 6.0/10
12. [欧洲央行 Vujčić就货币趋同发表讲话](#item-12) ⭐️ 6.0/10
13. [欧央行：2025 年欧元国际角色温和提升](#item-13) ⭐️ 6.0/10
14. [欧洲央行发布 2026 年 4 月消费者预期调查](#item-14) ⭐️ 6.0/10
15. [伊莎贝尔·施纳贝尔：从货币市场基金看稳定币监管](#item-15) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 4, 23:05

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
| QDII Nasdaq 100 Proxy | US | neutral 33/33/34 | bullish 38/31/31 | bullish 39/30/31 | high |
| US Mega Cap Basket | US | bullish 38/31/31 | neutral 33/33/34 | neutral 33/33/34 | high |
| Japan Equity Basket | JP | neutral 33/33/34 | bullish 38/31/31 | bullish 39/30/31 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| ^NDX price trend | close=30407.81; 1d=-0.53%; 5d=+0.61%; 20d=+6.32% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=740.61; 1d=-0.48%; 5d=+0.68%; 20d=+6.44% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=30358.50; 1d=-0.90%; 5d=+0.17%; 20d=+5.72% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=15.5%; implied_move=0.4%; put/call OI=3.1137608232935876 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=54.7; rating=neutral | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.47; 2Y=4.05; 10Y-2Y=0.41999999999999993 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| ^NDX price trend | close=30407.81; 1d=-0.53%; 5d=+0.61%; 20d=+6.32% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=740.61; 1d=-0.48%; 5d=+0.68%; 20d=+6.44% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=30358.50; 1d=-0.90%; 5d=+0.17%; 20d=+5.72% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NVDA price trend | close=218.66; 1d=+1.82%; 5d=+2.06%; 20d=+5.21% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=627.57; 1d=+0.74%; 5d=-1.22%; 20d=+2.40% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=418.45; 1d=-1.24%; 5d=-5.35%; 20d=+4.95% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=428.05; 1d=+0.17%; 5d=+0.25%; 20d=+3.63% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=311.23; 1d=+0.31%; 5d=-0.41%; 20d=+8.35% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=253.79; 1d=+1.51%; 5d=-7.38%; 20d=-7.71% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| NVDA options surface | ATM IV=26.9%; implied_move=1.6%; put/call OI=0.7665844750908222 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=25.2%; implied_move=1.4%; put/call OI=0.6107757723528887 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=16.8%; implied_move=1.0%; put/call OI=0.45480519613515685 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=23.9%; implied_move=1.4%; put/call OI=0.39289572081429164 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=27.1%; implied_move=1.6%; put/call OI=0.43843095408633115 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=23.6%; implied_move=1.4%; put/call OI=0.5128911752097495 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| MSFT insider filings | recent Form4 count=726 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| AAPL insider filings | recent Form4 count=587 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.47; 2Y=4.05; 10Y-2Y=0.41999999999999993 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=54.7; rating=neutral | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| NVDA price trend | close=218.66; 1d=+1.82%; 5d=+2.06%; 20d=+5.21% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=627.57; 1d=+0.74%; 5d=-1.22%; 20d=+2.40% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=418.45; 1d=-1.24%; 5d=-5.35%; 20d=+4.95% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 8035.T price trend | close=63660.00; 1d=+4.53%; 5d=+21.67%; 20d=+23.09% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=80040.00; 1d=-0.73%; 5d=+6.46%; 20d=+0.87% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=94.13; 1d=+0.20%; 5d=+1.54%; 20d=+2.67% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7377.00; 1d=-11.28%; 5d=+3.54%; 20d=+14.83% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3540.00; 1d=-2.18%; 5d=+2.58%; 20d=+13.10% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2838.50; 1d=-1.48%; 5d=-6.32%; 20d=-4.68% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=54.7; rating=neutral | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.47; 2Y=4.05; 10Y-2Y=0.41999999999999993 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 8035.T price trend | close=63660.00; 1d=+4.53%; 5d=+21.67%; 20d=+23.09% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=80040.00; 1d=-0.73%; 5d=+6.46%; 20d=+0.87% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=94.13; 1d=+0.20%; 5d=+1.54%; 20d=+2.67% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| KWEB price trend | close=27.13; 1d=-0.33%; 5d=+1.76%; 20d=-8.84% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=123.50; 1d=-2.45%; 5d=+1.40%; 20d=-7.97% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=22.52; 1d=-1.27%; 5d=-2.38%; 20d=-7.67% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=35.47; 1d=-0.20%; 5d=+1.37%; 20d=-5.39% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=28.38; 1d=-0.70%; 5d=-0.63%; 20d=-7.92% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=78.60; 1d=-2.24%; 5d=+7.23%; 20d=-4.73% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=54.7; rating=neutral | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.47; 2Y=4.05; 10Y-2Y=0.41999999999999993 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| KWEB price trend | close=27.13; 1d=-0.33%; 5d=+1.76%; 20d=-8.84% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=123.50; 1d=-2.45%; 5d=+1.40%; 20d=-7.97% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=22.52; 1d=-1.27%; 5d=-2.38%; 20d=-7.67% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

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

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [CBOE Volatility Index: VIX (VIXCLS) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/VIXCLS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Graph and download economic data for CBOE Volatility Index: VIX (VIXCLS) from 1990-01-02 to 2026-06-03 about VIX, volatility, stock market, and USA.

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

- [Move Index Chart - Barchart.com](https://www.barchart.com/stocks/quotes/$MOVE/interactive-chart)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Customizable interactive chart for Move Index with latest real-time price quote, charts, latest news, technical analysis and opinions.

- [QQQ Options - Live IV, Flow, Greeks & Analysis / ImpliedOptions ...](https://impliedoptions.com/ticker/qqq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Trade QQQ options with real-time implied volatility, IV rank, options flow, and Greeks. Analyze QQQ calls and puts with our free calculator and strategy builder.

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [US High Yield Master II Option-Adjusted Spread (Market Dail…](https://ycharts.com/indicators/us_high_yield_master_ii_optionadjusted_spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：View market daily updates and historical trends for US High Yield Master II Option-Adjusted Spread. from United States. Source: Bank of America Merrill Ly…

- [US - ICE BofA US High Yield Index Option-Adjusted Spread](https://en.macromicro.me/series/78167/us-ice-bofa-us-high-yield-index-option-adjusted-spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：Zoom 6m YTD 1y 3y 5y All All US - ICE BofA US High Yield Index Option-Adjusted Spread 2000 2005 2010 2015 2020 2025 0 5 10 15 20 25

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

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [iShares MSCI Japan ETF (EWJ) Price, Holdings, & News](https://www.marketbeat.com/stocks/NYSEARCA/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Should You Buy or Sell iShares MSCI Japan ETF Stock? Get The Latest EWJ Stock Price, Constituents List, Holdings Data, and Headlines at MarketBeat.

- [EWJ / iShares MSCI Japan ETF Overview / MarketWatch](https://www.marketwatch.com/investing/fund/ewj)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ / A complete iShares MSCI Japan ETF exchange traded fund overview by MarketWatch. View the latest ETF prices and news for better ETF investing.

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
## [联合国秘书长对美伊交火及伊朗袭击科威特巴林震惊](https://news.un.org/feed/view/en/story/2026/06/1167639) ⭐️ 10.0/10

联合国秘书长安东尼奥·古特雷斯周二对报道的美伊夜间交火以及伊朗攻击科威特和巴林表示震惊。 此次升级有可能引发更广泛的地区冲突，扰乱波斯湾能源供应，并可能因油价飙升和避险资金流动威胁全球市场稳定。 据报道，伊朗革命卫队声称对巴林和科威特的袭击负责；巴林拦截了三枚瞄准民用设施的导弹和无人机，科威特国际机场遇袭造成一人死亡，此前美国对伊朗南部发动了新一轮打击。

rss · UN News · Jun 3, 12:00

**背景**: 自 2026 年 2 月以来，美国与以色列一直与伊朗处于战争状态，初期空袭针对军事和政府设施。脆弱的停火协议已经生效，但最近美国对伊朗南部的打击据报道促使伊朗对海湾地区美国盟友进行报复。科威特和巴林设有美国军事基地，此前已受到伊朗盟友力量的威胁。霍尔木兹海峡是全球石油运输的关键通道，紧邻冲突区，以往的升级已扰乱了能源市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Iran_war">2026 Iran war - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/06/03/world/middleeast/iran-attacks-kuwait-bahrain-ceasefire.html">Attacks on Kuwait and Bahrain Add Further Strain to U.S.- Iran ...</a></li>
<li><a href="https://www.aljazeera.com/news/2026/6/3/iran-kuwait-bahrain-hit-is-the-war-in-the-gulf-escalating-again">Iran , Kuwait , Bahrain hit: Is the war in the Gulf escalating... | Al Jazeera</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`

---

<a id="item-3"></a>
## [叙利亚发现未申报化学武器，含古塔袭击同型火箭](https://news.un.org/feed/view/en/story/2026/06/1167652) ⭐️ 9.0/10

联合国裁军事务负责人称，禁止化学武器组织（OPCW）核查人员在叙利亚发现大量此前未申报的化学武器，其中包括 2013 年古塔沙林袭击中所使用的同型号火箭。这一“重大发现”于 2026 年 5 月 27 日公布。 这一发现可能重新引发对叙利亚违反《禁止化学武器公约》的国际审查和惩罚，或导致新制裁、外交孤立乃至军事回应，并使 2013 年旨在销毁叙利亚化武的裁军协议受到质疑。 OPCW 报告称在叙利亚多处地点发现数十件未申报的化学武器，包括与古塔袭击有关的弹药。联合国安理会预计将紧急讨论此事，要求叙利亚全面披露并销毁剩余库存。

rss · UN News · Jun 4, 12:00

**背景**: 2013 年 8 月，叙利亚政府军在大马士革古塔郊区发动沙林毒气袭击，造成数百人死亡。在西方军事打击威胁下，叙利亚同年加入《禁止化学武器公约》，同意在 OPCW 监督下销毁化学武库。尽管叙方声称已完成销毁，外界一直怀疑其隐匿库存并继续使用化武，OPCW 于 2021 年暂停了叙利亚的某些条约权利。此次发现直接证实了未申报武器的存在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167652">Undeclared chemical weapons found in Syria , including... | UN News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ghouta_chemical_attack">Ghouta chemical attack - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chemical_Weapons_Convention">Chemical Weapons Convention - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#sanctions`, `#military-risk`, `#middle-east`

---

<a id="item-4"></a>
## [联合国安理会就黎巴嫩蓝线紧张局势召开会议](https://news.un.org/feed/view/en/story/2026/06/1167625) ⭐️ 8.0/10

应法国请求，联合国安理会匆忙召开会议，应对以色列与真主党沿蓝线不断升级的冲突；同时有警告称以色列可能袭击贝鲁特南郊，且美伊和谈状况不明。 紧张局势升级增加了更广泛冲突的风险，威胁地区稳定、能源市场以及美国当前的调解努力，可能对全球外交和油价产生连锁影响。 此次于周一召开的会议由法国请求举行，讨论了暴力升级问题；同时有警告称以色列可能袭击贝鲁特南郊，且美伊和谈状况不明，该和谈与岌岌可危的停火协议相关联。

rss · UN News · Jun 2, 12:00

**背景**: 蓝线是联合国于 2000 年划定的一条以色列与黎巴嫩间的撤军线，从以色列 2000 年撤出黎巴嫩南部后设立。真主党是伊朗支持的黎巴嫩什叶派伊斯兰主义军事组织与政党，自 2023 年 10 月起与以色列持续冲突，导致 2024 年黎巴嫩战争。联合国安理会是负责国际和平与安全的主要机构，可实施制裁并授权动武，但五个常任理事国拥有否决权。近期美国调解的停火谈判陷入困境，同时对涉及伊朗的更广泛地区冲突的担忧加剧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blue_Line_(Lebanon)">Blue Line (Lebanon)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#military-risk`, `#middle-east`, `#diplomacy`, `#energy`

---

<a id="item-5"></a>
## [欧洲央行副行长德金多斯接受《拓展报》专访](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260531~f648dbde70.en.html) ⭐️ 8.0/10

欧洲央行副行长路易斯·德金多斯接受了《拓展报》专访，可能谈及欧元区货币政策、通胀和增长前景，或释放未来利率走向信号。 欧洲央行高层的言论可能改变市场对利率、欧元和债券收益率的预期，因此此次访谈对关注政策正常化的投资者和政策制定者至关重要。 讨论可能包含关于利率调整步伐的前瞻指引，或对服务业通胀粘性及欧元区增长乏力的评估。

rss · ECB Press Releases · May 31, 14:00

**背景**: 总部位于法兰克福的欧洲央行是欧元区 20 个成员国的中央银行，其维持物价稳定的目标是通胀率控制在 2%。2026 年初，全球增长预计为 3.3%，但欧洲面临贸易不确定性和通胀持续等逆风，使得欧洲央行的沟通成为关键的市场驱动因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank - Wikipedia</a></li>
<li><a href="https://www.imf.org/en/publications/weo/issues/2026/01/19/world-economic-outlook-update-january-2026">World Economic Outlook Update, January 2026: Global Economy...</a></li>
<li><a href="https://www.ey.com/en_pl/insights/economic-analysis-team/ey-european-economic-outlook-march-2026">EY European Economic Outlook – March 2026 | EY - Global</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#currency`, `#bonds`, `#europe`

---

<a id="item-6"></a>
## [联合国维和人员在黎南部遭迫击炮袭击身亡](https://news.un.org/feed/view/en/story/2026/06/1167645) ⭐️ 7.0/10

联合国驻黎巴嫩临时部队（UNIFIL）一名塞尔维亚籍维和人员于周四凌晨在黎南部城市迈尔季欧云附近的阵地遭迫击炮袭击后死亡。 此次袭击凸显黎以边境暴力升级，破坏了外交努力，并加大区域不稳定风险，可能波及能源市场和联合国维和行动的公信力。 袭击地点位于奈拜提耶省的迈尔季欧云区。拥有 48 国逾 8,200 名军人的 UNIFIL 此前也曾遭袭，包括 2024 年 10 月以色列坦克强行闯入联合国哨所。

rss · UN News · Jun 4, 12:00

**背景**: UNIFIL 于 1978 年以色列入侵黎巴嫩后设立，旨在恢复以黎边境和平，2006 年黎巴嫩战争后根据安理会第 1701 号决议扩大授权。其任务是监督停火、协助平民并支持黎巴嫩当局。该部队任期最近延长至 2026 年底，计划 2027 年缩编撤离。黎南部边境地区局势持续动荡，真主党等武装团体活动频繁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNIFIL">UNIFIL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Marjayoun_District">Marjayoun District - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/israeli_attack_on_ramyah_unifil_post">Israeli attack on Ramyah UNIFIL post</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#military-risk`, `#diplomacy`, `#geopolitics`

---

<a id="item-7"></a>
## [联合国人权高专办：加沙警察在停火下遭系统性袭击](https://news.un.org/feed/view/en/story/2026/06/1167631) ⭐️ 7.0/10

联合国人权高专办表示，尽管有名义上的停火协议，以色列的无人机和空袭仍在持续杀害加沙警察，危及和平与重建工作。 系统性袭击加沙警察破坏了停火协议的持久性，阻碍重建，增加局势升级风险，可能引发联合国安理会介入，加剧地区动荡。 联合国人权高专办的报告明确将警察列为袭击目标，尽管其对维持秩序至关重要，而‘名义停火’一词表明协议在很大程度上未被遵守。

rss · UN News · Jun 3, 12:00

**背景**: 停火是经调解达成的暂时停止交战协议，若未全面执行则十分脆弱。联合国人权高专办负责监督并报告此类违规行为。加沙警察在维持公共秩序和协助人道主义援助分发方面发挥关键作用，因此对警察的袭击直接破坏了持久和平的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ceasefire">Ceasefire - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OHCHR">OHCHR</a></li>
<li><a href="https://www.middleeasteye.net/news/lebanon-israel-ceasefire-plan-doubt-hezbollah-rejection">Lebanon-Israel ceasefire plans in doubt following Hezbollah's rejection | Middle East Eye</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#military-risk`, `#diplomacy`

---

<a id="item-8"></a>
## [以色列威胁打击真主党，贝鲁特家庭逃离](https://news.un.org/feed/view/en/story/2026/06/1167615) ⭐️ 7.0/10

以色列威胁加大对贝鲁特真主党的打击，导致平民家庭逃离，联合国在脆弱的停火延长期内继续提供人道主义援助。 局势升级可能打破脆弱的停火，引发以色列与真主党之间更广泛的冲突，并加剧黎巴嫩的人道主义危机。 最初于 2024 年 11 月签署并延长的停火协议遭到双方违反；尽管黎巴嫩政府努力解除武装，真主党仍是一支强大的武装力量。

rss · UN News · Jun 1, 12:00

**背景**: 真主党是伊朗支持的什叶派武装组织和政党，与以色列冲突数十年。2024 年 11 月的停火结束了重大升级，但仍很脆弱。联合国第 1701 号决议结束了 2006 年战争，要求真主党解除武装，但从未完全执行。黎巴嫩政府面临解除真主党武装的压力，但该组织依然强大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/06/02/world/middleeast/israel-lebanon-hezbollah.html">How Hezbollah Drones Changed Israel’s Strategy in Lebanon - The New York Times</a></li>
<li><a href="https://en.wikipedia.org/wiki/Israel-Hezbollah_Ceasefire_Deal">Israel-Hezbollah Ceasefire Deal</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#middle-east`, `#military-risk`, `#diplomacy`

---

<a id="item-9"></a>
## [FSB 全会警示全球金融稳定新风险](https://www.fsb.org/2026/06/fsb-plenary-highlights-potential-new-vulnerabilities-to-financial-stability/) ⭐️ 7.0/10

金融稳定理事会成员在伦敦开会讨论全球金融体系新出现的脆弱性，并审查多项工作进展。会议未详细披露具体风险，但表明全球金融监管机构正密切关注潜在威胁。 会议凸显监管机构对多重风险同时爆发的日益担忧，正如 FSB 主席所警告的。这可能导致更严格的金融监管，影响全球市场和政策协调。 FSB 主席在 2026 年 4 月致 G20 财长和央行行长的信中已警告，多重脆弱性同时爆发的风险增加。全体会议可能基于这一评估，但未公布细节。

rss · Financial Stability Board News · Jun 1, 17:43

**背景**: 金融稳定理事会是一个国际机构，负责监测全球金融体系并提出建议。它成立于 2008 年金融危机后，旨在协调各国金融监管机构和国际标准制定机构。FSB 全体会议汇集了来自 G20 国家央行、监管机构和财政部的官员，评估风险并制定政策应对措施。主权风险是标签主题之一，指政府违约债务的风险，可能成为全球金融体系的一个关键脆弱性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fsb.org/">Financial Stability Board - Promoting global financial stability ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_risk">Sovereign risk</a></li>

</ul>
</details>

**标签**: `#financial-stability`, `#central-bank`, `#macroeconomics`, `#global-markets`, `#sovereign-risk`

---

<a id="item-10"></a>
## [联合国大会选举孟加拉国拉赫曼为下届主席](https://news.un.org/feed/view/en/story/2026/06/1167626) ⭐️ 6.0/10

孟加拉国外交部长卡利鲁尔·拉赫曼在联合国大会第 81 届会议主席选举中击败塞浦路斯的安德烈亚斯·卡库里，当选为新任主席。 拉赫曼的当选使他能够在全球危机和联合国改革的关键之年主导多边讨论，可能影响安理会改革等议题的议程设置。 选举竞争激烈。大会主席按区域集团轮换，孟加拉国代表亚太集团。第 81 届会议将于 2026 年 9 月开幕。

rss · UN News · Jun 2, 12:00

**背景**: 联合国大会是联合国主要议事机构，由 193 个会员国组成。大会主席每年选举产生，按五个区域集团轮换。主席负责主持会议、设定临时议程，并可影响全球议题讨论。第 81 届会议将在危机加剧和联合国改革谈判的背景下召开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/President_of_the_United_Nations_General_Assembly">President of the United Nations General Assembly - Wikipedia</a></li>
<li><a href="https://www.cfr.org/backgrounders/un-general-assembly-unga-role">What Is the UN General Assembly ? | Council on Foreign Relations</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#united-nations`, `#south-asia`

---

<a id="item-11"></a>
## [世卫组织证实黎巴嫩提尔市医院遭袭](https://news.un.org/feed/view/en/story/2026/06/1167621) ⭐️ 6.0/10

世界卫生组织（WHO）正在核实有关黎巴嫩南部城市提尔一家医院周一遭袭的报告，该国医疗设施遇袭事件呈上升趋势。 此次袭击凸显了冲突地区针对医疗设施的暴力模式，可能加剧区域外交紧张局势，并使本已严峻的人道危机进一步恶化。 联合国驻黎巴嫩卫生机构正积极核实此次袭击，但尚未公布伤亡人数或破坏程度的具体数据。

rss · UN News · Jun 2, 12:00

**背景**: 提尔是黎巴嫩最大的城市之一，在最近以色列的攻势中遭受猛烈轰炸。国际人道法严格保护医院和医务人员，除非其被用于军事目的。世卫组织系统记录此类事件，以推动问责并强化对医疗的法律保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tyre,_Lebanon">Tyre , Lebanon - Wikipedia</a></li>
<li><a href="https://www.dropsitenews.com/p/tyre-sour-lebanon-israeli-assault-displacement">Tyre is Now the Epicenter of Israel’s Assault on Lebanon</a></li>
<li><a href="https://blogs.icrc.org/law-and-policy/2026/05/06/attacks-on-the-medical-mission-identification-of-issues-and-good-practices/">Attacks on the medical mission: identification of issues and good...</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#diplomacy`, `#geopolitics`, `#military-risk`

---

<a id="item-12"></a>
## [欧洲央行 Vujčić就货币趋同发表讲话](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260602~101b71c594.en.html) ⭐️ 6.0/10

2026 年 6 月 2 日，新任欧洲央行副行长鲍里斯·武伊契奇发表了关于欧洲货币趋同的演讲，分享了关于经济一体化和趋同标准的见解。 作为欧洲央行高级官员，他的观点可能预示央行对欧元采用和趋同的立场，影响非欧元区欧盟国家的预期和欧元区政策走向。 武伊契奇曾任克罗地亚央行行长（该国于 2023 年采用欧元），可能结合马斯特里赫特趋同标准和欧元采用的实际挑战提供了第一手经验。

rss · ECB Press Releases · Jun 2, 14:35

**背景**: 欧元趋同标准（马斯特里赫特标准）是欧盟国家采用欧元必须满足的经济和法律条件。鲍里斯·武伊契奇自 2012 年起担任克罗地亚央行行长，领导了 2023 年克罗地亚加入欧元区的进程。他于 2026 年 6 月 1 日起出任欧洲央行副行长，将实际趋同经验带入该职位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Euro_convergence_criteria">Euro convergence criteria - Wikipedia</a></li>
<li><a href="https://www.consilium.europa.eu/en/press/press-releases/2026/03/19/european-council-appoints-boris-vujcic-as-vice-president-of-the-european-central-bank/">European Council appoints Boris Vujčić as... - Consilium</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#europe`, `#currency`, `#macroeconomics`

---

<a id="item-13"></a>
## [欧央行：2025 年欧元国际角色温和提升](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260602~f941e87516.en.html) ⭐️ 6.0/10

欧央行 2025 年报告显示，欧元国际债券发行量创历史新高，并在全球绿色债券市场中首次占据领先地位，但其在外汇日常交易中的使用明显下降。 这一渐进变化表明全球可能正在减少对美元的依赖，增强了欧洲的战略自主权和全球金融影响力，对储备货币构成和外汇市场产生深远影响。 欧元计价的国际债券发行量创新高，并在绿色与可持续债券发行上超越美元；但外汇日均交易份额下降，凸显进展不均衡。

rss · ECB Press Releases · Jun 2, 08:00

**背景**: 货币的国际角色通过其在全球储备、贸易计价和金融交易中的使用来衡量。欧元是仅次于美元的第二重要货币。自全球金融危机以来，欧元的份额保持稳定，但政策制定者寻求进一步增强其角色以减少对美元的依赖。欧央行每年发布追踪这些指标的报告。2025 年报告于 2026 年 6 月发布，显示整体温和提升，但不同市场领域趋势不一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/press/other-publications/ire/html/ecb.ire202606.en.html">The international role of the euro , June 2026</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-06-02/euro-s-global-role-gains-slightly-but-still-distant-from-dollar">EUR USD: Euro ’s Global Role Gains Slightly But Still... - Bloomberg</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#currency`, `#macroeconomics`, `#europe`, `#global-markets`

---

<a id="item-14"></a>
## [欧洲央行发布 2026 年 4 月消费者预期调查](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260601~bf8026bfc2.en.html) ⭐️ 6.0/10

欧洲央行公布了 2026 年 4 月消费者预期调查结果，揭示了欧元区家庭对通胀感知、收入预期和支出意向的最新变化。 该调查数据影响欧洲央行对中期物价稳定的评估，因为通胀预期是实际通胀的关键驱动因素，进而影响货币政策决策。 该调查由益普索执行，追踪消费者对未来 12 个月和 3 年的通胀预期，4 月数据可能显示 3 月出现的上升趋势是否延续。

rss · ECB Press Releases · Jun 1, 08:00

**背景**: 欧洲央行消费者预期调查是 2020 年启动的月度调查，旨在收集欧元区家庭的经济预期数据。欧洲央行的首要任务是维持物价稳定，即中期内通胀率低于但接近 2%。通胀预期至关重要，因为它们可能自我实现，因此央行需要锚定预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/stats/ecb_surveys/consumer_exp_survey/html/index.en.html">Consumer Expectations Survey</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3981218">ECB Consumer Expectations Survey : An Overview and... :: SSRN</a></li>
<li><a href="https://en.wikipedia.org/wiki/Price_stability">Price stability - Wikipedia</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`

---

<a id="item-15"></a>
## [伊莎贝尔·施纳贝尔：从货币市场基金看稳定币监管](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260601~38dffe5ec5.en.html) ⭐️ 6.0/10

2026 年 6 月 1 日，欧央行执委伊莎贝尔·施纳贝尔发表演讲，讨论了货币市场基金暴露的脆弱性（如流动性错配和挤兑风险）如何为稳定币监管提供借鉴，以增强金融稳定。 该讲话标志着央行对稳定币风险的高度关注，可能会影响欧盟未来监管框架（如 MiCA）并塑造全球加密资产标准；趋严的规则可能影响稳定币发行方和更广泛的数字支付生态系统。 施纳贝尔可能强调了相似之处，如依赖短期融资、需要稳健的流动性缓冲，以及可能对稳定币实施类似货币市场基金的赎回限制。该讲话也呼应了国际清算银行和 IMF 在稳定币稳定性方面的工作。

rss · ECB Press Releases · Jun 1, 00:10

**背景**: 货币市场基金投资于短期债务，通常被视为低风险，但压力时期可能遭遇挤兑，如 2008 年和 2020 年所见证。稳定币是锚定美元等稳定资产的数字资产，其储备常包括商业票据等与货币市场基金相似的资产。监管机构担心主要稳定币的信任丧失可能引发挤兑，并扰乱更广泛的金融市场。欧盟《加密资产市场法规》部分于 2024 年生效，为稳定币发行方设定了规则，但央行仍在评估额外保障措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bis.org/publ/work905.pdf">Stablecoins : risks, potential and regulation</a></li>
<li><a href="https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026074-source-pdf.pdf">Making Stablecoins Stable, WP/26/74, April 2026</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#europe`, `#global-markets`

---