---
layout: default
title: "Horizon Summary: 2026-05-18 (ZH)"
date: 2026-05-18
lang: zh
---

> From 42 items, 12 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [全球能源及贸易中断加剧贫困与债务压力](#item-2) ⭐️ 8.0/10
3. [欧洲央行副行长接受金融时报采访](#item-3) ⭐️ 8.0/10
4. [美联储任命鲍威尔为临时主席以待沃什宣誓就职](#item-4) ⭐️ 8.0/10
5. [联合国车辆在乌克兰赫尔松遭两次袭击](#item-5) ⭐️ 7.0/10
6. [联合国谴责俄对基辅平民袭击违反人道法](#item-6) ⭐️ 7.0/10
7. [联黎部队警告无人机事件危及黎巴嫩维和人员](#item-7) ⭐️ 7.0/10
8. [欧洲央行首席经济学家莱恩谈能源供应冲击分析](#item-8) ⭐️ 7.0/10
9. [联合国警告：古巴停电致手术暂停，危机加剧](#item-9) ⭐️ 6.0/10
10. [以色列空袭加沙、西岸和黎巴嫩人道危机恶化](#item-10) ⭐️ 6.0/10
11. [也门各方同意在联合国调解下释放 1600 名被拘留者](#item-11) ⭐️ 6.0/10
12. [WFP 因资金紧缺将叙粮食援助减半](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 17, 23:03

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
| QDII Nasdaq 100 Proxy | US | neutral 33/33/34 | neutral 33/33/34 | bullish 42/29/30 | high |
| US Mega Cap Basket | US | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | high |
| Japan Equity Basket | JP | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | bullish 36/31/32 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=29240.50; 1d=+0.03%; 5d=-0.62%; 20d=+9.32% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=708.93; 1d=-1.51%; 5d=-0.32%; 20d=+9.26% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29125.20; 1d=-1.54%; 5d=-0.38%; 20d=+9.20% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=20.2%; implied_move=1.2%; put/call OI=2.5785918138795565 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.59; 2Y=4.09; 10Y-2Y=0.5 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=62.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：有效交易信号不足，使用保守基准分布。
- 1月：20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1月 | 42% | 29% | 30% | bullish | 20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| NQ=F price trend | close=29240.50; 1d=+0.03%; 5d=-0.62%; 20d=+9.32% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=708.93; 1d=-1.51%; 5d=-0.32%; 20d=+9.26% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29125.20; 1d=-1.54%; 5d=-0.38%; 20d=+9.20% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| MSFT price trend | close=421.92; 1d=+3.05%; 5d=+1.64%; 20d=-0.21% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=225.32; 1d=-4.42%; 5d=+4.70%; 20d=+11.72% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=396.78; 1d=-1.07%; 5d=-1.00%; 20d=+16.13% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=264.14; 1d=-1.15%; 5d=-3.13%; 20d=+5.42% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=300.23; 1d=+0.68%; 5d=+2.45%; 20d=+11.20% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=422.24; 1d=-4.75%; 5d=-1.43%; 20d=+5.40% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| MSFT options surface | ATM IV=35.6%; implied_move=2.0%; put/call OI=0.6081990223125696 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=32.1%; implied_move=1.7%; put/call OI=0.7374275419081936 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=31.9%; implied_move=1.8%; put/call OI=0.544439647196694 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=21.9%; implied_move=1.2%; put/call OI=0.5327261105784595 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=28.3%; implied_move=1.6%; put/call OI=0.40361334442288144 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=44.0%; implied_move=2.6%; put/call OI=0.6453932129159652 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| NVDA insider filings | recent Form4 count=562 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| CNN Fear & Greed | score=62.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.59; 2Y=4.09; 10Y-2Y=0.5 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| MSFT insider filings | recent Form4 count=730 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| AAPL insider filings | recent Form4 count=586 | 内部人交易节奏可作为估值温度辅助校验信号。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | high |
| 1月 | 42% | 29% | 30% | bullish | 20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| MSFT price trend | close=421.92; 1d=+3.05%; 5d=+1.64%; 20d=-0.21% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=225.32; 1d=-4.42%; 5d=+4.70%; 20d=+11.72% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=396.78; 1d=-1.07%; 5d=-1.00%; 20d=+16.13% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 7203.T price trend | close=3085.00; 1d=+2.56%; 5d=+5.90%; 20d=-7.05% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=5745.00; 1d=-0.43%; 5d=-6.30%; 20d=+52.63% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77180.00; 1d=-0.17%; 5d=-8.30%; 20d=+21.51% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3576.00; 1d=+3.83%; 5d=+14.84%; 20d=+10.00% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=50290.00; 1d=-1.78%; 5d=-4.12%; 20d=+18.44% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=91.07; 1d=-1.08%; 5d=-1.25%; 20d=+0.98% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.59; 2Y=4.09; 10Y-2Y=0.5 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=62.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
- 1月：20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | medium |
| 1月 | 42% | 29% | 30% | bullish | 20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 7203.T price trend | close=3085.00; 1d=+2.56%; 5d=+5.90%; 20d=-7.05% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=5745.00; 1d=-0.43%; 5d=-6.30%; 20d=+52.63% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77180.00; 1d=-0.17%; 5d=-8.30%; 20d=+21.51% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9618.HK price trend | close=127.90; 1d=-1.69%; 5d=+7.93%; 20d=+3.31% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=24.06; 1d=-1.47%; 5d=-0.91%; 20d=+2.51% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=132.30; 1d=-4.06%; 5d=-4.82%; 20d=-2.58% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=30.70; 1d=-3.22%; 5d=-3.09%; 20d=-4.24% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=82.70; 1d=-3.50%; 5d=-1.61%; 20d=-6.82% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=28.17; 1d=-3.53%; 5d=-4.67%; 20d=-7.49% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=62.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.59; 2Y=4.09; 10Y-2Y=0.5 | 利率曲线决定权益估值贴现与风险偏好上限。 |
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
- 1月：风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1月 | 36% | 31% | 32% | bullish | 风险偏好仍可控且波动未失控，中期上行概率提高 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 9618.HK price trend | close=127.90; 1d=-1.69%; 5d=+7.93%; 20d=+3.31% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=24.06; 1d=-1.47%; 5d=-0.91%; 20d=+2.51% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=132.30; 1d=-4.06%; 5d=-4.82%; 20d=-2.58% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days out or more. IV is a forward looking prediction of the likelihood...

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [Cboe Global Indices: CNIV01 Index Dashboard](https://www.cboe.com/us/indices/dashboard/cniv01/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Cboe Nasdaq-100 Implied Volatility Index Series is designed to measure the market's expectation of volatility implied by Nasdaq-100 Index puts and calls (NDX options) over a...

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [Cboe Global Indices: VIX Index Dashboard](https://www.cboe.com/us/indices/dashboard/vix/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：The VIX Index is often referred to as the market's "fear gauge". The VIX Index is the centerpiece of Cboe Global Markets' volatility franchise, which includes volatility indexes...

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

- [US High Yield Master II Option-Adjusted Spread (Market Dail…](https://ycharts.com/indicators/us_high_yield_master_ii_optionadjusted_spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：View market daily updates and historical trends for US High Yield Master II Option-Adjusted Spread. from United States. Source: Bank of America Merrill Ly…

- [United States - ICE BofA US High Yield Index Option-Adjusted Spread ...](https://tradingeconomics.com/united-states/bofa-merrill-lynch-us-high-yield-option-adjusted-spread-fed-data.html)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：United States - ICE BofA US High Yield Index Option-Adjusted Spread was 2.79% in May of 2026, according to the United States Federal Reserve. Historically, United States - ICE B...

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [QQQ Stock Volatility History & Chart Since 1999](https://wallstreetnumbers.com/etfs/qqq/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Get all-time historical data of QQQ historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [iShares MSCI Japan ETF / EWJ](https://www.ishares.com/us/products/239665/ishares-msci-japan-etf)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：The iShares MSCI Japan ETF seeks to track the investment results of an index composed of Japanese equities.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Nikkei Average Volatility (^NKVI.OS) - Yahoo Finance](https://finance.yahoo.com/quote/%5ENKVI.OS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Find the latest information on Nikkei Average Volatility (^NKVI.OS) including data, charts, related news and more from Yahoo Finance

- [Index Information - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index/profile?idx=nk225vi)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：The Nikkei Stock Average Volatility Index are calculated by using prices of Nikkei 225 futures and Nikkei 225 options on the Osaka Exchange (OSE). In the calculation, taking nea...

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
## [全球能源及贸易中断加剧贫困与债务压力](https://news.un.org/feed/view/en/story/2026/05/1167526) ⭐️ 8.0/10

联合国最新报告显示，全球能源和贸易中断导致食品和必需品价格上涨，经济增长放缓，脆弱国家数百万民众面临贫困和债务困境。 该报告凸显地缘政治与供应链冲击对贫困和主权债务的连锁影响，或促使 IMF、世界银行等多边机构加大援助与债务减免，并引发大宗商品价格波动，影响全球政策与市场。 报告虽未给出具体数据，但预示多边援助及主权债务谈判可能增加，尤其关注已处债务困境的国家。需密切关注 IMF、世界银行、G20 及各国政府的后续行动。

rss · UN News · May 15, 12:00

**背景**: 地缘政治冲突与贸易路线中断推高全球能源、粮食及运输成本，进口依赖型发展中国家首当其冲。许多国家已面临严重债务压力，偿债困难。IMF 和世界银行通过债务可持续性分析框架定期评估此类风险，当前形势可能进一步恶化其困境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.worldbank.org/en/programs/debt-toolkit/dsa">Debt Sustainability Analysis - World Bank Group</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#macroeconomics`, `#energy`, `#supply-chain`, `#sovereign-risk`

---

<a id="item-3"></a>
## [欧洲央行副行长接受金融时报采访](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260511~3fa2df2fa9.en.html) ⭐️ 8.0/10

路易斯·德金多斯讨论了欧元区经济前景、通胀及利率路径，暗示未来政策可能的调整。 他的言论为欧洲央行政策方向提供重要信号，可能影响利率预期、债券收益率和欧元汇率。 他强调依赖数据，并指出持续的经济阻力，未确认利率变动的具体时间表。

rss · ECB Press Releases · May 11, 04:00

**背景**: 作为欧洲央行副行长，德金多斯在欧元区货币政策制定中发挥关键作用。金融时报是一家重要的财经报纸，政策制定者常通过其向市场传递信号。欧洲央行一直在应对高通胀和低增长，市场密切关注降息信号。

**标签**: `#central-bank`, `#macroeconomics`, `#global-markets`, `#europe`, `#bonds`

---

<a id="item-4"></a>
## [美联储任命鲍威尔为临时主席以待沃什宣誓就职](https://www.federalreserve.gov/newsevents/pressreleases/other20260515a.htm) ⭐️ 8.0/10

美联储理事会于 2026 年 5 月 15 日任命杰罗姆·鲍威尔为代理主席，暂时履行职务，直至 5 月 13 日获参议院确认的凯文·沃什宣誓就任新主席。 这一领导层交接预示着货币政策方向可能出现转变，市场将评估沃什预期的鹰派或鸽派立场，从而影响利率、美元和金融状况。 临时任命遵循过往惯例；沃什的宣誓就职日期尚未公布，他此前的联储理事经历（2006-2011 年）暗示其政策取向或更趋市场化。

rss · Federal Reserve Press Releases · May 15, 21:00

**背景**: 美联储理事会领导美国中央银行，主席对货币政策具有重大影响力。杰罗姆·鲍威尔自 2018 年起担任主席，其任期近日结束。凯文·沃什曾于 2006 年至 2011 年担任美联储理事，也是一位金融家，由总统提名并于 2026 年 5 月 13 日获参议院确认接任。“代理主席”的任命确保在新主席宣誓就职前的连续性，这是过渡期的标准做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.federalreserve.gov/newsevents/pressreleases/other20260515a.htm">Federal Reserve Board names Jerome H. Powell as chair pro tempore ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kevin_Warsh">Kevin Warsh - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/business/2026/may/13/kevin-warsh-federal-reserve-chair">US Senate confirms Kevin Warsh as Federal Reserve chair, replacing Jerome Powell | Federal Reserve | The Guardian</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#united-states`, `#macroeconomics`, `#bonds`, `#currencies`

---

<a id="item-5"></a>
## [联合国车辆在乌克兰赫尔松遭两次袭击](https://news.un.org/feed/view/en/story/2026/05/1167525) ⭐️ 7.0/10

5 月 14 日，一辆带有明显联合国标志的人道主义车辆在乌克兰赫尔松市遭到两次无人机袭击，严重受损；联合国秘书长对此表示震惊，乌克兰官员指认是俄罗斯军队所为。 此次袭击直接威胁到中立的人道主义行动，可能违反了保护救援人员的国际人道法，并可能危及平民救援通道和脆弱的停火外交。 该车辆按联合国标准清晰标示，但仍被两次击中；目前没有立即报告人员伤亡，但车辆严重损坏；联合国人道主义事务协调厅指出，无人机的广泛使用增加了援助交付的难度。

rss · UN News · May 15, 12:00

**背景**: 自 2022 年俄罗斯全面入侵乌克兰以来，联合国在该国各地——常在前线附近——提供大规模人道主义援助。国际人道法（第 31 条规则）规定必须尊重并保护人道主义救援人员。此次事件突显了在无人机战和争夺前线并存的冲突中，救援人员面临日益增长的危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167525">World News in Brief: UN relief vehicle struck in Ukraine, emergency airdrops in South Sudan, backlash against LGBTIQ+ rights | UN News</a></li>
<li><a href="https://www.newsweek.com/videos/un-vehicle-struck-by-russian-drone-in-kherson-ukraine">UN Vehicle Struck By Russian Drone In Kherson, Ukraine - Newsweek</a></li>
<li><a href="https://ihl-databases.icrc.org/en/customary-ihl/v1/rule31">Customary IHL - Rule 31. Humanitarian Relief Personnel</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#military-risk`, `#diplomacy`, `#geopolitics`

---

<a id="item-6"></a>
## [联合国谴责俄对基辅平民袭击违反人道法](https://news.un.org/feed/view/en/story/2026/05/1167509) ⭐️ 7.0/10

联合国驻乌克兰人道协调员（a.i.）贝尔纳黛特·卡斯特尔-霍林斯沃思强烈谴责俄罗斯周四对基辅平民区的军事袭击，称其明显违反国际人道法。 这一正式谴责加大了国际社会对俄罗斯的法律和外交压力，可能促使联合国安理会或国际法院采取进一步行动，并凸显了冲突造成的人道代价。 袭击于周四发生在基辅平民区；联合国官员的声明明确将此次袭击定性为明显违反国际人道法的行为，但未提供伤亡数字。

rss · UN News · May 14, 12:00

**背景**: 联合国人道协调员是面临人道主义紧急情况国家中的联合国高级官员，负责协调救援行动。日内瓦公约中包含的国际人道法禁止攻击平民和民用物体。自 2022 年 2 月俄罗斯全面入侵乌克兰以来，已多次被指控违反这些法律。联合国一直记录平民伤亡并呼吁遵守国际人道法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Humanitarian_Coordinator">Humanitarian Coordinator - Wikipedia</a></li>
<li><a href="https://www.icrc.org/en/law-and-policy/geneva-conventions-and-their-commentaries">The Geneva Conventions and their Commentaries - ICRC</a></li>
<li><a href="https://casebook.icrc.org/highlight/protection-civilians">Protection of Civilians | How does law protect in war ...</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#diplomacy`, `#military-risk`, `#geopolitics`

---

<a id="item-7"></a>
## [联黎部队警告无人机事件危及黎巴嫩维和人员](https://news.un.org/feed/view/en/story/2026/05/1167496) ⭐️ 7.0/10

联合国驻黎巴嫩临时部队（联黎部队）警告称，涉及疑似真主党无人机和以色列军队的无人机活动及附近爆炸事件不断升级，正在危及联黎部队人员的安全。 这增加了以色列与真主党之间发生误判和更大范围冲突的风险，可能破坏黎巴嫩的稳定并影响地区地缘政治，甚至可能引动联合国安理会的介入。 事件涉及真主党无人机及以色列在联合国阵地附近的军事行动，爆炸发生在维和人员附近。

rss · UN News · May 13, 12:00

**背景**: 联黎部队成立于 1978 年，旨在确认以色列撤军并恢复和平，其任务在 2006 年战争后得到加强，负责监督停火并支持黎巴嫩军队。真主党是一个受伊朗支持的强大什叶派武装组织，实际控制着黎巴嫩南部部分地区，造成了脆弱的安全局势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Interim_Force_in_Lebanon">United Nations Interim Force in Lebanon - Wikipedia</a></li>
<li><a href="https://www.cfr.org/backgrounders/what-hezbollah">What Is Hezbollah? | Council on Foreign Relations</a></li>
<li><a href="https://en.kataeb.org/articles/eu-pledges-60-million-to-bolster-laf-role-in-southern-lebanon-stability">EU Pledges €60 Million to Bolster LAF Role in Southern Lebanon ...</a></li>

</ul>
</details>

**标签**: `#military-risk`, `#middle-east`, `#diplomacy`, `#geopolitics`, `#escalation-risk`

---

<a id="item-8"></a>
## [欧洲央行首席经济学家莱恩谈能源供应冲击分析](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260513~5b14c78806.en.html) ⭐️ 7.0/10

欧洲央行执行委员会委员菲利普·莱恩发表演讲，提出了分析能源供应冲击的框架，并评估其宏观经济和政策影响。 该演讲揭示了欧洲央行对能源驱动通胀风险的评估和货币政策应对思路，在市场高度关注地缘政治紧张局势和高能源价格之际，可能影响市场对利率和通胀的预期。 莱恩的演讲可能详细阐述了能源价格直接影响与更广泛通胀压力之间的区别，并强调欧洲央行专注于防止通过工资和通胀预期产生的第二轮效应。

rss · ECB Press Releases · May 13, 19:00

**背景**: 欧洲央行负责欧元区 20 国的货币政策。首席经济学家菲利普·莱恩负责经济分析方面的思想领导。能源供应冲击（能源供应突然中断或价格急剧上涨）可能推高通胀并抑制经济活动，给中央银行带来复杂的权衡取舍。在近期因地缘政治紧张导致能源价格飙升的背景下，欧洲央行强调需要遏制通胀的第二轮效应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp260325~ac2916a211.en.html">Navigating energy shocks: risks and policy responses</a></li>
<li><a href="https://www.euronews.com/business/2026/03/19/markets-on-edge-as-ecb-prepares-to-set-interest-rates-amid-energy-price-surge">Markets on edge as ECB prepares to set interest rates</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#energy`, `#macroeconomics`, `#commodities`

---

<a id="item-9"></a>
## [联合国警告：古巴停电致手术暂停，危机加剧](https://news.un.org/feed/view/en/story/2026/05/1167524) ⭐️ 6.0/10

联合国高级官员警告称，由于长期停电和燃料短缺，古巴各地医院正在暂停手术并面临严重药品短缺，医疗系统陷入瘫痪。 这预示着可能的人道主义紧急情况，或加速移民潮并加剧外交紧张，凸显美国制裁和能源短缺对平民生活的严重冲击。 哈瓦那部分地区停电长达 20 至 22 小时，医院无法运行救生设备，古巴能源部长证实该国已无燃油和柴油可用。

rss · UN News · May 15, 12:00

**背景**: 古巴正深陷经济危机，源于长达数十年的美国封锁、政府管理不善以及近期美方限制石油运输的举措。该国高度依赖进口化石燃料来供电、交通和基本服务。燃料短缺导致大面积停电，破坏了医疗、食品和供水系统。联合国一再警告称，若石油供应不恢复，可能出现人道主义崩溃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ohchr.org/en/press-briefing-notes/2026/02/concerns-over-cubas-deepening-economic-crisis">Concerns over Cuba’s deepening economic crisis | OHCHR</a></li>
<li><a href="https://news.un.org/en/story/2026/04/1167254">Cuba energy crisis: Humanitarian needs remain despite fuel supplies | UN News</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#sovereign-risk`, `#latin-america`

---

<a id="item-10"></a>
## [以色列空袭加沙、西岸和黎巴嫩人道危机恶化](https://news.un.org/feed/view/en/story/2026/05/1167521) ⭐️ 6.0/10

联合国机构报告称，以色列在加沙、约旦河西岸和黎巴嫩持续进行的军事行动导致平民苦难加剧、流离失所，使人道援助工作不堪重负。 不断恶化的人道局势可能加剧国际社会对停火的外交压力，并带来区域不稳定的风险，若冲突升级扩散，或影响能源市场和地缘政治格局。 最新消息强调，联合国援助行动日益受持续敌对行动的限制，目前看不到立即停火的迹象，平民承受着最大冲击。

rss · UN News · May 15, 12:00

**背景**: 自 2023 年 10 月以来，以色列在加沙针对哈马斯展开军事行动，同时约旦河西岸暴力事件激增，与黎巴嫩真主党的跨境交火升级。这些冲突导致严重的人道危机，包括大量流离失所、伤亡和基础设施破坏，联合国机构一再呼吁缓和局势并允许援助进入。

**标签**: `#military-risk`, `#geopolitics`, `#middle-east`, `#diplomacy`

---

<a id="item-11"></a>
## [也门各方同意在联合国调解下释放 1600 名被拘留者](https://news.un.org/feed/view/en/story/2026/05/1167511) ⭐️ 6.0/10

在联合国于约旦的调解下，也门交战各方达成协议，释放超过 1600 名与冲突有关的被拘留者，这是自 2014 年内战开始以来最大规模的囚犯交换。 这一罕见的外交突破可能建立对立双方之间的信任，有望重启停滞的和平谈判，同时缓解人道主义关切并改善地区稳定观感。 该协议在约旦安曼经过数月谈判后敲定，由联合国特使汉斯·格伦德贝里宣布；一些报道称，该协议包括释放七名沙特囚犯。

rss · UN News · May 14, 12:00

**背景**: 也门内战始于 2014 年，胡塞叛军占领首都萨那，导致伊朗支持的胡塞武装与沙特支持的受国际认可政府之间长期冲突。自 2022 年起，联合国斡旋的脆弱休战得以维持，但和平进程陷入停滞。囚犯交换过去曾是建立信任的关键措施，上一次大规模交换发生在 2020 年。这项由约旦和联合国促成的协议，是迄今为止规模最大的一次释放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167511">Yemen parties agree under UN mediation to release 1,600 ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yemeni_civil_war_(2014–present)">Yemeni civil war (2014–present) - Wikipedia</a></li>
<li><a href="https://planet.news/article/yemen-prisoner-exchange-deal-1750-detainees-release-2026">Historic Yemen Prisoner Exchange Deal to Free 1,750... | Planet News</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`

---

<a id="item-12"></a>
## [WFP 因资金紧缺将叙粮食援助减半](https://news.un.org/feed/view/en/story/2026/05/1167499) ⭐️ 6.0/10

由于资金严重短缺，联合国世界粮食计划署已将叙利亚的紧急粮食援助减半，削减了对数十万弱势群体的支持。 这一削减加剧了数百万在脆弱冲突地区民众的粮食不安全状况，可能引发更多不稳定、流离失所，并对邻国和欧洲造成压力，进而影响外交和资金动态。 粮食计划署此前向数百万叙利亚人提供粮食援助；此次削减具体影响紧急援助，包括减少配给或取消受益者。目前尚未宣布新的资金承诺。

rss · UN News · May 13, 12:00

**背景**: 叙利亚自 2011 年以来陷入长期内战，导致大规模流离失所、基础设施毁坏和经济崩溃。联合国及人道主义机构一直在提供救生援助，但由于捐助疲劳和全球竞争性危机，资金逐渐减少。世界粮食计划署是全球抗击饥饿的最大人道主义组织，完全依赖自愿捐款。

**标签**: `#middle-east`, `#geopolitics`, `#humanitarian`

---