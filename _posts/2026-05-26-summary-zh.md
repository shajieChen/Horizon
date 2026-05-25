---
layout: default
title: "Horizon Summary: 2026-05-26 (ZH)"
date: 2026-05-26
lang: zh
---

> From 40 items, 14 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [俄罗斯用 90 枚导弹袭击基辅，含高超音速武器](#item-2) ⭐️ 10.0/10
3. [凯文·沃什宣誓就任美联储主席及 FOMC 主席](#item-3) ⭐️ 10.0/10
4. [古特雷斯：重开霍尔木兹海峡、改革安理会势在必行](#item-4) ⭐️ 8.0/10
5. [欧央行首席经济学家莱恩谈欧洲与全球经济](#item-5) ⭐️ 8.0/10
6. [第 11 次 NPT 审议大会未达成共识，核军备竞赛担忧加剧](#item-6) ⭐️ 7.0/10
7. [联合国警告医疗物资封锁加剧加沙危机](#item-7) ⭐️ 7.0/10
8. [联合国特使警告加沙过渡计划停滞将导致永久危机](#item-8) ⭐️ 7.0/10
9. [联合国难民署谴责乌克兰第聂伯罗致命导弹袭击](#item-9) ⭐️ 7.0/10
10. [欧央行官员强调气候与自然风险威胁金融稳定](#item-10) ⭐️ 7.0/10
11. [联合国大会支持国际法院气候咨询意见](#item-11) ⭐️ 6.0/10
12. [古特雷斯谴责以色列在东耶路撒冷 UNRWA 大院设军事设施](#item-12) ⭐️ 6.0/10
13. [安理会就平民保护举行辩论，每 14 分钟一平民丧生](#item-13) ⭐️ 6.0/10
14. [欧洲央行管理委员会发布非利率决策](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 25, 22:54

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
| QDII Nasdaq 100 Proxy | US | bullish 38/31/31 | bullish 38/31/31 | bullish 42/29/30 | high |
| US Mega Cap Basket | US | neutral 33/33/34 | neutral 33/33/34 | bullish 42/29/30 | high |
| Japan Equity Basket | JP | bullish 38/31/31 | bullish 38/31/31 | bullish 42/29/30 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | bullish 36/31/32 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=29904.25; 1d=+1.17%; 5d=+2.78%; 20d=+8.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=717.54; 1d=+0.42%; 5d=+1.21%; 20d=+8.08% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29481.64; 1d=+0.42%; 5d=+1.22%; 20d=+7.98% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=18.5%; implied_move=1.0%; put/call OI=2.1809228366271123 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：1日篮子收益与5日均线结构偏强
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | high |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | high |
| 1月 | 42% | 29% | 30% | bullish | 20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| NQ=F price trend | close=29904.25; 1d=+1.17%; 5d=+2.78%; 20d=+8.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=717.54; 1d=+0.42%; 5d=+1.21%; 20d=+8.08% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29481.64; 1d=+0.42%; 5d=+1.22%; 20d=+7.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NVDA price trend | close=215.33; 1d=-1.90%; 5d=-4.43%; 20d=+3.39% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=426.01; 1d=+1.95%; 5d=+0.89%; 20d=+13.21% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=418.57; 1d=-0.12%; 5d=-0.58%; 20d=-1.21% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=610.26; 1d=+0.47%; 5d=-0.65%; 20d=-9.60% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=382.97; 1d=-1.21%; 5d=-3.48%; 20d=+11.20% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=266.32; 1d=-0.80%; 5d=+0.83%; 20d=+0.88% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| AMZN options surface | ATM IV=27.2%; implied_move=1.6%; put/call OI=0.8934443145078077 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=24.8%; implied_move=1.4%; put/call OI=0.6160994497656409 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=39.7%; implied_move=2.3%; put/call OI=0.6466562449994461 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=35.8%; implied_move=2.1%; put/call OI=0.4118417504526368 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=20.0%; implied_move=1.1%; put/call OI=0.6927348662168984 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=26.2%; implied_move=1.5%; put/call OI=0.36467855537239624 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| AAPL insider filings | recent Form4 count=586 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| MSFT insider filings | recent Form4 count=731 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| NVDA insider filings | recent Form4 count=562 | 内部人交易节奏可作为估值温度辅助校验信号。 |

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
| NVDA price trend | close=215.33; 1d=-1.90%; 5d=-4.43%; 20d=+3.39% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=426.01; 1d=+1.95%; 5d=+0.89%; 20d=+13.21% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=418.57; 1d=-0.12%; 5d=-0.58%; 20d=-1.21% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 8035.T price trend | close=52180.00; 1d=+4.72%; 5d=+5.93%; 20d=+13.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=78860.00; 1d=-0.64%; 5d=+2.64%; 20d=+24.84% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7070.00; 1d=+4.63%; 5d=+26.41%; 20d=+36.46% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=91.61; 1d=+0.26%; 5d=+0.59%; 20d=+4.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=3026.00; 1d=+1.31%; 5d=+2.42%; 20d=-7.74% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3598.00; 1d=+2.07%; 5d=+0.06%; 20d=+7.53% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 跨层分歧信息有限，后续需补充更多波动与事件市场数据。

**Time stratification**
- 1日：1日篮子收益与5日均线结构偏强
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | medium |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | medium |
| 1月 | 42% | 29% | 30% | bullish | 20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 8035.T price trend | close=52180.00; 1d=+4.72%; 5d=+5.93%; 20d=+13.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=78860.00; 1d=-0.64%; 5d=+2.64%; 20d=+24.84% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7070.00; 1d=+4.63%; 5d=+26.41%; 20d=+36.46% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| EWH price trend | close=23.49; 1d=-1.43%; 5d=-2.37%; 20d=+0.56% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=127.00; 1d=+0.79%; 5d=-4.01%; 20d=-2.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=81.35; 1d=-0.91%; 5d=-1.63%; 20d=-2.11% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=121.70; 1d=-1.46%; 5d=-4.85%; 20d=+2.53% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=30.00; 1d=+1.15%; 5d=-2.28%; 20d=-3.78% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=441.40; 1d=+0.55%; 5d=-3.29%; 20d=-9.83% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
| EWH price trend | close=23.49; 1d=-1.43%; 5d=-2.37%; 20d=+0.56% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=127.00; 1d=+0.79%; 5d=-4.01%; 20d=-2.61% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=81.35; 1d=-0.91%; 5d=-1.63%; 20d=-2.11% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [Cboe Global Indices: VIX Index Dashboard](https://www.cboe.com/us/indices/dashboard/vix/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：The VIX Index is often referred to as the market's "fear gauge". The VIX Index is the centerpiece of Cboe Global Markets' volatility franchise, which includes volatility indexes...

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days out or more. IV is a forward looking prediction of the likelihood...

- [Cboe Global Indices: VXN Index Dashboard](https://www.cboe.com/us/indices/dashboard/VXN/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Cboe NASDAQ-100 Volatility Index SM (VXN) The Cboe NASDAQ-100 Volatility Index SM (VXN) is a key measure of market expectations of near-term volatility conveyed by NASDAQ-100 ®...

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [MOVE Index (MOVE) - MacroMicro](https://en.macromicro.me/charts/35584/us-treasury-move-index)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：The Merrill Lynch Option Volatility Estimate (MOVE) Index reflects the level of volatility in U.S. Treasury futures. The index is considered a proxy for term premiums of U.S. Tr...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [US High Yield Master II Option-Adjusted Spread (Market Dail…](https://ycharts.com/indicators/us_high_yield_master_ii_optionadjusted_spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：View market daily updates and historical trends for US High Yield Master II Option-Adjusted Spread. from United States. Source: Bank of America Merrill Ly…

- [U.S. High Yield Bond Spread (1996-2026) - Macrotrends](https://www.macrotrends.net/3229/us-high-yield-bond-spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：U.S. High Yield Bond Spread: 3.05% as of May 21, 2026. Units: Percent Frequency: Daily, Close Release: ICE BofA Indices Source: Ice Data Indices, LLC

- [QQQ Options Chain — Open Interest, Implied Volatility, Max Pain & Gamma ...](https://whalequant.io/en/stocks/QQQ/options-analytics)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Explore the live QQQ options chain with strikes, open interest, volume, implied volatility (IV), max pain levels, gamma exposure, dealer positioning and options flow analysis. P...

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [Current Values - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index?idx=nk225)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Current Values Nikkei calculates and publishes various types of the indexes such as the "Nikkei Stock Average (Nikkei 225)" which is known as a representative Japanese stock mar...

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

- [Live US Dollar to Yens Exchange Rate - $ 1 USD/JPY Today](https://usd.currencyrate.today/jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest and best $1 US Dollar to Yens rate for FREE. USD/JPY - Live exchange rates, banks, historical data & currency charts.

- [JPY to US Dollar Exchange Rate Today / Real-Time Currency Converter](https://xe-rates.com/jpy-to-usd)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert JPY to USD with real-time exchange rates. Free, fast currency converter with up-to-date rates for Japanese Yen to US Dollar conversions. Updated hourly.

- [USD/JPY (USDJPY=X) Live Rate, Chart & News - Yahoo Finance](https://finance.yahoo.com/quote/USDJPY=X/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Find the latest USD/JPY (USDJPY=X) currency exchange rate, plus historical data, charts, relevant news and more

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

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
## [俄罗斯用 90 枚导弹袭击基辅，含高超音速武器](https://news.un.org/feed/view/en/story/2026/05/1167583) ⭐️ 10.0/10

一夜之间，俄罗斯向基辅发射了约 90 枚导弹和 60 架无人机，其中包括一枚高超音速弹道导弹；联合国驻乌克兰高级官员谴责了此次袭击，并呼吁停止伤害平民。 这次升级加剧了地缘政治紧张局势，可能破坏外交努力，并可能因俄罗斯能源基础设施受损或进一步制裁而扰乱能源市场。 袭击中使用了高超音速弹道导弹，该导弹因其速度和机动性强而难以拦截；此类武器代表了俄罗斯打击能力的重大进步。

rss · UN News · May 24, 12:00

**背景**: 自 2022 年开始的俄乌冲突中，双方频繁攻击彼此的能源基础设施，导致全球能源价格波动。高超音速导弹是指速度超过 5 马赫且能在飞行中机动的导弹，对现有防御系统构成巨大挑战。俄罗斯此前已在乌克兰使用过“匕首”等高超音速武器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Russo-Ukrainian_war_(2022–present)">Russo- Ukrainian war (2022–present) - Wikipedia</a></li>
<li><a href="https://www.popularmechanics.com/military/a42386379/hypersonic-missiles-arms-race/">popularmechanics.com/ military /a42386379/ hypersonic - missiles ...</a></li>
<li><a href="https://www.breitbart.com/europe/2026/05/02/ukraine-strikes-oil-depots-deep-inside-russia-sending-prices-soaring/">Ukraine Strikes Oil Depots Deep Inside Russia , Sending Prices Soaring</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#military-risk`, `#geopolitics`, `#diplomacy`, `#energy`

---

<a id="item-3"></a>
## [凯文·沃什宣誓就任美联储主席及 FOMC 主席](https://www.federalreserve.gov/newsevents/pressreleases/other20260522a.htm) ⭐️ 10.0/10

2026 年 5 月 22 日，凯文·沃什宣誓就任美联储理事会主席及理事会成员，联邦公开市场委员会一致推选其担任该委员会主席。 作为美联储的最高决策者，此次领导层更迭可能预示着美国货币政策方向的转变，从而影响全球利率预期、通胀管理及金融市场状况。 沃什接替杰罗姆·鲍威尔出任主席，联邦公开市场委员会的一致推选显示了内部高度共识。主席任期四年，可连任，负责主持美联储理事会和制定联邦基金利率及公开市场操作的 FOMC。

rss · Federal Reserve Press Releases · May 22, 20:15

**背景**: 美联储理事会由七名理事组成，经总统任命、参议院批准，任期 14 年；主席从理事中选出，领导理事会和联邦公开市场委员会（FOMC）。FOMC 由全体七名理事和五名地区联邦储备银行行长组成，负责设定联邦基金利率目标，主导货币政策实施。凯文·沃什曾担任美联储理事和经济政策顾问，此次就任正值外界高度关注通胀与经济增长之际。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Board_of_Governors_of_the_Federal_Reserve_System">Board of Governors of the Federal Reserve System</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federal_Open_Market_Committee">Federal Open Market Committee - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chair_of_the_Federal_Reserve">Chair of the Federal Reserve - Wikipedia</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#united-states`, `#macroeconomics`, `#global-markets`

---

<a id="item-4"></a>
## [古特雷斯：重开霍尔木兹海峡、改革安理会势在必行](https://news.un.org/feed/view/en/story/2026/05/1167555) ⭐️ 8.0/10

联合国秘书长安东尼奥·古特雷斯呼吁立即重新开放霍尔木兹海峡，并敦促扩大联合国安理会成员范围，以限制常任理事国的否决权。 霍尔木兹海峡是全球最关键的能源通道，其封锁会冲击石油市场；安理会改革则可能重塑国际治理格局、减少僵局，对地缘政治和金融市场影响深远。 该海峡自 2026 年 2 月 28 日美以对伊朗发动空袭并刺杀其最高领袖后被封锁。古特雷斯明确将改革与限制否决权超级大国‘不受惩罚’的状况相挂钩，但未公布具体扩员方案。

rss · UN News · May 20, 12:00

**背景**: 霍尔木兹海峡每日通过约 2000 万桶石油，对全球能源至关重要。封锁起因于军事冲突。联合国安理会五个常任理事国拥有否决权，增加席位并限制否决权的改革努力因五常的抵制而长期停滞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis">2026 Strait of Hormuz crisis - Wikipedia</a></li>
<li><a href="https://windward.ai/glossary/the-strait-of-hormuz/">What Is the Strait of Hormuz ?</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council_veto_power">United Nations Security Council veto power - Wikipedia</a></li>

</ul>
</details>

**标签**: `#energy`, `#supply-chain`, `#geopolitics`, `#middle-east`, `#diplomacy`

---

<a id="item-5"></a>
## [欧央行首席经济学家莱恩谈欧洲与全球经济](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260522~f0f11a5f05.en.html) ⭐️ 8.0/10

欧央行首席经济学家菲利普·莱恩于 2026 年 5 月 22 日发表演讲，讨论欧洲及全球经济前景，可能涉及通胀、增长和货币政策方向的信号。 莱恩的评估可能影响市场对欧央行利率决策的预期，进而影响欧元汇率、债券收益率和全球资产价格。 演讲可能就通胀持续性、全球贸易紧张带来的增长风险以及货币政策正常化步伐提供最新看法。

rss · ECB Press Releases · May 22, 01:15

**背景**: 菲利普·莱恩自 2019 年起担任欧央行首席经济学家和执行委员会委员，主导货币政策分析。欧央行的首要职责是维持物价稳定，莱恩的演讲常在政策会议前预示管委会的思路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Philip_R._Lane">Philip R. Lane - Wikipedia</a></li>
<li><a href="https://www.ecb.europa.eu/mopo/strategy/html/index.en.html">Monetary policy strategy | European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`, `#currencies`

---

<a id="item-6"></a>
## [第 11 次 NPT 审议大会未达成共识，核军备竞赛担忧加剧](https://news.un.org/feed/view/en/story/2026/05/1167580) ⭐️ 7.0/10

《不扩散核武器条约》第 11 次审议大会在联合国经过四周谈判后，未能达成一致最终宣言。 未能达成共识削弱了全球核不扩散机制，加剧新的核军备竞赛担忧，并在地缘政治紧张局势加剧的背景下削弱了多边裁军努力。 会议未能产生最终文件，而该文件通常概述核裁军、核不扩散及和平利用核能的承诺。这延续了审议大会屡次失败的模式，反映出核武国与无核国之间的深刻分歧。

rss · UN News · May 23, 12:00

**背景**: 《不扩散核武器条约》自 1970 年生效，是全球核不扩散机制的基石，拥有 191 个缔约国。它基于三大支柱：不扩散、裁军及和平利用核能。审议大会每五年举行一次以评估进展，但经常无果而终，包括 2015 年和 2022 年的大会，加深了外界对该条约效力的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Non-Proliferation_Treaty">Non-Proliferation Treaty</a></li>
<li><a href="https://capssindia.org/the-role-of-the-npt-in-preserving-nuclear-dynamics-during-a-power-transition/">Why the 11th NPT Review Conference Matters in 2026</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#arms-control`

---

<a id="item-7"></a>
## [联合国警告医疗物资封锁加剧加沙危机](https://news.un.org/feed/view/en/story/2026/05/1167572) ⭐️ 7.0/10

联合国机构周五警告称，医疗物资被封锁，加上持续不断的暴力、鼠患和传染病蔓延，正在加剧加沙的人道主义危机。 这一警告加大了对以色列解除援助封锁的外交压力，可能影响停火谈判，并引发对安理会可能行动的关注，但目前对市场的直接影响有限。 关键细节包括有报道称出现鼠患和疾病传播，无国界医生组织自 2026 年 1 月 1 日起无法向加沙运送任何物资，医院面临非传染性疾病药物和纱布等基本用品的严重短缺。

rss · UN News · May 22, 12:00

**背景**: 加沙地带因以色列和哈马斯之间的长期战争而满目疮痍，2025 年 10 月达成的停火协议仅得到部分执行。尽管停火，以色列仍严格控制援助物资进入，导致食品、药品和其他必需品严重短缺。联合国及援助组织多次呼吁允许人道主义援助畅通无阻，警告可能出现饥荒和疾病暴发。国际法院此前裁决也要求以色列确保满足民众基本需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.doctorswithoutborders.org/latest/aid-and-supplies-are-still-being-blocked-entering-gaza">Aid and supplies are still being blocked from entering Gaza</a></li>
<li><a href="https://www.aljazeera.com/news/2025/12/7/no-gauze-no-gloves-israels-severe-restrictions-on-medical-aid-to-gaza">No essential supplies in truce: Gaza’s healthcare system ...</a></li>
<li><a href="https://news.un.org/en/story/2026/01/1166784">Gaza humanitarian crisis ‘far from being over,’ UN aid ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`, `#humanitarian`

---

<a id="item-8"></a>
## [联合国特使警告加沙过渡计划停滞将导致永久危机](https://news.un.org/feed/view/en/story/2026/05/1167568) ⭐️ 7.0/10

联合国特使在安理会表示，加沙过渡计划的拖延正加深人道主义苦难，并可能使该地区陷入永久性危机。 这一警告表明地区稳定风险上升；停火崩溃可能引发大规模暴力重燃，扰乱能源市场，并对美国主导的外交努力构成压力。 特使指出，停火脆弱且人道准入受限，若无政治进展，安全与人道局势将持续恶化。

rss · UN News · May 21, 12:00

**背景**: 联合国安理会根据《联合国宪章》第七章有权通过具有约束力的决议。为应对 2023 年加沙战争，安理会批准了战后治理与重建的过渡计划。加沙地带自 2007 年起遭受以色列封锁，200 多万人口面临严重人道危机。尽管 2025 年初促成了停火，但长期外交僵局和当地紧张局势使该计划停滞不前。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gaza_Strip">Gaza Strip - Wikipedia</a></li>
<li><a href="https://www.aljazeera.com/news/2025/1/15/what-do-we-know-about-the-israel-gaza-ceasefire-deal">What do we know about the Israel-Hamas ceasefire deal... | Al Jazeera</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`, `#sovereign-risk`

---

<a id="item-9"></a>
## [联合国难民署谴责乌克兰第聂伯罗致命导弹袭击](https://news.un.org/feed/view/en/story/2026/05/1167562) ⭐️ 7.0/10

周二晚，俄罗斯对乌克兰中东部城市第聂伯罗发动导弹和无人机袭击，造成平民死亡并摧毁人道主义援助。联合国难民署驻乌克兰代表对此予以强烈谴责。 此次袭击凸显针对乌克兰平民和人道主义行动的暴力仍在持续，可能促使西方盟友加大对乌军事援助并强化对俄制裁。 袭击目标是乌克兰中东部的主要工业和交通枢纽第聂伯罗。虽未立即公布具体伤亡数字，但人道主义援助物资被毁将直接阻碍救援工作。

rss · UN News · May 20, 12:00

**背景**: 难民署是联合国负责保护全球难民和流离失所者的机构。第聂伯罗是第聂伯河畔拥有近百万人口的城市，是重要的工业和交通枢纽。俄乌战争自 2014 年以来持续，2022 年 2 月俄罗斯全面入侵后急剧升级，造成大量平民伤亡和民众流离失所。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNHCR">UNHCR</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dnipro">Dnipro - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Russia-Ukraine_war">Russia-Ukraine war</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#military-risk`, `#geopolitics`, `#diplomacy`, `#humanitarian`

---

<a id="item-10"></a>
## [欧央行官员强调气候与自然风险威胁金融稳定](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260521~ccae6782e3.en.pdf) ⭐️ 7.0/10

欧洲央行执委会成员弗兰克·埃尔德森重申，气候变化和自然退化对金融稳定构成实质性风险，央行将把其纳入货币政策与银行监管之中。 此次发言为欧洲央行的政策走向提供了前瞻性指引，可能影响银行审慎标准、抵押品资质及投资者预期，并凸显气候风险在全球央行决策中日益重要的地位。 该演讲于 2026 年 5 月 21 日发表，可能讨论了实体风险和转型风险，并将关注范围延伸至自然退化，表明金融监管中全面纳入环境风险的趋势。

rss · ECB Press Releases · May 21, 15:30

**背景**: 欧洲央行的首要职责是维持价格稳定，但其次要目标是支持包括环境可持续在内的欧盟经济政策。近年来，全球央行普遍认识到气候变化通过实体损害和转型成本对金融稳定构成实质性风险。欧洲央行已开始将气候考量纳入银行监管，并在一定程度上融入货币政策操作，将气候风险视为金融风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank - Wikipedia</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#climate-risk`, `#europe`, `#regulation`

---

<a id="item-11"></a>
## [联合国大会支持国际法院气候咨询意见](https://news.un.org/feed/view/en/story/2026/05/1167561) ⭐️ 6.0/10

联合国大会通过了一项决议，支持国际法院 2025 年发布的咨询意见，该意见阐明了各国应对气候变化的法律义务。 此举加强了气候问责的法律框架，可能影响未来关于减排的国际诉讼和外交谈判。 该决议为不具约束力的国际法院意见增添了政治分量，该意见承认了条约法和习惯国际法下防止温室气体排放损害的义务。

rss · UN News · May 20, 12:00

**背景**: 国际法院是联合国的主要司法机关，应大会请求于 2025 年 7 月发布了咨询意见，确认各国有义务根据国际法防止气候变化造成的跨界环境损害。该决议由瓦努阿图等气候脆弱国家推动，在面临一些反对的情况下仍获得通过，肯定了上述意见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167561">General Assembly backs historic World Court climate crisis ...</a></li>
<li><a href="https://www.icj-cij.org/case/187">Obligations of States in respect of Climate Change</a></li>
<li><a href="https://en.wikipedia.org/wiki/Obligations_of_States_in_respect_of_climate_change">Obligations of States in respect of climate change - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#international-law`, `#climate`, `#united-nations`, `#sovereign-risk`

---

<a id="item-12"></a>
## [古特雷斯谴责以色列在东耶路撒冷 UNRWA 大院设军事设施](https://news.un.org/feed/view/en/story/2026/05/1167560) ⭐️ 6.0/10

周三，联合国秘书长古特雷斯强烈谴责以色列决定在东耶路撒冷被占领的 UNRWA 大院建立军事设施，称此举“完全不可接受”。 此举加剧了以色列与联合国之间的外交冲突，可能危及 UNRWA 向数百万巴勒斯坦难民提供援助的能力，并凸显了东耶路撒冷在国际法下的争议地位。 以色列此决定紧随其 2025 年将 UNRWA 定性为恐怖组织的法律和 2025 年 12 月警方闯入该大院的事件，尽管国际法院裁定以色列未能证实对 UNRWA 的指控。

rss · UN News · May 20, 12:00

**背景**: UNRWA 是联合国自 1949 年起向巴勒斯坦难民提供救济的机构，在包括东耶路撒冷在内的西岸、加沙等地运作。东耶路撒冷自 1967 年被以色列占领，1980 年被吞并，但未获国际承认。近年来，以色列指控 UNRWA 与哈马斯有关联并通过法律禁止其运作，而国际法院裁定这些指控缺乏证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNRWA">UNRWA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Occupied_East_Jerusalem">Occupied East Jerusalem</a></li>
<li><a href="https://www.i24news.tv/en/news/israel/diplomacy/artc-un-condemns-israel-s-seizure-of-unrwa-compound-as-ben-gvir-flotilla-stunt-draws-fire-at-home-and-abroad">UN condemns Israel's seizure of UNRWA compound as Ben-Gvir ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`, `#israel-palestine`

---

<a id="item-13"></a>
## [安理会就平民保护举行辩论，每 14 分钟一平民丧生](https://news.un.org/feed/view/en/story/2026/05/1167554) ⭐️ 6.0/10

联合国安理会召开了年度保护武装冲突中平民的公开辩论，联合国紧急救援协调员报告称，去年冲突中每 14 分钟就有一名平民遇难。 此次辩论凸显了不断上升的平民伤亡，可能影响未来的安理会决议或人道主义外交，并引起对国际人道法执行不力的关注。 该辩论虽为例行会议，但为谴责违反国际人道法的行为提供了平台；‘每 14 分钟一平民丧生’的惊人数据强调了危机的严重性，不过并未宣布立即的政策变化。

rss · UN News · May 20, 12:00

**背景**: 联合国安理会作为维护国际和平与安全的主要机构，自 1999 年以来每年举行保护平民的公开辩论，这是基于一系列敦促冲突各方遵守国际人道法的决议。尽管《日内瓦公约》及其附加议定书规定了法律义务，但平民仍承受着武装冲突的最大伤害，经常面临有针对性的攻击、不分皂白的轰炸和人道主义准入受阻。由人道事务协调厅等机构协调的联合国平民保护议程，强调各方在军事行动中必须始终注意避免伤害平民。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://www.unocha.org/protection-civilians">Protection of civilians | OCHA</a></li>
<li><a href="https://www.un.org/en/global-issues/crisis-and-emergency-response">Crisis and Emergency Response | United Nations</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`

---

<a id="item-14"></a>
## [欧洲央行管理委员会发布非利率决策](https://www.ecb.europa.eu//press/govcdec/otherdec/2026/html/ecb.gc260522~a4812a8f23.en.html) ⭐️ 6.0/10

2026 年 5 月 22 日，欧洲央行管理委员会公布了关于非利率货币政策措施的定期决议，涵盖资产购买计划、抵押品规则或流动性操作的调整。 这些决定可能影响欧元区的金融状况、债券收益率和外汇市场，并可能预示欧洲央行在利率之外的货币政策立场变化。 虽然完整细节载于公布的文件中，但市场参与者将仔细审视疫情紧急购买计划（PEPP）再投资、定向长期再融资操作（TLTRO）或抵押品宽松措施的任何修订。

rss · ECB Press Releases · May 22, 13:00

**背景**: 欧洲央行管理委员会是欧洲央行的主要决策机构，负责制定欧元区的货币政策。除了关键利率外，它还决定量化宽松（QE）计划和向银行提供流动性等非常规措施。这些工具对于管理通胀、支持贷款和稳定金融市场至关重要。欧洲央行在管委会会议后定期公布这些决议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ECB_Governing_Council">ECB Governing Council</a></li>
<li><a href="https://www.ecb.europa.eu/ecb/decisions/govc/html/index.en.html">Governing Council | European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`, `#bonds`

---