---
layout: default
title: "Horizon Summary: 2026-05-12 (ZH)"
date: 2026-05-12
lang: zh
---

> From 45 items, 14 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [联合国秘书长呼吁霍尔木兹海峡危机降温](#item-2) ⭐️ 10.0/10
3. [美巴提出霍尔木兹海峡安理会决议](#item-3) ⭐️ 9.0/10
4. [安理会就阿联酋遇袭举行闭门磋商](#item-4) ⭐️ 9.0/10
5. [欧央行施纳贝尔警示央行独立性受侵蚀](#item-5) ⭐️ 9.0/10
6. [FSB 警告私人信贷系统性漏洞](#item-6) ⭐️ 9.0/10
7. [以色列空袭贝鲁特南郊致平民流离失所，联合国谴责](#item-7) ⭐️ 8.0/10
8. [欧央行副行长德金多斯释放政策信号](#item-8) ⭐️ 8.0/10
9. [欧央行委员剖析新能源冲击情景与政策](#item-9) ⭐️ 8.0/10
10. [联合国称黎巴嫩人道危机恶化，加沙暴力未停](#item-10) ⭐️ 7.0/10
11. [联合国：无人机导致逾 80%苏丹内战平民死亡](#item-11) ⭐️ 7.0/10
12. [联合国报告：乌克兰一周内 70 多名平民死亡](#item-12) ⭐️ 6.0/10
13. [欧央行拉加德：分离货币功能与工具](#item-13) ⭐️ 6.0/10
14. [欧洲央行工资追踪器显示 2026 年协议工资压力稳定](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 12, 11:51

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
| US Mega Cap Basket | US | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | high |
| Japan Equity Basket | JP | bullish 38/31/31 | bullish 38/31/31 | bullish 42/29/30 | medium |
| Hong Kong Equity Basket | HK | neutral 33/33/34 | bullish 38/31/31 | bullish 42/29/30 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| NQ=F price trend | close=29175.75; 1d=-0.84%; 5d=+3.70%; 20d=+12.23% | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=713.29; 1d=+0.29%; 5d=+6.01%; 20d=+15.53% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29320.66; 1d=+0.29%; 5d=+6.04%; 20d=+15.51% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=0.8%; implied_move=0.0%; put/call OI=8.629844097995546 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.42; 2Y=3.95; 10Y-2Y=0.46999999999999975 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=65.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: NASDAQ 100 implied volatility current | NASDAQ 100 implied volatility current => 100.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |

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
| NQ=F price trend | close=29175.75; 1d=-0.84%; 5d=+3.70%; 20d=+12.23% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| QQQ price trend | close=713.29; 1d=+0.29%; 5d=+6.01%; 20d=+15.53% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29320.66; 1d=+0.29%; 5d=+6.04%; 20d=+15.51% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| TSLA price trend | close=445.00; 1d=+3.89%; 5d=+13.37%; 20d=+26.27% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=598.86; 1d=-1.77%; 5d=-1.89%; 20d=-5.62% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=268.99; 1d=-1.35%; 5d=-1.12%; 20d=+12.13% | 价格趋势与均线位置用于判断短中期方向概率。 |
| GOOGL price trend | close=388.64; 1d=-3.03%; 5d=+1.41%; 20d=+20.95% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=292.68; 1d=-0.13%; 5d=+5.82%; 20d=+13.02% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=219.44; 1d=+1.97%; 5d=+10.56%; 20d=+15.92% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| NVDA options surface | ATM IV=0.4%; implied_move=0.0%; put/call OI=2.5215820048635504 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=0.1%; implied_move=0.0%; put/call OI=0.12632227213447325 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=0.8%; implied_move=0.0%; put/call OI=0.6076871066729079 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AAPL options surface | ATM IV=0.2%; implied_move=0.0%; put/call OI=0.12585659706078553 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| TSLA options surface | ATM IV=0.0%; implied_move=0.0%; put/call OI=0.9441622487979288 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=0.8%; implied_move=0.0%; put/call OI=0.5219675126323903 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| CNN Fear & Greed | score=65.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| MSFT insider filings | recent Form4 count=742 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| AAPL insider filings | recent Form4 count=586 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.42; 2Y=3.95; 10Y-2Y=0.46999999999999975 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| TSLA price trend | close=445.00; 1d=+3.89%; 5d=+13.37%; 20d=+26.27% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=598.86; 1d=-1.77%; 5d=-1.89%; 20d=-5.62% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=268.99; 1d=-1.35%; 5d=-1.12%; 20d=+12.13% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 6758.T price trend | close=3484.00; 1d=+3.32%; 5d=+11.92%; 20d=+2.83% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2843.00; 1d=-0.94%; 5d=-5.95%; 20d=-15.99% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.26; 1d=+0.04%; 5d=+4.70%; 20d=+4.43% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=52160.00; 1d=+0.15%; 5d=+17.50%; 20d=+22.99% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=5987.00; 1d=+4.25%; 5d=+14.72%; 20d=+56.65% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6861.T price trend | close=79260.00; 1d=-3.69%; 5d=+11.16%; 20d=+30.96% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| US Treasury curve | 10Y=4.42; 2Y=3.95; 10Y-2Y=0.46999999999999975 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=65.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |

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
| 6758.T price trend | close=3484.00; 1d=+3.32%; 5d=+11.92%; 20d=+2.83% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2843.00; 1d=-0.94%; 5d=-5.95%; 20d=-15.99% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=92.26; 1d=+0.04%; 5d=+4.70%; 20d=+4.43% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| EWH price trend | close=24.32; 1d=+0.16%; 5d=+3.75%; 20d=+2.53% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=37.47; 1d=+0.62%; 5d=+2.52%; 20d=+2.77% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=457.20; 1d=-1.55%; 5d=-3.18%; 20d=-6.69% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=133.30; 1d=-0.45%; 5d=+1.60%; 20d=+8.20% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 1810.HK price trend | close=31.46; 1d=-0.76%; 5d=+3.28%; 20d=+2.61% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=29.59; 1d=+0.14%; 5d=+3.50%; 20d=+3.03% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.42; 2Y=3.95; 10Y-2Y=0.46999999999999975 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| CNN Fear & Greed | score=65.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
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
| EWH price trend | close=24.32; 1d=+0.16%; 5d=+3.75%; 20d=+2.53% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=37.47; 1d=+0.62%; 5d=+2.52%; 20d=+2.77% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 0700.HK price trend | close=457.20; 1d=-1.55%; 5d=-3.18%; 20d=-6.69% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 neutral/bullish/bullish，基于 2 个独立信号层的多信号综合判断。

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

- [MOVE Index Charts and Quotes — TradingView](https://www.tradingview.com/symbols/TVC-MOVE/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：MOVE INDEX Setup for Top in World stock markets The chart is the Move index it is reaching an area which I consider High level of Complacency I say this as of this writing The 1...

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Volatility Term Structure chart plots the at-the-money implied volatility across expirations, which are an invaluable tool in determining options strategies based on anticipated...

- [Nasdaq-100 Volatility Index (VOLQ)](https://www.nasdaq.com/market-activity/index/volq)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Find the latest information on Nasdaq-100 Volatility Index (VOLQ), including data, charts, related news, and more from Nasdaq.com

- [NDAQ Implied Volatility Chart Nasdaq - MarketChameleon.com](https://marketchameleon.com/Overview/NDAQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：View volatility charts for Nasdaq (NDAQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the interactive...

- [CBOE Volatility Index (^VIX) Charts, Data & News - Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：Find the latest data, charts, news, and insights on the CBOE Volatility Index (^VIX) to support your trading and investment decisions.

- [Cboe Global Indices: VIX Index Dashboard](https://www.cboe.com/us/indices/dashboard/vix/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：The VIX Index is often referred to as the market's "fear gauge". The VIX Index is the centerpiece of Cboe Global Markets' volatility franchise, which includes volatility indexes...

- [QQQ: Invesco QQQ Trust Implied Volatility (IV) / OptionCharts](https://optioncharts.io/options/QQQ/volatility-skew)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ Volatility Skew The Implied Volatility Skew Chart offers a visual representation of the implied volatility (IV). The chart displays the strikes on the x-axis and the IV on t...

- [QQQ Implied Volatility / IV Rank & Percentile / projectoption](https://projectoption.com/stocks/qqq/implied-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：QQQ implied volatility is 20.7%. View IV Rank, IV Percentile, and 1-year historical IV chart for Invesco QQQ Trust.

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [VIX / Cboe Volatility Index Overview / MarketWatch](https://www.marketwatch.com/investing/index/vix)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：VIX current level
  - 摘要：VIX / A complete Cboe Volatility Index index overview by MarketWatch. View stock market news, stock market data and trading information.

- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：The ICE BofA High Yield Master II OAS uses an index of bonds that are below investment grade (those rated BB or below). This data represents the ICE BofA US High Yield Index val...

- [United States - ICE BofA US High Yield Index Option-Adjusted Spread ...](https://tradingeconomics.com/united-states/bofa-merrill-lynch-us-high-yield-option-adjusted-spread-fed-data.html)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：US high yield OAS current
  - 摘要：United States - ICE BofA US High Yield Index Option-Adjusted Spread was 2.79% in May of 2026, according to the United States Federal Reserve. Historically, United States - ICE B...

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

- [Index Information - Nikkei Indexes](https://indexes.nikkei.co.jp/en/nkave/index/profile?idx=nk225vi)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：The Nikkei Stock Average Volatility Index are calculated by using prices of Nikkei 225 futures and Nikkei 225 options on the Osaka Exchange (OSE). In the calculation, taking nea...

- [Nikkei Average Volatility (^NKVI.OS) - Yahoo Finance](https://finance.yahoo.com/quote/%5ENKVI.OS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Find the latest information on Nikkei Average Volatility (^NKVI.OS) including data, charts, related news and more from Yahoo Finance

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
## [联合国秘书长呼吁霍尔木兹海峡危机降温](https://news.un.org/feed/view/en/story/2026/05/1167478) ⭐️ 10.0/10

随着霍尔木兹海峡危机加剧、油价周一早盘上涨，联合国秘书长安东尼奥·古特雷斯紧急呼吁和平解决，并警告危机正对非洲及其他地区产生广泛经济影响。 霍尔木兹海峡承担全球约 25%的海运石油贸易，长期中断将严重扰乱能源供应，推高通胀，冲击金融市场，非洲和亚洲的发展中经济体尤其脆弱。 危机源于 2026 年伊朗战争，霍尔木兹海峡成为关键冲突点；2025 年每日约 2000 万桶石油经过该海峡。周一油价再次上涨，联合国秘书长特别指出非洲正遭受严重的间接冲击。

rss · UN News · May 11, 12:00

**背景**: 霍尔木兹海峡是波斯湾唯一海上通道，对全球能源运输至关重要。因伊朗核计划以及 2026 年伊朗战争（起因于镇压反政府抗议），美伊冲突持续升级。尽管 2025–2026 年日内瓦谈判一度接近达成历史性协议，但最终未能避免军事对抗。历史上该海峡极少被关闭，但伊朗多次威胁封锁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Iran_war">2026 Iran war - Wikipedia</a></li>
<li><a href="https://www.bbc.com/news/articles/c78n6p09pzno">Iran war: What is the Strait of Hormuz and why does it matter?</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#energy`, `#military-risk`, `#middle-east`, `#commodities`

---

<a id="item-3"></a>
## [美巴提出霍尔木兹海峡安理会决议](https://news.un.org/feed/view/en/story/2026/05/1167464) ⭐️ 9.0/10

周四，巴林和美国在纽约联合国总部散发了一份安理会决议草案，要求伊朗停止在霍尔木兹海峡的袭击。 该决议在伊朗自 2026 年 2 月以来基本封锁海峡的危机中增加对伊外交压力，威胁全球能源供应并可能引发油价进一步飙升。 决议草案的具体内容和是否援引第七章尚不明确，且由于俄罗斯和中国过去常庇护伊朗免受联合国制裁，决议能否通过存在不确定性，两国可能动用否决权。

rss · UN News · May 7, 12:00

**背景**: 霍尔木兹海峡是关键海上咽喉，全球约 20%的石油和液化天然气经此运输。自 2026 年 2 月下旬美国与以色列发动空袭并暗杀伊朗最高领袖哈梅内伊以来，伊朗基本封锁了该海峡，导致能源贸易严重中断和油价飙升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis">2026 Strait of Hormuz crisis - Wikipedia</a></li>
<li><a href="https://www.bbc.com/news/articles/c78n6p09pzno">Iran war: What is the Strait of Hormuz and why does it matter?</a></li>
<li><a href="https://unctad.org/publication/strait-hormuz-disruptions-implications-global-trade-and-development">Strait of Hormuz disruptions: Implications for global trade and development | UN Trade and Development (UNCTAD)</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`, `#united-states`

---

<a id="item-4"></a>
## [安理会就阿联酋遇袭举行闭门磋商](https://news.un.org/feed/view/en/story/2026/05/1167453) ⭐️ 9.0/10

联合国安理会周三就阿联酋遇袭事件举行闭门磋商，此次袭击与不断升级的霍尔木兹海峡危机有关。联合国发言人斯特凡·杜加里克重申，联合国将继续致力于支持和平努力。 此次磋商可能引发安理会采取行动，如制裁或授权军事措施，可能导致冲突升级。霍尔木兹海峡是关键石油运输通道，任何中断都有可能推高全球能源价格并引发市场动荡。 鉴于会议闭门进行，暂无公开细节；但自 2026 年 2 月美以空袭后伊朗封锁海峡以来，油价一度飙升至每桶 126 美元以上。阿联酋作为主要石油出口国和美国盟友，一直是伊朗报复性袭击的目标。

rss · UN News · May 6, 12:00

**背景**: 联合国安理会是维护国际和平的主要机构，有权实施制裁或授权使用武力。霍尔木兹海峡危机始于 2026 年 2 月 28 日，美以对伊朗发动空袭后，伊朗封锁海峡，造成自 1970 年代以来最严重的能源供应中断。阿联酋位于波斯湾，是美国重要盟友，并为联合国等联军提供基地，因此成为冲突目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UN_Security_Council">UN Security Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz_crisis">Strait of Hormuz crisis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Foreign_relations_of_the_United_Arab_Emirates">Foreign relations of the United Arab Emirates - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`

---

<a id="item-5"></a>
## [欧央行施纳贝尔警示央行独立性受侵蚀](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260507_1~d5ae988ece.en.html) ⭐️ 9.0/10

欧洲央行执行委员会成员伊莎贝尔·施纳贝尔警告称，央行独立性正受到悄然侵蚀，对欧元区货币政策可信度和宏观经济稳定构成风险。 这种侵蚀可能推高通胀预期，引发债券市场波动和欧元汇率压力，影响欧元区资产与金融稳定，预示着可能出现的政治干预将削弱欧洲央行维护物价稳定的能力。 施纳贝尔的讲话强调这种侵蚀是悄然渐进的，而非公开攻击。这一警告出自欧洲央行高官之口，反映出央行界内部的深切担忧。

rss · ECB Press Releases · May 7, 17:00

**背景**: 央行独立性使货币政策能够专注于物价稳定，不受政治干预。这是现代宏观经济学的基石，有证据表明独立性更强的央行通常能实现更低通胀。欧洲央行根据欧盟条约具有法定独立性，但来自政府或舆论的压力可能间接削弱其实效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Central_bank_independence">Central bank independence</a></li>
<li><a href="https://en.wikipedia.org/wiki/Monetary_policy_credibility">Monetary policy credibility</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#financial-stability`, `#europe`, `#sovereign-risk`

---

<a id="item-6"></a>
## [FSB 警告私人信贷系统性漏洞](https://www.fsb.org/2026/05/fsb-warns-on-private-credit-vulnerabilities/) ⭐️ 9.0/10

金融稳定委员会（FSB）警告称，私人信贷市场（目前规模估计为 1.5 至 2 万亿美元）的复杂性、高杠杆和高度互联性可能在不利情景下放大压力，威胁金融稳定。 这一警告预示着可能的监管审查，并可能引发资产重新定价或向银行和债券市场蔓延，影响投资者和中型企业融资。 FSB 指出私人信贷的不透明和‘轻契约’贷款，加上其在 2008 年后迅速扩张，构成了传染渠道；但该行业在压力下的韧性尚未经过检验。

rss · Financial Stability Board News · May 6, 06:00

**背景**: FSB 是协调二十国集团（G20）金融稳定政策的国际机构。私人信贷指由非银行机构（通常为基金）向企业发放的贷款，自 2008 年危机后因银行监管收紧而迅速增长。系统性风险指因相互关联而可能导致整个金融体系崩溃的风险。FSB 的警告反映出私人信贷与银行及投资者的关联可能传导冲击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Financial_Stability_Board">Financial Stability Board</a></li>
<li><a href="https://en.wikipedia.org/wiki/Private_credit">Private credit</a></li>
<li><a href="https://en.wikipedia.org/wiki/Systemic_risk">Systemic risk</a></li>

</ul>
</details>

**标签**: `#financial-stability`, `#macroeconomics`, `#global-markets`, `#private-credit`, `#systemic-risk`

---

<a id="item-7"></a>
## [以色列空袭贝鲁特南郊致平民流离失所，联合国谴责](https://news.un.org/feed/view/en/story/2026/05/1167460) ⭐️ 8.0/10

以色列夜间空袭了贝鲁特南郊的真主党据点，导致新一波平民流离失所，联合国对此进行严厉谴责，称其“非常令人震惊”。 此次空袭可能引发真主党更大规模的报复，破坏地区稳定，推高油价，加剧本已严峻的人道主义危机，并考验脆弱的国际停火努力。 以色列称空袭针对的是人口稠密的达希耶地区的一名真主党精锐拉德万部队高级指挥官；此次袭击发生在美国促成三周停火延期之后。

rss · UN News · May 7, 12:00

**背景**: 贝鲁特南郊的达希耶是真主党的大本营。以色列与黎巴嫩的冲突于 2024 年底急剧升级，以色列发动了大规模空袭和地面入侵。真主党是受伊朗支持的强大军事和政治力量。美国近期促成了一项临时停火延期，但违反停火的行为时有发生。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/middle-east/strike-hits-beiruts-southern-suburbs-first-time-weeks-sources-say-2026-05-06/">Israel says carried out strike targeting commander of Hezbollah's elite force</a></li>
<li><a href="https://www.bbc.com/news/articles/c62kyk5j28do">Trump says Israel - Lebanon ceasefire to be extended by three weeks</a></li>
<li><a href="https://www.kurdistan24.net/en/story/912580/senior-hezbollah-commander-killed-in-israeli-strike-on-beirut-suburbs">Senior Hezbollah Commander Killed in Israeli Strike on Beirut Suburbs</a></li>

</ul>
</details>

**标签**: `#military-risk`, `#middle-east`, `#geopolitics`, `#humanitarian`, `#diplomacy`

---

<a id="item-8"></a>
## [欧央行副行长德金多斯释放政策信号](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260511~3fa2df2fa9.en.html) ⭐️ 8.0/10

欧央行副行长路易斯·德金多斯于 2026 年 5 月 11 日接受《金融时报》采访，讨论了欧元区经济前景、通胀及未来货币政策走向。 其言论可能改变市场对欧央行未来利率决策的预期，从而影响欧元区债券收益率、欧元汇率和股市。 此次采访可能透露关于经济增长风险或通胀持续性的具体看法，为降息时机和节奏、或资产负债表调整提供新线索。

rss · ECB Press Releases · May 11, 04:00

**背景**: 路易斯·德金多斯自 2018 年起担任欧央行副行长，其公开言论被密切关注以获取政策信号。欧央行为欧元区 20 国制定关键利率，通过引导货币状况来维持物价稳定。《金融时报》是国际领先的财经媒体，为央行提供一个高调的沟通平台，其采访常引发市场波动。

**标签**: `#central-bank`, `#macroeconomics`, `#currency`, `#europe`, `#global-markets`

---

<a id="item-9"></a>
## [欧央行委员剖析新能源冲击情景与政策](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260506~1bbd4ed780.en.html) ⭐️ 8.0/10

欧洲央行执行委员皮耶罗·西波隆于 2026 年 6 月 5 日发表演讲，探讨欧元区新一次能源冲击的经济情景与政策影响。 演讲释放了欧央行对能源再冲击引发通胀与增长风险的应对信号，可能动摇市场利率预期并波及欧元资产定价。 西波隆可能阐述了能源价格持续高位或地缘政治事件导致飙升等情景，及其对价格稳定的影响；虽未公布即时措施，但基调会左右后续利率决策。

rss · ECB Press Releases · May 6, 08:20

**背景**: 欧洲央行负责欧元区 20 国货币政策。意大利经济学家西波隆自 2023 年 11 月起担任执行委员。欧元区对能源冲击高度敏感，2022 年乌克兰危机曾推动通胀创纪录并引发激进加息。本次讲话正值全球能源持续动荡、绿色转型面临挑战之际。

**标签**: `#central-bank`, `#macroeconomics`, `#energy`, `#commodities`, `#europe`

---

<a id="item-10"></a>
## [联合国称黎巴嫩人道危机恶化，加沙暴力未停](https://news.un.org/feed/view/en/story/2026/05/1167483) ⭐️ 7.0/10

联合国周一报告，尽管上月与以色列达成停火，但黎巴嫩人道主义局势仍在恶化，同时加沙的暴力仍在继续。 这表明停火可能崩溃，加剧地区不稳定风险，可能影响能源市场并引发外交或军事升级。 尽管上月与以色列达成停火协议，黎巴嫩的人道主义指标仍在下降，加沙仍处于冲突中，联合国警告平民苦难加剧。

rss · UN News · May 11, 12:00

**背景**: 黎巴嫩正应对经济崩溃和政治动荡。以色列与 Hezbollah 之间的停火在上个月生效，此前发生了跨境敌对行动。同时，以色列在加沙针对 Hamas 的军事行动自 2023 年 10 月以来持续，造成广泛破坏和严重人道危机。联合国定期监测并报告两地状况。

**标签**: `#middle-east`, `#military-risk`, `#diplomacy`, `#geopolitics`

---

<a id="item-11"></a>
## [联合国：无人机导致逾 80%苏丹内战平民死亡](https://news.un.org/feed/view/en/story/2026/05/1167479) ⭐️ 7.0/10

联合国人权事务高级专员报告称，2026 年 1 月至 4 月，武装无人机导致苏丹战争中超过 80%的平民死亡，至少 880 人遇难，并警告无人机使用增加可能使冲突进入更致命的阶段。 这标志着冲突升级，可能引发更多国际关注、潜在制裁或武器禁运，并影响地区稳定，包括石油管道和难民潮，产生重大外交和人道主义影响。 数据涵盖 2026 年前四个月，无人机袭击造成至少 880 名平民死亡；联合国警告说，随着无人机战加剧，这可能进入一个“新的、甚至更致命的阶段”。

rss · UN News · May 11, 12:00

**背景**: 自 2023 年 4 月以来，苏丹陷入苏丹武装部队与快速支援部队之间的内战，已造成数千人死亡和大规模流离失所。双方越来越多地使用无人机，经常针对平民区，引发国际人道法的关切，该法禁止直接攻击平民。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.euronews.com/2026/05/11/sudan-drone-strikes-killed-at-least-880-civilians-between-january-and-april-un-says">Sudan drone strikes killed at least 880 civilians between... | Euronews</a></li>
<li><a href="https://news.un.org/en/story/2026/05/1167479">Armed drones leading cause of civilian death in Sudan war: UN rights ...</a></li>
<li><a href="https://www.rfi.fr/en/africa/20260511-sudan-conflict-enters-deadlier-phase-due-to-drones-un-civilan-deaths">Sudan conflict enters 'deadlier' phase due to drones : UN - RFI</a></li>

</ul>
</details>

**标签**: `#sudan`, `#military-risk`, `#diplomacy`, `#geopolitics`, `#sovereign-risk`

---

<a id="item-12"></a>
## [联合国报告：乌克兰一周内 70 多名平民死亡](https://news.un.org/feed/view/en/story/2026/05/1167454) ⭐️ 6.0/10

联合国人权监察员周三报告称，自 5 月初以来，乌克兰各地至少有 70 名平民死亡、500 多人受伤。伤亡发生在袭击加剧和人道主义工作者难以进入前线附近地区之际。 平民伤亡的增加可能加大对俄罗斯的外交压力，增加进一步制裁的可能性，并影响全球市场的风险情绪，不过直接的金融影响有限。这凸显了持续的人道主义危机和军事升级的可能性。 这些数据由联合国人权监察员发布，背景是乌克兰城市遭受一波波攻击，人道主义工作者难以抵达前线附近的受影响社区。

rss · UN News · May 6, 12:00

**背景**: 联合国乌克兰人权监测团自 2014 年冲突开始以来一直在记录平民伤亡，并在 2022 年 2 月俄罗斯全面入侵后加强了工作。该特派团定期发布报告，常会影响国际舆论和政策应对。平民死亡人数是评估国际人道法遵守情况的关键指标。

**标签**: `#russia-ukraine`, `#military-risk`, `#diplomacy`, `#global-markets`

---

<a id="item-13"></a>
## [欧央行拉加德：分离货币功能与工具](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260508~dd909fbed1.en.html) ⭐️ 6.0/10

2026 年 5 月 8 日，欧央行行长拉加德在一次演讲中提出，应将货币的经济功能（计价单位、交易媒介、价值储存）与实现这些功能的工具（现金、存款、稳定币）进行概念分离，以理清对数字货币的监管处理。 这一框架可能影响欧盟对稳定币的监管方针及数字欧元的设计，进而可能影响私有数字货币的处理方式和央行货币的演变，对金融稳定和货币主权产生影响。 演讲可能表明欧央行倾向于建立一种将货币类功能与提供这些功能的工具区分开的监管体系，这可能导致根据用途对不同类型的稳定币实施不同规则；未宣布具体政策，但这一概念可能影响欧盟即将出台的数字金融立法。

rss · ECB Press Releases · May 8, 07:00

**背景**: 欧洲央行是欧元区的中央银行，负责维持价格稳定。它一直在探索数字欧元，即一种补充现金的央行数字货币。稳定币是旨在与参考资产保持稳定价值的加密货币，但由于其对金融稳定和货币政策构成风险而受到密切关注。拉加德的演讲正值全球讨论数字资产监管和推进央行数字货币之际。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stablecoin">Stablecoin</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_euro">Digital euro</a></li>
<li><a href="https://en.wikipedia.org/wiki/European_Central_Bank">European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#stablecoins`, `#currency`, `#financial-stability`

---

<a id="item-14"></a>
## [欧洲央行工资追踪器显示 2026 年协议工资压力稳定](https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260506~4ea17afd4a.en.html) ⭐️ 6.0/10

欧洲央行发布了工资追踪器的新数据，表明欧元区的协议工资压力在 2026 年保持稳定；包含一次性支付的未经平滑处理的指标显示，2025 年为 3.0%，2026 年降至 2.6%。 工资增长稳定表明来自工资的国内通胀压力得到控制，降低了工资-价格螺旋上升的风险，为欧洲央行维持或加快货币宽松提供了支持，并对欧元区债券收益率和欧元汇率产生影响。 该追踪器的未经平滑处理的一次性支付指标显示，2026 年协议工资增长率为 2.6%，低于 2025 年的 3.0%；2026 年第四季度数据从上季度的 2.5%微升至 2.6%，但总体趋势表明工资压力在逐步正常化。

rss · ECB Press Releases · May 6, 08:00

**背景**: 欧洲央行的工资追踪器是欧元区协议工资增长的指标，政策制定者密切关注它，将其作为通胀预测的关键输入。协议工资是通过集体谈判协议确定的，可以作为服务通胀的先行指标。在 2023-2024 年因高通胀补偿而飙升后，工资增长一直在放缓，最新数据证实了正常化趋势，减轻了对持续的二轮通胀效应的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tradingeconomics.com/euro-area/wage-tracker">ECB Wage Tracker</a></li>
<li><a href="https://www.einpresswire.com/article/910848039/new-data-release-ecb-wage-tracker-indicates-negotiated-wage-pressures-stable-in-2026">New data release: ECB wage tracker indicates negotiated wage ...</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#bonds`

---