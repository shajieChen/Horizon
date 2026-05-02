---
layout: default
title: "Horizon Summary: 2026-05-02 (ZH)"
date: 2026-05-02
lang: zh
---

> From 31 items, 12 important content pieces were selected

---

1. [Ubuntu 服务器遭国家支持攻击，旨在阻止关键补丁发布](#item-1) ⭐️ 9.0/10
2. [WhatCable: 识别 USB-C 线缆能力的 macOS 菜单栏应用](#item-2) ⭐️ 8.0/10
3. [Flock 利用儿童体操房摄像头进行销售演示](#item-3) ⭐️ 8.0/10
4. [博客称 AI 用水量低于公众预期](#item-4) ⭐️ 8.0/10
5. [Spotify 添加验证徽章以区分人类艺术家与 AI](#item-5) ⭐️ 8.0/10
6. [TI-84 Evo 引入 ARM Cortex CPU，取代经典 z80](#item-6) ⭐️ 7.0/10
7. [信用卡易受暴力破解攻击](#item-7) ⭐️ 7.0/10
8. [“同性恋越狱”技术引发大模型安全辩论](#item-8) ⭐️ 7.0/10
9. [提出“内存墙”概念的莎莉·麦基去世](#item-9) ⭐️ 7.0/10
10. [新研究表明人们可以在梦中学习和解决问题](#item-10) ⭐️ 6.0/10
11. [末日预警系统追踪私人飞机检测精英逃离迹象](#item-11) ⭐️ 6.0/10
12. [Adobe 1991 年 PostScript 解释器在浏览器中运行](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Ubuntu 服务器遭国家支持攻击，旨在阻止关键补丁发布](https://arstechnica.com/security/2026/05/ubuntu-infrastructure-has-been-down-for-more-than-a-day/) ⭐️ 9.0/10

此次攻击可能导致 Ubuntu 系统无法针对 CopyFail 漏洞进行修补，该漏洞允许任何非特权本地用户自 2017 年以来在所有主要 Linux 发行版上获得 root 权限，对全球数百万台服务器和容器构成严重风险。 攻击专门针对 Ubuntu 的基础设施，包括软件包镜像和安全门户，以阻止补丁分发；CopyFail 漏洞的 CVSS 评分为 7.8，影响多租户环境，其中容器逃逸是一个值得关注的问题。

hackernews · RattlesnakeJake · May 1, 19:14

**背景**: CopyFail（CVE-2026-31431）是 Linux 写时复制机制中发现的高严重性本地权限提升漏洞，自 2017 年以来影响所有主要发行版。它允许非特权本地用户静默提升至 root 权限，使攻击者能够危害整个系统，包括容器主机。Ubuntu 是最流行的 Linux 发行版之一，其基础设施托管关键安全更新。旨在阻止访问这些更新的持续 DDoS 攻击将使许多系统在攻击平息或使用替代镜像机制之前保持脆弱状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/04/new-linux-copy-fail-vulnerability.html">New Linux 'Copy Fail' Vulnerability Enables Root Access on Major Distributions</a></li>
<li><a href="https://cybersecuritynews.com/pack2theroot-vulnerability/">Critical Pack2TheRoot Vulnerability Let Attackers Gain Root Access or Compromise the System</a></li>

</ul>
</details>

**社区讨论**: 一些评论者质疑攻击是否真的阻止了更新，指出 apt 镜像分布广泛。其他人提到攻击可能试图阻止对特定 CVE 页面的访问，并提供了手动缓解的说明。大家一致认为攻击者很可能是伊朗国家行为者，旨在通过阻止 CopyFail 漏洞的修补来最大化损害，该漏洞可轻松获得 root 权限。

**标签**: `#security`, `#Ubuntu`, `#infrastructure attack`, `#vulnerability`, `#DDoS`

---

<a id="item-2"></a>
## [WhatCable: 识别 USB-C 线缆能力的 macOS 菜单栏应用](https://github.com/darrylmorley/whatcable) ⭐️ 8.0/10

WhatCable 是一款新发布的开源 macOS 菜单栏应用，它直接从 Mac 的内置数据中读取 USB-C 线缆的能力——充电功率、数据传输速度、显示支持等。 这款应用解决了 USB-C 线缆外观相似难以区分的常见问题，无需额外硬件即可轻松识别线缆规格。它帮助用户在充电、数据传输或显示连接时选择正确的线缆。 该应用采用 Swift/SwiftUI 开发，开源免费且无追踪。它读取 USB-C 线缆内置的 e-marker 芯片数据，Mac 通过其 USB 控制器已可访问这些数据。

hackernews · sleepingNomad · May 1, 08:43

**背景**: USB-C 线缆外观常相似，但支持的能力却大相径庭，例如 5W 充电与 100W 充电及 Thunderbolt 4 的区别。每条合规的 USB-C 线缆内部都有一个 e-marker 芯片，存储着线缆的能力信息。macOS 可以通过系统信息应用或内置接口查询该芯片。WhatCable 自动完成此查询，并以友好的菜单栏界面呈现信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.totalphase.com/blog/2020/10/what-is-e-marker-how-does-it-work/">What is an E-Marker in a USB Type-C Cable and How Does It Work?</a></li>
<li><a href="https://www.macworld.com/article/612242/usb-c-thunderbolt-cables-speed-power.html">How the Mac can help untangle the USB-C cable conundrum | Macworld</a></li>
<li><a href="https://apple.stackexchange.com/questions/365708/is-there-a-way-to-easily-test-the-speed-and-power-capacity-of-a-usb-c-cable">hardware - Is there a way to easily test the speed and power capacity of a USB-C cable? - Ask Different</a></li>

</ul>
</details>

**社区讨论**: 社区反响非常积极，获得 401 分和 128 条评论。用户称赞开发者快速迭代（7 小时内发布了 16 个版本），并请求支持 Linux 和 KDE Plasma 平台。部分用户讨论了使用 GPT 生成 Plasmoid 的替代方案，还有用户提到 ChromeOS 中也有类似功能。

**标签**: `#USB-C`, `#macOS`, `#open source`, `#Swift`, `#utility`

---

<a id="item-3"></a>
## [Flock 利用儿童体操房摄像头进行销售演示](https://www.404media.co/city-learns-flock-accessed-cameras-in-childrens-gymnastics-room-as-a-sales-pitch-demo-renews-contract-anyway/) ⭐️ 8.0/10

据 404 Media 报道，Flock Safety 未经明确授权，访问了佐治亚州邓伍迪市一间儿童体操房的摄像头实时画面，用于进行销售演示。 这一事件凸显了一家监控技术公司严重的隐私和道德违规，引发了对滥用实时摄像头画面（尤其是涉及儿童的画面）以及公私监控合作缺乏监管的担忧。 邓伍迪市是 Flock 的“演示合作伙伴计划”的一部分，该计划允许特定员工使用实时数据演示新产品。尽管存在未经授权的访问，该市仍续签了与 Flock 的合同。

hackernews · joshcsimmons · May 1, 18:37

**背景**: Flock Safety 是一家向警察局和私人客户销售云连接摄像头和车牌读取器的公司，利用 AI 分析视频并与执法部门共享数据。该公司的系统通常部署在公共空间，但此次事件显示其扩展到儿童体操房等私人敏感区域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.aclu.org/news/privacy-technology/flock-roundup">Flock's Aggressive Expansions Go Far Beyond Simple Driver Surveillance | ACLU</a></li>

</ul>
</details>

**社区讨论**: 评论者质疑为什么 Flock 需要实时数据而非专用演示环境进行演示，并批评 YC 总裁 Garry Tan 为 Flock 辩护。其他人则对儿童区域的监控摄像头以及实时监控的正常化提出了更广泛的隐私担忧。

**标签**: `#privacy`, `#surveillance`, `#ethics`, `#tech`, `#Flock`

---

<a id="item-4"></a>
## [博客称 AI 用水量低于公众预期](https://californiawaterblog.com/2026/04/26/ai-water-use-distractions-and-lessons-for-california/) ⭐️ 8.0/10

加州水博客发表文章，认为 AI 的用水量相比农业和城市用水相对较小，公众担忧常基于误导性比较。 这一分析可能重新定义围绕 AI 的环境辩论，将注意力引向更大的用水户，并鼓励数据中心用水的透明报告。 博客使用 AI 生成的加州数据中心蒸发量估算，并指出数据中心可采用蒸发冷却或闭环系统，蒸发冷却更为耗水但节能。

hackernews · hirpslop · May 1, 17:18

**背景**: 数据中心需要冷却以防止服务器过热；传统方法会蒸发大量水。水使用效率（WUE）指标衡量效率。训练一次 GPT-3 约蒸发 70 万升清洁淡水，引发担忧。博客认为 AI 的总用水量相比其他行业仍然很小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vertiv.com/fr-ca/about/news-and-insights/articles/blog-posts/evolving-chilled-water-cooling-methods-for-slab-floor-data-centers/">Evolving Chilled Water Cooling System for Slab Floor Data Centers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Water_usage_effectiveness">Water usage effectiveness - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2304.03271">[2304.03271] Making AI Less "Thirsty": Uncovering and Addressing the Secret Water Footprint of AI Models</a></li>

</ul>
</details>

**社区讨论**: 评论者就 AI 用水与农业和卫生等必要用途比较的公平性展开辩论。一些人指出 AI 用水相对于牛肉生产微不足道，而另一些人则强调了谷歌用水给当地供水带来压力的案例。

**标签**: `#AI`, `#water usage`, `#environment`, `#sustainability`, `#data centers`

---

<a id="item-5"></a>
## [Spotify 添加验证徽章以区分人类艺术家与 AI](https://www.bbc.com/news/articles/c5yerr4m1yno) ⭐️ 8.0/10

Spotify 推出了“Verified by Spotify”验证徽章，用于标记艺术家资料，确认其为真实人类并符合真实性标准，旨在帮助听众区分人类创作的音乐与 AI 生成的内容。 此举回应了音乐领域对 AI 真实性的日益关切，帮助听众做出明智选择，并可能影响艺术家的署名和报酬方式。它为流媒体平台处理 AI 生成内容树立了先例。 要获得徽章，艺术家需在 Spotify 平台内外展示可辨识的存在，例如演唱会日期、商品和关联的社交媒体账户。徽章将显示在艺术家资料页面上。

hackernews · reconnecting · May 1, 16:42

**背景**: AI 生成的音乐在流媒体平台上日渐增多，引发了关于真实性和公平报酬的疑问。与以往的技术进步不同，AI 可以在没有直接人类创意的情况下模仿人类风格。Spotify 的验证系统旨在提供透明度，尽管检测工具仍不完善，且“人类”身份的标准可能无法涵盖所有细微差别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c5yerr4m1yno">Spotify adds 'Verified' badges to distinguish human artists from AI</a></li>
<li><a href="https://newsroom.spotify.com/2026-04-30/verified-by-spotify-badge-artist-details/">Introducing Verified by Spotify, a Signal of Authenticity and Trust for the Artists Behind the Music — Spotify</a></li>
<li><a href="https://techcrunch.com/2026/04/30/spotify-introduces-verified-artist-badges-to-help-distinguish-humans-from-ai/">Spotify introduces verified artist badges to help distinguish humans from AI | TechCrunch</a></li>

</ul>
</details>

**社区讨论**: 评论展现了不同观点：一些人质疑 AI 与人类创作之间的界限在哪里，而另一些人怀疑 Spotify 可能通过推荐 AI 音乐来避免支付艺术家报酬从而获利。还提到了代际差异，年轻用户可能更接受 AI 生成的内容。此外，有评论者批评当前 AI 音乐质量低劣且缺乏原创性。

**标签**: `#AI`, `#music`, `#Spotify`, `#verification`, `#authenticity`

---

<a id="item-6"></a>
## [TI-84 Evo 引入 ARM Cortex CPU，取代经典 z80](https://education.ti.com/en/products/calculators/graphing-calculators/ti-84-evo) ⭐️ 7.0/10

德州仪器 (TI) 的 TI-84 Evo 升级为运行在 156 MHz 的 ARM Cortex CPU，取代了使用超过 30 年的经典 z80 架构。相比之前型号的 48 MHz，处理能力提升了 3 倍。 从 z80 到 ARM Cortex 的转变标志着标志性 TI-84 系列的重大硬件演进，可能支持更先进的教育软件，并延长计算器在课堂中的使用寿命。这也标志着长期服役的 z80 架构在图形计算器中的终结。 ARM Cortex CPU 运行在 156 MHz，相比之前型号的 48 MHz eZ80 有了显著提升。这一改变打破了持续 30 多年的 z80 兼容性，可能影响现有的计算器程序和模拟器。

hackernews · thatxliner · May 1, 20:06

**背景**: TI-84 系列历史上一直使用 Zilog 的 z80 或 eZ80 CPU，最早可追溯到 1990 年推出的 TI-81。ARM Cortex 是一种现代 RISC 架构，广泛用于智能手机和嵌入式设备，提供更高的性能和能效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/List_of_ARM_processors">List of ARM processors - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ARM_architecture_family">ARM architecture family - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Z80_architecture">Z80 architecture</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些人分享在特殊情况下使用 TI 计算器的怀旧故事，而另一些人则批评学校强制购买昂贵计算器。少数人讨论了转向 ARM 的技术影响，指出可能存在兼容性问题。

**标签**: `#TI-84`, `#calculator`, `#ARM`, `#hardware`, `#retro`

---

<a id="item-7"></a>
## [信用卡易受暴力破解攻击](https://metin.nextc.org/posts/Credit_Cards_Are_Vulnerable_To_Brute_Force_Kind_Attacks.html) ⭐️ 7.0/10

一篇博客文章详细介绍了如何利用 Luhn 算法和银行识别码（BIN）等可预测模式，结合支付网关速率限制不足，对信用卡号码进行暴力破解。 此漏洞可能导致卡片枚举和欺诈，影响消费者和商户，并凸显了采用 3D 安全认证等更强身份验证以及支付处理器加强速率限制的必要性。 攻击利用 Luhn 算法进行校验和验证，并利用 BIN 前缀缩小有效卡号范围；然而，Stripe 等支付处理商会主动监控并处罚枚举尝试，且在 EMV 系统中，结算与授权是分离的。

hackernews · kodbraker · May 1, 20:26

**背景**: 信用卡号码遵循 ISO/IEC 7812 标准，前六位为银行识别码（BIN），后跟账号和 Luhn 校验位。Luhn 算法是一种简单的校验和，用于检测偶然错误，而非恶意篡改。暴力破解攻击尝试大量号码组合；速率限制和欺诈检测系统是常见的防御措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Luhn_algorithm">Luhn algorithm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bank_Identification_Number">Bank Identification Number</a></li>
<li><a href="https://docs.stripe.com/rate-limits">Rate limits | Stripe Documentation</a></li>

</ul>
</details>

**社区讨论**: 评论者指出结算与授权分离，限制了欺诈影响，且 Stripe 等支付处理商会处罚枚举行为。部分用户反映即使更换卡片后仍出现欺诈交易，而另一些用户则强调 3D 安全认证在地区性使用中作为保护层，但可能将责任转移给持卡人。

**标签**: `#security`, `#credit cards`, `#brute force`, `#payments`, `#cybersecurity`

---

<a id="item-8"></a>
## [“同性恋越狱”技术引发大模型安全辩论](https://github.com/Exocija/ZetaLib/blob/main/The%20Gay%20Jailbreak/The%20Gay%20Jailbreak.md) ⭐️ 7.0/10

一种名为“同性恋越狱”的新型 LLM 越狱技术已在 GitHub 上分享，声称结合其他技术时可以突破甚至像 o3 这样的模型的防护栏。 该技术凸显了 LLM 安全机制中持续存在的漏洞以及攻击者绕过防护栏的创意方式，强调了构建强健防御体系的必要性。 该技术据称通过链式组合已知的漏洞（如角色扮演和语言选择）来工作，但一些评论者认为“同性恋”因素并非核心。GitHub 仓库声称正确使用时理论上可以突破任何防护栏。

hackernews · bobsmooth · May 1, 16:59

**背景**: 大语言模型越狱技术是指旨在绕过大型语言模型安全过滤器的提示词。常见方法包括角色扮演、要求模型模拟 Linux 终端，或使用多轮攻击。该技术因涉及露骨内容而具有争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Exocija/ZetaLib/blob/main/The+Gay+Jailbreak/The+Gay+Jailbreak.md">ZetaLib/The Gay Jailbreak /The Gay Jailbreak .md at main...</a></li>
<li><a href="https://www.anthropic.com/research/many-shot-jailbreaking">Many-shot jailbreaking - Anthropic</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了该技术的有效性，有人将其归因于角色扮演或语言选择而非露骨内容。其他人指出作者给出的“为什么有效”的解释有趣但肤浅。一条评论幽默地引用了《绝命毒师》。

**标签**: `#LLM safety`, `#jailbreak`, `#prompt engineering`, `#Hacker News discussion`

---

<a id="item-9"></a>
## [提出“内存墙”概念的莎莉·麦基去世](https://www.online-tribute.com/SallyMcKee) ⭐️ 7.0/10

计算机科学家莎莉·麦基去世，她曾提出对计算机体系结构影响深远的术语“内存墙”。她的死讯通过在线悼念页面公布。 “内存墙”这一术语在揭示 CPU 速度与内存延迟之间日益扩大的差距方面具有基础性作用，影响了数十年来计算机体系结构和系统的研究方向。随着这一差距持续推动内存技术和处理器设计的创新，麦基的贡献至今仍具有重要意义。 麦基于 1995 年合著了开创性论文《遭遇内存墙：显而易见的启示》（ACM DOI: 10.1145/216585.216588）。她拥有计算机科学博士学位，并作为流动教授经历了漫长的学术生涯。

hackernews · deater · May 1, 14:45

**背景**: 内存墙指的是 CPU 速度与内存速度之间日益扩大的差距，即内存延迟无法跟上处理器性能提升的步伐。这一概念在计算机体系结构中至关重要，推动了内存层次结构、缓存以及新型内存技术的研究。随机存取存储器（RAM）是一种允许按任意顺序读写数据的数据存储形式，通常采用 DRAM 等易失性存储。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Memory_wall">Memory wall</a></li>
<li><a href="https://en.wikipedia.org/wiki/Random-access_memory">Random-access memory - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区表达了敬意和哀悼，许多人表示此前并不知道麦基是该术语的提出者。一位评论者指出她的悼念页面中有一个“Memory Wall”链接用于分享回忆，另一人则感叹虽然以内存墙概念为基础撰写了论文，却未曾听说过她。

**标签**: `#memory wall`, `#computer architecture`, `#obituary`, `#Sally McKee`, `#CS pioneer`

---

<a id="item-10"></a>
## [新研究表明人们可以在梦中学习和解决问题](https://www.newyorker.com/culture/annals-of-inquiry/its-possible-to-learn-in-our-sleep-should-we) ⭐️ 6.0/10

这项研究可能彻底改变我们对待学习和解决问题的方式，表明睡眠不仅仅是休息，而是一种可以被利用的活跃认知状态。它可能带来加速学习和增强创造力的新技术。 文章重点介绍了实验证据和轶事报告，显示人们在梦中获得见解或练习技能，但确切机制仍不清楚。研究人员正在探索梦境交流如何运作，但许多问题尚未解答。

hackernews · XzetaU8 · May 1, 17:47

**背景**: 长期以来，人们已知睡眠在记忆巩固中发挥作用，但关于梦中主动学习或交流的想法更具争议。清醒梦（做梦者意识到自己在做梦）已被研究用于可能的技能练习。这项研究突破了睡眠期间被认为可能实现的界限。

**社区讨论**: 社区成员分享了在梦中解决编程错误和数学问题的个人经历，支持了研究声称。一些人表达了对于梦中个体之间如何交流的好奇，指出文章仅简要提及这一方面。

**标签**: `#sleep-learning`, `#dreaming`, `#problem-solving`, `#neuroscience`

---

<a id="item-11"></a>
## [末日预警系统追踪私人飞机检测精英逃离迹象](https://ews.kylemcdonald.net/) ⭐️ 6.0/10

该网站通过 ADS-B 数据实时监控私人飞机活动，旨在发现异常飞行模式，这可能表明富裕阶层正因预感末日来临而逃离。 它反映了社会焦虑以及对公开数据的投机性使用，但同时受到数据偏差和滞后指标的局限。 系统使用来自 Flightradar24 等来源的 ADS-B 聚合数据，但大多数追踪到的飞机位于美国，这可能反映的是数据可用性而非实际活动。

hackernews · carlsborg · May 1, 16:21

**背景**: ADS-B（自动相关监视-广播）是一种广播飞机位置的技术，可实现实时追踪。Flightradar24 是一个主要服务，通过全球接收器网络聚合 ADS-B 数据进行飞行追踪。私人飞机常被富裕人士用于旅行，但将其用于末日预测是投机性的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_Dependent_Surveillance–Broadcast">Automatic Dependent Surveillance–Broadcast - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Flightradar24">Flightradar24</a></li>

</ul>
</details>

**社区讨论**: 评论包括：对网站并非 AI 生成的欣慰，提及一个 2007 年的类似项目，批评其是滞后指标，质疑在末日场景中飞行员可能关闭应答器，以及关于数据偏向美国的问题。

**标签**: `#private jets`, `#data visualization`, `#early warning`, `#speculation`, `#apocalypse`

---

<a id="item-12"></a>
## [Adobe 1991 年 PostScript 解释器在浏览器中运行](https://www.pagetable.com/?p=1854) ⭐️ 6.0/10

一篇博文展示了如何通过 Emscripten 将 Adobe 最初于 1991 年发布的 PostScript 解释器编译为 WebAssembly，并在网页浏览器中运行。 这一复古计算成果复活了历史上的软件作品，让用户无需模拟器即可在现代浏览器中直接执行经典的 PostScript 文件。它展示了 WebAssembly 在保存遗留软件方面的强大能力和可移植性。 该解释器可能通过 Emscripten 编译，Emscripten 是一个基于 LLVM 的工具链，可将 C/C++代码转换为 WebAssembly。虽然可能不支持所有 PostScript 特性，但社区测试显示许多文件可以正常工作，仅缺少部分颜色渲染。

hackernews · ingve · May 1, 11:58

**背景**: PostScript 是 Adobe 在 20 世纪 80 年代开发的一种页面描述语言，广泛用于打印和桌面出版。WebAssembly（Wasm）是一种低级二进制格式，能在浏览器中以接近原生速度运行代码。Emscripten 是一个编译器，可将 C/C++应用移植到 WebAssembly，使得像 PostScript 解释器这样的遗留软件能够在网络上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Emscripten">Emscripten</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>

</ul>
</details>

**社区讨论**: 评论者表现出热情，有人分享了 PostScript 参考手册和测试文件的链接。另一些人感叹最新 macOS 版本丢失了 PostScript 支持。关于 502 错误的幽默评论表明兴趣很高。一位用户讨论了为网络应用编译 jbig2 解码器为 Wasm，展示了更广泛的关联性。

**标签**: `#PostScript`, `#browser`, `#retrocomputing`, `#interpreter`, `#Adobe`

---