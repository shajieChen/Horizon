---
layout: default
title: "Horizon Summary: 2026-05-16 (ZH)"
date: 2026-05-16
lang: zh
---

> From 43 items, 12 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [美联储任命鲍威尔为临时主席，直至沃什宣誓就职](#item-2) ⭐️ 9.0/10
3. [全球能源与贸易中断致数百万人走向贫困](#item-3) ⭐️ 8.0/10
4. [安理会就叙利亚过渡及人道危机召开会议](#item-4) ⭐️ 7.0/10
5. [联合国警告索马里濒临饥荒，中东战火加剧危机](#item-5) ⭐️ 7.0/10
6. [古特雷斯呼吁改革提升非洲全球话语权](#item-6) ⭐️ 7.0/10
7. [联黎部队警告无人机事件威胁维和人员安全](#item-7) ⭐️ 7.0/10
8. [拉加德呼吁建设持久的欧洲](#item-8) ⭐️ 7.0/10
9. [欧洲央行首席经济学家分析能源供应冲击](#item-9) ⭐️ 7.0/10
10. [欧洲央行副行长谈货币政策与经济展望](#item-10) ⭐️ 7.0/10
11. [联合国救援车辆在乌克兰赫尔松遭两次袭击](#item-11) ⭐️ 6.0/10
12. [联合国斡旋也门换俘，1600 名被拘留者将获释](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 15, 22:59

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
| QDII Nasdaq 100 Proxy | US | neutral 33/33/34 | neutral 33/33/34 | bullish 42/29/30 | high |
| US Mega Cap Basket | US | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | high |
| Japan Equity Basket | JP | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | neutral 33/33/34 | bullish 36/31/32 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=29173.00; 1d=-1.73%; 5d=-0.54%; 20d=+8.75% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29125.20; 1d=-1.54%; 5d=-0.38%; 20d=+9.20% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=708.93; 1d=-1.51%; 5d=-0.32%; 20d=+9.26% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=10.9%; implied_move=0.3%; put/call OI=1.9739360780333226 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=62.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.59; 2Y=4.09; 10Y-2Y=0.5 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| NQ=F price trend | close=29173.00; 1d=-1.73%; 5d=-0.54%; 20d=+8.75% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29125.20; 1d=-1.54%; 5d=-0.38%; 20d=+9.20% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=708.93; 1d=-1.51%; 5d=-0.32%; 20d=+9.26% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/neutral/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| AAPL price trend | close=300.23; 1d=+0.68%; 5d=+2.45%; 20d=+11.20% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=614.23; 1d=-0.68%; 5d=+0.75%; 20d=-10.79% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=264.14; 1d=-1.15%; 5d=-3.13%; 20d=+5.42% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=225.32; 1d=-4.42%; 5d=+4.70%; 20d=+11.72% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=396.78; 1d=-1.07%; 5d=-1.00%; 20d=+16.13% | 价格趋势与均线位置用于判断短中期方向概率。 |
| TSLA price trend | close=422.24; 1d=-4.75%; 5d=-1.43%; 20d=+5.40% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| META options surface | ATM IV=6.7%; implied_move=0.2%; put/call OI=0.4452908567417742 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=13.5%; implied_move=0.5%; put/call OI=0.8904641301774299 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=7.0%; implied_move=0.2%; put/call OI=0.8686297133890248 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=9.9%; implied_move=0.4%; put/call OI=0.6396633986669097 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=6.9%; implied_move=0.3%; put/call OI=0.9348965912769039 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=5.7%; implied_move=0.2%; put/call OI=0.7818781356639317 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: US high yield OAS current | US high yield OAS current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.59; 2Y=4.09; 10Y-2Y=0.5 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=62.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| MSFT insider filings | recent Form4 count=730 | 内部人交易节奏可作为估值温度辅助校验信号。 |

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
| AAPL price trend | close=300.23; 1d=+0.68%; 5d=+2.45%; 20d=+11.20% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=614.23; 1d=-0.68%; 5d=+0.75%; 20d=-10.79% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=264.14; 1d=-1.15%; 5d=-3.13%; 20d=+5.42% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 9984.T price trend | close=5745.00; 1d=-0.43%; 5d=-6.30%; 20d=+52.63% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3576.00; 1d=+3.83%; 5d=+14.84%; 20d=+10.00% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=91.07; 1d=-1.08%; 5d=-1.25%; 20d=+0.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=77180.00; 1d=-0.17%; 5d=-8.30%; 20d=+21.51% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=3085.00; 1d=+2.56%; 5d=+5.90%; 20d=-7.05% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=50290.00; 1d=-1.78%; 5d=-4.12%; 20d=+18.44% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.59; 2Y=4.09; 10Y-2Y=0.5 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=62.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
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
| 9984.T price trend | close=5745.00; 1d=-0.43%; 5d=-6.30%; 20d=+52.63% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3576.00; 1d=+3.83%; 5d=+14.84%; 20d=+10.00% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=91.07; 1d=-1.08%; 5d=-1.25%; 20d=+0.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 0700.HK price trend | close=456.40; 1d=+0.33%; 5d=-2.05%; 20d=-10.69% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=82.70; 1d=-3.50%; 5d=-1.61%; 20d=-6.82% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=30.70; 1d=-3.22%; 5d=-3.09%; 20d=-4.24% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=28.17; 1d=-3.53%; 5d=-4.67%; 20d=-7.49% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=132.30; 1d=-4.06%; 5d=-4.82%; 20d=-2.58% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=36.20; 1d=-2.79%; 5d=-2.79%; 20d=-3.72% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=62.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.59; 2Y=4.09; 10Y-2Y=0.5 | 利率曲线决定权益估值贴现与风险偏好上限。 |
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
| 0700.HK price trend | close=456.40; 1d=+0.33%; 5d=-2.05%; 20d=-10.69% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=82.70; 1d=-3.50%; 5d=-1.61%; 20d=-6.82% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=30.70; 1d=-3.22%; 5d=-3.09%; 20d=-4.24% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

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

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [ICE BofAML MOVE Index (^MOVE) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EMOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Find the latest information on ICE BofAML MOVE Index (^MOVE) including data, charts, related news and more from Yahoo Finance

- [MOVE Index Charts and Quotes — TradingView](https://www.tradingview.com/symbols/TVC-MOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：MOVE INDEX Setup for Top in World stock markets The chart is the Move index it is reaching an area which I consider High level of Complacency I say this as of this writing The 1...

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [$NDX: NASDAQ 100 Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/$NDX/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on the y-axis, making it...

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days or more out. IV is a forward looking prediction of the likelihood...

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [US High Yield Master II Option-Adjusted Spread (Market Dail…](https://ycharts.com/indicators/us_high_yield_master_ii_optionadjusted_spread)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：View market daily updates and historical trends for US High Yield Master II Option-Adjusted Spread. from United States. Source: Bank of America Merrill Ly…

- [ICE BofA US High Yield (MERH0A0) - Investing.com](https://www.investing.com/indices/ice-bofa-us-high-yield)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：Get detailed information on the ICE BofA US High Yield including charts, technical analysis, components and more.

- [QQQ: Invesco QQQ Trust Option Overview / OptionCharts](https://optioncharts.io/options/QQQ)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View comprehensive QQQ options with our latest charts on volume, open interest, max pain, and implied volatility.

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [USD JPY / US Dollar to Yen Live Rate - Investing.com](https://www.investing.com/currencies/usd-jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get real time data on the USD/JPY pair including the live rate, as well as our currency converter, analysis, news, historical data and more.

- [1 USD to JPY - US Dollars to Japanese Yen Exchange Rate - Xe](https://www.xe.com/en/currencyconverter/convert/?Amount=1&From=USD&To=JPY)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest 1 US Dollar to Japanese Yen rate for FREE with the original Universal Currency Converter. Set rate alerts for USD to JPY and learn more about US Dollars and Japan...

- [Live US Dollar to Yens Exchange Rate - $ 1 USD/JPY Today](https://usd.currencyrate.today/jpy)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：USD JPY exchange rate current
  - 摘要：Get the latest and best $1 US Dollar to Yens rate for FREE. USD/JPY - Live exchange rates, banks, historical data & currency charts.

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://ca.finance.yahoo.com/quote/EWJ/)
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
  - 摘要：The iShares MSCI Japan ETF seeks to track the investment results of an index composed of Japanese equities.

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
## [美联储任命鲍威尔为临时主席，直至沃什宣誓就职](https://www.federalreserve.gov/newsevents/pressreleases/other20260515a.htm) ⭐️ 9.0/10

2026 年 5 月 15 日，美联储理事会任命杰罗姆·鲍威尔为临时主席，直至凯文·沃什宣誓就任新主席。此前，参议院于 5 月 13 日确认了对沃什的任命。 这次领导层交接可能改变货币政策方向，因为沃什可能在利率和监管方面持不同观点，进而影响债券收益率、股市和美元。 鲍威尔的主席任期已结束，沃什尚未宣誓就职，因此需要临时任命以确保治理连续性。沃什由特朗普总统于 2026 年 1 月提名，并于 5 月 13 日获参议院确认。

rss · Federal Reserve Press Releases · May 15, 21:00

**背景**: 美联储主席领导货币政策和银行监管。凯文·沃什曾任美联储理事，是知名保守派经济学家，其 2026 年 1 月的提名预示着可能的政策转向。任命临时主席是为了在过渡期维持理事会运作，这在美联储历史上时有发生。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.federalreserve.gov/newsevents/pressreleases/other20260515a.htm">Federal Reserve Board - Federal Reserve Board names Jerome H. Powell as chair pro tempore; Powell will serve as chair pro tempore until Kevin M. Warsh is sworn in as the new chair</a></li>
<li><a href="https://apnews.com/article/fed-warsh-senate-confirmation-b665712fa5d40d3fcea53d80d0a79c64">Senate confirms Kevin Warsh as Federal Reserve chairman | AP News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chair_of_the_Federal_Reserve">Chair of the Federal Reserve - Wikipedia</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#united-states`, `#bonds`, `#equities`, `#macroeconomics`

---

<a id="item-3"></a>
## [全球能源与贸易中断致数百万人走向贫困](https://news.un.org/feed/view/en/story/2026/05/1167526) ⭐️ 8.0/10

联合国报告称，全球能源供应和贸易走廊中断正推高食品、交通和基本商品成本，减缓经济增长，威胁弱势群体和债务沉重的发展中国家。 成本上升和增长放缓可能引发主权违约，加深贫困，动摇脆弱经济体，对全球市场和国际安全产生溢出效应。 联合国报告强调了对大宗商品价格和主权债务的连锁效应，但未具体说明受影响的国家或贸易路线，凸显了关注政策应对的必要性。

rss · UN News · May 15, 12:00

**背景**: 主权信用风险指政府可能债务违约的风险，外部冲击会加剧这一风险。近期能源供应中断，如伊朗战争等，导致油气价格创纪录飙升。贸易走廊不稳定，包括红海紧张局势和对俄制裁，已改变航运路线并增加成本。债务负担沉重的发展中国家尤其容易受到此类叠加危机的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_credit_risk">Sovereign credit risk - Wikipedia</a></li>
<li><a href="https://news.un.org/en/story/2026/05/1167526">Global energy and trade disruption pushing millions towards ...</a></li>
<li><a href="https://moderndiplomacy.eu/2026/04/22/iran-war-triggers-record-energy-shock-as-global-supply-disruption-surpasses-historic-crises/">Iran War Triggers Record Energy Shock as Global Supply ...</a></li>

</ul>
</details>

**标签**: `#energy`, `#supply-chain`, `#macroeconomics`, `#sovereign-risk`, `#global-markets`

---

<a id="item-4"></a>
## [安理会就叙利亚过渡及人道危机召开会议](https://news.un.org/feed/view/en/story/2026/05/1167518) ⭐️ 7.0/10

联合国安理会召开会议讨论叙利亚脆弱的政治过渡和人道主义危机，副特使克劳迪奥·科尔多内和联合国救济事务负责人汤姆·弗莱彻进行简报。 此次会议可能就援助、制裁（近期已解除）和外交接触等政策释放信号，影响叙利亚重建和地区稳定。 会议进行现场直播，此时正值阿萨德政权于 2024 年 12 月倒台后，美欧于 2025 年解除对叙利亚的大部分制裁。

rss · UN News · May 15, 12:00

**背景**: 叙利亚内战始于 2011 年，导致严厉国际制裁。阿萨德政权于 2024 年 12 月垮台，开启了脆弱的政治过渡。美国和欧盟于 2025 年解除了大部分制裁，旨在支持重建。联合国安理会定期开会监测局势，协调国际支持并解决人道主义需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sanctions_on_Syria">Sanctions on Syria</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#middle-east`

---

<a id="item-5"></a>
## [联合国警告索马里濒临饥荒，中东战火加剧危机](https://news.un.org/feed/view/en/story/2026/05/1167516) ⭐️ 7.0/10

周五，联合国援助团队警告称，索马里有 600 万人面临饥荒风险，其中近 200 万儿童面临患病或死亡的高风险，中东战争正加剧这场危机。 这一警告凸显了中东冲突对脆弱地区的严重人道主义影响，可能需要大规模援助动员，并可能引发地区不稳定，促使国际外交介入。 综合粮食安全阶段分类（IPC）将饥荒定义为第 5 级并有具体阈值；索马里目前处于“真实风险”但尚未被正式宣布为饥荒，幼儿受影响尤为严重。

rss · UN News · May 15, 12:00

**背景**: 索马里历史上曾多次发生粮食危机，包括 2011 年导致 26 万人死亡的饥荒。当前危机因中东战争而加剧，该战争扰乱了全球食品供应链，推高了航运和化肥成本，导致全球食品价格上涨。索马里一半以上的谷物依赖进口，极易受到此类冲击。世界粮食计划署（WFP）和联合国人道主义事务协调办公室（OCHA）等联合国机构正在协调救援工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Integrated_Food_Security_Phase_Classification">Integrated Food Security Phase Classification - Wikipedia</a></li>
<li><a href="https://www.wfp.org/stories/why-middle-east-conflict-threatens-record-levels-hunger">Why the Middle East conflict threatens record levels of hunger | World Food Programme</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#sovereign-risk`, `#middle-east`

---

<a id="item-6"></a>
## [古特雷斯呼吁改革提升非洲全球话语权](https://news.un.org/feed/view/en/story/2026/05/1167503) ⭐️ 7.0/10

在亚的斯亚贝巴举行的第十次联合国-非盟高级别对话上，联合国秘书长安东尼奥·古特雷斯警告称，过时的全球机构和不公平的借贷成本制约了非洲日益增长的影响力，并呼吁进行改革以赋予非洲更强大的发言权。 这一高级别外交推动可能影响即将举行的 G20、IMF 和世界银行关于国际金融架构改革和主权债务重组的讨论，从而可能降低非洲国家的借贷成本并改变全球治理格局。 联合国开发计划署估计，有偏见的信用评级每年给非洲带来高达 460 亿美元的额外借贷成本，16 个国家的偿债额超出合理水平。联合国-非盟伙伴关系的再次确认建立在 2017 年和平与安全框架之上。

rss · UN News · May 13, 12:00

**背景**: 联合国安理会缺少常任非洲成员国，这是二战后权力结构的遗留问题，非洲国家长期要求改革。西方主导的信用评级机构经常给非洲主权国家较低的评级，造成“非洲风险溢价”。2017 年非盟-联合国联合框架加强了和平、安全与发展合作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/05/1167503">In Addis Ababa, Guterres urges reforms to give Africa ...</a></li>
<li><a href="https://www.undp.org/africa/publications/lowering-cost-borrowing-africa-role-sovereign-credit-ratings">LOWERING THE COST OF BORROWING IN AFRICA - The Role of Sovereign Credit Ratings | United Nations Development Programme</a></li>
<li><a href="https://www.csis.org/analysis/africas-design-reformed-un-security-council">Africa’s Design for a Reformed UN Security Council - CSIS</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#sovereign-risk`, `#financial-stability`, `#africa`

---

<a id="item-7"></a>
## [联黎部队警告无人机事件威胁维和人员安全](https://news.un.org/feed/view/en/story/2026/05/1167496) ⭐️ 7.0/10

联合国驻黎巴嫩临时部队（联黎部队）警告，不断增加的无人机事件及附近爆炸，涉及疑似真主党无人机和以色列军队，正危及维和人员安全并破坏黎巴嫩南部的稳定。 这一升级凸显了联合国第 1701 号决议下黎巴嫩停火的脆弱性，增加了以色列与真主党直接冲突的风险，并危及联合国维和人员安全，可能引发外交干预并进一步破坏地区稳定。 真主党新型光纤无人机可规避雷达和干扰，正在考验以色列的防御系统，而联黎部队在黎巴嫩南部的授权已进入最后阶段，至 2026 年 12 月到期，随后在 2027 年逐步撤出。

rss · UN News · May 13, 12:00

**背景**: 联黎部队于 1978 年成立，旨在确认以色列撤军并恢复和平。2006 年战争后，根据联合国第 1701 号决议，其授权扩展至监督停止敌对行动，并协助黎巴嫩军队确保利塔尼河以南地区没有未经授权的武装团体。伊朗支持的真主党近年来大幅提升了无人机能力，给以色列防空系统和维和任务带来新挑战。2024 年冲突后的停火依然脆弱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://peacekeeping.un.org/en/mission/unifil">UNIFIL | UN Peacekeeping - the United Nations</a></li>
<li><a href="https://apnews.com/article/israel-hezbollah-ceasefire-united-nations-resolution-1701-86e3668220e8dbdb390bc803004e9660">UN Resolution 1701 is at the heart of the Israel-Hezbollah... | AP News</a></li>
<li><a href="https://www.aljazeera.com/news/2026/4/29/how-hezbollahs-fibre-optic-drones-test-israels-sophisticated-radar-system">How Hezbollah's fibre optic drones test Israel's sophisticated radar ...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#middle-east`, `#united-nations`

---

<a id="item-8"></a>
## [拉加德呼吁建设持久的欧洲](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260513_1~ab5ae9e754.en.html) ⭐️ 7.0/10

欧洲央行行长克里斯蒂娜·拉加德于 2026 年 5 月 13 日发表演讲，呼吁深化欧洲一体化并增强韧性，强调建设持久欧洲所需的勇气。 该演讲暗示欧洲央行可能支持财政或政治联盟，这或影响欧元区政治凝聚力预期及主权债务市场。 演讲题为《建设持久欧洲的勇气》，发布于欧洲央行官网，但未提出具体政策建议或后续行动。

rss · ECB Press Releases · May 13, 19:50

**背景**: 欧洲央行历来倡导加强欧元区财政一体化，以补充其货币政策。拉加德曾任国际货币基金组织总裁，经常强调多边主义。此次演讲可能基于欧盟在新冠疫情和能源危机后关于韧性的近期讨论。

**标签**: `#central-bank`, `#europe`, `#sovereign-risk`, `#diplomacy`, `#financial-stability`

---

<a id="item-9"></a>
## [欧洲央行首席经济学家分析能源供应冲击](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260513~5b14c78806.en.html) ⭐️ 7.0/10

欧洲央行首席经济学家菲利普·莱恩发表演讲，阐述了能源供应冲击的分析视角，可能提及近期霍尔木兹海峡关闭和美伊战争导致的全球石油供应中断及其对通胀和货币政策的影响。 他的分析可能影响市场对欧洲央行应对能源驱动通胀的政策预期，进而影响欧元区利率走势和金融稳定。 演讲提供分析框架而非直接政策声明，但正值史上最大石油供应中断（日产量减少逾 1000 万桶）之际，引发衰退担忧。

rss · ECB Press Releases · May 13, 19:00

**背景**: 欧洲央行是欧元区的中央银行，负责维持价格稳定。1970 年代石油禁运等能源供应冲击曾引发滞胀。近期霍尔木兹海峡关闭引发新的供应冲击，给货币政策带来两难：抗通胀同时避免扼杀增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rmi.org/energy-shocks-are-back-this-time-the-response-can-be-different/">Energy Shocks Are Back. This Time, the Response Can Be ...</a></li>
<li><a href="https://oilprice.com/Energy/Crude-Oil/The-Oil-Supply-Shock-Will-Scar-the-World-for-Years.html">The Oil Supply Shock Will Scar the World for Years</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#energy`, `#macroeconomics`, `#europe`, `#commodities`

---

<a id="item-10"></a>
## [欧洲央行副行长谈货币政策与经济展望](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260511~3fa2df2fa9.en.html) ⭐️ 7.0/10

欧洲央行副行长路易斯·德金多斯在接受《金融时报》采访时讨论了欧元区经济前景和货币政策，这可能影响市场对欧洲央行利率决策的预期。 在欧洲央行应对通胀风险和增长担忧之际，副行长的言论可能为未来利率走向提供线索，从而影响欧元区债券和货币市场。 没有宣布具体政策变化，但市场将仔细分析采访中关于通胀、增长或金融状况评估的任何细微转变。

rss · ECB Press Releases · May 11, 04:00

**背景**: 路易斯·德金多斯是欧洲中央银行副行长。欧洲央行负责制定欧元区 20 国的货币政策，并一直在调整利率以管理通胀和支持经济活动。欧洲央行高层的采访被密切关注，以寻找未来政策路径的信号。

**标签**: `#central-bank`, `#macroeconomics`, `#currency`, `#europe`, `#bonds`

---

<a id="item-11"></a>
## [联合国救援车辆在乌克兰赫尔松遭两次袭击](https://news.un.org/feed/view/en/story/2026/05/1167525) ⭐️ 6.0/10

5 月 14 日，一辆带有明显联合国标志的救援车辆在乌克兰赫尔松遭到两次袭击，引发联合国秘书长的警觉。 此次袭击可能加剧围绕冲突行为的外交紧张局势，或引发联合国安理会的谴责，并恶化人道主义准入状况。 遇袭车辆有明显的联合国标志，事件发生在南部城市赫尔松，该地区在战争中争夺激烈。

rss · UN News · May 15, 12:00

**背景**: 联合国人道主义车辆受国际人道法保护，蓄意袭击此类车辆可能构成战争罪。自 2022 年俄罗斯入侵乌克兰以来，赫尔松一直是前线城市，双方相互指责对方违反战争法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Attacks_on_humanitarian_workers">Attacks on humanitarian workers - Wikipedia</a></li>
<li><a href="https://www.icrc.org/en/law-and-policy/protected-persons">International humanitarian law protects a wide range of people and...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#russia-ukraine`, `#military-risk`

---

<a id="item-12"></a>
## [联合国斡旋也门换俘，1600 名被拘留者将获释](https://news.un.org/feed/view/en/story/2026/05/1167511) ⭐️ 6.0/10

联合国在约旦经数月谈判后促成协议，将释放也门 1600 多名与冲突有关的被拘留者，这是内战开始以来最大规模的换俘行动。 这一难得的建立信任措施可能为重陷停滞的和平努力注入新动力，为更广泛的政治谈判打开大门，对地区稳定和人道主义危机产生积极影响。 该协议经过联合国主导的约旦数月谈判最终敲定；这是自 2014 年冲突爆发以来最大规模的释放行动，但具体时间表和被拘留者的确切分类未立即公布。

rss · UN News · May 14, 12:00

**背景**: 也门内战始于 2014 年胡塞叛军占领首都萨那，2015 年沙特领导的多国联军介入。联合国根据 2018 年《斯德哥尔摩协议》多次斡旋换俘，以在受国际承认的政府与胡塞武装之间建立互信。尽管 2022 年联合国促成了停火，全面和平依然遥不可及，此次大规模释放提供了难得的一线进展。

**标签**: `#diplomacy`, `#yemen`, `#middle-east`, `#conflict-resolution`

---