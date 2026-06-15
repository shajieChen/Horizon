---
layout: default
title: "Horizon Summary: 2026-06-16 (ZH)"
date: 2026-06-16
lang: zh
---

> From 42 items, 13 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [古特雷斯欢迎美伊和平协议，称其为结束冲突的关键一步](#item-2) ⭐️ 10.0/10
3. [美伊和平协议待签之际，联合国呼吁开放霍尔木兹援助走廊](#item-3) ⭐️ 9.0/10
4. [联合国对美伊可能停火的消息表示鼓舞](#item-4) ⭐️ 9.0/10
5. [霍尔木兹海峡油轮遇袭致三名海员死亡，联合国警告影响扩大](#item-5) ⭐️ 9.0/10
6. [欧央行公布货币政策决议与前瞻指引](#item-6) ⭐️ 9.0/10
7. [俄军袭击乌克兰致平民死亡、文化遗产受损](#item-7) ⭐️ 8.0/10
8. [安理会辩论中东政治解决方案 美伊停火仍脆弱](#item-8) ⭐️ 8.0/10
9. [联合国报告黎巴嫩医院遭袭，人道危机加剧](#item-9) ⭐️ 7.0/10
10. [五月乌克兰平民伤亡创四年新高](#item-10) ⭐️ 7.0/10
11. [联合国：黎巴嫩建筑损失逾 3.65 亿美元，提尔空袭再致八死](#item-11) ⭐️ 7.0/10
12. [欧洲央行行长拉加德探讨货币未来与数字欧元](#item-12) ⭐️ 6.0/10
13. [欧央行执委埃尔德森谈论政策与气候风险](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 15, 23:01

**Trading Analysis**

> 分析方法：digital-oracle multi-signal synthesis  
> 分析范围：QDII 纳斯达克 100 / 海外股票 / 美国股票 / 日本股票 / 香港股票  
> 时间维度：1日 / 1周 / 1月  
> 数据原则：仅使用市场交易数据，不使用新闻观点或分析师观点  
> 可追溯性：结构化 provider 数据 + WebSearch 市场数据引用，参考文章列于报告末尾。  
> 免责声明：本分析仅基于市场数据进行概率估算，不构成投资建议。市场存在不确定性，请独立判断并承担相应风险。

> 数据状态：部分市场数据暂不可用，已采用保守基准概率估计。

### 资产概率总览 (Asset Probability Overview)

| 资产 | 市场 | 1日 | 1周 | 1月 | 数据质量 |
|---|---|---|---|---|---|
| QDII Nasdaq 100 Proxy | US | bullish 38/31/31 | bullish 38/31/31 | bullish 39/30/31 | high |
| US Mega Cap Basket | US | bullish 38/31/31 | neutral 33/33/34 | neutral 33/33/34 | high |
| Japan Equity Basket | JP | bullish 38/31/31 | bullish 38/31/31 | bullish 39/30/31 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=30798.75; 1d=+3.83%; 5d=+4.56%; 20d=+5.36% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=744.00; 1d=+3.14%; 5d=+3.90%; 20d=+4.95% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=30543.92; 1d=+3.06%; 5d=+3.84%; 20d=+4.87% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=1.6%; implied_move=0.0%; put/call OI=2.51701100530408 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.47; 2Y=4.07; 10Y-2Y=0.39999999999999947 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=40.9; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：1日篮子收益与5日均线结构偏强
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | high |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | high |
| 1月 | 39% | 30% | 31% | bullish | 20日趋势维持上行，1月窗口偏多 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| NQ=F price trend | close=30798.75; 1d=+3.83%; 5d=+4.56%; 20d=+5.36% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=744.00; 1d=+3.14%; 5d=+3.90%; 20d=+4.95% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=30543.92; 1d=+3.06%; 5d=+3.84%; 20d=+4.87% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| MSFT price trend | close=399.76; 1d=+2.31%; 5d=-2.91%; 20d=-5.05% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=593.48; 1d=+4.67%; 5d=+1.38%; 20d=-3.38% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=369.35; 1d=+2.69%; 5d=+1.66%; 20d=-6.86% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=296.42; 1d=+1.82%; 5d=-1.70%; 20d=-1.27% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=212.45; 1d=+3.54%; 5d=+1.83%; 20d=-5.60% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=411.15; 1d=+1.16%; 5d=+0.54%; 20d=-2.63% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| META options surface | ATM IV=5.2%; implied_move=0.2%; put/call OI=0.5733163181294253 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=8.2%; implied_move=0.4%; put/call OI=0.531509197196462 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=5.0%; implied_move=0.3%; put/call OI=0.6993772624863934 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=2.3%; implied_move=0.1%; put/call OI=0.7706280103742127 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=6.1%; implied_move=0.2%; put/call OI=0.45468783588735684 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=8.1%; implied_move=0.3%; put/call OI=0.6600749580826512 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=40.9; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| NVDA insider filings | recent Form4 count=561 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.47; 2Y=4.07; 10Y-2Y=0.39999999999999947 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：1日篮子收益与5日均线结构偏强
- 1周：有效交易信号不足，使用保守基准分布。
- 1月：有效交易信号不足，使用保守基准分布。

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | high |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1月 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| MSFT price trend | close=399.76; 1d=+2.31%; 5d=-2.91%; 20d=-5.05% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=593.48; 1d=+4.67%; 5d=+1.38%; 20d=-3.38% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=369.35; 1d=+2.69%; 5d=+1.66%; 20d=-6.86% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 8035.T price trend | close=72760.00; 1d=+7.00%; 5d=+32.24%; 20d=+47.71% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7139.00; 1d=+10.31%; 5d=+2.34%; 20d=+27.64% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3320.00; 1d=+0.85%; 5d=-5.36%; 20d=-7.68% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=75650.00; 1d=+4.17%; 5d=+0.89%; 20d=-1.54% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2902.50; 1d=+4.58%; 5d=+2.83%; 20d=-1.76% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=94.06; 1d=+1.46%; 5d=+2.29%; 20d=+3.28% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.47; 2Y=4.07; 10Y-2Y=0.39999999999999947 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=40.9; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 跨层分歧信息有限，后续需补充更多波动与事件市场数据。

**Time stratification**
- 1日：1日篮子收益与5日均线结构偏强
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | medium |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | medium |
| 1月 | 39% | 30% | 31% | bullish | 20日趋势维持上行，1月窗口偏多 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 8035.T price trend | close=72760.00; 1d=+7.00%; 5d=+32.24%; 20d=+47.71% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7139.00; 1d=+10.31%; 5d=+2.34%; 20d=+27.64% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3320.00; 1d=+0.85%; 5d=-5.36%; 20d=-7.68% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| EWH price trend | close=21.87; 1d=-0.59%; 5d=+0.09%; 20d=-9.10% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=78.25; 1d=+0.45%; 5d=+2.62%; 20d=-5.38% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=112.50; 1d=-0.09%; 5d=-0.88%; 20d=-12.04% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=26.26; 1d=+0.23%; 5d=-4.09%; 20d=-14.46% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=459.60; 1d=-0.86%; 5d=+2.96%; 20d=+0.70% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.62; 1d=+0.49%; 5d=+1.91%; 20d=-5.50% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.47; 2Y=4.07; 10Y-2Y=0.39999999999999947 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=40.9; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| EWH price trend | close=21.87; 1d=-0.59%; 5d=+0.09%; 20d=-9.10% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=78.25; 1d=+0.45%; 5d=+2.62%; 20d=-5.38% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=112.50; 1d=-0.09%; 5d=-0.88%; 20d=-12.04% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Volatility Term Structure chart plots the at-the-money implied volatility across expirations, which are an invaluable tool in determining options strategies based on anticipated...

- [Volatility NASDAQ - 100 (NASDAQVOLNDX) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/NASDAQVOLNDX)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Graph and download economic data for Volatility NASDAQ - 100 (NASDAQVOLNDX) from 2010-07-23 to 2026-01-16 about volatility, NASDAQ, indexes, and USA.

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [Move Index Chart - Barchart.com](https://www.barchart.com/stocks/quotes/$MOVE/interactive-chart)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Customizable interactive chart for Move Index with latest real-time price quote, charts, latest news, technical analysis and opinions.

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [BAMLH0A0HYM2: US High Yield OAS Daily Data - eco3min.fr](https://eco3min.fr/en/credit-spreads-recession-risk-dataset/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：BAMLH0A0HYM2 is the ICE BofA US High Yield Index Option-Adjusted Spread — the daily market-priced premium that below-investment-grade US corporate bonds pay over equivalent-matu...

- [US High Yield Master II Option-Adjusted Spread (Market Dail…](https://ycharts.com/indicators/us_high_yield_master_ii_optionadjusted_spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：View market daily updates and historical trends for US High Yield Master II Option-Adjusted Spread. from United States. Source: Bank of America Merrill Ly…

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [Invesco QQQ (QQQ) - Implied Volatility (Mean) (30-Day) - AlphaQuery](https://www.alphaquery.com/stock/QQQ/volatility-option-statistics/30-day/iv-mean)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Implied Volatility (Mean): The forecasted future volatility of the security over the selected time frame, derived from the average of the put and call implied volatilities for o...

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [iShares MSCI Japan ETF / EWJ](https://www.ishares.com/us/products/239665/ishares-msci-japan-etf)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：The iShares MSCI Japan ETF seeks to track an index composed of Japanese equities. The fund offers a way to express a single-country view and gain targeted exposure to companies...

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [USD/JPY (JPY=X) Live Rate, Chart & News - Yahoo Finance](https://finance.yahoo.com/quote/JPY=X/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Find the latest USD/JPY currency exchange rate, historical data, charts, and relevant news for informed trading and investing.

- [Live US Dollar to Yens Exchange Rate - $ 1 USD/JPY Today](https://usd.currencyrate.today/jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest and best $1 US Dollar to Yens rate for FREE. USD/JPY - Live exchange rates, banks, historical data & currency charts.

- [USD to JPY / Convert Live / Exchange Rates UK](https://www.exchangerates.org.uk/Dollars-to-Yen-currency-conversion-page.html)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：To convert Dollars to Yen or determine the Dollar Yen exchange rate simply use the currency converter on the right of this page, which offers fast live exchange rate conversions...

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
## [古特雷斯欢迎美伊和平协议，称其为结束冲突的关键一步](https://news.un.org/feed/view/en/story/2026/06/1167716) ⭐️ 10.0/10

联合国秘书长安东尼奥·古特雷斯公开支持美伊之间达成的和平协议，称这是结束敌对行动、重塑地区格局的关键举措。 该协议标志着长期对手之间的历史性和解，可能解除经济制裁，从而提振伊朗石油出口、缓解全球能源价格，同时减少中东军事对抗的风险。 协议细节尚未公布，但有报道称这可能是一个临时框架，设有 60 天期限以达成全面核协议，制裁解除与双方履约情况挂钩。

rss · UN News · Jun 14, 12:00

**背景**: 联合国长期寻求调解美伊关系。自 2018 年美国退出伊核协议并实施严厉制裁以来，两国关系恶化。伊朗石油出口锐减，引发全球供应担忧。此次和平协议是在多年紧张局势和代理人冲突后取得的潜在突破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations">United Nations - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/2025–2026_Iran–United_States_negotiations">2025-2026 Iran-United States negotiations - Wikipedia</a></li>
<li><a href="https://www.atlanticcouncil.org/dispatches/experts-react-the-us-and-iran-just-announced-an-interim-peace-deal-heres-what-we-know-so-far/">Experts react: The US and Iran just announced an interim peace deal ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#middle-east`, `#sanctions`

---

<a id="item-3"></a>
## [美伊和平协议待签之际，联合国呼吁开放霍尔木兹援助走廊](https://news.un.org/feed/view/en/story/2026/06/1167717) ⭐️ 9.0/10

据报道，伊朗和美国即将签署和平协议。与此同时，联合国紧急呼吁在霍尔木兹海峡开通援助走廊，以防止全球饥饿危机。 美伊协议若达成，可能解除制裁，缓和海湾地区紧张局势，稳定石油市场；联合国的呼吁凸显了海峡封锁对人道主义和供应链的严重危机。 伊朗革命卫队于 2026 年 3 月关闭了霍尔木兹海峡，每日约 2000 万桶石油运输受阻；据报，即将达成的和平协议不包括限制弹道导弹，也未要求政权更迭。

rss · UN News · Jun 15, 12:00

**背景**: 霍尔木兹海峡是全球最重要的石油运输咽喉，约占全球石油运输量的 20%。2025 年以来，伊朗与美国在紧张局势升级和短暂战争后进行了多轮艰难谈判。海上封锁和制裁加剧了人道主义危机，联合国依据国际人道法呼吁设立安全走廊以转运援助物资。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/world/2026/jun/15/analysis-us-iran-peace-deal-shipping-sanctions-relief-nuclear-talks-ballistic-missiles">US-Iran peace deal hinges on shipping, sanctions relief and deferred nuclear talks | US-Israel war on Iran | The Guardian</a></li>
<li><a href="https://en.wikipedia.org/wiki/Humanitarian_corridor">Humanitarian corridor - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#sanctions`, `#energy`, `#supply-chain`

---

<a id="item-4"></a>
## [联合国对美伊可能停火的消息表示鼓舞](https://news.un.org/feed/view/en/story/2026/06/1167713) ⭐️ 9.0/10

联合国发言人表示，该组织对有关美国与伊朗可能达成停火协议的报道感到“鼓舞”，但同时指出这些报道相互矛盾。 停火将极大缓解中东地区的紧张局势，降低全球能源供应和航运路线的风险，并可能带来制裁放松和市场情绪改善。 相关报道未经证实且相互矛盾，联合国正在继续关注事态发展。截至联合国简报时，华盛顿和德黑兰均未发表官方声明。

rss · UN News · Jun 12, 12:00

**背景**: 自 2018 年美国退出 2015 年伊朗核协议（JCPOA）并重新实施制裁以来，美伊关系一直紧张。2025 至 2026 年间，紧张局势升级，双方发生军事打击，并危及关键的能源咽喉霍尔木兹海峡。此前的停火尝试或被拒绝，或未得到证实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2025–2026_Iran–United_States_negotiations">2025–2026 Iran–United States negotiations - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Iran_nuclear_deal">Iran nuclear deal - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#united-states`, `#energy`

---

<a id="item-5"></a>
## [霍尔木兹海峡油轮遇袭致三名海员死亡，联合国警告影响扩大](https://news.un.org/feed/view/en/story/2026/06/1167697) ⭐️ 9.0/10

周三，一艘油轮在霍尔木兹海峡附近遇袭，造成三名印度海员死亡。联合国警告称，该事件可能加剧燃料价格上涨、威胁粮食安全并扰乱全球供应链。 这场针对关键石油运输咽喉要道的袭击引发了人们对更大范围地区冲突的担忧，直接威胁到全球能源供应，并可能引发燃料价格急剧上涨。它还加剧了本已存在的粮食安全和供应链脆弱性，影响全球经济。 霍尔木兹海峡承担着全球约 20%的石油贸易，此次袭击发生前，伊朗曾在 2026 年 3 月威胁关闭该水道。遇难海员为印度籍，凸显了不断升级的军事紧张局势下的人员代价。

rss · UN News · Jun 11, 12:00

**背景**: 霍尔木兹海峡是位于伊朗和阿曼之间的狭窄水道，被认为是全球最重要的石油运输咽喉。每天约有 2000 万桶石油（约占全球供应量的 20%）经过此地。2026 年的危机始于伊朗宣布关闭该海峡并威胁袭击过往船只，尽管后来对“友好”国家的船只开了特例。此类中断历来会导致油价迅速飙升和全球贸易动荡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis">2026 Strait of Hormuz crisis - Wikipedia</a></li>
<li><a href="https://www.eia.gov/todayinenergy/detail.php?id=65504">Amid regional conflict, the Strait of Hormuz remains critical oil chokepoint - U.S. Energy Information Administration (EIA)</a></li>
<li><a href="https://autozealot.com/strait-of-hormuz-chaos-how-the-iran-conflict-is-hammering-fuel-costs/">Iran War Tanker Attacks Spike Gas Prices: Off-Road Impact</a></li>

</ul>
</details>

**标签**: `#military-risk`, `#energy`, `#supply-chain`, `#middle-east`, `#global-markets`

---

<a id="item-6"></a>
## [欧央行公布货币政策决议与前瞻指引](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html) ⭐️ 9.0/10

2026 年 6 月 11 日，欧洲央行公布了其最新货币政策决议，调整了关键利率并更新了前瞻指引，以应对不断变化的经济形势。 该决议直接影响欧元区的借贷成本、欧元汇率和金融环境，并对全球债券和股票市场产生重大的溢出效应。 市场参与者将仔细研读政策声明和行长拉加德的新闻发布会，关注通胀预测、增长评估的任何变化以及未来利率路径的信号。

rss · ECB Press Releases · Jun 11, 12:15

**背景**: 欧洲央行是欧元的中央银行，负责为采用欧元的 20 个国家制定货币政策。其主要任务是维持物价稳定，中期通胀目标为 2%。欧洲央行管理委员会大约每六周召开一次会议，决定利率和其他政策工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank - Wikipedia</a></li>
<li><a href="https://www.ecb.europa.eu/ecb/orga/escb/html/index.en.html">ECB, ESCB and the Eurosystem - European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#currencies`, `#bonds`

---

<a id="item-7"></a>
## [俄军袭击乌克兰致平民死亡、文化遗产受损](https://news.un.org/feed/view/en/story/2026/06/1167718) ⭐️ 8.0/10

联合国周一表示，俄罗斯对基辅和哈尔科夫的夜间袭击导致数名平民死亡、数十人受伤，并破坏了文化遗产。 此次袭击可能加剧国际社会对俄罗斯的谴责，引发新制裁，并加大对西方盟友提升对乌克兰军事援助的压力。 联合国周一声明指出基辅和哈尔科夫出现平民伤亡及文化遗产破坏，但未公布确切数字或受损地标名称。

rss · UN News · Jun 15, 12:00

**背景**: 俄罗斯于 2022 年 2 月发动对乌克兰的全面入侵。俄军屡次袭击乌克兰城市，造成平民伤亡与财产损失。根据国际人道法，文化财产应受保护，蓄意攻击可能构成战争罪。联合国经常谴责此类事件。

**标签**: `#russia-ukraine`, `#military-risk`, `#diplomacy`, `#geopolitics`, `#europe`

---

<a id="item-8"></a>
## [安理会辩论中东政治解决方案 美伊停火仍脆弱](https://news.un.org/feed/view/en/story/2026/06/1167689) ⭐️ 8.0/10

联合国安理会周三就推进中东政治解决方案举行高级别辩论，联合国秘书长警告称，在美伊脆弱停火之际，局势升级正跨越国界和大陆蔓延。 此次辩论凸显外交风险之高；美伊停火一旦破裂可能重新引发冲突，扰乱全球能源市场与地区安全。 由巴基斯坦斡旋的停火协议包括暂停美以对伊朗攻击两周、美国放松制裁以及重新开放霍尔木兹海峡，但执行依然脆弱。

rss · UN News · Jun 10, 12:00

**背景**: 联合国安理会负责维护国际和平与安全。2026 年伊朗战争于 2026 年 2 月因美以军事打击爆发，扰乱了霍尔木兹海峡的石油运输。在巴基斯坦调解下，冲突持续 40 天后于 2026 年 4 月达成停火，但紧张局势持续。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aljazeera.com/news/2026/4/8/us-iran-ceasefire-deal-what-are-the-terms-and-whats-next">US - Iran ceasefire deal: What are the terms, and... | Al Jazeera</a></li>
<li><a href="https://www.bbc.com/news/live/cj0grpyg4v1t">Iran and US agree deal to end war as Israel says its... - BBC News</a></li>
<li><a href="https://main.un.org/securitycouncil/en">Homepage | Security Council</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#iran`, `#energy`

---

<a id="item-9"></a>
## [联合国报告黎巴嫩医院遭袭，人道危机加剧](https://news.un.org/feed/view/en/story/2026/06/1167714) ⭐️ 7.0/10

联合国报告称，以色列与真主党之间的持续敌对行动越来越多地针对黎巴嫩的医疗设施，最近的空袭破坏了医院并中断了基本医疗服务。 针对医疗基础设施的攻击加剧了人道危机，增加了地区不稳定的风险，并可能引发联合国安理会干预或制裁讨论，从而影响能源市场。 尽管 2024 年黎巴嫩战争后达成了停火协议，敌对行动仍在继续，医院遭袭凸显了休战的脆弱性；黎巴嫩政府最近批准了解除真主党武装的路线图，但执行情况尚不明朗。

rss · UN News · Jun 12, 12:00

**背景**: 真主党是黎巴嫩什叶派伊斯兰武装组织兼政党，与伊朗关系密切。自 1980 年代成立以来，一直与以色列长期冲突，包括 2006 年战争以及最近 2023-2024 年升级为全面战争并随后停火。黎巴嫩本已深陷严重的经济危机和政治动荡，冲突使该国人道主义紧急情况雪上加霜。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://en.wikipedia.org/wiki/Israeli-Hezbollah_conflict">Israeli-Hezbollah conflict</a></li>
<li><a href="https://www.iom.int/lebanon-humanitarian-crisis">Lebanon Humanitarian Crisis | International Organization for Migration</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`, `#energy`

---

<a id="item-10"></a>
## [五月乌克兰平民伤亡创四年新高](https://news.un.org/feed/view/en/story/2026/06/1167707) ⭐️ 7.0/10

联合国调查人员报告称，2026 年 5 月乌克兰平民伤亡总数达到过去四年来的月度最高水平。 平民伤亡激增表明冲突加剧，可能促使国际社会加大停火谈判压力，影响外交关系及全球能源和粮食市场。 自 2014 年起追踪伤亡情况的联合国乌克兰人权监测团指出，五月的伤亡是 2022 年战事升级以来的最高值；最新报告未提供具体伤亡数字。

rss · UN News · Jun 12, 12:00

**背景**: 联合国乌克兰人权监测团（HRMMU）于 2014 年应乌克兰政府邀请部署，旨在监测俄乌冲突期间的人权状况。该团定期发布平民伤亡更新。“四年”的参照点可追溯至 2022 年 5 月，即俄罗斯全面入侵开始后不久，当时伤亡人数曾急剧攀升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Human_Rights_Monitoring_Mission_in_Ukraine">UN Human Rights Monitoring Mission in Ukraine</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#geopolitics`, `#military-risk`, `#europe`, `#humanitarian`

---

<a id="item-11"></a>
## [联合国：黎巴嫩建筑损失逾 3.65 亿美元，提尔空袭再致八死](https://news.un.org/feed/view/en/story/2026/06/1167685) ⭐️ 7.0/10

联合国牵头的一项快速损失评估估计贝鲁特和黎巴嫩山地区建筑损失超过 3.65 亿美元，同时对提尔的新空袭造成至少八人死亡，违反了脆弱的停火协议。 不断升级的违规和破坏凸显了全面冲突再起的风险，威胁地区稳定，加重人道主义压力，并可能引来外部势力干预。 评估覆盖了 2026 年 2 月至 4 月期间 146 栋被毁和 264 栋部分受损的建筑，瓦砾量达 648,942 立方米。自 2024 年 11 月生效以来，停火协议屡遭双方违反。

rss · UN News · Jun 9, 12:00

**背景**: 2024 年由美国等国家斡旋的停火协议，旨在结束自 2023 年 10 月哈马斯袭击后以色列与真主党之间长达一年多的敌对行动。以色列于 2024 年 10 月入侵黎巴嫩，已造成数千人死亡。联合国一直在协调人道主义和重建工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167685">Fresh strikes on Tyre kill eight, as UN puts Lebanon destruction bill at $365 million, and rising | UN News</a></li>
<li><a href="https://www.undp.org/arab-states/press-releases/rapid-damage-assessment-estimates-over-us365-million-building-damage-across-beirut-and-mount-lebanon">Rapid damage assessment estimates over US$365 Million in building damage across Beirut and Mount Lebanon | United Nations Development Programme</a></li>
<li><a href="https://en.wikipedia.org/wiki/2024_Israel–Lebanon_ceasefire_agreement">2024 Israel– Lebanon ceasefire agreement - Wikipedia</a></li>

</ul>
</details>

**标签**: `#lebanon`, `#ceasefire`, `#military-risk`, `#middle-east`, `#diplomacy`

---

<a id="item-12"></a>
## [欧洲央行行长拉加德探讨货币未来与数字欧元](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260615~35e6c6c4de.en.html) ⭐️ 6.0/10

欧洲央行行长克里斯蒂娜·拉加德于 2026 年 6 月 15 日发表了题为‘转型中的货币’的演讲，阐述了欧洲央行对央行数字货币和货币演变的最新思考。 此次演讲标志着欧洲央行在数字欧元上的战略方向，这可能重塑欧元区的支付体系、货币政策传导和金融稳定，影响银行、消费者和企业。 未提供具体推出时间表，但拉加德强调了隐私保障和商业银行公平竞争环境的必要性。

rss · ECB Press Releases · Jun 15, 07:30

**背景**: 欧洲央行自 2020 年起研究数字欧元，2021 年启动正式调查阶段，2023 年开始准备阶段。最终发行决定取决于立法审批和技术准备。拉加德此前曾强调央行货币在日益数字化的经济中的重要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/">European Central Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/Central_bank_digital_currency">Central bank digital currency</a></li>
<li><a href="https://en.wikipedia.org/wiki/Christine_Lagarde">Christine Lagarde</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#financial-stability`, `#europe`, `#global-markets`

---

<a id="item-13"></a>
## [欧央行执委埃尔德森谈论政策与气候风险](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260610~439aa97519.en.html) ⭐️ 6.0/10

欧央行执委会成员弗兰克·埃尔德森接受《荷兰金融日报》采访，讨论了货币政策展望、金融稳定和气候相关的银行监管。 他的言论可能预示欧元区货币政策的变化，或透露新的气候相关金融监管信息，从而影响市场和银行业。 采访未确认具体政策变动，但作为欧央行的常规沟通，需关注是否有前瞻性指引或气候压力测试的更新。

rss · ECB Press Releases · Jun 10, 14:00

**背景**: 弗兰克·埃尔德森是欧央行执委会成员兼监事会副主席，负责银行监管，并领导欧央行的气候变化中心。总部位于法兰克福的欧洲央行制定欧元区货币政策，并通过压力测试确保金融稳定。他接受荷兰金融报纸的采访，可能讨论了通胀和荷兰及更广泛经济前景的关切。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://www.ecb.europa.eu/">European Central Bank</a></li>
<li><a href="https://corporatefinanceinstitute.com/resources/economics/what-is-european-central-bank-ecb/">European Central Bank ( ECB ) - Overview, History, Roles</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#financial-stability`, `#global-markets`

---