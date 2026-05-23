---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> From 40 items, 12 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [《不扩散核武器条约》审议大会未达成共识](#item-2) ⭐️ 9.0/10
3. [无人机袭阿联酋核电，安理会急议](#item-3) ⭐️ 9.0/10
4. [凯文·沃什宣誓就任美联储主席，FOMC 一致推选其为委员会主席](#item-4) ⭐️ 9.0/10
5. [2026 年 4 月 FOMC 会议纪要暗示鹰派转向，考虑放弃宽松倾向](#item-5) ⭐️ 9.0/10
6. [霍尔木兹危机扰乱全球贸易与能源成本](#item-6) ⭐️ 8.0/10
7. [联合国震惊于卢甘斯克宿舍遭致命袭击](#item-7) ⭐️ 7.0/10
8. [联合国大会通过决议支持国际法院气候意见](#item-8) ⭐️ 7.0/10
9. [欧洲央行莱恩谈欧洲与世界经济](#item-9) ⭐️ 7.0/10
10. [联合国警告：加沙过渡计划若停滞恐陷永久僵局](#item-10) ⭐️ 6.0/10
11. [古特雷斯谴责以色列在没收的 UNRWA 大院设立军事设施](#item-11) ⭐️ 6.0/10
12. [古特雷斯呼吁重开霍尔木兹海峡并改革安理会](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 23, 22:46

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
| ^NDX price trend | close=29481.64; 1d=+0.42%; 5d=+1.22%; 20d=+7.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29558.75; 1d=+0.38%; 5d=+1.12%; 20d=+7.74% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=717.54; 1d=+0.42%; 5d=+1.21%; 20d=+8.08% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=13.1%; implied_move=1.0%; put/call OI=2.078502574937277 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
| ^NDX price trend | close=29481.64; 1d=+0.42%; 5d=+1.22%; 20d=+7.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29558.75; 1d=+0.38%; 5d=+1.12%; 20d=+7.74% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=717.54; 1d=+0.42%; 5d=+1.21%; 20d=+8.08% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| MSFT price trend | close=418.57; 1d=-0.12%; 5d=-0.58%; 20d=-1.21% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=215.33; 1d=-1.90%; 5d=-4.43%; 20d=+3.39% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=610.26; 1d=+0.47%; 5d=-0.65%; 20d=-9.60% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=308.82; 1d=+1.26%; 5d=+2.86%; 20d=+14.04% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=426.01; 1d=+1.95%; 5d=+0.89%; 20d=+13.21% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=382.97; 1d=-1.21%; 5d=-3.48%; 20d=+11.20% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| GOOGL options surface | ATM IV=19.1%; implied_move=1.6%; put/call OI=0.5876896402254009 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=18.5%; implied_move=1.5%; put/call OI=0.3705599747971962 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=25.3%; implied_move=2.1%; put/call OI=0.411732603978068 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=14.1%; implied_move=1.1%; put/call OI=0.6938888632269389 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=28.0%; implied_move=2.3%; put/call OI=0.6260825456524967 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=19.2%; implied_move=1.6%; put/call OI=0.8807740324594258 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| NVDA insider filings | recent Form4 count=562 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| MSFT insider filings | recent Form4 count=731 | 内部人交易节奏可作为估值温度辅助校验信号。 |

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
| MSFT price trend | close=418.57; 1d=-0.12%; 5d=-0.58%; 20d=-1.21% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=215.33; 1d=-1.90%; 5d=-4.43%; 20d=+3.39% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=610.26; 1d=+0.47%; 5d=-0.65%; 20d=-9.60% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 7203.T price trend | close=2987.00; 1d=+0.30%; 5d=-3.18%; 20d=-11.89% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=49830.00; 1d=+2.11%; 5d=-0.91%; 20d=+12.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3525.00; 1d=-0.82%; 5d=-1.43%; 20d=+4.17% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=91.61; 1d=+0.26%; 5d=+0.59%; 20d=+4.91% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6757.00; 1d=+11.89%; 5d=+17.62%; 20d=+41.54% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=79370.00; 1d=+3.13%; 5d=+2.84%; 20d=+23.96% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 7203.T price trend | close=2987.00; 1d=+0.30%; 5d=-3.18%; 20d=-11.89% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=49830.00; 1d=+2.11%; 5d=-0.91%; 20d=+12.61% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3525.00; 1d=-0.82%; 5d=-1.43%; 20d=+4.17% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 1810.HK price trend | close=30.00; 1d=+1.15%; 5d=-2.28%; 20d=-3.78% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=23.49; 1d=-1.43%; 5d=-2.37%; 20d=+0.56% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=81.35; 1d=-0.91%; 5d=-1.63%; 20d=-2.11% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=127.00; 1d=+0.79%; 5d=-4.01%; 20d=-2.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=441.40; 1d=+0.55%; 5d=-3.29%; 20d=-9.83% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=26.91; 1d=-2.61%; 5d=-4.47%; 20d=-6.66% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.56; 2Y=4.13; 10Y-2Y=0.4299999999999997 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=58.6; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
| 1810.HK price trend | close=30.00; 1d=+1.15%; 5d=-2.28%; 20d=-3.78% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=23.49; 1d=-1.43%; 5d=-2.37%; 20d=+0.56% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=81.35; 1d=-0.91%; 5d=-1.63%; 20d=-2.11% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [ICE BofA US Bond Market Option Volatility Estimate Index](https://www.cnbc.com/quotes/.MOVE)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get ICE BofA US Bond Market Option Volatility Estimate Index (.MOVE:NYSE Arca) real-time stock quotes, news, price and financial information from CNBC.

- [Cboe Global Indices: VIX Index Dashboard](https://www.cboe.com/us/indices/dashboard/vix/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：The VIX Index is often referred to as the market's "fear gauge". The VIX Index is the centerpiece of Cboe Global Markets' volatility franchise, which includes volatility indexes...

- [VIX Volatility Index (Fear Gauge) - Live Chart & Guide / WhaleQuant](https://whalequant.io/en/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Explore the VIX Volatility Index, Wall Street's fear gauge. View live VIX levels, historical volatility chart, volatility regimes, and a practical guide on how to read VIX, term...

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Volatility Term Structure chart plots the at-the-money implied volatility across expirations, which are an invaluable tool in determining options strategies based on anticipated...

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

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
  - 摘要：U.S. High Yield Bond Spread: 3.08% as of May 20, 2026. Units: Percent Frequency: Daily, Close Release: ICE BofA Indices Source: Ice Data Indices, LLC

- [QQQ Options Chain — Open Interest, Implied Volatility, Max Pain & Gamma ...](https://whalequant.io/en/stocks/QQQ/options-analytics)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Explore the live QQQ options chain with strikes, open interest, volume, implied volatility (IV), max pain levels, gamma exposure, dealer positioning and options flow analysis. P...

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [Valuta EX - Currency Converter / Real-Time Exchange Rates](https://valuta.exchange/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

- [USD JPY Exchange Rate, Live USD to JPY Forex Rate at Forex Rates](https://www.forexrates.net/fx-rates/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：USD JPY Exchange Rate This is the live USD JPY rate forex data page, displaying the FX price for the USD/JPY. The FX rate self-updates every few seconds. Compare exchange rates...

- [USD to Japanese Yen Exchange Rate Today / Real-Time Currency Converter](https://xe-rates.com/usd-to-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Convert USD to JPY with real-time exchange rates. Free, fast currency converter with up-to-date rates for US Dollar to Japanese Yen conversions. Updated hourly.

- [EWJ - iShares MSCI Japan ETF - ETF Stock Quote / Morningstar](https://www.morningstar.com/etfs/arcx/ewj/quote)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ - iShares MSCI Japan ETF - Check EWJ price, review total assets, see historical growth, and review the analyst rating from Morningstar.

- [iShares MSCI Japan ETF (EWJ) stock price, news, quote and history ...](https://sg.finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [iShares MSCI Japan ETF (EWJ) Price, Holdings, & News](https://www.marketbeat.com/stocks/NYSEARCA/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Should You Buy or Sell iShares MSCI Japan ETF Stock? Get The Latest EWJ Stock Price, Constituents List, Holdings Data, and Headlines at MarketBeat.

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
## [《不扩散核武器条约》审议大会未达成共识](https://news.un.org/feed/view/en/story/2026/05/1167580) ⭐️ 9.0/10

第十一次《不扩散核武器条约》（NPT）审议大会在纽约联合国总部经过四周谈判后于周五结束，未能就最终宣言达成共识。 会议未能通过最后宣言，严重削弱了全球核不扩散机制，加剧了对新一轮核军备竞赛的担忧，并破坏了遏制核扩散的外交努力。 本次会议于 2026 年 4 月 27 日至 5 月 22 日举行，是第十一次审议大会。未能达成共识，与 2015 年及推迟的 2020 年会议失败情形相似。

rss · UN News · May 23, 12:00

**背景**: 《不扩散核武器条约》自 1970 年生效，是全球裁军努力的基石，旨在防止核武器扩散、促进和平利用核能并推进核裁军。审议大会每五年举行一次以评估条约执行情况。五个公认的核武器国家是美国、俄罗斯、英国、法国和中国。2010 年审议大会成功通过了最后宣言，但 2015 年和 2020 年（于 2021 年举行）的会议均因在裁军进展和中东无核武器区等问题上的分歧而未达成共识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.un.org/en/conferences/treaty-on-the-non-proliferation-of-nuclear-weapons-npt-2026">NPT Conference 2026 - Review conference of the parties to the treaty on NPT | United Nations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nuclear_Non-Proliferation_Treaty_(NPT)">Nuclear Non-Proliferation Treaty (NPT)</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`

---

<a id="item-3"></a>
## [无人机袭阿联酋核电，安理会急议](https://news.un.org/feed/view/en/story/2026/05/1167550) ⭐️ 9.0/10

2026 年 5 月 17 日，一架无人机袭击了阿联酋巴拉卡核电站附近，引发外围火灾。阿联酋国防部称该无人机源自伊拉克境内。联合国安理会随后召开紧急会议，国际原子能机构总干事格罗西就核安全与安保风险升高向成员国通报。 此次无人机袭击在中东动荡地区引发严重的核安全风险，可能导致放射性后果。这可能会扰乱能源市场、加剧地区军事紧张局势，并促使国际制裁或军事回应，尤其是考虑到无人机据称来自伊拉克。 火灾仅限于电站外围，未有辐射泄漏报告。国际原子能机构正密切监测局势，安理会可能考虑决议或其他措施。

rss · UN News · May 19, 12:00

**背景**: 巴拉卡核电站由阿联酋核能公司运营，是阿拉伯世界首座核电站，供应阿联酋约 25%的电力。联合国安理会是负责维护国际和平与安全的联合国机构，五个常任理事国拥有否决权。国际原子能机构是一个政府间组织，促进核能的安全与和平利用，并就核安全威胁向安理会报告。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/Barakah_nuclear_power_plant">Barakah nuclear power plant</a></li>
<li><a href="https://en.wikipedia.org/wiki/IAEA">IAEA</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#nuclear-safety`, `#military-risk`

---

<a id="item-4"></a>
## [凯文·沃什宣誓就任美联储主席，FOMC 一致推选其为委员会主席](https://www.federalreserve.gov/newsevents/pressreleases/other20260522a.htm) ⭐️ 9.0/10

凯文·沃什宣誓就任联邦储备系统理事会主席和成员，联邦公开市场委员会（FOMC）一致推选他担任委员会主席。 鉴于沃什广为人知的分化立场（对资产负债表持鹰派态度但对政策利率持鸽派立场），此次领导层变动可能改变美国货币政策，进而影响全球利率、货币和风险资产。 沃什曾在 2006 年至 2011 年担任美联储理事，一直批评量化宽松政策，但最近却暗示偏好低利率，这预示着美联储可能在量化紧缩与降息之间作出调整。

rss · Federal Reserve Press Releases · May 22, 20:15

**背景**: 美联储理事会由七名成员组成，FOMC 则包括所有理事和 12 位联邦储备银行行长中的五位。按照惯例，美联储主席同时担任 FOMC 主席，主导短期货币政策。凯文·沃什曾担任美联储理事，此次由总统提名并经参议院确认出任该职位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kevin_Warsh">Kevin Warsh - Wikipedia</a></li>
<li><a href="https://learn.backpack.exchange/articles/who-is-kevin-warsh">Who Is Kevin Warsh ? Trump's Fed Chair Pick Explained (2026)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federal_Reserve_Board_of_Governors">Federal Reserve Board of Governors - Wikipedia</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#currency`, `#bonds`, `#global-markets`

---

<a id="item-5"></a>
## [2026 年 4 月 FOMC 会议纪要暗示鹰派转向，考虑放弃宽松倾向](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260520a.htm) ⭐️ 9.0/10

2026 年 4 月 FOMC 会议纪要显示，决策者们正在积极考虑取消委员会的宽松倾向，这可能预示着未来会议将转向加息。 这一转变影响对美国货币政策的预期，可能引发全球债券收益率、货币和股票市场的重新定价，因为投资者需适应美联储更加鹰派的立场。 纪要提供了对经济前景的详细分析，包括通胀评估和劳动力市场状况，但未具体说明利率变动的时间表。

rss · Federal Reserve Press Releases · May 20, 18:00

**背景**: 联邦公开市场委员会（FOMC）是美联储的货币政策制定机构，负责设定联邦基金利率目标。会议纪要于每次会议后三周发布，提供委员会审议的深入见解。‘宽松倾向’表明降息倾向，其取消通常预示着随后加息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Federal_Open_Market_Committee">Federal Open Market Committee</a></li>
<li><a href="https://www.investing.com/economic-calendar/fomc-meeting-minutes-108">U.S. Federal Reserve (Fed) Meeting Minutes</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#global-markets`, `#bonds`, `#currencies`

---

<a id="item-6"></a>
## [霍尔木兹危机扰乱全球贸易与能源成本](https://news.un.org/feed/view/en/story/2026/05/1167548) ⭐️ 8.0/10

尽管美伊达成脆弱停火，霍尔木兹海峡持续不稳定仍在扰乱全球航运、推高能源价格并加剧生活成本危机。 霍尔木兹海峡承担全球逾二成石油运输；持续不稳定推高全球能源成本，助长通胀并威胁经济复苏。 分析师指出，即便间歇性中断也强化石油和液化天然气的地缘政治风险溢价；完全封锁将影响全球 20%的供应。

rss · UN News · May 19, 12:00

**背景**: 霍尔木兹海峡是连接波斯湾与阿拉伯海的狭窄通道，对全球石油和液化天然气出口至关重要。由于伊朗有能力威胁航运，该地区长期是地缘政治热点。2026 年伊朗战争导致海峡暂时封锁，随后美伊达成脆弱停火，但局势依然紧张。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.britannica.com/place/Strait-of-Hormuz">Strait of Hormuz | Map, Importance, Conflict and Closure, Control, Oil ...</a></li>
<li><a href="https://www.woodmac.com/press-releases/strait-of-hormuz-closure-risks-greatest-global-energy-supply-shock-in-decades/">Strait of Hormuz closure risks greatest global energy supply shock in decades | Wood Mackenzie</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Iran_war">2026 Iran war - Wikipedia</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#energy`, `#supply-chain`, `#middle-east`, `#global-markets`

---

<a id="item-7"></a>
## [联合国震惊于卢甘斯克宿舍遭致命袭击](https://news.un.org/feed/view/en/story/2026/05/1167579) ⭐️ 7.0/10

联合国对有关卢甘斯克州斯塔罗比尔斯克一所职业学校和宿舍遭夜间袭击的报道表示震惊，袭击造成至少六名平民（含儿童）死亡。俄罗斯指责乌克兰故意袭击该宿舍，乌方则称其打击的是俄军无人机指挥部。 该事件加剧外交裂痕，可能引发联合国安理会关于平民保护的辩论，影响国际叙事及未来对乌军事援助。同时也凸显了冲突中军事与民用目标界限模糊的问题。 俄方任命的州长声称学生宿舍遭袭，安理会应莫斯科要求召开会议。乌克兰否认攻击平民目标，坚称目标是俄军无人机指挥中心。联合国尚未独立核实该事件。

rss · UN News · May 22, 12:00

**背景**: 卢甘斯克是俄罗斯 2022 年声称吞并的四个乌克兰地区之一，国际社会普遍不承认这一行为。联合国安理会是维护和平与安全的主要机构，但因俄罗斯的否决权在乌克兰问题上陷入僵局。双方此前都曾指责对方袭击平民。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Russian-occupied_territories_of_Ukraine">Russian- occupied territories of Ukraine - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Starobilsk_strike">2026 Starobilsk strike - Wikipedia</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#diplomacy`, `#military-risk`, `#europe`, `#geopolitics`

---

<a id="item-8"></a>
## [联合国大会通过决议支持国际法院气候意见](https://news.un.org/feed/view/en/story/2026/05/1167561) ⭐️ 7.0/10

联合国大会周三通过一项决议，支持国际法院关于各国气候义务的咨询意见，联合国秘书长安东尼奥·古特雷斯称这是对国际法、气候正义和科学的有力肯定。 该决议加强了气候诉讼的法律基础，并向政府和企业施压以加速脱碳，对全球监管风险、能源转型和 ESG 投资产生影响。 决议在联合国大会第 80 届会议上通过；虽不具法律约束力，但具有重大外交分量，并强化了国际法院的裁定，即国际法要求各国防止严重气候损害。

rss · UN News · May 20, 12:00

**背景**: 国际法院是联合国的主要司法机关，其咨询意见虽不具约束力，但阐明了国际法。联合国大会由 193 个成员国平等代表，可请求此类意见并通过决议表达集体意愿。该气候意见确认了各国防止损害的义务，并引发了关于气候正义的辩论，气候正义关注气候变化对弱势群体的不成比例影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.un.org/en/ga/">General Assembly of the United Nations</a></li>
<li><a href="https://www.iisd.org/articles/deep-dive/icj-advisory-opinion-climate-change">Historic International Court of Justice Opinion Confirms States...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Climate_justice">Climate justice</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#energy`, `#commodities`, `#global-markets`

---

<a id="item-9"></a>
## [欧洲央行莱恩谈欧洲与世界经济](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260522~f0f11a5f05.en.html) ⭐️ 7.0/10

欧洲央行首席经济学家菲利普·莱恩于 2022 年 5 月 26 日发表了题为'欧洲与世界经济'的演讲，内容涉及欧元区前景、货币政策及全球风险。 此次演讲可能表明欧洲央行在高通胀和地缘政治紧张局势下的政策立场，影响欧元/美元、债券收益率和股市，并可能提供加息时机和步伐的线索。 莱恩通常被视为鸽派，其关于通胀持续性和增长风险的言论备受关注；在俄乌战争和能源价格背景下，任何鹰派转向或对分裂的担忧都可能引发市场波动。

rss · ECB Press Releases · May 22, 01:15

**背景**: 菲利普·莱恩是欧洲央行首席经济学家，在货币政策制定中发挥关键作用。2022 年 5 月，欧洲央行正筹备退出刺激措施，通胀因供给冲击和能源成本高企而远超目标。欧元区面临战争相关不确定性和金融分裂风险。莱恩此次演讲正值六月关键政策会议前夕，市场普遍预期届时将开启加息。

**标签**: `#central-bank`, `#europe`, `#macroeconomics`, `#currency`, `#global-markets`

---

<a id="item-10"></a>
## [联合国警告：加沙过渡计划若停滞恐陷永久僵局](https://news.un.org/feed/view/en/story/2026/05/1167568) ⭐️ 6.0/10

一名联合国高级特使在安理会警告称，由于停火协议岌岌可危和人道主义状况恶化，落实安理会支持的加沙过渡计划的延误可能导致永久性僵局。 这凸显了外交紧迫性和冲突升级的可能，可能影响国际谈判、人道主义资金以及区域稳定，对中东地缘政治和军事冲突再起的风险产生影响。 关键细节：根据 2025 年 11 月通过的联合国安理会第 2803 号决议，该过渡计划设想了一个加沙过渡管理机构，但执行已陷入停滞；同时，停火仍然脆弱，平民伤亡持续，裁军未见进展。

rss · UN News · May 21, 12:00

**背景**: 加沙战争于 2023 年 10 月爆发，引发严重人道主义危机。2025 年 1 月达成停火协议，随后联合国安理会在 2025 年 11 月通过第 2803 号决议，规划了过渡治理路径。然而，停火屡遭违反，局势恶化，出现大范围饥荒和基础设施损毁。联合国特使发出警告之际，人们愈发担心政治真空和援助封锁正将加沙推向永久不稳定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167568">Gaza risks ‘permanent’ state of limbo if transition plan stalls, Security Council hears | UN News</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Security_Council_Resolution_2803">United Nations Security Council Resolution 2803 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gaza_humanitarian_crisis">Gaza humanitarian crisis</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-11"></a>
## [古特雷斯谴责以色列在没收的 UNRWA 大院设立军事设施](https://news.un.org/feed/view/en/story/2026/05/1167560) ⭐️ 6.0/10

2026 年 5 月 20 日，联合国秘书长安东尼奥·古特雷斯以最强烈的措辞谴责以色列决定在东耶路撒冷谢赫贾拉街区的近东救济工程处（UNRWA）大院设立军事设施，该大院于今年 1 月被以色列没收。他称此举“完全不可接受”。 此次谴责加剧了联合国与以色列之间的外交紧张关系，引起国际社会对侵犯联合国驻地与国际法行为的关注，并可能在联合国论坛引发进一步辩论或决议，影响地区稳定。 谢赫贾拉大院在被没收前已由近东救济工程处使用数十年；古特雷斯指出军事用途违反了联合国特权和豁免。此次谴责正值以色列在被占领的东耶路撒冷持续扩建定居点和推进吞并行动之际。

rss · UN News · May 20, 12:00

**背景**: 联合国近东巴勒斯坦难民救济和工程处（UNRWA）自 1950 年起在东耶路撒冷为巴勒斯坦难民提供基本服务。东耶路撒冷自 1967 年以来被以色列占领，以色列在那里的定居点和吞并行为根据国际法是非法的。以色列与联合国之间的紧张关系因以色列在占领区的一再行动而加剧，包括此前对定居点扩建和军事行动的谴责。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://eng.chinamil.com.cn/2025xb/W/N/16462560.html">UN chief condemns Israeli decision to establish military facilities at...</a></li>
<li><a href="https://en.wikipedia.org/wiki/UNRWA">UNRWA - Wikipedia</a></li>
<li><a href="https://www.emirates247.com/world/un-condemns-israeli-decision-to-establish-military-facilities-in-unrwa-compound-in-east-jerusalem/1832">UN condemns Israeli decision to establish military ... - Emirates 24|7</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`, `#israel-palestine`

---

<a id="item-12"></a>
## [古特雷斯呼吁重开霍尔木兹海峡并改革安理会](https://news.un.org/feed/view/en/story/2026/05/1167555) ⭐️ 6.0/10

周三，联合国秘书长安东尼奥·古特雷斯敦促在 2026 年伊朗战争期间重新开放霍尔木兹海峡，并呼吁扩大安理会成员以限制常任理事国的否决权。 他的声明凸显了能源安全与外交僵局的关联：海峡封锁威胁全球油气供应，而安理会在冲突上的瘫痪凸显了改革的紧迫性，两者都影响市场和国际稳定。 未提供具体时间表或方案；安理会任何扩大或否决权改革都需五个常任理事国一致同意，它们历来抵制削弱自身权力的变革。

rss · UN News · May 20, 12:00

**背景**: 霍尔木兹海峡是伊朗与阿曼之间的狭窄水道，2023-2025 年间承载了全球 20%的液化天然气和 25%的海运石油。2026 年伊朗战争期间该海峡爆发危机。联合国安理会五个常任理事国（中国、法国、俄罗斯、英国、美国）对实质性决议拥有否决权，经常导致在冲突中无所作为。改革提案已流传数十年，但因五常反对及需要广泛共识而停滞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council_veto">UN Security Council veto</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council_reform">UN Security Council reform</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#middle-east`

---