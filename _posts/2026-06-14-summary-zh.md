---
layout: default
title: "Horizon Summary: 2026-06-14 (ZH)"
date: 2026-06-14
lang: zh
---

> From 41 items, 11 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [霍尔木兹海峡油轮遇袭致三人死亡，联合国警告供应链冲击](#item-2) ⭐️ 9.0/10
3. [欧洲央行货币政策声明及拉加德与武伊奇新闻发布会](#item-3) ⭐️ 9.0/10
4. [联合国对美伊可能停火协议表示鼓舞](#item-4) ⭐️ 8.0/10
5. [联合国警告乌克兰战争处于 2022 年以来最致命阶段](#item-5) ⭐️ 8.0/10
6. [黎巴嫩医院遭袭，人道状况恶化](#item-6) ⭐️ 7.0/10
7. [联合国称 5 月乌克兰平民伤亡创四年新高](#item-7) ⭐️ 7.0/10
8. [安理会辩论中东政治方案，联合国秘书长警告升级影响全球](#item-8) ⭐️ 7.0/10
9. [黎巴嫩提尔遭袭致 8 死，联合国估算损失超 3.65 亿美元](#item-9) ⭐️ 7.0/10
10. [联合国报告：巴勒斯坦人遭定居者和哈马斯系统虐待](#item-10) ⭐️ 6.0/10
11. [欧央行执委埃尔德森接受荷兰财经日报采访](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 13, 22:41

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
| QDII Nasdaq 100 Proxy | US | bullish 38/31/31 | neutral 33/33/34 | neutral 33/33/34 | high |
| US Mega Cap Basket | US | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | high |
| Japan Equity Basket | JP | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |
| Hong Kong Equity Basket | HK | bullish 38/31/31 | neutral 33/33/34 | neutral 33/33/34 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=29662.00; 1d=+0.67%; 5d=+2.19%; 20d=-0.09% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=721.34; 1d=+0.59%; 5d=+2.31%; 20d=+0.22% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29635.95; 1d=+0.64%; 5d=+2.34%; 20d=+0.19% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=20.0%; implied_move=1.4%; put/call OI=1.842459555799287 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.48; 2Y=4.09; 10Y-2Y=0.39000000000000057 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=34.0; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| NQ=F price trend | close=29662.00; 1d=+0.67%; 5d=+2.19%; 20d=-0.09% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=721.34; 1d=+0.59%; 5d=+2.31%; 20d=+0.22% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29635.95; 1d=+0.64%; 5d=+2.34%; 20d=+0.19% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| TSLA price trend | close=406.43; 1d=+1.82%; 5d=+3.95%; 20d=-8.32% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=238.55; 1d=-1.23%; 5d=-3.04%; 20d=-10.73% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=359.68; 1d=+0.53%; 5d=-2.34%; 20d=-10.27% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=291.13; 1d=-1.52%; 5d=-5.27%; 20d=-2.37% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=205.19; 1d=+0.16%; 5d=+0.04%; 20d=-12.86% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=390.74; 1d=+0.10%; 5d=-6.22%; 20d=-4.36% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| NVDA options surface | ATM IV=27.1%; implied_move=1.9%; put/call OI=0.7887573324683048 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=25.1%; implied_move=1.8%; put/call OI=0.3819433391691867 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=26.7%; implied_move=1.9%; put/call OI=0.736036997509783 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=26.4%; implied_move=1.9%; put/call OI=0.47175863278704955 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=46.1%; implied_move=3.3%; put/call OI=0.6420545746388443 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=18.7%; implied_move=1.3%; put/call OI=0.41203978814106706 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| NVDA insider filings | recent Form4 count=561 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| CNN Fear & Greed | score=34.0; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| MSFT insider filings | recent Form4 count=736 | 内部人交易节奏可作为估值温度辅助校验信号。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：有效交易信号不足，使用保守基准分布。
- 1月：有效交易信号不足，使用保守基准分布。

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1月 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| TSLA price trend | close=406.43; 1d=+1.82%; 5d=+3.95%; 20d=-8.32% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=238.55; 1d=-1.23%; 5d=-3.04%; 20d=-10.73% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=359.68; 1d=+0.53%; 5d=-2.34%; 20d=-10.27% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| EWJ price trend | close=92.71; 1d=+0.57%; 5d=+2.19%; 20d=+0.71% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=72620.00; 1d=+1.89%; 5d=-6.98%; 20d=-5.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2775.50; 1d=+1.02%; 5d=-2.61%; 20d=-10.03% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3292.00; 1d=-2.29%; 5d=-7.50%; 20d=-7.94% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=68000.00; 1d=+7.26%; 5d=+14.38%; 20d=+35.22% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6472.00; 1d=+1.54%; 5d=-12.85%; 20d=+12.65% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.48; 2Y=4.09; 10Y-2Y=0.39000000000000057 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=34.0; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| EWJ price trend | close=92.71; 1d=+0.57%; 5d=+2.19%; 20d=+0.71% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=72620.00; 1d=+1.89%; 5d=-6.98%; 20d=-5.91% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2775.50; 1d=+1.02%; 5d=-2.61%; 20d=-10.03% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9618.HK price trend | close=112.60; 1d=+3.40%; 5d=-2.76%; 20d=-13.45% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=110.20; 1d=+2.61%; 5d=-9.87%; 20d=-20.00% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.49; 1d=-0.30%; 5d=+0.42%; 20d=-9.28% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=77.90; 1d=-0.26%; 5d=-2.56%; 20d=-9.10% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=26.20; 1d=+1.39%; 5d=-5.76%; 20d=-17.40% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=35.29; 1d=+1.09%; 5d=+1.55%; 20d=-5.24% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.48; 2Y=4.09; 10Y-2Y=0.39000000000000057 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=34.0; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 跨层分歧信息有限，后续需补充更多波动与事件市场数据。

**Time stratification**
- 1日：1日篮子收益与5日均线结构偏强
- 1周：有效交易信号不足，使用保守基准分布。
- 1月：有效交易信号不足，使用保守基准分布。

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | medium |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1月 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 9618.HK price trend | close=112.60; 1d=+3.40%; 5d=-2.76%; 20d=-13.45% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=110.20; 1d=+2.61%; 5d=-9.87%; 20d=-20.00% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.49; 1d=-0.30%; 5d=+0.42%; 20d=-9.28% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [CBOE NASDAQ 100 Volatility Index - FRED / St. Louis Fed](https://fred.stlouisfed.org/series/VXNCLS)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Graph and download economic data for CBOE NASDAQ 100 Volatility Index (VXNCLS) from 2001-02-02 to 2026-06-11 about VIX, volatility, stock market, and USA.

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Volatility Term Structure chart plots the at-the-money implied volatility across expirations, which are an invaluable tool in determining options strategies based on anticipated...

- [Volatility NASDAQ - 100 (NASDAQVOLNDX) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/NASDAQVOLNDX)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Graph and download economic data for Volatility NASDAQ - 100 (NASDAQVOLNDX) from 2010-07-23 to 2026-01-16 about volatility, NASDAQ, indexes, and USA.

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

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [QQQ Options Volatility — NASDAQ:QQQ — TradingView](https://www.tradingview.com/symbols/NASDAQ-QQQ/options-volatility/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Analyze Invesco QQQ Trust, Series 1 puts and calls to craft a reliable strategy and optimize your options trading with implied volatility charts.

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [iShares MSCI Japan ETF / EWJ](https://www.ishares.com/us/products/239665/ishares-msci-japan-etf)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：The iShares MSCI Japan ETF seeks to track an index composed of Japanese equities. The fund offers a way to express a single-country view and gain targeted exposure to companies...

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Current Values - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index?idx=nk225)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Current Values Nikkei calculates and publishes various types of the indexes such as the "Nikkei Stock Average (Nikkei 225)" which is known as a representative Japanese stock mar...

- [Nikkei Average Volatility (^NKVI.OS) - Yahoo Finance](https://finance.yahoo.com/quote/%5ENKVI.OS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Find the latest information on Nikkei Average Volatility (^NKVI.OS) including data, charts, related news and more from Yahoo Finance

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
## [霍尔木兹海峡油轮遇袭致三人死亡，联合国警告供应链冲击](https://news.un.org/feed/view/en/story/2026/06/1167697) ⭐️ 9.0/10

周三，一艘油轮在霍尔木兹海峡附近遭袭，导致三名印度籍海员死亡，这标志着这条关键能源航运咽喉要道的冲突致命升级。联合国警告称，粮食安全、燃料价格和全球供应链面临的风险正在扩大。 霍尔木兹海峡承载着全球约 20%的石油贸易，该地区的不稳定直接威胁能源市场、保险成本和航运路线。此次袭击可能引发油价飙升、军事回应以及中东更广泛的地缘政治紧张局势。 遇难者为印度籍，事件发生在全球最重要航运通道之一的敌对行动重新抬头之际。联合国特别强调了粮食安全和断链风险，但袭击者身份等细节仍不清楚。

rss · UN News · Jun 11, 12:00

**背景**: 霍尔木兹海峡连接波斯湾与阿曼湾和阿拉伯海，是全球最重要的石油运输咽喉。该地区历史上的干扰或袭击曾导致原油价格和航运保险费飙升。伊朗、阿曼和阿联酋濒临该海峡，地区大国或非国家行为体之间的紧张关系常常通过海上事件体现。联合国通常会发出此类警告，以推动国际外交努力，并减轻对依赖能源进口的脆弱经济体的次生经济影响。

**标签**: `#energy`, `#supply-chain`, `#military-risk`, `#middle-east`, `#commodities`

---

<a id="item-3"></a>
## [欧洲央行货币政策声明及拉加德与武伊奇新闻发布会](https://www.ecb.europa.eu//press/press_conference/monetary-policy-statement/2026/html/ecb.is260611~372040d313.en.html) ⭐️ 9.0/10

欧洲央行发布了最新货币政策声明，详细说明了利率决定、更新的经济预测和前瞻性指引，随后行长拉加德与首席经济学家武伊奇举行了新闻发布会。 此次会议直接影响欧元汇率、欧洲债券收益率和全球风险情绪，对全球投资者、政策制定者和金融市场至关重要。 声明和问答环节提供了管理委员会政策动因以及其对通胀、增长和资产负债表评估的详细信息。

rss · ECB Press Releases · Jun 11, 13:00

**背景**: 欧洲中央银行（ECB）是欧元区的货币当局，负责维持价格稳定。其管理委员会定期召开会议制定关键利率并决定非常规措施。前瞻性指引是一种沟通工具，用于预示未来的政策路径，影响市场预期。由行长和首席经济学家出席的新闻发布会是透明度和市场反应的关键渠道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forward_guidance">Forward guidance</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#currency`, `#europe`, `#global-markets`

---

<a id="item-4"></a>
## [联合国对美伊可能停火协议表示鼓舞](https://news.un.org/feed/view/en/story/2026/06/1167713) ⭐️ 8.0/10

联合国秘书长发言人周五表示，该组织对有关美伊可能达成停火协议的报道感到‘鼓舞’，同时继续关注相互矛盾的报道。 停火可能缓解中东军事紧张局势，可能带来制裁放松、油价波动降低以及全球市场风险偏好改善。 这些报道出现在谈判陷入僵局之际，此前在 2026 年 4 月由巴基斯坦斡旋达成过一次为期两周的短暂停火，随后恢复了更广泛和平协议的谈判。

rss · UN News · Jun 12, 12:00

**背景**: 自 2026 年初以来，美伊陷入军事冲突，导致全球能源市场严重动荡——布伦特原油价格一度突破每桶 80 美元。2026 年 4 月达成的临时停火未能转为永久协议。联合国一直支持通过外交努力解决这场危机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire">2026 Iran war ceasefire - Wikipedia</a></li>
<li><a href="https://apnews.com/article/iran-us-israel-war-what-to-know-beb5625f8537ceaf22c061cf073210aa">What to know as ceasefire negotiations in the Iran war remain in flux ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/2025–2026_Iran–United_States_negotiations">2025-2026 Iran-United States negotiations - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#energy`, `#sanctions`

---

<a id="item-5"></a>
## [联合国警告乌克兰战争处于 2022 年以来最致命阶段](https://news.un.org/feed/view/en/story/2026/06/1167674) ⭐️ 8.0/10

联合国负责政治事务的副秘书长罗斯玛丽·迪卡洛向安理会通报，乌克兰战争已进入自 2022 年俄罗斯全面入侵以来最致命的阶段，大规模的空中袭击造成平民伤亡不断加剧。 这一急剧升级表明地缘政治风险加剧，可能促使进一步的军事援助、制裁和外交行动，从而扰乱能源市场并提升市场风险情绪。 通报是在周一举行的安理会会议上进行的，迪卡洛指出近几个月发生了冲突中一些最大规模的空中袭击，双方平民伤亡不断攀升。

rss · UN News · Jun 8, 12:00

**背景**: 联合国安理会是负责维护国际和平与安全的主要机构。俄罗斯于 2022 年 2 月对乌克兰发动全面入侵，该冲突此后牵涉广泛国际参与，包括对乌克兰的军事援助和对俄罗斯的制裁。罗斯玛丽·迪卡洛是美国外交官，自 2018 年起担任主管政治事务的副秘书长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council">United Nations Security Council - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rosemary_DiCarlo">Rosemary DiCarlo - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#russia-ukraine`, `#global-markets`

---

<a id="item-6"></a>
## [黎巴嫩医院遭袭，人道状况恶化](https://news.un.org/feed/view/en/story/2026/06/1167714) ⭐️ 7.0/10

据联合国 2026 年 6 月报道，以色列与真主党持续交火，黎巴嫩医院及医疗设施遭直接打击，人道局势进一步恶化。 此事件加剧中东地缘政治风险，可能引发国际外交后果，并因能源价格压力导致市场避险情绪。 联合国报道未给出具体伤亡数字，但确认医疗设施遭袭，此举可能违反国际人道法。

rss · UN News · Jun 12, 12:00

**背景**: 真主党是黎巴嫩什叶派伊斯兰政治与军事组织，1982 年成立，与伊朗关系密切，与以色列长期冲突。2023 年 10 月后冲突升级，引发 2024 年黎巴嫩战争及随后停火。2025-2026 年黎巴嫩政府试图解除真主党武装，但其仍具军事实力。当前医院遇袭发生在这一紧张背景下。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://en.wikipedia.org/wiki/Israeli-Hezbollah_conflict">Israeli-Hezbollah conflict</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#military-risk`, `#geopolitics`, `#diplomacy`

---

<a id="item-7"></a>
## [联合国称 5 月乌克兰平民伤亡创四年新高](https://news.un.org/feed/view/en/story/2026/06/1167707) ⭐️ 7.0/10

联合国人权观察员报告称，5 月乌克兰平民伤亡人数创下四年来单月最高纪录，凸显冲突持续造成严重人道代价。 平民伤亡激增凸显战争的残酷性，可能加剧国际社会对追责、重启外交努力或对俄追加制裁的呼声。 报告未公布具体数字，但强调实际伤亡可能更高；此趋势可能逆转此前伤亡下降的态势。

rss · UN News · Jun 12, 12:00

**背景**: 联合国乌克兰人权监测团自 2022 年 2 月俄乌冲突全面爆发以来持续记录平民伤亡。此前马里乌波尔战役期间曾出现高峰，但 5 月创新高表明近期战事可能进一步激化。

**标签**: `#russia-ukraine`, `#geopolitics`, `#military-risk`, `#diplomacy`

---

<a id="item-8"></a>
## [安理会辩论中东政治方案，联合国秘书长警告升级影响全球](https://news.un.org/feed/view/en/story/2026/06/1167689) ⭐️ 7.0/10

联合国安理会周三就推进中东政治解决方案举行高级别辩论，联合国秘书长警告在美伊脆弱停火之际，局势升级‘影响跨越国界和大陆’。 这一高级别外交接触表明国际社会加大施压缓和局势，可能影响对伊朗的制裁、全球能源市场和地区稳定。联合国秘书长措辞严厉的警告凸显了可能将大国卷入的更广泛冲突风险。 此次辩论是在最近一次中东危机爆发近四个月后举行的，美伊停火仍然脆弱。安理会作为唯一有权通过具有约束力决议的联合国机构，如果局势恶化可能考虑制裁或维和措施。

rss · UN News · Jun 10, 12:00

**背景**: 联合国安理会是联合国维护国际和平与安全的主要机构，由 15 个成员组成，其中五个常任理事国拥有否决权。历史上，安理会曾多次授权在中东进行干预和制裁。当前危机大约在四个月前因美伊直接敌对行动而升级，随后达成脆弱停火。此次辩论凸显了事态的严重性，因为局势升级可能通过霍尔木兹海峡扰乱全球能源供应，并引发更广泛的地缘政治重组。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#united-states`, `#iran`

---

<a id="item-9"></a>
## [黎巴嫩提尔遭袭致 8 死，联合国估算损失超 3.65 亿美元](https://news.un.org/feed/view/en/story/2026/06/1167685) ⭐️ 7.0/10

尽管停火协议脆弱，黎巴嫩提尔市仍遭新空袭，造成 8 人死亡。联合国主导的评估显示，自最近局势升级以来，贝鲁特和黎巴嫩山地区的建筑损失已超过 3.65 亿美元。 停火协议遭违反可能重新点燃以色列与真主党之间的全面冲突，破坏地区稳定。经济损失评估凸显了重建的迫切需求，但在黎巴嫩深陷金融危机的背景下，恢复工作更加复杂。 3.65 亿美元的估算仅涵盖贝鲁特和黎巴嫩山地区的建筑毁损，随着评估深入，总额还会增加。提尔的空袭发生在停火期间，表明国际监督执行机制有限。

rss · UN News · Jun 9, 12:00

**背景**: 黎巴嫩长期陷入经济危机和政治不稳定。2024 年以色列与真主党的冲突造成大规模破坏，尽管于 2024 年 11 月达成停火协议，但违规行为持续。联合国的损失评估是快速损害与需求评估（RDNA）的一部分，通常与世界银行和欧盟合作进行，以指导恢复和重建工作。

**标签**: `#middle-east`, `#geopolitics`, `#military-risk`

---

<a id="item-10"></a>
## [联合国报告：巴勒斯坦人遭定居者和哈马斯系统虐待](https://news.un.org/feed/view/en/story/2026/06/1167682) ⭐️ 6.0/10

联合国人权理事会调查人员发布报告，详述巴勒斯坦人遭受系统虐待，包括约旦河西岸定居者暴力升级和哈马斯在加沙基于恐惧的统治。 该报告可能加剧对以色列定居点问题和巴勒斯坦治理问题的外交压力，或影响联合国决议和制裁讨论，但市场即时影响有限。 报告明确指出约旦河西岸定居者暴力升级和加沙哈马斯的恐惧统治，凸显巴勒斯坦平民面临的双重人权危机。

rss · UN News · Jun 9, 12:00

**背景**: 自 1967 年以来，以色列占领的约旦河西岸定居点被国际社会普遍视为非法，并常伴随针对巴勒斯坦人的暴力。哈马斯自 2007 年与法塔赫内战后控制加沙，其统治受到人权侵犯和威权主义的批评。联合国多次记录两地侵犯人权行为，本报告延续了要求问责的系列调查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Israeli_settlers">Israeli settlers</a></li>
<li><a href="https://en.wikipedia.org/wiki/West_Bank">West Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hamas">Hamas</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#human-rights`

---

<a id="item-11"></a>
## [欧央行执委埃尔德森接受荷兰财经日报采访](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260610~439aa97519.en.html) ⭐️ 6.0/10

欧央行执行委员会委员弗兰克·埃尔德森接受了荷兰《金融日报》的采访；具体内容尚未公开，但此类采访通常涉及货币政策、金融稳定或银行监管议题。 欧央行执委的任何公开言论都可能释放政策信号，进而影响欧元汇率、欧元区债券收益率及市场对利率的预期。 该采访发布于欧央行官网，显示其重要性，但缺乏文字记录或摘要，因此无法直接解读出具体的政策暗示。

rss · ECB Press Releases · Jun 10, 14:00

**背景**: 欧央行是欧元区的中央银行，负责货币政策和银行监管。执行委员埃尔德森同时担任监管委员会副主席，经常就金融稳定、气候风险及数字欧元等议题发表讲话。金融市场密切关注欧央行官员的采访，以寻找未来利率变动或监管调整的线索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#currency`, `#bonds`

---