---
layout: default
title: "Horizon Summary: 2026-06-21 (ZH)"
date: 2026-06-21
lang: zh
---

> From 44 items, 11 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [美联储维持利率在 3.5%-3.75%区间并发布经济预测](#item-2) ⭐️ 10.0/10
3. [IAEA 欢迎美伊备忘录并愿协助核核查](#item-3) ⭐️ 9.0/10
4. [联合国欢迎以黎停火报道，人权专家敦促伊朗问责](#item-4) ⭐️ 8.0/10
5. [欧洲央行首席经济学家连恩谈欧元区经济前景](#item-5) ⭐️ 8.0/10
6. [安理会讨论加沙严峻局势](#item-6) ⭐️ 7.0/10
7. [欧洲央行工资追踪器显示 2026 年薪资压力稳定](#item-7) ⭐️ 7.0/10
8. [美联储提议要求稳定币发行人建立客户识别程序](#item-8) ⭐️ 7.0/10
9. [联合国特使：利比亚政治进程势头恢复但行动窗口收窄](#item-9) ⭐️ 6.0/10
10. [联合国儿童基金会：停火期间黎巴嫩每日有 12 名儿童死伤](#item-10) ⭐️ 6.0/10
11. [欧洲央行行长拉加德暗示数字欧元与支付改革](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · Jun 20, 22:44

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
| NQ=F price trend | close=30647.00; 1d=+1.27%; 5d=+3.32%; 20d=+4.07% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=740.62; 1d=+2.51%; 5d=+3.28%; 20d=+3.85% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=30406.19; 1d=+2.48%; 5d=+3.26%; 20d=+3.78% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=16.7%; implied_move=1.2%; put/call OI=3.1215094884190777 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

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
| NQ=F price trend | close=30647.00; 1d=+1.27%; 5d=+3.32%; 20d=+4.07% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=740.62; 1d=+2.51%; 5d=+3.28%; 20d=+3.85% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=30406.19; 1d=+2.48%; 5d=+3.26%; 20d=+3.78% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| GOOGL price trend | close=368.03; 1d=+1.17%; 5d=+2.87%; 20d=-5.31% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=379.40; 1d=+0.13%; 5d=-2.80%; 20d=-9.70% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=298.01; 1d=+0.70%; 5d=+0.81%; 20d=-1.40% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=577.22; 1d=+1.70%; 5d=+1.64%; 20d=-4.51% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=210.69; 1d=+2.95%; 5d=+2.84%; 20d=-5.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=400.49; 1d=+1.04%; 5d=+0.34%; 20d=-4.02% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| GOOGL options surface | ATM IV=26.3%; implied_move=1.7%; put/call OI=1.143438453713123 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=29.7%; implied_move=2.1%; put/call OI=0.9844313545278578 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=26.5%; implied_move=1.8%; put/call OI=0.6471850852446952 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=27.5%; implied_move=1.9%; put/call OI=0.7012071778140294 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=26.2%; implied_move=1.8%; put/call OI=0.6221465876415704 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=33.0%; implied_move=2.3%; put/call OI=0.6534623739469827 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| AAPL insider filings | recent Form4 count=589 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| CNN Fear & Greed | score=37.3; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| NVDA insider filings | recent Form4 count=558 | 内部人交易节奏可作为估值温度辅助校验信号。 |

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
| GOOGL price trend | close=368.03; 1d=+1.17%; 5d=+2.87%; 20d=-5.31% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=379.40; 1d=+0.13%; 5d=-2.80%; 20d=-9.70% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=298.01; 1d=+0.70%; 5d=+0.81%; 20d=-1.40% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 bullish/neutral/neutral，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 6758.T price trend | close=3140.00; 1d=-3.38%; 5d=-4.62%; 20d=-10.92% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=75360.00; 1d=-0.95%; 5d=+10.82%; 20d=+51.23% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77700.00; 1d=+0.23%; 5d=+7.00%; 20d=-2.10% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7111.00; 1d=-1.08%; 5d=+9.87%; 20d=+5.24% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=96.26; 1d=+1.92%; 5d=+4.99%; 20d=+6.11% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2776.50; 1d=-0.61%; 5d=+0.04%; 20d=-7.05% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=37.3; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |
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
| 6758.T price trend | close=3140.00; 1d=-3.38%; 5d=-4.62%; 20d=-10.92% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=75360.00; 1d=-0.95%; 5d=+10.82%; 20d=+51.23% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77700.00; 1d=+0.23%; 5d=+7.00%; 20d=-2.10% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 3690.HK price trend | close=71.80; 1d=-3.49%; 5d=-8.07%; 20d=-13.34% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=24.58; 1d=-3.30%; 5d=-4.88%; 20d=-18.45% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=25.24; 1d=-0.55%; 5d=-5.01%; 20d=-10.24% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=33.30; 1d=-1.04%; 5d=-3.90%; 20d=-7.42% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=440.20; 1d=-1.17%; 5d=-3.72%; 20d=-3.30% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=21.28; 1d=-0.28%; 5d=-1.17%; 20d=-9.45% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.46; 2Y=4.19; 10Y-2Y=0.2699999999999996 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=37.3; rating=fear | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| 3690.HK price trend | close=71.80; 1d=-3.49%; 5d=-8.07%; 20d=-13.34% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=24.58; 1d=-3.30%; 5d=-4.88%; 20d=-18.45% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=25.24; 1d=-0.55%; 5d=-5.01%; 20d=-10.24% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/neutral，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [Volatility NASDAQ - 100 (NASDAQVOLNDX) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/NASDAQVOLNDX)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Graph and download economic data for Volatility NASDAQ - 100 (NASDAQVOLNDX) from 2010-07-23 to 2026-01-16 about volatility, NASDAQ, indexes, and USA.

- [NDAQ Implied Volatility Chart Nasdaq - MarketChameleon.com](https://marketchameleon.com/Overview/NDAQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：View volatility charts for Nasdaq (NDAQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the interactive...

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

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

- [CBOE Volatility Index: VIX (VIXCLS) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/VIXCLS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Graph and download economic data for CBOE Volatility Index: VIX (VIXCLS) from 1990-01-02 to 2026-06-17 about VIX, volatility, stock market, and USA.

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [BAMLH0A0HYM2: US High Yield OAS Daily Data - eco3min.fr](https://eco3min.fr/en/credit-spreads-recession-risk-dataset/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：BAMLH0A0HYM2 is the ICE BofA US High Yield Index Option-Adjusted Spread — the daily market-priced premium that below-investment-grade US corporate bonds pay over equivalent-matu...

- [ICE BofA Single-B US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A2HYB/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：For more data, go to the source. This data represents the Option-Adjusted Spread (OAS) of the ICE BofA US Corporate B Index, a subset of the ICE BofA US High Yield Master II Ind...

- [QQQ Options - Live IV, Flow, Greeks & Analysis / ImpliedOptions ...](https://impliedoptions.com/ticker/qqq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Trade QQQ options with real-time implied volatility, IV rank, options flow, and Greeks. Analyze QQQ calls and puts with our free calculator and strategy builder.

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [USD/JPY — US Dollar to Japanese Yen Live Exchange Rate](https://www.live-rates.com/rates/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：The US Dollar (USD) is the world's primary reserve currency and the most traded currency on the foreign exchange market; the Japanese Yen (JPY) is the currency of Japan and the...

- [USD JPY / US Dollar to Yen Live Rate - Investing.com](https://www.investing.com/currencies/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get real time data on the USD/JPY pair including the live rate, as well as our currency converter, analysis, news, historical data and more.

- [Valuta EX - Currency Converter / Real-Time Exchange Rates](https://valuta.exchange/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

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
## [美联储维持利率在 3.5%-3.75%区间并发布经济预测](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm) ⭐️ 10.0/10

联邦公开市场委员会将联邦基金利率目标区间维持在 3.5%至 3.75%不变，并发布了包括 GDP、失业率和通胀预测在内的季度经济预测摘要。 这一决定和预测影响着未来利率走向的预期，直接波及债券收益率、股票估值和美元汇率，同时传递了美联储对增长与通胀风险的评估。 更新的经济预测摘要包含了决策者对未来几年利率预测的“点阵图”，为利率的可能路径提供线索。

rss · Federal Reserve Press Releases · Jun 17, 18:00

**背景**: 联邦公开市场委员会（FOMC）是美国央行的货币政策决策机构，每年召开八次会议设定联邦基金利率，即银行间隔夜拆借准备金的利率。美联储的双重使命是促进最大就业和物价稳定。季度经济预测摘要提供了与会者对关键经济变量和适当政策节奏的预测。声明中的前瞻指引传达委员会对前景和政策意图的看法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm">Federal Reserve Board - Federal Reserve issues FOMC statement</a></li>
<li><a href="https://www.federalreserve.gov/monetarypolicy/fomc.htm">The Fed - Federal Open Market Committee</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#bonds`, `#equities`, `#global-markets`

---

<a id="item-3"></a>
## [IAEA 欢迎美伊备忘录并愿协助核核查](https://news.un.org/feed/view/en/story/2026/06/1167748) ⭐️ 9.0/10

国际原子能机构总干事欢迎美伊签署谅解备忘录，并提议协助进行核核查，这是实施初步停火框架的关键一步。 这一进展标志着重大外交突破，可能导致中东紧张局势缓和、美国对伊朗石油制裁的解除，并对全球石油供应和能源市场产生深远影响。 备忘录规定了 60 天停火，并计划在 IAEA 监督下稀释浓缩铀，但浓缩水平等核心问题留待后续谈判；美国仅在签署最终协议时才会解除对伊朗石油出口的制裁。

rss · UN News · Jun 18, 12:00

**背景**: IAEA 通过保障监督体系负责核查各国是否将核材料仅用于和平目的。几十年来，伊朗核计划一直是国际紧张局势的根源，外界担忧其可能发展核武器。2025-2026 年的谈判是在美伊军事冲突升级后启动的，旨在结束敌对状态并解决核问题。伊朗石油工业长期受到美国制裁的打击，该协议将开始解除这些制裁，可能恢复大量原油出口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2025–2026_Iran–United_States_negotiations">2025–2026 Iran–United States negotiations - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/06/17/world/europe/us-iran-oil-sanctions.html">U.S. Will Waive Oil Sanctions That Have Long Crimped Iran</a></li>
<li><a href="https://www.iaea.org/topics/safeguards-and-verification">Safeguards and verification | IAEA</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#sanctions`, `#energy`, `#middle-east`, `#military-risk`

---

<a id="item-4"></a>
## [联合国欢迎以黎停火报道，人权专家敦促伊朗问责](https://news.un.org/feed/view/en/story/2026/06/1167768) ⭐️ 8.0/10

周五，联合国对以色列与真主党之间达成新停火协议的报道表示欢迎，同时联合国人权专家呼吁就伊朗在冲突中的作用追究其责任。 停火可能缓解地区紧张局势，减少能源供应中断风险，稳定全球市场。追究伊朗的责任或将为国家支持武装团体行为树立先例。 尽管联合国对报道表示欢迎，但仍警告称平民仍在因不安全局势逃离，停火的落实尚不确定。以往的停火协议十分脆弱，真主党的解除武装进程仍在争议中推进。

rss · UN News · Jun 19, 12:00

**背景**: 真主党是一个黎巴嫩什叶派伊斯兰政治和军事组织，1982 年在伊朗支持下成立，是反以色列的“抵抗轴心”组成部分。该组织与以色列多次冲突，包括 2006 年黎巴嫩战争和 2023 年 10 月以来的敌对行动引发的 2024 年冲突。真主党被许多西方国家列为恐怖组织。联合国安理会决议要求解除其武装，黎巴嫩政府在 2025-2026 年已采取措施推进此事。中东冲突地区对全球能源流动至关重要，那里的动荡可能导致油价飙升，威胁能源安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://en.wikipedia.org/wiki/Energy_supply_disruption">Energy supply disruption</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#energy`, `#global-markets`

---

<a id="item-5"></a>
## [欧洲央行首席经济学家连恩谈欧元区经济前景](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260616~8076dabd2c.en.pdf) ⭐️ 8.0/10

2026 年 6 月 16 日，欧洲央行首席经济学家菲利普·连恩发表讲话，讨论欧元区当前经济前景，可能透露未来货币政策走向的线索。 作为核心决策者，连恩的言论可能影响市场对利率的预期，进而波及欧元、主权债券及欧元区整体金融状况。 此次讲话属于欧洲央行的常规沟通，虽未宣布即时政策变动，但可能包含对通胀、增长及风险的评估，影响下一次管理委员会决策。

rss · ECB Press Releases · Jun 16, 13:10

**背景**: 欧洲央行（ECB）负责欧元区的货币政策，以维持物价稳定为首要目标。首席经济学家菲利普·连恩在经济分析和政策建议中发挥关键作用。欧元区由 20 个已采用欧元的欧盟成员国组成，金融市场高度一体化。欧洲央行的讲话常被密切关注，以寻找未来利率路径的信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://european-union.europa.eu/institutions-law-budget/institutions-and-bodies/search-all-eu-institutions-and-bodies/european-central-bank-ecb_en">European Central Bank ( ECB ) | European Union</a></li>
<li><a href="https://economy-finance.ec.europa.eu/euro/what-euro-area_en">What is the euro area ? - Economy and Finance - European ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Monetary_policy">Monetary policy - Wikipedia</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#currency`, `#bonds`

---

<a id="item-6"></a>
## [安理会讨论加沙严峻局势](https://news.un.org/feed/view/en/story/2026/06/1167750) ⭐️ 7.0/10

联合国安理会应 10 个非常任理事国请求召开会议，讨论加沙持续的人道主义危机。救济负责人汤姆·弗莱彻报告称，尽管自 2025 年 10 月起停火，但改善仅为'脆弱的成果'和'最低限度'。 这场高级别辩论表明国际社会持续外交关注加沙，可能影响安理会未来决议、援助准入及更广泛的中东政策，同时凸显若停火崩溃则存在升级风险。 名义上自 2025 年 10 月生效的停火已造成近千名巴勒斯坦人死亡，大多数加沙人仍流离失所，联合国紧急救济协调员汤姆·弗莱彻强调改善甚微。

rss · UN News · Jun 18, 12:00

**背景**: 联合国安理会由 15 个成员组成：5 个常任理事国（中国、法国、俄罗斯、英国、美国）拥有否决权，10 个非常任理事国由大会选举产生，任期两年。汤姆·弗莱彻自 2024 年 10 月起担任主管人道主义事务副秘书长兼紧急救济协调员，领导人道主义事务协调厅。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council">United Nations Security Council - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Emergency_Relief_Co-ordinator">UN Emergency Relief Co-ordinator</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`, `#humanitarian`

---

<a id="item-7"></a>
## [欧洲央行工资追踪器显示 2026 年薪资压力稳定](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260617~79dfc49802.en.html) ⭐️ 7.0/10

欧洲央行最新工资追踪数据显示，2025 年协议工资增长（含平滑处理的一次性支付）为 3.2%，2026 年预计降至 2.3%，表明薪资压力趋于稳定。 薪资压力稳定降低了工资-物价螺旋上升的风险，强化了通胀放缓前景，为欧洲央行放松货币政策提供依据，可能压低债券收益率并削弱欧元。 该追踪器涵盖参与欧元区国家约 49.5%的员工，对一次性支付进行 12 个月平滑处理，并基于七个主要经济体的集体谈判协议数据。

rss · ECB Press Releases · Jun 17, 08:00

**背景**: 欧洲央行工资追踪器利用微观集体谈判数据实时监测协议工资增长。在 2023 年通胀飙升期间，协议工资增速曾超过 5%，此后逐步回落，这对欧洲央行判断通胀正回归 2%目标至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.einnews.com/pr_news/876807723/new-data-release-ecb-wage-tracker-suggests-lower-wage-growth-and-gradual-normalisation-of-negotiated-wage-pressures-in-2026">New data release: ECB wage tracker suggests lower wage growth...</a></li>
<li><a href="https://cryptobriefing.com/ecb-wage-tracker-stable-pressures-2026/">European Central Bank wage tracker shows stable wage pressures ...</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#bonds`, `#currency`

---

<a id="item-8"></a>
## [美联储提议要求稳定币发行人建立客户识别程序](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260618a.htm) ⭐️ 7.0/10

美联储理事会就一项提案公开征求意见，该提案要求特定支付稳定币发行人建立并维护有效的客户识别程序（CIP）。 该提案表明美国对稳定币的监管将收紧，可能增加发行人的合规成本并重塑市场结构，同时旨在加强金融稳定和遏制非法融资。 该要求针对'支付稳定币发行人'，并强制实施类似于银行反洗钱规则的客户识别程序；评论期允许行业在最终规则通过前提供反馈。

rss · Federal Reserve Press Releases · Jun 18, 13:00

**背景**: 美联储理事会是美国中央银行的主要治理机构。支付稳定币是一种旨在用作支付手段的数字资产，锚定于美元等稳定价值。客户识别程序（CIP）是美国《爱国者法案》下的一项监管要求，要求金融机构核实客户身份，以防止洗钱和恐怖融资。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Reserve_Board_of_Governors">Federal Reserve Board of Governors</a></li>
<li><a href="https://www.federalreserve.gov/econres/notes/feds-notes/payment-stablecoins-and-cross-border-payments-benefits-and-implications-for-monetary-policy-20260330.html">The Fed - Payment Stablecoins and Cross Border Payments: Benefits and Implications for Monetary Policy Implementation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Customer_Identification_Program">Customer Identification Program</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#united-states`, `#stablecoin`, `#macro-risk`

---

<a id="item-9"></a>
## [联合国特使：利比亚政治进程势头恢复但行动窗口收窄](https://news.un.org/feed/view/en/story/2026/06/1167757) ⭐️ 6.0/10

联合国特使汉娜·特塔赫警告安理会，利比亚政治进程虽通过联利支助团推动的对话恢复势头，但采取具体行动的窗口正在缩小。为期六个月的结构化对话产生了近 600 项建议，但急需落实，以免再次陷入瘫痪。 利比亚是重要产油国和通往欧洲的移民枢纽，其政治稳定直接影响全球能源市场和地区安全。联合国主导路线图的成败可能影响石油产量、外国投资以及北非的地缘政治格局。 联利支助团的路线图涵盖选举、机构统一、安全、经济改革和民族和解。结构化对话邀请了约 120 名不同背景的利比亚人参与，产生了涵盖治理、安全、经济和人权等领域的近 600 项建议。

rss · UN News · Jun 18, 12:00

**背景**: 自 2011 年穆阿迈尔·卡扎菲政权垮台以来，利比亚一直深陷政治分裂，多个政府和武装组织争夺控制权。联合国利比亚支助团（联利支助团）多次尝试调解，推动选举和统一进程。前任特使阿卜杜拉耶·巴蒂利因进展陷入僵局于 2024 年辞职，汉娜·特塔赫于 2025 年接任。依赖石油的经济因封锁和冲突受到重创，同时该国仍是移民前往欧洲的主要出发点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/06/1167757">Libya’s political process regains momentum, but window for action is narrowing, UN envoy warns | UN News</a></li>
<li><a href="https://www.aa.com.tr/en/analysis/opinion-uns-libyan-envoy-resigns-what-does-it-mean-for-libyas-political-future/3231641">Anadolu Ajansı: OPINION - UN 's Libyan envoy resigns: What does it...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#middle-east`, `#sovereign-risk`

---

<a id="item-10"></a>
## [联合国儿童基金会：停火期间黎巴嫩每日有 12 名儿童死伤](https://news.un.org/feed/view/en/story/2026/06/1167736) ⭐️ 6.0/10

联合国儿童基金会报告指出，即使真主党与以色列达成停火协议已逾百日，黎巴嫩平均每日仍有 12 名儿童丧生或致残，凸显停火未能终止平民伤亡。 这一披露可能加大对以色列和真主党的外交压力，影响人道主义援助分配，并使停火的可持续性及未来和谈复杂化。 儿基会指出，伤亡包括未爆弹药、持续的以色列袭击及恶劣的流离失所条件造成的死伤，尽管有停火协议。

rss · UN News · Jun 17, 12:00

**背景**: 真主党是黎巴嫩什叶派伊斯兰组织，拥有强大准军事力量，自 2023 年 10 月起与以色列交战。2024 年 11 月曾达成停火，但 2026 年 3 月战火重燃。在美国调解下，双方于 2026 年 6 月 1 日再次停火。联合国儿童基金会的报告突显了黎巴嫩持续的人道主义危机，儿童尤其受害。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://en.wikipedia.org/wiki/2024_Israel–Lebanon_ceasefire_agreement">2024 Israel–Lebanon ceasefire agreement - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Israel–Lebanon_ceasefire">2026 Israel–Lebanon ceasefire - Wikipedia</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#military-risk`, `#diplomacy`, `#humanitarian`

---

<a id="item-11"></a>
## [欧洲央行行长拉加德暗示数字欧元与支付改革](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260615~35e6c6c4de.en.html) ⭐️ 6.0/10

欧洲央行行长拉加德题为“转型中的货币”的演讲预计将就数字欧元项目和正在进行的支付系统改革提供新见解，包括可能的时间表和监管更新。 这次演讲可能影响对数字欧元的预期，作为一种央行数字货币，它可能重塑欧洲支付格局、增强货币主权，并影响金融稳定和传统银行的作用。 拉加德可能讨论了数字欧元的法定货币地位、隐私保护、离线功能，以及欧洲央行近期批准的将 T2 支付系统运行时间延长至全天候的路线图。

rss · ECB Press Releases · Jun 15, 07:30

**背景**: 欧洲央行一直在探索数字欧元以补充现金，欧盟委员会于 2023 年提出了相关法律框架。另外，欧洲央行的 T2 实时全额结算系统正在升级为全天候运行，体现了对更高效、更具韧性的支付基础设施的推动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/euro/digital_euro/html/index.en.html">Digital euro - European Central Bank</a></li>
<li><a href="https://www.ecb.europa.eu/euro/digital_euro/faqs/html/ecb.faq_digital_euro.en.html">FAQs on the digital euro - European Central Bank</a></li>
<li><a href="https://chb44.com/2026/06/ecb-climate-rules-weekend-payments-eurozone/">ECB Expands Climate Rules and Weekend Payments : What It Means...</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#currency`, `#financial-stability`, `#europe`, `#macroeconomics`

---