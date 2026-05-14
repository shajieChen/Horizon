---
layout: default
title: "Horizon Summary: 2026-05-15 (ZH)"
date: 2026-05-15
lang: zh
---

> From 41 items, 12 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [联合国秘书长促霍尔木兹海峡紧急降级](#item-2) ⭐️ 10.0/10
3. [欧央行副行长德金多斯在金融时报采访中谈货币政策](#item-3) ⭐️ 8.0/10
4. [联黎部队警告无人机事件危及其在南黎巴嫩的人员安全](#item-4) ⭐️ 7.0/10
5. [联合国警告黎巴嫩和加沙危机恶化](#item-5) ⭐️ 7.0/10
6. [联合国：武装无人机致苏丹战争超八成平民死亡](#item-6) ⭐️ 7.0/10
7. [欧洲央行莱恩分析能源供应冲击](#item-7) ⭐️ 7.0/10
8. [拉加德：稳定币须分离货币与技术功能](#item-8) ⭐️ 7.0/10
9. [联合国欢迎美国 18 亿美元人道援助](#item-9) ⭐️ 6.0/10
10. [联合国斡旋协议下也门将释放 1600 名被拘留者](#item-10) ⭐️ 6.0/10
11. [联合国官员谴责俄罗斯对基辅平民的袭击](#item-11) ⭐️ 6.0/10
12. [古特雷斯呼吁改革以增强非洲全球话语权](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 14, 23:05

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
| Japan Equity Basket | JP | neutral 33/33/34 | neutral 33/33/34 | bullish 42/29/30 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| QQQ price trend | close=719.79; 1d=+0.71%; 5d=+3.58%; 20d=+12.38% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29580.30; 1d=+0.73%; 5d=+3.56%; 20d=+12.33% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29711.75; 1d=+0.79%; 5d=+3.59%; 20d=+12.17% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=1.9%; implied_move=0.1%; put/call OI=3.552764248483295 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.47; 2Y=4.0; 10Y-2Y=0.46999999999999975 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=66.1; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
| QQQ price trend | close=719.79; 1d=+0.71%; 5d=+3.58%; 20d=+12.38% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29580.30; 1d=+0.73%; 5d=+3.56%; 20d=+12.33% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29711.75; 1d=+0.79%; 5d=+3.59%; 20d=+12.17% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| MSFT price trend | close=409.43; 1d=+1.04%; 5d=-2.70%; 20d=-2.58% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=618.43; 1d=+0.29%; 5d=+0.26%; 20d=-8.63% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=401.07; 1d=-0.38%; 5d=+0.77%; 20d=+19.36% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=443.30; 1d=-0.44%; 5d=+7.65%; 20d=+13.99% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=267.22; 1d=-1.08%; 5d=-1.46%; 20d=+7.02% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=298.21; 1d=-0.22%; 5d=+3.84%; 20d=+13.32% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| NVDA options surface | ATM IV=35.1%; implied_move=2.1%; put/call OI=0.8604241841275334 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=41.4%; implied_move=2.4%; put/call OI=0.8232979311739206 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=25.1%; implied_move=1.5%; put/call OI=0.6335385363087764 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=25.5%; implied_move=1.5%; put/call OI=0.4710184500731667 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=22.3%; implied_move=1.3%; put/call OI=0.8608327755884109 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=23.2%; implied_move=1.3%; put/call OI=0.5265853690901129 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| NVDA insider filings | recent Form4 count=567 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.47; 2Y=4.0; 10Y-2Y=0.46999999999999975 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=66.1; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| MSFT price trend | close=409.43; 1d=+1.04%; 5d=-2.70%; 20d=-2.58% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=618.43; 1d=+0.29%; 5d=+0.26%; 20d=-8.63% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=401.07; 1d=-0.38%; 5d=+0.77%; 20d=+19.36% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 6861.T price trend | close=77310.00; 1d=-2.68%; 5d=-2.57%; 20d=+23.81% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=3008.00; 1d=+2.33%; 5d=+1.01%; 20d=-9.37% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=51200.00; 1d=-0.27%; 5d=-1.01%; 20d=+16.26% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.06; 1d=-1.11%; 5d=+1.18%; 20d=+2.96% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3444.00; 1d=-5.90%; 5d=+10.03%; 20d=+3.58% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=5770.00; 1d=-4.03%; 5d=-10.18%; 20d=+52.73% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=66.1; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.47; 2Y=4.0; 10Y-2Y=0.46999999999999975 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 跨层分歧信息有限，后续需补充更多波动与事件市场数据。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：有效交易信号不足，使用保守基准分布。
- 1月：20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1周 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1月 | 42% | 29% | 30% | bullish | 20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 6861.T price trend | close=77310.00; 1d=-2.68%; 5d=-2.57%; 20d=+23.81% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=3008.00; 1d=+2.33%; 5d=+1.01%; 20d=-9.37% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=51200.00; 1d=-0.27%; 5d=-1.01%; 20d=+16.26% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 1810.HK price trend | close=31.72; 1d=-0.25%; 5d=+1.93%; 20d=+2.65% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=37.24; 1d=-2.67%; 5d=+0.13%; 20d=+0.03% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=454.90; 1d=-0.52%; 5d=-3.60%; 20d=-7.78% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=85.70; 1d=-2.17%; 5d=+1.72%; 20d=-0.70% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=29.20; 1d=-4.54%; 5d=-1.08%; 20d=-2.99% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=137.90; 1d=+3.84%; 5d=-2.13%; 20d=+7.23% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.47; 2Y=4.0; 10Y-2Y=0.46999999999999975 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=66.1; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 跨层分歧信息有限，后续需补充更多波动与事件市场数据。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | medium |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | medium |
| 1月 | 42% | 29% | 30% | bullish | 20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高 | medium |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| 1810.HK price trend | close=31.72; 1d=-0.25%; 5d=+1.93%; 20d=+2.65% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=37.24; 1d=-2.67%; 5d=+0.13%; 20d=+0.03% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=454.90; 1d=-0.52%; 5d=-3.60%; 20d=-7.78% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。

### 信息缺口 (Missing Evidence)
- CMEFedWatchProvider: probabilities unavailable (request failed: https://www.cmegroup.com/services/fed-funds-target/fed-funds-target.json)
- insufficient independent market signal layers (<3).

### Trading 分析参考文章

- [Cboe Global Indices: VIX Index Dashboard](https://www.cboe.com/us/indices/dashboard/vix/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：The VIX Index is often referred to as the market's "fear gauge". The VIX Index is the centerpiece of Cboe Global Markets' volatility franchise, which includes volatility indexes...

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days or more out. IV is a forward looking prediction of the likelihood...

- [Cboe Global Indices: VXN Index Dashboard](https://www.cboe.com/us/indices/dashboard/VXN/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Cboe NASDAQ-100 Volatility Index SM (VXN) The Cboe NASDAQ-100 Volatility Index SM (VXN) is a key measure of market expectations of near-term volatility conveyed by NASDAQ-100 ®...

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
  - 摘要：U.S. High Yield Bond Spread: 3.07% as of May 8, 2026. Units: Percent Frequency: Daily, Close Release: ICE BofA Indices Source: Ice Data Indices, LLC

- [QQQ: Invesco QQQ Trust Option Overview / OptionCharts](https://optioncharts.io/options/QQQ)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View comprehensive QQQ options with our latest charts on volume, open interest, max pain, and implied volatility.

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [USD to JPY - US Dollar to Japanese Yen Conversion - Exchange Rates](https://www.exchange-rates.org/converter/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Use the USD to JPY currency converter at Exchange-Rates.org for accurate and up-to-date exchange rates. Easily convert US Dollars to Japanese Yen with real-time data.

- [1 USD to JPY - US Dollars to Japanese Yen Exchange Rate - Xe](https://www.xe.com/en/currencyconverter/convert/?Amount=1&From=USD&To=JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest 1 US Dollar to Japanese Yen rate for FREE with the original Universal Currency Converter. Set rate alerts for USD to JPY and learn more about US Dollars and Japan...

- [USD JPY / US Dollar to Yen Live Rate - Investing.com](https://www.investing.com/currencies/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get real time data on the USD/JPY pair including the live rate, as well as our currency converter, analysis, news, historical data and more.

- [Index Information - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index/profile?idx=nk225vi)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：The Nikkei Stock Average Volatility Index are calculated by using prices of Nikkei 225 futures and Nikkei 225 options on the Osaka Exchange (OSE). In the calculation, taking nea...

- [Nikkei Average Volatility (^NKVI.OS) - Yahoo Finance](https://finance.yahoo.com/quote/%5ENKVI.OS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Find the latest information on Nikkei Average Volatility (^NKVI.OS) including data, charts, related news and more from Yahoo Finance

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

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
## [联合国秘书长促霍尔木兹海峡紧急降级](https://news.un.org/feed/view/en/story/2026/05/1167478) ⭐️ 10.0/10

联合国秘书长安东尼奥·古特雷斯在周一早间油价上涨之际呼吁和平解决霍尔木兹海峡危机，并警告称其经济影响将扩大到非洲乃至全球。 由于霍尔木兹海峡是全球石油运输的关键咽喉，这场危机威胁着全球能源安全；长期封锁可能导致油价飙升、供应链中断，并破坏非洲及其他地区的经济稳定。 自 2026 年 2 月 28 日美国和以色列发动空袭以来，伊朗已基本封锁霍尔木兹海峡；据报道达成的停火协议取决于是否保证该航道安全通行。

rss · UN News · May 11, 12:00

**背景**: 霍尔木兹海峡承担着全球约五分之一的石油运输。2026 年危机始于 2 月 28 日美国和以色列对伊朗发动空袭并刺杀了最高领袖阿里·哈梅内伊，随后伊朗封锁了该海峡。联合国秘书长作为全球最高外交官，常在类似冲突中进行斡旋。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis">2026 Strait of Hormuz crisis - Wikipedia</a></li>
<li><a href="https://www.bbc.com/news/articles/c78n6p09pzno">Iran war: What is the Strait of Hormuz and why does it matter?</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#energy`, `#military-risk`, `#middle-east`, `#commodities`

---

<a id="item-3"></a>
## [欧央行副行长德金多斯在金融时报采访中谈货币政策](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260511~3fa2df2fa9.en.html) ⭐️ 8.0/10

欧央行副行长路易斯·德金多斯接受《金融时报》采访，讨论了欧元区的货币政策立场和经济前景，可能释放未来利率决策信号。 此次采访可能提供欧央行政策的前瞻指引，影响欧元区债券收益率、欧元汇率和欧洲股市，因投资者会从他的言论中寻找通胀和增长路径的线索。 虽然具体内容未提供，但如此高调的采访通常会涉及欧央行对通胀风险、增长动能以及政策利率适当路径的评估。

rss · ECB Press Releases · May 11, 04:00

**背景**: 欧央行是欧元区的中央银行，负责维持价格稳定。其副行长的公开言论受到密切关注，以获取政策信号。欧元区由 21 个已采用欧元的欧盟成员国组成，主要经济体包括德国、法国和意大利。欧央行一直在应对疫情后的通胀和不均衡增长，因此此类采访对市场预期至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://en.wikipedia.org/wiki/Eurozone">Eurozone</a></li>
<li><a href="https://en.wikipedia.org/wiki/Monetary_policy">Monetary policy</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#europe`, `#macroeconomics`, `#currency`, `#bonds`

---

<a id="item-4"></a>
## [联黎部队警告无人机事件危及其在南黎巴嫩的人员安全](https://news.un.org/feed/view/en/story/2026/05/1167496) ⭐️ 7.0/10

联合国驻黎巴嫩临时部队（联黎部队）警告称，涉及真主党和以色列军队的无人机活动及附近爆炸事件不断升级，正危及维和人员安全并威胁黎巴嫩南部的稳定。 这一警告表明以色列与真主党之间的军事升级风险加剧，可能将联合国部队卷入交火或引发外交干预，从而重塑地区安全格局。 联黎部队由来自 48 个国家的 8000 多名军人组成，根据联合国安理会第 1701 号决议监督蓝线；近期事件涉及疑似真主党无人机及以色列在联合国阵地附近的军事回应。

rss · UN News · May 13, 12:00

**背景**: 联黎部队于 1978 年成立，旨在恢复以色列-黎巴嫩边境的和平与安全，其任务授权在 2006 年战争后扩大。真主党是一个拥有强大武装力量的黎巴嫩什叶派伊斯兰组织，自 2023 年 10 月以来一直与以色列交战。尽管有停火努力，敌对行动仍在继续，已导致数千人流离失所，并引发对更广泛冲突的担忧。联黎部队的存在旨在协助停止敌对行动，并支持黎巴嫩政府在该地区行使权力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNIFIL">UNIFIL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>
<li><a href="https://www.cfr.org/global-conflict-tracker/conflict/political-instability-lebanon">Conflict With Hezbollah in Lebanon | Global Conflict Tracker</a></li>

</ul>
</details>

**标签**: `#military-risk`, `#middle-east`, `#diplomacy`

---

<a id="item-5"></a>
## [联合国警告黎巴嫩和加沙危机恶化](https://news.un.org/feed/view/en/story/2026/05/1167483) ⭐️ 7.0/10

联合国报告称，尽管与以色列上个月达成了停火协议，黎巴嫩的人道主义状况仍在恶化，加沙的暴力活动也持续不断，引发了对停火持久性和地区稳定的担忧。 持续不断的暴力事件可能破坏脆弱的停火协议，颠覆外交成果，加剧地区紧张局势，并对能源市场和人道主义成本产生潜在溢出效应。 2024 年 11 月的停火协议要求真主党解除武装并以色列撤军，但双方均有违规报道，人道主义伤亡持续上升。

rss · UN News · May 11, 12:00

**背景**: 2023 年 10 月，真主党为声援哈马斯袭击以色列，导致数月跨境交火。2024 年 10 月，以色列对黎巴嫩发动地面进攻。2024 年 11 月 27 日，在美国等各方调解下达成停火协议，旨在解除真主党武装并恢复稳定。与此同时，加沙地带自 2023 年 10 月以来的冲突已造成大面积破坏和人道主义危机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.un.org/en/">United Nations | Peace, dignity and equality on a healthy planet</a></li>
<li><a href="https://en.wikipedia.org/wiki/2024_Israel–Lebanon_ceasefire_agreement">2024 Israel – Lebanon ceasefire agreement - Wikipedia</a></li>
<li><a href="https://www.aljazeera.com/news/2024/11/30/analysis-can-hezbollah-israel-ceasefire-hold">Analysis: Can the Hezbollah- Israel ceasefire hold? | Al Jazeera</a></li>

</ul>
</details>

**标签**: `#middle-east`, `#diplomacy`, `#military-risk`, `#geopolitics`

---

<a id="item-6"></a>
## [联合国：武装无人机致苏丹战争超八成平民死亡](https://news.un.org/feed/view/en/story/2026/05/1167479) ⭐️ 7.0/10

联合国人权事务高级专员指出，2026 年前四个月，武装无人机造成苏丹战争中超过 80%的平民死亡，至少 880 人遇难，并警告若无人机战争升级，冲突可能进入更致命阶段。 这一事态表明苏丹内战危险升级，人道主义后果严重，可能促使国际制裁、对武器供应方的审查以及重新施压停火的外交努力。 数据涵盖 2026 年 1 月至 4 月，无人机袭击造成的平民死亡总数至少达 880 人。联合国人权事务高级专员福尔克尔·蒂尔克特别谴责了苏丹武装部队（SAF）和快速支援部队（RSF）双方使用此类武器。

rss · UN News · May 11, 12:00

**背景**: 苏丹自 2023 年 4 月起陷入苏丹武装部队（SAF）与快速支援部队（RSF）之间的内战，导致大规模流离失所、饥荒和包括种族灭绝在内的暴行。冲突吸引了地区行为体介入，并引来了国际武器供应，阿联酋被指控向 RSF 输送武器。武装无人机在现代战争中日益普遍，其在纳卡冲突和叙利亚等冲突中的使用表明其对缺乏先进防空系统的部队具有高效性。联合国人权事务高级专员领导联合国人权高专办（OHCHR），负责监测和报告全球人权侵犯行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167479">Armed drones leading cause of civilian death in Sudan war: UN rights chief | UN News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sudan_civil_war_(2023-present)">Sudan civil war (2023-present)</a></li>
<li><a href="https://en.wikipedia.org/wiki/UN_High_Commissioner_for_Human_Rights">UN High Commissioner for Human Rights</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#diplomacy`, `#military-risk`, `#sovereign-risk`, `#africa`

---

<a id="item-7"></a>
## [欧洲央行莱恩分析能源供应冲击](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260513~5b14c78806.en.html) ⭐️ 7.0/10

欧洲央行首席经济学家菲利普·莱恩发表讲话，就能源供应冲击提供了分析视角，阐述了评估其宏观经济影响的框架。 此次讲话可能透露欧洲央行如何看待能源驱动的通胀与增长风险，从而为未来货币政策方向提供指引并影响市场预期。 尽管讲话侧重于分析工具而非即时政策行动，但强调了能源供应中断是欧洲央行风险评估中的关键变量。

rss · ECB Press Releases · May 13, 19:00

**背景**: 在欧洲地缘政治紧张局势下，能源供应冲击成为推高通胀的部分原因，欧洲央行一直应对这一问题。作为首席经济学家，菲利普·莱恩的讲话通常为欧洲央行的政策决策提供分析基础，特别是关于结构性冲击如何传导至欧元区经济。

**标签**: `#central-bank`, `#macroeconomics`, `#energy`, `#europe`, `#supply-chain`

---

<a id="item-8"></a>
## [拉加德：稳定币须分离货币与技术功能](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260508~dd909fbed1.en.html) ⭐️ 7.0/10

欧洲央行行长克里斯蒂娜·拉加德在 2026 年 5 月 8 日的演讲中指出，稳定币具有货币功能和技术功能两种不同属性，政策制定者必须将二者分开对待，并警告欧元稳定币可能威胁货币主权。 这一表态表明监管审查将加强，可能影响欧盟稳定币规则制定、加密市场走向及数字欧元设计，并凸显央行对金融稳定和货币政策主导权的重视。 拉加德特别警告，私人发行的欧元稳定币可能导致银行存款流失并削弱欧洲央行的货币政策传导机制；该演讲发表于西班牙银行拉美经济论坛。

rss · ECB Press Releases · May 8, 07:00

**背景**: 稳定币是与特定资产挂钩的加密资产，常用于加密货币交易和跨境支付。欧洲央行长期对私人数字货币持谨慎态度，并正在推进数字欧元项目，预计 2029 年具备技术能力。欧盟近期提议将加密资产监管权集中至欧洲证券和市场管理局（ESMA），这反映出对系统性风险的日益重视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp260508~dd909fbed1.en.html">Stablecoins and the future of money : separating functions from ...</a></li>
<li><a href="https://cryip.co/christine-lagarde-euro-stablecoins-ecb-digital-payment-infrastructure/">Christine Lagarde Warns Against Euro Stablecoins as ECB... | Cryip</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_euro">Digital euro - Wikipedia</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#financial-stability`, `#currency`, `#europe`, `#global-markets`

---

<a id="item-9"></a>
## [联合国欢迎美国 18 亿美元人道援助](https://news.un.org/feed/view/en/story/2026/05/1167513) ⭐️ 6.0/10

美国宣布向联合国人道主义行动追加 18 亿美元资金，用于扩大全球紧急救援。 美国大幅增加人道主义资金，凸显其对全球稳定的承诺，并可能鼓励其他国家在创纪录的全球需求下增加捐助。 公告未说明资金在不同联合国机构或危机间的分配情况，且仍需国会批准。

rss · UN News · May 14, 12:00

**背景**: 美国历来是联合国人道主义项目的最大政府捐助国，但近年来由于冲突、气候灾害和经济不稳定，全球人道主义需求激增。许多援助行动面临长期资金不足，迫使机构优先分配援助。

**标签**: `#diplomacy`, `#geopolitics`, `#united-states`

---

<a id="item-10"></a>
## [联合国斡旋协议下也门将释放 1600 名被拘留者](https://news.un.org/feed/view/en/story/2026/05/1167511) ⭐️ 6.0/10

经过数月在约旦的谈判，联合国促成了一项协议，也门各方将释放 1600 多名冲突相关被拘留者，这是自内战爆发以来规模最大的换囚行动。 这次罕见的也门外交突破为停滞的和平进程注入了信心，可能为更广泛的停火或政治谈判铺路，但对市场的直接影响有限。 这项协议是在约旦经过数月联合国主导的谈判后最终达成的，是 2014 年冲突爆发以来单次最大规模的囚犯释放；但执行情况将取决于各方持续遵守，且过去类似协议曾出现拖延。

rss · UN News · May 14, 12:00

**背景**: 也门内战始于 2014 年胡塞武装占领首都萨那，2015 年沙特领导的联军介入。联合国多次斡旋囚犯交换，以建立信任，特别是根据 2018 年《斯德哥尔摩协议》建立了被拘留者释放机制。此次协议是这一框架的重要落实，正值和平谈判长期僵局之际。

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#yemen`

---

<a id="item-11"></a>
## [联合国官员谴责俄罗斯对基辅平民的袭击](https://news.un.org/feed/view/en/story/2026/05/1167509) ⭐️ 6.0/10

联合国乌克兰人道协调员伯纳黛特·卡斯特-霍林斯沃思强烈谴责俄罗斯对基辅平民区的军事打击，称其明显违反国际人道法。 这一谴责强化了俄罗斯战争罪的叙事，可能加大外交压力和制裁讨论，并可能影响对乌克兰的进一步军事援助。 袭击发生在周四的基辅，目标是平民区。联合国官员的声明明确引用违反人道法，这可能为未来的法律或调查行动提供支持。

rss · UN News · May 14, 12:00

**背景**: 国际人道法由日内瓦公约编纂，规范武装冲突以保护平民并限制战争手段。联合国乌克兰人道协调员负责协调人道主义救援并报告违法行为。俄罗斯于 2022 年 2 月开始全面入侵乌克兰，多次被指控袭击平民。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Humanitarian_law">Humanitarian law</a></li>
<li><a href="https://en.wikipedia.org/wiki/International_humanitarian_law">International humanitarian law - Wikipedia</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#diplomacy`, `#sanctions`, `#military-risk`, `#europe`

---

<a id="item-12"></a>
## [古特雷斯呼吁改革以增强非洲全球话语权](https://news.un.org/feed/view/en/story/2026/05/1167503) ⭐️ 6.0/10

联合国秘书长安东尼奥·古特雷斯在亚的斯亚贝巴与非洲联盟会晤时警告，非洲日益增长的影响力正受到过时的全球机构和不公平借贷成本的制约，并呼吁进行紧急改革。 古特雷斯的呼吁凸显了系统性不平等问题，可能影响即将到来的国际金融架构改革辩论，并鉴于非盟已是 G20 成员，或能降低非洲主权风险溢价，改变 G20 动态。 会议期间，联合国与非盟重申了战略伙伴关系。未宣布具体改革措施，但对不公平借贷成本的关注表明将致力于解决信用评级和贷款实践中存在的风险认知偏见。

rss · UN News · May 13, 12:00

**背景**: 非洲联盟由 55 个成员国组成，于 2002 年取代非洲统一组织。国际货币基金组织和世界银行等全球金融机构长期因发展中国家代表性不足而受到批评。由于存在感知的主权风险，非洲国家往往面临更高的借贷成本，这已成为政策辩论和国际货币基金组织研究的议题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/African_Union">African Union</a></li>
<li><a href="https://en.wikipedia.org/wiki/International_financial_institutions">International financial institutions - Wikipedia</a></li>
<li><a href="https://www.imf.org/-/media/files/publications/wp/2023/english/wpiea2023130-print-pdf.pdf">Sub-Saharan Africas Risk Perception Premium: In the Search of...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#sovereign-risk`, `#africa`

---