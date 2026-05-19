---
layout: default
title: "Horizon Summary: 2026-05-20 (ZH)"
date: 2026-05-20
lang: zh
---

> From 39 items, 8 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [阿联酋核电站遭无人机袭击，联合国安理会紧急会议](#item-2) ⭐️ 9.0/10
3. [霍尔木兹危机扰乱贸易，加剧生活成本危机](#item-3) ⭐️ 8.0/10
4. [欧洲央行首席经济学家分析能源供应冲击](#item-4) ⭐️ 8.0/10
5. [乌克兰战争“日益致命”，联合国安理会接获警告](#item-5) ⭐️ 7.0/10
6. [联合国警告核恐怖主义威胁达历史新高](#item-6) ⭐️ 7.0/10
7. [联合国警告地缘政治冲突加剧全球经济脆弱性](#item-7) ⭐️ 6.0/10
8. [停电与燃料短缺导致古巴医疗系统陷入危机](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 19, 23:04

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
| QDII Nasdaq 100 Proxy | US | neutral 33/33/34 | neutral 33/33/34 | bullish 40/32/28 | high |
| US Mega Cap Basket | US | neutral 33/33/34 | neutral 33/33/34 | bullish 40/32/28 | high |
| Japan Equity Basket | JP | neutral 33/33/34 | neutral 33/33/34 | bullish 40/32/28 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | neutral 34/34/31 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=28905.75; 1d=-0.65%; 5d=-0.91%; 20d=+8.53% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=701.53; 1d=-0.62%; 5d=-0.81%; 20d=+8.88% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=28818.84; 1d=-0.61%; 5d=-0.85%; 20d=+8.83% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=2.6%; implied_move=0.1%; put/call OI=1.7189177008654721 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=60.4; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.67; 2Y=4.13; 10Y-2Y=0.54 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：有效交易信号不足，使用保守基准分布。
- 1月：20日趋势维持上行，1月窗口偏多；长端美债收益率偏高，对成长风格估值形成压制；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1月 | 40% | 32% | 28% | bullish | 20日趋势维持上行，1月窗口偏多；长端美债收益率偏高，对成长风格估值形成压制；风险偏好仍可控且波动未失控，中期上行概率提高 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| NQ=F price trend | close=28905.75; 1d=-0.65%; 5d=-0.91%; 20d=+8.53% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=701.53; 1d=-0.62%; 5d=-0.81%; 20d=+8.88% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=28818.84; 1d=-0.61%; 5d=-0.85%; 20d=+8.83% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| GOOGL price trend | close=387.66; 1d=-2.34%; 5d=+0.08%; 20d=+16.66% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=298.97; 1d=+0.38%; 5d=+1.41%; 20d=+12.43% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=417.42; 1d=-1.44%; 5d=+2.37%; 20d=-1.59% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=220.61; 1d=-0.77%; 5d=-0.08%; 20d=+10.37% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=404.11; 1d=-1.43%; 5d=-6.77%; 20d=+4.58% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=602.61; 1d=-1.41%; 5d=-0.06%; 20d=-9.90% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| AMZN options surface | ATM IV=24.3%; implied_move=1.4%; put/call OI=0.6228129205921938 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=23.5%; implied_move=1.3%; put/call OI=0.7175497544585164 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=17.3%; implied_move=1.0%; put/call OI=0.3229755777255301 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=34.2%; implied_move=2.0%; put/call OI=0.5070939179930432 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=31.2%; implied_move=1.7%; put/call OI=0.6453726073220591 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=73.3%; implied_move=6.1%; put/call OI=0.5726356128740313 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| NVDA insider filings | recent Form4 count=562 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| CNN Fear & Greed | score=60.4; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| AAPL insider filings | recent Form4 count=586 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| MSFT insider filings | recent Form4 count=731 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.67; 2Y=4.13; 10Y-2Y=0.54 | 利率曲线决定权益估值贴现与风险偏好上限。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：有效交易信号不足，使用保守基准分布。
- 1月：20日趋势维持上行，1月窗口偏多；长端美债收益率偏高，对成长风格估值形成压制；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1月 | 40% | 32% | 28% | bullish | 20日趋势维持上行，1月窗口偏多；长端美债收益率偏高，对成长风格估值形成压制；风险偏好仍可控且波动未失控，中期上行概率提高 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| GOOGL price trend | close=387.66; 1d=-2.34%; 5d=+0.08%; 20d=+16.66% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=298.97; 1d=+0.38%; 5d=+1.41%; 20d=+12.43% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=417.42; 1d=-1.44%; 5d=+2.37%; 20d=-1.59% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 6758.T price trend | close=3720.00; 1d=+3.45%; 5d=+6.77%; 20d=+11.38% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=90.29; 1d=-0.69%; 5d=-1.92%; 20d=+3.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=5361.00; 1d=-4.15%; 5d=-10.46%; 20d=+20.63% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=75000.00; 1d=-2.38%; 5d=-5.37%; 20d=+19.52% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2957.00; 1d=+0.08%; 5d=+4.01%; 20d=-12.54% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=47160.00; 1d=-4.26%; 5d=-9.59%; 20d=+8.41% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=60.4; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.67; 2Y=4.13; 10Y-2Y=0.54 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 跨层分歧信息有限，后续需补充更多波动与事件市场数据。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：有效交易信号不足，使用保守基准分布。
- 1月：20日趋势维持上行，1月窗口偏多；长端美债收益率偏高，对成长风格估值形成压制；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1月 | 40% | 32% | 28% | bullish | 20日趋势维持上行，1月窗口偏多；长端美债收益率偏高，对成长风格估值形成压制；风险偏好仍可控且波动未失控，中期上行概率提高 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 6758.T price trend | close=3720.00; 1d=+3.45%; 5d=+6.77%; 20d=+11.38% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=90.29; 1d=-0.69%; 5d=-1.92%; 20d=+3.61% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=5361.00; 1d=-4.15%; 5d=-10.46%; 20d=+20.63% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 3690.HK price trend | close=83.05; 1d=+1.10%; 5d=-1.31%; 20d=-2.47% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=28.28; 1d=+0.78%; 5d=-2.98%; 20d=-3.84% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=23.65; 1d=-1.34%; 5d=-2.19%; 20d=+1.59% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=460.00; 1d=+2.40%; 5d=+1.78%; 20d=-10.94% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=125.90; 1d=-0.47%; 5d=+6.33%; 20d=+2.86% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=36.28; 1d=+0.33%; 5d=-2.81%; 20d=-2.24% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.67; 2Y=4.13; 10Y-2Y=0.54 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=60.4; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
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
- 1月：长端美债收益率偏高，对成长风格估值形成压制；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1月 | 34% | 34% | 31% | neutral | 长端美债收益率偏高，对成长风格估值形成压制；风险偏好仍可控且波动未失控，中期上行概率提高 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 3690.HK price trend | close=83.05; 1d=+1.10%; 5d=-1.31%; 20d=-2.47% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=28.28; 1d=+0.78%; 5d=-2.98%; 20d=-3.84% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=23.65; 1d=-1.34%; 5d=-2.19%; 20d=+1.59% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days out or more. IV is a forward looking prediction of the likelihood...

- [Option Implied Volatility Rankings Report](https://marketchameleon.com/volReports/VolatilityRankings)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：What can I find on the Implied Volatility Rankings Report? Market Chameleon's Implied Volatility Rankings Report shows a detailed set of data for stocks, comparing their current...

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

- [CBOE Volatility Index: VIX (VIXCLS) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/VIXCLS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Graph and download economic data for CBOE Volatility Index: VIX (VIXCLS) from 1990-01-02 to 2026-05-15 about VIX, volatility, stock market, and USA.

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

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
  - 摘要：United States - ICE BofA US High Yield Index Option-Adjusted Spread was 2.76% in May of 2026, according to the United States Federal Reserve. Historically, United States - ICE B...

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [QQQ Stock Volatility History & Chart Since 1999](https://wallstreetnumbers.com/etfs/qqq/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Get all-time historical data of QQQ historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Live US Dollar to Yens Exchange Rate - $ 1 USD/JPY Today](https://usd.currencyrate.today/jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest and best $1 US Dollar to Yens rate for FREE. USD/JPY - Live exchange rates, banks, historical data & currency charts.

- [USD/JPY (USDJPY=X) Live Rate, Chart & News - Yahoo Finance](https://finance.yahoo.com/quote/USDJPY=X/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Find the latest USD/JPY (USDJPY=X) currency exchange rate, plus historical data, charts, relevant news and more

- [1 USD to JPY - US Dollars to Japanese Yen Exchange Rate - Xe](https://www.xe.com/en/currencyconverter/convert/?Amount=1&From=USD&To=JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest 1 US Dollar to Japanese Yen rate for FREE with the original Universal Currency Converter. Set rate alerts for USD to JPY and learn more about US Dollars and Japan...

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [iShares MSCI Japan ETF (EWJ) Price, Holdings, & News](https://www.marketbeat.com/stocks/NYSEARCA/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Should You Buy or Sell iShares MSCI Japan ETF Stock? Get The Latest EWJ Stock Price, Constituents List, Holdings Data, and Headlines at MarketBeat.

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
## [阿联酋核电站遭无人机袭击，联合国安理会紧急会议](https://news.un.org/feed/view/en/story/2026/05/1167550) ⭐️ 9.0/10

联合国安理会就 2026 年 5 月 17 日阿联酋巴拉卡核电站附近遭无人机袭击一事召开紧急会议。国际原子能机构总干事拉斐尔·格罗西向成员国通报情况，并警告核安全与安保风险。 该事件增加了动荡地区发生核事故的风险，并可能扰乱全球能源市场，因为阿联酋是主要的石油和天然气生产国。如果袭击被归因于某个国家或非国家行为体，还可能加剧地区紧张局势升级的担忧。 无人机导致核电站周边起火，阿联酋国防部随后报告称无人机来自伊拉克境内。国际原子能机构的通报强调在冲突期间保障核设施安全的必要性。

rss · UN News · May 19, 12:00

**背景**: 巴拉卡核电站是阿拉伯世界首座商业核电站，由四座 APR-1400 反应堆组成。国际原子能机构是联合国的核监督机构，根据《核不扩散条约》负责监督核计划并促进安全。联合国安理会可召开紧急会议以应对国际和平与安全面临的威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Barakah_nuclear_power_plant">Barakah nuclear power plant</a></li>
<li><a href="https://en.wikipedia.org/wiki/International_Atomic_Energy_Agency">International Atomic Energy Agency - Wikipedia</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#middle-east`, `#energy`, `#military-risk`, `#nuclear-safety`

---

<a id="item-3"></a>
## [霍尔木兹危机扰乱贸易，加剧生活成本危机](https://news.un.org/feed/view/en/story/2026/05/1167548) ⭐️ 8.0/10

尽管美伊停火协议脆弱，霍尔木兹海峡周边的持续不稳定仍在扰乱全球贸易、推高能源成本，并引发就业和生活成本危机。 霍尔木兹海峡是全球石油运输的关键咽喉，持续的不稳定直接威胁能源安全、加剧通胀并影响全球经济稳定。 停火于 2026 年 4 月 8 日通过巴基斯坦斡旋达成，包括为期两周的有条件休战及后续持久协议谈判，但海峡仍面临安全事件风险。

rss · UN News · May 19, 12:00

**背景**: 霍尔木兹海峡是连接波斯湾与阿曼湾的狭窄水道，是全球最关键的石油运输咽喉，每日约有 2000 万桶石油通过。美伊停火于 2026 年 4 月经斡旋达成，此前冲突持续六周，协议条款包括停止伊朗核计划、限制导弹、重新开放海峡，以换取制裁放松。尽管停火，残余不稳定仍持续影响全球能源市场和供应链。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz - Wikipedia</a></li>
<li><a href="https://commonslibrary.parliament.uk/research-briefings/cbp-10637/">US-Iran ceasefire and nuclear talks in 2026 - House of Commons Library</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#supply-chain`, `#middle-east`

---

<a id="item-4"></a>
## [欧洲央行首席经济学家分析能源供应冲击](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260513~5b14c78806.en.html) ⭐️ 8.0/10

欧洲央行首席经济学家菲利普·莱恩在 2026 年 5 月 13 日的演讲中阐述了能源供应冲击——尤其是全球性冲击——如何通过国际供应链产生复合效应，这与局部冲击不同。 这一分析可能影响欧洲央行对能源驱动通胀的货币政策应对，从而塑造市场对利率、债券收益率和欧元的预期。 莱恩区分了局部和全球能源冲击：全球冲击导致价格复合上涨，因为所有国际供应商都转嫁更高的成本，没有进口渠道的缓解。

rss · ECB Press Releases · May 13, 19:00

**背景**: 欧洲央行是欧元区的中央银行，负责维护价格稳定。能源供应冲击（如石油或天然气价格飙升）可能推高通胀并拖累经济增长，给货币政策带来两难。作为首席经济学家，菲利普·莱恩的观点有助于塑造央行的政策立场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260513~5b14c78806.en.html">Analytical perspectives on energy supply shocks</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank - Wikipedia</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#energy`, `#macroeconomics`, `#europe`, `#commodities`

---

<a id="item-5"></a>
## [乌克兰战争“日益致命”，联合国安理会接获警告](https://news.un.org/feed/view/en/story/2026/05/1167546) ⭐️ 7.0/10

一名联合国高级官员周二向安理会通报称，已进入第五个年头的乌克兰战争“日益致命”，表明冲突正在进一步升级。 这一警告凸显了能源与粮食供应风险的加剧、制裁与军事援助升级的可能性，以及更广泛的地缘政治不稳定，直接冲击全球市场与风险偏好。 通报强调了局势恶化，但未宣布任何具体措施；由于俄罗斯拥有否决权，安理会就乌克兰问题基本陷入僵局。

rss · UN News · May 19, 12:00

**背景**: 联合国安理会由 15 个成员国组成，其中五个常任理事国（中国、法国、俄罗斯、英国、美国）拥有否决权，对维护国际和平与安全负有首要责任。俄罗斯多次使用否决权阻止涉乌克兰决议的通过，使安理会无法采取果断行动。此次通报正值外交僵局持续、人道主义关切加剧之际。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/Permanent_members_of_the_United_Nations_Security_Council">Permanent members of the United Nations Security Council - Wikipedia</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#geopolitics`, `#diplomacy`, `#military-risk`, `#energy`

---

<a id="item-6"></a>
## [联合国警告核恐怖主义威胁达历史新高](https://news.un.org/feed/view/en/story/2026/05/1167501) ⭐️ 7.0/10

联合国警告，由于军用无人机和人工智能的广泛普及，核恐怖主义威胁已达到前所未有的高度。 该评估可能促使全球加强防扩散努力、收紧两用技术出口管制，并在联合国安理会和国际原子能机构重新聚焦核安全，可能影响国防和科技领域。 警告强调了新兴技术在放大核恐怖主义风险方面的作用，但未披露具体事件或情报。

rss · UN News · May 17, 12:00

**背景**: 《制止核恐怖主义行为国际公约》由联合国大会于 2005 年通过、2007 年生效，将核恐怖主义定为犯罪并促进国际合作。尽管有此类框架，但无人机和人工智能等两用技术的快速发展给核安全和出口管制带来了新挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/International_Convention_for_the_Suppression_of_Acts_of_Nuclear_Terrorism">International Convention for the Suppression of Acts of Nuclear Terrorism</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dual-use_technology">Dual-use technology - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#nuclear-proliferation`, `#technology`

---

<a id="item-7"></a>
## [联合国警告地缘政治冲突加剧全球经济脆弱性](https://news.un.org/feed/view/en/story/2026/05/1167551) ⭐️ 6.0/10

联合国警告称，地缘政治冲突、能源成本上升和金融不稳定正在加剧全球经济脆弱性，对增长和贸易构成威胁。 联合国的这一警告表明宏观风险加剧，可能影响市场情绪、贸易政策和国际合作，凸显地缘政治紧张局势正在产生切实的经济后果。 联合国报告虽强调广泛风险，但未提供具体数据或宣布新政策措施；报告还简要提及加沙和南苏丹的人道主义关切。

rss · UN News · May 19, 12:00

**背景**: 联合国定期监测全球经济趋势，其评估常为 G7、G20 和 IMF 讨论提供参考。持续冲突，包括乌克兰战争和中东紧张局势，已导致能源价格飙升和供应链中断。这些因素与各国为抑制通胀而收紧货币政策共同增加了衰退风险和市场波动。

**标签**: `#geopolitics`, `#macroeconomics`, `#energy`, `#global-markets`, `#financial-stability`

---

<a id="item-8"></a>
## [停电与燃料短缺导致古巴医疗系统陷入危机](https://news.un.org/feed/view/en/story/2026/05/1167524) ⭐️ 6.0/10

联合国高级官员周五警告称，古巴医疗系统因长期停电和燃料短缺而承受巨大压力，医院暂停手术并面临药品短缺。 日益严重的危机可能引发大规模移民和地区不稳定，同时凸显了美国制裁的经济和人道主义代价，以及古巴的能源脆弱性。 美国禁运阻止了燃料进口，加剧了危机；关键燃料供应国墨西哥因美国压力不愿违抗，使短缺进一步恶化。

rss · UN News · May 15, 12:00

**背景**: 美国自 1960 年以来对古巴实施全面经济禁运，严重限制其获得燃料、商品和金融市场准入。古巴发电高度依赖进口石油，近期美国措施进一步限制了燃料运输。这导致频繁停电，使依赖稳定电力进行手术和药品冷藏的医院等基本服务陷入瘫痪。这场危机是更广泛经济崩溃的一部分，加剧了移民压力和地区稳定担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_States_embargo_against_Cuba">United States embargo against Cuba - Wikipedia</a></li>
<li><a href="https://www.travelandtourworld.com/news/article/united-states-fuel-blockade-deepens-cubas-tourism-crisis-hotel-closures-flight-cancellations-and-economic-strain-all-you-need-to-know/">United States Fuel Blockade Deepens Cuba ’s Tourism Crisis Hotel...</a></li>

</ul>
</details>

**标签**: `#energy`, `#supply-chain`, `#cuba`, `#geopolitics`, `#sovereign-risk`

---