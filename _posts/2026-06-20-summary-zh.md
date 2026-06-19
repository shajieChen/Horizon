---
layout: default
title: "Horizon Summary: 2026-06-20 (ZH)"
date: 2026-06-20
lang: zh
---

> From 44 items, 14 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [IAEA 欢迎美伊备忘录并提议核核查](#item-2) ⭐️ 9.0/10
3. [美联储发布 6 月 FOMC 经济预测](#item-3) ⭐️ 9.0/10
4. [联合国欢迎黎巴嫩新停火报道，人权专家敦促伊朗问责](#item-4) ⭐️ 8.0/10
5. [ECB 莱恩阐释欧元区经济前景](#item-5) ⭐️ 8.0/10
6. [联合国安理会辩论加沙危机，停火名存实亡](#item-6) ⭐️ 7.0/10
7. [联合国儿童基金会：黎巴嫩停火后每日仍有 12 名儿童伤亡](#item-7) ⭐️ 7.0/10
8. [欧央行皮耶罗·奇波洛内阐述数字欧元愿景](#item-8) ⭐️ 7.0/10
9. [ECB 工资追踪：2026 薪资压力稳定](#item-9) ⭐️ 7.0/10
10. [欧洲央行行长拉加德谈货币的数字化过渡](#item-10) ⭐️ 7.0/10
11. [联合国重申黎巴嫩维和人员行动自由](#item-11) ⭐️ 6.0/10
12. [联合国特使警告：利比亚政治窗口收窄](#item-12) ⭐️ 6.0/10
13. [欧央行奇波洛内谈央行货币与主权](#item-13) ⭐️ 6.0/10
14. [美联储提议要求稳定币发行方实施客户身份识别计划](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 19, 22:40

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
| Japan Equity Basket | JP | neutral 33/33/34 | bullish 38/31/31 | bullish 39/30/31 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | neutral 33/33/34 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| QQQ price trend | close=740.62; 1d=+2.51%; 5d=+3.28%; 20d=+3.85% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=30406.19; 1d=+2.48%; 5d=+3.26%; 20d=+3.78% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=30647.00; 1d=+1.27%; 5d=+3.32%; 20d=+4.07% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=14.5%; implied_move=1.2%; put/call OI=3.1215094884190777 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=37.3; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| QQQ price trend | close=740.62; 1d=+2.51%; 5d=+3.28%; 20d=+3.85% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=30406.19; 1d=+2.48%; 5d=+3.26%; 20d=+3.78% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=30647.00; 1d=+1.27%; 5d=+3.32%; 20d=+4.07% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| AAPL price trend | close=298.01; 1d=+0.70%; 5d=+0.81%; 20d=-1.40% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=368.03; 1d=+1.17%; 5d=+2.87%; 20d=-5.31% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=210.69; 1d=+2.95%; 5d=+2.84%; 20d=-5.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=244.39; 1d=+2.90%; 5d=+1.19%; 20d=-7.78% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=379.40; 1d=+0.13%; 5d=-2.80%; 20d=-9.70% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=400.49; 1d=+1.04%; 5d=+0.34%; 20d=-4.02% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| META options surface | ATM IV=23.8%; implied_move=1.9%; put/call OI=0.7012071778140294 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=16.2%; implied_move=1.3%; put/call OI=0.8416480751886837 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=22.7%; implied_move=1.7%; put/call OI=1.143438453713123 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=22.7%; implied_move=1.8%; put/call OI=0.6221465876415704 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=25.8%; implied_move=2.1%; put/call OI=0.9844313545278578 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=23.0%; implied_move=1.8%; put/call OI=0.6471850852446952 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=37.3; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| MSFT insider filings | recent Form4 count=729 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| AAPL insider filings | recent Form4 count=589 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| AAPL price trend | close=298.01; 1d=+0.70%; 5d=+0.81%; 20d=-1.40% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=368.03; 1d=+1.17%; 5d=+2.87%; 20d=-5.31% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=210.69; 1d=+2.95%; 5d=+2.84%; 20d=-5.61% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 8035.T price trend | close=75360.00; 1d=-0.95%; 5d=+10.82%; 20d=+51.23% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7111.00; 1d=-1.08%; 5d=+9.87%; 20d=+5.24% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3140.00; 1d=-3.38%; 5d=-4.62%; 20d=-10.92% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=96.26; 1d=+1.92%; 5d=+4.99%; 20d=+6.11% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2776.50; 1d=-0.61%; 5d=+0.04%; 20d=-7.05% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77700.00; 1d=+0.23%; 5d=+7.00%; 20d=-2.10% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=37.3; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 跨层分歧信息有限，后续需补充更多波动与事件市场数据。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | medium |
| 1月 | 39% | 30% | 31% | bullish | 20日趋势维持上行，1月窗口偏多 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 8035.T price trend | close=75360.00; 1d=-0.95%; 5d=+10.82%; 20d=+51.23% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7111.00; 1d=-1.08%; 5d=+9.87%; 20d=+5.24% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3140.00; 1d=-3.38%; 5d=-4.62%; 20d=-10.92% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 0700.HK price trend | close=440.20; 1d=-1.17%; 5d=-3.72%; 20d=-3.30% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=21.28; 1d=-0.28%; 5d=-1.17%; 20d=-9.45% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=71.80; 1d=-3.49%; 5d=-8.07%; 20d=-13.34% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=24.58; 1d=-3.30%; 5d=-4.88%; 20d=-18.45% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=104.90; 1d=-1.87%; 5d=-2.33%; 20d=-20.38% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=108.90; 1d=-1.98%; 5d=+0.00%; 20d=-14.79% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=37.3; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| 0700.HK price trend | close=440.20; 1d=-1.17%; 5d=-3.72%; 20d=-3.30% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=21.28; 1d=-0.28%; 5d=-1.17%; 20d=-9.45% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=71.80; 1d=-3.49%; 5d=-8.07%; 20d=-13.34% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX Index / CBOE Volatility (indexcboe: vix) - Investing.com](https://www.investing.com/indices/volatility-s-p-500)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Live VIX Index quote, charts, historical data, analysis and news. View VIX (CBOE volatility index) price, based on real time data from S&P 500 options.

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [VIX S&P 500 Volatility and MOVE Treasury Volatility / StreetStats](https://streetstats.finance/markets/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：This page provides current and historical values for key volatility metrics, including the CBOE Volatility Index (VIX) for stock market volatility and the Merrill Lynch Option V...

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days out or more. IV is a forward looking prediction of the likelihood...

- [NDAQ Implied Volatility Chart Nasdaq - MarketChameleon.com](https://marketchameleon.com/Overview/NDAQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：View volatility charts for Nasdaq (NDAQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the interactive...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [ICE BofA Single-B US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A2HYB/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：For more data, go to the source. This data represents the Option-Adjusted Spread (OAS) of the ICE BofA US Corporate B Index, a subset of the ICE BofA US High Yield Master II Ind...

- [BAMLH0A0HYM2: US High Yield OAS Daily Data - eco3min.fr](https://eco3min.fr/en/credit-spreads-recession-risk-dataset/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：BAMLH0A0HYM2 is the ICE BofA US High Yield Index Option-Adjusted Spread — the daily market-priced premium that below-investment-grade US corporate bonds pay over equivalent-matu...

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

- [Valuta EX - Currency Converter / Real-Time Exchange Rates](https://valuta.exchange/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

- [USD JPY Exchange Rate, Live USD to JPY Forex Rate at Forex Rates](https://www.forexrates.net/fx-rates/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：USD JPY Exchange Rate This is the live USD JPY rate forex data page, displaying the FX price for the USD/JPY. The FX rate self-updates every few seconds. Compare exchange rates...

- [Live US Dollar to Yens Exchange Rate - $ 1 USD/JPY Today](https://usd.currencyrate.today/jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest and best $1 US Dollar to Yens rate for FREE. USD/JPY - Live exchange rates, banks, historical data & currency charts.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Current Values - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index?idx=nk225)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Current Values Nikkei calculates and publishes various types of the indexes such as the "Nikkei Stock Average (Nikkei 225)" which is known as a representative Japanese stock mar...

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
## [IAEA 欢迎美伊备忘录并提议核核查](https://news.un.org/feed/view/en/story/2026/06/1167748) ⭐️ 9.0/10

国际原子能机构（IAEA）欢迎一份旨在结束敌对行动的美伊初步备忘录，并提出协助核查伊朗核计划，这被视为解除制裁的关键条件。 这一降级信号可能为解除对伊朗制裁铺平道路，有助于稳定石油市场并降低地缘政治风险溢价。这也是解决长期核僵局的关键一步。 备忘录的具体内容尚未公开，核查需要伊朗的充分配合，而以往合作并不稳定。进展取决于技术会谈与政治意愿。

rss · UN News · Jun 18, 12:00

**背景**: 国际原子能机构（IAEA）是联合国下属机构，负责监督核活动。根据 2015 年《伊核协议》（JCPOA），伊朗同意限制核计划以换取制裁解除，但 2018 年美国退出后协议破裂。此后伊朗扩大铀浓缩活动，IAEA 在核查方面面临困难。这份新备忘录表明外交接触重新启动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/International_Atomic_Energy_Agency">International Atomic Energy Agency - Wikipedia</a></li>
<li><a href="https://www.iaea.org/topics/monitoring-and-verification-in-iran">Monitoring and Verification in Iran | IAEA</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#sanctions`, `#iran`, `#middle-east`, `#energy`

---

<a id="item-3"></a>
## [美联储发布 6 月 FOMC 经济预测](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm) ⭐️ 9.0/10

美联储发布了 6 月 16-17 日联邦公开市场委员会会议的经济预测摘要，更新了对 GDP 增长、失业率、通胀和联邦基金利率路径的预测。 这些预测，尤其是利率预期的点阵图，可能改变市场对未来货币政策的预期，进而影响债券收益率、股票估值和汇率。 点阵图显示每位 FOMC 参与者对年底和长期联邦基金利率的匿名预测，中位数预测通常驱动市场重新定价。

rss · Federal Reserve Press Releases · Jun 17, 18:00

**背景**: 联邦公开市场委员会（FOMC）是美联储系统的货币政策制定机构。每年召开八次会议，其中四次（通常为 3 月、6 月、9 月和 12 月）会后发布《经济预测摘要》。该报告包含每位成员对关键经济指标和联邦基金利率的预测，即“点阵图”。这些预测揭示了委员会的经济展望和政策倾向，是金融市场的重要参考。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Reserve_Board_of_Governors">Federal Reserve Board of Governors</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federal_Open_Market_Committee">Federal Open Market Committee</a></li>
<li><a href="https://www.investing.com/economic-calendar/fomc-economic-projections-1061">U.S. Federal Reserve (Fed) Economic Projections</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#bonds`, `#equities`, `#global-markets`

---

<a id="item-4"></a>
## [联合国欢迎黎巴嫩新停火报道，人权专家敦促伊朗问责](https://news.un.org/feed/view/en/story/2026/06/1167768) ⭐️ 8.0/10

联合国于 2026 年 6 月 19 日星期五对以色列和真主党达成的新停火协议表示欢迎，同时联合国人权专家另行呼吁追究伊朗在地区冲突中的责任。 此次停火若能持续，可能缓解中东重大冲突，降低全球能源市场的地缘政治风险溢价，并改善地区稳定。追究伊朗责任回应了人权关切，可能迫使德黑兰限制对代理人的军事支持。 据报道，此次停火由美国、卡塔尔和伊朗促成，此前数月停火协议脆弱且空袭不断。同时，平民仍在逃离受影响地区，联合国专家谴责了美以对伊朗的非法军事攻击。

rss · UN News · Jun 19, 12:00

**背景**: 自 2023 年 10 月以来，以色列与真主党冲突大幅升级，成为伊朗-以色列代理人战争的一部分，卷入多方并扰乱全球能源市场。2024 年和 2025 年的停火协议均昙花一现，2026 年伊朗战争进一步加剧地区动荡。霍尔木兹海峡与红海航运路线依然脆弱，影响石油供应安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Israel-Hezbollah_conflict_(2023-2024)">Israel-Hezbollah conflict (2023-2024)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Economic_impact_of_the_2026_Iran_war">Economic impact of the 2026 Iran war - Wikipedia</a></li>
<li><a href="https://www.nationaltribune.com.au/un-experts-call-for-de-escalation-and-accountability-iran/">UN experts call for de-escalation and accountability : Iran</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`, `#energy`

---

<a id="item-5"></a>
## [ECB 莱恩阐释欧元区经济前景](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260616~8076dabd2c.en.pdf) ⭐️ 8.0/10

欧洲央行首席经济学家菲利普·莱恩就欧元区经济前景发表讲话，传递了关于通胀、增长及货币政策的未来信号。 其言论可能影响市场对欧洲央行利率走向的预期，进而波及欧元区债券收益率和欧元汇率。 讲话可能提及近期通胀动态和最新的宏观经济预测，但具体政策承诺尚不确定。

rss · ECB Press Releases · Jun 16, 13:10

**背景**: 欧洲央行正面临通胀回落但经济活动疲软的局面。作为首席经济学家，莱恩的观点对管理委员会的政策决策有重大影响。市场密切关注其讲话，以寻找利率调整时机和步伐的线索。

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#currency`, `#global-markets`

---

<a id="item-6"></a>
## [联合国安理会辩论加沙危机，停火名存实亡](https://news.un.org/feed/view/en/story/2026/06/1167750) ⭐️ 7.0/10

联合国安理会应十个非常任理事国要求就加沙不断恶化的人道局势举行辩论。联合国救援负责人汤姆·弗莱彻报告称，自 2025 年 10 月名义停火以来，已有近 1000 名巴勒斯坦人被杀，大多数人仍流离失所。 此次辩论突显国际社会担忧加沙危机正被更广泛的地区紧张局势所掩盖，而安理会因否决权而无法采取行动，可能进一步损害外交信誉并加剧地区不稳定。 该停火协议自 2025 年 10 月以来仅‘名义上’存在，但暴力持续，近 1000 人死亡。汤姆·弗莱彻称当前进展仅是‘巴勒斯坦人需求的最低限度’，会议系由安理会非常任理事国召集。

rss · UN News · Jun 18, 12:00

**背景**: 负责维护国际和平的联合国安理会在加沙问题上陷入僵局，美国多次否决相关决议。2023 年 10 月爆发的以色列-哈马斯战争造成广泛破坏和人道灾难。2025 年 1 月达成的停火协议于 3 月破裂。2025 年 10 月宣布了新的停火协议，但违反行为持续，加沙大多数民众仍流离失所，面临严重的食物和医疗短缺。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gaza_humanitarian_crisis">Gaza humanitarian crisis</a></li>
<li><a href="https://www.aljazeera.com/news/liveblog/2025/10/9/live-israel-hamas-agree-on-first-phase-of-gaza-ceasefire-deal">Updates: Israel approves Gaza ceasefire deal; Hamas... | Al Jazeera</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-7"></a>
## [联合国儿童基金会：黎巴嫩停火后每日仍有 12 名儿童伤亡](https://news.un.org/feed/view/en/story/2026/06/1167736) ⭐️ 7.0/10

联合国儿童基金会报告称，在真主党与以色列停火后的 100 多天里，平均每天仍有 12 名儿童在黎巴嫩遭到杀害或伤残，突显出停火协议的脆弱性。 高企的儿童伤亡率表明停火并不稳固，可能重新引发更广泛的冲突，破坏中东稳定并扰乱能源市场；同时也揭示了一场不断加深的人道主义危机，亟需国际社会的紧急关注。 该报告涵盖了 100 多天的冲突，尽管 2024 年至 2026 年间停火协议多次延期和更新，但每日儿童伤亡数字依然居高不下。

rss · UN News · Jun 17, 12:00

**背景**: 真主党是伊朗支持的什叶派武装和政治团体，自 2023 年 10 月以来与以色列持续敌对，导致 2024 年黎巴嫩战争并达成多次停火。最近的停火于 2026 年 6 月 1 日根据美国提案达成，但暴力事件仍在发生。联合国儿童基金会是致力于儿童福利的联合国机构，负责监测和报告冲突地区的人道主义影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Israel–Lebanon_ceasefire">2026 Israel–Lebanon ceasefire - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/UNICEF">UNICEF</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`

---

<a id="item-8"></a>
## [欧央行皮耶罗·奇波洛内阐述数字欧元愿景](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260618~da08e71469.en.pdf) ⭐️ 7.0/10

欧洲央行执行委员会成员皮耶罗·奇波洛内发表演讲，详细阐述了数字欧元的目的，即在数字化经济中保持央行货币的相关性，并对支付、货币政策以及欧元的国际角色产生影响。 该演讲表明欧洲央行正战略性地推动数字欧元，这可能重塑欧洲支付体系，增强货币主权，改变全球货币竞争格局，同时引发对金融稳定和银行中介功能的关注。 欧洲央行的目标是在 2029 年之前做好首次发行数字欧元的准备，并从 2027 年年中开始测试，前提是欧盟在 2026 年通过相关立法；数字欧元将不采用区块链技术，免费使用，安全保密，并与现金互补。

rss · ECB Press Releases · Jun 18, 12:00

**背景**: 数字欧元是欧洲央行于 2021 年启动的央行数字货币（CBDC）项目，旨在探索欧元现金的电子形式。与去中心化的加密货币不同，CBDC 是央行的直接负债，旨在补充实物现金。该项目已历经调查和准备阶段，潜在推出取决于欧盟立法批准。全球还有 100 多个国家也在研究或试点 CBDC，包括中国的数字人民币。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_euro">Digital euro</a></li>
<li><a href="https://www.ecb.europa.eu/euro/digital_euro/html/index.en.html">Digital euro - European Central Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/Central_bank_digital_currency">Central bank digital currency</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#europe`, `#macroeconomics`, `#financial-stability`, `#global-markets`

---

<a id="item-9"></a>
## [ECB 工资追踪：2026 薪资压力稳定](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260617~79dfc49802.en.html) ⭐️ 7.0/10

欧央行工资追踪器显示，2025 年协商工资增长 3.2%，2026 年增长 2.3%，表明工资压力保持稳定。 持续的国内工资增长可能推迟欧洲央行的政策正常化，并影响欧元收益率和欧元汇率。 数据覆盖 2025 年 51.5%和 2026 年 43.2%的员工，基于九个欧元区国家的集体谈判协议。

rss · ECB Press Releases · Jun 17, 08:00

**背景**: 欧央行工资追踪器由欧洲央行与九国央行合作开发，追踪主要欧元区经济体的集体谈判协议中的协商工资。它有助于评估工资压力，这对通胀和货币政策决策至关重要。在高通胀时期，工资增长加速，工人寻求补偿，现在追踪器显示正常化趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260617~79dfc49802.en.html">New data release: ECB wage tracker points to stable negotiated wage pressures in 2026</a></li>
<li><a href="https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260506~4ea17afd4a.en.html">New data release: ECB wage tracker indicates negotiated wage pressures stable in 2026</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#currency`, `#bonds`

---

<a id="item-10"></a>
## [欧洲央行行长拉加德谈货币的数字化过渡](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260615~35e6c6c4de.en.html) ⭐️ 7.0/10

欧洲央行行长克里斯蒂娜·拉加德发表关于货币过渡的演讲，可能涉及数字欧元项目以及央行货币在支付系统中不断演变的角色。 该演讲表明了欧洲央行对央行数字货币的战略思路，这可能会重塑欧元区的货币政策实施、支付基础设施以及金融稳定。 数字欧元目前处于准备阶段，欧洲央行计划在 2026 年通过欧盟立法后，从 2027 年年中开始测试，目标是到 2029 年实现首次发行。

rss · ECB Press Releases · Jun 15, 07:30

**背景**: 欧洲央行于 2021 年 7 月启动数字欧元项目，旨在探索一种补充现金和银行存款的央行数字货币。准备阶段于 2023 年 11 月开始。欧洲央行的首要任务是维持物价稳定，任何数字欧元的设计都必须确保不会对货币政策传导或金融稳定产生负面影响。全球已有 130 多个国家在研究央行数字货币，少数国家已正式推出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_euro">Digital euro</a></li>
<li><a href="https://www.ecb.europa.eu/euro/digital_euro/html/index.en.html">Digital euro - European Central Bank</a></li>
<li><a href="https://www.ecb.europa.eu/mopo/html/index.en.html">Overview of monetary policy and markets</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#financial-stability`

---

<a id="item-11"></a>
## [联合国重申黎巴嫩维和人员行动自由](https://news.un.org/feed/view/en/story/2026/06/1167758) ⭐️ 6.0/10

联合国再次要求其驻黎巴嫩维和人员（联黎部队）能够自由行动，此举正值美伊达成临时协议之后。这凸显了黎巴嫩南部持续存在的行动限制和潜在摩擦。 行动不受阻碍对联黎部队监督停火和维护黎巴嫩南部稳定至关重要，直接影响地区安全。限制行动可能加剧真主党、以色列与黎巴嫩当局之间的紧张，并可能使初生的美伊外交重新调整复杂化。 联黎部队多次遭遇以色列国防军等行为体对其行动的限制，最近一次在 2026 年 4 月。美伊临时协议是一份 14 点框架文件，旨在结束为期 3 个半月的战争，取消制裁并为伊朗设立重建基金。

rss · UN News · Jun 18, 12:00

**背景**: 联合国驻黎巴嫩临时部队（联黎部队）于 1978 年成立，旨在核实以色列撤军并协助黎巴嫩政府恢复权力。其行动自由长期受到国家和非国家行为体的挑战，这反映了更广泛的地区紧张局势。美伊临时协议结束了一场短暂但激烈的战争，其条款可能重塑在黎巴嫩及更广泛地区的影响力，而伊朗支持的真主党是关键角色。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://unifil.unmissions.org/en/background">Background | UNIFIL</a></li>
<li><a href="https://www.timesofisrael.com/liveblog_entry/unifil-accuses-idf-of-harming-its-freedom-of-movement-in-southern-lebanon/">UNIFIL accuses IDF of harming its 'freedom of movement' in southern Lebanon | The Times of Israel</a></li>
<li><a href="https://www.brusselstimes.com/2198028/us-and-iran-sign-provisional-agreement-tbtb">US and Iran sign provisional agreement to end war</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`, `#united-states`

---

<a id="item-12"></a>
## [联合国特使警告：利比亚政治窗口收窄](https://news.un.org/feed/view/en/story/2026/06/1167757) ⭐️ 6.0/10

联合国特使汉娜·塞瓦·泰特警告称，利比亚政治进程虽重获动力，但采取行动的窗口正在收窄，加剧了再次陷入不稳定的风险。 利比亚作为主要石油出口国，其不稳定威胁到地区外交和全球能源市场；若未能确保选举，可能延长政治真空和冲突。 2024 年底联合国支持的计划旨在设立咨询委员会，解决选举法争议并为全国选举铺路，但执行已陷入停滞。

rss · UN News · Jun 18, 12:00

**背景**: 自 2011 年穆阿迈尔·卡扎菲被推翻以来，利比亚一直不稳定，分裂为的黎波里和东部两个对立政府。联合国利比亚支助团（UNSMIL）一直在调解以统一机构并举行选举。在前任努力失败后，2025 年任命了新特使汉娜·塞瓦·泰特。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2024/12/1158241">UN announces plan to address political impasse, overdue elections in Libya | UN News</a></li>
<li><a href="https://press.un.org/en/2024/sc15938.doc.htm">United Nations Libya Mission Unveils Plan to End Political Deadlock, Pave Way for National Elections | UN Meetings Coverage and Press Releases</a></li>
<li><a href="https://press.un.org/en/2024/sc15737.doc.htm">Libyans Overwhelmingly Want Political Agreement, Credible Elections ‘to Restore Legitimacy to All Institutions’, Briefer Tells Security Council | Meetings Coverage and Press Releases</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#energy`, `#sovereign-risk`

---

<a id="item-13"></a>
## [欧央行奇波洛内谈央行货币与主权](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260619~53145e5a0b.en.html) ⭐️ 6.0/10

欧央行执委会成员皮耶罗·奇波洛内强调，央行货币是国家货币自主权的支柱，暗示数字欧元可增强这一主权。 该言论表明欧央行致力于将数字欧元作为维持货币控制权的工具，尤其是在其他司法管辖区推进央行数字货币和私人数字货币涌现的背景下。 讲话正值数字欧元项目推进，可能在 2029 年前发行，但需欧盟立法批准；奇波洛内的论述可能暗示法律和技术上的优先事项。

rss · ECB Press Releases · Jun 19, 10:15

**背景**: 央行货币即基础货币，包括流通中现金和银行准备金。货币主权指国家发行货币和实施货币政策的排他性权利。欧央行自 2021 年起开发数字欧元（一种央行数字货币），目前处于准备阶段，目标在 2029 年前做好发行准备，但需待立法修改。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Central_bank_money">Central bank money</a></li>
<li><a href="https://grokipedia.com/page/monetary_sovereignty">Monetary sovereignty</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_euro">Digital euro</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#europe`, `#sovereign-risk`, `#financial-stability`, `#macroeconomics`

---

<a id="item-14"></a>
## [美联储提议要求稳定币发行方实施客户身份识别计划](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260618a.htm) ⭐️ 6.0/10

美联储委员会提出一项规则，要求某些支付稳定币发行方实施客户身份识别计划，作为反洗钱工作的一部分。 这标志着对稳定币更严格的监管，可能影响它们与传统金融的融合，并影响对国债等储备资产的需求。 该提案公开征求意见，具体要求尚未详细说明。它适用于特定的支付稳定币发行方，而非全部。

rss · Federal Reserve Press Releases · Jun 18, 13:00

**背景**: 客户身份识别计划（CIP）是美国《爱国者法案》下的监管要求，强制金融机构核实客户身份。支付稳定币是与稳定价值挂钩的数字资产，通常用于交易，发行方持有国债等储备。美联储一直在研究稳定币对货币政策和跨境支付的影响。该提案反映出监管机构对加密资产的日益关注，以确保金融体系完整性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.federalreserve.gov/econres/notes/feds-notes/payment-stablecoins-and-cross-border-payments-benefits-and-implications-for-monetary-policy-20260330.html">The Fed - Payment Stablecoins and Cross Border Payments: Benefits and Implications for Monetary Policy Implementation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Customer_Identification_Program">Customer Identification Program</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federal_Reserve_Board_of_Governors">Federal Reserve Board of Governors</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#bonds`, `#global-markets`

---