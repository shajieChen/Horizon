---
layout: default
title: "Horizon Summary: 2026-05-13 (ZH)"
date: 2026-05-13
lang: zh
---

> From 44 items, 12 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [联合国秘书长呼吁霍尔木兹海峡紧急降级](#item-2) ⭐️ 9.0/10
3. [美巴提出安理会决议要求伊朗停止霍尔木兹海峡袭击](#item-3) ⭐️ 9.0/10
4. [联合国称以色列空袭贝鲁特南郊“非常令人担忧”](#item-4) ⭐️ 8.0/10
5. [欧央行副行长德金多斯接受金融时报采访](#item-5) ⭐️ 8.0/10
6. [拉加德：稳定币功能与工具应分离](#item-6) ⭐️ 8.0/10
7. [FSB 警告私人信贷脆弱性](#item-7) ⭐️ 8.0/10
8. [黎巴嫩与加沙暴力持续，停火协议形同虚设](#item-8) ⭐️ 7.0/10
9. [欧央行施纳贝尔警告央行独立性正悄然侵蚀](#item-9) ⭐️ 7.0/10
10. [欧央行奇波洛内谈新能冲击情景与政策启示](#item-10) ⭐️ 7.0/10
11. [欧洲央行工资追踪器显示 2026 年谈判工资压力稳定](#item-11) ⭐️ 7.0/10
12. [黎巴嫩脆弱停火下，家庭觅食维生难](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 13, 02:00

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
| QDII Nasdaq 100 Proxy | US | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | high |
| US Mega Cap Basket | US | neutral 31/34/35 | bullish 36/29/34 | bullish 40/32/28 | high |
| Japan Equity Basket | JP | bullish 38/31/31 | bullish 38/31/31 | bullish 42/29/30 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=29235.00; 1d=-0.64%; 5d=+3.91%; 20d=+12.46% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29064.80; 1d=-0.87%; 5d=+3.75%; 20d=+12.47% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=707.24; 1d=-0.85%; 5d=+3.76%; 20d=+12.51% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=20.5%; implied_move=0.9%; put/call OI=1.4669350201265094 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.42; 2Y=3.95; 10Y-2Y=0.46999999999999975 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=66.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| NQ=F price trend | close=29235.00; 1d=-0.64%; 5d=+3.91%; 20d=+12.46% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29064.80; 1d=-0.87%; 5d=+3.75%; 20d=+12.47% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=707.24; 1d=-0.85%; 5d=+3.76%; 20d=+12.51% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| TSLA price trend | close=433.45; 1d=-2.60%; 5d=+11.32%; 20d=+19.01% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=220.78; 1d=+0.61%; 5d=+12.36%; 20d=+12.35% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=294.80; 1d=+0.72%; 5d=+3.83%; 20d=+14.00% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=387.35; 1d=-0.33%; 5d=-0.28%; 20d=+16.35% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=407.77; 1d=-1.18%; 5d=-0.88%; 20d=+3.73% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=265.82; 1d=-1.18%; 5d=-2.83%; 20d=+6.75% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| META options surface | ATM IV=33.5%; implied_move=1.4%; put/call OI=0.5486978128163441 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=27.2%; implied_move=1.1%; put/call OI=0.2676625765631001 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=32.0%; implied_move=1.3%; put/call OI=0.6076871066729079 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=61.5%; implied_move=2.6%; put/call OI=0.9441622487979288 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=44.0%; implied_move=1.8%; put/call OI=0.6352335573896026 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=31.0%; implied_move=1.3%; put/call OI=0.5219675126323903 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.42; 2Y=3.95; 10Y-2Y=0.46999999999999975 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| AAPL insider filings | recent Form4 count=587 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| NVDA insider filings | recent Form4 count=567 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| CNN Fear & Greed | score=66.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：短线隐含波动偏高，回撤与震荡风险上升
- 1周：5日收益与20日均线结构支持1周偏多；期权隐含波动较高，1周方向分歧增加
- 1月：20日趋势维持上行，1月窗口偏多；期权市场仍在计入较高下行尾部风险；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 31% | 34% | 35% | neutral | 短线隐含波动偏高，回撤与震荡风险上升 | high |
| 1周 | 36% | 29% | 34% | bullish | 5日收益与20日均线结构支持1周偏多；期权隐含波动较高，1周方向分歧增加 | high |
| 1月 | 40% | 32% | 28% | bullish | 20日趋势维持上行，1月窗口偏多；期权市场仍在计入较高下行尾部风险；风险偏好仍可控且波动未失控，中期上行概率提高 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| TSLA price trend | close=433.45; 1d=-2.60%; 5d=+11.32%; 20d=+19.01% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=220.78; 1d=+0.61%; 5d=+12.36%; 20d=+12.35% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=294.80; 1d=+0.72%; 5d=+3.83%; 20d=+14.00% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9984.T price trend | close=5977.00; 1d=-0.17%; 5d=+10.20%; 20d=+58.33% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.06; 1d=-0.22%; 5d=+3.14%; 20d=+2.96% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=78950.00; 1d=-0.39%; 5d=+3.26%; 20d=+28.19% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=50890.00; 1d=-2.43%; 5d=+7.25%; 20d=+20.62% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2912.50; 1d=+2.44%; 5d=-2.92%; 20d=-12.56% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3695.00; 1d=+6.06%; 5d=+18.16%; 20d=+9.48% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=66.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.42; 2Y=3.95; 10Y-2Y=0.46999999999999975 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| 9984.T price trend | close=5977.00; 1d=-0.17%; 5d=+10.20%; 20d=+58.33% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.06; 1d=-0.22%; 5d=+3.14%; 20d=+2.96% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=78950.00; 1d=-0.39%; 5d=+3.26%; 20d=+28.19% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9618.HK price trend | close=126.40; 1d=+6.76%; 5d=+8.59%; 20d=+9.53% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=31.28; 1d=-0.57%; 5d=+1.49%; 20d=+1.30% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=37.33; 1d=-0.37%; 5d=+2.30%; 20d=+1.19% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=24.18; 1d=-0.58%; 5d=+1.98%; 20d=+1.30% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=86.20; 1d=+2.44%; 5d=+4.48%; 20d=+1.29% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=458.80; 1d=+0.35%; 5d=-0.91%; 20d=-6.97% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.42; 2Y=3.95; 10Y-2Y=0.46999999999999975 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=66.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| 9618.HK price trend | close=126.40; 1d=+6.76%; 5d=+8.59%; 20d=+9.53% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=31.28; 1d=-0.57%; 5d=+1.49%; 20d=+1.30% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=37.33; 1d=-0.37%; 5d=+2.30%; 20d=+1.19% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [MOVE Index Charts and Quotes — TradingView](https://www.tradingview.com/symbols/TVC-MOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：MOVE INDEX Setup for Top in World stock markets The chart is the Move index it is reaching an area which I consider High level of Complacency I say this as of this writing The 1...

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [Cboe Global Indices: VIX Index Dashboard](https://www.cboe.com/us/indices/dashboard/vix/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：The VIX Index is often referred to as the market's "fear gauge". The VIX Index is the centerpiece of Cboe Global Markets' volatility franchise, which includes volatility indexes...

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days or more out. IV is a forward looking prediction of the likelihood...

- [Cboe Nasdaq-100 Implied Volatil (^CNIV05) - Yahoo Finance](https://finance.yahoo.com/quote/%5ECNIV05/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Find the latest information on Cboe Nasdaq-100 Implied Volatil (^CNIV05) including data, charts, related news and more from Yahoo Finance

- [QQQ Implied Volatility / IV Rank & Percentile / projectoption](https://projectoption.com/stocks/qqq/implied-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ implied volatility is 20.7%. View IV Rank, IV Percentile, and 1-year historical IV chart for Invesco QQQ Trust.

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

- [ICE BofA US High Yield (MERH0A0) - Investing.com](https://www.investing.com/indices/ice-bofa-us-high-yield)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：Get detailed information on the ICE BofA US High Yield including charts, technical analysis, components and more.

- [iShares MSCI Japan ETF (EWJ) - Yahoo Finance](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [iShares MSCI Japan ETF / EWJ](https://www.ishares.com/us/products/239665/ishares-msci-japan-etf)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：The iShares MSCI Japan ETF seeks to track the investment results of an index composed of Japanese equities.

- [EWJ ETF Stock Price & Overview](https://stockanalysis.com/etf/ewj/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Get a real-time stock price for the EWJ ETF (iShares MSCI Japan ETF) with an overview of various metrics and statistics.

- [1 USD to JPY - US Dollars to Japanese Yen Exchange Rate - Xe](https://www.xe.com/en/currencyconverter/convert/?Amount=1&From=USD&To=JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest 1 US Dollar to Japanese Yen rate for FREE with the original Universal Currency Converter. Set rate alerts for USD to JPY and learn more about US Dollars and Japan...

- [USD to JPY - US Dollar to Japanese Yen Conversion - Exchange Rates](https://www.exchange-rates.org/converter/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Use the USD to JPY currency converter at Exchange-Rates.org for accurate and up-to-date exchange rates. Easily convert US Dollars to Japanese Yen with real-time data.

- [USD JPY / US Dollar to Yen Live Rate - Investing.com](https://www.investing.com/currencies/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get real time data on the USD/JPY pair including the live rate, as well as our currency converter, analysis, news, historical data and more.

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

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
## [联合国秘书长呼吁霍尔木兹海峡紧急降级](https://news.un.org/feed/view/en/story/2026/05/1167478) ⭐️ 9.0/10

联合国秘书长紧急呼吁在霍尔木兹海峡实现降级，因伊朗与美国紧张局势升温推动油价走高。 该海峡是全球能源运输的关键咽喉，任何中断都会威胁石油供应、推高价格并带来广泛的经济与安全影响，尤其对能源进口地区。 该海峡承载全球 20%的液化天然气及 25%的海运石油贸易量，关闭将严重冲击欧亚。当前危机源于 2026 年伊朗战争。

rss · UN News · May 11, 12:00

**背景**: 霍尔木兹海峡是伊朗与阿曼之间一条狭窄水道，连接波斯湾与阿曼湾及阿拉伯海，是多个海湾国家唯一出海通道，也是全球能源供应的关键航线。自 2026 年起，紧张局势升级为活跃危机，军事冲突风险威胁安全通航。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://www.britannica.com/place/Strait-of-Hormuz">Strait of Hormuz | Map, Importance, Conflict and Closure ... Strait of Hormuz - Wikipedia What is the Strait of Hormuz, and Why Does it Matter? Strait of Hormuz Live Tracker — Real-Time Shipping & Oil ... What to know as the US tries to open the Strait of Hormuz and ... Images What is the Strait of Hormuz, and why does its closure matter ... Explainer: What is the Strait of Hormuz and why is it so ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#middle-east`, `#military-risk`

---

<a id="item-3"></a>
## [美巴提出安理会决议要求伊朗停止霍尔木兹海峡袭击](https://news.un.org/feed/view/en/story/2026/05/1167464) ⭐️ 9.0/10

巴林和美国在联合国安理会散发了一份决议草案，呼吁伊朗停止在霍尔木兹海峡的袭击，两国大使周四在联合国总部向记者通报了此事。 霍尔木兹海峡是全球石油和液化天然气运输的关键咽喉要道；安理会决议可能导致进一步制裁或军事行动，扰乱能源市场并影响全球供应链。 决议草案于周四在联合国总部向记者概述；若根据第七章通过，可授权执行措施，但五个常任理事国中的任何一国都可行使否决权。决议的具体要求和执行机制尚未公开。

rss · UN News · May 7, 12:00

**背景**: 联合国安理会负责维护国际和平与安全，有权根据第七章实施制裁或授权动武。霍尔木兹海峡是全球最重要的石油运输咽喉，约 25%的海运石油通过此处。2026 年，伊朗战争和霍尔木兹海峡危机导致紧张局势升级；伊朗历史上曾威胁关闭该航道。巴林是海湾君主国，也是美国第五舰队司令部所在地，是美国的紧密盟友，此次联合行动是一次协调的外交施压。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#middle-east`, `#iran`

---

<a id="item-4"></a>
## [联合国称以色列空袭贝鲁特南郊“非常令人担忧”](https://news.un.org/feed/view/en/story/2026/05/1167460) ⭐️ 8.0/10

以色列夜间空袭贝鲁特南郊（达希耶），造成新一波平民流离失所，联合国谴责此为“非常令人担忧的事态发展”。 这次空袭标志着以色列-真主党冲突的危险升级，威胁地区稳定，并可能扰乱能源市场。它还破坏了近期的停火努力，引发了对更广泛人道主义危机的担忧。 此次空袭的目标是人口稠密的什叶派聚居区和真主党据点达希耶，但当地也居住着大量平民。伤亡和破坏的全部程度尚不清楚，在持续停火谈判中袭击的精确触发因素也不明确。

rss · UN News · May 7, 12:00

**背景**: 以色列-真主党冲突始于 2023 年 10 月，真主党声援加沙的巴勒斯坦人。2024 年的升级导致以色列对黎巴嫩进行了猛烈轰炸、入侵，并暗杀了真主党领导人哈桑·纳斯鲁拉。2024 年 11 月达成了停火，并延长至 2025 年，但 2026 年伊朗战争后暴力再度爆发。达希耶是贝鲁特的南郊，尽管是住宅区，但作为真主党的据点经常成为袭击目标。此前的袭击已使黎巴嫩超过一百万人流离失所。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167460">Lebanon: Fresh strike on Beirut suburbs ‘a very alarming development’ | UN News</a></li>
<li><a href="https://www.bbc.com/news/articles/cz7jx575pg7o">Dahieh : The Beirut suburb bearing the brunt of Israeli bombing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Israel-Hezbollah_conflict_(2023-2024)">Israel-Hezbollah conflict (2023-2024)</a></li>

</ul>
</details>

**标签**: `#military-risk`, `#middle-east`, `#diplomacy`, `#geopolitics`, `#energy`

---

<a id="item-5"></a>
## [欧央行副行长德金多斯接受金融时报采访](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260511~3fa2df2fa9.en.html) ⭐️ 8.0/10

欧央行副行长路易斯·德金多斯接受《金融时报》采访，就货币政策立场、通胀前景和欧元区经济状况发表了看法。 该采访可能改变市场对欧央行利率变动的预期，影响欧元、欧洲债券和整体风险情绪，因为欧央行高层的言论常会引发市场波动。 采访的具体内容未在本文中公开，但高层采访本身表明欧央行可能在为市场预做准备，应对潜在的政策转向。

rss · ECB Press Releases · May 11, 04:00

**背景**: 欧央行负责制定欧元区货币政策，欧元区目前由 21 个使用欧元的欧盟国家组成。副行长德金多斯是关键决策者，其采访能让外界一窥管理委员会的思路。《金融时报》是重要财经媒体，央行官员在该报的采访常含有影响市场的言论。市场会仔细解读此类采访，以寻找关于未来利率决议和经济前景的线索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://www.ecb.europa.eu/">European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#currencies`, `#global-markets`

---

<a id="item-6"></a>
## [拉加德：稳定币功能与工具应分离](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260508~dd909fbed1.en.html) ⭐️ 8.0/10

欧洲央行行长拉加德在关于稳定币与货币未来的演讲中，主张将支付等货币功能与执行功能的私人工具明确分离，强化了欧洲央行的监管立场。 这表明欧洲央行决心通过确保稳定币接受央行监督来维护货币主权和金融稳定，这将塑造欧盟加密货币监管并推动数字欧元的紧迫性。 演讲可能强调稳定币可处理支付功能，但不应在没有监管保障的情况下发行类似货币的负债，同时凸显欧洲央行数字欧元项目补充实物现金的必要性。

rss · ECB Press Releases · May 8, 07:00

**背景**: 稳定币是锚定法币等稳定资产的加密货币，引发了威胁货币主权和金融稳定的担忧。欧洲央行长期警惕美元稳定币侵蚀欧元地位，并正在开发数字欧元作为公共替代方案。欧盟的《加密资产市场监管》法规为稳定币设定了规则，但欧洲央行推动更严格的措施，确保只有央行货币仍是支付系统的锚定物。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ainvest.com/news/ecb-stablecoin-stance-impact-global-fintech-markets-2510/">ECB 's Stablecoin Stance and Its Impact on Global Fintech Markets</a></li>
<li><a href="https://www.brookings.edu/articles/what-are-stablecoins-and-how-are-they-regulated/">What are stablecoins, and how are they regulated? | Brookings</a></li>
<li><a href="https://en.wikipedia.org/wiki/Central_bank_digital_currency">Central bank digital currency</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#digital-currency`, `#financial-stability`, `#regulation`, `#europe`

---

<a id="item-7"></a>
## [FSB 警告私人信贷脆弱性](https://www.fsb.org/2026/05/fsb-warns-on-private-credit-vulnerabilities/) ⭐️ 8.0/10

金融稳定理事会（FSB）正式警告，私人信贷领域的复杂性、高杠杆和深度互联互通可能在不利经济条件下放大压力，威胁更广泛的金融稳定。 作为主要国际标准制定机构的警告，它表明快速增长的私人信贷市场存在较高的系统性风险，可能导致监管收紧，影响中型企业的信贷供给和更广泛的市场流动性。 警告指出，私人信贷资产规模迅速增长至约 1.5 至 2 万亿美元，并指出其复杂性、杠杆和互联互通是关键脆弱点；FSB 虽无正式执法权，但其制定的全球监管标准通常会影响到国家政策。

rss · Financial Stability Board News · May 6, 06:00

**背景**: 金融稳定理事会（FSB）是 2008 年金融危机后成立的国际机构，旨在监测全球金融体系并提出建议，成员包括所有 G20 主要经济体，总部设在巴塞尔。私人信贷是指非银行、不在公开市场交易的直接贷款，属于影子银行体系，自 2008 年危机后因银行面临更严格监管而迅速增长。该市场目前为中型企业提供大量融资，但透明度和监管程度低于传统银行贷款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Financial_Stability_Board">Financial Stability Board</a></li>
<li><a href="https://en.wikipedia.org/wiki/Private_credit">Private credit</a></li>
<li><a href="https://www.fsb.org/">Financial Stability Board - Promoting global financial stability through strong financial sector policies</a></li>

</ul>
</details>

**标签**: `#financial-stability`, `#macroeconomics`, `#global-markets`

---

<a id="item-8"></a>
## [黎巴嫩与加沙暴力持续，停火协议形同虚设](https://news.un.org/feed/view/en/story/2026/05/1167483) ⭐️ 7.0/10

联合国周一表示，尽管上月与以色列宣布停火，黎巴嫩的人道主义局势仍在恶化；与此同时，黎巴嫩和加沙地区的致命暴力事件持续发生。 持续不断的暴力事件破坏了停火协议，可能重新点燃更广泛的地区冲突，或将邻国卷入其中，干扰外交努力和人道主义援助的进行。 停火协议规定真主党需解除武装，并由黎巴嫩军队和联合国驻黎临时部队（UNIFIL）监督执行，但双方均有违反协议的行为，执行力度薄弱。

rss · UN News · May 11, 12:00

**背景**: 2024 年 11 月达成的以色列-黎巴嫩停火协议结束了自 2023 年 10 月 8 日真主党发动袭击、以色列随后入侵以来长达一年多的跨境战斗。联合国安理会 2006 年通过的第 1701 号决议旨在黎巴嫩南部建立缓冲区。加沙人道主义危机自 2023 年 10 月以哈战争爆发以来持续至今，造成大面积破坏与民众流离失所。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2024_Israel–Lebanon_ceasefire_agreement">2024 Israel – Lebanon ceasefire agreement - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/04/17/world/middleeast/israel-lebanon-ceasefire.html">Israel - Lebanon Cease - Fire : What to Know - The New York Times</a></li>
<li><a href="https://www.cfr.org/articles/israel-hamas-war-humanitarian-crisis-gaza">The Israel-Hamas War: The Humanitarian Crisis in Gaza | Council on...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-9"></a>
## [欧央行施纳贝尔警告央行独立性正悄然侵蚀](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260507_1~d5ae988ece.en.html) ⭐️ 7.0/10

2026 年 5 月 7 日，欧央行执委会成员伊莎贝尔·施纳贝尔发表讲话，警告央行独立性正悄悄受到侵蚀，可能威胁通胀控制与金融稳定。 这种侵蚀危及货币政策长期可信度与宏观经济稳定，政治干预或财政主导可能削弱欧央行维持价格稳定的能力，反映出全球民粹主义抬头与债务压力下的普遍风险。 施纳贝尔指出，央行独立性不仅可能因法律修改受损，还可能因授权扩大、政治施压以及财政与货币政策界线模糊等渐进方式被侵蚀。

rss · ECB Press Releases · May 7, 17:00

**背景**: 央行独立性指中央银行在制定货币政策时不受短期政治干预的原则，这一概念在 20 世纪 70 年代高通胀后为锚定通胀预期而被广泛采纳。根据《马斯特里赫特条约》设立的欧央行在法律上具有高度独立性，将价格稳定作为首要任务。近年来，欧元区央行面临为政府债务融资及扩大职权范围的压力，引发了对‘财政主导’与独立性侵蚀的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Central_bank_independence">Central bank independence</a></li>
<li><a href="https://www.imf.org/en/news/articles/2024/06/17/sp061424-central-bank-independence">Central Bank Independence: Why It’s Needed and How to ... - IMF</a></li>
<li><a href="https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp260507_annex~dbb6d582b4.en.pdf">The quiet erosion of central bank independence</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#financial-stability`, `#europe`, `#monetary-policy`

---

<a id="item-10"></a>
## [欧央行奇波洛内谈新能冲击情景与政策启示](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260506~1bbd4ed780.en.html) ⭐️ 7.0/10

2026 年 5 月 6 日，欧央行执董会成员皮耶罗·奇波洛内发表演讲，详细阐述了影响欧洲的最新能源冲击的经济情景与政策影响。 该演讲可传递欧央行对能源驱动通胀风险与增长前景的评估，可能影响市场对未来利率决策的预期，进而影响债券收益率与欧元汇率。 奇波洛内强调，尽管存在贸易紧张，欧洲实际收入、消费和投资仍展现韧性，这一平衡的经济背景可能影响欧央行的政策校准。

rss · ECB Press Releases · May 6, 08:20

**背景**: 自 2022 年以来，欧洲遭遇了多次能源冲击：俄乌战争引发天然气价格飙升、2023-2024 年红海航运受阻，以及 2024-2026 年的第三次价格激增。欧央行此前曾大幅收紧政策以应对能源驱动的通胀。此次新冲击考验央行在增长脆弱、反通胀仍在进行中的策略，奇波洛内的讲话成为观察其当前思路的风向标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp260506~1bbd4ed780.en.html">The new energy shock: economic scenarios and policy implications</a></li>
<li><a href="https://www.ecb.europa.eu/press/blog/date/2026/html/ecb.blog20260413~78ef6fe470.en.html">Why monetary policy hits harder after big shocks</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#energy`, `#macroeconomics`, `#europe`, `#financial-stability`

---

<a id="item-11"></a>
## [欧洲央行工资追踪器显示 2026 年谈判工资压力稳定](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260506~4ea17afd4a.en.html) ⭐️ 7.0/10

欧洲央行工资追踪器显示，欧元区经平滑处理的一次性支付后的谈判工资增速从 2025 年的 3.2%下降至 2026 年的 2.3%，涵盖范围也从 51.3%降至 41.9%。这表明工资驱动的通胀压力依然受控，且未再次加速。 稳定的工资压力支持了潜在通胀正在缓和的观点，这可能使欧洲央行得以维持或放松其限制性货币政策立场。这会影响欧元区债券收益率、欧元汇率以及市场对降息的预期。 该追踪器利用活跃集体谈判协议的细粒度数据库，覆盖了九个欧元区国家。一次性支付经过平滑处理，这些机械性效应预计在 2026 年消退，同时各国间工资压力的差异较往年收窄。

rss · ECB Press Releases · May 6, 08:00

**背景**: 欧洲央行工资追踪器是欧元体系下的一个合作项目，由欧洲央行和九个国家央行共同参与。它汇总集体谈判协议数据，以提供工资变动的及时指标，这对评估通胀动态至关重要。该追踪器于 2022 年首次推出，用于监测疫情后的工资趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260506~4ea17afd4a.en.html">New data release: ECB wage tracker indicates negotiated wage pressures stable in 2026</a></li>
<li><a href="https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260211_1~dd029e0063.en.html">New data release: ECB wage tracker continues to suggest normalisation of negotiated wage pressures in 2026</a></li>

</ul>
</details>

**标签**: `#macroeconomics`, `#central-bank`, `#europe`, `#bonds`, `#global-markets`

---

<a id="item-12"></a>
## [黎巴嫩脆弱停火下，家庭觅食维生难](https://news.un.org/feed/view/en/story/2026/05/1167467) ⭐️ 6.0/10

尽管停火协议生效，以色列空袭仍使黎巴嫩南部村庄面目全非，导致持续杀戮与流离失所，救援队周五报告称家庭被迫觅食。 持续的人道主义灾难与停火的脆弱性可能引发以色列与真主党冲突再起，破坏地区稳定、干扰外交进程并影响全球能源市场。 救援组织称黎南村庄因以军空袭‘完全无法辨认’，凸显停火未能遏制暴力与流离失所。

rss · UN News · May 8, 12:00

**背景**: 自 2023 年 10 月以来，以色列与真主党跨境冲突升级，至 2024 年底演变为公开战争，对黎南造成严重破坏。2024 年 11 月达成的停火协议岌岌可危，违规行为持续，流离失所民众面临严重食品短缺。

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`

---