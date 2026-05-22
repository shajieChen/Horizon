---
layout: default
title: "Horizon Summary: 2026-05-23 (ZH)"
date: 2026-05-23
lang: zh
---

> From 40 items, 12 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [无人机袭击阿联酋核电站附近，安理会召开紧急会议](#item-2) ⭐️ 9.0/10
3. [凯文·沃什宣誓就任美联储主席及 FOMC 主席](#item-3) ⭐️ 9.0/10
4. [古特雷斯：重启霍尔木兹海峡与安理会改革](#item-4) ⭐️ 8.0/10
5. [霍尔木兹危机持续扰乱全球贸易与生活成本](#item-5) ⭐️ 8.0/10
6. [联合国特使警告：加沙过渡计划若停滞恐陷永久僵局](#item-6) ⭐️ 7.0/10
7. [联合国大会支持国际法院气候裁决](#item-7) ⭐️ 7.0/10
8. [古特雷斯谴责以色列在东耶路撒冷将扣押的 UNRWA 设施军事化](#item-8) ⭐️ 7.0/10
9. [联合国安理会就卢甘斯克争议袭击召开会议](#item-9) ⭐️ 6.0/10
10. [联合国警告加沙医疗封锁与疾病蔓延](#item-10) ⭐️ 6.0/10
11. [安理会辩论加沙未来与西岸恶化局势](#item-11) ⭐️ 6.0/10
12. [联合国安理会警告乌克兰战争日益致命](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 22, 22:51

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
| NQ=F price trend | close=29520.75; 1d=+0.25%; 5d=+0.99%; 20d=+7.60% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29481.64; 1d=+0.42%; 5d=+1.22%; 20d=+7.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=717.54; 1d=+0.42%; 5d=+1.21%; 20d=+8.08% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=4.7%; implied_move=0.1%; put/call OI=2.3547849407992567 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| NQ=F price trend | close=29520.75; 1d=+0.25%; 5d=+0.99%; 20d=+7.60% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29481.64; 1d=+0.42%; 5d=+1.22%; 20d=+7.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=717.54; 1d=+0.42%; 5d=+1.21%; 20d=+8.08% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| GOOGL price trend | close=382.97; 1d=-1.21%; 5d=-3.48%; 20d=+11.20% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=610.26; 1d=+0.47%; 5d=-0.65%; 20d=-9.60% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=308.82; 1d=+1.26%; 5d=+2.86%; 20d=+14.04% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=266.32; 1d=-0.80%; 5d=+0.83%; 20d=+0.88% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=215.33; 1d=-1.90%; 5d=-4.43%; 20d=+3.39% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=426.01; 1d=+1.95%; 5d=+0.89%; 20d=+13.21% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| AMZN options surface | ATM IV=7.7%; implied_move=0.4%; put/call OI=0.5594700285173787 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=6.1%; implied_move=0.3%; put/call OI=0.37649137814596373 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=3.0%; implied_move=0.1%; put/call OI=0.4269670641767571 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=4.2%; implied_move=0.2%; put/call OI=0.5591338568648683 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=7.5%; implied_move=0.3%; put/call OI=0.7595612002347161 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=7.7%; implied_move=0.3%; put/call OI=0.6343084436836011 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| AAPL insider filings | recent Form4 count=586 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| NVDA insider filings | recent Form4 count=562 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| GOOGL price trend | close=382.97; 1d=-1.21%; 5d=-3.48%; 20d=+11.20% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=610.26; 1d=+0.47%; 5d=-0.65%; 20d=-9.60% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=308.82; 1d=+1.26%; 5d=+2.86%; 20d=+14.04% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| EWJ price trend | close=91.61; 1d=+0.26%; 5d=+0.59%; 20d=+4.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=79370.00; 1d=+3.13%; 5d=+2.84%; 20d=+23.96% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3525.00; 1d=-0.82%; 5d=-1.43%; 20d=+4.17% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=49830.00; 1d=+2.11%; 5d=-0.91%; 20d=+12.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2987.00; 1d=+0.30%; 5d=-3.18%; 20d=-11.89% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6757.00; 1d=+11.89%; 5d=+17.62%; 20d=+41.54% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
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
| EWJ price trend | close=91.61; 1d=+0.26%; 5d=+0.59%; 20d=+4.91% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=79370.00; 1d=+3.13%; 5d=+2.84%; 20d=+23.96% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3525.00; 1d=-0.82%; 5d=-1.43%; 20d=+4.17% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 1810.HK price trend | close=30.00; 1d=+1.15%; 5d=-2.28%; 20d=-3.78% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.91; 1d=-2.61%; 5d=-4.47%; 20d=-6.66% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=81.35; 1d=-0.91%; 5d=-1.63%; 20d=-2.11% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=127.00; 1d=+0.79%; 5d=-4.01%; 20d=-2.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=441.40; 1d=+0.55%; 5d=-3.29%; 20d=-9.83% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=35.52; 1d=-1.03%; 5d=-1.88%; 20d=-3.64% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| 1810.HK price trend | close=30.00; 1d=+1.15%; 5d=-2.28%; 20d=-3.78% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.91; 1d=-2.61%; 5d=-4.47%; 20d=-6.66% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=81.35; 1d=-0.91%; 5d=-1.63%; 20d=-2.11% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [MOVE Index Charts and Quotes — TradingView](https://www.tradingview.com/symbols/TVC-MOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：MOVE INDEX Setup for Top in World stock markets The chart is the Move index it is reaching an area which I consider High level of Complacency I say this as of this writing The 1...

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days or more out. IV is a forward looking prediction of the likelihood...

- [Nasdaq 100 (NDX) - Implied Volatility (Mean) (30-Day)](https://www.alphaquery.com/stock/NDX/volatility-option-statistics/30-day/iv-mean)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility (Mean): The forecasted future volatility of the security over the selected time frame, derived from the average of the put and call implied volatilities for o...

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [CBOE Volatility Index: VIX (VIXCLS) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/VIXCLS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Graph and download economic data for CBOE Volatility Index: VIX (VIXCLS) from 1990-01-02 to 2026-05-21 about VIX, volatility, stock market, and USA.

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [US High Yield Master II Option-Adjusted Spread (Market Dail…](https://ycharts.com/indicators/us_high_yield_master_ii_optionadjusted_spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：View market daily updates and historical trends for US High Yield Master II Option-Adjusted Spread. from United States. Source: Bank of America Merrill Ly…

- [BofA US High Yield Index Option-Adjusted Spread - GuruFocus](https://www.gurufocus.com/economic_indicators/5735/bofa-us-high-yield-index-optionadjusted-spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：BofA US High Yield Index Option-Adjusted Spread as of report date (2026-04-16) is 2.86. BofA US High Yield Index Option-Adjusted Spread charts, data and related items.

- [QQQ Options - Live IV, Flow, Greeks & Analysis / ImpliedOptions ...](https://impliedoptions.com/ticker/qqq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Trade QQQ options with real-time implied volatility, IV rank, options flow, and Greeks. Analyze QQQ calls and puts with our free calculator and strategy builder.

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

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

- [USD/JPY (USDJPY=X) Live Rate, Chart & News - Yahoo Finance](https://finance.yahoo.com/quote/USDJPY=X/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Find the latest USD/JPY (USDJPY=X) currency exchange rate, plus historical data, charts, relevant news and more

- [Valuta EX - Currency Converter / Real-Time Exchange Rates](https://valuta.exchange/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

- [USD JPY Exchange Rate, Live USD to JPY Forex Rate at Forex Rates](https://www.forexrates.net/fx-rates/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：USD JPY Exchange Rate This is the live USD JPY rate forex data page, displaying the FX price for the USD/JPY. The FX rate self-updates every few seconds. Compare exchange rates...

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
## [无人机袭击阿联酋核电站附近，安理会召开紧急会议](https://news.un.org/feed/view/en/story/2026/05/1167550) ⭐️ 9.0/10

阿联酋巴拉卡核电站附近发生无人机袭击，促使联合国安理会召开紧急会议，国际原子能机构总干事格罗西向成员国通报了核安全与安保关切。 该事件在局势动荡的中东地区引发严重核安全风险，可能升级为更广泛冲突；鉴于阿联酋是重要石油生产国且该核电站承担大量电力供应，能源市场可能受到冲击。 巴拉卡核电站是阿拉伯世界首座核电站，拥有四座 APR-1400 反应堆，年发电量约 40 太瓦时，满足阿联酋近 25%的电力需求。国际原子能机构正主导安全评估，但袭击者身份及损害程度尚未公布。

rss · UN News · May 19, 12:00

**背景**: 巴拉卡核电站自 2020 年运营，是阿联酋能源多元化战略的核心。国际原子能机构是联合国下属机构，负责推动和平利用核能并制定全球安全标准。此前安理会曾就中东紧张局势召开紧急会议，例如 2026 年 2 月美以打击伊朗后，凸显地区脆弱性和安理会的危机管理角色。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Barakah_nuclear_power_plant">Barakah nuclear power plant - Wikipedia</a></li>
<li><a href="https://www.iaea.org/topics/nuclear-safety-and-security">Nuclear safety and security | IAEA</a></li>
<li><a href="https://news.un.org/en/story/2026/02/1167060">MIDDLE EAST LIVE: UN Security Council meeting in emergency session over Iran | UN News</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`

---

<a id="item-3"></a>
## [凯文·沃什宣誓就任美联储主席及 FOMC 主席](https://www.federalreserve.gov/newsevents/pressreleases/other20260522a.htm) ⭐️ 9.0/10

凯文·沃什已正式宣誓就任联邦储备系统理事会主席和成员，联邦公开市场委员会一致选举他为主席，标志着美国央行的领导层更迭。 作为美联储主席，沃什将引导美国货币政策，影响利率、通胀和金融监管，对全球市场、资产价格和国际资本流动产生重大影响。 沃什的任命是在 2026 年 5 月 13 日参议院确认之后；他的政策立场以及与前任杰罗姆·鲍威尔相比的任何转变都将受到投资者和政策制定者的密切关注。

rss · Federal Reserve Press Releases · May 22, 20:15

**背景**: 美联储是美国的中央银行，承担着最大就业和物价稳定的双重使命。理事会负责监督整个系统，联邦公开市场委员会通过联邦基金利率制定货币政策。主席由总统任命并经参议院确认，对经济政策具有重大影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Reserve_System">Federal Reserve System</a></li>
<li><a href="https://en.wikipedia.org/wiki/Board_of_Governors_of_the_Federal_Reserve_System">Board of Governors of the Federal Reserve System</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federal_Open_Market_Committee">Federal Open Market Committee</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#united-states`, `#global-markets`, `#macroeconomics`, `#financial-stability`

---

<a id="item-4"></a>
## [古特雷斯：重启霍尔木兹海峡与安理会改革](https://news.un.org/feed/view/en/story/2026/05/1167555) ⭐️ 8.0/10

联合国秘书长安东尼奥·古特雷斯周三呼吁有效重新开放霍尔木兹海峡，并扩大联合国安理会成员数量，以遏制拥有否决权的超级大国的行为。 他将这两个问题联系起来，表明围绕这一关键石油咽喉要道的地缘政治紧张局势和潜在军事风险不断加剧，对全球能源市场和多边外交的可信度产生重大影响。 霍尔木兹海峡承载着全球 20%的液化天然气和 25%的海运石油贸易；安理会任何改革均需五个拥有否决权的常任理事国全部同意，使得实质性变革极为困难。

rss · UN News · May 20, 12:00

**背景**: 霍尔木兹海峡连接波斯湾与阿曼湾，是全球最重要的石油和天然气运输通道之一。联合国安理会五个常任理事国——中国、法国、俄罗斯、英国和美国——均拥有否决权，批评者认为这导致安理会在重大冲突中陷入瘫痪。古特雷斯的声明正值报道所称“霍尔木兹海峡危机”期间，该危机发生于 2026 年伊朗战争，可能意味着海峡被有效封锁。安理会改革的呼吁已持续数十年，但需要五个拥有否决权的常任理事国一致同意，使得改革难以实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council_reform">UN Security Council reform</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council_Veto_power">UN Security Council Veto power</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`

---

<a id="item-5"></a>
## [霍尔木兹危机持续扰乱全球贸易与生活成本](https://news.un.org/feed/view/en/story/2026/05/1167548) ⭐️ 8.0/10

尽管美伊达成脆弱停火协议，霍尔木兹海峡周边持续不稳定仍在扰乱全球航运、推高能源成本并加剧生活成本危机。 作为关键石油咽喉要道，海峡持续受阻威胁全球能源安全，推高通胀，对发展中经济体打击最重，并可能加剧地缘政治紧张。 霍尔木兹海峡每日运输约 2000 万桶石油，其中 82%的原油运往亚洲市场；停火协议因双方相互指责违反协议而依旧脆弱。

rss · UN News · May 19, 12:00

**背景**: 霍尔木兹海峡是全球最关键的石油运输咽喉，连接波斯湾产油国与全球市场。2026 年初，美伊军事冲突导致海峡部分关闭和航运袭击。2026 年 4 月巴基斯坦斡旋达成停火，但紧张持续，海峡仍是地缘政治热点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eia.gov/todayinenergy/detail.php?id=61002">The Strait of Hormuz is the world's most important oil transit ...</a></li>
<li><a href="https://www.worldbank.org/en/news/press-release/2026/04/28/commodity-markets-outlook-april-2026-press-release">Middle East War to Spark Biggest Energy Price Surge in Four Years</a></li>
<li><a href="https://www.nytimes.com/2026/04/10/world/middleeast/strait-hormuz-iran-ships-oil.html">With Iran Setting Limits, Strait of Hormuz Remains Thorny Politically</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#energy`, `#supply-chain`, `#middle-east`, `#commodities`

---

<a id="item-6"></a>
## [联合国特使警告：加沙过渡计划若停滞恐陷永久僵局](https://news.un.org/feed/view/en/story/2026/05/1167568) ⭐️ 7.0/10

一位联合国高级特使周四向安理会表示，加沙地带停火脆弱、人道状况恶化，安理会支持的过渡计划执行延误将使该地面临陷入“永久”僵局的风险。 该警告表明，执行停滞可能引发冲突再起，加剧人道灾难和地区动荡，进而损害联合国公信力和脆弱的和平进程。 第 2803 号决议（2025 年）规定的过渡计划设立了和平委员会、巴勒斯坦全国行政委员会及国际稳定部队。执行延误正加剧原本脆弱的停火和不断恶化的人道状况。

rss · UN News · May 21, 12:00

**背景**: 联合国安理会于 2025 年 11 月 17 日通过第 2803 号决议，旨在为加沙战争后的加沙地带安排过渡治理。该决议借鉴了此前的联合国过渡行政当局模式，授权设立国际机构协助管理并部署国际稳定部队。该计划是美国牵头达成的以色列与哈马斯多边和平协议的一部分，巴勒斯坦权力机构对此表示欢迎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167568">Gaza risks ‘permanent’ state of limbo if transition plan ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gaza_Transitional_Authority">Gaza Transitional Authority</a></li>
<li><a href="https://betterworldcampaign.org/peace-and-security/the-un-security-council-just-backed-the-u-s-plan-for-gaza-what-it-means-and-what-comes-next">The UN Security Council Just Backed the U.S. Plan for Gaza ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-7"></a>
## [联合国大会支持国际法院气候裁决](https://news.un.org/feed/view/en/story/2026/05/1167561) ⭐️ 7.0/10

联合国大会通过一项决议，支持国际法院关于气候变化的咨询意见，该意见宣布各国有防止对气候造成重大损害的法律义务。 这一支持加强了气候行动的国际法律框架，可能加大对各国的外交压力，要求其履行气候承诺，并为未来的气候诉讼开辟途径。 该决议于周三（很可能在 2026 年 5 月）通过，联合国秘书长安东尼奥·古特雷斯称其是对国际法、气候正义和科学的有力肯定。

rss · UN News · May 20, 12:00

**背景**: 国际法院是联合国的主要司法机关，可应大会等联合国机构的请求就法律问题发表咨询意见。在这一历史性意见中，国际法院阐明，根据国际法，各国必须防止对气候系统造成重大损害，这一义务与人权和气候正义原则相关。气候正义关注气候变化对弱势群体造成的过重负担。大会的决议虽不具约束力，但为国际法院的结论增添了政治分量和道德权威。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iisd.org/articles/deep-dive/icj-advisory-opinion-climate-change">Historic International Court of Justice Opinion Confirms States...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Climate_justice">Climate justice - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#international-law`

---

<a id="item-8"></a>
## [古特雷斯谴责以色列在东耶路撒冷将扣押的 UNRWA 设施军事化](https://news.un.org/feed/view/en/story/2026/05/1167560) ⭐️ 7.0/10

周三，联合国秘书长古特雷斯强烈谴责以色列在被占领的东耶路撒冷一个被扣押的联合国近东救济工程处（UNRWA）设施内建立军事设施的决定，称其“完全不可接受”。 这一谴责加剧了以色列与联合国之间的外交紧张，可能引发安理会审议或进一步联合国措施，并凸显了对联合国房舍不可侵犯性及国际法的违反，可能对以巴关系和更广泛的中东稳定产生连锁影响。 该设施位于东耶路撒冷的谢赫贾拉，古特雷斯强调它仍是联合国房舍，并敦促以色列立即撤销决定并将设施归还给联合国。

rss · UN News · May 20, 12:00

**背景**: 联合国近东救济工程处（UNRWA）向巴勒斯坦难民提供基本服务。根据包括联合国和国际法院在内的国际法，东耶路撒冷被视为被占领的巴勒斯坦领土。该 UNRWA 设施此前已被以色列扣押，此次军事化标志着围绕联合国房舍的争端升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167560">Guterres condemns Israeli move to militarise seized compound in...</a></li>
<li><a href="https://en.wikipedia.org/wiki/UNRWA">UNRWA - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Status_of_Jerusalem">Status of Jerusalem - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-9"></a>
## [联合国安理会就卢甘斯克争议袭击召开会议](https://news.un.org/feed/view/en/story/2026/05/1167578) ⭐️ 6.0/10

俄罗斯请求召开联合国安理会紧急会议，指责乌克兰袭击了卢甘斯克占领区一栋平民学生宿舍，据报造成 6 人死亡（含儿童）。基辅方面否认针对民用建筑，称其打击的是俄军无人机指挥总部。 这起事件凸显了冲突中信息战的升级及核实平民伤害的难度，可能影响未来西方军事援助决策和联合国人道主义响应。尽管因俄罗斯的否决权，安理会会议难以产生实质性行动，但它将影响全球关于遵守国际人道主义法的外交叙事。 俄罗斯声称袭击造成 6 人死亡（含儿童）及数十人受伤；乌克兰指认目标为‘鲁比康’无人机部队总部。目前无独立核实，且会议紧随莫斯科近期宣布完全控制卢甘斯克之后举行。

rss · UN News · May 22, 12:00

**背景**: 联合国安理会是负责维护国际和平与安全的机构，俄罗斯是拥有否决权的常任理事国。乌克兰东部的卢甘斯克地区自 2022 年以来大部被俄军占领，莫斯科多次声称乌方袭击平民设施，但基辅及西方盟国常提出异议。由于俄罗斯的否决权，安理会在乌克兰问题上基本陷入僵局，难以采取实质性行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.straitstimes.com/world/europe/russia-says-four-killed-35-children-wounded-in-ukrainian-attack-on-luhansk-region">Putin accuses Ukraine of deadly attack on student dorm, Kyiv ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council">United Nations Security Council - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Russian-occupied_territories_of_Ukraine">Russian-occupied territories of Ukraine - Wikipedia</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#diplomacy`, `#geopolitics`, `#military-risk`

---

<a id="item-10"></a>
## [联合国警告加沙医疗封锁与疾病蔓延](https://news.un.org/feed/view/en/story/2026/05/1167572) ⭐️ 6.0/10

联合国机构周五警告称，基本医疗物资的封锁正加剧加沙的恶劣状况，暴力持续，疾病在鼠患中蔓延。 不断恶化的人道主义危机可能加大停火或改善援助准入的外交压力，间接影响地区稳定和风险认知。 自 2007 年以来，封锁严格限制包括医疗和建筑物资在内的“双重用途”物品进口，使人道主义行动濒临崩溃。

rss · UN News · May 22, 12:00

**背景**: 加沙地带自 2007 年以来处于以色列和埃及的封锁下，人员和货物流动严重受限。联合国近东救济工程处等机构提供援助，但封锁形成了“露天监狱”，经济与卫生状况恶劣。持续冲突导致大量平民流离失所，基础设施被毁，23 个联合国机构难以满足人道需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaza_Strip_blockade">Gaza Strip blockade</a></li>
<li><a href="https://unsdg.un.org/latest/stories/how-un-helping-civilians-gaza">Unsdg | How the UN is helping civilians in Gaza</a></li>
<li><a href="https://www.unrwa.org/">UNRWA | United Nations Relief and Works Agency for Palestine Refugees</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#military-risk`, `#diplomacy`, `#humanitarian`

---

<a id="item-11"></a>
## [安理会辩论加沙未来与西岸恶化局势](https://news.un.org/feed/view/en/story/2026/05/1167563) ⭐️ 6.0/10

联合国安理会举行公开辩论，讨论加沙和平进程停滞及约旦河西岸局势恶化，重点是治理与解除武装问题，但外界普遍预计不会立即取得突破。 此次辩论凸显了加沙战后治理与解除武装方面的外交僵局，可能影响地区稳定和人道主义状况，但短期内对市场影响有限。 脆弱的停火虽已基本停止了战斗，但解除武装遥遥无期；西岸平民伤亡持续增加，人道需求上升；目前并无新的决议或制裁提案。

rss · UN News · May 21, 12:00

**背景**: 联合国安理会负责维护国际和平与安全，五个常任理事国（美、英、法、俄、中）拥有否决权。加沙停火协议一度停止了大部分战斗，但要求解除武装和过渡治理的后续阶段陷入僵局。约旦河西岸自 1967 年被以色列占领，暴力升级和定居点扩张加剧了巴以冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gaza_peace_plan">Gaza peace plan - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/West_Bank">West Bank</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-12"></a>
## [联合国安理会警告乌克兰战争日益致命](https://news.un.org/feed/view/en/story/2026/05/1167546) ⭐️ 6.0/10

一名联合国高级官员在安理会通报中指出，已进入第五年的乌克兰战争正日益致命。 这一警告突显了冲突进一步升级和人道主义危机恶化的风险，可能促使各方重新展开外交努力、制裁或维和行动。 通报于周二进行，但摘要中未透露官员姓名。该声明强调，尽管国际社会持续介入，暴力活动仍不断发生。

rss · UN News · May 19, 12:00

**背景**: 俄罗斯-乌克兰战争始于 2022 年 2 月，已导致数万人伤亡、大规模流离失所和严重破坏。联合国安理会负责维护国际和平，但因否决权而难以果断行动。这场冲突还扰乱了全球粮食和能源市场。

**标签**: `#diplomacy`, `#geopolitics`, `#russia-ukraine`, `#military-risk`, `#united-nations`

---