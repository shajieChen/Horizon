---
layout: default
title: "Horizon Summary: 2026-06-18 (ZH)"
date: 2026-06-18
lang: zh
---

> From 41 items, 11 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [联合国在伊朗-美国和平协议之际敦促霍尔木兹援助走廊](#item-2) ⭐️ 10.0/10
3. [美联储发布 FOMC 声明及经济预测](#item-3) ⭐️ 10.0/10
4. [欧央行拉加德与武伊契奇就 2026 年 6 月利率路径释放信号](#item-4) ⭐️ 9.0/10
5. [欧洲央行莱恩谈欧元区经济展望](#item-5) ⭐️ 8.0/10
6. [拉加德在“货币转型”演讲中阐述数字欧元愿景](#item-6) ⭐️ 8.0/10
7. [停火难护儿童：黎巴嫩每日 12 名儿童伤亡](#item-7) ⭐️ 7.0/10
8. [俄军袭击基辅和哈尔科夫，造成平民伤亡及文化遗产受损](#item-8) ⭐️ 7.0/10
9. [以军袭击黎巴嫩医院 人道危机加剧](#item-9) ⭐️ 7.0/10
10. [联合国报告称地区紧张局势中黎巴嫩暴力减少](#item-10) ⭐️ 6.0/10
11. [欧洲央行工资追踪器显示 2026 年协商工资压力稳定](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 17, 22:51

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
| QDII Nasdaq 100 Proxy | US | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | high |
| US Mega Cap Basket | US | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | high |
| Japan Equity Basket | JP | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=30231.00; 1d=+0.79%; 5d=+5.87%; 20d=+4.52% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29670.95; 1d=-0.99%; 5d=+4.08%; 20d=+2.96% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=722.51; 1d=-1.01%; 5d=+4.15%; 20d=+2.99% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=3.6%; implied_move=0.2%; put/call OI=1.4975703401523788 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=32.7; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.49; 2Y=4.2; 10Y-2Y=0.29000000000000004 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| NQ=F price trend | close=30231.00; 1d=+0.79%; 5d=+5.87%; 20d=+4.52% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29670.95; 1d=-0.99%; 5d=+4.08%; 20d=+2.96% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=722.51; 1d=-1.01%; 5d=+4.15%; 20d=+2.99% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| GOOGL price trend | close=363.79; 1d=-2.53%; 5d=+2.08%; 20d=-6.10% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=237.50; 1d=-3.46%; 5d=-0.21%; 20d=-8.42% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=567.58; 1d=-5.44%; 5d=-0.50%; 20d=-5.73% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=396.38; 1d=-2.05%; 5d=+3.88%; 20d=-1.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=204.65; 1d=-1.33%; 5d=+2.11%; 20d=-7.13% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=378.91; 1d=-3.79%; 5d=-4.64%; 20d=-9.03% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| GOOGL options surface | ATM IV=7.8%; implied_move=0.4%; put/call OI=0.4766380146493194 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=9.7%; implied_move=0.4%; put/call OI=0.7940015136060018 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=6.0%; implied_move=0.3%; put/call OI=0.8909044484163549 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=6.6%; implied_move=0.2%; put/call OI=0.6360814502110752 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=4.3%; implied_move=0.2%; put/call OI=0.7415896626849974 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=3.0%; implied_move=0.1%; put/call OI=0.39518343169682424 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| MSFT insider filings | recent Form4 count=729 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| NVDA insider filings | recent Form4 count=561 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=32.7; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
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
| GOOGL price trend | close=363.79; 1d=-2.53%; 5d=+2.08%; 20d=-6.10% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=237.50; 1d=-3.46%; 5d=-0.21%; 20d=-8.42% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=567.58; 1d=-5.44%; 5d=-0.50%; 20d=-5.73% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9984.T price trend | close=6880.00; 1d=-3.13%; 5d=+6.49%; 20d=+36.54% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=94.45; 1d=+0.35%; 5d=+6.35%; 20d=+5.18% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2810.00; 1d=-1.32%; 5d=-0.14%; 20d=-4.49% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=72640.00; 1d=+2.51%; 5d=+17.48%; 20d=+57.57% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3286.00; 1d=+0.34%; 5d=-2.92%; 20d=-8.87% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=75600.00; 1d=+0.13%; 5d=+3.72%; 20d=+3.69% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=32.7; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.49; 2Y=4.2; 10Y-2Y=0.29000000000000004 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| 9984.T price trend | close=6880.00; 1d=-3.13%; 5d=+6.49%; 20d=+36.54% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=94.45; 1d=+0.35%; 5d=+6.35%; 20d=+5.18% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2810.00; 1d=-1.32%; 5d=-0.14%; 20d=-4.49% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 0700.HK price trend | close=445.40; 1d=-0.45%; 5d=-4.34%; 20d=-3.17% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=33.65; 1d=-2.63%; 5d=-2.44%; 20d=-6.55% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=25.42; 1d=-0.94%; 5d=-3.42%; 20d=-17.04% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=106.90; 1d=-0.09%; 5d=-5.81%; 20d=-19.71% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=111.10; 1d=-0.45%; 5d=-0.98%; 20d=-11.76% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=74.40; 1d=-1.20%; 5d=-5.82%; 20d=-10.42% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.49; 2Y=4.2; 10Y-2Y=0.29000000000000004 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=32.7; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| 0700.HK price trend | close=445.40; 1d=-0.45%; 5d=-4.34%; 20d=-3.17% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=33.65; 1d=-2.63%; 5d=-2.44%; 20d=-6.55% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=25.42; 1d=-0.94%; 5d=-3.42%; 20d=-17.04% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [Move Index Chart - Barchart.com](https://www.barchart.com/stocks/quotes/$MOVE/interactive-chart)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Customizable interactive chart for Move Index with latest real-time price quote, charts, latest news, technical analysis and opinions.

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [VIX S&P 500 Volatility and MOVE Treasury Volatility / StreetStats](https://streetstats.finance/markets/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：This page provides current and historical values for key volatility metrics, including the CBOE Volatility Index (VIX) for stock market volatility and the Merrill Lynch Option V...

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [VIX Index / CBOE Volatility (indexcboe: vix) - Investing.com](https://www.investing.com/indices/volatility-s-p-500)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Live VIX Index quote, charts, historical data, analysis and news. View VIX (CBOE volatility index) price, based on real time data from S&P 500 options.

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Volatility Term Structure chart plots the at-the-money implied volatility across expirations, which are an invaluable tool in determining options strategies based on anticipated...

- [NDAQ Implied Volatility Chart Nasdaq - MarketChameleon.com](https://marketchameleon.com/Overview/NDAQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：View volatility charts for Nasdaq (NDAQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the interactive...

- [QQQ Options - Live IV, Flow, Greeks & Analysis / ImpliedOptions ...](https://impliedoptions.com/ticker/qqq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Trade QQQ options with real-time implied volatility, IV rank, options flow, and Greeks. Analyze QQQ calls and puts with our free calculator and strategy builder.

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [Invesco QQQ (QQQ) - Implied Volatility (Mean) (30-Day) - AlphaQuery](https://www.alphaquery.com/stock/QQQ/volatility-option-statistics/30-day/iv-mean)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Implied Volatility (Mean): The forecasted future volatility of the security over the selected time frame, derived from the average of the put and call implied volatilities for o...

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

- [USD/JPY Currency Exchange Rate & News - Google Finance](https://www.google.com/finance/beta/quote/USD-JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：The United States dollar is the official currency of the United States and several other countries. The Coinage Act of 1792 introduced the U.S. dollar at par with the Spanish si...

- [Live US Dollar to Yens Exchange Rate - $ 1 USD/JPY Today](https://usd.currencyrate.today/jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest and best $1 US Dollar to Yens rate for FREE. USD/JPY - Live exchange rates, banks, historical data & currency charts.

- [USD JPY Exchange Rate, Live USD to JPY Forex Rate at Forex Rates](https://www.forexrates.net/fx-rates/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：USD JPY Exchange Rate This is the live USD JPY rate forex data page, displaying the FX price for the USD/JPY. The FX rate self-updates every few seconds. Compare exchange rates...

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Current Values - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index?idx=nk225)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Current Values Nikkei calculates and publishes various types of the indexes such as the "Nikkei Stock Average (Nikkei 225)" which is known as a representative Japanese stock mar...

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
## [联合国在伊朗-美国和平协议之际敦促霍尔木兹援助走廊](https://news.un.org/feed/view/en/story/2026/06/1167717) ⭐️ 10.0/10

据报道，伊朗和美国正在敲定和平协议之际，联合国呼吁立即开辟人道主义走廊，穿越被封锁的霍尔木兹海峡，以避免全球粮食危机。 这一进展可能缓解因海峡封锁导致的石油和粮食供应危机，影响全球能源价格和粮食安全；该协议还可能重塑中东外交格局并降低地缘政治风险溢价。 霍尔木兹海峡每日通过约 2000 万桶石油，因冲突被封锁；联合国警告饥荒危机加剧，而人道协调厅报告称黎巴嫩流离失所者仍面临困难。

rss · UN News · Jun 15, 12:00

**背景**: 霍尔木兹海峡是连接波斯湾与全球市场的重要海上咽喉。人道主义走廊是临时非军事区，允许援助和平民安全通行。据报道，伊朗-美国和平协议是在紧张局势升级后达成的，让人想起 2015 年伊核协议，可能稳定该地区。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c78n6p09pzno">Iran war: What is the Strait of Hormuz and why does it matter?</a></li>
<li><a href="https://www.theguardian.com/world/2026/jun/14/trump-calls-for-restraint-israel-airstrikes-beirut-us-iran-peace-deal">US and Iran reach framework peace deal to end war | The Guardian</a></li>
<li><a href="https://en.wikipedia.org/wiki/Humanitarian_corridor">Humanitarian corridor - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#energy`, `#supply-chain`

---

<a id="item-3"></a>
## [美联储发布 FOMC 声明及经济预测](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm) ⭐️ 10.0/10

美联储发布了 6 月 16-17 日 FOMC 会议的声明和经济预测摘要，概述了最新货币政策立场。 该声明引导全球利率预期，影响货币和债券市场，塑造全球金融环境。 声明包括联邦基金利率目标区间、委员利率预测的'点阵图'，以及美联储主席的新闻发布会。

rss · Federal Reserve Press Releases · Jun 17, 18:00

**背景**: 联邦公开市场委员会（FOMC）是美联储的货币政策决策机构，每年召开八次会议设定联邦基金利率目标区间。其决策基于最大化就业和稳定物价的双重使命。季度经济预测摘要包含委员对政策利率预测的'点阵图'，受到全球市场密切关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Reserve">Federal Reserve</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federal_Open_Market_Committee">Federal Open Market Committee - Wikipedia</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#global-markets`, `#bonds`, `#equities`

---

<a id="item-4"></a>
## [欧央行拉加德与武伊契奇就 2026 年 6 月利率路径释放信号](https://www.ecb.europa.eu//press/press_conference/monetary-policy-statement/2026/html/ecb.is260611~372040d313.en.html) ⭐️ 9.0/10

欧央行行长拉加德与武伊契奇行长发布了 2026 年 6 月货币政策声明，对欧元区利率路径和经济前景释放关键信号。 该声明直接塑造市场对欧元区利率、债券收益率和欧元汇率的预期，将引发欧元交叉盘、欧洲债市和股市的波动。 问答环节增添了细节，可能包含关于政策工具或地缘政治风险的言论，具有引发市场波动的潜力。

rss · ECB Press Releases · Jun 11, 13:00

**背景**: 欧央行管理委员会负责制定欧元区货币政策。定期政策声明与新闻发布会是其关键沟通渠道。鲍里斯·武伊契奇为克罗地亚央行行长兼管理委员会成员。此类事件受到全球投资者密切关注，以获取利率、资产购买和经济前景的信号。

**标签**: `#central-bank`, `#europe`, `#macroeconomics`, `#bonds`, `#currency`

---

<a id="item-5"></a>
## [欧洲央行莱恩谈欧元区经济展望](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260616~8076dabd2c.en.pdf) ⭐️ 8.0/10

欧洲央行首席经济学家菲利普·莱恩就欧元区经济前景发表演讲，可能基于增长和通胀评估暗示未来的货币政策方向。 该演讲可能影响对欧洲央行利率的预期，从而影响欧元汇率和债券市场，并为投资者和政策制定者提供前瞻性指引。 演讲以 PDF 形式发布在欧洲央行官网，表明是官方沟通；但摘要未透露具体的预测或政策暗示。

rss · ECB Press Releases · Jun 16, 13:10

**背景**: 菲利普·莱恩是欧洲央行首席经济学家，负责经济分析和货币政策制定。欧元区经济面临增长缓慢和通胀低于目标的挑战，促使欧洲央行使用多种工具。重要官员的讲话被密切关注以寻找未来政策动向的信号。

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#bonds`, `#currencies`

---

<a id="item-6"></a>
## [拉加德在“货币转型”演讲中阐述数字欧元愿景](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260615~35e6c6c4de.en.html) ⭐️ 8.0/10

欧洲央行行长拉加德发表题为“货币转型”的演讲，强调向数字支付的转变以及央行推出数字欧元以维护货币主权和支付效率的计划。 该演讲标志着数字欧元项目可能加速推进，这将重塑欧洲支付格局，对私人稳定币构成挑战，并对货币政策传导和金融稳定产生深远影响。 拉加德强调，在技术开发完成后，数字欧元已成为欧洲央行管理委员会和欧洲议会的当务之急。

rss · ECB Press Releases · Jun 15, 07:30

**背景**: 数字欧元是欧洲央行的央行数字货币（CBDC）项目，于 2021 年启动，旨在用数字形式的央行货币补充现金。在私人加密货币和稳定币兴起的背景下，许多央行正在探索 CBDC，以确保支付系统的安全性和效率。欧洲央行一直在开发技术基础设施，目前正朝着潜在发行迈进，但尚待立法批准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_euro">Digital euro - Wikipedia</a></li>
<li><a href="https://www.ecb.europa.eu/euro/digital_euro/html/index.en.html">Digital euro | European Central Bank</a></li>
<li><a href="https://www.bis.org/publ/othp88.htm">Central bank digital currencies: legal and system design considerations</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#europe`, `#global-markets`, `#macroeconomics`

---

<a id="item-7"></a>
## [停火难护儿童：黎巴嫩每日 12 名儿童伤亡](https://news.un.org/feed/view/en/story/2026/06/1167736) ⭐️ 7.0/10

联合国儿童基金会周三报告称，尽管真主党与以色列达成停火，但经过 100 多天的战争，黎巴嫩平均每天仍有 12 名儿童被杀或致残。 这一发现表明停火的脆弱性及平民面临的持续危险，若敌对行动重燃，可能影响地区稳定和全球能源市场。 联合国儿童基金会的报告强调，以色列的袭击和强迫流离失所仍在继续，自 2024 年 11 月底生效的停火并未终止针对儿童的暴力。

rss · UN News · Jun 17, 12:00

**背景**: 2024 年以色列-黎巴嫩停火协议于 2024 年 11 月 27 日签署，结束了始于真主党为声援哈马斯而攻击以色列的一年多跨境冲突。真主党是黎巴嫩什叶派伊斯兰政治和军事组织，拥有强大军事实力，被许多西方国家认定为恐怖组织。尽管有停火协议，但零星暴力事件持续发生，尤其影响脆弱社区。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2024_Israel–Lebanon_ceasefire_agreement">2024 Israel –Lebanon ceasefire agreement - Wikipedia</a></li>
<li><a href="https://www.unicef.org/lebanon/">UNICEF Lebanon</a></li>

</ul>
</details>

**标签**: `#military-risk`, `#geopolitics`, `#middle-east`, `#israel`, `#lebanon`

---

<a id="item-8"></a>
## [俄军袭击基辅和哈尔科夫，造成平民伤亡及文化遗产受损](https://news.un.org/feed/view/en/story/2026/06/1167718) ⭐️ 7.0/10

联合国称，俄罗斯对基辅和哈尔科夫发动夜间袭击，造成多名平民死亡、数十人受伤，并损坏了当地文化遗产。 袭击造成平民伤亡和文化遗产破坏，可能加剧国际社会对俄谴责和制裁讨论，并提升冲突进一步升级的风险。 联合国报告指出，袭击针对基辅、哈尔科夫和文化遗产，但未提供具体伤亡数字或受损地标的详细信息。

rss · UN News · Jun 15, 12:00

**背景**: 自 2022 年 2 月以来的俄乌战争已造成大量平民伤亡和广泛破坏。联合国多次谴责针对平民区和文化遗产的袭击。根据国际人道法，文化遗产受保护，蓄意攻击可能构成战争罪。

**标签**: `#russia-ukraine`, `#diplomacy`, `#geopolitics`, `#military-risk`

---

<a id="item-9"></a>
## [以军袭击黎巴嫩医院 人道危机加剧](https://news.un.org/feed/view/en/story/2026/06/1167714) ⭐️ 7.0/10

以色列军队在与真主党的持续敌对行动中袭击了黎巴嫩的医院，将人道主义局势推向更深的危机，并威胁到基本医疗服务。 袭击医院可能引发国际谴责和潜在的联合国安理会行动，同时加剧地区不稳定，并有可能波及能源市场和更广泛的中东地缘政治。 在冲突早期，2023 年 10 月至 2024 年 10 月期间，以色列轰炸了黎巴嫩 37 处卫生设施，导致 70 名卫生专业人员死亡。蓄意攻击医疗设施已成为冲突地区有据可查的模式，削弱了国际人道主义法下的保护。

rss · UN News · Jun 12, 12:00

**背景**: 真主党是黎巴嫩什叶派伊斯兰政治党派及受伊朗支持的激进组织，被许多西方国家列为恐怖组织。与以色列的敌对行动于 2023 年 10 月升级，导致 2024 年黎巴嫩战争及随后的停火。尽管黎巴嫩政府在 2025–2026 年批准了真主党解除武装计划，真主党仍继续军事行动。冲突中对医疗保健的攻击在全球范围内有所增加，以色列在加沙和黎巴嫩的行动尤其令人担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://globalvoices.org/2025/04/07/across-war-zones-targeting-healthcare-has-become-a-strategy-not-an-accident/">Across war zones , targeting healthcare has become a strategy, not an...</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#military-risk`, `#middle-east`, `#diplomacy`

---

<a id="item-10"></a>
## [联合国报告称地区紧张局势中黎巴嫩暴力减少](https://news.un.org/feed/view/en/story/2026/06/1167733) ⭐️ 6.0/10

联合国发言人斯特凡·杜加里克周二表示，尽管维和人员仍在黎巴嫩观察到暴力和交火，但暴力程度与周末相比已显著降低。 暴力减少可能表明以色列军队与真主党之间的局势有所缓和，降低了眼前的安全风险。然而，持续紧张仍可能威胁稳定和联合国维和人员的安全。 联合国未披露具体事件数据，但此前联黎部队维和人员遭遇致命袭击，引发国际谴责。

rss · UN News · Jun 16, 12:00

**背景**: 联合国驻黎巴嫩临时部队（联黎部队）成立于 1978 年，2006 年扩充，负责监督以色列与黎巴嫩的停火。近期升级的交火和多次针对维和人员的袭击，使数十个国家予以谴责。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Interim_Force_in_Lebanon">United Nations Interim Force in Lebanon - Wikipedia</a></li>
<li><a href="https://news.un.org/en/story/2026/03/1167222">UN condemns killing of two more peacekeepers in Lebanon</a></li>
<li><a href="https://www.reuters.com/world/asia-pacific/dozens-states-condemn-attacks-un-peacekeepers-lebanon-2026-04-09/">Dozens of states condemn attacks on U.N. peacekeepers in Lebanon</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#middle-east`, `#military-risk`, `#sovereign-risk`, `#humanitarian`

---

<a id="item-11"></a>
## [欧洲央行工资追踪器显示 2026 年协商工资压力稳定](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260617~79dfc49802.en.html) ⭐️ 6.0/10

欧洲央行更新的工资追踪数据显示，根据九个欧元区国家的集体谈判协议，欧元区协商工资增长压力预计在 2026 年保持稳定。 工资压力稳定表明服务业通胀风险减弱，可能降低进一步收紧货币政策的必要性，并影响市场对欧洲央行未来利率决策的预期。 该追踪器包含经平滑处理和未经平滑处理的一次性支付，这些支付预计在 2026 年消退，使基本工资趋势更加清晰。覆盖范围包括比利时、德国、希腊、西班牙、法国、意大利、荷兰、奥地利和芬兰。

rss · ECB Press Releases · Jun 17, 08:00

**背景**: 欧洲央行工资追踪器是欧元体系开发的实验性工具，利用 1000 多份集体谈判协议的细粒度数据监测协商工资增长，覆盖约 60%的欧元区雇员。它于 2023 年推出，有助于评估工资发展是否符合欧洲央行 2%的通胀目标。定期更新为货币政策提供前瞻性信号，尤其是在疫情后通胀飙升凸显工资动态重要性之后。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260617~79dfc49802.en.html">New data release: ECB wage tracker points to stable negotiated wage pressures in 2026</a></li>
<li><a href="https://data.ecb.europa.eu/data/datasets/EWT/data-information">ECB Wage Tracker - EWT | ECB Data Portal</a></li>
<li><a href="https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260211_1~dd029e0063.en.html">New data release: ECB wage tracker continues to suggest normalisation of negotiated wage pressures in 2026</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`

---