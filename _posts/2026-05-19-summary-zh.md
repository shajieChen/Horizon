---
layout: default
title: "Horizon Summary: 2026-05-19 (ZH)"
date: 2026-05-19
lang: zh
---

> From 41 items, 10 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [IAEA 在阿联酋核电站遭遇无人机袭击后呼吁核安全](#item-2) ⭐️ 8.0/10
3. [美联储任命鲍威尔为临时主席，直至沃什宣誓就职](#item-3) ⭐️ 8.0/10
4. [联合国警告能源贸易中断将数百万人推向贫困](#item-4) ⭐️ 7.0/10
5. [联合国救援车辆在乌克兰赫尔松两次遭袭](#item-5) ⭐️ 7.0/10
6. [联合国斡旋也门最大规模换俘，超 1600 人获释](#item-6) ⭐️ 7.0/10
7. [欧央行首席经济学家莱恩分析能源供给冲击](#item-7) ⭐️ 7.0/10
8. [联合国人权高专办：加沙杀戮持续，西岸定居者侵占与强迫迁移激增](#item-8) ⭐️ 6.0/10
9. [联合国警告核恐怖主义威胁达历史最高](#item-9) ⭐️ 6.0/10
10. [联合国警告：停电和燃料短缺致古巴医疗体系崩溃](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 18, 22:59

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
| US Mega Cap Basket | US | neutral 33/33/34 | bullish 38/31/31 | bullish 40/32/28 | high |
| Japan Equity Basket | JP | neutral 33/33/34 | neutral 33/33/34 | bullish 40/32/28 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | neutral 34/34/31 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| QQQ price trend | close=705.88; 1d=-0.43%; 5d=-1.04%; 20d=+9.14% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=28994.37; 1d=-0.45%; 5d=-1.11%; 20d=+9.04% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29144.25; 1d=-0.30%; 5d=-0.95%; 20d=+8.96% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=16.8%; implied_move=0.4%; put/call OI=2.5875825269060324 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.61; 2Y=4.07; 10Y-2Y=0.54 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=62.8; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
| QQQ price trend | close=705.88; 1d=-0.43%; 5d=-1.04%; 20d=+9.14% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=28994.37; 1d=-0.45%; 5d=-1.11%; 20d=+9.04% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29144.25; 1d=-0.30%; 5d=-0.95%; 20d=+8.96% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| AAPL price trend | close=297.84; 1d=-0.80%; 5d=+1.76%; 20d=+9.18% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=611.21; 1d=-0.49%; 5d=+2.06%; 20d=-8.90% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=222.32; 1d=-1.33%; 5d=+1.31%; 20d=+10.03% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=423.54; 1d=+0.38%; 5d=+2.64%; 20d=+1.31% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=396.94; 1d=+0.04%; 5d=+2.14%; 20d=+17.64% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=409.99; 1d=-2.90%; 5d=-7.87%; 20d=+4.46% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| META options surface | ATM IV=6.7%; implied_move=0.2%; put/call OI=0.5613887773356212 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=5.9%; implied_move=0.2%; put/call OI=0.8623864473361159 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=3.3%; implied_move=0.1%; put/call OI=0.6970676879039073 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=5.7%; implied_move=0.3%; put/call OI=0.5691721132897604 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=4.0%; implied_move=0.2%; put/call OI=0.6079541879051035 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=4.6%; implied_move=0.2%; put/call OI=0.7752532397713768 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=62.8; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| AAPL insider filings | recent Form4 count=586 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| MSFT insider filings | recent Form4 count=731 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| NVDA insider filings | recent Form4 count=562 | 内部人交易节奏可作为估值温度辅助校验信号。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多；长端美债收益率偏高，对成长风格估值形成压制；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | high |
| 1月 | 40% | 32% | 28% | bullish | 20日趋势维持上行，1月窗口偏多；长端美债收益率偏高，对成长风格估值形成压制；风险偏好仍可控且波动未失控，中期上行概率提高 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| AAPL price trend | close=297.84; 1d=-0.80%; 5d=+1.76%; 20d=+9.18% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=611.21; 1d=-0.49%; 5d=+2.06%; 20d=-8.90% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=222.32; 1d=-1.33%; 5d=+1.31%; 20d=+10.03% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 8035.T price trend | close=49260.00; 1d=-2.05%; 5d=-5.41%; 20d=+12.72% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=5593.00; 1d=-2.65%; 5d=-2.61%; 20d=+31.85% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=90.92; 1d=-0.16%; 5d=-1.45%; 20d=+1.78% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2954.50; 1d=-4.23%; 5d=+2.94%; 20d=-11.17% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3596.00; 1d=+0.56%; 5d=+6.64%; 20d=+9.63% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=76830.00; 1d=-0.45%; 5d=-6.65%; 20d=+22.24% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=62.8; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.61; 2Y=4.07; 10Y-2Y=0.54 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| 8035.T price trend | close=49260.00; 1d=-2.05%; 5d=-5.41%; 20d=+12.72% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=5593.00; 1d=-2.65%; 5d=-2.61%; 20d=+31.85% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=90.92; 1d=-0.16%; 5d=-1.45%; 20d=+1.78% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9618.HK price trend | close=126.50; 1d=-1.09%; 5d=+6.75%; 20d=+3.18% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=30.66; 1d=-0.13%; 5d=-3.28%; 20d=-4.19% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=449.20; 1d=-1.58%; 5d=-2.15%; 20d=-10.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=28.06; 1d=-0.39%; 5d=-5.17%; 20d=-7.36% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=82.15; 1d=-0.67%; 5d=-2.61%; 20d=-5.03% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=131.70; 1d=-0.45%; 5d=-1.64%; 20d=-3.45% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=62.8; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.61; 2Y=4.07; 10Y-2Y=0.54 | 利率曲线决定权益估值贴现与风险偏好上限。 |
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
| 9618.HK price trend | close=126.50; 1d=-1.09%; 5d=+6.75%; 20d=+3.18% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=30.66; 1d=-0.13%; 5d=-3.28%; 20d=-4.19% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=449.20; 1d=-1.58%; 5d=-2.15%; 20d=-10.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

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
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days out or more. IV is a forward looking prediction of the likelihood...

- [CBOE Nasdaq 100 Volatility Index Today (VXN) - Investing.com](https://www.investing.com/indices/cboe-nasdaq-100-voltility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Get detailed information on the CBOE Nasdaq 100 Volatility including charts, technical analysis, components and more.

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

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

- [QQQ Stock Volatility History & Chart Since 1999](https://wallstreetnumbers.com/etfs/qqq/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Get all-time historical data of QQQ historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [ICE BofA US High Yield (MERH0A0) - Investing.com](https://www.investing.com/indices/ice-bofa-us-high-yield)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：Get detailed information on the ICE BofA US High Yield including charts, technical analysis, components and more.

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [EWJ / iShares MSCI Japan ETF Overview / MarketWatch](https://www.marketwatch.com/investing/fund/ewj)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ / A complete iShares MSCI Japan ETF exchange traded fund overview by MarketWatch. View the latest ETF prices and news for better ETF investing.

- [EWJ ETF Stock Price & Overview](https://stockanalysis.com/etf/ewj/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Get a real-time stock price for the EWJ ETF (iShares MSCI Japan ETF) with an overview of various metrics and statistics.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

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
## [IAEA 在阿联酋核电站遭遇无人机袭击后呼吁核安全](https://news.un.org/feed/view/en/story/2026/05/1167540) ⭐️ 8.0/10

周日一架无人机袭击了阿联酋巴拉卡核电站，引发外围火灾，但未造成人员伤亡或重大损害；国际原子能机构总干事随后强调在武装冲突中必须保护核设施。 此次袭击凸显了关键能源基础设施在非对称战争中的脆弱性，加剧了对冲突地区核安全的担忧和地区局势升级的可能性，可能扰乱能源市场并促成更严格的国际核安全措施。 火势仅限于外围并被扑灭，未影响反应堆；没有放射性物质泄漏。阿联酋未指责任何方，IAEA 也未说明无人机来源，尽管事件发生在与伊朗相关紧张局势加剧的背景下。

rss · UN News · May 18, 12:00

**背景**: 巴拉卡核电站是阿联酋唯一的核设施，也是阿拉伯世界首座核电站，拥有四座韩国设计的反应堆，位于阿布扎比阿尔达夫拉地区的海湾沿岸。国际原子能机构（IAEA）负责制定全球核安全标准，并多次呼吁在冲突地区（如乌克兰扎波罗热核电站）保持克制。也门胡塞武装曾声称对阿联酋发动过无人机和导弹袭击，这与更广泛的伊朗-沙特博弈有关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apnews.com/article/iran-us-uae-nuclear-drones-71e7e58f45193b7dee3df28740532a7b">UAE nuclear plant targeted in drone strike amid Iran tensions ...</a></li>
<li><a href="https://news.un.org/en/story/2026/05/1167540">UN underscores protection of nuclear sites following drone ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Barakah_nuclear_power_plant">Barakah nuclear power plant - Wikipedia</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#energy`, `#military-risk`, `#geopolitics`

---

<a id="item-3"></a>
## [美联储任命鲍威尔为临时主席，直至沃什宣誓就职](https://www.federalreserve.gov/newsevents/pressreleases/other20260515a.htm) ⭐️ 8.0/10

美联储理事会任命杰罗姆·鲍威尔为临时主席，直至凯文·沃什宣誓就任新主席；鲍威尔的任期已结束，此项任命是过渡期的常规做法。 此次领导层更迭可能预示着货币政策方向转变，因为沃什在抗通胀和美联储沟通方式上的观点与鲍威尔不同，可能影响利率前景和市场预期。 沃什的就职日期尚未确定；他的提名因其对美联储独立性的表述引发争议，其政策优先事项包括更聚焦的通胀目标、减少公开指引，但短期内政策大幅转向的可能性不大。

rss · Federal Reserve Press Releases · May 15, 21:00

**背景**: 美联储主席任期四年；若继任者尚未确认，根据《联邦储备法》，现任主席可被任命为临时主席。凯文·沃什曾任美联储理事，是总统提名的下任主席。他主张优先遏制通胀，并对美联储独立性提出质疑，引发前官员争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.federalreserve.gov/newsevents/pressreleases/other20260515a.htm">Federal Reserve Board names Jerome H. Powell as chair pro ...</a></li>
<li><a href="https://www.cnbc.com/2026/05/04/fed-kevin-warsh-interest-rates.html">Warsh's take on Fed independence is met with confusion and some concern</a></li>
<li><a href="https://www.chase.com/personal/investments/learning-and-insights/article/kevin-warsh-is-the-new-chair-of-the-federal-reserve">Kevin Warsh Is the New Chair of the Federal Reserve: Here’s What That Could Mean for Markets and Investors in 2026 | Chase</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#united-states`, `#bonds`, `#global-markets`

---

<a id="item-4"></a>
## [联合国警告能源贸易中断将数百万人推向贫困](https://news.un.org/feed/view/en/story/2026/05/1167526) ⭐️ 7.0/10

联合国警告，全球能源供应和贸易通道中断正推高粮食、运输和基本商品成本，导致经济增长放缓，将数百万人推向贫困，债务沉重的发展中国家尤为承压。 这表明全球经济稳定和主权债务可持续性面临系统性风险，可能引发国际金融机构的援助倡议、政策干预，并在脆弱经济体中引发市场波动。 中断影响基本商品，通胀削弱购买力；数百万人面临风险，尤其是面临主权信用压力的债务沉重发展中国家。

rss · UN News · May 15, 12:00

**背景**: 联合国是一个拥有 193 个成员国的政府间组织，致力于维护和平与促进发展。主权风险指政府债务违约的可能性，在全球危机期间对发展中经济体尤为令人担忧。能源供应中断往往源于地缘政治冲突，直接影响全球运输和生产成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations">United Nations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_risk">Sovereign risk</a></li>

</ul>
</details>

**标签**: `#energy`, `#supply-chain`, `#macroeconomics`, `#sovereign-risk`, `#global-markets`

---

<a id="item-5"></a>
## [联合国救援车辆在乌克兰赫尔松两次遭袭](https://news.un.org/feed/view/en/story/2026/05/1167525) ⭐️ 7.0/10

5 月 14 日，一辆明显标识的联合国救援车辆在乌克兰赫尔松市两次遭到袭击，联合国秘书长对此表示震惊。 此次袭击表明，对保护人道主义工作者的国际规范的无视可能正在升级，这可能危及正在进行的救援行动，并加剧俄乌冲突中的外交压力。 该车辆清晰标示为联合国人道主义车辆，在位于前线的赫尔松市被两次击中，联合国秘书长对此表达震惊。

rss · UN News · May 15, 12:00

**背景**: 赫尔松是乌克兰南部的前线城市，曾于 2022 年被俄军占领后解放，至今仍遭受猛烈炮击和无人机袭击。国际人道法规定必须保护援助人员和标明的人道主义车辆。联合国安理会多次谴责针对人道主义人员的袭击，并呼吁追究责任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167525">World News in Brief: UN relief vehicle struck in Ukraine ... | UN News</a></li>
<li><a href="https://www.euronews.com/2025/11/11/three-years-since-the-liberation-of-kherson-no-russian-troops-but-thousands-of-attack-dron">Three years since the liberation of Kherson: No Russian ...</a></li>
<li><a href="https://www.orfonline.org/expert-speak/international-cooperation-for-the-protection-of-humanitarian-workers">International cooperation for the protection of humanitarian workers</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#diplomacy`, `#geopolitics`, `#military-risk`

---

<a id="item-6"></a>
## [联合国斡旋也门最大规模换俘，超 1600 人获释](https://news.un.org/feed/view/en/story/2026/05/1167511) ⭐️ 7.0/10

在联合国调解下，也门国际公认政府与胡塞武装达成协议，将释放超过 1600 名与冲突有关的被拘留者，这是内战爆发以来最大规模的换俘。 这一罕见的建立信任措施可能缓解长达 11 年的冲突，重启停滞的和平谈判，并可能减轻地区不稳定及与也门战略位置相关的能源风险溢价。 该协议在约旦安曼经联合国数月的调解谈判后达成，并基于 2025 年 12 月在阿曼马斯喀特达成的框架。据部分报道，预计将涉及 1728 名被拘留者，但核查工作仍至关重要。

rss · UN News · May 14, 12:00

**背景**: 也门内战始于 2014 年，伊朗支持的胡塞武装占领首都萨那，2015 年沙特领导的联军介入。联合国已促成多次休战和换俘，包括 2023 年约 900 人的交换。尽管存在事实上的停火，但正式和平协议仍未达成，人道主义状况严峻。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apnews.com/article/yemen-civil-war-detainees-swap-c8fbb495ba32f5b547fc1ae112a2fac2">Yemen government and Houthis agree to free 1,600 detainees in the largest swap of the 11-year war</a></li>
<li><a href="https://www.washingtonpost.com/world/2026/05/14/yemen-civil-war-detainees-swap/631be0ee-4fab-11f1-97e7-22c6c29ff0d8_story.html">Yemen sides agree to release over 1,600 detainees in the largest swap of 11-year war - The Washington Post</a></li>
<li><a href="https://www.yemenmonitor.com/en/Details/ArtMID/908/ArticleID/171750">UN Calls for Release of All Arbitrary Detainees Amid Major Yemen Prisoner Swap Agreement - Yemen Monitor</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-7"></a>
## [欧央行首席经济学家莱恩分析能源供给冲击](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260513~5b14c78806.en.html) ⭐️ 7.0/10

欧洲央行首席经济学家菲利普·莱恩发表演讲，分析了能源供给冲击，区分了本地与全球冲击，并指出全球冲击通过国际供应链产生成本复合效应。 这一分析揭示了欧洲央行应对未来能源冲击的框架，在持续地缘政治紧张局势下，将影响利率预期和金融市场定价。 关键细节在于，全球能源冲击无法通过进口渠道缓解，且会通过国际供应链累积成本，这或影响欧洲央行对通胀持续性的判断。

rss · ECB Press Releases · May 13, 19:00

**背景**: 欧洲央行负责欧元区货币政策，致力于维护物价稳定。霍尔木兹海峡等地缘事件引发的能源供给中断，可导致价格飙升，使央行在平衡通胀与增长时面临挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260513~5b14c78806.en.html">Analytical perspectives on energy supply shocks</a></li>
<li><a href="https://www.einnews.com/pr_news/912731734/philip-r-lane-analytical-perspectives-on-energy-supply-shocks">Philip R. Lane: Analytical perspectives on energy supply shocks - EIN Presswire</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#energy`, `#macroeconomics`, `#europe`, `#geopolitics`

---

<a id="item-8"></a>
## [联合国人权高专办：加沙杀戮持续，西岸定居者侵占与强迫迁移激增](https://news.un.org/feed/view/en/story/2026/05/1167538) ⭐️ 6.0/10

联合国人权事务高级专员办事处（OHCHR）称，尽管以色列与哈马斯已停火，加沙地带的杀戮与破坏仍在继续，而被占西岸的强迫迁移已达到“数十年来未曾见过的”规模。 该报告凸显了停火的脆弱性及冲突升级的高风险，这不仅使中东外交努力复杂化，还加剧了对加沙和西岸平民的人道主义关切。 联合国人权高专办高级官员周一在日内瓦发出警告，指出定居点扩建和定居者暴力是导致强迫迁移危机的主要因素，同时军事行动也仍在持续。

rss · UN News · May 18, 12:00

**背景**: 被占领的西岸（约旦河西岸）自 1967 年起处于以色列军事占领之下，根据国际法被视为被占领土，以色列在其上建立定居点被联合国安理会和国际法院认定非法。联合国人权事务高级专员办事处（OHCHR）是负责监测人权状况的联合国机构。以色列与哈马斯此前在加沙爆发大规模冲突后达成的停火协议依然脆弱，并未阻止以军在约旦河西岸的军事行动或定居者的侵占行为，这些行为常伴随暴力与土地掠夺。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Occupied_West_Bank">Occupied West Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/OHCHR">OHCHR</a></li>
<li><a href="https://www.aljazeera.com/news/2025/10/3/what-israeli-settler-encroachment-intimidation-look-like-in-the-west-bank">What Israeli settler encroachment , intimidation look like... | Al Jazeera</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#diplomacy`, `#geopolitics`, `#military-risk`

---

<a id="item-9"></a>
## [联合国警告核恐怖主义威胁达历史最高](https://news.un.org/feed/view/en/story/2026/05/1167501) ⭐️ 6.0/10

联合国警告，由于军用无人机和人工智能等技术的广泛普及，核恐怖主义威胁已达到前所未有的最高水平。 这一警告表明全球安全风险加剧，可能影响外交重点、国防开支和防扩散努力。它凸显了技术扩散可能增强非国家行为体能力，使国际反恐策略复杂化。 联合国特别指出军用无人机和人工智能是关键推动因素，但未引用具体情报或即将发生的阴谋。该评估基于长期关切，包括 2005 年《制止核恐怖主义行为国际公约》所定义的脏弹或破坏风险。

rss · UN News · May 17, 12:00

**背景**: 核恐怖主义指非国家行为体使用或威胁使用核或放射性武器，这一问题自核时代开启以来便备受关注。2005 年联合国公约将此类行为定为刑事犯罪，但迄今为止尚无恐怖组织成功获得可用的核武器。军用无人机和人工智能的扩散降低了袭击核设施或走私路线所需的技术门槛。成立于 1945 年以维护国际和平的联合国定期评估全球威胁，因此这次明确的警告格外引人注目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nuclear_terrorism">Nuclear terrorism</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations">United Nations</a></li>
<li><a href="https://www.npr.org/2026/03/18/nx-s1-5752387/how-drones-are-being-used-globally-in-conflicts-and-by-criminals">Evolving use of militarized drones in Mexico, Sudan and... : NPR</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#technology`

---

<a id="item-10"></a>
## [联合国警告：停电和燃料短缺致古巴医疗体系崩溃](https://news.un.org/feed/view/en/story/2026/05/1167524) ⭐️ 6.0/10

联合国官员警告，由于持续停电和燃料短缺，古巴各地医院正在暂停手术、难以维持救命设备运转，并面临严重药品短缺。 医疗系统崩溃预示着人道主义危机恶化，可能推高向美国和邻国的移民潮，增加古巴主权债务风险并给地区稳定带来压力。 古巴已耗尽其柴油和燃料油储备，导致部分地区停电长达 20 小时。美国制裁收紧及委内瑞拉石油运输减少加剧了能源危机。

rss · UN News · May 15, 12:00

**背景**: 古巴长期面临美国经济封锁，限制其获得能源和进入金融市场。拜登政府近期收紧制裁，切断燃料供应。加之委内瑞拉石油运输减少，古巴燃料耗尽，导致长时间停电和基本服务崩溃，引发自 1990 年代以来最大的移民潮。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehill.com/policy/energy-environment/5878261-energy-blockade-cuba-crisis/">Cuban energy system on the brink amid US sanctions, minister says</a></li>
<li><a href="https://www.evadaily.com/article/cuba-fuel-depletion-us-embargo-energy-crisis">Cuba Faces Total Fuel Depletion as US Oil Embargo Tightens ...</a></li>

</ul>
</details>

**标签**: `#cuba`, `#energy`, `#supply-chain`, `#sovereign-risk`, `#geopolitics`

---