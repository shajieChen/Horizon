---
layout: default
title: "Horizon Summary: 2026-05-28 (ZH)"
date: 2026-05-28
lang: zh
---

> From 37 items, 13 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [以色列空袭黎巴嫩升级，加沙援助仍受限](#item-2) ⭐️ 9.0/10
3. [俄罗斯使用高超音速导弹大规模袭击基辅](#item-3) ⭐️ 9.0/10
4. [欧洲央行警告：地缘经济冲击下金融稳定风险居高](#item-4) ⭐️ 9.0/10
5. [凯文·沃什宣誓就任美联储主席及 FOMC 主席](#item-5) ⭐️ 9.0/10
6. [NPT 审议会破裂，核军备竞赛恐慌加剧](#item-6) ⭐️ 8.0/10
7. [联合国特使警告：加沙若无过渡计划将陷入永久僵局](#item-7) ⭐️ 8.0/10
8. [欧央行首席莱恩受访暗示加息可能性](#item-8) ⭐️ 8.0/10
9. [欧洲央行首席经济学家莱恩谈欧洲与全球经济](#item-9) ⭐️ 8.0/10
10. [联合国秘书长警告世界秩序面临危险侵蚀](#item-10) ⭐️ 7.0/10
11. [俄军袭击摧毁第聂伯罗粮食署食品仓库](#item-11) ⭐️ 7.0/10
12. [欧央行执委施纳贝尔接受路透采访谈货币政策](#item-12) ⭐️ 7.0/10
13. [欧洲央行公布非利率货币政策措施决定](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 27, 23:01

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
| QDII Nasdaq 100 Proxy | US | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | high |
| US Mega Cap Basket | US | bullish 38/31/31 | bullish 38/31/31 | bullish 42/29/30 | high |
| Japan Equity Basket | JP | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | bullish 36/31/32 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=30057.25; 1d=-0.05%; 5d=+3.92%; 20d=+10.63% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=729.45; 1d=-0.11%; 5d=+3.98%; 20d=+10.93% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29973.57; 1d=-0.09%; 5d=+4.01%; 20d=+10.89% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=6.6%; implied_move=0.2%; put/call OI=2.855438705021136 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=60.7; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.48; 2Y=4.0; 10Y-2Y=0.4800000000000004 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |

##### Analysis

**Resonance signals**
- 已覆盖信号层：Options / Volatility, Price Trend, Risk Appetite / Macro。
- 价格趋势层与风险偏好层形成交叉验证。

**Key divergences**
- 价格方向与期权隐含波动可能出现背离，需跟踪IV变化。

**Time stratification**
- 1日：有效交易信号不足，使用保守基准分布。
- 1周：5日收益与20日均线结构支持1周偏多
- 1月：20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高

##### Probability Estimates
| Horizon | Up | Down | Neutral | Bias | Basis | Confidence |
|---|---:|---:|---:|---|---|---|
| 1日 | 33% | 33% | 34% | neutral | 有效交易信号不足，使用保守基准分布。 | high |
| 1周 | 38% | 31% | 31% | bullish | 5日收益与20日均线结构支持1周偏多 | high |
| 1月 | 42% | 29% | 30% | bullish | 20日趋势维持上行，1月窗口偏多；风险偏好仍可控且波动未失控，中期上行概率提高 | high |

##### Signals to Monitor
| Signal | Current value | Threshold | Meaning |
|---|---:|---:|---|
| NQ=F price trend | close=30057.25; 1d=-0.05%; 5d=+3.92%; 20d=+10.63% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=729.45; 1d=-0.11%; 5d=+3.98%; 20d=+10.93% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29973.57; 1d=-0.09%; 5d=+4.01%; 20d=+10.89% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| META price trend | close=635.26; 1d=+3.74%; 5d=+5.42%; 20d=-5.38% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=310.85; 1d=+0.82%; 5d=+3.97%; 20d=+14.93% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=212.60; 1d=-1.05%; 5d=-3.63%; 20d=-0.27% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=412.67; 1d=-0.81%; 5d=-0.92%; 20d=-3.65% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=388.83; 1d=-0.01%; 5d=+0.30%; 20d=+11.16% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=271.85; 1d=+2.47%; 5d=+4.82%; 20d=+4.68% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| NVDA options surface | ATM IV=3.3%; implied_move=0.1%; put/call OI=0.46432963141799455 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=6.3%; implied_move=0.3%; put/call OI=0.9887683084161797 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=5.3%; implied_move=0.3%; put/call OI=0.6755986979772146 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=9.6%; implied_move=0.3%; put/call OI=0.4381611994824568 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=5.4%; implied_move=0.2%; put/call OI=0.627850651795618 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=6.0%; implied_move=0.2%; put/call OI=0.43862287618892776 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| NVDA insider filings | recent Form4 count=562 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.48; 2Y=4.0; 10Y-2Y=0.4800000000000004 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=60.7; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| META price trend | close=635.26; 1d=+3.74%; 5d=+5.42%; 20d=-5.38% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=310.85; 1d=+0.82%; 5d=+3.97%; 20d=+14.93% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=212.60; 1d=-1.05%; 5d=-3.63%; 20d=-0.27% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 8035.T price trend | close=52500.00; 1d=+2.10%; 5d=+13.88%; 20d=+15.44% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7272.00; 1d=-7.26%; 5d=+44.31%; 20d=+24.58% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3525.00; 1d=-0.65%; 5d=-2.25%; 20d=+8.03% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=75780.00; 1d=-1.74%; 5d=+3.94%; 20d=+19.39% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.29; 1d=-0.66%; 5d=+2.22%; 20d=+5.40% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=3008.00; 1d=-0.46%; 5d=+2.24%; 20d=-3.68% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=60.7; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.48; 2Y=4.0; 10Y-2Y=0.4800000000000004 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| 8035.T price trend | close=52500.00; 1d=+2.10%; 5d=+13.88%; 20d=+15.44% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=7272.00; 1d=-7.26%; 5d=+44.31%; 20d=+24.58% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3525.00; 1d=-0.65%; 5d=-2.25%; 20d=+8.03% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| KWEB price trend | close=27.04; 1d=-0.81%; 5d=-4.38%; 20d=-3.81% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=124.30; 1d=-2.59%; 5d=-6.75%; 20d=-4.53% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=35.32; 1d=-1.20%; 5d=-2.65%; 20d=-2.57% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=28.40; 1d=-4.57%; 5d=-7.31%; 20d=-8.68% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=434.40; 1d=-1.05%; 5d=-5.57%; 20d=-8.18% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWH price trend | close=23.10; 1d=-1.03%; 5d=-2.33%; 20d=-0.73% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=60.7; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.48; 2Y=4.0; 10Y-2Y=0.4800000000000004 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| KWEB price trend | close=27.04; 1d=-0.81%; 5d=-4.38%; 20d=-3.81% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=124.30; 1d=-2.59%; 5d=-6.75%; 20d=-4.53% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=35.32; 1d=-1.20%; 5d=-2.65%; 20d=-2.57% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

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

- [MOVE Index (MOVE) - MacroMicro](https://en.macromicro.me/charts/35584/us-treasury-move-index)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：The Merrill Lynch Option Volatility Estimate (MOVE) Index reflects the level of volatility in U.S. Treasury futures. The index is considered a proxy for term premiums of U.S. Tr...

- [MOVE Index Charts and Quotes — TradingView](https://www.tradingview.com/symbols/TVC-MOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：MOVE INDEX Setup for Top in World stock markets The chart is the Move index it is reaching an area which I consider High level of Complacency I say this as of this writing The 1...

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

- [Cboe Nasdaq-100 Implied Volatil (^CNIV05) - Yahoo Finance](https://finance.yahoo.com/quote/%5ECNIV05/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Find the latest information on Cboe Nasdaq-100 Implied Volatil (^CNIV05) including data, charts, related news and more from Yahoo Finance

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
  - 摘要：U.S. High Yield Bond Spread: 3.05% as of May 21, 2026. Units: Percent Frequency: Daily, Close Release: ICE BofA Indices Source: Ice Data Indices, LLC

- [QQQ Options Chain — Open Interest, Implied Volatility, Max Pain & Gamma ...](https://whalequant.io/en/stocks/QQQ/options-analytics)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Explore the live QQQ options chain with strikes, open interest, volume, implied volatility (IV), max pain levels, gamma exposure, dealer positioning and options flow analysis. P...

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [QQQ Stock Volatility History & Chart Since 1999](https://wallstreetnumbers.com/etfs/qqq/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Get all-time historical data of QQQ historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Live US Dollar to Yens Exchange Rate - $ 1 USD/JPY Today](https://usd.currencyrate.today/jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest and best $1 US Dollar to Yens rate for FREE. USD/JPY - Live exchange rates, banks, historical data & currency charts.

- [USD/JPY (USDJPY=X) Live Rate, Chart & News - Yahoo Finance](https://finance.yahoo.com/quote/USDJPY=X/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Find the latest USD/JPY (USDJPY=X) currency exchange rate, plus historical data, charts, relevant news and more

- [USD JPY / US Dollar to Yen Live Rate - Investing.com](https://www.investing.com/currencies/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get real time data on the USD/JPY pair including the live rate, as well as our currency converter, analysis, news, historical data and more.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

- [Index Information - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index/profile?idx=nk225vi)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：The Nikkei Stock Average Volatility Index are calculated by using prices of Nikkei 225 futures and Nikkei 225 options on the Osaka Exchange (OSE). In the calculation, taking nea...

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
## [以色列空袭黎巴嫩升级，加沙援助仍受限](https://news.un.org/feed/view/en/story/2026/05/1167590) ⭐️ 9.0/10

联合国周二报告，以色列夜间对黎巴嫩的空袭升级，迫使居民再次逃离家园，同时加沙地带的人道主义援助准入仍受到严格限制。 事态升级增加了地区冲突扩大的风险，可能引发真主党报复，破坏外交努力并扰乱能源市场，同时加深加沙的人道主义灾难。 联合国未提供具体伤亡数字或袭击地点，但指出民众反复流离失所表明当地持续不稳。加沙的援助限制在国际压力下仍在持续，且未明确放宽时间表。

rss · UN News · May 26, 12:00

**背景**: 自 2023 年 10 月哈马斯袭击及随后的战争以来，以色列-黎巴嫩边境频繁发生交火，真主党与以军冲突不断。以色列对真主党目标实施间歇性空袭，同时外交渠道试图避免全面战争。在加沙，自冲突开始以来，以色列一直维持严格封锁和援助控制，导致粮食、药品和燃料严重短缺。

**标签**: `#middle-east`, `#military-risk`, `#geopolitics`, `#energy`, `#diplomacy`

---

<a id="item-3"></a>
## [俄罗斯使用高超音速导弹大规模袭击基辅](https://news.un.org/feed/view/en/story/2026/05/1167583) ⭐️ 9.0/10

俄罗斯对基辅发动大规模夜间导弹和无人机袭击，发射约 90 枚导弹（包括一枚高超音速弹道导弹）和 60 架无人机，引发联合国呼吁停止伤害平民。 此次升级表明俄罗斯仍愿意使用先进武器打击乌克兰城市，导致平民伤亡和基础设施破坏风险上升，可能扰乱能源市场并加剧国际制裁讨论。 据报道，此次袭击使用了飞行速度超过 5 马赫的高超音速弹道导弹，难以拦截；联合国安理会当时正在讨论冲突中的平民保护问题。

rss · UN News · May 24, 12:00

**背景**: 俄乌战争中已多次发生袭击平民区事件。高超音速武器具有高机动性和超过 5 马赫的速度，使防空系统难以应对。联合国定期监测平民伤害并呼吁遵守国际人道法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hypersonic_weapon">Hypersonic weapon - Wikipedia</a></li>
<li><a href="https://news.un.org/en/story/2026/05/1167554">Security Council LIVE: Civilians in conflict under spotlight ...</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#military-risk`, `#diplomacy`, `#geopolitics`, `#energy`

---

<a id="item-4"></a>
## [欧洲央行警告：地缘经济冲击下金融稳定风险居高](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260527~92140c5054.en.html) ⭐️ 9.0/10

2026 年 5 月 27 日，欧洲央行发布新闻稿称，由于地缘经济冲击持续发展，金融稳定脆弱性依然高企，地缘经济趋势和关税影响的不确定性给欧元区金融体系带来风险。 这一警告预示着欧元区可能面临系统性风险，可能影响银行信贷、主权债券息差和市场信心，或促使欧洲央行和其他监管机构采取政策应对措施。 欧洲央行指出，尽管银行保持健康的偿付能力和流动性缓冲，但非银行金融部门的脆弱性显著，且因地缘政治紧张局势和贸易政策不确定性而加剧。该新闻稿是欧洲央行最新《金融稳定评估报告》的一部分。

rss · ECB Press Releases · May 27, 08:00

**背景**: 地缘经济学指的是利用经济工具实现地缘政治目标，包括关税和制裁。欧洲央行定期发布《金融稳定评估报告》，以评估欧元区金融体系面临的风险。欧元区过去曾面临系统性风险，尤其是在主权债务危机期间，高度的互联性导致了传染效应。当前的贸易争端等地缘经济冲击可能扰乱全球市场和金融稳定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/press/financial-stability-publications/fsr/html/index.en.html">Financial Stability Review | European Central Bank</a></li>
<li><a href="https://siepr.stanford.edu/news/power-geoeconomics-make-sense-turbulent-world">The power of ‘geoeconomics’ to make sense of a turbulent ...</a></li>
<li><a href="https://eaccny.com/news/chapternews/ecb-financial-stability-in-uncertain-times/">ECB | Financial stability in uncertain times | European American...</a></li>

</ul>
</details>

**标签**: `#financial-stability`, `#central-bank`, `#geopolitics`, `#europe`, `#macroeconomics`

---

<a id="item-5"></a>
## [凯文·沃什宣誓就任美联储主席及 FOMC 主席](https://www.federalreserve.gov/newsevents/pressreleases/other20260522a.htm) ⭐️ 9.0/10

2026 年 5 月 22 日，凯文·沃什宣誓就任美联储理事会主席及理事，联邦公开市场委员会一致推选他为委员会主席。 这一领导层变动可能导致货币政策转向更鹰派或更市场化的方向，可能影响利率决策、金融监管和全球市场稳定。 联邦公开市场委员会一致投票表明对沃什的广泛支持，他曾在 2006 年至 2011 年担任美联储理事，并以对长期宽松货币政策持怀疑态度而闻名。

rss · Federal Reserve Press Releases · May 22, 20:15

**背景**: 美联储系统由七名成员组成的理事会领导，主席任期四年。联邦公开市场委员会由理事会成员和地区联储主席组成，负责制定货币政策。凯文·沃什曾担任经济顾问和美联储理事，接替任期于 2026 年结束的杰罗姆·鲍威尔。沃什过去曾直言批评量化宽松政策，可能推行更严格的监管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chair_of_the_Federal_Reserve">Chair of the Federal Reserve - Wikipedia</a></li>
<li><a href="https://www.federalreserve.gov/aboutthefed/bios/board/default.htm">Federal Reserve Board - Board Members</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#global-markets`, `#united-states`, `#monetary-policy`, `#macroeconomics`

---

<a id="item-6"></a>
## [NPT 审议会破裂，核军备竞赛恐慌加剧](https://news.un.org/feed/view/en/story/2026/05/1167580) ⭐️ 8.0/10

第十一届《不扩散核武器条约》审议大会在纽约联合国总部进行了四周谈判后，于周五结束，未能就最终宣言达成共识。 这次失败动摇了全球核不扩散机制，加剧了大国间新一轮军备竞赛的风险，并可能影响国防开支和市场风险认知。 这是继 2022 年陷入僵局后，NPT 审议大会连续第二次未能达成共识，凸显核武国家与无核武国家之间在裁军进展上的深刻分歧。

rss · UN News · May 23, 12:00

**背景**: 《不扩散核武器条约》于 1970 年生效，拥有 191 个缔约国，是全球核治理的基石，建立在防扩散、裁军及和平利用核能三大支柱之上。审议大会每五年举行一次以评估条约执行情况。2015 年和 2022 年的审议大会也未能达成共识，反映出围绕核裁军步伐的紧张局势不断加剧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nuclear_Non-Proliferation_Treaty">Nuclear Non-Proliferation Treaty</a></li>
<li><a href="https://en.wikipedia.org/wiki/2010_NPT_Review_Conference">2010 NPT Review Conference</a></li>
<li><a href="https://capssindia.org/the-role-of-the-npt-in-preserving-nuclear-dynamics-during-a-power-transition/">Why the 11th NPT Review Conference Matters in 2026</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#global-markets`

---

<a id="item-7"></a>
## [联合国特使警告：加沙若无过渡计划将陷入永久僵局](https://news.un.org/feed/view/en/story/2026/05/1167568) ⭐️ 8.0/10

一位联合国高级特使向安理会警告，由于停火协议执行乏力且人道状况恶化，加沙过渡计划的拖延可能导致该地区陷入永久僵局。 这一警告表明加沙冲突重燃的风险加剧，人道危机加深，可能对地区稳定及全球能源市场产生溢出效应。 安理会支持的过渡计划面临治理和解除武装等未决挑战，而停火协议的多阶段结构仍停留在早期阶段，进展停滞。

rss · UN News · May 21, 12:00

**背景**: 2025 年 1 月达成的加沙停火协议包含多个阶段，包括释放人质和以色列撤军。联合国安理会支持一项旨在恢复加沙治理和重建的过渡计划，提案包括由英国前首相布莱尔提出的加沙国际过渡管理局，以及美国前总统特朗普提出的包含‘和平委员会’的全面计划。但因解除武装和治理争议，进展受阻。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaza_International_Transitional_Authority">Gaza International Transitional Authority - Wikipedia</a></li>
<li><a href="https://www.whitehouse.gov/briefings-statements/2026/01/statement-on-president-trumps-comprehensive-plan-to-end-the-gaza-conflict/">Statement on President Trump’s Comprehensive Plan to End the Gaza ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/January_2025_Gaza_war_ceasefire">January 2025 Gaza war ceasefire - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`, `#military-risk`

---

<a id="item-8"></a>
## [欧央行首席莱恩受访暗示加息可能性](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260526_1~71caa51b14.en.html) ⭐️ 8.0/10

欧洲央行首席经济学家菲利普·莱恩在接受日经采访时讨论了经济前景和货币政策，暗示央行可能因持续的通胀压力而加息。 莱恩的言论因其对欧洲央行政策的前瞻指引而备受关注，可能影响欧元区债券收益率、欧元汇率和全球金融市场。 市场已经预计欧洲央行将在 6 月会议上加息，多数交易员预期年底前至少加息 50 个基点。莱恩的讲话可能加强或缓和这些预期。

rss · ECB Press Releases · May 26, 10:00

**背景**: 欧洲中央银行（ECB）是欧元区的中央银行，负责维持价格稳定，通胀目标为 2%。欧洲央行管理委员会设定关键利率以引导经济。作为首席经济学家，菲利普·莱恩在制定欧洲央行的货币政策分析和沟通方面发挥关键作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/05/26/ecb-villeroy-inflation-iran-war.html">ECB 'will do what is necessary' to tame inflation, Bank of France governor tells CNBC</a></li>
<li><a href="https://www.ecb.europa.eu/mopo/html/index.en.html">Overview of monetary policy and markets</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#bonds`, `#currencies`

---

<a id="item-9"></a>
## [欧洲央行首席经济学家莱恩谈欧洲与全球经济](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260522~f0f11a5f05.en.html) ⭐️ 8.0/10

欧洲央行首席经济学家菲利普·莱恩发表题为‘欧洲与世界经济’的演讲，可能在全球不确定性中释放货币政策信号。 其言论可能影响欧元区利率预期、欧元汇率及债券市场，并透露欧洲央行对通胀、增长和外部风险的看法。 演讲无具体政策公告，但若侧重全球逆风或内部韧性，可能左右市场定价。

rss · ECB Press Releases · May 22, 01:15

**背景**: 菲利普·莱恩是爱尔兰经济学家，自 2019 年起担任欧洲央行首席经济学家，为政策讨论注入学术严谨性。欧洲央行为 20 国欧元区制定货币政策，以物价稳定为目标。此次演讲正值全球贸易格局变化和通胀动态演变之际，这些因素对欧洲央行的利率决策至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Philip_R._Lane">Philip R. Lane</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>
<li><a href="https://www.ecb.europa.eu/">European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#global-markets`, `#currency`

---

<a id="item-10"></a>
## [联合国秘书长警告世界秩序面临危险侵蚀](https://news.un.org/feed/view/en/story/2026/05/1167589) ⭐️ 7.0/10

联合国秘书长古特雷斯在安理会警告称，战争、军备竞赛和地缘政治分裂正危险地侵蚀二战后建立的的多边体系和世界秩序。他表示，《联合国宪章》正面临数十年来最严峻的考验。 这一高级别警告表明地缘政治不确定性升高，全球合作可能进一步分裂，从而影响国际市场和外交稳定。它凸显了多边框架若被削弱，可能无法有效应对危机的风险。 安理会召开了关于加强以联合国为中心的国际体系的高级别辩论，重点包括捍卫《联合国宪章》、改革全球治理以及恢复对安理会危机应对能力的信心。此次辩论表明机构担忧及可能的后续行动。

rss · UN News · May 26, 12:00

**背景**: 《联合国宪章》于 1945 年签署，是联合国的根本性条约，旨在维护国际和平与安全。安理会是主要负责此项任务的联合国机构，有权实施制裁或授权军事行动。多边主义指多国为追求共同目标而进行的合作。近几十年来，单边军事干预、贸易争端及退出国际协议等挑战给这一体系带来压力。古特雷斯的警告反映了持续冲突和大国竞争累积的压力。

**标签**: `#diplomacy`, `#geopolitics`, `#united-nations`, `#global-markets`

---

<a id="item-11"></a>
## [俄军袭击摧毁第聂伯罗粮食署食品仓库](https://news.un.org/feed/view/en/story/2026/05/1167586) ⭐️ 7.0/10

俄罗斯对乌克兰第聂伯罗市的一个世界粮食计划署仓库发动袭击，摧毁了原本将运往前线地区的大批粮食援助。 此次袭击加剧了冲突的人道主义影响，直接威胁到脆弱群体的粮食安全，可能引发国际谴责、干扰联合国行动并左右援助态势。 世界粮食计划署谴责了此次袭击，强调被毁粮食原计划运往数千名前线地区民众，且损失 "相当大"。

rss · UN News · May 26, 12:00

**背景**: 世界粮食计划署是联合国的粮食援助机构，也是全球最大的人道主义组织，曾因在冲突地区抗击饥饿获 2020 年诺贝尔和平奖。第聂伯罗是乌克兰东部重要工业城市，是向受战争影响的前线社区分发援助的关键枢纽。俄乌冲突严重破坏了粮食供应链，数百万人依赖人道主义援助。根据国际人道法，蓄意袭击救援行动可能构成战争罪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_Food_Programme">World Food Programme</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dnipro">Dnipro - Wikipedia</a></li>

</ul>
</details>

**标签**: `#russia-ukraine`, `#diplomacy`, `#geopolitics`, `#military-risk`, `#supply-chain`

---

<a id="item-12"></a>
## [欧央行执委施纳贝尔接受路透采访谈货币政策](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260526~6736a05aaa.en.html) ⭐️ 7.0/10

欧洲央行执行委员会委员伊莎贝尔·施纳贝尔在接受路透社采访时讨论了经济前景和货币政策立场，提供了可能影响市场对利率和通胀预期的见解。 她的讲话被密切关注，以寻找未来利率走向的早期信号，可能对欧元区债券收益率、外汇市场和更广泛的金融状况产生影响。 作为关键决策者，施纳贝尔的评论常暗示欧洲央行对通胀持续性、增长风险或资产负债表缩减的看法，但新闻摘要中未透露具体政策指引。

rss · ECB Press Releases · May 26, 06:00

**背景**: 伊莎贝尔·施纳贝尔是欧洲央行执行委员会成员，负责实施欧元区货币政策。她以分析性方法著称，此前曾就绿色货币政策和量化宽松等话题发表讲话。执委会成员的公开声明可能影响市场，因为投资者会仔细解读以寻找政策线索。

**标签**: `#central-bank`, `#europe`, `#macroeconomics`, `#currency`, `#bonds`

---

<a id="item-13"></a>
## [欧洲央行公布非利率货币政策措施决定](https://www.ecb.europa.eu//press/govcdec/otherdec/2026/html/ecb.gc260522~a4812a8f23.en.html) ⭐️ 7.0/10

2026 年 5 月 22 日，欧洲央行管理委员会公布了除利率设定外的货币政策措施决定，可能涉及资产购买计划、定向贷款操作或抵押品框架的调整。 这些措施直接影响欧元流动性状况、银行融资成本和主权债券收益率，从而影响欧元区的货币政策传导和金融稳定。 公告中未提供具体操作细节，但此类决定通常是欧洲央行常规非标准货币政策工具的一部分，旨在通过利率调整之外的手段引导金融状况。

rss · ECB Press Releases · May 22, 13:00

**背景**: 欧洲央行运用常规利率政策以及非标准措施（如量化宽松（APP/PEPP）、定向长期再融资操作（TLTROs）和抵押品宽松）来实现物价稳定任务。非标准措施在 2008 年金融危机后变得突出，并在欧元区债务危机和疫情期间被大量使用。管理委员会定期发布这些工具的决定，以确保透明度并引导市场预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ecb.europa.eu/mopo/decisions/html/index.en.html">Decisions, statements & accounts - European Central Bank</a></li>
<li><a href="https://publications.banque-france.fr/sites/default/files/medias/documents/economics_in_brief_non_stantard_or_unconventional_monetary_policy.pdf">Non-standard or unconventional monetary policy - Banque de France</a></li>
<li><a href="https://www.ecb.europa.eu/ecb-and-you/explainers/tell-me-more/html/excess_liquidity.en.html">What is excess liquidity ? | European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#bonds`, `#currency`, `#europe`

---