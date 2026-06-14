---
layout: default
title: "Horizon Summary: 2026-06-15 (ZH)"
date: 2026-06-15
lang: zh
---

> From 41 items, 10 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [霍尔木兹海峡油轮遇袭 三名船员丧生](#item-2) ⭐️ 9.0/10
3. [欧洲央行公布货币政策决议](#item-3) ⭐️ 9.0/10
4. [联合国乐见美伊停火协议传闻](#item-4) ⭐️ 8.0/10
5. [联合国报告：乌克兰五月平民伤亡创四年新高](#item-5) ⭐️ 8.0/10
6. [以军空袭黎医院，人道危机恶化](#item-6) ⭐️ 7.0/10
7. [泰尔遭袭致八人死亡 联合国评估黎巴嫩损失超 3.65 亿美元](#item-7) ⭐️ 7.0/10
8. [欧央行副行长埃尔德森谈货币政策与稳定](#item-8) ⭐️ 7.0/10
9. [美联储将于 6 月 24 日公布年度银行压力测试结果](#item-9) ⭐️ 7.0/10
10. [FSB 就金融机构 AI 采用发布健全实践咨询报告](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 14, 22:43

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
| QQQ price trend | close=721.34; 1d=+0.59%; 5d=+2.31%; 20d=+0.22% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29635.95; 1d=+0.64%; 5d=+2.34%; 20d=+0.19% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=30038.75; 1d=+1.27%; 5d=+1.98%; 20d=+2.76% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=24.5%; implied_move=1.4%; put/call OI=1.842459555799287 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=34.0; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.48; 2Y=4.09; 10Y-2Y=0.39000000000000057 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| QQQ price trend | close=721.34; 1d=+0.59%; 5d=+2.31%; 20d=+0.22% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29635.95; 1d=+0.64%; 5d=+2.34%; 20d=+0.19% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=30038.75; 1d=+1.27%; 5d=+1.98%; 20d=+2.76% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| MSFT price trend | close=390.74; 1d=+0.10%; 5d=-6.22%; 20d=-4.36% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=359.68; 1d=+0.53%; 5d=-2.34%; 20d=-10.27% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=205.19; 1d=+0.16%; 5d=+0.04%; 20d=-12.86% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=291.13; 1d=-1.52%; 5d=-5.27%; 20d=-2.37% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=238.55; 1d=-1.23%; 5d=-3.04%; 20d=-10.73% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=406.43; 1d=+1.82%; 5d=+3.95%; 20d=-8.32% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| MSFT options surface | ATM IV=30.7%; implied_move=1.8%; put/call OI=0.3819433391691867 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=55.3%; implied_move=3.3%; put/call OI=0.6420545746388443 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=32.7%; implied_move=1.9%; put/call OI=0.736036997509783 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=33.2%; implied_move=1.9%; put/call OI=0.7887573324683048 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=22.9%; implied_move=1.3%; put/call OI=0.41203978814106706 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=32.4%; implied_move=1.9%; put/call OI=0.47175863278704955 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| NVDA insider filings | recent Form4 count=561 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.48; 2Y=4.09; 10Y-2Y=0.39000000000000057 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=34.0; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| AAPL insider filings | recent Form4 count=587 | 内部人交易节奏可作为估值温度辅助校验信号。 |

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
| MSFT price trend | close=390.74; 1d=+0.10%; 5d=-6.22%; 20d=-4.36% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=359.68; 1d=+0.53%; 5d=-2.34%; 20d=-10.27% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=205.19; 1d=+0.16%; 5d=+0.04%; 20d=-12.86% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 8035.T price trend | close=68000.00; 1d=+7.26%; 5d=+14.38%; 20d=+35.22% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3292.00; 1d=-2.29%; 5d=-7.50%; 20d=-7.94% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.71; 1d=+0.57%; 5d=+2.19%; 20d=+0.71% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6472.00; 1d=+1.54%; 5d=-12.85%; 20d=+12.65% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=72620.00; 1d=+1.89%; 5d=-6.98%; 20d=-5.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2775.50; 1d=+1.02%; 5d=-2.61%; 20d=-10.03% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=34.0; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.48; 2Y=4.09; 10Y-2Y=0.39000000000000057 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| 8035.T price trend | close=68000.00; 1d=+7.26%; 5d=+14.38%; 20d=+35.22% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3292.00; 1d=-2.29%; 5d=-7.50%; 20d=-7.94% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.71; 1d=+0.57%; 5d=+2.19%; 20d=+0.71% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9618.HK price trend | close=112.60; 1d=+3.40%; 5d=-2.76%; 20d=-13.45% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=35.29; 1d=+1.09%; 5d=+1.55%; 20d=-5.24% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=26.20; 1d=+1.39%; 5d=-5.76%; 20d=-17.40% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=77.90; 1d=-0.26%; 5d=-2.56%; 20d=-9.10% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=22.00; 1d=+0.55%; 5d=+0.82%; 20d=-9.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=463.60; 1d=+1.40%; 5d=+2.29%; 20d=+1.91% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=34.0; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.48; 2Y=4.09; 10Y-2Y=0.39000000000000057 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| FXI price trend | close=35.29; 1d=+1.09%; 5d=+1.55%; 20d=-5.24% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=26.20; 1d=+1.39%; 5d=-5.76%; 20d=-17.40% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [Volatility NASDAQ - 100 (NASDAQVOLNDX) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/NASDAQVOLNDX)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Graph and download economic data for Volatility NASDAQ - 100 (NASDAQVOLNDX) from 2010-07-23 to 2026-01-16 about volatility, NASDAQ, indexes, and USA.

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days or more out. IV is a forward looking prediction of the likelihood...

- [Nasdaq-100 Volatility Index (VOLQ)](https://www.nasdaq.com/market-activity/index/volq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Find the latest information on Nasdaq-100 Volatility Index (VOLQ), including data, charts, related news, and more from Nasdaq.com

- [VIX S&P 500 Volatility and MOVE Treasury Volatility / StreetStats](https://streetstats.finance/markets/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：This page provides current and historical values for key volatility metrics, including the CBOE Volatility Index (VIX) for stock market volatility and the Merrill Lynch Option V...

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [MOVE Index Charts and Quotes — TradingView](https://www.tradingview.com/symbols/TVC-MOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：MOVE INDEX Setup for Top in World stock markets The chart is the Move index it is reaching an area which I consider High level of Complacency I say this as of this writing The 1...

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [QQQ Options - Live IV, Flow, Greeks & Analysis / ImpliedOptions ...](https://impliedoptions.com/ticker/qqq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Trade QQQ options with real-time implied volatility, IV rank, options flow, and Greeks. Analyze QQQ calls and puts with our free calculator and strategy builder.

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

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [iShares MSCI Japan ETF / EWJ](https://www.ishares.com/us/products/239665/ishares-msci-japan-etf)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：The iShares MSCI Japan ETF seeks to track an index composed of Japanese equities. The fund offers a way to express a single-country view and gain targeted exposure to companies...

- [Nikkei Average Volatility (^NKVI.OS) - Yahoo Finance](https://finance.yahoo.com/quote/%5ENKVI.OS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Find the latest information on Nikkei Average Volatility (^NKVI.OS) including data, charts, related news and more from Yahoo Finance

- [Index Information - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index/profile?idx=nk225vi)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：The Nikkei Stock Average Volatility Index are calculated by using prices of Nikkei 225 futures and Nikkei 225 options on the Osaka Exchange (OSE). In the calculation, taking nea...

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
## [霍尔木兹海峡油轮遇袭 三名船员丧生](https://news.un.org/feed/view/en/story/2026/06/1167697) ⭐️ 9.0/10

周三，霍尔木兹海峡附近一艘油轮遇袭，造成三名印度船员死亡，这条关键航运走廊再度爆发敌对行动。联合国警告称，此次事件的影响正在扩大。 霍尔木兹海峡承担着全球约 20%的石油运输，在此发生的袭击直接威胁能源供应链，并可能导致燃料价格飙升、全球市场不稳定。该事件可能引发大国军事回应和外交干预。 三名遇难者均为印度籍；暂无组织宣称负责。此次袭击是近几个月一系列针对商船的打击事件的最新一起，加剧了航运保险和石油期货的风险。

rss · UN News · Jun 11, 12:00

**背景**: 霍尔木兹海峡是位于伊朗与阿曼之间的狭窄水道，是全球能源运输的重要咽喉，每日约有 2000 万桶石油通过。自 2026 年 3 月以来，由于区域冲突，针对油轮和商船的袭击事件激增，导致军事存在加强和航运中断。联合国等机构多次警告粮食安全和供应链面临风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis">2026 Strait of Hormuz crisis - Wikipedia</a></li>
<li><a href="https://www.eia.gov/todayinenergy/detail.php?id=61002">The Strait of Hormuz is the world's most important oil transit chokepoint - U.S. Energy Information Administration (EIA)</a></li>
<li><a href="https://www.cnbc.com/2026/03/12/iran-war-persian-gulf-strait-of-hormuz-ships-uae-iraq.html">Three more ships struck in the Gulf as Iran warns of oil ...</a></li>

</ul>
</details>

**标签**: `#military-risk`, `#energy`, `#supply-chain`, `#middle-east`, `#global-markets`

---

<a id="item-3"></a>
## [欧洲央行公布货币政策决议](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html) ⭐️ 9.0/10

欧洲央行于 2026 年 6 月 11 日公布了其最新货币政策立场，确定了关键利率和前瞻指引，这将影响欧元区的金融状况和资产价格。 欧洲央行的决策直接影响欧元区借贷成本、欧元汇率和全球风险偏好，这是一个可能影响市场的事件，对国际贸易和投资流动有潜在影响。 虽然未提供利率变动或资产购买调整的具体幅度，但政策声明可能涉及通胀动态、增长前景和金融稳定风险。

rss · ECB Press Releases · Jun 11, 12:15

**背景**: 欧洲央行是欧元区的中央银行，负责制定货币政策以维持价格稳定，主要目标是中期内将通胀率控制在低于但接近 2%的水平。其政策决定影响整个欧元区的利率，影响政府、企业和家庭。管理委员会定期开会评估经济状况，并决定适当的政策措施。

**标签**: `#central-bank`, `#macroeconomics`, `#currency`, `#bonds`, `#europe`

---

<a id="item-4"></a>
## [联合国乐见美伊停火协议传闻](https://news.un.org/feed/view/en/story/2026/06/1167713) ⭐️ 8.0/10

联合国秘书长发言人表示，对有关美伊可能达成停火协议的矛盾传闻感到鼓舞，这暗示着可能的外交突破。 美伊停火可能缓解中东紧张局势，稳定能源市场，重塑制裁政策，对地区安全和全球外交产生广泛影响。 相关报道相互矛盾，有待确认；联合国安理会近期就推进中东政治解决方案举行了高级别辩论，凸显局势脆弱。

rss · UN News · Jun 12, 12:00

**背景**: 自 2026 年伊朗战争爆发以来，尽管达成了脆弱的停火，紧张局势仍在持续。联合国安理会一直积极参与寻求政治解决方案，并认识到海湾合作委员会等区域组织在缓和努力中的作用。美伊长期敌对，近期的冲突还涉及以色列和代理组织。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Iran_war">2026 Iran war - Wikipedia</a></li>
<li><a href="https://www.cfr.org/global-conflict-tracker/conflict/confrontation-between-united-states-and-iran">Iran’s War With Israel and the United States | Global ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council">United Nations Security Council - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#united-states`, `#military-risk`

---

<a id="item-5"></a>
## [联合国报告：乌克兰五月平民伤亡创四年新高](https://news.un.org/feed/view/en/story/2026/06/1167707) ⭐️ 8.0/10

联合国乌克兰人权监测团宣布，2026 年 5 月乌克兰平民伤亡人数达到 2022 年 2 月俄罗斯全面入侵以来的最高月度水平。 伤亡激增表明冲突加剧，可能加速西方军事援助和制裁，并可能推高能源和金融市场的地缘政治风险溢价。 这一激增是在 4 月已有 238 名平民死亡、1404 人受伤的基础上发生的，反映出空袭和前线战事的加剧。

rss · UN News · Jun 12, 12:00

**背景**: 俄罗斯于 2022 年 2 月对乌克兰发动全面入侵，造成大量平民伤亡。联合国乌克兰人权监测团自 2014 年以来一直系统记录平民死伤情况，其报告被广泛用于国际政策和制裁讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Casualties_of_the_Russo-Ukrainian_War">Casualties of the Russo-Ukrainian war - Wikipedia</a></li>
<li><a href="https://ukraine.ohchr.org/en/reports">All reports | UN Human Rights Monitoring Mission in Ukraine</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#geopolitics`, `#military-risk`, `#diplomacy`, `#europe`

---

<a id="item-6"></a>
## [以军空袭黎医院，人道危机恶化](https://news.un.org/feed/view/en/story/2026/06/1167714) ⭐️ 7.0/10

在以色列军队与黎巴嫩真主党的持续敌对行动中，以色列空袭了黎巴嫩的医院和医疗机构，进一步加剧了人道危机并导致基本服务中断。 这种升级可能引发国际谴责和潜在制裁，同时加大外交干预的压力；若冲突扩大至区域范围，还可能影响能源市场稳定。 空袭针对包括医疗在内的基本服务，据报有医院进一步遭袭；黎巴嫩政府近期已在美国主导计划下着手解除真主党武装，但落实仍存不确定性。

rss · UN News · Jun 12, 12:00

**背景**: 真主党是黎巴嫩强大的什叶派政治与军事组织，与以色列多次冲突，包括 2006 年战争及自 2023 年 10 月以来的敌对行动。尽管 2024 年达成停火，零星打击仍在继续；黎巴嫩政府已批准解除真主党武装的计划。该国医疗系统本已因经济崩溃和 2020 年贝鲁特港爆炸而脆弱，如今又遭直接袭击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>

</ul>
</details>

**标签**: `#military-risk`, `#middle-east`, `#geopolitics`, `#israel`, `#lebanon`

---

<a id="item-7"></a>
## [泰尔遭袭致八人死亡 联合国评估黎巴嫩损失超 3.65 亿美元](https://news.un.org/feed/view/en/story/2026/06/1167685) ⭐️ 7.0/10

黎巴嫩泰尔市遭新一轮空袭，造成八人死亡；同时联合国发布报告，估计近期冲突升级对贝鲁特和黎巴嫩山地区造成的建筑损毁超过 3.65 亿美元。 这些袭击破坏了本就脆弱的停火协议，对地区稳定构成威胁；联合国的损失评估突显了巨大的经济代价，可能促使国际社会加大人道主义和外交介入。 此次损失评估由联合国开发计划署（UNDP）与黎巴嫩国家科学研究院等机构合作进行，仅涵盖建筑直接损失，实际数字可能更高；2026 年 4 月达成的停火协议已多次遭违反。

rss · UN News · Jun 9, 12:00

**背景**: 泰尔是联合国教科文组织世界遗产地，历史悠久的腓尼基港口城市。本轮升级是以色列与黎巴嫩真主党长期冲突的一部分，伊朗将黎巴嫩战线与更广泛的地区博弈挂钩，包括霍尔木兹海峡紧张局势。2026 年 4 月达成的 10 天停火协议十分脆弱。黎巴嫩本已深陷严重经济危机，战事令局势雪上加霜。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167685">Fresh strikes on Tyre kill eight, as UN puts Lebanon ...</a></li>
<li><a href="https://www.undp.org/arab-states/press-releases/rapid-damage-assessment-estimates-over-us365-million-building-damage-across-beirut-and-mount-lebanon">Rapid damage assessment estimates over US$365 Million in ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-8"></a>
## [欧央行副行长埃尔德森谈货币政策与稳定](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260610~439aa97519.en.html) ⭐️ 7.0/10

欧央行副行长弗兰克·埃尔德森接受《荷兰财经日报》采访，就欧央行当前货币政策立场、通胀前景和欧元区金融稳定发表评论，可能预示未来政策动向。 其言论可能影响市场对欧元区利率和银行监管的预期，进而影响欧洲的借贷成本和投资者情绪。 作为欧央行副行长及银行监管关键人物，埃尔德森对通胀持续性和银行韧性的看法举足轻重；采访或透露政策变化时机与方向的线索。

rss · ECB Press Releases · Jun 10, 14:00

**背景**: 弗兰克·埃尔德森是欧央行监事会副主席、执行委员会成员，负责单一监管机制（SSM）并参与货币政策决策。ECB 通过加息应对高通胀，市场密切关注官员政策信号。

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#financial-stability`, `#global-markets`

---

<a id="item-9"></a>
## [美联储将于 6 月 24 日公布年度银行压力测试结果](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260609a.htm) ⭐️ 7.0/10

美联储宣布将于美国东部时间 6 月 24 日（周三）下午 4 点发布年度银行压力测试结果，该测试旨在评估美国大型银行在假设经济衰退情景下的抗风险能力。 压力测试结果对金融市场至关重要，因为它决定银行能否提高股息和股票回购，从而影响股价估值，并传递金融行业整体稳健性的信号。 发布时间定于美股收盘后，可能引发次日市场波动；测试基于美联储设计的严重不利情景，但具体假设参数尚未公布。

rss · Federal Reserve Press Releases · Jun 9, 20:00

**背景**: 自 2008 年金融危机以来，美联储根据《多德-弗兰克法案》每年对大型银行进行压力测试（现分为综合资本分析评估 CCAR 和多德-弗兰克法案压力测试 DFAST），检验银行在严重衰退期间的资本充足性和持续放贷能力。测试结果直接影响银行的股息和回购等资本分配计划，未通过者将面临限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Reserve_Board_of_Governors">Federal Reserve Board of Governors</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bank_stress_test">Bank stress test</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#equities`, `#bonds`, `#macroeconomics`

---

<a id="item-10"></a>
## [FSB 就金融机构 AI 采用发布健全实践咨询报告](https://www.fsb.org/2026/06/sound-practices-for-responsible-adoption-of-artificial-intelligence-ai-consultation-report/) ⭐️ 7.0/10

金融稳定理事会（FSB）发布了一份咨询报告，提出 12 项健全实践，供金融机构在负责任地采用人工智能时参考，涵盖治理和人工智能生命周期，并邀请利益相关方提供反馈。 此次咨询表明国际社会可能迈向针对金融领域 AI 的监管标准，这将影响金融机构如何管理 AI 风险，并可能影响市场稳定。此举反映了全球在平衡创新与防范系统性风险方面的努力。 报告提出了 12 项健全实践，适用于各类金融机构，重点关注组织整体的 AI 治理和 AI 生命周期管理。作为咨询文件，这些实践尚未具有约束力，可能会根据反馈意见进行调整。

rss · Financial Stability Board News · Jun 10, 08:00

**背景**: FSB 是设在瑞士巴塞尔的国际机构，由 G20 在 2008 年金融危机后设立，旨在监测全球金融体系并提出建议。它不具备正式法律权力，但通过其成员机构（包括主要经济体的央行和监管机构）协调政策。人工智能在金融领域的快速应用，从信用评分到欺诈检测，引发了人们对算法偏见、缺乏透明度以及潜在系统性风险的担忧，促使监管机构制定指引以确保金融稳定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fsb.org/2026/06/sound-practices-for-responsible-adoption-of-artificial-intelligence-ai-consultation-report/">Sound Practices for Responsible Adoption of Artificial ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Financial_Stability_Board">Financial Stability Board</a></li>

</ul>
</details>

**标签**: `#financial-stability`, `#global-markets`, `#central-bank`

---