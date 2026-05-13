---
layout: default
title: "Horizon Summary: 2026-05-13 (ZH)"
date: 2026-05-13
lang: zh
---

> From 41 items, 9 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [联合国秘书长呼吁紧急缓解霍尔木兹海峡危机](#item-2) ⭐️ 9.0/10
3. [巴林与美国就霍尔木兹海峡提出安理会决议](#item-3) ⭐️ 9.0/10
4. [欧洲央行 Cipollone 就新能源冲击风险发出警告](#item-4) ⭐️ 9.0/10
5. [联合国警告黎巴嫩人道危机恶化，加沙暴力持续](#item-5) ⭐️ 7.0/10
6. [联合国：以色列再次空袭贝鲁特南郊，引发新一轮流离失所](#item-6) ⭐️ 7.0/10
7. [欧洲央行拉加德谈稳定币与货币主权](#item-7) ⭐️ 7.0/10
8. [欧洲央行施纳贝尔警告央行独立性正遭悄然侵蚀](#item-8) ⭐️ 7.0/10
9. [欧央行副行长德金多斯接受《金融时报》采访](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 13, 08:49

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
| US Mega Cap Basket | US | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | high |
| Japan Equity Basket | JP | bullish 38/31/31 | bullish 38/31/31 | bullish 42/29/30 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=29437.25; 1d=+0.92%; 5d=+2.51%; 20d=+11.65% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=707.24; 1d=-0.85%; 5d=+3.76%; 20d=+12.51% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29064.80; 1d=-0.87%; 5d=+3.75%; 20d=+12.47% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=0.8%; implied_move=0.0%; put/call OI=N/A | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=65.5; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.46; 2Y=4.0; 10Y-2Y=0.45999999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| NQ=F price trend | close=29437.25; 1d=+0.92%; 5d=+2.51%; 20d=+11.65% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=707.24; 1d=-0.85%; 5d=+3.76%; 20d=+12.51% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29064.80; 1d=-0.87%; 5d=+3.75%; 20d=+12.47% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| AMZN price trend | close=265.82; 1d=-1.18%; 5d=-2.83%; 20d=+6.75% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=407.77; 1d=-1.18%; 5d=-0.88%; 20d=+3.73% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=433.45; 1d=-2.60%; 5d=+11.32%; 20d=+19.01% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=294.80; 1d=+0.72%; 5d=+3.83%; 20d=+14.00% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=603.00; 1d=+0.69%; 5d=-0.32%; 20d=-8.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=387.35; 1d=-0.33%; 5d=-0.28%; 20d=+16.35% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| META options surface | ATM IV=0.2%; implied_move=0.0%; put/call OI=N/A | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=0.2%; implied_move=0.0%; put/call OI=N/A | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=0.2%; implied_move=0.0%; put/call OI=N/A | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=0.8%; implied_move=0.0%; put/call OI=N/A | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=0.8%; implied_move=0.0%; put/call OI=N/A | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=0.2%; implied_move=0.0%; put/call OI=N/A | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| AAPL insider filings | recent Form4 count=586 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| NVDA insider filings | recent Form4 count=567 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.46; 2Y=4.0; 10Y-2Y=0.45999999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| AMZN price trend | close=265.82; 1d=-1.18%; 5d=-2.83%; 20d=+6.75% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=407.77; 1d=-1.18%; 5d=-0.88%; 20d=+3.73% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=433.45; 1d=-2.60%; 5d=+11.32%; 20d=+19.01% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 6861.T price trend | close=79440.00; 1d=+0.23%; 5d=+3.90%; 20d=+28.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2939.50; 1d=+3.39%; 5d=-2.02%; 20d=-11.75% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3660.00; 1d=+5.05%; 5d=+17.05%; 20d=+8.44% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.06; 1d=-0.22%; 5d=+3.14%; 20d=+2.96% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6012.00; 1d=+0.42%; 5d=+10.84%; 20d=+59.26% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=51340.00; 1d=-1.57%; 5d=+8.20%; 20d=+21.69% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.46; 2Y=4.0; 10Y-2Y=0.45999999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=65.5; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
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
| 6861.T price trend | close=79440.00; 1d=+0.23%; 5d=+3.90%; 20d=+28.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2939.50; 1d=+3.39%; 5d=-2.02%; 20d=-11.75% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3660.00; 1d=+5.05%; 5d=+17.05%; 20d=+8.44% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9618.HK price trend | close=128.20; 1d=+8.28%; 5d=+10.14%; 20d=+11.09% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=37.33; 1d=-0.37%; 5d=+2.30%; 20d=+1.19% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=87.60; 1d=+4.10%; 5d=+6.18%; 20d=+2.94% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=132.80; 1d=-0.38%; 5d=-1.04%; 20d=+6.67% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=31.80; 1d=+1.08%; 5d=+3.18%; 20d=+2.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=24.18; 1d=-0.58%; 5d=+1.98%; 20d=+1.30% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=65.5; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.46; 2Y=4.0; 10Y-2Y=0.45999999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 9618.HK price trend | close=128.20; 1d=+8.28%; 5d=+10.14%; 20d=+11.09% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=37.33; 1d=-0.37%; 5d=+2.30%; 20d=+1.19% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=87.60; 1d=+4.10%; 5d=+6.18%; 20d=+2.94% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

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

- [NDAQ Implied Volatility Chart Nasdaq - MarketChameleon.com](https://marketchameleon.com/Overview/NDAQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：View volatility charts for Nasdaq (NDAQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the interactive...

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Volatility Term Structure chart plots the at-the-money implied volatility across expirations, which are an invaluable tool in determining options strategies based on anticipated...

- [Nasdaq-100 Volatility Index (VOLQ)](https://www.nasdaq.com/market-activity/index/volq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Find the latest information on Nasdaq-100 Volatility Index (VOLQ), including data, charts, related news, and more from Nasdaq.com

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

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [QQQ Volatility Term Structure for Nasdaq QQQ Invesco ETF - Barchart.com](https://www.barchart.com/stocks/quotes/QQQ/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Help Volatility Term Structure charts plot the at-the-money implied volatility across expirations, which are an invaluable tool in determining options strategies based on antici...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [US High Yield Master II Option-Adjusted Spread (Market Dail…](https://ycharts.com/indicators/us_high_yield_master_ii_optionadjusted_spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：View market daily updates and historical trends for US High Yield Master II Option-Adjusted Spread. from United States. Source: Bank of America Merrill Ly…

- [iShares MSCI Japan ETF (EWJ) - Yahoo Finance](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [EWJ / iShares MSCI Japan ETF Overview / MarketWatch](https://www.marketwatch.com/investing/fund/ewj)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ / A complete iShares MSCI Japan ETF exchange traded fund overview by MarketWatch. View the latest ETF prices and news for better ETF investing.

- [iShares MSCI Japan ETF / EWJ](https://www.ishares.com/us/products/239665/ishares-msci-japan-etf)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：The iShares MSCI Japan ETF seeks to track the investment results of an index composed of Japanese equities.

- [Nikkei Average Volatility (^NKVI.OS) - Yahoo Finance](https://finance.yahoo.com/quote/%5ENKVI.OS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Find the latest information on Nikkei Average Volatility (^NKVI.OS) including data, charts, related news and more from Yahoo Finance

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

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
## [联合国秘书长呼吁紧急缓解霍尔木兹海峡危机](https://news.un.org/feed/view/en/story/2026/05/1167478) ⭐️ 9.0/10

联合国秘书长安东尼奥·古特雷斯在周一油价上涨后紧急呼吁为霍尔木兹海峡紧张局势降温，并警告全球特别是非洲将遭受广泛经济冲击。 霍尔木兹海峡是全球关键的能源咽喉，承载 20%的液化天然气和 25%的海运石油贸易；任何中断都可能引发供应短缺和油价飙升，动摇脆弱经济体和全球金融市场。 周一早盘油价上涨，但未公布具体数字。警告强调了该海峡是多个海湾国家唯一的海上通道，任何关闭都可能对非洲和亚洲造成不成比例的伤害。

rss · UN News · May 11, 12:00

**背景**: 霍尔木兹海峡位于伊朗与阿曼之间，是连接波斯湾与公海的狭窄水道。2023 至 2025 年间，每日约 2000 万桶石油通过该海峡。2026 年伊朗战争使其成为冲突焦点，存在布雷或军事对抗的高度风险。安东尼奥·古特雷斯自 2017 年起担任联合国秘书长，多次参与危机降级外交。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://www.bbc.com/news/articles/c78n6p09pzno">Iran war: What is the Strait of Hormuz and why does it matter?</a></li>
<li><a href="https://en.wikipedia.org/wiki/António_Guterres">António Guterres - Wikipedia</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`, `#global-markets`

---

<a id="item-3"></a>
## [巴林与美国就霍尔木兹海峡提出安理会决议](https://news.un.org/feed/view/en/story/2026/05/1167464) ⭐️ 9.0/10

巴林和美国在周四的联合国总部介绍了一项安理会决议草案，要求伊朗停止在霍尔木兹海峡的袭击。 该决议直指伊朗在关键石油咽喉要道的行动，加剧外交升级风险，并可能扰乱经该海峡日均 2000 万桶的原油运输，导致全球油价飙升和市场动荡。 该决议草案很可能遭到俄罗斯和中国的否决，两国作为安理会常任理事国与伊朗关系密切，因此可能最终只能通过一份不具约束力的主席声明。

rss · UN News · May 7, 12:00

**背景**: 霍尔木兹海峡是阿曼与伊朗之间的狭窄海上通道，每日约有 2000 万桶石油通过。联合国安理会由 15 个成员国组成，其中美、英、法、俄、中五个常任理事国拥有否决权。巴林境内设有美国海军第五舰队，其外交政策常与美国保持一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council">United Nations Security Council - Wikipedia</a></li>
<li><a href="https://www.presstv.ir/Detail/2026/05/08/768239/Iran-rejects-US-Bahrain-one-sided-draft-resolution-on-Strait-of-Hormuz">Iran warns UN about dangerous US - Bahraini resolution on Strait of...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#military-risk`, `#middle-east`

---

<a id="item-4"></a>
## [欧洲央行 Cipollone 就新能源冲击风险发出警告](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260506~1bbd4ed780.en.html) ⭐️ 9.0/10

欧洲央行执行委员会成员 Piero Cipollone 发表了题为《新能源冲击：经济情景与政策影响》的演讲，评估了能源价格飙升和供应中断可能带来的影响。 这一高层沟通表明欧洲央行正密切关注能源驱动的增长和通胀风险，这或将影响未来的利率决策和市场预期。 该演讲发表之际，地缘政治紧张局势加剧，包括霍尔木兹海峡的中断，推高了全球油价，引发了对更广泛经济冲击的担忧。

rss · ECB Press Releases · May 6, 08:20

**背景**: Piero Cipollone 于 2023 年 11 月加入欧洲央行执行委员会，此前担任意大利央行副行长。欧洲央行负责维护欧元区的价格稳定。'新能源冲击'指的是近期因地缘冲突而加剧的全球能源危机，导致石油供应中断和价格大幅波动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Piero_Cipollone">Piero Cipollone</a></li>
<li><a href="https://www.weforum.org/stories/2026/05/world-facing-biggest-ever-energy-crisis-and-more-top-energy-stories/">World facing 'biggest' energy crisis – and more energy stories</a></li>
<li><a href="https://www.ecb.europa.eu/">European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#energy`, `#commodities`, `#global-markets`

---

<a id="item-5"></a>
## [联合国警告黎巴嫩人道危机恶化，加沙暴力持续](https://news.un.org/feed/view/en/story/2026/05/1167483) ⭐️ 7.0/10

联合国报告称，尽管上个月与以色列宣布停火，黎巴嫩的人道主义局势仍在恶化，同时加沙的暴力持续不断。 这表明停火脆弱且冲突再升级风险高，威胁地区稳定，使中东的国际外交努力复杂化。 联合国声明强调，尽管停火，黎巴嫩当地状况并未改善，加沙的敌对行动仍在继续。

rss · UN News · May 11, 12:00

**背景**: 黎巴嫩与以色列有冲突历史，近期真主党参与导致局势升级。上个月达成停火，但人道状况依然严峻。同时，自 2023 年 10 月以来以色列与哈马斯在加沙的冲突持续，造成大量平民伤亡和破坏。

**标签**: `#middle-east`, `#diplomacy`, `#geopolitics`, `#military-risk`

---

<a id="item-6"></a>
## [联合国：以色列再次空袭贝鲁特南郊，引发新一轮流离失所](https://news.un.org/feed/view/en/story/2026/05/1167460) ⭐️ 7.0/10

联合国表示，以色列对贝鲁特南郊的夜间空袭导致新的平民流离失所，并称这是“非常令人担忧的事态发展”。 此次针对首都郊区的打击标志着以色列-黎巴嫩冲突的危险升级，可能破坏脆弱的停火努力，并有可能将更广泛的地区大国卷入其中。 据联合国官员称，袭击在夜间发生，打击了南郊地区，使已因数月敌对行动而流离失所的平民处境更加艰难。

rss · UN News · May 7, 12:00

**背景**: 贝鲁特南郊（达希耶区）是黎巴嫩真主党的据点。自 2023 年 10 月以来，受加沙战争影响，以色列与真主党之间的跨境冲突不断升级。尽管各方进行外交努力，但持久停火仍遥遥无期，此前的局势升级已造成大量平民伤亡和流离失所。

**标签**: `#middle-east`, `#military-risk`, `#geopolitics`, `#diplomacy`

---

<a id="item-7"></a>
## [欧洲央行拉加德谈稳定币与货币主权](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260508~dd909fbed1.en.html) ⭐️ 7.0/10

欧洲央行行长拉加德就稳定币发表演讲，可能阐述了监管观点及其对金融稳定和货币主权的影响。 该演讲预示着欧洲央行对稳定币的监管立场，可能影响欧盟政策并冲击加密市场、金融科技创新及数字欧元的发展，同时凸显央行维护货币主权的决心。 由于未获取演讲全文，具体政策建议尚不明确，但拉加德可能强调了加强监管以防范系统性风险，以及稳定币监管国际合作的必要性。

rss · ECB Press Releases · May 8, 07:00

**背景**: 稳定币是通过与法币等资产挂钩来保持价值稳定的加密货币。其快速发展引发了对消费者保护、金融稳定和货币主权（国家对货币及货币政策的排他性控制）的担忧。欧洲央行一直在推进数字欧元，作为私人数字货币的公共替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stablecoin">Stablecoin</a></li>
<li><a href="https://en.wikipedia.org/wiki/Monetary_sovereignty">Monetary sovereignty</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#europe`, `#global-markets`, `#currency`

---

<a id="item-8"></a>
## [欧洲央行施纳贝尔警告央行独立性正遭悄然侵蚀](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260507_1~d5ae988ece.en.html) ⭐️ 7.0/10

欧洲央行执委伊莎贝尔·施纳贝尔发表演讲，指出央行独立性正遭受“悄然侵蚀”，并警告结构性力量正在削弱政策可信度，可能影响市场对欧元区稳定性的看法。 央行独立性遭侵蚀会威胁通胀预期的锚定和债券市场稳定，可能外溢至主权风险溢价和欧元区的凝聚力。 演讲指出，除了明显的政治压力，结构性变化（包括财政主导和机构边界模糊）正悄然侵蚀独立货币政策有效运行的条件。

rss · ECB Press Releases · May 7, 17:00

**背景**: 央行独立性指货币当局不受政治影响的自主性，是现代货币政策的基石，被认为在大缓和时期降低了通胀和波动性。欧洲央行负有维持价格稳定的使命，其设计旨在保持独立。在高公共债务或政府寻求更宽松政策时，对独立性的质疑常常出现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Central_bank_independence">Central bank independence</a></li>
<li><a href="https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp260507_annex~dbb6d582b4.en.pdf">The quiet erosion of central bank independence</a></li>
<li><a href="https://mostlyeconomics.wordpress.com/2026/05/08/the-quiet-erosion-of-central-bank-independence/">The quiet erosion of central bank independence | Mostly Economics</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#financial-stability`, `#sovereign-risk`, `#europe`

---

<a id="item-9"></a>
## [欧央行副行长德金多斯接受《金融时报》采访](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260511~3fa2df2fa9.en.html) ⭐️ 6.0/10

欧洲央行副行长路易斯·德金多斯于 2026 年 5 月 11 日接受《金融时报》采访，讨论了欧元区经济状况和货币政策。谈话可能涉及增长、通胀和金融稳定问题。 作为欧央行重要官员，德金多斯的言论可能预示央行政策走向，影响市场对利率和资产购买的预期。任何语气上的变化都可能影响欧元区债券收益率和欧元汇率。 采访形式通常比官方声明能传达更细微的信息，但并未报道具体的政策声明或前瞻性指引变化。完整记录可在欧央行网站查阅。

rss · ECB Press Releases · May 11, 04:00

**背景**: 路易斯·德金多斯自 2018 年起担任欧央行副行长，此前曾任西班牙财政部长。欧央行利用媒体采访补充正式政策沟通，为其决策和经济评估提供背景。近年来欧元区面临增长乏力和通胀高于目标，使得欧央行沟通备受投资者关注。

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`, `#financial-stability`

---