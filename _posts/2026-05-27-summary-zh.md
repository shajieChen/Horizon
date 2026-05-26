---
layout: default
title: "Horizon Summary: 2026-05-27 (ZH)"
date: 2026-05-27
lang: zh
---

> From 43 items, 15 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [俄罗斯大规模导弹无人机袭击基辅](#item-2) ⭐️ 9.0/10
3. [《不扩散核武器条约》审议大会未达成共识，引发军备竞赛担忧](#item-3) ⭐️ 9.0/10
4. [凯文·沃什宣誓就任美联储主席](#item-4) ⭐️ 9.0/10
5. [古特雷斯警告联合国创始原则面临严重压力](#item-5) ⭐️ 8.0/10
6. [ECB 首席经济学家莱恩日经访谈释放政策信号](#item-6) ⭐️ 8.0/10
7. [欧央行执委施纳贝尔路透采访谈利率前景](#item-7) ⭐️ 8.0/10
8. [美联储公布 2026 年 4 月 28-29 日 FOMC 会议纪要](#item-8) ⭐️ 8.0/10
9. [以军空袭黎巴嫩，加沙援助受限](#item-9) ⭐️ 7.0/10
10. [安理会就卢甘斯克宿舍遇袭指控召开紧急会议](#item-10) ⭐️ 7.0/10
11. [俄军空袭第聂伯罗致平民死亡、毁坏联合国援助物资](#item-11) ⭐️ 7.0/10
12. [加沙药物封锁与疾病蔓延致人道危机恶化](#item-12) ⭐️ 6.0/10
13. [联合国特使警告：加沙过渡计划若停滞或陷永久僵局](#item-13) ⭐️ 6.0/10
14. [古特雷斯谴责以军占用 UNRWA 驻地建军事设施](#item-14) ⭐️ 6.0/10
15. [菲利普·莱恩谈欧洲与世界经济](#item-15) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 26, 23:02

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
| QDII Nasdaq 100 Proxy | US | bullish 38/31/31 | bullish 38/31/31 | bullish 42/29/30 | high |
| US Mega Cap Basket | US | bullish 38/31/31 | bullish 38/31/31 | bullish 42/29/30 | high |
| Japan Equity Basket | JP | bullish 38/31/31 | bullish 38/31/31 | bullish 42/29/30 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | bullish 36/31/32 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=30041.00; 1d=+1.63%; 5d=+3.25%; 20d=+9.48% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=30001.32; 1d=+1.76%; 5d=+3.47%; 20d=+9.87% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=730.28; 1d=+1.78%; 5d=+3.46%; 20d=+9.94% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=1.7%; implied_move=0.1%; put/call OI=2.8367752947426723 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.5; 2Y=4.01; 10Y-2Y=0.4900000000000002 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=60.8; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
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
- 1月：20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | high |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | high |
| 1月 | 42% | 29% | 30% | bullish | 20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| NQ=F price trend | close=30041.00; 1d=+1.63%; 5d=+3.25%; 20d=+9.48% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=30001.32; 1d=+1.76%; 5d=+3.47%; 20d=+9.87% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=730.28; 1d=+1.78%; 5d=+3.46%; 20d=+9.94% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| AMZN price trend | close=265.29; 1d=-0.39%; 5d=+0.16%; 20d=+1.60% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=612.34; 1d=+0.34%; 5d=+0.18%; 20d=-9.77% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=308.33; 1d=-0.16%; 5d=+3.52%; 20d=+15.32% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=433.59; 1d=+1.78%; 5d=+5.76%; 20d=+14.50% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=214.86; 1d=-0.22%; 5d=-3.36%; 20d=-0.81% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=388.88; 1d=+1.54%; 5d=-2.03%; 20d=+11.00% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| MSFT options surface | ATM IV=7.8%; implied_move=0.3%; put/call OI=0.6362317926729302 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=5.4%; implied_move=0.3%; put/call OI=0.5455784805951552 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=3.1%; implied_move=0.1%; put/call OI=0.7140460526315789 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=2.8%; implied_move=0.1%; put/call OI=0.3865218602060707 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=7.9%; implied_move=0.3%; put/call OI=0.6225108421697964 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=8.0%; implied_move=0.3%; put/call OI=0.6561125769569042 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| AAPL insider filings | recent Form4 count=586 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.5; 2Y=4.01; 10Y-2Y=0.4900000000000002 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| NVDA insider filings | recent Form4 count=562 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| CNN Fear & Greed | score=60.8; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| MSFT insider filings | recent Form4 count=731 | 内部人交易节奏可作为估值温度辅助校验信号。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：1日篮子收益与5日均线结构偏强
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 38% | 31% | 31% | bullish | 1日篮子收益与5日均线结构偏强 | high |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | high |
| 1月 | 42% | 29% | 30% | bullish | 20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| AMZN price trend | close=265.29; 1d=-0.39%; 5d=+0.16%; 20d=+1.60% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=612.34; 1d=+0.34%; 5d=+0.18%; 20d=-9.77% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=308.33; 1d=-0.16%; 5d=+3.52%; 20d=+15.32% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 8035.T price trend | close=51420.00; 1d=-1.46%; 5d=+9.03%; 20d=+13.01% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.90; 1d=+1.41%; 5d=+2.18%; 20d=+5.95% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3548.00; 1d=-1.39%; 5d=-4.62%; 20d=+6.13% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=3022.00; 1d=-0.13%; 5d=+2.20%; 20d=-5.30% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7841.00; 1d=+10.91%; 5d=+46.26%; 20d=+39.52% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77120.00; 1d=-2.21%; 5d=+2.83%; 20d=+20.88% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=60.8; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.5; 2Y=4.01; 10Y-2Y=0.4900000000000002 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 8035.T price trend | close=51420.00; 1d=-1.46%; 5d=+9.03%; 20d=+13.01% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.90; 1d=+1.41%; 5d=+2.18%; 20d=+5.95% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3548.00; 1d=-1.39%; 5d=-4.62%; 20d=+6.13% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9618.HK price trend | close=118.60; 1d=-2.55%; 5d=-6.25%; 20d=+0.08% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=29.76; 1d=-0.80%; 5d=-2.94%; 20d=-4.62% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=27.26; 1d=+1.30%; 5d=-2.85%; 20d=-3.88% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=23.34; 1d=-0.64%; 5d=-2.63%; 20d=+0.04% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=78.80; 1d=-3.13%; 5d=-4.08%; 20d=-4.43% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=35.75; 1d=+0.65%; 5d=-1.13%; 20d=-1.92% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.5; 2Y=4.01; 10Y-2Y=0.4900000000000002 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=60.8; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 9618.HK price trend | close=118.60; 1d=-2.55%; 5d=-6.25%; 20d=+0.08% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=29.76; 1d=-0.80%; 5d=-2.94%; 20d=-4.62% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=27.26; 1d=+1.30%; 5d=-2.85%; 20d=-3.88% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [Cboe Global Indices: VIX Index Dashboard](https://www.cboe.com/us/indices/dashboard/vix/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：The VIX Index is often referred to as the market's "fear gauge". The VIX Index is the centerpiece of Cboe Global Markets' volatility franchise, which includes volatility indexes...

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days out or more. IV is a forward looking prediction of the likelihood...

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [Cboe Nasdaq-100 Implied Volatil (^CNIV05) - Yahoo Finance](https://finance.yahoo.com/quote/%5ECNIV05/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Find the latest information on Cboe Nasdaq-100 Implied Volatil (^CNIV05) including data, charts, related news and more from Yahoo Finance

- [MOVE Index (MOVE) - MacroMicro](https://en.macromicro.me/charts/35584/us-treasury-move-index)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：The Merrill Lynch Option Volatility Estimate (MOVE) Index reflects the level of volatility in U.S. Treasury futures. The index is considered a proxy for term premiums of U.S. Tr...

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

- [BofA US High Yield Index Option-Adjusted Spread - GuruFocus](https://www.gurufocus.com/economic_indicators/5735/bofa-us-high-yield-index-optionadjusted-spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：Basic Info BofA US High Yield Index Option-Adjusted Spread was 2.86 as of 2026-04-16, according to Federal Reserve Economic Data. Historically, BofA US High Yield Index Option-A...

- [QQQ Options Chain — Open Interest, Implied Volatility, Max Pain & Gamma ...](https://whalequant.io/en/stocks/QQQ/options-analytics)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Explore the live QQQ options chain with strikes, open interest, volume, implied volatility (IV), max pain levels, gamma exposure, dealer positioning and options flow analysis. P...

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Index Information - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index/profile?cid=2&idx=nk225vi)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：The Nikkei Stock Average Volatility Index are calculated by using prices of Nikkei 225 futures and Nikkei 225 options on the Osaka Exchange (OSE). In the calculation, taking nea...

- [USD/JPY Currency Exchange Rate & News - Google Finance](https://www.google.com/finance/beta/quote/USD-JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：USD/JPY Weekly Outlook: Waller Validates Hawkish Shift as 160 Looms Profile The United States dollar is the official currency of the United States and several other countries.

- [Convert US Dollar to Japanese Yen / USD/JPY Exchange Rate - Investing.com](https://www.investing.com/currencies/usd-jpy-converter)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Our real time US Dollar Japanese Yen converter will enable you to convert your amount from USD to JPY. All prices are in real time.

- [USD to JPY / Convert Live / Exchange Rates UK](https://www.exchangerates.org.uk/Dollars-to-Yen-currency-conversion-page.html)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：To convert Dollars to Yen or determine the Dollar Yen exchange rate simply use the currency converter on the right of this page, which offers fast live exchange rate conversions...

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

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
## [俄罗斯大规模导弹无人机袭击基辅](https://news.un.org/feed/view/en/story/2026/05/1167583) ⭐️ 9.0/10

一夜之间，俄罗斯对基辅发动大规模袭击，动用约 90 枚导弹（含高超音速弹道导弹）和 60 架无人机，联合国驻乌克兰高级官员呼吁停止伤害平民。 这次重大军事升级显著加剧了地缘政治风险，可能引发北约和欧盟的强烈反应、对俄新制裁以及能源市场动荡，同时推高全球避险情绪。 袭击动用了能够以 5 马赫以上速度机动的高超音速弹道导弹，使其更难被拦截。总计约有 150 件武器瞄准了首都。

rss · UN News · May 24, 12:00

**背景**: 高超音速弹道导弹飞行速度超过 5 马赫，且可在大气层内机动，令防御系统难以拦截。联合国长期肩负武装冲突中保护平民的使命，通常通过维和行动和官方谴责来执行。自 2022 年 2 月俄罗斯全面入侵以来，基辅频繁遭袭，但如此规模的攻击罕见，标志着危险的升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hypersonic_ballistic_missile">Hypersonic ballistic missile</a></li>
<li><a href="https://peacekeeping.un.org/en/protection-of-civilians-mandate">Protection of civilians mandate | UN Peacekeeping</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#military-risk`, `#diplomacy`, `#geopolitics`, `#energy`

---

<a id="item-3"></a>
## [《不扩散核武器条约》审议大会未达成共识，引发军备竞赛担忧](https://news.un.org/feed/view/en/story/2026/05/1167580) ⭐️ 9.0/10

经过四周的谈判，《不扩散核武器条约》第十一次审议大会于周五在纽约联合国总部结束，未能达成共识性的最终宣言。 此次失败削弱了全球防扩散架构，加深了有核国家与无核国家之间的不信任，并增加了新一轮核军备竞赛的风险，可能对国际安全与市场稳定产生溢出效应。 在联合国总部举行的四周会议因在核裁军时间表、防扩散合规性以及大国地缘政治紧张等问题上持续存在分歧，未能通过最终文件。

rss · UN News · May 23, 12:00

**背景**: 《不扩散核武器条约》于 1970 年生效，旨在防止核武器扩散、促进和平利用核能及推动核裁军。审议大会每五年举行一次；上一次达成协商一致最终宣言是在 2010 年，2015 年和 2022 年的大会也均以无共识告终，削弱了该条约的公信力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nuclear_Non-Proliferation_Treaty">Nuclear Non-Proliferation Treaty</a></li>
<li><a href="https://meetings.unoda.org/npt-revcon/treaty-on-the-non-proliferation-of-nuclear-weapons-eleventh-review-conference-2026">Treaty on the Non-Proliferation of Nuclear Weapons -EleventhReview Conference (2026) | United Nations</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#global-markets`

---

<a id="item-4"></a>
## [凯文·沃什宣誓就任美联储主席](https://www.federalreserve.gov/newsevents/pressreleases/other20260522a.htm) ⭐️ 9.0/10

凯文·沃什宣誓就任美联储理事会主席和成员，联邦公开市场委员会一致推选他为主席，标志着美国央行的领导层交接。 这一变动可能重塑美国的货币政策、利率决策和金融监管，从而影响全球市场、债券收益率和美元；联邦公开市场委员会的一致投票表明对新主席的机构支持。 沃什曾是美联储理事和经济顾问，具有金融市场和政府背景；他的政策观点将在接下来的演讲和联邦公开市场委员会会议记录中受到密切关注。

rss · Federal Reserve Press Releases · May 22, 20:15

**背景**: 美联储是美国的中央银行，成立于 1913 年，负责管理货币政策和确保金融稳定。理事会是其管理机构，主席是货币政策的核心代表。联邦公开市场委员会由理事和地区联储行长组成，负责设定利率和公开市场操作。联邦公开市场委员会主席通常由理事会主席兼任，其领导风格深刻影响经济预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Board_of_Governors_of_the_Federal_Reserve_System">Board of Governors of the Federal Reserve System</a></li>
<li><a href="https://www.federalreserve.gov/monetarypolicy/fomc.htm">The Fed - Federal Open Market Committee</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federal_Reserve_System">Federal Reserve System</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#united-states`, `#bonds`, `#currency`

---

<a id="item-5"></a>
## [古特雷斯警告联合国创始原则面临严重压力](https://news.un.org/feed/view/en/story/2026/05/1167585) ⭐️ 8.0/10

在联合国安理会关于强化多边体系的高级别辩论中，秘书长古特雷斯警告，《联合国宪章》正面临数十年来最严峻的考验，战争、军备竞赛、气候冲击和国际法侵蚀给旨在防止第三次世界大战的多边体系带来了巨大压力。 这一警告表明多边机制功能失调加剧，对全球治理和冲突解决产生长期影响。对市场而言，基于规则的国际秩序被削弱可能推高地缘政治风险和经济碎片化，影响贸易、投资和金融稳定。 辩论的重点包括捍卫《联合国宪章》、改革全球治理以及恢复对安理会应对危机能力的信心。安理会仍因大国使用否决权而陷入瘫痪，如俄罗斯就乌克兰问题、美国就加沙问题行使否决权。

rss · UN News · May 26, 12:00

**背景**: 《联合国宪章》于 1945 年签署，是建立联合国及其原则的基础性条约。安理会是联合国六大主要机构之一，肩负维护国际和平与安全的首要责任，五个常任理事国拥有否决权。多边主义这一多国合作方式正受到民族主义、民粹主义和大国竞争加剧的压力。由于在乌克兰和加沙等冲突上陷入僵局，安理会的效力受到质疑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Charter">UN Charter</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multilateralism">Multilateralism</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#multilateralism`, `#global-markets`, `#sovereign-risk`

---

<a id="item-6"></a>
## [ECB 首席经济学家莱恩日经访谈释放政策信号](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260526_1~71caa51b14.en.html) ⭐️ 8.0/10

在日经的采访中，欧洲央行首席经济学家菲利普·莱恩讨论了欧元区的货币政策和经经济前景，就可能提供利率和通胀的前瞻指引。 莱恩的言论受到金融市场密切关注，以寻觅欧洲央行政策方向的线索，可能影响欧元、债券收益率和欧洲股市，尤其是在持续的经济不确定性中。 作为欧洲央行的首席经济学家，莱恩塑造了政策决策的分析框架；这次采访可能揭示欧洲央行对近期通胀趋势的评估以及货币宽松的适当步伐，但完整细节依赖于官方文本。

rss · ECB Press Releases · May 26, 10:00

**背景**: 欧洲央行为 20 个欧元区国家制定货币政策，目标为 2%的通胀率。菲利普·莱恩曾任爱尔兰央行行长，自 2019 年起担任欧洲央行首席经济学家，是管理委员会重要声音。欧洲央行 2021 年策略评估采用了对称通胀目标，其政策决策对欧洲和全球金融市场影响重大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Philip_R._Lane">Philip R. Lane - Wikipedia</a></li>
<li><a href="https://www.ecb.europa.eu/mopo/strategy/strategy-review/ecb.strategyreview_monpol_strategy_overview.en.html">An overview of the ECB ’s monetary policy strategy - 2021</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#currencies`, `#bonds`, `#europe`

---

<a id="item-7"></a>
## [欧央行执委施纳贝尔路透采访谈利率前景](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260526~6736a05aaa.en.html) ⭐️ 8.0/10

欧洲央行执委会成员伊莎贝尔·施纳贝尔接受路透社采访，讨论了欧元区货币政策前景，包括通胀趋势和未来利率路径。 作为执委会重要成员，她的言论可能显著改变市场对欧央行利率决策的预期，从而影响欧元区债券收益率和欧元汇率。 采访很可能强调了依赖数据决策的立场，并可能回应了市场对服务业通胀和工资增长持续担忧的问题，为政策调整时机提供线索。

rss · ECB Press Releases · May 26, 06:00

**背景**: 伊莎贝尔·施纳贝尔是欧洲央行执行委员会中具有影响力的成员，以其数据驱动的分析观点著称。随着通胀趋缓，欧央行逐步降息，但因服务业通胀粘性仍保持谨慎。此类采访常为市场提供非正式政策指引，是投资者关注欧元区货币政策走向的关键事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank - Wikipedia</a></li>
<li><a href="https://www.ecb.europa.eu/mopo/html/index.en.html">Overview of monetary policy and markets - European Central Bank</a></li>
<li><a href="https://www.cnbc.com/2026/02/05/ecb-rate-decision-economists-analysts-next-move.html">ECB holds rates but it's not a 'non-event,' economists say ...</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`, `#bonds`

---

<a id="item-8"></a>
## [美联储公布 2026 年 4 月 28-29 日 FOMC 会议纪要](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260520a.htm) ⭐️ 8.0/10

会议纪要详细揭示了联邦公开市场委员会对通胀、就业及货币政策路径的讨论，为未来利率调整提供线索。 会议纪要有望改变市场对联邦基金利率的预期，从而影响美国国债收益率、美元和股市，因投资者将仔细解读委员会的基调与经济展望。 纪要涵盖 2026 年 4 月 28-29 日的会议，当时通胀和劳动力市场数据可能影响了决策者的看法；公布内容可能揭示投票委员之间的分歧或共识程度。

rss · Federal Reserve Press Releases · May 20, 18:00

**背景**: 联邦公开市场委员会是美联储系统内的 12 人决策机构，通过设定联邦基金利率目标来制定美国货币政策。它每年召开八次会议评估经济状况，并决定利率和资产购买。会议纪要在每次会议三周后发布，提供更详细的政策讨论记录。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Open_Market_Committee">Federal Open Market Committee</a></li>
<li><a href="https://www.federalreserve.gov/monetarypolicy/fomc.htm">The Fed - Federal Open Market Committee</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#united-states`, `#bonds`, `#currencies`

---

<a id="item-9"></a>
## [以军空袭黎巴嫩，加沙援助受限](https://news.un.org/feed/view/en/story/2026/05/1167590) ⭐️ 7.0/10

联合国报告称，以色列连夜对黎巴嫩发动猛烈空袭，导致民众再次逃离家园，同时加沙地带的人道主义援助物资进入仍持续受限。 局势升级可能引发与真主党乃至伊朗的更广泛冲突，给外交斡旋带来压力并可能扰乱能源市场；加沙援助受限则加剧了本已严峻的人道主义危机。 空袭是针对真主党的军事行动的一部分，该组织向以色列发射火箭弹；在加沙，联合国此前报告称以色列任意阻挠了大部分援助物资的进入。

rss · UN News · May 26, 12:00

**背景**: 自 2024 年 10 月以来，以色列与真主党之间的敌对行动升级，双方跨境交火，黎巴嫩境内发布疏散令。加沙方面，2023 年开始的战争导致严重人道主义危机，以色列当局多次限制援助进入，联合国和国际社会对违反国际法的行为表示关切。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.npr.org/2024/08/25/nx-s1-5089083/israel-airstrikes-lebanon-hezbollah">Israel hits Hezbollah targets in Lebanon in what it's calling... : NPR</a></li>
<li><a href="https://www.unrwa.org/resources/reports/unrwa-situation-report-197-situation-gaza-strip-and-west-bank-including-east-jerusalem">UNRWA Situation Report #197 on the Humanitarian Crisis in the ...</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#military-risk`, `#diplomacy`, `#geopolitics`, `#energy`

---

<a id="item-10"></a>
## [安理会就卢甘斯克宿舍遇袭指控召开紧急会议](https://news.un.org/feed/view/en/story/2026/05/1167578) ⭐️ 7.0/10

应俄罗斯要求，联合国安理会召开会议，此前莫斯科指责乌克兰袭击了被占领土卢甘斯克的一栋学生宿舍，造成包括儿童在内的六名平民死亡。乌克兰否认这一指控，称其打击的是俄罗斯军用无人机指挥所。 此事件加剧外交紧张局势，突显在冲突叙事矛盾中核实平民伤亡的挑战，可能影响国际法律评估，并进一步分化联合国安理会。 据称袭击发生在俄占卢甘斯克地区的斯塔罗比尔斯克。联合国对平民伤亡表示震惊，而乌克兰坚称目标是军事设施，凸显冲突中事实认定的严重分歧。

rss · UN News · May 22, 12:00

**背景**: 卢甘斯克是乌克兰的一个地区，自 2022 年以来大部分被俄罗斯军队控制。联合国安理会负有维护国际和平的主要责任，但常因俄罗斯等常任理事国的否决权而陷入瘫痪。国际人道法要求冲突方区分平民与战斗员，禁止直接攻击平民。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cfr.org/backgrounders/un-security-council">The UN Security Council | Council on Foreign Relations</a></li>
<li><a href="https://www.icrc.org/en/law-and-policy/protected-persons-civilians">Protected persons: Civilians | ICRC</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#russia-ukraine`, `#united-nations`, `#military-risk`

---

<a id="item-11"></a>
## [俄军空袭第聂伯罗致平民死亡、毁坏联合国援助物资](https://news.un.org/feed/view/en/story/2026/05/1167562) ⭐️ 7.0/10

周二晚，俄罗斯对第聂伯罗的导弹和无人机袭击造成平民死亡，并摧毁了联合国难民署的人道主义援助物资，该机构驻乌克兰代表对此表示强烈谴责。 这次袭击凸显了针对平民设施和援助物资的违反国际人道法行为，可能加大对俄罗斯的外交压力，并影响西方对乌克兰的进一步支持。 袭击发生在周二夜间的第聂伯罗市；联合国难民署援助物资被毁；驻乌克兰代表予以谴责。未提及任何俄方军事目标，符合多次打击平民区的模式。

rss · UN News · May 20, 12:00

**背景**: 自 2022 年俄罗斯入侵以来，第聂伯罗一直是人道主义援助的后勤枢纽和流离失所者的避难所。联合国难民署在乌克兰提供保护和援助。俄罗斯对平民区的多次打击已屡遭国际谴责。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unhcr.org/where-we-work/countries/ukraine">Ukraine | UNHCR</a></li>
<li><a href="https://www.jurist.org/news/2025/09/un-responds-to-civilian-harm-following-russias-latest-strikes-on-ukraine/">UN responds to civilian harm following latest Russia strikes ...</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#diplomacy`, `#military-risk`, `#europe`

---

<a id="item-12"></a>
## [加沙药物封锁与疾病蔓延致人道危机恶化](https://news.un.org/feed/view/en/story/2026/05/1167572) ⭐️ 6.0/10

联合国机构周五警告，加沙的基本医疗用品仍被封锁，持续暴力、鼠患和传染病蔓延正使人道状况严重恶化。 这可能加大国际社会对停火和援助准入的外交压力，影响联合国安理会的讨论和援助政策，并可能增加对以色列放松限制的施压。 无国界医生组织称自 2026 年 1 月 1 日起未能运入任何物资，非传染性疾病药物严重短缺；近东救济工程处已裁员 600 人并削减薪资。

rss · UN News · May 22, 12:00

**背景**: 自战争爆发以来，以色列加强了对加沙的封锁，导致燃料、食品、水和医疗物资严重短缺。联合国近东救济工程处是加沙主要的人道主义援助机构，但其运作因准入限制和资金问题严重受阻。由美国、埃及和卡塔尔斡旋的停火谈判一再陷入僵局，而人道局势持续恶化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaza_humanitarian_crisis">Gaza humanitarian crisis - Wikipedia</a></li>
<li><a href="https://www.doctorswithoutborders.org/latest/aid-and-supplies-are-still-being-blocked-entering-gaza">Aid and supplies are still being blocked from entering Gaza | Doctors Without Borders - USA</a></li>
<li><a href="https://www.unrwa.org/resources/reports/unrwa-situation-report-218-humanitarian-crisis-gaza-strip-and-occupied-west-bank">UNRWA Situation Report #218 on the Humanitarian Crisis in the ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#supply-chain`, `#middle-east`

---

<a id="item-13"></a>
## [联合国特使警告：加沙过渡计划若停滞或陷永久僵局](https://news.un.org/feed/view/en/story/2026/05/1167568) ⭐️ 6.0/10

周四在安理会会议上，一名联合国高级特使警告，执行安理会支持的加沙过渡计划出现延误，正在加剧苦难，并可能导致永久僵局，此时脆弱的停火和人道状况持续恶化。 过渡停滞可能延长加沙的不稳定状态，损害地区安全与外交努力，并可能对以巴紧张局势及更广泛的中东地缘政治产生溢出效应。 安理会第 2803 号决议（2025 年 11 月）授权的过渡计划包括设立“和平委员会”以支持治理，但解除武装问题仍未解决，停火已出现裂痕。

rss · UN News · May 21, 12:00

**背景**: 2025 年 11 月 17 日通过的第 2803 号决议为加沙战后治理建立了框架，纳入了美国支持的和平计划。以色列与哈马斯于 2025 年 1 月达成的停火协议脆弱，同年 3 月破裂，随后出现大规模拆毁和持续暴力。约旦河西岸的冲突和人道危机也在升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167568">Gaza risks ‘permanent’ state of limbo if transition plan ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gaza_Strip_under_Resolution_2803">Gaza Strip under Resolution 2803 - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2025/11/17/world/middleeast/un-security-council-gaza-peace-plan.html">U.N. Security Council Adopts Trump’s Peace Plan for Gaza ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`

---

<a id="item-14"></a>
## [古特雷斯谴责以军占用 UNRWA 驻地建军事设施](https://news.un.org/feed/view/en/story/2026/05/1167560) ⭐️ 6.0/10

联合国秘书长安东尼奥·古特雷斯强烈谴责以色列决定在占领的东耶路撒冷一处被没收的 UNRWA 驻地建立军事设施，称此举“完全不可接受”。以色列政府于 2026 年 5 月 18 日批准了在该地点建设国防综合体的计划。 这一谴责加剧了以巴冲突的外交紧张局势，可能加大对以色列处理联合国机构和占领领土的国际压力。此举可能导致联合国安理会讨论及以色列的进一步孤立。 该驻地原为 UNRWA 在东耶路撒冷的总部，以色列此前已禁止该机构运营并没收其财产。规划的军事综合体将包括以色列国防军博物馆、征兵办公室和国防部长办公室，从而实际上巩固了以色列对该地点的控制。

rss · UN News · May 20, 12:00

**背景**: UNRWA 是自 1949 年以来向巴勒斯坦难民提供援助的联合国机构，在加沙、西岸（包括东耶路撒冷）及邻国开展活动。东耶路撒冷在国际法下被视为被占领的巴勒斯坦领土，尽管以色列于 1980 年吞并了该地。2024 至 2025 年，以色列指称 UNRWA 与哈马斯有关联，禁止该机构并没收其财产。国际法院后来认定以色列的指控缺乏充分证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNRWA">UNRWA</a></li>
<li><a href="https://www.timesofisrael.com/israel-approves-new-defense-complex-at-former-unrwa-east-jerusalem-headquarters/">Israel approves new defense complex on site of former UNRWA ...</a></li>
<li><a href="https://apnews.com/article/israel-unrwa-jerusalem-military-compound-palestinian-ad6e610f64415f2f994d29b3faf656e2">Israel to build military compound on UN relief agency site ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#israel`, `#united-nations`

---

<a id="item-15"></a>
## [菲利普·莱恩谈欧洲与世界经济](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260522~f0f11a5f05.en.html) ⭐️ 6.0/10

欧洲央行执委菲利普·莱恩发表了关于欧洲与世界经济的演讲，可能在全球不确定性背景下透露欧洲央行政策前景的线索。 他的言论可能暗示欧洲央行货币政策的变化，影响市场对利率和资产购买的预期，特别是如果他强调贸易紧张或地缘政治逆风等新风险。 提供的摘要未透露具体细节；演讲可能涵盖增长、通胀和外部风险，市场关注其是否偏离近期的鸽派指引。

rss · ECB Press Releases · May 22, 01:15

**背景**: 菲利普·莱恩是欧洲央行首席经济学家兼执行委员会委员，负责货币政策分析。欧洲央行一直在应对高通胀、增长放缓和贸易政策及地缘冲突带来的不确定性。他的演讲通常在政策会议前引导市场预期。从演讲标题看，可能涉及全球经济相互联系及其对欧元区的影响。

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`

---