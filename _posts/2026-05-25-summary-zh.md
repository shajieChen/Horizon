---
layout: default
title: "Horizon Summary: 2026-05-25 (ZH)"
date: 2026-05-25
lang: zh
---

> From 40 items, 17 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [联合国安理会就阿联酋核电站遭无人机袭击召开紧急会议](#item-2) ⭐️ 9.0/10
3. [凯文·沃什宣誓就任美联储主席及 FOMC 主席](#item-3) ⭐️ 9.0/10
4. [《不扩散核武器条约》审议大会未达成共识，引发军备竞赛担忧](#item-4) ⭐️ 8.0/10
5. [联合国难民署谴责俄罗斯对乌克兰第聂伯罗的致命袭击](#item-5) ⭐️ 8.0/10
6. [古特雷斯呼吁重开霍尔木兹海峡并扩大安理会](#item-6) ⭐️ 8.0/10
7. [美伊停火脆弱，霍尔木兹危机仍冲击全球贸易](#item-7) ⭐️ 8.0/10
8. [美联储公布 2026 年 4 月 FOMC 会议纪要](#item-8) ⭐️ 8.0/10
9. [联合国安理会就卢甘斯克宿舍楼遭袭事件开会](#item-9) ⭐️ 7.0/10
10. [加沙：救命药品被封锁，杀戮持续，疾病蔓延](#item-10) ⭐️ 7.0/10
11. [联合国安理会辩论加沙未来 停火进展停滞](#item-11) ⭐️ 7.0/10
12. [欧洲央行莱恩就欧洲与世界经济发表演讲](#item-12) ⭐️ 7.0/10
13. [联合国大会通过历史性国际法院气候危机裁决决议](#item-13) ⭐️ 6.0/10
14. [古特雷斯谴责以色列将 UNRWA 园区用作军事设施](#item-14) ⭐️ 6.0/10
15. [联合国报告：黎巴嫩急救人员在真主党与以色列冲突中面临日益增长的危险](#item-15) ⭐️ 6.0/10
16. [联合国警告地缘政治紧张局势导致全球经济脆弱](#item-16) ⭐️ 6.0/10
17. [欧洲央行发布 2026 年 3 月 SESFOD 调查结果](#item-17) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 24, 22:53

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
| ^NDX price trend | close=29481.64; 1d=+0.42%; 5d=+1.22%; 20d=+7.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=717.54; 1d=+0.42%; 5d=+1.21%; 20d=+8.08% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29558.75; 1d=+0.00%; 5d=+1.59%; 20d=+7.72% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=15.1%; implied_move=1.0%; put/call OI=2.1809228366271123 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
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
| ^NDX price trend | close=29481.64; 1d=+0.42%; 5d=+1.22%; 20d=+7.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=717.54; 1d=+0.42%; 5d=+1.21%; 20d=+8.08% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29558.75; 1d=+0.00%; 5d=+1.59%; 20d=+7.72% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| AMZN price trend | close=266.32; 1d=-0.80%; 5d=+0.83%; 20d=+0.88% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=426.01; 1d=+1.95%; 5d=+0.89%; 20d=+13.21% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=215.33; 1d=-1.90%; 5d=-4.43%; 20d=+3.39% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=418.57; 1d=-0.12%; 5d=-0.58%; 20d=-1.21% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=382.97; 1d=-1.21%; 5d=-3.48%; 20d=+11.20% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=610.26; 1d=+0.47%; 5d=-0.65%; 20d=-9.60% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| AAPL options surface | ATM IV=16.3%; implied_move=1.1%; put/call OI=0.6927348662168984 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=32.4%; implied_move=2.3%; put/call OI=0.6466562449994461 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=22.2%; implied_move=1.6%; put/call OI=0.8934443145078077 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=21.4%; implied_move=1.5%; put/call OI=0.36467855537239624 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=29.2%; implied_move=2.1%; put/call OI=0.4118417504526368 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=20.3%; implied_move=1.4%; put/call OI=0.6160994497656409 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| MSFT insider filings | recent Form4 count=731 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| AAPL insider filings | recent Form4 count=586 | 内部人交易节奏可作为估值温度辅助校验信号。 |

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
| AMZN price trend | close=266.32; 1d=-0.80%; 5d=+0.83%; 20d=+0.88% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=426.01; 1d=+1.95%; 5d=+0.89%; 20d=+13.21% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=215.33; 1d=-1.90%; 5d=-4.43%; 20d=+3.39% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 8035.T price trend | close=49830.00; 1d=+2.11%; 5d=-0.91%; 20d=+12.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=79370.00; 1d=+3.13%; 5d=+2.84%; 20d=+23.96% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6757.00; 1d=+11.89%; 5d=+17.62%; 20d=+41.54% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=91.61; 1d=+0.26%; 5d=+0.59%; 20d=+4.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3525.00; 1d=-0.82%; 5d=-1.43%; 20d=+4.17% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2987.00; 1d=+0.30%; 5d=-3.18%; 20d=-11.89% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 8035.T price trend | close=49830.00; 1d=+2.11%; 5d=-0.91%; 20d=+12.61% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=79370.00; 1d=+3.13%; 5d=+2.84%; 20d=+23.96% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6757.00; 1d=+11.89%; 5d=+17.62%; 20d=+41.54% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9988.HK price trend | close=127.00; 1d=+0.79%; 5d=-4.01%; 20d=-2.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=81.35; 1d=-0.91%; 5d=-1.63%; 20d=-2.11% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.91; 1d=-2.61%; 5d=-4.47%; 20d=-6.66% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=35.52; 1d=-1.03%; 5d=-1.88%; 20d=-3.64% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=23.49; 1d=-1.43%; 5d=-2.37%; 20d=+0.56% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=441.40; 1d=+0.55%; 5d=-3.29%; 20d=-9.83% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
| 9988.HK price trend | close=127.00; 1d=+0.79%; 5d=-4.01%; 20d=-2.61% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=81.35; 1d=-0.91%; 5d=-1.63%; 20d=-2.11% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.91; 1d=-2.61%; 5d=-4.47%; 20d=-6.66% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [MOVE Index Charts and Quotes — TradingView](https://www.tradingview.com/symbols/TVC-MOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：MOVE INDEX Setup for Top in World stock markets The chart is the Move index it is reaching an area which I consider High level of Complacency I say this as of this writing The 1...

- [Cboe Global Indices: VIX Index Dashboard](https://www.cboe.com/us/indices/dashboard/vix/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：The VIX Index is often referred to as the market's "fear gauge". The VIX Index is the centerpiece of Cboe Global Markets' volatility franchise, which includes volatility indexes...

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
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days out or more. IV is a forward looking prediction of the likelihood...

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [QQQ Options - Live IV, Flow, Greeks & Analysis / ImpliedOptions ...](https://impliedoptions.com/ticker/qqq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Trade QQQ options with real-time implied volatility, IV rank, options flow, and Greeks. Analyze QQQ calls and puts with our free calculator and strategy builder.

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

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

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

- [Index Information - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index/profile?idx=nk225vi)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：The Nikkei Stock Average Volatility Index are calculated by using prices of Nikkei 225 futures and Nikkei 225 options on the Osaka Exchange (OSE). In the calculation, taking nea...

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [iShares MSCI Japan ETF (EWJ) stock price, news, quote and history ...](https://sg.finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [iShares MSCI Japan ETF (EWJ) Price Today, Chart, Holdings & Expense Ratio](https://vestedfinance.com/us-stocks/etf/ewj/japan-msci-etf-ishares-share-price/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Check the live iShares MSCI Japan ETF (EWJ) price, performance chart, historical returns, top holdings, expense ratio, and key fund details. Track real-time ETF data and insights.

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
## [联合国安理会就阿联酋核电站遭无人机袭击召开紧急会议](https://news.un.org/feed/view/en/story/2026/05/1167550) ⭐️ 9.0/10

联合国安理会召开紧急会议，讨论阿联酋巴拉卡核电站附近遭无人机袭击一事；国际原子能机构总干事拉斐尔·马里亚诺·格罗西向成员国通报了核安全与安保方面的关切。 这一事件直接提升了核事故风险，加剧了地区紧张局势，可能影响全球能源市场，并促使国际社会作出外交和军事回应。 无人机袭击发生在 2026 年 5 月 17 日，导致核电站周边起火；阿联酋国防部称该无人机来自伊拉克境内。国际原子能机构正在评估情况，安理会可能考虑进一步行动。

rss · UN News · May 19, 12:00

**背景**: 联合国安理会负责维护国际和平与安全，由 15 个成员国组成，其中 5 个常任理事国拥有否决权。国际原子能机构推动核能和平利用并监督核安全。巴拉卡核电站是阿拉伯世界首座核电站，于 2020 年投入运营，提供阿联酋高达 25%的电力。袭击核基础设施可能违反国际法，并引发人道主义和环境灾难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/IAEA">IAEA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Barakah_nuclear_power_plant">Barakah nuclear power plant</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`

---

<a id="item-3"></a>
## [凯文·沃什宣誓就任美联储主席及 FOMC 主席](https://www.federalreserve.gov/newsevents/pressreleases/other20260522a.htm) ⭐️ 9.0/10

凯文·沃什宣誓就任联邦储备系统理事会主席及理事，联邦公开市场委员会一致推选他担任委员会主席，正式接掌美国央行领导权。 作为美联储主席，沃什将主导美国货币政策，影响利率、通胀与金融稳定，其政策取向可能牵动全球市场与经济状况，因此备受关注。 主席任期为四年；FOMC 全票通过显示成员间高度共识。沃什在经济关键节点接任，但新闻稿未具名前任主席。

rss · Federal Reserve Press Releases · May 22, 20:15

**背景**: 美联储是美国的中央银行体系，由理事会和 12 家地区联邦储备银行构成。主席同时领导理事会与联邦公开市场委员会（FOMC），负责制定联邦基金利率以实现充分就业和价格稳定。凯文·沃什的任命遵循总统提名、参议院确认的既定程序，其领导将影响美联储双重使命下的货币政策决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Reserve_System">Federal Reserve System</a></li>
<li><a href="https://en.wikipedia.org/wiki/Board_of_Governors_of_the_Federal_Reserve">Board of Governors of the Federal Reserve</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federal_Open_Market_Committee">Federal Open Market Committee</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#united-states`, `#global-markets`, `#financial-stability`

---

<a id="item-4"></a>
## [《不扩散核武器条约》审议大会未达成共识，引发军备竞赛担忧](https://news.un.org/feed/view/en/story/2026/05/1167580) ⭐️ 8.0/10

《不扩散核武器条约》第十一次审议大会在联合国总部经过四周谈判后于周五结束，未能通过最后宣言。 此次失败表明核武国家与无核国家之间的分歧加深，削弱了全球核不扩散机制，可能助长不受约束的核军备竞赛，破坏国际安全并影响市场的地缘政治风险评估。 尽管对条约的三大支柱（核不扩散、核裁军与和平利用核能）进行了全面审议，但各方未能就统一路径达成一致，最后宣言草案因未解决的分歧而被否决。

rss · UN News · May 23, 12:00

**背景**: 《不扩散核武器条约》自 1970 年生效，是全球核不扩散的基石，拥有 191 个缔约国。条约承认五个核武国家（美、俄、英、法、中）并规定其有义务推进核裁军，无核国家则承诺不获取核武器。审议大会每五年举行一次；上一次 2022 年会议也未能达成共识文件，此次连续失败对条约信誉造成严重打击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nuclear_Non-Proliferation_Treaty_(NPT)">Nuclear Non-Proliferation Treaty (NPT)</a></li>
<li><a href="https://www.iaea.org/publications/documents/treaties/npt">Treaty on the Non - Proliferation of Nuclear Weapons ( NPT ) | IAEA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Arms_race">Arms race</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`

---

<a id="item-5"></a>
## [联合国难民署谴责俄罗斯对乌克兰第聂伯罗的致命袭击](https://news.un.org/feed/view/en/story/2026/05/1167562) ⭐️ 8.0/10

周二晚间，俄罗斯对乌克兰第聂伯罗发动导弹和无人机袭击，造成平民伤亡和严重基础设施损毁，引发联合国难民署（UNHCR）的强烈谴责。 第聂伯罗是乌克兰防御后勤的战略要地，此次袭击突显冲突持续升级，可能引发更强烈的国际外交回应，同时加剧地缘政治风险，影响能源市场情绪。 袭击击中了第聂伯罗，该市是距离各主要战线大致等距的关键后勤枢纽，有平民伤亡报告，但当时未立即公布具体死伤人数。

rss · UN News · May 20, 12:00

**背景**: 联合国难民署自 1994 年起在乌克兰开展工作，2014 年冲突后及 2022 年全面入侵后大幅扩大了人道主义响应。第聂伯罗是战略要地，距离顿涅茨克和哈尔科夫等主要战场约 320 公里，是乌克兰防御行动的关键后勤和补给枢纽。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unhcr.org/ua/en">UNHCR, the UN Refugee Agency | UNHCR Ukraine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dnipro">Dnipro - Wikipedia</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#diplomacy`, `#military-risk`, `#geopolitics`, `#europe`

---

<a id="item-6"></a>
## [古特雷斯呼吁重开霍尔木兹海峡并扩大安理会](https://news.un.org/feed/view/en/story/2026/05/1167555) ⭐️ 8.0/10

联合国秘书长安东尼奥·古特雷斯公开呼吁重新开放霍尔木兹海峡，并主张扩大联合国安理会以限制常任理事国的否决权。 霍尔木兹海峡是全球石油和天然气运输的关键咽喉要道，其关闭可能导致能源价格飙升和供应中断。将此与安理会改革挂钩，加大了迫使否决权大国有效应对冲突的外交压力。 该海峡每年运输全球 20%的液化天然气和 25%的海运石油，并已受到 2026 年伊朗战争的影响。古特雷斯明确要求扩大安理会成员，以遏制他所谓的超级大国否决权滥用。

rss · UN News · May 20, 12:00

**背景**: 位于伊朗和阿曼之间的霍尔木兹海峡是波斯湾唯一的出海通道，对全球能源安全至关重要。联合国安理会设有五个拥有否决权的常任理事国（中国、法国、俄罗斯、英国、美国），这一架构被普遍认为已经过时。数十年来改革讨论不断，但需要所有五常同意才能实现。2026 年伊朗战争导致该海峡关闭，引发危机，古特雷斯借此机会强调制度改革之必要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council_reform">UN Security Council reform</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council_Veto_power">UN Security Council Veto power</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#middle-east`, `#supply-chain`

---

<a id="item-7"></a>
## [美伊停火脆弱，霍尔木兹危机仍冲击全球贸易](https://news.un.org/feed/view/en/story/2026/05/1167548) ⭐️ 8.0/10

尽管美伊达成脆弱停火，霍尔木兹海峡周边的不稳定局势持续扰乱全球贸易，推高能源成本，加剧全球生活成本危机。 这一关键咽喉要道的不稳定威胁石油和液化天然气供应，推高通胀，给全球家庭预算带来压力，并可能影响货币政策与地缘政治紧张局势。 霍尔木兹海峡处理全球 20%的液化天然气和 25%的海运石油，在 2026 年伊朗战争期间首次遭遇严重持续中断；目前的谈判旨在全面重开该海峡，但航运中断和高额保险成本仍在持续。

rss · UN News · May 19, 12:00

**背景**: 霍尔木兹海峡是伊朗与阿曼之间的狭窄水道，是波斯湾唯一的出海通道。全球 20%的液化天然气和 25%的海运石油经由该海峡运输。2026 年伊朗战争导致海峡部分关闭，引发危机。6 月宣布停火，但不稳定局势依然存在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire">2026 Iran war ceasefire - Wikipedia</a></li>
<li><a href="https://apnews.com/article/iran-us-war-ceasefire-negotiations-hormuz-e603a7759d6cbd70ce5ed01f439a29dc">Details emerge of a potential Iran deal after Trump claims progress | AP News</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#energy`, `#supply-chain`, `#middle-east`, `#commodities`

---

<a id="item-8"></a>
## [美联储公布 2026 年 4 月 FOMC 会议纪要](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260520a.htm) ⭐️ 8.0/10

美联储公布了 2026 年 4 月 28-29 日联邦公开市场委员会会议纪要，详细披露了决策者对经济前景、通胀趋势及利率决策依据的讨论。 会议纪要为市场提供了美联储政策倾向的重要洞察，塑造对未来利率走向的预期，并影响债券收益率、股票估值和美元走势。 关键细节通常包括工作人员经济预测、对前景风险的讨论以及任何反对票，这些可以预示货币政策的可能路径。

rss · Federal Reserve Press Releases · May 20, 18:00

**背景**: 联邦公开市场委员会是美联储的货币政策制定机构。其会议纪要在政策决定三周后公布，比会后声明更全面地反映了委员会的审议情况，被市场密切分析以寻找未来政策调整的信号。

**标签**: `#central-bank`, `#macroeconomics`, `#bonds`, `#equities`, `#currency`

---

<a id="item-9"></a>
## [联合国安理会就卢甘斯克宿舍楼遭袭事件开会](https://news.un.org/feed/view/en/story/2026/05/1167578) ⭐️ 7.0/10

俄罗斯指责乌克兰袭击了卢甘斯克占领区的一栋民用宿舍楼，造成六人死亡，而乌克兰声称其打击的是一个军用无人机指挥中心，此事促使联合国安理会召开会议，会上一位联合国高级官员警告战争‘正日益致命’。 该事件加剧了俄乌之间的外交紧张局势，可能影响未来联合国安理会的动态或制裁讨论，同时突显了沉重的平民伤亡和对国际法的涉嫌违反。 有争议的袭击据称发生在夜间，伤亡者中包括儿童；俄罗斯请求召开安理会会议，指控其违反国际人道法。

rss · UN News · May 22, 12:00

**背景**: 由于俄罗斯作为常任理事国拥有否决权，安理会在应对乌克兰战争时往往陷入僵局。国际人道法，尤其是《日内瓦公约》，要求冲突方区分军事目标和平民。卢甘斯克地区自 2014 年以来一直被俄罗斯支持的力量占领，但国际社会公认其属于乌克兰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ukraine_and_the_United_Nations">Ukraine and the United Nations - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/International_humanitarian_law">International humanitarian law - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#russia-ukraine`, `#military-risk`

---

<a id="item-10"></a>
## [加沙：救命药品被封锁，杀戮持续，疾病蔓延](https://news.un.org/feed/view/en/story/2026/05/1167572) ⭐️ 7.0/10

联合国机构警告称，加沙急需的医疗物资被阻止进入，加剧了人道主义危机，当地暴力持续，鼠患和传染病蔓延。 在持续冲突中封锁医疗物资可能导致卫生灾难，可能促使国际制裁、援助行动或外交转变，影响地区稳定和全球市场。 2026 年前五个月已记录超过 12.5 万例与鼠类和寄生虫相关的皮肤感染病例；以色列的封锁将部分医疗用品列为“双重用途”物资，限制其进口。

rss · UN News · May 22, 12:00

**背景**: 自 2007 年哈马斯掌控加沙以来，以色列与埃及实施封锁，严格管制物资进入。以色列以安全为由，将某些医疗设备视为可能被用于军事的“双重用途”物品，限制其进口。持续冲突已严重破坏加沙的医疗系统，导致清洁水源和卫生设施不足，鼠患和传染病因此蔓延。联合国近东救济工程处（UNRWA）虽在加沙提供教育、医疗和援助，但面临巨大的准入挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaza_imports">Blockade of the Gaza Strip - Wikipedia</a></li>
<li><a href="https://phr.org/our-work/resources/faqs-access-to-health-care-supplies-and-dual-use-items-and-restrictions/">FAQs: Access to Health Care Supplies and “Dual Use” Items and Restrictions - PHR</a></li>
<li><a href="https://hodhodyemennews.net/en_US/2026/05/21/gaza-facing-acute-spread-of-rodent-and-parasite-related-diseases-due-to-zionist-siege/">Gaza facing acute spread of rodent and parasite related diseases due...</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#diplomacy`, `#geopolitics`, `#military-risk`, `#humanitarian`

---

<a id="item-11"></a>
## [联合国安理会辩论加沙未来 停火进展停滞](https://news.un.org/feed/view/en/story/2026/05/1167563) ⭐️ 7.0/10

联合国安理会开会讨论加沙局势，一名高级特使警告说，安理会支持的过渡计划延迟实施将加剧苦难并破坏恢复。 这次辩论凸显国际社会在推动加沙和平上的困难，若停火破裂或治理争端升级，可能影响地区稳定和能源市场。 该过渡计划需要哈马斯解除武装并放弃治理，接受国际监督，但在脆弱的停火条件下实施受阻。

rss · UN News · May 21, 12:00

**背景**: 联合国安理会负责维护国际和平与安全，五个常任理事国拥有否决权。加沙冲突在 2023 年 10 月哈马斯袭击后升级，演变为持久战争。2025 年 10 月达成脆弱的停火，但人道主义状况依然严峻。安理会现正讨论一项涉及哈马斯解除武装和建立新治理结构的过渡计划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://www.un.org/unispal/document/amid-a-tenuous-ceasefire-and-soaring-humanitarian-needs-the-security-council-hears-updates-on-transitional-governance-structures-and-reconstruction-efforts-in-gaza/">Amid a tenuous ceasefire and soaring humanitarian needs, the Security Council hears updates on transitional governance structures and reconstruction efforts in Gaza - Question of Palestine</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-12"></a>
## [欧洲央行莱恩就欧洲与世界经济发表演讲](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260522~f0f11a5f05.en.html) ⭐️ 7.0/10

欧洲央行首席经济学家菲利普·莱恩于 2026 年 5 月 22 日发表了关于欧洲在全球经济中作用的演讲，可能透露了欧洲央行对经济前景和政策立场的见解。 市场密切关注莱恩的言论，以寻找未来利率和量化紧缩路径的信号，这可能影响债券收益率、欧元汇率和股市。 该演讲发布在欧洲央行官网上，但详细内容未立即公布；任何语气变化都可能影响对欧洲央行未来政策会议的预期。

rss · ECB Press Releases · May 22, 01:15

**背景**: 欧洲央行负责制定欧元区货币政策以维持物价稳定。作为首席经济学家，菲利普·莱恩主导支撑管理委员会决策的经济分析。他的讲话经常提供关于利率和资产购买方向的线索，尤其是在政策会议之前。莱恩曾任爱尔兰中央银行行长，以其学术背景和对欧洲央行政策的重大影响力而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/Philip_R._Lane">Philip R. Lane</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`

---

<a id="item-13"></a>
## [联合国大会通过历史性国际法院气候危机裁决决议](https://news.un.org/feed/view/en/story/2026/05/1167561) ⭐️ 6.0/10

联合国大会通过决议，支持国际法院关于各国在气候变化方面承担法律义务的咨询意见，将气候行动从政治酌情权转变为国际法下的法定义务。 这强化了追究国家法律责任的法律基础，可能重塑气候诉讼、企业风险评估，并对更雄心勃勃的气候政策形成外交压力，对能源、大宗商品和保险市场产生长期影响。 该决议于 2026 年 5 月 20 日以 A/80/L.65 号文件通过，虽不具约束力，但强化了 2025 年 7 月国际法院的咨询意见；该意见同样不具约束力，但具有权威分量，可能影响国家法院的判决和国际谈判。

rss · UN News · May 20, 12:00

**背景**: 2025 年 7 月，联合国主要司法机关国际法院发布了一项具有里程碑意义的咨询意见，明确了各国在国际法下应对气候变化的义务，包括减排和合作的义务。该意见应瓦努阿图等国家联盟的请求作出，认为不作为构成国际不法行为，将引发国家责任。2026 年联合国大会的决议正式支持这一意见，旨在巩固其权威并推动其融入国家和国际政策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ejiltalk.org/from-opinion-to-action-the-general-assembly-votes-to-operationalize-the-icjs-climate-advisory-opinion/">From Opinion to Action: The General Assembly Votes to...</a></li>
<li><a href="https://www.ipsnews.net/2026/05/un-general-assembly-votes-for-resolution-on-icj-advisory-ruling-on-climate-obligations/">UNGA Votes on ICJ Advisory Ruling on Climate Obligations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Obligations_of_States_in_respect_of_climate_change">Obligations of States in respect of climate change - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#sovereign-risk`

---

<a id="item-14"></a>
## [古特雷斯谴责以色列将 UNRWA 园区用作军事设施](https://news.un.org/feed/view/en/story/2026/05/1167560) ⭐️ 6.0/10

联合国秘书长古特雷斯强烈谴责以色列在被占领的东耶路撒冷没收联合国近东救济工程处（UNRWA）园区并设立军事设施的决定，称此举“完全不可接受”。 此举加剧了以色列与联合国的紧张关系，损害联合国机构的特权和豁免，引发对 UNRWA 所服务的 590 万巴勒斯坦难民的人道主义关切，并可能促使联合国安理会采取行动或引发更广泛的外交后果。 该园区属于 UNRWA，其任务期限已延长至 2026 年 6 月。以色列对 UNRWA 的禁令于 2025 年 1 月生效，国际法院于 2025 年 10 月裁定以色列对该机构的指控缺乏依据。

rss · UN News · May 20, 12:00

**背景**: UNRWA 于 1949 年成立，旨在援助巴勒斯坦难民，在包括西岸和东耶路撒冷在内的五个地区开展业务。东耶路撒冷自 1967 年起被以色列占领并于 1980 年吞并，根据国际法被视为被占领土。以色列长期反对 UNRWA，于 2025 年禁止其活动并指控其与哈马斯有联系，但国际法院未支持这些指控。没收园区并将其军事化标志着严重升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNRWA">UNRWA</a></li>
<li><a href="https://www.ejiltalk.org/another-brick-in-the-wall-israels-seizure-of-unrwa-facilities-in-east-jerusalem/">Another Brick in the Wall: Israel ’s Seizure of UNRWA Facilities in East ...</a></li>
<li><a href="https://www.nytimes.com/2026/01/20/world/middleeast/israel-unrwa-jerusalem.html">Israel Seizes UNRWA ’s Jerusalem Headquarters - The New York...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-15"></a>
## [联合国报告：黎巴嫩急救人员在真主党与以色列冲突中面临日益增长的危险](https://news.un.org/feed/view/en/story/2026/05/1167556) ⭐️ 6.0/10

联合国强调，自 2026 年 3 月 2 日真主党与以色列的敌对行动升级以来，黎巴嫩救援人员和医护人员每天都面临生命危险，经常在前往袭击现场前相互诀别。 这凸显了冲突的惨重人道代价和救援人员面临的风险，可能促使各界呼吁加强对平民和人道主义准入的保护，并影响国际外交努力和资金支持。 救援人员出发前告别的画面在广泛传播的视频中可见；联合国指出，尽管此前宣布了停火，但人道局势仍在恶化，不过报告未提供急救人员的具体伤亡数字。

rss · UN News · May 20, 12:00

**背景**: 真主党是黎巴嫩的什叶派伊斯兰政治和军事组织，与以色列的冲突断断续续持续数十年。2026 年 3 月 2 日，在经历相对平静和黎巴嫩政府近期试图解除该组织武装的背景下，冲突再次升级。联合国驻黎巴嫩临时部队（UNIFIL）自 1978 年以来一直监督边境地区，但未能阻止敌对行动。冲突导致大量平民流离失所，使黎巴嫩本就脆弱的医疗系统承受重压，急救人员不得不在极度危险的环境中工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167483">Middle East: Deadly weekend in Lebanon , continued... | UN News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://www.etude.lu/article/lebanon-israel-hezbollah-escalation-2026">Israel - Hezbollah Escalation Has Killed 2,500 in... — Étude — Étude</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#military-risk`, `#middle-east`, `#humanitarian`

---

<a id="item-16"></a>
## [联合国警告地缘政治紧张局势导致全球经济脆弱](https://news.un.org/feed/view/en/story/2026/05/1167551) ⭐️ 6.0/10

联合国警告称，地缘政治冲突、能源成本上升和金融不稳定正在威胁全球经济增长与贸易，标志着世界经济进入一个更加脆弱的时期。 这一官方警告表明宏观脆弱性加剧，可能影响市场情绪、各国政策协调以及稳定全球经济的国际努力。 该警告是联合国新闻简报的一部分，该简报还涵盖了加沙援助资金短缺、南苏丹暴力事件以及清真寺袭击事件，表明目前同时存在多重危机。未提供具体的经济数据或政策应对措施。

rss · UN News · May 19, 12:00

**背景**: 联合国定期监测全球经济状况，此前已多次强调贸易紧张局势、能源市场混乱和金融市场波动带来的风险。持续的俄乌冲突和中东不稳定等地缘政治冲突加剧了这些担忧，推高能源价格并扰乱供应链。

**标签**: `#geopolitics`, `#energy`, `#financial-stability`, `#macroeconomics`, `#trade-policy`

---

<a id="item-17"></a>
## [欧洲央行发布 2026 年 3 月 SESFOD 调查结果](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260520~feb373ad0d.en.html) ⭐️ 6.0/10

欧洲央行发布了 2026 年 3 月最新的 SESFOD 季度调查结果，详细说明了证券融资和场外衍生品交易的价格与非价格信贷条件变化，提供了关于市场流动性、对手方风险和抵押品要求的最新指标。 该调查是监测欧元区金融稳定的关键工具，信贷条件收紧可能表明风险厌恶情绪上升或融资压力加大，进而影响银行间借贷、市场流动性和资产价格，并对欧洲央行的货币政策和宏观审慎决策产生影响。 SESFOD 调查涵盖不同对手方类型的价格条件（如利差）和非价格条件（如折扣率、最长期限），提供了对市场运作的细致洞察，补充了银行借贷调查等其他欧洲央行调查。

rss · ECB Press Releases · May 20, 09:00

**背景**: SESFOD 调查由欧洲央行自 2012 年起每季度进行，调查对象为欧元区主要银行的高级信贷官员。调查重点在于证券融资（回购）和场外衍生品市场中的欧元计价交易，这些市场对银行融资和风险管理至关重要。调查结果用于评估金融体系的潜在脆弱性，并为欧洲央行的金融稳定审查提供参考。

**标签**: `#central-bank`, `#financial-stability`, `#bonds`, `#europe`, `#macro-risk`

---