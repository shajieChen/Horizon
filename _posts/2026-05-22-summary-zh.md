---
layout: default
title: "Horizon Summary: 2026-05-22 (ZH)"
date: 2026-05-22
lang: zh
---

> From 40 items, 9 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [联合国安理会就阿联酋核电站遇袭召开紧急会议](#item-2) ⭐️ 9.0/10
3. [霍尔木兹危机在美伊停火下持续扰乱贸易](#item-3) ⭐️ 8.0/10
4. [美联储公布 2026 年 4 月 FOMC 会议纪要](#item-4) ⭐️ 7.0/10
5. [安理会辩论加沙未来，和平进程停滞](#item-5) ⭐️ 6.0/10
6. [联合国大会通过决议支持国际法院气候咨询意见](#item-6) ⭐️ 6.0/10
7. [俄军袭击第聂伯罗，致平民死伤、毁联合国难民署物资](#item-7) ⭐️ 6.0/10
8. [古特雷斯谴责以色列将没收的 UNRWA 大院军事化](#item-8) ⭐️ 6.0/10
9. [古特雷斯呼吁重开霍尔木兹海峡并改革安理会](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 21, 23:05

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
| QDII Nasdaq 100 Proxy | US | bullish 38/31/31 | neutral 33/33/34 | bullish 42/29/30 | high |
| US Mega Cap Basket | US | neutral 33/33/34 | neutral 33/33/34 | bullish 42/29/30 | high |
| Japan Equity Basket | JP | bullish 38/31/31 | bullish 38/31/31 | bullish 42/29/30 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | bullish 36/31/32 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| ^NDX price trend | close=29357.27; 1d=+0.20%; 5d=-0.75%; 20d=+9.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=714.51; 1d=+0.19%; 5d=-0.73%; 20d=+9.69% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29539.25; 1d=+0.51%; 5d=-0.50%; 20d=+9.67% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=1.4%; implied_move=0.1%; put/call OI=2.1516350432373437 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.57; 2Y=4.08; 10Y-2Y=0.4900000000000002 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=58.3; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
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
- 1月：20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | high |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1月 | 42% | 29% | 30% | bullish | 20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| ^NDX price trend | close=29357.27; 1d=+0.20%; 5d=-0.75%; 20d=+9.61% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=714.51; 1d=+0.19%; 5d=-0.73%; 20d=+9.69% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29539.25; 1d=+0.51%; 5d=-0.50%; 20d=+9.67% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| MSFT price trend | close=419.09; 1d=-0.47%; 5d=+2.36%; 20d=+0.80% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=219.51; 1d=-1.77%; 5d=-6.88%; 20d=+9.95% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=607.38; 1d=+0.38%; 5d=-1.79%; 20d=-7.85% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=387.66; 1d=-0.32%; 5d=-3.34%; 20d=+14.39% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=417.85; 1d=+0.14%; 5d=-5.74%; 20d=+11.81% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=268.46; 1d=+1.30%; 5d=+0.46%; 20d=+5.25% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| NVDA options surface | ATM IV=34.9%; implied_move=2.0%; put/call OI=0.5428098693214841 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=33.8%; implied_move=2.0%; put/call OI=0.8139158429719928 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=23.8%; implied_move=1.4%; put/call OI=0.6474814540781557 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=24.6%; implied_move=1.4%; put/call OI=0.42257057546145493 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=24.4%; implied_move=1.4%; put/call OI=0.43885736999963865 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=22.7%; implied_move=1.3%; put/call OI=0.5334434606745042 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| NVDA insider filings | recent Form4 count=562 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| MSFT insider filings | recent Form4 count=731 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| CNN Fear & Greed | score=58.3; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| MSFT price trend | close=419.09; 1d=-0.47%; 5d=+2.36%; 20d=+0.80% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=219.51; 1d=-1.77%; 5d=-6.88%; 20d=+9.95% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=607.38; 1d=+0.38%; 5d=-1.79%; 20d=-7.85% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 8035.T price trend | close=48800.00; 1d=+5.86%; 5d=-4.69%; 20d=+10.88% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3554.00; 1d=-1.44%; 5d=+3.19%; 20d=+4.68% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=76960.00; 1d=+5.55%; 5d=-0.45%; 20d=+22.53% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2978.00; 1d=+1.22%; 5d=-1.00%; 20d=-10.92% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=91.37; 1d=+0.18%; 5d=-0.75%; 20d=+4.94% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6039.00; 1d=+19.85%; 5d=+4.66%; 20d=+33.40% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=58.3; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.57; 2Y=4.08; 10Y-2Y=0.4900000000000002 | 利率曲线决定权益估值贴现与风险偏好上限。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 跨层分歧信息有限，后续需补充更多波动与事件市场数据。

**Time stratification**
- 1日：1日篮子收益与5日均线结构偏强
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | medium |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | medium |
| 1月 | 42% | 29% | 30% | bullish | 20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 8035.T price trend | close=48800.00; 1d=+5.86%; 5d=-4.69%; 20d=+10.88% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3554.00; 1d=-1.44%; 5d=+3.19%; 20d=+4.68% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=76960.00; 1d=+5.55%; 5d=-0.45%; 20d=+22.53% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9988.HK price trend | close=126.00; 1d=-4.47%; 5d=-8.63%; 20d=-4.18% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=35.89; 1d=-0.97%; 5d=-3.63%; 20d=-1.64% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=123.50; 1d=-3.36%; 5d=-5.07%; 20d=+2.75% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=29.66; 1d=-1.59%; 5d=-6.49%; 20d=-6.73% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=23.83; 1d=-0.21%; 5d=-2.42%; 20d=+2.45% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=27.63; 1d=-1.74%; 5d=-5.38%; 20d=-2.81% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.57; 2Y=4.08; 10Y-2Y=0.4900000000000002 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=58.3; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 9988.HK price trend | close=126.00; 1d=-4.47%; 5d=-8.63%; 20d=-4.18% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=35.89; 1d=-0.97%; 5d=-3.63%; 20d=-1.64% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=123.50; 1d=-3.36%; 5d=-5.07%; 20d=+2.75% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

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

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days or more out. IV is a forward looking prediction of the likelihood...

- [Option Implied Volatility Rankings Report](https://marketchameleon.com/volReports/VolatilityRankings)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：What can I find on the Implied Volatility Rankings Report? Market Chameleon's Implied Volatility Rankings Report shows a detailed set of data for stocks, comparing their current...

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [CBOE Volatility Index: VIX (VIXCLS) / FRED / St. Louis Fed](https://fred.stlouisfed.org/series/VIXCLS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Graph and download economic data for CBOE Volatility Index: VIX (VIXCLS) from 1990-01-02 to 2026-05-19 about VIX, volatility, stock market, and USA.

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

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

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [iShares MSCI Japan ETF / EWJ](https://www.ishares.com/us/products/239665/ishares-msci-japan-etf)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：The iShares MSCI Japan ETF seeks to track an index composed of Japanese equities. The fund offers a way to express a single-country view and gain targeted exposure to companies...

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

- [Valuta EX - Currency Converter / Real-Time Exchange Rates](https://valuta.exchange/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

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
## [联合国安理会就阿联酋核电站遇袭召开紧急会议](https://news.un.org/feed/view/en/story/2026/05/1167550) ⭐️ 9.0/10

在阿联酋巴拉卡核电站附近发生无人机袭击后，联合国安理会召开紧急会议。国际原子能机构总干事拉斐尔·马里亚诺·格罗西向成员国通报了核安全与安保关切。 这一事件直接威胁动荡地区的核安全，可能加剧紧张局势，影响能源安全和全球市场。它凸显了冲突地区关键基础设施的脆弱性以及国际原子能机构在预防核灾难方面的作用。 无人机袭击发生在巴拉卡核电站附近，该核电站是阿拉伯世界首座投入运营的核电站。国际原子能机构的介入突显了风险的严重性，但袭击方细节仍不明确。

rss · UN News · May 19, 12:00

**背景**: 巴拉卡核电站位于阿联酋，是该国能源多元化战略的基石，也是阿拉伯世界首座核电站。它曾引发地区安全关切，包括 2019 年卡塔尔向 IAEA 提出的投诉。阿联酋坚称其符合最高核安全标准。IAEA 根据《核安全公约》推动全球核安保并应对事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://press.un.org/en/content/security-council">Security Council - UN Meetings Coverage and Press Releases</a></li>
<li><a href="https://en.wikipedia.org/wiki/Barakah_nuclear_power_plant">Barakah nuclear power plant - Wikipedia</a></li>
<li><a href="https://www.iaea.org/topics/nuclear-safety-and-security">Nuclear safety and security | IAEA</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`, `#energy`

---

<a id="item-3"></a>
## [霍尔木兹危机在美伊停火下持续扰乱贸易](https://news.un.org/feed/view/en/story/2026/05/1167548) ⭐️ 8.0/10

尽管 2026 年 4 月达成停火，霍尔木兹海峡仍实际受阻，伊朗征收通行费而美国实施反封锁，使全球供应链混乱和能源高成本持续。 该海峡承载全球 20%的液化天然气和 25%的海运石油；其长期受阻推高能源价格，加剧通胀，威胁全球经济稳定。 布伦特原油在 2026 年 3 月飙升至创纪录的月度峰值每桶 126 美元；超过 2000 艘船只和 2 万名海员被困，因双重封锁导致航运成本飙升。

rss · UN News · May 19, 12:00

**背景**: 霍尔木兹海峡是伊朗与阿曼之间的狭窄水道，为波斯湾唯一出海口。2026 年 2 月美以打击后，伊朗关闭海峡，造成自 1970 年代以来最严重的能源供应中断。2026 年 4 月 8 日有条件停火达成，但相互封锁和通行费要求使通行严重受限，伊朗控制过境而美国封锁伊朗港口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hormuz_crisis">Hormuz crisis</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#energy`, `#supply-chain`, `#middle-east`, `#military-risk`

---

<a id="item-4"></a>
## [美联储公布 2026 年 4 月 FOMC 会议纪要](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260520a.htm) ⭐️ 7.0/10

美联储公布了 2026 年 4 月 28 日至 29 日 FOMC 会议纪要，详细阐述了委员们对经济前景、通胀趋势和货币政策适当路径的看法。 会议纪要提供了美联储对经济状况评估及未来利率动向的关键洞察，影响市场对短期利率、国债收益率和美元的预期。 分析师将仔细审视纪要中关于通胀上行风险、劳动力市场紧张状况或潜在利率调整时机的任何讨论，特别是此次会议正值贸易政策不确定性加剧之际。

rss · Federal Reserve Press Releases · May 20, 18:00

**背景**: FOMC 是美联储的货币政策制定机构，通过设定联邦基金利率目标来实现充分就业和物价稳定的双重使命。会议纪要于每次会议三周后发布，通常揭示辩论深度，包括反对意见和经济预测。这些细节可能导致市场波动，因交易员会调整其对加息或降息的预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Open_Market_Committee">Federal Open Market Committee - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/FOMC_meeting_minutes">FOMC meeting minutes</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#united-states`, `#global-markets`, `#bonds`

---

<a id="item-5"></a>
## [安理会辩论加沙未来，和平进程停滞](https://news.un.org/feed/view/en/story/2026/05/1167563) ⭐️ 6.0/10

联合国安理会正就加沙的治理与恢复进行现场辩论，讨论脆弱的停火及哈马斯解除武装的僵局。 此次辩论表明外交僵局持续，但可能预示着国际压力的重新加大或政策转变，这将影响地区稳定与重建努力。 第 2803 号决议支持美国提出的和平计划与和平委员会，但因特使姆拉德诺夫坚持要求哈马斯解除武装而哈马斯拒绝，进展停滞。

rss · UN News · May 21, 12:00

**背景**: 2026 年 2 月，联合国安理会通过第 2803 号决议，支持《结束加沙冲突全面计划》。决议设立了和平委员会以监督重建，并授权部署国际稳定部队。该计划要求成立加沙管理全国委员会作为过渡治理机构。然而，要求哈马斯解除武装的第二阶段停火陷入僵局，双方互相指责对方违反协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council_Resolution_2803">United Nations Security Council Resolution 2803 - Wikipedia</a></li>
<li><a href="https://press.un.org/en/2025/sc16225.doc.htm">Security Council Authorizes International Stabilization Force in Gaza, Adopting Resolution 2803 (2025) | UN Meetings Coverage and Press Releases</a></li>
<li><a href="https://www.pbs.org/newshour/world/board-of-peace-envoy-mladenov-says-ceasefire-hinges-on-hamas-disarmament">Board of Peace envoy Mladenov says ceasefire hinges on Hamas' disarmament | PBS News</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`, `#ceasefire`

---

<a id="item-6"></a>
## [联合国大会通过决议支持国际法院气候咨询意见](https://news.un.org/feed/view/en/story/2026/05/1167561) ⭐️ 6.0/10

联合国大会通过一项决议，支持国际法院关于气候危机的咨询意见，该意见确认了各国在国际法下的义务。 这一外交举措强化了全球对各国在法律框架下应对气候变化的期望，并可能通过为国家问责提供依据，影响未来的气候诉讼。 联合国大会决议不具有法律约束力，国际法院的咨询意见也非约束性，但该背书为国际气候义务的解释增添了政治分量。

rss · UN News · May 20, 12:00

**背景**: 联合国大会是联合国的主要审议机构，所有 193 个会员国拥有平等代表权。国际法院（亦称世界法院）是联合国的主要司法机构，对诉讼案件作出具有约束力的判决，并就法律问题发表不具约束力的咨询意见。2023 年，一些岛国请求国际法院就国家的气候义务发表咨询意见，相关程序于 2025 年结束。大会决议现在正式对该意见表示欢迎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_General_Assembly">UN General Assembly</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_Court">World Court</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advisory_opinion">Advisory opinion</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#climate`, `#un`

---

<a id="item-7"></a>
## [俄军袭击第聂伯罗，致平民死伤、毁联合国难民署物资](https://news.un.org/feed/view/en/story/2026/05/1167562) ⭐️ 6.0/10

周二晚，俄罗斯对乌克兰第聂伯罗发动导弹和无人机袭击，造成平民死亡并摧毁了联合国难民署的人道主义援助物资，引发该机构驻乌克兰代表的强烈谴责。 此次袭击凸显了乌克兰人道主义行动面临的持续风险，可能干扰关键援助物资的运送，并加大国际社会对俄罗斯袭击民用设施的外交压力。 袭击发生在第聂伯罗，该城在战争中屡次受袭；被毁的联合国难民署物资原定用于帮助流离失所者，平民伤亡进一步增加了战争不断上升的死亡人数。

rss · UN News · May 20, 12:00

**背景**: 联合国难民署（UNHCR）为因俄乌战争而流离失所的数百万人提供保护和援助。这场战争始于 2014 年，并在 2022 年俄罗斯全面入侵后升级。第聂伯罗是乌克兰中东部的重镇，常成为俄罗斯导弹和无人机袭击的目标，远离前线的平民区屡屡被击中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNHCR">UNHCR</a></li>
<li><a href="https://en.wikipedia.org/wiki/Russia-Ukraine_war">Russia-Ukraine war</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#military-risk`, `#diplomacy`

---

<a id="item-8"></a>
## [古特雷斯谴责以色列将没收的 UNRWA 大院军事化](https://news.un.org/feed/view/en/story/2026/05/1167560) ⭐️ 6.0/10

联合国秘书长安东尼奥·古特雷斯强烈谴责以色列决定在被占领的东耶路撒冷一处没收的联合国近东巴勒斯坦难民救济和工程处（UNRWA）大院内设立军事设施，称此举“完全不可接受”。 这一谴责加剧了联合国与以色列之间的外交紧张，可能影响 UNRWA 对巴勒斯坦难民的关键人道主义行动，并推动联合国安理会就以色列在被占东耶路撒冷的行动展开进一步讨论。 被没收的大院是 UNRWA 的耶路撒冷总部；以色列于 2026 年 1 月没收了该地，声称根据以色列和国际法它不享有豁免权，而 UNRWA 认为没收非法。

rss · UN News · May 20, 12:00

**背景**: UNRWA（联合国近东巴勒斯坦难民救济和工程处）自 1949 年起为巴勒斯坦难民提供教育、医疗和救济服务。东耶路撒冷自 1967 年起被以色列占领，并于 1980 年被吞并，此举未获大多数国家承认。该大院原本是 UNRWA 的总部，直至以色列于 2026 年 1 月将其没收，背景是关于 UNRWA 角色及与哈马斯关联指控的紧张局势。这一最新行动标志着以色列政府拆除 UNRWA 在耶路撒冷存在的努力进一步升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unrwa.org/what-mandate-unrwa-0">What is the mandate of UNRWA ? | UNRWA</a></li>
<li><a href="https://en.wikipedia.org/wiki/East_Jerusalem">East Jerusalem - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/01/20/world/middleeast/israel-unrwa-jerusalem.html">Israel Seizes UNRWA ’s Jerusalem Headquarters - The New York Times</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`

---

<a id="item-9"></a>
## [古特雷斯呼吁重开霍尔木兹海峡并改革安理会](https://news.un.org/feed/view/en/story/2026/05/1167555) ⭐️ 6.0/10

2026 年 5 月 27 日，联合国秘书长安东尼奥·古特雷斯呼吁立即重新开放霍尔木兹海峡，并扩大安理会成员规模，以遏制“拥有否决权超级大国的有罪不罚”现象。 霍尔木兹海峡是全球能源运输的关键咽喉，其关闭可能导致严重供应中断和价格飙升；安理会改革呼声则凸显在 2026 年伊朗战争等僵局下，改革二战后治理体系的压力日益增大。 古特雷斯未提出具体计划或时间表。霍尔木兹海峡危机源于 2026 年伊朗战争，而安理会改革面临五个拥有否决权的常任理事国必须同意的障碍。

rss · UN News · May 20, 12:00

**背景**: 霍尔木兹海峡位于伊朗与阿曼之间，是波斯湾唯一的出海口，承担全球约两成液化天然气和两成五海运石油运输，在 2026 年伊朗战争中成为冲突焦点并遭关闭。联合国安理会改革已争论数十年，上一次结构性调整在 1965 年；五个常任理事国（中国、法国、俄罗斯、英国、美国）拥有的否决权被批评阻碍了对卢旺达种族灭绝和乌克兰战争等危机的应对。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council_reform">UN Security Council reform</a></li>
<li><a href="https://en.wikipedia.org/wiki/Security_Council_veto_power">Security Council veto power</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#energy`, `#supply-chain`, `#diplomacy`, `#middle-east`

---