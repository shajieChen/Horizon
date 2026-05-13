---
layout: default
title: "Horizon Summary: 2026-05-14 (ZH)"
date: 2026-05-14
lang: zh
---

> From 43 items, 10 important content pieces were selected

---

1. [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](#item-1) ⭐️ 10.0/10
2. [联合国秘书长呼吁霍尔木兹海峡危机紧急缓和](#item-2) ⭐️ 10.0/10
3. [欧央行副行长接受金融时报采访谈货币政策](#item-3) ⭐️ 7.5/10
4. [联合国驻黎部队警告无人机活动威胁南黎巴嫩维和人员安全](#item-4) ⭐️ 7.0/10
5. [联合国警告：停火后黎巴嫩局势仍在恶化](#item-5) ⭐️ 7.0/10
6. [欧央行施纳贝尔警告央行独立性受侵蚀](#item-6) ⭐️ 7.0/10
7. [联合国：无人机致苏丹内战平民死亡超八成](#item-7) ⭐️ 6.0/10
8. [联合国评估中东核能利弊](#item-8) ⭐️ 6.0/10
9. [索马里饥饿危机加剧，濒临灾难边缘](#item-9) ⭐️ 6.0/10
10. [黎巴嫩停火脆弱 以色列袭击不断](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Daily Trading Watchlist: QDII Nasdaq 100 / US / Japan / Hong Kong Stocks](https://github.com/shajieChen/Horizon) ⭐️ 10.0/10

Daily fixed trading watchlist analysis for QDII Nasdaq 100, overseas stocks, US stocks, Japan stocks, and Hong Kong stocks.

rss · Horizon Trading · May 13, 23:07

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
| Hong Kong Equity Basket | HK | bullish 38/31/31 | bullish 38/31/31 | bullish 42/29/30 | medium |

### Digital Oracle Signal Layers

#### QDII Nasdaq 100 Proxy *(代理品种)*

市场：US
品种：QQQ, ^NDX, NQ=F

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| QQQ price trend | close=714.71; 1d=+1.06%; 5d=+2.72%; 20d=+12.13% | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29366.94; 1d=+1.04%; 5d=+2.68%; 20d=+12.07% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29590.50; 1d=+1.44%; 5d=+3.04%; 20d=+12.23% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| QQQ options surface | ATM IV=2.5%; implied_move=0.1%; put/call OI=2.6456606380306456 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: VIX current level | VIX current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: MOVE index current level | MOVE index current level => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| CNN Fear & Greed | score=65.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| US Treasury curve | 10Y=4.46; 2Y=3.98; 10Y-2Y=0.48 | 利率曲线决定权益估值贴现与风险偏好上限。 |
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
| QQQ price trend | close=714.71; 1d=+1.06%; 5d=+2.72%; 20d=+12.13% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| ^NDX price trend | close=29366.94; 1d=+1.04%; 5d=+2.68%; 20d=+12.07% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| NQ=F price trend | close=29590.50; 1d=+1.44%; 5d=+3.04%; 20d=+12.23% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> QDII Nasdaq 100 Proxy: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### US Mega Cap Basket

市场：US
品种：AAPL, MSFT, NVDA, GOOGL, META, AMZN, TSLA

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| TSLA price trend | close=445.27; 1d=+2.73%; 5d=+11.67%; 20d=+13.60% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=298.87; 1d=+1.38%; 5d=+4.05%; 20d=+12.28% | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=405.21; 1d=-0.63%; 5d=-2.11%; 20d=-1.46% | 价格趋势与均线位置用于判断短中期方向概率。 |
| NVDA price trend | close=225.83; 1d=+2.29%; 5d=+8.66%; 20d=+13.56% | 价格趋势与均线位置用于判断短中期方向概率。 |
| AMZN price trend | close=270.13; 1d=+1.62%; 5d=-1.77%; 20d=+8.70% | 价格趋势与均线位置用于判断短中期方向概率。 |
| META price trend | close=616.63; 1d=+2.26%; 5d=+0.61%; 20d=-8.18% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| AAPL options surface | ATM IV=6.0%; implied_move=0.3%; put/call OI=0.37094440213252095 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| AMZN options surface | ATM IV=4.0%; implied_move=0.1%; put/call OI=0.6319684964653414 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| NVDA options surface | ATM IV=7.5%; implied_move=0.4%; put/call OI=0.6493682078488223 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| GOOGL options surface | ATM IV=3.8%; implied_move=0.1%; put/call OI=0.5741249509401648 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| MSFT options surface | ATM IV=2.6%; implied_move=0.1%; put/call OI=0.49606058131939906 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |
| META options surface | ATM IV=5.4%; implied_move=0.2%; put/call OI=0.4888041417218825 | 期权隐含波动与仓位结构刻画短期波动区间和尾部风险定价。 |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| AAPL insider filings | recent Form4 count=586 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| CNN Fear & Greed | score=65.9; rating=greed | 风险偏好指数用于识别情绪顺风或逆风。 |
| Web metric: QQQ implied volatility current | QQQ implied volatility current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| MSFT insider filings | recent Form4 count=742 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| NVDA insider filings | recent Form4 count=567 | 内部人交易节奏可作为估值温度辅助校验信号。 |
| US Treasury curve | 10Y=4.46; 2Y=3.98; 10Y-2Y=0.48 | 利率曲线决定权益估值贴现与风险偏好上限。 |

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
| TSLA price trend | close=445.27; 1d=+2.73%; 5d=+11.67%; 20d=+13.60% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| AAPL price trend | close=298.87; 1d=+1.38%; 5d=+4.05%; 20d=+12.28% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| MSFT price trend | close=405.21; 1d=-0.63%; 5d=-2.11%; 20d=-1.46% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> US Mega Cap Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 3 个独立信号层的多信号综合判断。


#### Japan Equity Basket

市场：JP
品种：7203.T, 6758.T, 9984.T, 8035.T, 6861.T

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 6861.T price trend | close=79440.00; 1d=+0.23%; 5d=+3.90%; 20d=+28.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=51340.00; 1d=-1.57%; 5d=+8.20%; 20d=+21.69% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2939.50; 1d=+3.39%; 5d=-2.02%; 20d=-11.75% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 6758.T price trend | close=3660.00; 1d=+5.05%; 5d=+17.05%; 20d=+8.44% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9984.T price trend | close=6012.00; 1d=+0.42%; 5d=+10.84%; 20d=+59.26% | 价格趋势与均线位置用于判断短中期方向概率。 |
| EWJ price trend | close=93.09; 1d=+1.12%; 5d=+1.54%; 20d=+4.51% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Japan equity ETF EWJ price current | Japan equity ETF EWJ price current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.46; 2Y=3.98; 10Y-2Y=0.48 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: Nikkei 225 volatility current | Nikkei 225 volatility current => 225.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD JPY exchange rate current | USD JPY exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
| 6861.T price trend | close=79440.00; 1d=+0.23%; 5d=+3.90%; 20d=+28.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 8035.T price trend | close=51340.00; 1d=-1.57%; 5d=+8.20%; 20d=+21.69% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 7203.T price trend | close=2939.50; 1d=+3.39%; 5d=-2.02%; 20d=-11.75% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Japan Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。


#### Hong Kong Equity Basket

市场：HK
品种：0700.HK, 9988.HK, 3690.HK, 1810.HK, 9618.HK

##### Layer 1: Price Trend
| Signal | Data | What it's saying |
|---|---|---|
| 1810.HK price trend | close=31.80; 1d=+1.08%; 5d=+3.18%; 20d=+2.98% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=132.80; 1d=-0.38%; 5d=-1.04%; 20d=+6.67% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=87.60; 1d=+4.10%; 5d=+6.18%; 20d=+2.94% | 价格趋势与均线位置用于判断短中期方向概率。 |
| FXI price trend | close=38.26; 1d=+2.49%; 5d=+2.05%; 20d=+3.74% | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9618.HK price trend | close=128.20; 1d=+8.28%; 5d=+10.14%; 20d=+11.09% | 价格趋势与均线位置用于判断短中期方向概率。 |
| KWEB price trend | close=30.59; 1d=+4.94%; 5d=+2.79%; 20d=+3.21% | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Layer 2: Options / Volatility
| Signal | Data | What it's saying |
|---|---|---|
| - | - | - |

##### Layer 3: Risk Appetite / Macro
| Signal | Data | What it's saying |
|---|---|---|
| Web metric: Hang Seng volatility index current | Hang Seng volatility index current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| Web metric: USD HKD exchange rate current | USD HKD exchange rate current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
| US Treasury curve | 10Y=4.46; 2Y=3.98; 10Y-2Y=0.48 | 利率曲线决定权益估值贴现与风险偏好上限。 |
| Web metric: China high yield dollar bond spread current | China high yield dollar bond spread current => 1.0 | 补充性交易数据用于校验波动与信用风险状态。 |
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
| 1810.HK price trend | close=31.80; 1d=+1.08%; 5d=+3.18%; 20d=+2.98% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 9988.HK price trend | close=132.80; 1d=-0.38%; 5d=-1.04%; 20d=+6.67% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |
| 3690.HK price trend | close=87.60; 1d=+4.10%; 5d=+6.18%; 20d=+2.94% | regime shift | 价格趋势与均线位置用于判断短中期方向概率。 |

##### Conclusion

> Hong Kong Equity Basket: 1日/1周/1月偏向分别为 bullish/bullish/bullish，基于 2 个独立信号层的多信号综合判断。

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

- [ICE BofAML MOVE Index Today (MOVE) - Investing.com](https://www.investing.com/indices/ice-bofaml-move)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Get detailed information on the ICE BofAML MOVE including charts, technical analysis, components and more.

- [Move Index Chart - Barchart.com](https://www.barchart.com/stocks/quotes/$MOVE/interactive-chart)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：MOVE index current level
  - 摘要：Customizable interactive chart for Move Index with latest real-time price quote, charts, latest news, technical analysis and opinions.

- [Nasdaq 100 Index Volatility Term Structure - Barchart.com](https://www.barchart.com/stocks/quotes/$IUXX/volatility-charts)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Implied Volatility: The average implied volatility (IV) of the nearest monthly options contract that is 30-days or more out. IV is a forward looking prediction of the likelihood...

- [Cboe Global Indices: VXN Index Dashboard](https://www.cboe.com/us/indices/dashboard/VXN/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：NASDAQ 100 implied volatility current
  - 摘要：Cboe NASDAQ-100 Volatility Index SM (VXN) The Cboe NASDAQ-100 Volatility Index SM (VXN) is a key measure of market expectations of near-term volatility conveyed by NASDAQ-100 ®...

- [QQQ: Invesco QQQ Trust Option Overview / OptionCharts](https://optioncharts.io/options/QQQ)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View comprehensive QQQ options with our latest charts on volume, open interest, max pain, and implied volatility.

- [QQQ Implied Volatility Chart Invesco QQQ Trust - MarketChameleon.com](https://marketchameleon.com/Overview/QQQ/IV/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：View volatility charts for Invesco QQQ Trust (QQQ) including implied volatility and realized volatility. Overlay and compare different stocks and volatility metrics using the in...

- [Invesco QQQ (QQQ) Options Chain & Prices 2026 - MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/QQQ/options/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：QQQ implied volatility current
  - 摘要：Are you trading options on Invesco QQQ (NASDAQ:QQQ)? View the latest QQQ options chain and put and call options prices at MarketBeat.

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

- [iShares MSCI Japan ETF (EWJ) Stock Price, News, Quote & History - Yahoo ...](https://finance.yahoo.com/quote/EWJ/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：Find the latest iShares MSCI Japan ETF (EWJ) stock quote, history, news and other vital information to help you with your stock trading and investing.

- [EWJ / iShares MSCI Japan ETF Overview / MarketWatch](https://www.marketwatch.com/investing/fund/ewj)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：EWJ / A complete iShares MSCI Japan ETF exchange traded fund overview by MarketWatch. View the latest ETF prices and news for better ETF investing.

- [iShares MSCI Japan ETF / EWJ](https://www.ishares.com/us/products/239665/ishares-msci-japan-etf)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Japan equity ETF EWJ price current
  - 摘要：The iShares MSCI Japan ETF seeks to track the investment results of an index composed of Japanese equities.

- [Nikkei Average Volatility (^NKVI.OS) - Yahoo Finance](https://finance.yahoo.com/quote/%5ENKVI.OS/)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Find the latest information on Nikkei Average Volatility (^NKVI.OS) including data, charts, related news and more from Yahoo Finance

- [Nikkei Volatility Index Today (JNIVE) - Investing.com](https://www.investing.com/indices/nikkei-volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get detailed information on the Nikkei Volatility including charts, technical analysis, components and more.

- [Nikkei 225 Index Volatility History & Chart Since 1974](https://wallstreetnumbers.com/indexes/n225/volatility)
  - 来源：WebSearchProvider / Risk Appetite / Macro
  - 查询：Nikkei 225 volatility current
  - 摘要：Get all-time historical data of Nikkei 225 index historical volatility, analyze it on an interactive chart, and compare its performance with other metrics

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
## [联合国秘书长呼吁霍尔木兹海峡危机紧急缓和](https://news.un.org/feed/view/en/story/2026/05/1167478) ⭐️ 10.0/10

由于伊朗与美国在霍尔木兹海峡的紧张局势持续升级，周一早盘油价再度上涨。联合国秘书长呼吁和平解决危机，并警告称冲突可能对非洲及其他地区造成广泛的经济影响。 霍尔木兹海峡是全球石油和天然气贸易的关键咽喉，任何干扰都可能导致能源价格飙升，加剧通胀，给全球特别是非洲等依赖进口的地区经济带来压力。 联合国秘书长特别警告经济影响将波及‘非洲及其他地区’，凸显依赖进口的发展中经济体所受冲击尤为严重，油价已徘徊在每桶 100 美元以上。

rss · UN News · May 11, 12:00

**背景**: 霍尔木兹海峡位于伊朗与阿曼之间，是全球最重要的能源咽喉之一，约 25%的全球海运石油和 20%的液化天然气经过此通道。2026 年初，伊朗与美国紧张局势升级为军事冲突，导致海峡部分关闭，油价飙升至每桶 100 美元以上。这场危机扰乱了全球能源市场，对依赖进口的国家尤其构成严重经济威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Strait_of_Hormuz">Strait of Hormuz - Wikipedia</a></li>
<li><a href="https://www.reuters.com/business/energy/oil-jumps-us-iran-fail-reach-agreement-peace-proposal-2026-05-10/">Oil prices settle higher after Trump says Iran ceasefire "on life support" | Reuters</a></li>
<li><a href="https://press.un.org/en/2026/sgsm23033.doc.htm">Following Iran Strikes, Secretary-General Warns Security Council of Wider Conflict in Middle East, Calls for De-escalation, Immediate Ceasefire | UN Meetings Coverage and Press Releases</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#energy`, `#middle-east`

---

<a id="item-3"></a>
## [欧央行副行长接受金融时报采访谈货币政策](https://www.ecb.europa.eu//press/inter/date/2026/html/ecb.in260511~3fa2df2fa9.en.html) ⭐️ 7.5/10

欧央行副行长路易斯·德金多斯接受金融时报采访，讨论了欧元区经济前景、通胀动态和货币政策未来路径，可能预示即将到来的利率调整。 他的言论对金融市场至关重要，因其可能影响市场对欧央行利率决策的预期，从而影响欧元汇率、主权债券收益率和欧元区银行业信心。 采访可能讨论了控制顽固通胀与支持疲弱经济增长之间的平衡，德金多斯重申欧央行依赖数据的立场，但对降息时机留有解读空间。

rss · ECB Press Releases · May 11, 04:00

**背景**: 路易斯·德金多斯曾任西班牙经济部长，自 2018 年起担任欧央行副行长。欧央行为欧元区 20 国制定货币政策，目标是 2%的通胀。这样高调的采访常被用来试探市场反应或为政策调整做准备。

**标签**: `#central-bank`, `#macroeconomics`, `#europe`, `#bonds`, `#currencies`

---

<a id="item-4"></a>
## [联合国驻黎部队警告无人机活动威胁南黎巴嫩维和人员安全](https://news.un.org/feed/view/en/story/2026/05/1167496) ⭐️ 7.0/10

联合国驻黎巴嫩临时部队（UNIFIL）警告称，疑似真主党无人机和以色列军队引发的无人机活动及爆炸事件不断升级，正危及维和人员并威胁南黎巴嫩本已脆弱的稳定。 这一警告凸显以色列-黎巴嫩边境军事活动加剧，有将联合国维和人员卷入交火的风险，可能升级为更广泛的地区冲突，从而影响市场和外交局势。 该警告于周三发布，恰逢拥有来自 48 个国家逾 8000 名士兵的联黎部队在“蓝线”（以色列与黎巴嫩之间的非正式边界）附近面临来自空中的直接威胁。

rss · UN News · May 13, 12:00

**背景**: 联黎部队于 1978 年为监督以色列撤军而设立，此后一直负责监测以色列-黎巴嫩边境。真主党是受伊朗支持的强大武装组织，被许多国家认定为恐怖组织。该边境地区时有暴力事件发生，包括 2006 年的重大战争和 2024 年的新一轮冲突，目前维持着脆弱的停火。联黎部队的职责是防止局势升级，但越来越频繁地被卷入交火。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UNIFIL">UNIFIL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hezbollah">Hezbollah</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#military-risk`, `#middle-east`, `#diplomacy`

---

<a id="item-5"></a>
## [联合国警告：停火后黎巴嫩局势仍在恶化](https://news.un.org/feed/view/en/story/2026/05/1167483) ⭐️ 7.0/10

联合国报告称，尽管上月与以色列达成停火，黎巴嫩的人道主义局势仍在恶化，黎巴嫩和加沙的致命暴力仍在继续。 暴力持续和人道状况恶化可能导致停火破裂，重新引发更广泛的地区冲突，威胁能源市场和外交稳定。 联合国的警告未提供具体伤亡数字，但强调上月促成的停火协议未能制止黎巴嫩南部的敌对行动，也未能解决并行的加沙冲突。

rss · UN News · May 11, 12:00

**背景**: 自哈马斯 2023 年 10 月袭击以色列以来，该地区陷入冲突，加沙全面战争爆发，并牵动黎以边境的真主党。经过紧张外交斡旋，以色列和真主党于 2024 年 11 月达成停火，但执行脆弱，偶有交火，大规模流离失所和基础设施破坏加剧了人道危机。

**标签**: `#middle-east`, `#geopolitics`, `#military-risk`, `#diplomacy`

---

<a id="item-6"></a>
## [欧央行施纳贝尔警告央行独立性受侵蚀](https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260507_1~d5ae988ece.en.html) ⭐️ 7.0/10

欧洲央行执行委员会委员伊莎贝尔·施纳贝尔发表讲话，指出央行独立性正在悄然受到侵蚀，危及货币政策效力和金融稳定，呼吁保持警惕。 欧洲央行高层的这一警告表明，政治压力和公众批评正日益威胁欧央行独立制定货币政策的能力，这可能导致欧元区市场的通胀预期、债券收益率和风险溢价上升。 演讲日期为 2026 年 5 月 7 日，可能讨论了财政主导、对央行行长的个人攻击以及通过立法限制货币政策工具等具体侵蚀渠道，但未提供确切细节。

rss · ECB Press Releases · May 7, 17:00

**背景**: 央行独立性是指货币政策应免受短期政治影响以维持价格稳定的原则。欧洲央行的独立性受《欧盟条约》保护，但自 2008 年金融危机及疫情后通胀期间，全球央行面临的压力日益增加。近期学术研究和国际货币基金组织的分析均确认，独立性对于低通胀和经济稳定至关重要，但正受到民粹主义运动和财政需求的威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Central_bank_independence">Central bank independence</a></li>
<li><a href="https://www.imf.org/en/news/articles/2024/06/17/sp061424-central-bank-independence">Central Bank Independence: Why It’s Needed and How to Protect It</a></li>
<li><a href="https://www.ecb.europa.eu/ecb/all-about-us/html/index.en.html">All about us | European Central Bank</a></li>

</ul>
</details>

**标签**: `#central-bank`, `#macroeconomics`, `#financial-stability`, `#europe`, `#global-markets`

---

<a id="item-7"></a>
## [联合国：无人机致苏丹内战平民死亡超八成](https://news.un.org/feed/view/en/story/2026/05/1167479) ⭐️ 6.0/10

联合国人权事务高级专员报告称，2026 年前四个月苏丹战争中超过 80%的平民死亡由武装无人机造成，至少 880 人丧生，并警告冲突可能进入更致命的阶段。 这一揭露可能加大国际社会对武器管控或制裁的外交压力，突显无人机使用升级和严重的平民伤亡，进而影响全球武装无人机扩散的政策。 具体而言，2026 年初无人机造成至少 880 名平民死亡，占所有平民死亡人数的 80%以上。联合国人权事务高级专员福尔克尔·蒂尔克警告，无人机进一步升级可能使冲突更为致命。

rss · UN News · May 11, 12:00

**背景**: 苏丹自 2023 年 4 月以来陷入苏丹武装部队与准军事快速支援部队之间的残酷内战，造成数万人死亡和全球最大的流离失所危机。武装无人机，包括外国支持者提供的无人机，已成为冲突的显著特征。联合国人权事务高级专员办事处（OHCHR）负责调查此类危机中的人权侵犯行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_High_Commissioner_for_Human_Rights">United Nations High Commissioner for Human Rights</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sudan_civil_war_(2023-present)">Sudan civil war (2023-present)</a></li>
<li><a href="https://dronewars.net/2024/02/13/proliferation-of-armed-drones-continues-apace-resulting-in-numerous-civilian-casualties/">Proliferation of armed drones continues apace resulting in numerous...</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#military-risk`, `#sovereign-risk`

---

<a id="item-8"></a>
## [联合国评估中东核能利弊](https://news.un.org/feed/view/en/story/2026/05/1167448) ⭐️ 6.0/10

联合国新闻发布分析文章，探讨中东国家日益增长的核能雄心，背景是近期冲突如 2025 年美伊冲突及俄罗斯在该地区不断扩大的核能外交。 核能扩张在动荡的中东可能引发安全困境，增加核扩散风险，并可能动摇全球能源市场；亦考验国际防核扩散机制并影响大国竞争。 分析未宣布新项目，但强调需强有力的安全规程和国际监督；指出沙特、埃及、土耳其等国正推进计划，而近期国际原子能机构报告显示伊朗的铀浓缩能力在增长。

rss · UN News · May 9, 12:00

**背景**: 自 2023 年中东危机以来，地区紧张局势升级，2025 年 6 月的十二日战争中以色列发动打击，美军空袭了伊朗核设施。俄罗斯在土耳其、埃及等国建造核电站，扩大影响力。国际核能合作框架（IFNEC）为和平核能合作提供渠道，而《不扩散核武器条约》（NPT）是全球防止核武器扩散的基石。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/International_Framework_for_Nuclear_Energy_Cooperation">International Framework for Nuclear Energy Cooperation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Iran_war">2026 Iran war - Wikipedia</a></li>
<li><a href="https://nationalinterest.org/feature/the-middle-east-nuclear-power-play-no-one-talking-about-13372">The Middle East Nuclear Power Play No One... - The National Interest</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#energy`, `#middle-east`

---

<a id="item-9"></a>
## [索马里饥饿危机加剧，濒临灾难边缘](https://news.un.org/feed/view/en/story/2026/05/1167473) ⭐️ 6.0/10

联合国紧急警告，索马里的饥饿危机并非遥远的威胁，而是一场正在迅速加深的现实灾难，危及生命与地区稳定。 这场危机可能破坏非洲之角的稳定，该地区对全球贸易航道至关重要；并引发紧急人道主义资金需求，同时可能加剧索马里的主权违约风险和地缘政治脆弱性。 联合国称局势正在实时发生且迅速恶化，暗示着一场与以往饥荒规模相当的灾难迫在眉睫，但未提供具体时间表或数据。

rss · UN News · May 8, 12:00

**背景**: 索马里历史上多次发生饥荒，最著名的是 2011 年导致超过 25 万人死亡的大饥荒。综合粮食安全阶段分类（IPC）系统将饥荒定义为极度缺乏食物，出现饥饿和死亡。索马里所在的非洲之角是一个地缘政治动荡的地区，拥有承载全球 12%贸易量的战略性海上通道（红海），其稳定与否关系到全球大国和供应链安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Integrated_Food_Security_Phase_Classification">Integrated Food Security Phase Classification - Wikipedia</a></li>
<li><a href="https://www.newsweek.com/stability-horn-africa-vital-global-trade-security-opinion-1998578">Stability in the Horn of Africa Is Vital to Global Trade and... - Newsweek</a></li>
<li><a href="https://www.un.org/unispal/wp-content/uploads/2024/03/IPC_Famine_Factsheet.pdf">IPC _ Famine _Factsheet</a></li>

</ul>
</details>

**标签**: `#diplomacy`, `#geopolitics`, `#sovereign-risk`, `#food-security`

---

<a id="item-10"></a>
## [黎巴嫩停火脆弱 以色列袭击不断](https://news.un.org/feed/view/en/story/2026/05/1167467) ⭐️ 6.0/10

周五，救援团队报告称，尽管存在脆弱的停火协议，以色列仍对黎巴嫩南部发动袭击，毁坏村庄并造成家庭流离失所。 以色列的持续打击有可能导致以黎冲突再度升级，威胁地区稳定，并加剧黎巴嫩的人道主义危机。 救援报告称南部村庄'完全无法辨认'，持续的杀戮和流离失所表明停火协议脆弱且缺乏有效执行。

rss · UN News · May 8, 12:00

**背景**: 黎巴嫩与以色列之间的停火协议在激烈跨境交火后达成，尤其针对冲突多发的黎巴嫩南部地区，该地历史上曾经历 2006 年战争。以往的停火常因间歇性袭击而受损，导致持续动荡。

**标签**: `#middle-east`, `#military-risk`, `#diplomacy`, `#geopolitics`

---