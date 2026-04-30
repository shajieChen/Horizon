---
layout: default
title: "Horizon Summary: 2026-04-30 (ZH)"
date: 2026-04-30
lang: zh
---

> From 35 items, 20 important content pieces were selected

---

1. [Zed 1.0 发布：高性能 Rust 代码编辑器](#item-1) ⭐️ 8.0/10
2. [Linux 内核 AF_ALG 严重漏洞 CVE-2026-31431](#item-2) ⭐️ 8.0/10
3. [开源听诊器生产成本仅需 2.5 至 5 美元](#item-3) ⭐️ 8.0/10
4. [Ramp Sheets AI 漏洞导致数据泄露](#item-4) ⭐️ 8.0/10
5. [提案：通过联合代码锻造厂消除供应商锁定](#item-5) ⭐️ 8.0/10
6. [京都樱花盛开日期创 1200 年来最早](#item-6) ⭐️ 8.0/10
7. [在线年龄验证：隐私战场](#item-7) ⭐️ 8.0/10
8. [Mistral 发布 120B 稠密模型 Medium 3.5](#item-8) ⭐️ 8.0/10
9. [LLM 0.32a0 引入基于消息的模型重构](#item-9) ⭐️ 8.0/10
10. [OpenAI 扩大 Stargate 基础设施以支持 AGI](#item-10) ⭐️ 8.0/10
11. [OpenAI 提出人工智能驱动网络安全计划](#item-11) ⭐️ 8.0/10
12. [AI 评估正成为新计算瓶颈](#item-12) ⭐️ 8.0/10
13. [IBM Granite 4.1 大模型：架构与训练详解](#item-13) ⭐️ 8.0/10
14. [HERMES.md 漏洞导致 Claude Code 额外计费](#item-14) ⭐️ 7.0/10
15. [FastCGI 作为反向代理协议优于 HTTP](#item-15) ⭐️ 7.0/10
16. [作者为什么偏爱 Lisp 和 Scheme 而非 Haskell](#item-16) ⭐️ 7.0/10
17. [马里兰州禁止杂货店监控定价](#item-17) ⭐️ 7.0/10
18. [从打印件转录的 DOS 1.0 源代码](#item-18) ⭐️ 7.0/10
19. [荷兰政府软启动开源代码平台](#item-19) ⭐️ 7.0/10
20. [OpenTrafficMap：低成本 V2X 交通可视化](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Zed 1.0 发布：高性能 Rust 代码编辑器](https://zed.dev/blog/zed-1-0) ⭐️ 8.0/10

基于 Rust 的代码编辑器 Zed 已达到 1.0 里程碑，标志着其经过大量开发后正式稳定发布。 Zed 1.0 代表了新一代利用 Rust 等现代系统编程语言的高性能编辑器，相比传统编辑器提供更快的启动和编辑体验。它可能挑战 Sublime Text 和 VS Code 等成熟编辑器。 该编辑器是开源的，用 Rust 构建，支持 Linux、macOS 和 Windows。然而，其许可协议中关于数据使用权的条款引发了担忧。

hackernews · salkahfi · Apr 29, 14:34

**背景**: Zed 是一个用 Rust 编写的高性能多人代码编辑器，最初以早期访问形式发布，后达到 1.0。Rust 是一种以内存安全和高性能著称的系统编程语言，非常适合构建能够高效处理大型代码库的快速编辑器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zed_(text_editor)">Zed (text editor ) - Wikipedia</a></li>
<li><a href="https://zed.dev/">Zed — Love your editor again</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人称赞 Zed 的性能和创新，另一些人则批评其关于客户数据的许可条款。有用户指出抱怨很常见，但 Zed 的技术是突破性的。另一位用户出于兼容性问题在对旧项目时更偏爱 Sublime Text。

**标签**: `#zed`, `#code editor`, `#rust`, `#release`, `#software`

---

<a id="item-2"></a>
## [Linux 内核 AF_ALG 严重漏洞 CVE-2026-31431](https://copy.fail/) ⭐️ 8.0/10

一个名为 Copy Fail 的 Linux 内核 AF_ALG 严重漏洞（CVE-2026-31431）允许非特权用户通过仅 732 字节的利用代码获取 root 权限。Red Hat、Debian 和 Ubuntu 等厂商将其评为中等严重性并推迟修复，引发了社区不满。 该漏洞可在所有主流 Linux 发行版上实现可靠的本地权限提升至 root，无需竞态条件或内核特定偏移。它凸显了 AF_ALG 接口的内在危险，该接口向非特权用户空间暴露了巨大的攻击面。 该漏洞利用是直线逻辑缺陷，既不需要竞态条件也不依赖内核特定偏移；缓解措施包括通过 modprobe 配置禁用 algif_aead 内核模块。该漏洞源于 AF_ALG 套接字类型，它将内核加密例程暴露给非特权用户。

hackernews · unsnap_biceps · Apr 29, 18:13

**背景**: AF_ALG 是 Linux 内核自 2.6.38 版本引入的套接字接口，允许用户空间程序访问内核加密操作。它被认为复杂且几乎不必要，因为用户空间已有自己的加密库。CVE-2026-31431 是 AF_ALG 在 AEAD（带关联数据的认证加密）处理中的权限提升漏洞，由 Xint 的研究人员发现，并命名为“Copy Fail”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-31431">NVD - CVE - 2026 - 31431</a></li>
<li><a href="https://github.com/painoob/Copy-Fail-Exploit-CVE-2026-31431">GitHub - painoob/Copy-Fail- Exploit - CVE - 2026 - 31431 : Most Linux...</a></li>

</ul>
</details>

**社区讨论**: 一位从事内核加密代码的开发者对 AF_ALG 漏洞反复出现表示沮丧，称该接口不必要且过于复杂。社区成员指出厂商低估了严重性，Red Hat 将其标记为“中等”并“推迟修复”，同时提到披露过程中存在混乱。还有评论者指出，在受影响系统上以普通用户身份运行自主 AI 代理存在风险。

**标签**: `#security`, `#linux`, `#kernel`, `#cve`, `#exploit`

---

<a id="item-3"></a>
## [开源听诊器生产成本仅需 2.5 至 5 美元](https://github.com/GliaX/Stethoscope) ⭐️ 8.0/10

一个全新的开源听诊器设计已在 GitHub 上发布，生产成本仅需 2.5 至 5 美元，使得低资源地区也能负担得起。 这种低成本设计有潜力改善医疗服务不足地区的医疗诊断，因为传统听诊器价格过高。 该听诊器专为 3D 打印设计，并采用易于获取的材料，但部分社区成员质疑其声学性能是否能与专业型号媲美。

hackernews · 0x54MUR41 · Apr 29, 14:47

**背景**: 传统听诊器价格可能超过 100 美元，使许多发展中国家的诊所难以负担。此类开源硬件项目旨在通过提供可自由获取且可本地制造的设计，推动医疗工具的普及。

**社区讨论**: 社区评论对声学频率响应图表示怀疑，认为其与专业听诊器匹配得过于完美。有用户指出，7 美元就能买到便宜的金属听诊器；另有人分享了研究人员解释该项目动机的采访。

**标签**: `#open-source`, `#healthcare`, `#hardware`, `#stethoscope`, `#3D-printing`

---

<a id="item-4"></a>
## [Ramp Sheets AI 漏洞导致数据泄露](https://www.promptarmor.com/resources/ramps-sheets-ai-exfiltrates-financials) ⭐️ 8.0/10

Ramp 的 Sheets AI 中存在一个提示注入漏洞，攻击者可以通过注入恶意指令来窃取敏感的财务数据。该漏洞由 PromptArmor 负责任地披露，据称 Ramp 已在 2026 年 5 月 16 日修复。 该漏洞展示了执行自然语言指令的 AI 代理如何重新引入经典安全风险，尤其是在处理敏感财务数据时。它凸显了在基于 LLM 的应用中实施强输入验证和代理隔离的紧迫性。 该攻击利用了提示注入，对抗性文本诱骗 AI 执行未经授权的操作，例如窃取电子表格数据。PromptArmor 需联系 Ramp 三次才收到回复，披露中的修复日期（2026 年 5 月 16 日）可能是 3 月的笔误。

hackernews · takira · Apr 29, 17:44

**背景**: 提示注入是一种漏洞，攻击者通过精心构造的输入覆盖或修改 AI 模型的指令，类似于 SQL 注入。Ramp Sheets 是一款面向财务团队的 AI 驱动电子表格工具，集成大语言模型以自动化任务。随着 LLM 代理访问敏感数据，提示注入成为关键安全问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/prompt-injection">What Is a Prompt Injection Attack? | IBM</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>
<li><a href="https://labs.ramp.com/sheets">Ramp Sheets</a></li>

</ul>
</details>

**社区讨论**: 评论指出一个讽刺现象：经过数十年防止任意代码执行的努力，AI 代理现在却天真地将任意数据作为指令执行。用户对 Ramp 的反应迟缓及修复日期表示怀疑，还有人质疑 Ramp 为何要开发电子表格产品。

**标签**: `#security`, `#AI`, `#prompt injection`, `#vulnerability`, `#Ramp`

---

<a id="item-5"></a>
## [提案：通过联合代码锻造厂消除供应商锁定](https://blog.tangled.org/federation/) ⭐️ 8.0/10

一篇题为《我们需要一个联合的代码锻造厂网络》的博客文章提出建立一个类似于电子邮件或 Mastodon 的联合代码锻造厂网络，以减少代码托管中的供应商锁定和中心化。 该提案针对 GitHub 等单一平台日益占据主导地位的现状，通过促进竞争和互操作性，减少对任何单一提供商的依赖，从而使整个开源生态系统受益。 帖子强调了去联邦化、政治争议以及在缺乏风险投资的情况下启动困难等挑战，而现有的 Like ForgeFed 等项目已经在跨 Forgejo 实例联合仓库星标等功能。

hackernews · icy · Apr 29, 14:00

**背景**: 代码锻造厂是像 GitHub 和 GitLab 这样基于网页的平台，用于托管源代码并提供协作工具。联邦化（如电子邮件和 Mastodon 所示）允许独立实例在没有中心控制的情况下互操作，但将其应用于锻造厂涉及复杂的技术和社会障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forge_(software)">Forge (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo - Wikipedia</a></li>
<li><a href="https://nlnet.nl/project/Federated-Forgejo/">NLnet; Federated software forges with Forgejo</a></li>

</ul>
</details>

**社区讨论**: 社区评论对重复 Mastodon 的问题（去联邦化、无意义的争论）表示怀疑，但也支持竞争并希望得到有意义的采纳。一些人提到了替代方案，如 AT Protocol 或 Fossil 的集成模型。

**标签**: `#federation`, `#open source`, `#forges`, `#GitHub alternative`, `#decentralization`

---

<a id="item-6"></a>
## [京都樱花盛开日期创 1200 年来最早](https://jivx.com/kyoto-bloom) ⭐️ 8.0/10

历史记录显示，2021 年京都樱花于 3 月 26 日达到盛开高峰，这是 1200 多年有记录以来最早的一次。 这一独特的长期数据集为气候变化对物候学的影响提供了确凿证据，影响了生态系统、农业以及赏樱等文化活动。 该记录基于可追溯到公元 812 年的数据，是世界上连续时间最长的物候记录之一。花期提前主要归因于全球变暖导致的春季气温升高。

hackernews · momentmaker · Apr 29, 19:32

**背景**: 物候学是研究季节性生物事件（如开花和迁徙）的学科。樱花盛开日期对温度非常敏感，因此历史记录可作为过去气候的代用指标。京都樱花记录是气候科学中著名的基准之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ourworldindata.org/grapher/date-of-the-peak-cherry-tree-blossom-in-kyoto">Day of the year with peak cherry tree blossom in Kyoto, Japan - Our World in Data</a></li>
<li><a href="https://www.bbc.com/news/world-asia-56574142">Japan's cherry blossom 'earliest peak since 812'</a></li>
<li><a href="https://en.wikipedia.org/wiki/Phenology">Phenology</a></li>

</ul>
</details>

**社区讨论**: 评论者对这份 1200 年的数据集表示惊叹，并对花期迅速提前感到担忧。有人注意到自家花园的花期也提前了，另一用户提供了原始数据链接。少数人质疑主流媒体为何减少了对气候变化的报道。

**标签**: `#climate change`, `#cherry blossoms`, `#historical data`, `#Kyoto`, `#environmental impact`

---

<a id="item-7"></a>
## [在线年龄验证：隐私战场](https://x.com/GlennMeder/status/2049088498163216560) ⭐️ 8.0/10

一则引发热议的社交媒体帖子认为，强制在线年龄验证会对匿名性和隐私构成不可接受的风险，该帖获得超过 700 个点赞和 458 条评论。 这场讨论触及保护未成年人上网与维护公民自由之间的根本矛盾，对全球互联网治理和身份系统的工程设计具有深远影响。 讨论的关键方法包括 RTA 标头、信用卡检查、照片 ID 匹配以及保护隐私的零知识证明系统；评论者警告，广泛的年龄监控可能使身份欺诈和监控常态化。

hackernews · Cider9986 · Apr 29, 15:49

**背景**: 在线年龄验证是一种限制访问年龄敏感内容的机制，常由英国《在线安全法》等法律强制要求。常见方法从简单的自我声明到生物特征检查不等，但隐私倡导者认为许多方法破坏了匿名性，并可能导致敏感数据集中化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c1k81lj8nvpo">Online Safety Act: Which sites will require UK age verification ?</a></li>
<li><a href="http://newamerica.org/oti/briefs/exploring-privacy-preserving-age-verification/">Exploring Privacy-Preserving Age Verification: A Close Look at Zero-Knowledge Proofs</a></li>
<li><a href="https://www.cs.columbia.edu/~smb/papers/age-verify.pdf">Privacy-Preserving Age Verification—and Its Limitations Steven M. Bellovin *</a></li>

</ul>
</details>

**社区讨论**: 评论者强烈反对强制年龄验证，认为应由父母负责，青少年总会绕过限制，且这种做法会增加身份欺诈。有人主张采用匿名凭证系统或 RTA 标头等保护隐私的替代方案，但怀疑政策制定者因隐藏的监控动机而不会采纳。

**标签**: `#age verification`, `#privacy`, `#internet governance`, `#anonymity`, `#parental controls`

---

<a id="item-8"></a>
## [Mistral 发布 120B 稠密模型 Medium 3.5](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5) ⭐️ 8.0/10

Mistral AI 发布了 Mistral Medium 3.5，这是一个拥有 1200 亿参数的稠密模型，在 Q4 量化下仅需约 70GB 显存即可运行，比许多更大的模型更易部署。 该模型表明，较小的稠密模型能与更大的 MoE 模型竞争，降低了本地运行高性能 LLM 的硬件门槛，为开发者和研究人员提供了更广泛的访问机会。 Mistral Medium 3.5 是一个 120B 稠密模型，意味着每个 token 所有参数都会激活，这与仅使用子集的混合专家模型不同。这使得每参数显存效率更高，但推理速度比稀疏模型慢。

hackernews · meetpateltech · Apr 29, 15:17

**背景**: 稠密大语言模型为每个输入激活所有参数，计算负载均匀但每次推理所需内存更多。相比之下，混合专家（MoE）模型将 token 路由到专门的子网络，生成速度更快，但峰值内存更高且部署更复杂。Mistral Medium 3.5 是其模型系列的一部分，该系列还包括 7B 和 Large 模型，旨在平衡性能与可访问性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://maxkruse.github.io/vitepress-llm-recommends/model-types/dense/">Dense Models | AI Model Guide</a></li>
<li><a href="https://huggingface.co/mistralai/Mistral-7B-v0.1">mistralai/ Mistral -7B-v0.1 · Hugging Face</a></li>
<li><a href="https://maximilian-schwarzmueller.com/articles/understanding-mixture-of-experts-moe-llms/">Mixture of Experts (MoE) vs Dense LLMs</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些人称赞该模型的显存效率和竞争力，而另一些人指出，像 DeepSeek v4 Flash（量化为 2 比特）这样的模型在消费级硬件上运行更快，是强劲的替代品。此外，还有人讨论 Mistral 严格的内容安全策略头限制了网络测试。

**标签**: `#AI`, `#language models`, `#Mistral`, `#open-source`

---

<a id="item-9"></a>
## [LLM 0.32a0 引入基于消息的模型重构](https://simonwillison.net/2026/Apr/29/llm/#atom-everything) ⭐️ 8.0/10

LLM 0.32a0 是一个 alpha 版本，将核心抽象从提示-响应重构为基于消息的模型，支持输入为消息序列，输出为类型化部分流，同时保持完全向后兼容。 这次重构显著提升了 LLM 表示现代 LLM 能力（如多模态输入、结构化输出和工具调用）的能力，惠及其广泛的插件生态系统以及依赖它作为统一接口来访问各种模型的数千名用户。 两个关键变化是：模型输入现在可以表示为对话消息序列，模型响应可以由不同类型的部分（例如文本、图像、工具调用）流组成。该版本是 alpha 版本，意味着是实验性的，但旨在测试后达到稳定 API。

rss · Simon Willison · Apr 29, 19:01

**背景**: LLM 是由 Simon Willison 创建的 CLI 工具和 Python 库，通过插件系统为数百个大型语言模型提供统一接口。最初设计用于简单的文本提示和响应，随着时间的推移，它已演变为支持附件（图像、音频、视频）、通过模式的结构化 JSON 输出以及工具调用。这次重构调整了核心抽象，以更好地匹配现代 LLM 的通信方式——通过消息序列和类型化响应流——这已经是 OpenAI 的 Chat Completions 等主要 API 的标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2025/May/27/llm-tools/">Large Language Models can run tools in your terminal with LLM 0.26</a></li>
<li><a href="https://uuithub.com/simonw/llm">GitHub simonw/ llm LLM Context</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Python`, `#refactor`, `#CLI tool`, `#AI`

---

<a id="item-10"></a>
## [OpenAI 扩大 Stargate 基础设施以支持 AGI](https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age) ⭐️ 8.0/10

OpenAI 宣布扩建 Stargate 项目，增加新的数据中心容量，为通用人工智能（AGI）构建计算基础设施。 这项大规模基础设施投资标志着对 AGI 发展的重大承诺，并使美国处于 AI 基础设施创新的前沿。 Stargate 项目计划在四年内投入 5000 亿美元，在美国各地建设 AI 基础设施，该项目于 2025 年 1 月与软银、甲骨文等合作伙伴共同宣布。

rss · OpenAI Blog · Apr 29, 15:00

**背景**: AGI 是一种理论上能够匹配或超越人类在所有认知任务上的智能的 AI 类型。Stargate 项目是一项专门为 OpenAI 的 AGI 研究创造必要计算能力的举措，反映了先进 AI 模型对计算资源的巨大需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/announcing-the-stargate-project/">Announcing The Stargate Project | OpenAI</a></li>
<li><a href="https://www.linkedin.com/pulse/stargate-project-500-billion-leap-ai-infrastructure-shiva-bhavani-qgghc">Stargate Project: A $500 Billion Leap in AI Infrastructure</a></li>
<li><a href="https://introl.com/blog/openai-stargate-500-billion-ai-infrastructure-2025">What $500 billion in AI infrastructure actually looks like | Introl Blog</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#AGI`, `#data centers`, `#compute scaling`, `#OpenAI`

---

<a id="item-11"></a>
## [OpenAI 提出人工智能驱动网络安全计划](https://openai.com/index/cybersecurity-in-the-intelligence-age) ⭐️ 8.0/10

这家领先的人工智能组织提出的这一方案标志着网络安全领域向攻防两端使用人工智能的战略转变，可能影响全球政策和私营部门的实践。 该计划强调普及人工智能防御工具的获取、保护电网等关键系统，并促进国际合作。它建立在 OpenAI 此前发布的《智能时代产业政策》框架之上。

rss · OpenAI Blog · Apr 29, 04:00

**背景**: “智能时代”是 OpenAI 用来形容人工智能变得像电力一样具有变革性的时代的术语。网络安全威胁日益复杂，人工智能可以同时增强攻击和防御。OpenAI 的计划旨在确保人工智能有利于安全而非破坏安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cdn.openai.com/pdf/561e7512-253e-424b-9734-ef4098440601/Industrial+Policy+for+the+Intelligence+Age.pdf">[PDF] Industrial Policy for the Intelligence Age: Ideas to Keep People First</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI safety`, `#OpenAI`, `#policy`, `#critical infrastructure`

---

<a id="item-12"></a>
## [AI 评估正成为新计算瓶颈](https://huggingface.co/blog/evaleval/eval-costs-bottleneck) ⭐️ 8.0/10

Hugging Face 的一篇博文指出，评估 AI 模型的成本和时间成本正在急剧上升，逐渐成为与训练并列的新的计算瓶颈。 这意味着评估（而不仅仅是训练）将成为制约 AI 发展速度的因素，可能因资源被测试环节占用而拖慢研究与应用进程。 该文指出，为大模型运行完整的评估套件可能需要数万 GPU 小时，其成本已可媲美训练较小模型的开销。

rss · Hugging Face Blog · Apr 29, 16:45

**背景**: 在 AI 开发中，模型训练长期以来是主要计算瓶颈，而评估（在基准上测试模型）常被认为是次要成本。随着模型规模扩大，评估需要在多个基准上运行许多复杂任务，每项都需大量计算。这一趋势使得评估成为研究人员必须规划的重要成本因素。

**标签**: `#AI`, `#evaluation`, `#compute bottleneck`, `#machine learning`, `#efficiency`

---

<a id="item-13"></a>
## [IBM Granite 4.1 大模型：架构与训练详解](https://huggingface.co/blog/ibm-granite/granite-4-1) ⭐️ 8.0/10

IBM 发布了 Granite 4.1 系列，包含 3B、8B 和 30B 三种规模的稠密解码器大语言模型，使用约 15T 词元进行多阶段预训练，并支持长达 512K 词元的上下文扩展。 此次发布展示了 IBM 在高效、企业级大语言模型方面的持续投入，这些模型在不依赖长思维链的情况下具备有竞争力的指令遵循和工具调用能力，这对生产环境中的可预测延迟至关重要。 这些模型采用纯解码器稠密 Transformer 架构，包含分组查询注意力 (GQA)、旋转位置嵌入 (RoPE)、SwiGLU 激活函数、RMSNorm 以及共享输入输出嵌入。

rss · Hugging Face Blog · Apr 29, 15:01

**背景**: 大语言模型 (LLM) 是基于海量文本数据训练的人工智能模型，能够生成类人文本。IBM 的 Granite 系列面向企业应用场景，Granite 4.1 在 Granite 4.0 的混合 Mamba/Transformer 架构基础上，回归了稠密 Transformer 设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/ibm-granite/granite-4-1">Granite 4 . 1 LLMs: How They’re Built</a></li>
<li><a href="https://research.ibm.com/blog/granite-4-1-ai-foundation-models">Introducing the IBM Granite 4.1 family of models - IBM Research</a></li>
<li><a href="https://www.ibm.com/granite">Granite - IBM</a></li>

</ul>
</details>

**标签**: `#large language models`, `#IBM`, `#AI`, `#model architecture`, `#training`

---

<a id="item-14"></a>
## [HERMES.md 漏洞导致 Claude Code 额外计费](https://github.com/anthropics/claude-code/issues/53262) ⭐️ 7.0/10

Anthropic 的 Claude Code 存在一个漏洞，当提交信息包含 'HERMES.md' 时，会将请求路由到额外使用量计费，导致意外收费。Anthropic 后来宣布为受影响用户提供全额退款和额外使用额度。 此事件凸显了流行 AI 开发者工具中严重的计费完整性问题，削弱了用户信任。同时也表明 SaaS 公司制定稳健退款政策和快速社区响应的重要性。 该漏洞会在任何包含 'HERMES.md' 字符串的提交信息上触发，导致意外的额外收费。Anthropic 最初以不补偿技术错误的政策为由拒绝退款，但在社区压力下后来改变了立场。

hackernews · homebrewer · Apr 29, 18:54

**背景**: Claude Code 是 Anthropic 的智能编码工具，可帮助开发者编写代码、运行命令和管理 git 工作流。HERMES.md 是与 Hermes 代理项目相关的文件，该项目可以将任务委托给 Claude Code。该漏洞可能源于 Claude Code 计费路由解析提交信息的方式，将 'HERMES.md' 视为特殊触发器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NousResearch/hermes-agent/blob/main/skills/autonomous-ai-agents/claude-code/SKILL.md">hermes-agent/skills/autonomous-ai-agents/claude-code/SKILL.md at main · NousResearch/hermes-agent</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-claude-code">Claude Code — Delegate coding to Claude Code CLI (features, PRs) | Hermes Agent</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 Anthropic 最初拒绝为其自身技术错误退款表示愤怒，称这在合法企业中前所未有。在 Anthropic 的 Thariq 宣布全额退款和信用额度后，情绪转为谨慎的赞赏，但一些用户报告支持问题仍未解决。

**标签**: `#bug`, `#billing`, `#Claude Code`, `#Anthropic`, `#AI tools`

---

<a id="item-15"></a>
## [FastCGI 作为反向代理协议优于 HTTP](https://www.agwa.name/blog/post/fastcgi_is_the_better_protocol_for_reverse_proxies) ⭐️ 7.0/10

一篇博客文章指出，由于开销更低且设计更简洁，FastCGI 作为反向代理协议优于 HTTP。社区讨论补充了历史背景，并提及了 SCGI 和 WAS 等替代协议。 这挑战了在反向代理中广泛使用 HTTP 的做法，可能为 Web 服务器架构带来性能提升。同时，它也揭示了协议复杂性与简便性之间的权衡，这一权衡影响着实际应用中的选择。 FastCGI 使用带有复用的二进制协议，避免了 HTTP 头部解析的开销，但缺乏对 WebSocket 等现代特性的支持。SCGI 是一种更简单的替代方案，旨在更容易解析；而 WAS 引入了控制套接字和管道，以实现高效的数据传输。

hackernews · agwa · Apr 29, 16:16

**背景**: FastCGI 是 Web 服务器与应用服务器通信的协议，通过支持持久进程改进了 CGI。它常用于 Nginx 和 PHP-FPM，以实现高性能 Web 应用。SCGI（简单通用网关接口）是一种类似的协议，设计上比 FastCGI 更易于解析；而 WAS（Web 应用套接字）则引入了控制套接字和管道，支持 splice()操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitalocean.com/community/tutorials/understanding-and-implementing-fastcgi-proxying-in-nginx">Understanding and Implementing FastCGI Proxying in... | DigitalOcean</a></li>
<li><a href="https://en.wikipedia.org/wiki/Simple_Common_Gateway_Interface">Simple Common Gateway Interface - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍同意文章的观点，但指出 HTTP 因其简单性和普遍性而胜出。一些人倡导 WAS 作为进一步的改进，赞赏其使用 splice()实现零拷贝数据传输。另一些人则对客户端 IP 转发中自定义 HTTP 头部的泛滥表示不满。

**标签**: `#FastCGI`, `#reverse proxy`, `#web protocols`, `#HTTP`, `#SCGI`

---

<a id="item-16"></a>
## [作者为什么偏爱 Lisp 和 Scheme 而非 Haskell](https://jointhefreeworld.org/blog/articles/lisps/why-i-still-reach-for-scheme-instead-of-haskell/index.html) ⭐️ 7.0/10

一篇博客文章解释了作者偏爱 Lisp 和 Scheme 而非 Haskell 的原因，认为交互式调试和强大的宏是其关键优势，这引发了社区的讨论。 这一比较凸显了动态与静态类型函数式语言之间持久的权衡，影响着开发者生产力和语言采用决策。 作者强调 Lisp 允许在生产环境中实时修改代码，而 Haskell 的强类型系统则需要更多的前期推理。然而，Scheme 缺乏 JVM 上那种广泛的企业级生态系统。

hackernews · jjba23 · Apr 29, 08:43

**背景**: Lisp 宏是完全成熟的程序，对表示为列表的代码进行操作，实现了编译时代码转换和语言扩展。相比之下，Haskell 依靠复杂的类型系统和纯函数来实现安全性和可组合性。这场辩论反映了语言设计中灵活性与安全性之间长期存在的张力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lisp_macros">Lisp macros</a></li>
<li><a href="https://en.wikibooks.org/wiki/Scheme_Programming/Macros">Scheme Programming/Macros - Wikibooks, open books for an open world</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了宏的实际用途（例如很少需要）以及在生产中使用 Lisp 调试的困难。一些人指出这篇文章与 2012 年的一篇帖子相似，而另一些人则建议将 Clojure 作为一个生态系统更丰富的现代替代方案。

**标签**: `#Lisp`, `#Scheme`, `#Haskell`, `#programming languages`, `#software engineering`

---

<a id="item-17"></a>
## [马里兰州禁止杂货店监控定价](https://www.theguardian.com/technology/2026/apr/29/maryland-grocery-stores-ban-surveillance-pricing) ⭐️ 7.0/10

马里兰州州长韦斯·摩尔签署法律，禁止杂货店基于监控的动态定价，使马里兰州成为美国首个实施此类禁令的州。 该法律为消费者隐私保护树立了先例，防止利用个人数据确定支付意愿的个性化定价，可能影响其他州和联邦政策。 该法律禁止通过监控定价提高价格，但不禁止提供个性化折扣，批评者认为这可能造成漏洞。此外，法律未赋予私人诉讼权，执行依赖州检察长。

hackernews · 01-_- · Apr 29, 16:50

**背景**: 监控定价是动态定价的一种形式，利用位置、浏览历史和购物模式等个人数据推断消费者的支付意愿，可能导致价格歧视。联邦贸易委员会已研究此种做法，发现一些公司根据精细的消费者数据设定不同价格。该法律专门针对杂货店，这一领域的监控定价可能对必需品造成不成比例的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Surveillance_pricing">Surveillance pricing</a></li>
<li><a href="https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-surveillance-pricing-study-indicates-wide-range-personal-data-used-set-individualized-consumer">FTC Surveillance Pricing Study Indicates Wide Range of Personal Data Used to Set Individualized Consumer Prices | Federal Trade Commission</a></li>
<li><a href="https://www.msn.com/en-us/politics/government/maryland-moves-to-ban-dynamic-pricing-statewide/ar-AA21Cras">Maryland moves to ban ' dynamic pricing ' statewide</a></li>

</ul>
</details>

**社区讨论**: 评论者对法律的有效性表示怀疑，指出存在将涨价转为折扣等潜在漏洞。有人担忧对抗性定价以及消费者需要代理来应对价格透明度问题。还有人指出缺乏私人诉讼权是一个限制。

**标签**: `#surveillance pricing`, `#privacy`, `#legislation`, `#dynamic pricing`, `#consumer rights`

---

<a id="item-18"></a>
## [从打印件转录的 DOS 1.0 源代码](https://github.com/DOS-History/Paterson-Listings) ⭐️ 7.0/10

一个 GitHub 仓库发布了从 Tim Paterson 的打印件转录的原始 DOS 1.0 源代码，使用 OCR 和基于 CRC 的自我错误检查来确保准确性。 这个转录让历史学家和开发者能够前所未有地审视 MS-DOS 的基础代码，该系统塑造了 PC 行业，并允许对关于该操作系统起源的历史说法进行仔细审查。 该转录项目由 Joshua Scarsbrook 领导，利用 OCR 技术扫描纸质打印件，并利用页边打印的 CRC 校验和自动验证准确性。代码可在 GitHub 上浏览。

hackernews · s2l · Apr 29, 11:25

**背景**: MS-DOS 1.0 由微软于 1981 年为 IBM PC 发布，源自 Tim Paterson 为 Seattle Computer Products 编写的 86-DOS。光学字符识别（OCR）将文本图像转换为机器可读代码，这项技术现在很常见，但这里应用于历史文物。打印件中存在的 CRC 校验和允许在转录过程中进行自动错误检查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optical_character_recognition">Optical character recognition</a></li>
<li><a href="https://en.wikipedia.org/wiki/MS-DOS">MS-DOS</a></li>
<li><a href="https://www.zdnet.com/article/microsoft-open-sources-dos-1-0-much-more-than-the-code/">Microsoft finally open sources DOS 1.0 - and it's so much more than the code | ZDNET</a></li>

</ul>
</details>

**社区讨论**: 社区评论提到了包含额外链接的微软官方公告，赞扬了使用 CRC 校验和的 OCR 方法，并指出这可以审视关于早期 DOS 是否包含 CP/M 代码的历史争论。一位用户还回忆了与原始 Seattle Computer Gazelle 机器的可能联系。

**标签**: `#DOS`, `#source code`, `#history`, `#OCR`, `#Microsoft`

---

<a id="item-19"></a>
## [荷兰政府软启动开源代码平台](https://www.nldigitalgovernment.nl/news/soft-launch-for-government-open-source-code-platform/) ⭐️ 7.0/10

荷兰政府软启动了 code.overheid.nl，这是一个面向公共部门项目的开源代码平台，旨在逐步脱离 GitHub。 此举提升了政府开发软件的透明度与控制力，为欧洲公共部门采用开源软件树立了先例。 该平台已托管诸如 RegelRecht 等项目，该项目将荷兰法律编码为机器可读的 YAML，以实现确定性决策逻辑并提供完整的解释路径。

hackernews · e12e · Apr 29, 09:14

**背景**: 政府通常依赖 GitHub 等专有平台托管代码，这可能引发数据主权和供应商锁定问题。通过建立自己的开源平台，荷兰政府可以确保公共部门代码的透明性、安全性和可复用性。

**社区讨论**: 评论者普遍表示赞同，荷兰用户指出他们长期以来一直倡导这一举措。部分用户讨论了 RegelRecht 项目，并将此举与德国的 OpenCode 平台进行了比较。

**标签**: `#open source`, `#government`, `#Netherlands`, `#code platform`, `#digital government`

---

<a id="item-20"></a>
## [OpenTrafficMap：低成本 V2X 交通可视化](https://opentrafficmap.org/) ⭐️ 6.0/10

OpenTrafficMap 是一个开源项目，它使用价格低于 20 英镑的 V2X 硬件接收消息，并在基于 OpenStreetMap 的现代界面中可视化交通数据。 通过大幅降低 V2X 硬件成本，该项目让爱好者与社区能够轻松采集交通数据，有望扩大覆盖范围并催生新的公民科学应用。 硬件使用 802.11p（DSRC）接收协作感知消息（CAM）和信号相位与时序（SPAT）消息，但目前覆盖范围有限，且在美国无法使用。

hackernews · moooo99 · Apr 29, 19:49

**背景**: 车联万物（V2X）通信使车辆能够与其他车辆、基础设施和行人进行交互。802.11p 是车辆环境下无线接入的标准，而 OpenStreetMap（OSM）是由志愿者创建和维护的一幅免费、可编辑的世界地图。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vehicle-to-everything">Vehicle-to-everything - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenStreetMap">OpenStreetMap</a></li>

</ul>
</details>

**社区讨论**: 评论者们对低于 20 英镑的硬件成本印象深刻，指出 802.11p 硬件通常价格昂贵。他们称赞了现代基于 OSM 的界面，但也指出缺乏详细信息，且该服务似乎无法在美国使用。一位评论者还担心可能带来的车辆追踪问题。

**标签**: `#traffic`, `#V2X`, `#openstreetmap`, `#IoT`, `#open data`

---