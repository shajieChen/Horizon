---
layout: default
title: "Horizon Summary: 2026-06-22 (ZH)"
date: 2026-06-22
lang: zh
---

> From 44 items, 16 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [IAEA 欢迎美伊备忘录，提议核核查协助](#item-2) ⭐️ 9.0/10
3. [欧洲央行行长拉加德谈“转型中的货币”](#item-3) ⭐️ 8.0/10
4. [美联储发布 6 月 FOMC 经济预测](#item-4) ⭐️ 8.0/10
5. [联合国对以色列与真主党新停火报告表示欢迎](#item-5) ⭐️ 7.0/10
6. [皮耶罗·奇波洛内谈数字欧元：货币的未来](#item-6) ⭐️ 7.0/10
7. [欧央行薪资追踪器显示 2026 年协商薪资压力稳定](#item-7) ⭐️ 7.0/10
8. [欧洲央行莱恩谈欧元区经济前景，暗示政策方向](#item-8) ⭐️ 7.0/10
9. [安理会警告苏丹欧拜伊德或发生大规模暴行](#item-9) ⭐️ 6.0/10
10. [UNICEF：加沙停火后 265 名儿童遇难](#item-10) ⭐️ 6.0/10
11. [联合国安理会就加沙严峻人道危机举行辩论](#item-11) ⭐️ 6.0/10
12. [联合国警告厄尔尼诺逼近，脆弱地区气候冲击加剧](#item-12) ⭐️ 6.0/10
13. [尽管停火，黎巴嫩每天仍有 12 名儿童伤亡：UNICEF](#item-13) ⭐️ 6.0/10
14. [欧洲央行执委埃尔德森炉边谈话论经济](#item-14) ⭐️ 6.0/10
15. [欧央行官员 Cipollone：央行货币是国家主权基石](#item-15) ⭐️ 6.0/10
16. [美联储提议稳定币发行方客户身份识别规则](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 21, 22:46

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
| ^NDX price trend | close=30406.19; 1d=+2.48%; 5d=+3.26%; 20d=+3.78% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=740.62; 1d=+2.51%; 5d=+3.28%; 20d=+3.85% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=30527.00; 1d=+0.87%; 5d=+2.92%; 20d=+3.67% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=20.5%; implied_move=1.2%; put/call OI=3.1463489373974802 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=37.3; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| ^NDX price trend | close=30406.19; 1d=+2.48%; 5d=+3.26%; 20d=+3.78% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=740.62; 1d=+2.51%; 5d=+3.28%; 20d=+3.85% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=30527.00; 1d=+0.87%; 5d=+2.92%; 20d=+3.67% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| AAPL price trend | close=298.01; 1d=+0.70%; 5d=+0.81%; 20d=-1.40% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=244.39; 1d=+2.90%; 5d=+1.19%; 20d=-7.78% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=210.69; 1d=+2.95%; 5d=+2.84%; 20d=-5.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=379.40; 1d=+0.13%; 5d=-2.80%; 20d=-9.70% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=577.22; 1d=+1.70%; 5d=+1.64%; 20d=-4.51% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=400.49; 1d=+1.04%; 5d=+0.34%; 20d=-4.02% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| MSFT options surface | ATM IV=32.5%; implied_move=1.8%; put/call OI=0.6482991112473184 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=36.4%; implied_move=2.1%; put/call OI=0.9844313545278578 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=40.4%; implied_move=2.3%; put/call OI=0.6340456157787412 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=32.2%; implied_move=1.7%; put/call OI=1.14329302746073 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=33.7%; implied_move=1.9%; put/call OI=0.7017292006525285 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=32.1%; implied_move=1.8%; put/call OI=0.6211624091867822 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| AAPL insider filings | recent Form4 count=589 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| NVDA insider filings | recent Form4 count=558 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=37.3; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
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
| AAPL price trend | close=298.01; 1d=+0.70%; 5d=+0.81%; 20d=-1.40% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=244.39; 1d=+2.90%; 5d=+1.19%; 20d=-7.78% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=210.69; 1d=+2.95%; 5d=+2.84%; 20d=-5.61% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 7203.T price trend | close=2776.50; 1d=-0.61%; 5d=+0.04%; 20d=-7.05% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77700.00; 1d=+0.23%; 5d=+7.00%; 20d=-2.10% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=75360.00; 1d=-0.95%; 5d=+10.82%; 20d=+51.23% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=96.26; 1d=+1.92%; 5d=+4.99%; 20d=+6.11% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3140.00; 1d=-3.38%; 5d=-4.62%; 20d=-10.92% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7111.00; 1d=-1.08%; 5d=+9.87%; 20d=+5.24% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=37.3; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 7203.T price trend | close=2776.50; 1d=-0.61%; 5d=+0.04%; 20d=-7.05% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77700.00; 1d=+0.23%; 5d=+7.00%; 20d=-2.10% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=75360.00; 1d=-0.95%; 5d=+10.82%; 20d=+51.23% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| KWEB price trend | close=25.24; 1d=-0.55%; 5d=-5.01%; 20d=-10.24% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=33.30; 1d=-1.04%; 5d=-3.90%; 20d=-7.42% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=21.28; 1d=-0.28%; 5d=-1.17%; 20d=-9.45% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=71.80; 1d=-3.49%; 5d=-8.07%; 20d=-13.34% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=24.58; 1d=-3.30%; 5d=-4.88%; 20d=-18.45% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=108.90; 1d=-1.98%; 5d=+0.00%; 20d=-14.79% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=37.3; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
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
| KWEB price trend | close=25.24; 1d=-0.55%; 5d=-5.01%; 20d=-10.24% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=33.30; 1d=-1.04%; 5d=-3.90%; 20d=-7.42% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=21.28; 1d=-0.28%; 5d=-1.17%; 20d=-9.45% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days out or more. IV is a forward looking prediction of the likelihood...

- [NDAQ Implied Volatility Chart Nasdaq - MarketChameleon.com](https://marketchameleon.com/Overview/NDAQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：View volatility charts for Nasdaq (NDAQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the interactive...

- [Volatility NASDAQ - 100 (NASDAQVOLNDX) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/NASDAQVOLNDX)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Graph and download economic data for Volatility NASDAQ - 100 (NASDAQVOLNDX) from 2010-07-23 to 2026-01-16 about volatility, NASDAQ, indexes, and USA.

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [MOVE Index (MOVE) - MacroMicro](https://en.macromicro.me/charts/35584/us-treasury-move-index)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：The Merrill Lynch Option Volatility Estimate (MOVE) Index reflects the level of volatility in U.S. Treasury futures. The index is considered a proxy for term premiums of U.S. Tr...

- [VIX S&P 500 Volatility and MOVE Treasury Volatility / StreetStats](https://streetstats.finance/markets/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：This page provides current and historical values for key volatility metrics, including the CBOE Volatility Index (VIX) for stock market volatility and the Merrill Lynch Option V...

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX Index / CBOE Volatility (indexcboe: vix) - Investing.com](https://www.investing.com/indices/volatility-s-p-500)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Live VIX Index quote, charts, historical data, analysis and news. View VIX (CBOE volatility index) price, based on real time data from S&P 500 options.

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://alfred.stlouisfed.org/series?seid=BAMLH0A0HYM2)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：Graph and download revisions to economic data for from 2023-06-19 to 2026-06-17 about option-adjusted spread, yield, interest rate, interest, rate, and USA.

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

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [Nikkei Average Volatility (^NKVI.OS) - Yahoo Finance](https://finance.yahoo.com/quote/%5ENKVI.OS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Find the latest information on Nikkei Average Volatility (^NKVI.OS) including data, charts, related news and more from Yahoo Finance

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

- [Index Information - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index/profile?idx=nk225vi)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：The Nikkei Stock Average Volatility Index are calculated by using prices of Nikkei 225 futures and Nikkei 225 options on the Osaka Exchange (OSE). In the calculation, taking nea...

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [iShares MSCI Japan ETF / EWJ](https://www.ishares.com/us/products/239665/ishares-msci-japan-etf)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：The iShares MSCI Japan ETF seeks to track an index composed of Japanese equities. The fund offers a way to express a single-country view and gain targeted exposure to companies...

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
## [IAEA 欢迎美伊备忘录，提议核核查协助](https://news.un.org/feed/view/en/story/2026/06/1167748) ⭐️ 9.0/10

国际原子能机构总干事对美伊签署谅解备忘录表示欢迎，并提出协助双方就核计划核查这一关键争议点开展技术会谈。 这可能缓解军事紧张局势，为制裁解除开辟道路，并稳定能源市场，如果核查取得进展并推动最终协议解决伊朗核计划问题，影响尤为显著。 该谅解备忘录包括 60 天停火、豁免伊朗石油出口制裁以及要求降低铀浓缩水平，但将核核查和导弹计划等问题推迟到未来谈判解决。

rss · UN News · Jun 18, 12:00

**背景**: 国际原子能机构是联合国的核监督机构，负责根据《联合全面行动计划》监督伊朗核活动。美国于 2018 年退出该协议，导致伊朗提高铀浓缩水平。2026 年 6 月签署的《伊斯兰堡备忘录》经巴基斯坦等国斡旋，旨在结束美伊军事冲突。该框架协议暂时停止敌对行动并提供制裁减免，但将核计划限制等关键问题留待 60 天内最终敲定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/International_Atomic_Energy_Agency">International Atomic Energy Agency</a></li>
<li><a href="https://en.wikipedia.org/wiki/US-Iran_Memorandum">US-Iran Memorandum</a></li>
<li><a href="https://www.bbc.com/news/articles/c4gy700j0eko">US - Iran memorandum of understanding in full</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#sanctions`, `#energy`

---

<a id="item-3"></a>
## [欧洲央行行长拉加德谈“转型中的货币”](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260615~35e6c6c4de.en.html) ⭐️ 8.0/10

欧洲央行行长克里斯蒂娜·拉加德就货币的演变性质发表演讲，可能预示了数字欧元或货币政策调整的即将出台计划。 此次演讲可能指明欧洲央行在央行数字货币和货币政策上的未来方向，这可能影响欧洲金融市场、银行盈利能力及欧元的国际地位。 该演讲于 2026 年 6 月 15 日发布在欧洲央行网站上，但尚无详细文本；市场参与者将关注数字欧元的具体时间表或设计特征。

rss · ECB Press Releases · Jun 15, 07:30

**背景**: 欧洲央行一直在探索数字欧元以补充现金，旨在维护货币主权并改善支付。拉加德此前曾强调欧元区需要适应金融数字化。演讲标题“转型中的货币”暗示关注货币和支付的转型。

**标签**: `#central-bank`, `#europe`, `#financial-stability`, `#digital-currency`, `#monetary-policy`

---

<a id="item-4"></a>
## [美联储发布 6 月 FOMC 经济预测](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617b.htm) ⭐️ 8.0/10

美联储发布了 6 月 16-17 日 FOMC 会议的经济预测摘要，更新了对 GDP 增长、失业率、通胀和联邦基金利率的预测。 这些预测，尤其是利率预期的“点阵图”，直接影响债券、股票和美元的市场定价，并塑造全球风险评估和货币政策前景。 经济预测摘要包含各变量的中位数、集中趋势和预测范围，点阵图则展示了每位 FOMC 委员对截至 2028 年及更长期的利率预测。

rss · Federal Reserve Press Releases · Jun 17, 18:00

**背景**: FOMC 是美联储的货币政策制定机构，每年召开八次会议。它每季度发布经济预测，包括有影响力的点阵图，该图展示了每位委员对联邦基金利率路径的预期，是投资者的重要参考。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Open_Market_Committee">Federal Open Market Committee</a></li>
<li><a href="https://fredblog.stlouisfed.org/2026/03/fomc-summary-of-economic-projections-march-2026/">FOMC Summary of Economic Projections, March 2026 | FRED Blog</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#bonds`, `#equities`, `#currency`

---

<a id="item-5"></a>
## [联合国对以色列与真主党新停火报告表示欢迎](https://news.un.org/feed/view/en/story/2026/06/1167768) ⭐️ 7.0/10

联合国对周五以色列与真主党之间新的停火协议报告表示欢迎，同时警告称，由于持续的不安全局势，平民仍在逃离。联合国人权专家还敦促追究伊朗在冲突中的责任。 此次停火降低了眼前的军事风险，有助于地区稳定和能源市场信心，联合国的支持增加了其合法性。对伊朗追究责任的呼吁或将对德黑兰施加外交压力，并影响未来的军备控制讨论。 该停火协议是在以色列继续在黎巴嫩南部行动以及黎巴嫩政府于 2025 年决定解除真主党武装的背景下达成的。联合国人权专家的声明特别指出伊朗对真主党的支持违反了国际法。

rss · UN News · Jun 19, 12:00

**背景**: 真主党是伊朗支持的黎巴嫩什叶派伊斯兰组织，曾与以色列爆发多次战争，包括 2006 年黎巴嫩战争和 2024 年冲突。联合国驻黎巴嫩临时部队（联黎部队）自 1978 年以来一直部署，监督停火并协助黎巴嫩政府。2025 年，黎巴嫩政府批准了解除真主党武装的计划，但执行仍面临挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Interim_Force_in_Lebanon">United Nations Interim Force in Lebanon - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Israel-Lebanon_conflict">Israel-Lebanon conflict</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-6"></a>
## [皮耶罗·奇波洛内谈数字欧元：货币的未来](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260618~da08e71469.en.pdf) ⭐️ 7.0/10

欧洲央行执行委员会成员皮耶罗·奇波洛内发表演讲，阐述了数字欧元的设计和益处，强调其在提高支付效率、增强货币主权和促进创新方面的作用。 此次高层表态突显了数字欧元对欧盟支付领域战略自主的重要性，并为未来的立法和技术里程碑奠定基础，可能对金融稳定和欧元的全球角色产生连锁影响。 关键细节：数字欧元不会采用区块链技术，计划在 2026 年欧盟立法通过后，于 2027 年中开始测试，2029 年发行；它将作为央行负债，免费使用，并在欧元区内普遍适用。

rss · ECB Press Releases · Jun 18, 12:00

**背景**: 数字欧元是欧洲央行于 2021 年 7 月启动的项目，旨在探索央行数字货币（CBDC），作为现金和银行存款的补充。货币主权，即国家对货币的排他性控制，推动该倡议减少对外国支付提供商的依赖，并巩固欧元的国际地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_euro">Digital euro</a></li>
<li><a href="https://www.ecb.europa.eu/euro/digital_euro/html/index.en.html">Digital euro - European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#europe`, `#financial-stability`, `#macroeconomics`, `#currency`

---

<a id="item-7"></a>
## [欧央行薪资追踪器显示 2026 年协商薪资压力稳定](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260617~79dfc49802.en.html) ⭐️ 7.0/10

欧央行于 2026 年 6 月 17 日发布的最新薪资追踪数据显示，欧元区协商薪资增长率在 2026 年预计为 2.3%，与先前估算持平，该数据基于覆盖 43.2%雇员的集体协议。 薪资前景稳定表明国内通胀压力并未加剧，这为欧央行维持利率不变提供了依据，降低了进一步紧缩的可能性，从而安抚了债券市场和欧元。 2026 年 2.3%的增长率低于 2025 年的 3.2%，且协议覆盖率已从上个月的 41.9%提升至 43.2%，增强了指标的可靠性。该追踪指数仍低于 2023-2024 年的峰值水平。

rss · ECB Press Releases · Jun 17, 08:00

**背景**: 欧央行薪资追踪器是一个前瞻性指标，通过汇总欧元区各国的集体协议来预判未来薪资压力。协商薪资是服务业通胀和整体通胀持续性的关键驱动因素，因此欧央行在制定利率时会密切监测其走势。疫情后薪资追赶效应逐渐消退，该追踪器一直显示薪资压力逐步放缓，与欧央行中期 2%的通胀目标保持一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260617~79dfc49802.en.html">New data release: ECB wage tracker points to stable negotiated wage pressures in 2026</a></li>
<li><a href="https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260506~4ea17afd4a.en.html">New data release: ECB wage tracker indicates negotiated wage pressures stable in 2026</a></li>
<li><a href="https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op338~dd97c1f69e.pt.pdf">A forward-looking tracker of negotiated wages in the euro area</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#bonds`, `#currency`

---

<a id="item-8"></a>
## [欧洲央行莱恩谈欧元区经济前景，暗示政策方向](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260616~8076dabd2c.en.pdf) ⭐️ 7.0/10

2026 年 6 月 16 日，欧洲央行首席经济学家菲利普·莱恩发表讲话，评估欧元区经济前景，可能暗示央行在通胀和增长动态变化中的下一步利率行动。 莱恩的讲话可能改变市场对欧洲央行货币政策的预期，进而影响欧元汇率、债券收益率和欧洲股市。作为首席经济学家，他的观点对管理委员会即将做出的决策有重要影响。 讲话已在欧洲央行官网发布，但完整讲稿尚未立即公开；市场将分析其中关于工资增长、服务业通胀或贸易风险的任何评论，以判断降息时机。

rss · ECB Press Releases · Jun 16, 13:10

**背景**: 欧洲央行为 21 个成员国组成的欧元区制定货币政策。首席经济学家菲利普·莱恩在政策方向上具有重要发言权。由于通胀虽已放缓但仍高于 2%的目标，且增长乏力，每次欧洲央行的沟通都被仔细审视，以寻找是否进一步降息或维持利率的线索。自 2024 年年中以来，随着通胀缓解，欧洲央行已多次降息，但近期全球贸易紧张局势和内部因素增加了不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/">European Central Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank_(ECB)">European Central Bank (ECB)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Eurozone">Eurozone</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#currency`, `#bonds`

---

<a id="item-9"></a>
## [安理会警告苏丹欧拜伊德或发生大规模暴行](https://news.un.org/feed/view/en/story/2026/06/1167773) ⭐️ 6.0/10

联合国安理会对快速支援部队在苏丹欧拜伊德周围大规模增兵的报道表示震惊，并警告可能发动地面进攻，引发大规模暴行风险。 这一警告表明苏丹内战严重升级，危及地区稳定，可能引发国际外交或制裁反应，并对数百万平民造成灾难性人道主义后果。 快速支援部队是一支准军事力量，有记录显示其犯下战争罪、种族灭绝和性暴力；欧拜伊德是北科尔多凡州首府，不久前刚被苏丹军队打破近两年的围困，此次增兵引发对再次进攻的担忧。

rss · UN News · Jun 20, 12:00

**背景**: 快速支援部队源于金戈威德民兵，自 2023 年 4 月起与苏丹武装部队交战，犯下大规模暴行。联合国安理会负责维护国际和平与安全，已多次对这场已导致近 1400 万人流离失所、造成严重人道主义危机的冲突表示关切。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aljazeera.com/news/2026/6/18/dozens-of-countries-warn-of-atrocities-amid-escalation-in-sudans-el-obeid">At least 29 countries raise alarm about atrocities in Sudan ’s el - Obeid</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rapid_Support_Forces_(Sudan)">Rapid Support Forces (Sudan)</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#sovereign-risk`

---

<a id="item-10"></a>
## [UNICEF：加沙停火后 265 名儿童遇难](https://news.un.org/feed/view/en/story/2026/06/1167760) ⭐️ 6.0/10

联合国儿童基金会报告称，自 2025 年 10 月停火生效以来，加沙地带已有 265 名巴勒斯坦儿童遇难；与此同时，黎巴嫩再次爆发冲突，援助机构发出新警报。 此事凸显了持续的人道主义危机和可能的停火违规行为，可能增加对以色列的外交压力，引发联合国安理会讨论，并影响地区稳定及国际对冲突的政策。 联合国儿童基金会统计的 265 名儿童死亡数字反映了尽管存在多边停火协议，暴力仍在持续；据半岛电视台报道，停火后已有 442 名巴勒斯坦人丧生，且黎巴嫩冲突再起加剧了地区动荡。

rss · UN News · Jun 19, 12:00

**背景**: 2025 年 10 月停火，即《结束加沙冲突全面计划》，是由美国斡旋并经联合国安理会认可的多边协议，旨在停止敌对行动、释放人质，并启动加沙非军事化和重建。然而，协议执行因以色列几乎每日的违规行为以及哈马斯解除武装谈判停滞而受阻。此次警告发布之际，黎巴嫩也再度爆发暴力事件，当地脆弱的停火同样面临压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/October_2025_Gaza_ceasefire">October 2025 Gaza ceasefire</a></li>
<li><a href="https://www.aljazeera.com/news/2025/11/11/how-many-times-has-israel-violated-the-gaza-ceasefire-here-are-the-numbers">How many times has Israel violated the Gaza ceasefire ? | Al Jazeera</a></li>
<li><a href="https://x.com/UN_News_Centre/status/2051422869469770085">Lebanon's fragile ceasefire is being tested by renewed violence and ...</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#geopolitics`, `#diplomacy`, `#military-risk`

---

<a id="item-11"></a>
## [联合国安理会就加沙严峻人道危机举行辩论](https://news.un.org/feed/view/en/story/2026/06/1167750) ⭐️ 6.0/10

应十个非常任理事国要求，联合国安理会就加沙严峻人道局势举行辩论。联合国救援负责人汤姆·弗莱彻指出，自 2025 年 10 月停火以来，近千名巴勒斯坦人被杀，大多数人仍流离失所，进展仅为“最低限度”。 此次辩论凸显加沙停火的脆弱性，若人道状况恶化可能引发更广泛地区不稳定，因为停火未能遏制暴力和流离失所。 尽管有 2025 年 10 月停火协议，仍有近千名巴勒斯坦人被杀，大多数加沙人仍在境内流离失所。联合国官员称进展仅为最低限度，且辩论由非常任理事国要求举行，表明常任理事国之外也有关切。

rss · UN News · Jun 18, 12:00

**背景**: 联合国安理会由五个常任理事国（中、法、俄、英、美）和十个任期两年的非常任理事国组成。2025 年 10 月以色列与哈马斯达成停火协议，但暴力持续。汤姆·弗莱彻是联合国主管人道主义事务的副秘书长兼紧急救济协调员，负责人道协调厅。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council">United Nations Security Council - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tom_Fletcher_(diplomat)">Tom Fletcher (diplomat) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gaza_peace_plan">Gaza peace plan - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#gaza`, `#humanitarian`

---

<a id="item-12"></a>
## [联合国警告厄尔尼诺逼近，脆弱地区气候冲击加剧](https://news.un.org/feed/view/en/story/2026/06/1167753) ⭐️ 6.0/10

联合国机构周四警告称，在厄尔尼诺可能发生前，脆弱地区的极端天气风险正在加剧，威胁着粮食安全、流离失所和经济困难。 这一警报表明脆弱发展中国家面临粮食安全、供应链和经济稳定的潜在系统性风险，可能传导至大宗商品价格压力和更广泛的人道主义需求。 该警告基于日益加剧的气候模式，但厄尔尼诺的确切时间和强度仍不确定；过去事件曾与东南亚、澳大利亚和非洲部分地区的干旱以及南美洲的洪水相关。

rss · UN News · Jun 18, 12:00

**背景**: 厄尔尼诺是厄尔尼诺-南方涛动（ENSO）的暖位相，特征为热带太平洋中部和东部海面温度高于正常水平。它扰乱全球天气模式，通常每隔 2 到 7 年发生一次，并可能在不同地区引发严重干旱或洪水。依赖农业和渔业的发展中国家所受影响尤其严重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/El_Niño–Southern_Oscillation">El Niño–Southern Oscillation</a></li>
<li><a href="https://www.climate.gov/enso">El Niño & La Niña (El Niño-Southern Oscillation) | NOAA Climate.gov</a></li>

</ul>
</details>

**标签**: `#commodities`, `#supply-chain`, `#macroeconomics`, `#global-markets`, `#energy`

---

<a id="item-13"></a>
## [尽管停火，黎巴嫩每天仍有 12 名儿童伤亡：UNICEF](https://news.un.org/feed/view/en/story/2026/06/1167736) ⭐️ 6.0/10

联合国儿童基金会报告称，尽管真主党与以色列达成停火，但超过 100 天的冲突导致黎巴嫩平均每天有 12 名儿童丧生或致残。 持续的平民伤亡凸显停火协议十分脆弱，可能导致局势再次升级，进一步破坏地区稳定并引来外部调解方介入。 报告强调存在强迫流离失所现象，且以色列仍对黎巴嫩南部发动袭击，真主党指责以色列违反停火协议。

rss · UN News · Jun 17, 12:00

**背景**: 真主党是黎巴嫩什叶派准军事和政治组织，自 2023 年 10 月起与以色列爆发公开冲突。双方虽达成停火，但协议岌岌可危，以色列仍在黎巴嫩南部间歇性采取军事行动。黎巴嫩政府近期根据美国支持的计划着手解除真主党武装。联合国儿童基金会是专注于儿童福祉的联合国机构，在全球冲突地区开展工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://www.trtworld.com/article/18237408">Tens of thousands head home as Israel 's truce with Hezbollah holds</a></li>
<li><a href="https://economictimes.indiatimes.com/news/defence/hezbollah-says-israel-bears-full-responsibility-for-truce-violations/articleshow/131879118.cms">Hezbollah says Israel bears 'full responsibility' for truce violations</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`

---

<a id="item-14"></a>
## [欧洲央行执委埃尔德森炉边谈话论经济](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260619_1~09441a4cbe.en.html) ⭐️ 6.0/10

2026 年 6 月 19 日，欧洲央行执行董事会成员弗兰克·埃尔德森参加炉边谈话，讨论经济与金融议题。 作为欧洲央行高级官员，埃尔德森的言论可能暗示货币政策或金融监管的微妙变化，进而影响市场预期和资产价格。 炉边对话形式意味着讨论可能轻松但坦诚；未立即公开文字记录或详细议程，分析师需仔细研判其关于利率或气候风险的即兴评论。

rss · ECB Press Releases · Jun 19, 10:30

**背景**: 弗兰克·埃尔德森自 2020 年起担任欧洲央行执行董事会成员，负责法律事务，并兼任欧洲央行监事会副主席。此前，他曾在荷兰央行担任执行董事，主管监管工作。他经常就货币政策、金融稳定与气候变化的交叉议题发表讲话。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Frank_Elderson">Frank Elderson - Wikipedia</a></li>
<li><a href="https://www.ecb.europa.eu/ecb/decisions/html/cvelderson.en.html">Frank Elderson - European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#europe`, `#macroeconomics`, `#financial-stability`, `#global-markets`

---

<a id="item-15"></a>
## [欧央行官员 Cipollone：央行货币是国家主权基石](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260619~53145e5a0b.en.html) ⭐️ 6.0/10

欧央行执委 Piero Cipollone 发表演讲，强调央行货币是国家主权的基础，可能谈及数字欧元及全球货币动态。该演讲突显了欧央行将数字欧元作为主权工具的持续推进。 该演讲表明欧央行将维护货币主权作为战略重点，可能影响数字欧元的设计及其在对抗私有数字货币或他国央行数字货币中的角色。这或影响市场对欧元国际地位及欧盟监管努力的预期。 该演讲日期标注为 2026 年 6 月 19 日，正值欧央行推动数字欧元项目，目标 2029 年潜在发行，2027 年中开始测试。Cipollone 可能讨论了主权数字货币所需的法律和技术基础。

rss · ECB Press Releases · Jun 19, 10:15

**背景**: 央行货币包括实物现金和数字储备，是国家支付系统和货币主权的基石。欧央行自 2021 年起研究数字欧元，以确保公众在数字化经济中仍能使用央行货币。数字欧元将成为 ECB 的负债，补充现金，旨在提供独立于外国支付系统的欧洲支付解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Central_bank_money">Central bank money</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_euro">Digital euro</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#currency`, `#macroeconomics`, `#europe`, `#financial-stability`

---

<a id="item-16"></a>
## [美联储提议稳定币发行方客户身份识别规则](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260618a.htm) ⭐️ 6.0/10

美联储正在就一项提案征求公众意见，该提案要求特定支付稳定币发行机构建立并维护有效的客户身份识别计划，从而使稳定币业务与传统反洗钱标准接轨。 此举标志着美国对稳定币的监管显著收紧，可能通过要求其遵守类似于银行的《银行保密法》合规义务，影响稳定币的采用、运营成本及整个加密市场。 该提案可能适用于根据《天才法案》等联邦框架被认定为“许可支付稳定币发行机构”的主体，评论期允许行业利益相关方在规则最终确定前提出意见。

rss · Federal Reserve Press Releases · Jun 18, 13:00

**背景**: 稳定币是一种旨在维持与美元等资产挂钩的稳定价值的加密货币。《天才法案》是一项立法提案，旨在为支付稳定币建立全面的联邦监管框架，将其发行机构视为反洗钱法下的金融机构。美联储理事会作为美国中央银行的主要管理机构，有权对金融机构发布法规，包括根据《银行保密法》制定客户身份识别相关规则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-24.html">GENIUS Act: Reporting Forms and Instructions for Permitted Payment ...</a></li>
<li><a href="https://www.stlouisfed.org/on-the-economy/2025/dec/regulated-payment-stablecoins-become-reality-us">Regulated Payment Stablecoins Become a Reality in the U.S.</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#united-states`, `#stablecoin`, `#regulation`

---