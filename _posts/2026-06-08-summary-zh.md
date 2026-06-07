---
layout: default
title: "Horizon Summary: 2026-06-08 (ZH)"
date: 2026-06-08
lang: zh
---

> From 40 items, 11 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [美以空袭伊朗引发霍尔木兹海峡危机](#item-2) ⭐️ 10.0/10
3. [叙利亚发现未申报化武，与古塔袭击有关](#item-3) ⭐️ 9.0/10
4. [联合国安理会紧急开会应对以黎冲突升级](#item-4) ⭐️ 9.0/10
5. [联合国驻黎巴嫩维和人员遭迫击炮袭击身亡](#item-5) ⭐️ 7.0/10
6. [欧洲央行发布 2026 年 4 月消费者预期调查结果](#item-6) ⭐️ 7.0/10
7. [欧洲央行施纳贝尔谈货币市场基金与稳定币的教训](#item-7) ⭐️ 7.0/10
8. [欧洲央行埃尔德森呼吁加强面向 AI 的运营韧性](#item-8) ⭐️ 6.0/10
9. [欧洲央行称 2025 年欧元国际角色温和提升](#item-9) ⭐️ 6.0/10
10. [监管机构进一步删除声誉风险引用](#item-10) ⭐️ 6.0/10
11. [金融稳定理事会全体会议警示金融稳定新脆弱性](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 7, 22:43

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
| QDII Nasdaq 100 Proxy | US | neutral 31/34/35 | neutral 31/31/37 | bearish 31/36/32 | high |
| US Mega Cap Basket | US | neutral 31/34/35 | neutral 31/31/37 | bearish 31/36/32 | high |
| Japan Equity Basket | JP | neutral 33/33/34 | bullish 38/31/31 | bullish 39/30/31 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| QQQ price trend | close=705.06; 1d=-4.80%; 5d=-4.50%; 20d=+1.46% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=28990.50; 1d=-0.12%; 5d=-5.16%; 20d=-1.17% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=28957.60; 1d=-4.77%; 5d=-4.53%; 20d=+1.38% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=37.8%; implied_move=2.0%; put/call OI=2.4906895514792624 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=42.1; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.55; 2Y=4.17; 10Y-2Y=0.3799999999999999 | 利率曲线决定权益估值贴现与风险偏好上限。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：短线隐含波动偏高，回撤与震荡风险上升
- 1周：期权隐含波动较高，1周方向分歧增加
- 1月：期权市场仍在计入较高下行尾部风险

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 31% | 34% | 35% | neutral | 短线隐含波动偏高，回撤与震荡风险上升 | high |
| 1周 | 31% | 31% | 37% | neutral | 期权隐含波动较高，1周方向分歧增加 | high |
| 1月 | 31% | 36% | 32% | bearish | 期权市场仍在计入较高下行尾部风险 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| QQQ price trend | close=705.06; 1d=-4.80%; 5d=-4.50%; 20d=+1.46% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=28990.50; 1d=-0.12%; 5d=-5.16%; 20d=-1.17% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=28957.60; 1d=-4.77%; 5d=-4.53%; 20d=+1.38% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/neutral/bearish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| META price trend | close=593.00; 1d=-5.51%; 5d=-6.25%; 20d=-3.86% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=391.00; 1d=-6.56%; 5d=-10.28%; 20d=-5.05% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=416.67; 1d=-2.66%; 5d=-7.46%; 20d=-0.76% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=205.10; 1d=-6.20%; 5d=-2.75%; 20d=-2.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=307.34; 1d=-1.25%; 5d=-1.51%; 20d=+7.02% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=368.53; 1d=-0.98%; 5d=-3.11%; 20d=-7.40% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| TSLA options surface | ATM IV=50.5%; implied_move=3.0%; put/call OI=0.5966468511982166 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=37.8%; implied_move=2.1%; put/call OI=0.4164050551396603 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=39.1%; implied_move=2.2%; put/call OI=0.3051055705725573 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=31.3%; implied_move=1.8%; put/call OI=0.5842922374429224 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=45.4%; implied_move=2.5%; put/call OI=0.7474192694547379 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=39.5%; implied_move=2.2%; put/call OI=0.2832431905666813 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| MSFT insider filings | recent Form4 count=726 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| AAPL insider filings | recent Form4 count=587 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| NVDA insider filings | recent Form4 count=560 | 内部人交易节奏可作为估值温度辅助校验信号。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：短线隐含波动偏高，回撤与震荡风险上升
- 1周：期权隐含波动较高，1周方向分歧增加
- 1月：期权市场仍在计入较高下行尾部风险

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 31% | 34% | 35% | neutral | 短线隐含波动偏高，回撤与震荡风险上升 | high |
| 1周 | 31% | 31% | 37% | neutral | 期权隐含波动较高，1周方向分歧增加 | high |
| 1月 | 31% | 36% | 32% | bearish | 期权市场仍在计入较高下行尾部风险 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| META price trend | close=593.00; 1d=-5.51%; 5d=-6.25%; 20d=-3.86% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=391.00; 1d=-6.56%; 5d=-10.28%; 20d=-5.05% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=416.67; 1d=-2.66%; 5d=-7.46%; 20d=-0.76% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/bearish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| EWJ price trend | close=90.72; 1d=-3.62%; 5d=-2.41%; 20d=-0.30% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=59450.00; 1d=-6.61%; 5d=+13.41%; 20d=+13.35% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7426.00; 1d=+0.66%; 5d=-0.87%; 20d=+21.12% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=78070.00; 1d=-2.46%; 5d=-2.55%; 20d=-7.25% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3559.00; 1d=+0.54%; 5d=+3.34%; 20d=+14.29% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2850.00; 1d=+0.41%; 5d=-6.31%; 20d=-2.16% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.55; 2Y=4.17; 10Y-2Y=0.3799999999999999 | 利率曲线决定权益估值贴现与风险偏好上限。 |
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
| EWJ price trend | close=90.72; 1d=-3.62%; 5d=-2.41%; 20d=-0.30% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=59450.00; 1d=-6.61%; 5d=+13.41%; 20d=+13.35% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7426.00; 1d=+0.66%; 5d=-0.87%; 20d=+21.12% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 1810.HK price trend | close=27.80; 1d=-2.04%; 5d=-0.86%; 20d=-10.67% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=115.80; 1d=+0.70%; 5d=+2.03%; 20d=-2.69% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=79.95; 1d=+1.72%; 5d=+8.85%; 20d=-5.10% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=21.82; 1d=-3.11%; 5d=-5.58%; 20d=-10.35% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=122.40; 1d=-0.89%; 5d=+1.24%; 20d=-13.13% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=34.75; 1d=-2.03%; 5d=-0.86%; 20d=-6.56% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.55; 2Y=4.17; 10Y-2Y=0.3799999999999999 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=42.1; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| 1810.HK price trend | close=27.80; 1d=-2.04%; 5d=-0.86%; 20d=-10.67% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=115.80; 1d=+0.70%; 5d=+2.03%; 20d=-2.69% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=79.95; 1d=+1.72%; 5d=+8.85%; 20d=-5.10% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

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
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days out or more. IV is a forward looking prediction of the likelihood...

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [Move Index Chart - Barchart.com](https://www.barchart.com/stocks/quotes/$MOVE/interactive-chart)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Customizable interactive chart for Move Index with latest real-time price quote, charts, latest news, technical analysis and opinions.

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
  - 摘要：Majority Sell Bias Climbs in USD/JPY as Traders Anticipate Intervention TradingView · 3 days ago USD/JPY stays bid despite more hawkish BoJ's Ueda comments and imminent rate hik...

- [USD JPY / US Dollar to Yen Live Rate - Investing.com](https://www.investing.com/currencies/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get real time data on the USD/JPY pair including the live rate, as well as our currency converter, analysis, news, historical data and more.

- [Valuta EX - Currency Converter / Real-Time Exchange Rates](https://valuta.exchange/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Index Information - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index/profile?idx=nk225vi)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：The Nikkei Stock Average Volatility Index are calculated by using prices of Nikkei 225 futures and Nikkei 225 options on the Osaka Exchange (OSE). In the calculation, taking nea...

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
## [美以空袭伊朗引发霍尔木兹海峡危机](https://news.un.org/feed/view/en/story/2026/06/1167648) ⭐️ 10.0/10

2026 年 2 月 28 日，美国和以色列对伊朗发动协同空袭，袭击军事和政府目标，并击毙最高领袖阿里·哈梅内伊，一场重大战争由此开始。袭击使霍尔木兹海峡成为引爆点，伊朗军队威胁关闭这一关键石油咽喉。 霍尔木兹海峡承载着全球约 25%的海运石油贸易和 20%的液化天然气，一旦中断会导致油价飙升，破坏全球经济稳定。这场冲突直接威胁能源安全，可能引发报复升级，并重塑中东联盟格局。 海峡关闭可能使全球石油日流量减少约 1100 万桶，超过以往危机的影响。冲突已蔓延至伊朗境外，据报道伊朗袭击了科威特和巴林，并正在非洲和阿富汗引发粮食安全危机。

rss · UN News · Jun 5, 12:00

**背景**: 霍尔木兹海峡是连接波斯湾和阿曼湾的狭窄水道，对海湾产油国的油气运输至关重要。伊朗长期威胁在紧张局势时封锁海峡。2026 年 2 月 28 日，美以发动空袭，代号“咆哮雄狮行动”（以色列）和“史诗之怒行动”（美国），针对伊朗领导层和军事能力。这场战争有时被称为“十二日战争”，已导致伊朗军队几乎全面封锁海峡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis">2026 Strait of Hormuz crisis - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Iran_war">2026 Iran war - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`

---

<a id="item-3"></a>
## [叙利亚发现未申报化武，与古塔袭击有关](https://news.un.org/feed/view/en/story/2026/06/1167652) ⭐️ 9.0/10

联合国化学武器核查人员在叙利亚发现大量此前未申报的化学武器，其中包括与 2013 年古塔沙林毒气袭击所用类型相同的火箭弹。联合国裁军事务高级官员称这一发现对国际安全来说是“重大发现”。 这一发现表明叙利亚持续违反《禁止化学武器公约》，可能引发外交升级、新制裁或军事反应。它加剧了地缘政治风险，可能影响对中东紧张局势敏感的市场。 这批库存包括与 2013 年古塔惨案中释放沙林的火箭弹相同的火箭。核查由禁化武组织在未申报的高优先级地点进行，但目前尚不清楚这些武器的当前持有者。

rss · UN News · Jun 4, 12:00

**背景**: 2013 年古塔化学武器袭击使用沙林火箭弹，造成大马士革郊区反对派控制区数百人死亡。在美俄协议下，叙利亚当年加入《禁止化学武器公约》并承诺销毁化武，但禁化武组织随后发现其申报不完整且仍使用化武。2021 年，公约缔约国因叙利亚违规暂停了其投票权。禁化武组织的申报评估小组和实况调查团持续调查涉嫌化学袭击事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ghouta_chemical_attack">Ghouta chemical attack - Wikipedia</a></li>
<li><a href="https://apnews.com/article/syria-opcw-chemical-weapons-beb5273bdfe0499c30f929a671f98acd">OPCW says it found dozens of Assad-era chemical weapons in Syria this month | AP News</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`, `#sanctions`

---

<a id="item-4"></a>
## [联合国安理会紧急开会应对以黎冲突升级](https://news.un.org/feed/view/en/story/2026/06/1167625) ⭐️ 9.0/10

应法国请求，联合国安理会于周一紧急召开会议，以应对以色列军队与真主党武装在黎以边境地区日益升级的暴力冲突。 此次会议反映出国际社会日益加剧的担忧，以及更广泛地区战争风险上升，这可能会破坏中东稳定、影响能源市场，并对美国主导的调解努力构成挑战。 联合国划定的蓝线一直是个持续的冲突点；受伊朗支持的真主党尽管国际社会要求其解除武装，但仍保持着强大的军事力量。

rss · UN News · Jun 2, 12:00

**背景**: 蓝线是联合国于 2000 年设立的，用于确认以色列从黎巴嫩撤军。真主党是与伊朗紧密结盟的黎巴嫩什叶派政治和军事组织，被许多国家列为恐怖组织。联合国安理会第 1701 号决议结束了 2006 年战争，要求真主党解除武装，但其仍拥有重武器。联合国驻黎巴嫩临时部队（UNIFIL）监控该地区，但零星敌对行动持续不断，2024 年达成的停火协议曾短暂缓解紧张局势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blue_Line_(Israel-Lebanon_border)">Blue Line (Israel-Lebanon border)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://www.bbc.com/news/articles/cx2d3gj9ewxo">Lebanon ceasefire: What we know about Israel- Hezbollah deal</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`

---

<a id="item-5"></a>
## [联合国驻黎巴嫩维和人员遭迫击炮袭击身亡](https://news.un.org/feed/view/en/story/2026/06/1167645) ⭐️ 7.0/10

一名塞尔维亚籍联合国维和人员在黎巴嫩东南部迈尔季欧云附近遭迫击炮袭击身亡，联合国驻黎巴嫩临时部队（联黎部队）已证实此消息。此次袭击凸显了该地区维和人员面临的日益加剧的风险。 此次死亡事件表明地区不稳定加剧，可能引发加强部队保护或调整联黎部队任务授权的呼声，进而影响国际介入和黎巴嫩的安全局势。 遇难维和人员来自塞尔维亚，在黎巴嫩南部城镇迈尔季欧云附近遭遇迫击炮火身亡。尚无任何组织声称负责，此次袭击是近年来针对联黎部队的一系列事件中的最新一起。

rss · UN News · Jun 4, 12:00

**背景**: 联黎部队于 1978 年成立，在 2006 年黎巴嫩战争后得到加强，负责监督以色列与黎巴嫩边境的停火，并支持黎巴嫩政府。其任务授权目前延长至 2026 年 12 月，并计划随后缩减部署。该部队由 48 个国家的逾 8000 名军人组成。近期事件，包括 2024 年 10 月以色列坦克闯入联黎部队哨所，加剧了紧张局势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNIFIL">UNIFIL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Marjayoun">Marjayoun - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`

---

<a id="item-6"></a>
## [欧洲央行发布 2026 年 4 月消费者预期调查结果](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260601~bf8026bfc2.en.html) ⭐️ 7.0/10

欧洲央行发布了 2026 年 4 月消费者预期调查，提供了欧元区家庭通胀预期、收入增长和支出计划的最新微观数据。 该调查直接影响市场对欧洲央行加息或降息的预期，从而影响欧元区债券收益率和欧元汇率。任何与市场共识的显著偏离都可能引发对货币政策路径的重新定价。 2026 年 4 月调查为最新月度数据，市场关注 3 年期通胀预期中值和支出前景，此前读数徘徊在 2%目标附近。2026 年初，欧元短期利率远期曲线计入了年底前累计加息约 50 个基点。

rss · ECB Press Releases · Jun 1, 08:00

**背景**: 欧洲央行消费者预期调查自 2020 年启动，每月对欧元区各国家庭进行访问，衡量对通胀、经济增长和劳动力市场的感知与预期，是欧洲央行货币政策决策的关键分析工具。截至 2026 年 4 月，欧洲央行维持政策利率不变，整体通胀接近 2%目标，而市场预期下半年将启动紧缩周期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/stats/ecb_surveys/consumer_exp_survey/html/index.en.html">Consumer Expectations Survey</a></li>
<li><a href="https://www.ecb.europa.eu/press/economic-bulletin/html/eb202602.en.html">Economic Bulletin Issue 2, 2026 - European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#bonds`, `#currency`

---

<a id="item-7"></a>
## [欧洲央行施纳贝尔谈货币市场基金与稳定币的教训](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260601~38dffe5ec5.en.html) ⭐️ 7.0/10

欧洲央行执行委员会成员伊莎贝尔·施纳贝尔发表演讲，分析了货币市场基金和稳定币带来的金融稳定风险，并为央行政策和监管总结了教训。 此次演讲表明欧洲央行日益关注非银行金融中介和数字货币，可能对稳定币的严格监管、货币市场基金框架改革以及数字欧元的设计产生影响。 演讲可能着重指出了货币市场基金在 2008 年和 2020 年危机期间的挤兑风险，以及稳定币脱锚事件，呼吁建立强有力的监管保障和流动性要求。

rss · ECB Press Releases · Jun 1, 00:10

**背景**: 货币市场基金是投资于短期债务的共同基金，广泛用于现金管理，但容易发生流动性挤兑。稳定币是与美元等资产挂钩的加密货币，通常由储备资产支持，但曾发生脱锚并受到监管审查。包括欧洲央行在内的各国央行一直在研究这些工具对金融稳定构成的风险，特别是随着它们增长并与银行体系相互关联。此次演讲反映了金融稳定理事会等国际机构为加强非银行金融中介监管所做的持续努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Money_market_fund">Money market fund</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stablecoin">Stablecoin</a></li>
<li><a href="https://en.wikipedia.org/wiki/Financial_regulation">Financial regulation</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#currency`, `#global-markets`

---

<a id="item-8"></a>
## [欧洲央行埃尔德森呼吁加强面向 AI 的运营韧性](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260603~5b8e67f237.en.html) ⭐️ 6.0/10

2026 年 6 月 3 日，欧洲央行执行委员会成员弗兰克·埃尔德森发表讲话，强调需要增强金融机构的运营韧性，以应对人工智能带来的风险。 这表明欧洲央行将人工智能相关风险纳入金融稳定优先事项，可能导致更严格的监管预期，并影响《数字运营韧性法案》等监管框架。 讲话可能提及了现有的欧盟法规，如《数字运营韧性法案》（DORA），并强调金融实体需调整风险管理框架以应对人工智能特有的威胁。

rss · ECB Press Releases · Jun 3, 09:55

**背景**: 欧洲央行是欧元区的中央银行，负责货币政策和金融稳定。弗兰克·埃尔德森自 2020 年起担任执行委员会成员，负责法律服务并参与金融监管。欧盟的《数字运营韧性法案》（DORA）自 2025 年 1 月起生效，为金融部门的 ICT 风险管理设定了统一要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/Frank_Elderson">Frank Elderson</a></li>
<li><a href="https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en">Digital Operational Resilience Act (DORA) - European Insurance and...</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#europe`

---

<a id="item-9"></a>
## [欧洲央行称 2025 年欧元国际角色温和提升](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260602~f941e87516.en.html) ⭐️ 6.0/10

欧洲央行发布报告称，2025 年欧元在国际支付、官方储备和债务发行等方面的使用出现温和增长，反映出其全球角色的逐步提升。 这表明全球货币体系可能正逐渐多元化，减少对美元的依赖，有助于增强欧元区金融市场深度，并可能影响长期货币需求和全球储备管理策略。 报告可能包含欧元在全球支付、官方外汇储备和国际债务证券中的份额数据，但摘要未提供具体数字；更多细节需查阅完整报告。

rss · ECB Press Releases · Jun 2, 08:00

**背景**: 一种货币的国际角色通过其在发行国以外的使用来衡量，涉及贸易计价、官方储备和国际债务等领域。欧元自推出以来一直是仅次于美元的全球第二大货币。欧洲央行每年对此进行评估。

**标签**: `#central-bank`, `#currency`, `#macroeconomics`, `#global-markets`, `#europe`

---

<a id="item-10"></a>
## [监管机构进一步删除声誉风险引用](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260602a.htm) ⭐️ 6.0/10

美联储、联邦存款保险公司（FDIC）和货币监理署（OCC）联合更新了跨机构监管文件，进一步删除‘声誉风险’的提及。 此举表明银行监管的放松，可能降低合规成本，减少金融机构的风险规避，从而促进贷款和经济活动。 这是消除‘声誉风险’作为监管标准的持续努力的一部分，批评者认为该标准曾被用于施压银行切断与某些行业的联系。

rss · Federal Reserve Press Releases · Jun 2, 15:00

**背景**: 多年来，美国银行业监管机构在监管指引中使用‘声誉风险’来影响银行行为，常导致机构与合法但有政治争议的企业（如枪支制造商或发薪日贷款机构）切断联系。批评者认为这属于监管过度。2025 年，各机构开始删除这些引用，2026 年 6 月的行动延续了这一趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fdic.gov/news/press-releases/2026/agencies-remove-additional-references-reputation-risk">Agencies Remove Additional References to Reputation Risk | FDIC.gov</a></li>
<li><a href="https://www.jdsupra.com/legalnews/federal-banking-agencies-take-next-step-5273314/">Federal Banking Agencies Take Next Step in Dismantling “ Reputation ...”</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#united-states`

---

<a id="item-11"></a>
## [金融稳定理事会全体会议警示金融稳定新脆弱性](https://www.fsb.org/2026/06/fsb-plenary-highlights-potential-new-vulnerabilities-to-financial-stability/) ⭐️ 6.0/10

在近期于伦敦举行的全体会议上，金融稳定理事会（FSB）讨论了全球金融体系潜在的新脆弱性，但未公开具体细节。 作为 G20 负责金融稳定的关键国际机构，FSB 的警示表明监管机构可能很快将关注新兴风险，这可能导致更严格的宏观审慎政策，进而影响全球市场和金融机构。 此次讨论在一个非正式、非约束性论坛中进行；FSB 缺乏正式的监管权力，因此其警示有赖于成员辖区实施政策响应。未提供后续时间表或会议成果。

rss · Financial Stability Board News · Jun 1, 17:43

**背景**: 金融稳定理事会（FSB）于 2009 年由 G20 设立，以监测全球金融体系并提出建议，前身是金融稳定论坛。它包括所有 G20 主要经济体和欧盟委员会，由国际清算银行主办。与国际货币基金组织或世界银行不同，它没有条约基础，依靠成员合作。其全体会议通常评估当前状况和正在进行的工作流，例如非银行金融中介风险或气候相关财务披露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Financial_Stability_Board">Financial Stability Board</a></li>

</ul>
</details>

**标签**: `#financial-stability`, `#macroeconomics`, `#central-bank`, `#global-markets`

---