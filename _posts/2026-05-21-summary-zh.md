---
layout: default
title: "Horizon Summary: 2026-05-21 (ZH)"
date: 2026-05-21
lang: zh
---

> From 40 items, 13 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [安理会就阿联酋核电站遭无人机袭击召开紧急会议](#item-2) ⭐️ 9.0/10
3. [美联储会议纪要揭示政策辩论，利率预期转变](#item-3) ⭐️ 9.0/10
4. [联合国大会支持国际法院气候裁决](#item-4) ⭐️ 8.0/10
5. [霍尔木兹危机持续扰乱全球贸易与民生](#item-5) ⭐️ 8.0/10
6. [美联储任命鲍威尔为临时主席，待沃什宣誓就职](#item-6) ⭐️ 8.0/10
7. [俄罗斯空袭第聂伯罗摧毁联合国援助，难民署谴责](#item-7) ⭐️ 7.0/10
8. [古特雷斯谴责以色列将强占的 UNRWA 院落军事化](#item-8) ⭐️ 7.0/10
9. [古特雷斯呼吁重新开放霍尔木兹海峡并改革安理会](#item-9) ⭐️ 7.0/10
10. [联合国警告：乌克兰战争“日益致命”](#item-10) ⭐️ 6.0/10
11. [联合国报告称尽管停火，巴勒斯坦杀戮与强迫流离失所仍在持续](#item-11) ⭐️ 6.0/10
12. [世卫组织宣布刚果（金）埃博拉疫情为全球卫生紧急事件](#item-12) ⭐️ 6.0/10
13. [联合国警告核恐怖主义风险达历史最高](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 20, 23:15

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
| Japan Equity Basket | JP | neutral 33/33/34 | neutral 33/33/34 | bullish 36/31/32 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | bullish 36/31/32 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=29199.50; 1d=+0.95%; 5d=-0.95%; 20d=+7.81% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=713.15; 1d=+1.66%; 5d=-0.22%; 20d=+8.86% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29297.70; 1d=+1.66%; 5d=-0.24%; 20d=+8.76% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=15.4%; implied_move=0.6%; put/call OI=1.6124707971620444 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=60.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.57; 2Y=4.04; 10Y-2Y=0.5300000000000002 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| NQ=F price trend | close=29199.50; 1d=+0.95%; 5d=-0.95%; 20d=+7.81% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=713.15; 1d=+1.66%; 5d=-0.22%; 20d=+8.86% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29297.70; 1d=+1.66%; 5d=-0.24%; 20d=+8.76% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| TSLA price trend | close=417.26; 1d=+3.25%; 5d=-6.29%; 20d=+7.68% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=421.06; 1d=+0.87%; 5d=+3.91%; 20d=-2.74% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=302.25; 1d=+1.10%; 5d=+1.13%; 20d=+10.75% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=388.91; 1d=+0.32%; 5d=-3.41%; 20d=+14.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=265.01; 1d=+2.19%; 5d=-1.90%; 20d=+3.78% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=605.06; 1d=+0.41%; 5d=-1.88%; 20d=-10.32% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| TSLA options surface | ATM IV=7.4%; implied_move=0.3%; put/call OI=0.5639790127422636 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=7.9%; implied_move=0.3%; put/call OI=0.5522274400304608 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=5.1%; implied_move=0.2%; put/call OI=0.5625467159859708 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=81.6%; implied_move=5.9%; put/call OI=0.5684172836957783 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=7.4%; implied_move=0.3%; put/call OI=0.30973471821771403 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=3.7%; implied_move=0.1%; put/call OI=0.35650169820475497 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| NVDA insider filings | recent Form4 count=562 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.57; 2Y=4.04; 10Y-2Y=0.5300000000000002 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=60.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| AAPL insider filings | recent Form4 count=586 | 内部人交易节奏可作为估值温度辅助校验信号。 |

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
| TSLA price trend | close=417.26; 1d=+3.25%; 5d=-6.29%; 20d=+7.68% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=421.06; 1d=+0.87%; 5d=+3.91%; 20d=-2.74% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=302.25; 1d=+1.10%; 5d=+1.13%; 20d=+10.75% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 6861.T price trend | close=72910.00; 1d=-2.79%; 5d=-8.22%; 20d=+15.68% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2942.00; 1d=-0.51%; 5d=+0.09%; 20d=-13.27% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=46100.00; 1d=-2.25%; 5d=-10.21%; 20d=+0.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=91.21; 1d=+1.02%; 5d=-2.02%; 20d=+3.93% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=5039.00; 1d=-6.01%; 5d=-16.18%; 20d=+7.86% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3606.00; 1d=-3.06%; 5d=-1.48%; 20d=+5.84% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=60.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.57; 2Y=4.04; 10Y-2Y=0.5300000000000002 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| 6861.T price trend | close=72910.00; 1d=-2.79%; 5d=-8.22%; 20d=+15.68% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2942.00; 1d=-0.51%; 5d=+0.09%; 20d=-13.27% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=46100.00; 1d=-2.25%; 5d=-10.21%; 20d=+0.61% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 0700.HK price trend | close=455.20; 1d=-1.04%; 5d=-0.45%; 20d=-11.27% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=127.80; 1d=+1.51%; 5d=-0.31%; 20d=+3.90% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=23.88; 1d=+0.97%; 5d=-2.73%; 20d=+1.62% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=36.24; 1d=-0.11%; 5d=-5.28%; 20d=-1.97% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=30.14; 1d=-1.63%; 5d=-5.22%; 20d=-6.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=82.85; 1d=-0.24%; 5d=-5.42%; 20d=-4.16% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.57; 2Y=4.04; 10Y-2Y=0.5300000000000002 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=60.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| 0700.HK price trend | close=455.20; 1d=-1.04%; 5d=-0.45%; 20d=-11.27% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=127.80; 1d=+1.51%; 5d=-0.31%; 20d=+3.90% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=23.88; 1d=+0.97%; 5d=-2.73%; 20d=+1.62% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [Cboe Global Indices: CNIV01 Index Dashboard](https://www.cboe.com/us/indices/dashboard/cniv01/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Cboe Nasdaq-100 Implied Volatility Index Series is designed to measure the market's expectation of volatility implied by Nasdaq-100 Index puts and calls (NDX options) over a...

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days or more out. IV is a forward looking prediction of the likelihood...

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [CBOE Volatility Index (^VIX) - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
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

- [US High Yield Master II Option-Adjusted Spread (Market Dail…](https://ycharts.com/indicators/us_high_yield_master_ii_optionadjusted_spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：View market daily updates and historical trends for US High Yield Master II Option-Adjusted Spread. from United States. Source: Bank of America Merrill Ly…

- [U.S. High Yield Bond Spread (1996-2026) - Macrotrends](https://www.macrotrends.net/3229/us-high-yield-bond-spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：U.S. High Yield Bond Spread: 3.08% as of May 15, 2026. Units: Percent Frequency: Daily, Close Release: ICE BofA Indices Source: Ice Data Indices, LLC

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [USD to JPY - US Dollar to Japanese Yen Conversion - Exchange Rates](https://www.exchange-rates.org/converter/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Use the USD to JPY currency converter at Exchange-Rates.org for accurate and up-to-date exchange rates. Easily convert US Dollars to Japanese Yen with real-time data.

- [Valuta EX - Currency Converter / Real-Time Exchange Rates](https://valuta.exchange/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

- [1 USD to JPY - US Dollars to Japanese Yen Exchange Rate - Xe](https://www.xe.com/en/currencyconverter/convert/?Amount=1&From=USD&To=JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest 1 US Dollar to Japanese Yen rate for FREE with the original Universal Currency Converter. Set rate alerts for USD to JPY and learn more about US Dollars and Japan...

- [EWJ ETF Stock Price & Overview](https://stockanalysis.com/etf/ewj/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Get a real-time stock price for the EWJ ETF (iShares MSCI Japan ETF) with an overview of various metrics and statistics.

- [EWJ / iShares MSCI Japan ETF Overview / MarketWatch](https://www.marketwatch.com/investing/fund/ewj)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ / A complete iShares MSCI Japan ETF exchange traded fund overview by MarketWatch. View the latest ETF prices and news for better ETF investing.

- [iShares MSCI Japan ETF, EWJ:PCQ:USD summary - FT.com](https://markets.ft.com/data/etfs/tearsheet/summary?s=EWJ:PCQ:USD)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Latest iShares MSCI Japan ETF (EWJ:PCQ:USD) share price with interactive charts, historical prices, comparative analysis, forecasts, business profile and more.

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
## [安理会就阿联酋核电站遭无人机袭击召开紧急会议](https://news.un.org/feed/view/en/story/2026/05/1167550) ⭐️ 9.0/10

联合国安理会召开紧急会议，讨论阿联酋巴拉卡核电站附近遭无人机袭击事件。国际原子能机构总干事格罗西就核安全关切向成员国进行了通报，阿联酋则将此次袭击称为‘红线’。 此事件加剧了地区紧张局势，并可能因阿联酋作为主要石油生产国的地位及该核电站的战略重要性而危及能源市场稳定。同时，它突显了在冲突中保护核设施这一日益严峻的挑战。 无人机击中了核电站内层安全边界外的一台发电机，引发火灾但未造成人员伤亡或辐射泄漏。袭击发生在美国与伊朗停火协议脆弱的背景下，阿联酋已对袭击来源展开调查。

rss · UN News · May 19, 12:00

**背景**: 巴拉卡核电站是阿联酋首座核电站，于 2020 年投运，拥有四座反应堆，象征着和平利用核能的雄心。国际原子能机构负责监督全球核安全，尤其在战区。中东地区过去发生过与伊朗有关联组织的无人机袭击，而当前脆弱的美伊停火协议加剧了紧张。袭击核电站会带来放射性泄漏和军事升级的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167550">Security Council LIVE: Concerns grow over nuclear safety after UAE ...</a></li>
<li><a href="https://www.aljazeera.com/news/2026/5/17/drone-strike-sparks-fire-at-uaes-barakah-nuclear-power-plant">Drone strike sparks fire on perimeter of UAE’s Barakah nuclear power plant | Nuclear Energy News | Al Jazeera</a></li>
<li><a href="https://www.arabnews.com/node/2644228/middle-east">UAE says attack on Barakah nuclear plant a 'red line' as UN Security ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#nuclear-safety`, `#middle-east`

---

<a id="item-3"></a>
## [美联储会议纪要揭示政策辩论，利率预期转变](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260520a.htm) ⭐️ 9.0/10

美联储发布了 2026 年 4 月 28-29 日联邦公开市场委员会会议纪要，披露了关于经济状况和政策前景的内部讨论，这些讨论可能改变市场对未来利率变动和资产购买的预期。 会议纪要提供了有关美联储政策辩论的重要洞察，直接影响国债收益率、美元和股票估值，因为投资者将重新评估利率调整的时机和步伐。 纪要可能包含委员会对通胀持续性、劳动力市场强劲程度以及可能缩减资产负债表缩减的具体看法，这些对于近期政策指引至关重要。

rss · Federal Reserve Press Releases · May 20, 18:00

**背景**: 联邦公开市场委员会是美联储的货币政策制定机构，负责设定联邦基金利率目标并指导公开市场操作。其会议纪要在政策决定后三周发布，详细记录了经济评估和政策讨论，通常比最初的声明更能影响市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Open_Market_Committee">Federal Open Market Committee</a></li>
<li><a href="https://www.federalreserve.gov/monetarypolicy/fomc.htm">The Fed - Federal Open Market Committee</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#bonds`, `#currency`, `#united-states`

---

<a id="item-4"></a>
## [联合国大会支持国际法院气候裁决](https://news.un.org/feed/view/en/story/2026/05/1167561) ⭐️ 8.0/10

2026 年 5 月 13 日，联合国大会通过一项决议，正式支持国际法院关于各国有法律义务防止对气候造成重大损害的咨询意见。 这项决议加强了气候正义的多边共识，可能加速针对政府和企业的气候诉讼，影响未来的能源监管和碳市场，并提高高排放国家的主权风险。 国际法院咨询意见于 2025 年 7 月一致通过；联大决议虽无法律约束力，但具有重要的政治分量，并显示出联合国会员国的广泛支持。

rss · UN News · May 20, 12:00

**背景**: 国际法院是联合国的主要司法机关。应联合国大会请求，它就各国在气候变化问题上的义务发表了咨询意见。咨询意见不具法律约束力，但具有道德和法律权威。联大的支持增强了该意见对国家法院和国际气候谈判的影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/world/2026/may/14/un-members-prepare-for-pivotal-vote-on-landmark-icj-climate-justice-ruling">UN members prepare for pivotal vote on landmark ICJ climate justice ...</a></li>
<li><a href="https://www.iisd.org/articles/deep-dive/icj-advisory-opinion-climate-change">Historic International Court of Justice Opinion Confirms States’ Climate Obligations | International Institute for Sustainable Development</a></li>
<li><a href="https://www.icj-cij.org/case/187">icj -cij.org/case/187</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#energy`, `#sovereign-risk`, `#global-markets`

---

<a id="item-5"></a>
## [霍尔木兹危机持续扰乱全球贸易与民生](https://news.un.org/feed/view/en/story/2026/05/1167548) ⭐️ 8.0/10

尽管美伊于 2026 年 4 月达成脆弱的停火协议，霍尔木兹海峡周边持续的不稳定局势仍在扰乱海运、推高能源价格，并加剧全球生活成本危机，影响就业与家庭开支。 霍尔木兹海峡是全球约五分之一石油贸易和三分之一化肥出口的咽喉要道；持续的扰乱因此延长通胀压力，威胁粮食安全，并可能迫使各国央行维持紧缩货币政策，对全球市场产生连锁反应。 停火为自 2026 年 4 月 7 日起为期两周的有条件暂停，不包括黎巴嫩，且航运事件偶有发生；海峡最窄处仅 21 海里，极易受到干扰。

rss · UN News · May 19, 12:00

**背景**: 霍尔木兹海峡连接波斯湾与阿曼湾，是全球最具战略意义的水道之一，承担着约 20%的全球石油和 30%的海运化肥贸易。2026 年初，以美国为首的军事行动（“十二日战争”）对伊朗发动打击，导致地区紧张局势急剧升级，引发导弹袭击和海上封锁。4 月，在巴基斯坦斡旋下达成了脆弱的停火协议，但安全形势依然脆弱，进一步冲突的威胁令航运和能源市场持续紧张。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz - Wikipedia</a></li>
<li><a href="https://www.bbc.com/news/articles/c78n6p09pzno">Iran war: What is the Strait of Hormuz and why does it matter?</a></li>
<li><a href="https://www.cnn.com/2026/04/07/world/live-news/iran-war-trump-us-israel">Day 39 of Middle East conflict — US , Israel, Iran agree to ceasefire ...</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#energy`, `#supply-chain`, `#middle-east`, `#global-markets`

---

<a id="item-6"></a>
## [美联储任命鲍威尔为临时主席，待沃什宣誓就职](https://www.federalreserve.gov/newsevents/pressreleases/other20260515a.htm) ⭐️ 8.0/10

美联储理事会任命杰罗姆·鲍威尔为临时主席，他将担任此职务，直到新任主席凯文·沃什宣誓就职为止。 此次交接预示着货币政策可能转向：沃什强调美联储独立性、警惕财政主导，并可能倾向于更陡峭的收益率曲线，这将影响利率预期和金融市场稳定性。 鲍威尔仍为美联储理事；临时主席是过渡性安排，沃什宣誓日期尚未公布，市场将密切关注其未来的政策指导。

rss · Federal Reserve Press Releases · May 15, 21:00

**背景**: 美联储章程规定，当主席和副主席均缺席时，由理事会选举一名成员担任临时主席。鲍威尔于 2018 年就任主席，其主席任期于 2026 年 5 月届满。凯文·沃什曾于 2006 年至 2011 年担任美联储理事，若就任将成为自保罗·沃尔克以来最年轻的美联储主席。他曾批评大规模资产购买，主张强化治理以维护央行独立性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chair_of_the_Federal_Reserve">Chair of the Federal Reserve - Wikipedia</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2kwdHUtT0VSR0VIbnQyYTZsVzNpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en">Jerome Powell named Federal Reserve chair pro tempore - Overview</a></li>
<li><a href="https://www.investing.com/news/economy-news/who-is-kevin-warsh-and-what-does-his-policy-entail-4637398">Who is Kevin Warsh and what does his policy entail? By Investing.com</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#global-markets`, `#bonds`, `#currencies`

---

<a id="item-7"></a>
## [俄罗斯空袭第聂伯罗摧毁联合国援助，难民署谴责](https://news.un.org/feed/view/en/story/2026/05/1167562) ⭐️ 7.0/10

周二夜间，俄罗斯对第聂伯罗发动导弹和无人机袭击，造成平民死亡并摧毁了联合国难民署的人道主义援助物资，该机构驻乌克兰代表予以强烈谴责。 直接袭击联合国援助物资加剧了乌克兰的人道危机，可能破坏国际人道主义努力，或引发更强外交反应并影响西方的军事和财政支持。 袭击发生在乌克兰中东部的主要工业城市第聂伯罗，该城多次遭到打击；联合国难民署的谴责凸显了袭击人道主义资产的严重性，这违反了国际人道法。

rss · UN News · May 20, 12:00

**背景**: 联合国难民署是负责保护难民和流离失所者的联合国机构，自冲突开始以来一直在乌克兰开展工作。俄乌战争始于 2014 年俄罗斯吞并克里米亚，2022 年 2 月升级为全面入侵。第聂伯罗是乌克兰中东部战略城市，多次遭到俄军导弹袭击，造成平民伤亡。袭击人道主义援助物资违反国际人道法，已受到联合国谴责。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNHCR">UNHCR</a></li>
<li><a href="https://en.wikipedia.org/wiki/Russia-Ukraine_war">Russia-Ukraine war</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#military-risk`, `#geopolitics`

---

<a id="item-8"></a>
## [古特雷斯谴责以色列将强占的 UNRWA 院落军事化](https://news.un.org/feed/view/en/story/2026/05/1167560) ⭐️ 7.0/10

联合国秘书长安东尼奥·古特雷斯强烈谴责以色列决定在被占领的东耶路撒冷一个被强占的 UNRWA 院落内设立军事设施，称此举“完全不可接受”。 这一谴责加剧了以色列与联合国之间的外交摩擦，威胁到 UNRWA 对巴勒斯坦难民的人道主义援助行动的持续性，并可能在持续冲突中加剧地区紧张局势。 该院落此前已被以色列强占；以色列此前已禁止 UNRWA 活动并认定其为恐怖组织，但国际法院在 2025 年 10 月裁定，以色列未能证实该机构内有大量哈马斯成员的指控。

rss · UN News · May 20, 12:00

**背景**: UNRWA 是联合国于 1949 年成立的机构，旨在为巴勒斯坦难民提供救济和发展援助。东耶路撒冷自 1967 年起被以色列占领，其吞并未获国际承认。2025 年初，以色列以涉嫌与恐怖主义有关联为由禁止 UNRWA 在其境内活动，但国际法院随后驳回了相关指控。在这一敏感地区强占并将 UNRWA 院落军事化，标志着事态的重大升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNRWA">UNRWA</a></li>
<li><a href="https://en.wikipedia.org/wiki/East_Jerusalem">East Jerusalem - Wikipedia</a></li>
<li><a href="https://www.crisisgroup.org/rpt/middle-east-north-africa/israelpalestine/202-reversing-israels-deepening-annexation-occupied-east-jerusalem">Reversing Israel’s Deepening Annexation of Occupied East Jerusalem</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-9"></a>
## [古特雷斯呼吁重新开放霍尔木兹海峡并改革安理会](https://news.un.org/feed/view/en/story/2026/05/1167555) ⭐️ 7.0/10

联合国秘书长安东尼奥·古特雷斯呼吁有效重新开放霍尔木兹海峡，并扩大联合国安理会成员数量，以遏制行使否决权的“超级大国”免受惩罚的现象。 霍尔木兹海峡是全球石油和液化天然气运输的关键咽喉要道，长期关闭将引发严重的能源供应中断和价格飙升。安理会改革则旨在解决阻碍国际和平与安全应对的根本性治理僵局。 全球约 25%的海运石油和 20%的液化天然气每年经过该海峡。任何安理会改革都需获得五个拥有否决权的常任理事国的一致同意，这使得改革极难实现。

rss · UN News · May 20, 12:00

**背景**: 霍尔木兹海峡是伊朗与阿曼之间的狭窄水道，是波斯湾唯一的出海口，也是能源出口的重要通道。在 2026 年伊朗战争期间，该海峡关闭导致全球运输中断，成为危机焦点。联合国安理会改革自 1945 年以来一直争议不断，五个常任理事国（中国、法国、俄罗斯、英国和美国）拥有否决权，常被批评阻碍对冲突采取行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council_reform">UN Security Council reform</a></li>
<li><a href="https://www.bbc.com/news/articles/c78n6p09pzno">Iran war: What is the Strait of Hormuz and why does it matter?</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#energy`, `#supply-chain`, `#middle-east`, `#diplomacy`

---

<a id="item-10"></a>
## [联合国警告：乌克兰战争“日益致命”](https://news.un.org/feed/view/en/story/2026/05/1167546) ⭐️ 6.0/10

周二，一名联合国高级官员向安理会通报称，已进入第五年的乌克兰战争“正日益致命”，表明安全局势不断恶化。 这一警告凸显了冲突的持续动荡，它继续威胁地区稳定并使外交努力复杂化，而安理会因俄罗斯的否决权仍基本处于瘫痪状态。 此次通报未提出新措施，但严酷地提醒人们平民伤亡和基础设施破坏正在加剧，且看不到停火或政治解决的迹象。

rss · UN News · May 19, 12:00

**背景**: 联合国安理会负责维护国际和平，有五个常任理事国——俄罗斯、中国、美国、英国和法国——每个国家都拥有否决权。自 2014 年吞并克里米亚和 2022 年全面入侵以来，俄罗斯多次阻挠有关乌克兰的决议。战争已造成数千人死亡和严重的难民危机，而安理会的瘫痪限制了有效的国际应对。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council">United Nations Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/Russia-Ukraine_war">Russia-Ukraine war</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#russia-ukraine`, `#united-nations`

---

<a id="item-11"></a>
## [联合国报告称尽管停火，巴勒斯坦杀戮与强迫流离失所仍在持续](https://news.un.org/feed/view/en/story/2026/05/1167538) ⭐️ 6.0/10

联合国人权高专办一名高级官员周一在日内瓦表示，以色列与哈马斯的停火减少了加沙的暴力，但杀戮和破坏仍在继续，同时被占领的西岸的强迫流离失所达到了数十年来未见的程度。 持续的暴力和流离失所表明停火的脆弱性和人道主义危机的长期性，这可能破坏地区稳定，影响外交努力和国际关系。 联合国人权高专办强调，西岸的强迫流离失所‘数十年来未见’，包括以军空袭和推土机在内的强制性条件，但未提供具体的伤亡数字或对比数据。

rss · UN News · May 18, 12:00

**背景**: 联合国人权高专办是联合国人权机构，由高级专员福尔克尔·蒂尔克领导。以色列与哈马斯的冲突达成了包括释放人质和以色列撤军等阶段的停火协议。西岸的强迫流离失所是与以色列定居点和军事行动相关的长期问题，常被巴勒斯坦人称为‘第三次浩劫’。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OHCHR">OHCHR</a></li>
<li><a href="https://daleel-madani.org/civil-society-directory/united-nations-relief-and-works-agency-palestine-refugees/press-releases/large-scale-forced-displacement-west-bank-impacts-nearly-77000-people">Large-scale forced displacement in the West Bank ... | Daleel Madani</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#geopolitics`, `#diplomacy`, `#military-risk`

---

<a id="item-12"></a>
## [世卫组织宣布刚果（金）埃博拉疫情为全球卫生紧急事件](https://news.un.org/feed/view/en/story/2026/05/1167534) ⭐️ 6.0/10

世界卫生组织将刚果民主共和国东部的埃博拉疫情宣布为国际关注的突发公共卫生事件，专家警告全球大流行风险正在增加。 该疫情威胁到关键矿产供应链，尤其是钴，因为该地区占全球供应的主要份额，并可能加剧刚果（金）东部的人道主义和安全危机，增加主权风险并引发国际反应。 世卫组织并未宣布为大流行紧急情况，并建议不要关闭边境，但警告疫情规模可能远大于已发现的情况；刚果（金）生产全球 70%的钴，其中 90%在中国精炼。

rss · UN News · May 18, 12:00

**背景**: 世卫组织的‘国际关注的突发公共卫生事件’（PHEIC）是协调全球应对严重健康威胁的机制。刚果（金）东部数十年来饱受冲突之苦，包括基伍冲突，导致大规模流离失所和饥饿，削弱了卫生系统并助长了疾病传播。该地区对全球钴供应至关重要，生产全球约 70%的钴，这是电池和电子产品关键矿物，大部分出口至中国精炼。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/05/17/world/africa/ebola-congo-uganda-who-public-health-emergency.html">W.H.O. Declares Ebola Outbreak a Global Health Emergency</a></li>
<li><a href="https://medicalxpress.com/news/2026-05-ebola-outbreak-declared-global-health.html">What to know about the Ebola outbreak that the WHO has declared ...</a></li>
<li><a href="https://www.bbc.com/news/articles/cj6wwx7zxd9o">What are critical minerals , what are they used for and why do...</a></li>

</ul>
</details>

**标签**: `#health-emergency`, `#supply-chain`, `#africa`, `#sovereign-risk`

---

<a id="item-13"></a>
## [联合国警告核恐怖主义风险达历史最高](https://news.un.org/feed/view/en/story/2026/05/1167501) ⭐️ 6.0/10

联合国发出严厉警告，指出由于军事化无人机和人工智能的广泛可及性，核恐怖主义威胁目前已达到历史最高水平；恐怖组织正越来越多地利用这些技术招募专家，并可能部署脏弹。 这一事态发展引发了严重的全球安全担忧，因为人工智能与无人机技术的融合可能降低核攻击或放射性攻击的门槛，破坏威慑稳定，并迫使采取紧急的多边政策与防扩散应对措施。 一位联合国专家特别指出，恐怖组织已招募了人工智能专家，无人机可被用于发射脏弹；该警告于 2026 年 5 月发出，并着重提到了近期针对核设施的无人机袭击等实例。

rss · UN News · May 17, 12:00

**背景**: 自“9·11”事件以来，核恐怖主义风险持续存在，但无人机和人工智能的进步增添了新维度。无人机成本低、难以探测且可被武器化，而人工智能可协助规避安保或优化攻击计划。国际原子能机构等组织长期呼吁加强对核材料的保护，近期针对阿联酋巴拉卡核电站等场所的无人机事件凸显了这些脆弱性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167501">Nuclear terror threat ‘has never been so high’ | UN News</a></li>
<li><a href="https://www.jpost.com/middle-east/article-896581">UN expert warns that nuclear terror risk has 'never been so high</a></li>
<li><a href="https://toda.org/global-outlook/2025/drone-technology-and-the-future-of-nuclear-weapons.html">Drone Technology and the Future of Nuclear Weapons | Toda Peace Institute</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#military-risk`, `#nuclear`, `#terrorism`

---