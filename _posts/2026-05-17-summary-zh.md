---
layout: default
title: "Horizon Summary: 2026-05-17 (ZH)"
date: 2026-05-17
lang: zh
---

> From 43 items, 13 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [能源与贸易中断使数百万人陷入贫困](#item-2) ⭐️ 8.0/10
3. [欧洲央行副行长德金多斯接受金融时报采访谈货币政策](#item-3) ⭐️ 8.0/10
4. [联合国警告中东战争影响下索马里面临饥荒风险](#item-4) ⭐️ 7.0/10
5. [联合国驻黎部队警告无人机事件危及人员安全](#item-5) ⭐️ 7.0/10
6. [拉加德呼吁建设持久韧性的欧洲](#item-6) ⭐️ 7.0/10
7. [欧洲央行莱恩分析能源供应冲击](#item-7) ⭐️ 7.0/10
8. [联合国报告：加沙、西岸和黎巴嫩平民苦难加剧](#item-8) ⭐️ 6.0/10
9. [也门换囚 1600 名被拘者将获释](#item-9) ⭐️ 6.0/10
10. [联合国官员：俄军袭击基辅平民明显违反国际人道法](#item-10) ⭐️ 6.0/10
11. [古特雷斯敦促改革以增强非洲全球声音](#item-11) ⭐️ 6.0/10
12. [美联储任命鲍威尔为临时主席，等待沃什就职](#item-12) ⭐️ 6.0/10
13. [美联储发布 2025 年美国家庭经济福祉报告](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 16, 23:03

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
| NQ=F price trend | close=29231.75; 1d=-1.54%; 5d=-0.34%; 20d=+8.97% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=708.93; 1d=-1.51%; 5d=-0.32%; 20d=+9.26% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29125.20; 1d=-1.54%; 5d=-0.38%; 20d=+9.20% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=16.5%; implied_move=1.2%; put/call OI=2.5785918138795565 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=62.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.59; 2Y=4.09; 10Y-2Y=0.5 | 利率曲线决定权益估值贴现与风险偏好上限。 |
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
| NQ=F price trend | close=29231.75; 1d=-1.54%; 5d=-0.34%; 20d=+8.97% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
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
| AMZN price trend | close=264.14; 1d=-1.15%; 5d=-3.13%; 20d=+5.42% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=225.32; 1d=-4.42%; 5d=+4.70%; 20d=+11.72% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=396.78; 1d=-1.07%; 5d=-1.00%; 20d=+16.13% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=300.23; 1d=+0.68%; 5d=+2.45%; 20d=+11.20% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=422.24; 1d=-4.75%; 5d=-1.43%; 20d=+5.40% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=614.23; 1d=-0.68%; 5d=+0.75%; 20d=-10.79% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| GOOGL options surface | ATM IV=26.2%; implied_move=1.7%; put/call OI=0.7374275419081936 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=36.0%; implied_move=2.6%; put/call OI=0.6453932129159652 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=29.1%; implied_move=2.0%; put/call OI=0.6081990223125696 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=17.9%; implied_move=1.2%; put/call OI=0.5327261105784595 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=23.1%; implied_move=1.6%; put/call OI=0.40361334442288144 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=33.7%; implied_move=2.4%; put/call OI=0.9230932713696709 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| AAPL insider filings | recent Form4 count=586 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| MSFT insider filings | recent Form4 count=730 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.59; 2Y=4.09; 10Y-2Y=0.5 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=62.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| AMZN price trend | close=264.14; 1d=-1.15%; 5d=-3.13%; 20d=+5.42% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
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
| 8035.T price trend | close=50290.00; 1d=-1.78%; 5d=-4.12%; 20d=+18.44% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=91.07; 1d=-1.08%; 5d=-1.25%; 20d=+0.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3576.00; 1d=+3.83%; 5d=+14.84%; 20d=+10.00% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=5745.00; 1d=-0.43%; 5d=-6.30%; 20d=+52.63% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77180.00; 1d=-0.17%; 5d=-8.30%; 20d=+21.51% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=3085.00; 1d=+2.56%; 5d=+5.90%; 20d=-7.05% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.59; 2Y=4.09; 10Y-2Y=0.5 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=62.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 8035.T price trend | close=50290.00; 1d=-1.78%; 5d=-4.12%; 20d=+18.44% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=91.07; 1d=-1.08%; 5d=-1.25%; 20d=+0.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3576.00; 1d=+3.83%; 5d=+14.84%; 20d=+10.00% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 0700.HK price trend | close=456.40; 1d=+0.33%; 5d=-2.05%; 20d=-10.69% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=36.20; 1d=-2.79%; 5d=-2.79%; 20d=-3.72% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=30.70; 1d=-3.22%; 5d=-3.09%; 20d=-4.24% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=24.06; 1d=-1.47%; 5d=-0.91%; 20d=+2.51% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=28.17; 1d=-3.53%; 5d=-4.67%; 20d=-7.49% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=127.90; 1d=-1.69%; 5d=+7.93%; 20d=+3.31% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=62.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.59; 2Y=4.09; 10Y-2Y=0.5 | 利率曲线决定权益估值贴现与风险偏好上限。 |
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
| 0700.HK price trend | close=456.40; 1d=+0.33%; 5d=-2.05%; 20d=-10.69% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=36.20; 1d=-2.79%; 5d=-2.79%; 20d=-3.72% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=30.70; 1d=-3.22%; 5d=-3.09%; 20d=-4.24% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [Option Implied Volatility Rankings Report](https://marketchameleon.com/volReports/VolatilityRankings)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：What can I find on the Implied Volatility Rankings Report? Market Chameleon's Implied Volatility Rankings Report shows a detailed set of data for stocks, comparing their current...

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days or more out. IV is a forward looking prediction of the likelihood...

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

- [Cboe Global Indices: VIX Index Dashboard](https://www.cboe.com/us/indices/dashboard/vix/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：The VIX Index is often referred to as the market's "fear gauge". The VIX Index is the centerpiece of Cboe Global Markets' volatility franchise, which includes volatility indexes...

- [CBOE Volatility Index: VIX (VIXCLS) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/VIXCLS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Graph and download economic data for CBOE Volatility Index: VIX (VIXCLS) from 1990-01-02 to 2026-05-14 about VIX, volatility, stock market, and USA.

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
  - 摘要：U.S. High Yield Bond Spread: 3.09% as of May 12, 2026. Units: Percent Frequency: Daily, Close Release: ICE BofA Indices Source: Ice Data Indices, LLC

- [QQQ Options Chain — Open Interest, Implied Volatility, Max Pain & Gamma ...](https://whalequant.io/en/stocks/QQQ/options-analytics)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Explore the live QQQ options chain with strikes, open interest, volume, implied volatility (IV), max pain levels, gamma exposure, dealer positioning and options flow analysis. P...

- [QQQ Volatility Term Structure for Invesco QQQ Trust Series 1 ETF ...](https://www.barchart.com/stocks/quotes/QQQ/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Volatility Term Structure chart plots the at-the-money implied volatility across expirations, which are an invaluable tool in determining options strategies based on anticipated...

- [Invesco QQQ (QQQ) - Implied Volatility (Mean) (30-Day) - AlphaQuery](https://www.alphaquery.com/stock/QQQ/volatility-option-statistics/30-day/iv-mean)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Implied Volatility (Mean): The forecasted future volatility of the security over the selected time frame, derived from the average of the put and call implied volatilities for o...

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [1 USD to JPY - US Dollars to Japanese Yen Exchange Rate - Xe](https://www.xe.com/en/currencyconverter/convert/?Amount=1&From=USD&To=JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest 1 US Dollar to Japanese Yen rate for FREE with the original Universal Currency Converter. Set rate alerts for USD to JPY and learn more about US Dollars and Japan...

- [JPY to USD - Japanese Yen to US Dollar Conversion - Exchange Rates](https://www.exchange-rates.org/converter/jpy-usd)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Use the JPY to USD currency converter at Exchange-Rates.org for accurate and up-to-date exchange rates. Easily convert Japanese Yen to US Dollars with real-time data.

- [USD JPY / US Dollar to Yen Live Rate - Investing.com](https://www.investing.com/currencies/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get real time data on the USD/JPY pair including the live rate, as well as our currency converter, analysis, news, historical data and more.

- [iShares MSCI Japan ETF / EWJ](https://www.ishares.com/us/products/239665/ishares-msci-japan-etf)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：The iShares MSCI Japan ETF seeks to track the investment results of an index composed of Japanese equities.

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
## [能源与贸易中断使数百万人陷入贫困](https://news.un.org/feed/view/en/story/2026/05/1167526) ⭐️ 8.0/10

联合国报告警告，全球能源供应和贸易走廊中断正在推高食品、交通及其他基本商品的成本，减缓经济增长，并将数百万人推向贫困，脆弱发展中国家尤甚。 这预示着系统性宏观经济风险，可能导致贫困扩大、发展中国家陷入主权债务困境，并需要多边机构协调政策干预以稳定市场和供应链。 报告特别强调了对负债累累的发展中国家和脆弱家庭不成比例的影响，这对大宗商品价格和主权债务市场均有波及。

rss · UN News · May 15, 12:00

**背景**: 全球贸易走廊是连接主要经济体的关键海、陆、铁路线，每年运输超过 110 亿吨货物，包括来自中东的石油和美洲的农产品。因地缘政治冲突、制裁或基础设施故障导致的中断，会大幅推高基本商品成本。能源供应冲击同样会抬高运输和生产成本。这些影响对依赖进口且财政缓冲有限的发展中国家打击最大，加剧了主权债务风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mckinsey.com/mgi/our-research/global-trade-explorer-what-are-the-most-important-trade-corridors">What are the most important trade corridors? | McKinsey</a></li>
<li><a href="https://www.geopolitika.it/en/where-global-trade-flows-sea-land-and-rail-corridors-that-move-the-world/">Where Global Trade Flows and Corridors That Move the World</a></li>
<li><a href="https://unctad.org/news/new-corridors-global-trade">The new corridors of global trade - UNCTAD</a></li>

</ul>
</details>

**标签**: `#energy`, `#supply-chain`, `#macroeconomics`, `#sovereign-risk`, `#global-markets`

---

<a id="item-3"></a>
## [欧洲央行副行长德金多斯接受金融时报采访谈货币政策](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260511~3fa2df2fa9.en.html) ⭐️ 8.0/10

欧洲央行副行长路易斯·德金多斯接受《金融时报》采访，讨论了欧元区的货币政策立场和经济前景，可能释放未来利率决策或量化紧缩调整的信号。 央行沟通直接影响欧元汇率、欧洲债券收益率和整体金融环境，因此对于预期货币政策转变的投资者和政策制定者而言，此次采访至关重要。 该采访于 2026 年 5 月 11 日发布在欧洲央行官网上；作为副行长，德金多斯在执行委员会中扮演关键角色，负责实施货币政策决策。

rss · ECB Press Releases · May 11, 04:00

**背景**: 欧洲央行是欧元区的中央银行，负责制定货币政策。其执行董事会由行长、副行长和四名其他成员组成，总部设在法兰克福。路易斯·德金多斯曾任西班牙经济大臣，自 2018 年起担任副行长。央行利用利率调整和资产购买等工具来维持物价稳定并支持经济增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://www.ecb.europa.eu/">European Central Bank</a></li>
<li><a href="https://corporatefinanceinstitute.com/resources/economics/what-is-european-central-bank-ecb/">European Central Bank ( ECB ) - Overview, History, Roles</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#bonds`, `#currencies`

---

<a id="item-4"></a>
## [联合国警告中东战争影响下索马里面临饥荒风险](https://news.un.org/feed/view/en/story/2026/05/1167516) ⭐️ 7.0/10

联合国援助团队报告，由于中东战争的持续影响，至少 600 万索马里人连日缺乏足够食物，其中近 200 万幼儿面临患病或死亡的高风险。 该危机威胁地区稳定，可能引发大规模流离失所，并加剧本已不堪重负的国际援助体系压力，可能对大宗商品市场和捐助方优先事项产生溢出效应。 该警告强调五岁以下儿童最为脆弱，且地区冲突动态导致的供应链中断和人道主义准入减少进一步恶化了局势。

rss · UN News · May 15, 12:00

**背景**: 索马里长期面临周期性干旱、内部冲突和经济脆弱性，数百万人依赖人道主义援助。中东，尤其是也门和海湾国家，是索马里粮食进口和汇款的关键通道。该地区冲突升级可能推高全球粮食和燃料价格，扰乱航运路线，并转移国际捐助方对非洲之角的关注，从而加剧粮食不安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Middle_East_war">Middle East war</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#commodities`, `#geopolitics`, `#sovereign-risk`, `#supply-chain`

---

<a id="item-5"></a>
## [联合国驻黎部队警告无人机事件危及人员安全](https://news.un.org/feed/view/en/story/2026/05/1167496) ⭐️ 7.0/10

联合国驻黎巴嫩临时部队（联黎部队）警告称，近期其阵地附近涉及疑似真主党无人机和以色列军队的无人机活动及爆炸事件不断升级，危及维和人员安全，并威胁南黎巴嫩脆弱的稳定。 这一警告表明以色列与真主党之间的军事对抗风险上升，可能破坏停火协议，引发更广泛的地区冲突，并影响国际社会在黎巴嫩的维和努力。 联黎部队由 48 个国家约 8253 名人员组成，根据联合国安理会第 1701 号决议执行任务。该警告发布于 2024 年黎巴嫩战争停火后局势依然紧张的背景下。

rss · UN News · May 13, 12:00

**背景**: 联黎部队是根据 1978 年以色列入侵黎巴嫩后成立的联合国维和特派团，在 2006 年黎巴嫩战争后得到加强，负责监督停止敌对行动和蓝线边界。真主党是黎巴嫩什叶派政治和军事组织，被多国列为恐怖组织，多次与以色列发生冲突。2024 年黎巴嫩战争后虽达成停火，但双方紧张关系持续，黎巴嫩政府正推动真主党解除武装。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNIFIL">UNIFIL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`

---

<a id="item-6"></a>
## [拉加德呼吁建设持久韧性的欧洲](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260513_1~ab5ae9e754.en.html) ⭐️ 7.0/10

欧洲央行行长克里斯蒂娜·拉加德发表了题为《建设持久欧洲的勇气》的演讲，强调需要具有韧性的欧洲架构，可能预示着未来的政策方向。 她的言论可能影响市场对欧洲央行政策重点及欧洲经济一体化路径的预期，从而影响金融市场和投资者情绪。 演讲标题暗示要大胆迈向持久的欧洲架构，但可用的摘要中未透露具体政策提议或机构改革细节。

rss · ECB Press Releases · May 13, 19:50

**背景**: 克里斯蒂娜·拉加德自 2019 年起担任欧洲央行行长，经常谈及欧洲团结和经济韧性主题。欧洲央行在维持欧元区物价稳定方面发挥核心作用，其政策信号受到市场密切关注。近期欧洲面临财政协调、能源转型和地缘政治不确定性等挑战，使得拉加德对更持久欧洲的愿景尤为切题。

**标签**: `#central-bank`, `#europe`, `#macroeconomics`, `#financial-stability`, `#diplomacy`

---

<a id="item-7"></a>
## [欧洲央行莱恩分析能源供应冲击](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260513~5b14c78806.en.html) ⭐️ 7.0/10

2026 年 5 月 13 日，欧洲央行执行委员会成员菲利普·莱恩发表题为《能源供应冲击的分析视角》的演讲，阐述了央行对能源冲击如何推高通胀的看法。 该演讲揭示了欧洲央行对能源驱动型通胀的应对机制，可能影响货币政策预期和金融市场。 莱恩指出，全球性能源冲击会通过国际供应链产生复合价格效应，这与局部冲击不同。演讲可能借鉴了欧洲央行关于能源供应中断非线性影响的研究。

rss · ECB Press Releases · May 13, 19:00

**背景**: 欧洲央行负责欧元区货币政策，首要任务是维持物价稳定。能源供应冲击，如 2022 年俄罗斯入侵乌克兰后天然气价格飙升，可能严重扰乱通胀和经济活动。菲利普·莱恩作为欧洲央行重要决策者，经常就宏观经济和货币事务发表讲话。此次演讲基于欧洲央行此前关于能源冲击对产出和价格非对称影响的工作论文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp260513~5b14c78806.en.html">Analytical perspectives on energy supply shocks</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2834~db448f2eb2.en.pdf">Working Paper Series Energy supply shocks’ nonlinearities on output and prices</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#energy`, `#global-markets`, `#europe`

---

<a id="item-8"></a>
## [联合国报告：加沙、西岸和黎巴嫩平民苦难加剧](https://news.un.org/feed/view/en/story/2026/05/1167521) ⭐️ 6.0/10

联合国机构报告称，以色列在加沙、西岸和黎巴嫩的持续军事行动正加深平民苦难，造成人道主义援助压力增大，但未报告新的升级。 中东的持续动荡给地区外交、能源安全和全球供应链带来间接风险，可能对金融市场和地缘政治稳定产生溢出效应。 最新情况凸显了累积的人道主义压力和流离失所问题，OCHA 和 UNRWA 等援助机构面临资源有限；未宣布新的重大军事行动。

rss · UN News · May 15, 12:00

**背景**: 以色列与巴勒斯坦的冲突源于土地和自决权争议，导致数十年的占领和多次战争，包括 2023-2024 年的加沙战争。黎巴嫩真主党也与以色列长期敌对。联合国人道机构如 OCHA 和 UNRWA 负责协调受影响地区的救援工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Israeli-Palestinian_conflict">Israeli-Palestinian conflict</a></li>
<li><a href="https://en.wikipedia.org/wiki/Israel-Hezbollah_conflict">Israel-Hezbollah conflict</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Office_for_the_Coordination_of_Humanitarian_Affairs">United Nations Office for the Coordination of Humanitarian Affairs - Wikipedia</a></li>

</ul>
</details>

**标签**: `#military-risk`, `#middle-east`, `#diplomacy`, `#geopolitics`

---

<a id="item-9"></a>
## [也门换囚 1600 名被拘者将获释](https://news.un.org/feed/view/en/story/2026/05/1167511) ⭐️ 6.0/10

在联合国调解下，也门交战各方经过在约旦的数月谈判，同意释放超过 1600 名与冲突相关的被拘留者，这是内战以来规模最大的囚犯交换。 该协议是也门长期冲突中罕见的降级举措，可能为更广泛的和平谈判创造势头并改善人道主义状况，但对市场的直接影响有限。 该协议由联合国斡旋在约旦达成，涵盖冲突各方的被拘留者，但实施细节和时间表尚未公布。

rss · UN News · May 14, 12:00

**背景**: 也门内战始于 2014 年胡塞武装占领首都萨那，随后演变为地区代理人战争。联合国已多次调解谈判并促成过囚犯交换，但全面和平协议仍未达成。此次最大规模释放为停滞的和平进程带来新希望。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167511">Yemen parties agree under UN mediation to release 1,600 detainees | UN News</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-10"></a>
## [联合国官员：俄军袭击基辅平民明显违反国际人道法](https://news.un.org/feed/view/en/story/2026/05/1167509) ⭐️ 6.0/10

联合国驻乌克兰人道事务代理协调员贝尔纳黛特·卡斯特尔-霍林斯沃思强烈谴责俄军周四对基辅平民区的军事打击，称其明显违反国际人道法。 这一谴责可能加大对俄罗斯的外交压力，强化战争罪调查的呼声，并巩固国际社会对问责机制和制裁的支持。 袭击针对基辅平民区；联合国官员为代理人道事务协调员，事件发生在 2026 年 5 月的一个周四。

rss · UN News · May 14, 12:00

**背景**: 国际人道法在武装冲突中保护平民和民用物体，严重违反行为构成战争罪。联合国人道事务协调员负责协调人道主义应对并倡导平民保护。联合国经常就可能的违反国际人道法行为发表声明，以记录并呼吁遵守。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Humanitarian_law">Humanitarian law</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations">United Nations - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/War_crime">War crime</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#diplomacy`, `#military-risk`, `#europe`

---

<a id="item-11"></a>
## [古特雷斯敦促改革以增强非洲全球声音](https://news.un.org/feed/view/en/story/2026/05/1167503) ⭐️ 6.0/10

在亚的斯亚贝巴的非盟峰会上，联合国秘书长古特雷斯呼吁对全球机构进行彻底改革，指出许多非洲国家借贷成本高达基准利率的三倍且现有架构陈旧。他公开支持非洲开发银行主导的“新非洲金融架构”等非洲自主改革努力。 这一呼吁凸显了系统性金融不平等及争取更包容全球治理的努力，可能对主权债务动态、投资者信心和多边改革势头产生长期影响。若改革成功，可降低非洲国家借贷成本，将资源释放至卫生、教育和基础设施领域。 古特雷斯指出非洲借款人经常支付基准利率的三倍；他赞赏非洲开发银行联合非洲金融机构打造“新非洲金融架构”的倡议。峰会期间，联合国与非盟的战略伙伴关系得到重申。

rss · UN News · May 13, 12:00

**背景**: 国际货币基金组织和世界银行等全球金融机构长期因发展中国家代表性不足受批评。拥有 54 国的非洲投票权有限。信用评级和系统性偏见推高的主权借贷成本挤占了公共资源。非盟《2063 年议程》及非洲开发银行的“新非洲金融架构”等倡议旨在纠正这一失衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.globalissues.org/news/2026/05/13/43027">In Addis Ababa, Guterres urges reforms to give Africa stronger global voice — Global Issues</a></li>
<li><a href="https://news.un.org/en/story/2025/09/1165961">‘Africa’s voice is not heard’: Leaders issue call for equity, justice and courage | UN News</a></li>
<li><a href="https://commonslibrary.parliament.uk/research-briefings/cbp-10091/">Reforming global institutions: Africa's perspective - House of Commons Library</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#sovereign-risk`, `#financial-stability`, `#global-markets`

---

<a id="item-12"></a>
## [美联储任命鲍威尔为临时主席，等待沃什就职](https://www.federalreserve.gov/newsevents/pressreleases/other20260515a.htm) ⭐️ 6.0/10

2026 年 5 月 15 日，美联储理事会任命杰罗姆·鲍威尔为临时主席，直至新获参议院确认的凯文·沃什宣誓就任主席。 此次过渡表明美联储领导层即将更迭，市场预期沃什上任后可能采取更鹰派的货币政策立场，进而影响利率预期和金融市场。 参议院于 2026 年 5 月 13 日批准凯文·沃什担任主席，美联储表示任命临时主席符合领导层过渡期间的惯例。

rss · Federal Reserve Press Releases · May 15, 21:00

**背景**: 美联储主席领导美国中央银行制定货币政策。临时主席在正式主席任期结束而继任者尚未就职时任命。鲍威尔自 2018 年起担任主席。凯文·沃什曾于 2006 至 2011 年担任美联储理事，2026 年 1 月获特朗普总统提名，市场普遍认为其在对通胀问题上立场更偏鹰派。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.federalreserve.gov/newsevents/pressreleases/other20260515a.htm">Federal Reserve Board - Federal Reserve Board names Jerome H. Powell as chair pro tempore; Powell will serve as chair pro tempore until Kevin M. Warsh is sworn in as the new chair</a></li>
<li><a href="https://www.reuters.com/business/fed-names-powell-chair-pro-tempore-until-warsh-is-sworn-2026-05-15/">Fed names Powell as chair pro tempore until Warsh is sworn in | Reuters</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kevin_Warsh">Kevin Warsh - Wikipedia</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#monetary-policy`, `#united-states`

---

<a id="item-13"></a>
## [美联储发布 2025 年美国家庭经济福祉报告](https://www.federalreserve.gov/newsevents/pressreleases/other20260513a.htm) ⭐️ 6.0/10

美联储理事会发布了 2025 年度美国家庭经济福祉报告，提供了关于消费者财务健康、债务和储蓄的最新数据。 该报告是衡量消费者韧性和信贷风险的关键指标，可能影响美联储对经济状况的评估及未来货币政策决策。 该报告基于家庭经济与决策调查（SHED），涵盖收入稳定性、紧急储蓄以及应对意外开支能力等指标。

rss · Federal Reserve Press Releases · May 13, 15:30

**背景**: 美联储理事会监管美国中央银行系统并实施货币政策。其年度家庭经济与决策调查（SHED）提供了美国家庭财务福祉的洞察，补充了其他经济数据。该报告通常会影响政策制定者对消费者支出和信贷状况的看法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Reserve_Board_of_Governors">Federal Reserve Board of Governors</a></li>
<li><a href="https://en.wikipedia.org/wiki/Monetary_policy">Monetary policy</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#financial-stability`, `#united-states`

---