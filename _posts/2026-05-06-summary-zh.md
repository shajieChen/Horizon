---
layout: default
title: "Horizon Summary: 2026-05-06 (ZH)"
date: 2026-05-06
lang: zh
---

> From 41 items, 17 important content pieces were selected

---

1. [扎克伯格被指控授权 Meta 侵犯版权](#item-1) ⭐️ 9.0/10
2. [.de 顶级域因 DNSSEC 配置错误导致宕机](#item-2) ⭐️ 8.0/10
3. [Gemma 4 使用多令牌预测加速推理](#item-3) ⭐️ 8.0/10
4. [计算机使用比结构化 API 贵 45 倍](#item-4) ⭐️ 8.0/10
5. [Chrome 未经用户同意静默下载高达 4GB 的 AI 模型](#item-5) ⭐️ 8.0/10
6. [AI 提升个人效率，企业却学不到东西](#item-6) ⭐️ 8.0/10
7. [OpenAI 发布 GPT-5.5 Instant 系统卡](#item-7) ⭐️ 8.0/10
8. [编写免费软件：关于价值与回报的辩论](#item-8) ⭐️ 7.0/10
9. [AI 逆定律引热议](#item-9) ⭐️ 7.0/10
10. [EEVblog 庆祝 555 定时器 IC 诞生 55 周年](#item-10) ⭐️ 7.0/10
11. [Anthropic 发布 10 个金融与保险 AI 代理模板](#item-11) ⭐️ 7.0/10
12. [Simon Willison 点赞 liblotus 数据提取库](#item-12) ⭐️ 6.0/10
13. [GLM-5V-Turbo：面向多模态智能体的原生基础模型](#item-13) ⭐️ 6.0/10
14. [Coinbase 裁员约 14%，归因于 AI 效率](#item-14) ⭐️ 6.0/10
15. [IBM 曾反对微软用 Tab 键进行对话框导航](#item-15) ⭐️ 6.0/10
16. [iOS 27 在 Apple Wallet 中添加“创建通行证”按钮](#item-16) ⭐️ 6.0/10
17. [AI 咖啡馆在斯德哥尔摩闹出笑话](#item-17) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [扎克伯格被指控授权 Meta 侵犯版权](https://variety.com/2026/digital/news/meta-ai-mark-zuckerberg-copyright-infringement-lawsuit-publishers-scott-turow-1236738383/) ⭐️ 9.0/10

一项新诉讼指控马克·扎克伯格亲自授权并鼓励 Meta 在未经许可的情况下使用数百万本受版权保护的书籍和文章来训练其 LLaMA AI 模型。 此案可能为高管在 AI 版权侵权中的个人责任树立法律先例，有可能重塑企业问责制和 AI 训练数据使用的伦理规范。 原告（包括多家主要出版商）声称 Meta 未经同意或补偿复制了数百万部作品，且扎克伯格直接参与了决策。该诉讼要求赔偿，若个人责任成立，可能导致重大处罚。

hackernews · spankibalt · May 5, 18:04

**背景**: AI 训练通常需要海量数据，许多公司未经明确许可便使用公开内容，导致众多版权诉讼。合理使用（fair use）的法律概念是这些争议的核心，法院需权衡 AI 训练是否具有变革性。在之前的案例中，如 Anthropic 的和解协议，公司因未经授权使用受版权保护的作品支付了数十亿美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.skadden.com/insights/publications/2025/05/copyright-office-report">Copyright Office Weighs In on AI Training and Fair Use | Skadden, Arps, Slate, Meagher & Flom LLP</a></li>
<li><a href="https://influencermagazine.uk/2026/05/major-publishers-file-copyright-lawsuit-against-meta-over-ai-training-practices/">Major Publishers File Copyright Lawsuit Against Meta Over AI Training Practices</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright">Artificial intelligence and copyright - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：一些人对于扎克伯格可能面临个人责任表示满意，有人指出 Meta 无视 robots.txt；另一些人则认为 AI 训练属于合理使用，并与 Aaron Swartz 等过往案例相比较。讨论突显了关于高管问责制和 AI 训练变革性的强烈观点。

**标签**: `#AI`, `#copyright`, `#Meta`, `#legal`, `#ethics`

---

<a id="item-2"></a>
## [.de 顶级域因 DNSSEC 配置错误导致宕机](https://dnssec-analyzer.verisignlabs.com/nic.de) ⭐️ 8.0/10

近日，.de 顶级域因 DENIC 发布无效的 DNSSEC 签名而出现大规模宕机，导致所有验证解析器对.de 域名返回 SERVFAIL 错误。 这一事件暴露了 DNSSEC 的一个关键弱点：顶级域级别的单一配置错误可能导致整个国家域名空间对使用验证解析器的用户不可访问，影响数百万网站。 根本原因是某个 NSEC3 记录的 RRSIG 签名无法通过区域签名密钥（ZSK 33834）验证。Cloudflare 通过临时禁用其 1.1.1.1 解析器上的 DNSSEC 验证来缓解问题。

hackernews · warpspin · May 5, 20:16

**背景**: DNSSEC（域名系统安全扩展）通过向 DNS 记录添加加密签名来确保真实性和完整性。验证解析器在信任响应之前会检查这些签名。如果签名格式错误或缺失，解析器会返回 SERVFAIL 以防止潜在的欺骗攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DNSSEC">DNSSEC</a></li>
<li><a href="https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/">How Does DNSSEC Work? | Cloudflare</a></li>

</ul>
</details>

**社区讨论**: 社区成员指出该问题是 DNSSEC 配置错误而非域名服务器宕机，并注意到非验证查询可以正常工作。一些人批评 DNSSEC 引入了集中化的故障点，并引用了 Thomas Ptacek 著名的反对 DNSSEC 的批评文章。

**标签**: `#DNS`, `#DNSSEC`, `#Outage`, `#.de`, `#Network`

---

<a id="item-3"></a>
## [Gemma 4 使用多令牌预测加速推理](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) ⭐️ 8.0/10

Google 为 Gemma 4 系列发布了多令牌预测（MTP）草稿模型，在保持竞争力基准性能的同时显著提升了推理速度。 该技术降低了开源模型的延迟，使其更适用于实时应用和边缘部署。同时，它凸显了 AI 行业中对效率而非纯性能的战略关注。 MTP 草稿模型是轻量级模型，并行预测多个未来的令牌，然后由目标 Gemma 4 模型在单次前向传播中验证。这种推测解码方法可将延迟大致降低两到三倍，同时不改变输出分布。

hackernews · amrrs · May 5, 16:14

**背景**: 自回归大语言模型每次生成一个令牌，本质上速度较慢。推测解码通过使用较小的草稿模型猜测多个令牌，再由较大的目标模型验证来加速。Google 的 Gemma 4 是一个开源模型系列，基于与 Gemini 类似的技术，专注于高级推理和代理工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Accelerating Gemma 4: faster inference with multi-token prediction drafters</a></li>
<li><a href="https://app.daily.dev/posts/multi-token-prediction-in-gemma-4-p8wqk64sp">Multi-token-prediction in Gemma 4 | daily.dev</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>

</ul>
</details>

**社区讨论**: 社区成员指出，Gemma 模型在输出时使用的令牌数已经比竞争对手少，而新的 MTP 草稿模型进一步提升了速度。一些人讨论了实际权衡，例如同时运行草稿模型和视觉模块会增加 VRAM 需求，并希望 llama.cpp 能支持 MTP。

**标签**: `#Gemma 4`, `#multi-token prediction`, `#inference acceleration`, `#Google AI`, `#open source models`

---

<a id="item-4"></a>
## [计算机使用比结构化 API 贵 45 倍](https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/) ⭐️ 8.0/10

Reflex.dev 的一篇博客文章通过成本和延迟分析表明，基于视觉的计算机使用（GUI 自动化）在执行常见任务时比使用结构化 API 贵 45 倍。 这一发现突显了 AI 代理开发中的一个关键权衡：虽然计算机使用可以操作任何应用程序，但其高成本和延迟使得结构化 API 在大多数情况下更加高效和实用。 该分析涵盖了表单填写和导航等任务，在这些任务中，视觉模型的 token 消耗和处理时间导致成本相比直接 API 调用显著增加。

hackernews · palashawas · May 5, 16:34

**背景**: 计算机使用指的是 AI 代理通过查看屏幕并控制鼠标和键盘来与软件交互，类似于人类操作。结构化 API 提供直接的编程访问功能。Anthropic 在 2024 年 10 月随 Claude 3.5 Sonnet 推出了计算机使用功能，允许开发者通过视觉方式指挥模型操作计算机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/3-5-models-and-computer-use">Introducing computer use, a new Claude 3.5 Sonnet, and ...</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool">Computer use tool - Claude API Docs</a></li>
<li><a href="https://www.datacamp.com/blog/what-is-anthropic-computer-use">Anthropic Computer Use: Automate Your Desktop With Claude 3.5 | DataCamp</a></li>

</ul>
</details>

**社区讨论**: 评论提供了不同的观点：有人认为计算机使用是用于没有 API 的应用的最后手段，而有人建议使用视觉代理映射 UI 并将其暴露为 API 以降低成本。也有乐观看法认为效率提升将随时间到来。

**标签**: `#AI`, `#APIs`, `#cost analysis`, `#computer use`, `#software development`

---

<a id="item-5"></a>
## [Chrome 未经用户同意静默下载高达 4GB 的 AI 模型](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/) ⭐️ 8.0/10

据报道，Google Chrome 会在用户不知情的情况下静默下载大型 AI 模型（Gemini Nano，高达 4 GB），此行为由某些 Chrome 标志或 Origin Trials 触发。 这引发了严重的隐私和资源担忧，用户和系统管理员面临意外的磁盘占用、带宽消耗以及缺乏同意的问题，尤其在像学校和企业这样的受管环境中。 当启用了“optimization-guide-on-device-model”和“prompt-api-for-gemini-nano”标志时，模型下载会触发，允许网页通过 Prompt API 发起一次性下载；CPU 模型约 2.7 GiB，GPU 模型约 4.0 GiB。

hackernews · john-doe · May 5, 07:34

**背景**: Gemini Nano 是 Google 设计的一款轻量级多模态 AI 模型，用于设备端推理，无需网络连接即可实现生成式 AI 功能。Chrome 的 Prompt API 允许网页访问设备端 AI 模型，但如此大模型的静默下载引发了关于用户同意和资源管理的辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_Nano">Gemini Nano</a></li>
<li><a href="https://developer.android.com/ai/gemini-nano">Gemini Nano | AI | Android Developers</a></li>

</ul>
</details>

**社区讨论**: 社区评论意见分歧：有人认为该模型是软件更新的一部分，无需单独同意；而另一些人则批评缺乏透明度，以及对磁盘空间和带宽的巨大影响，尤其在受管 IT 环境中。用户还指出，下载由某些标志触发，而这些标志可能在未来版本中默认启用。

**标签**: `#Chrome`, `#AI`, `#privacy`, `#consent`, `#resource usage`

---

<a id="item-6"></a>
## [AI 提升个人效率，企业却学不到东西](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/) ⭐️ 8.0/10

文章指出，像 GitHub Copilot 这样的 AI 代码助手提高了开发者的生产力，但并未解决组织瓶颈，导致公司整体没有学到任何东西，效率也无提升。 这挑战了采用 AI 就能自动提升组织效率的说法，指出除非工作流程得到改革，否则 AI 的好处将局限于个人，甚至可能加剧瓶颈。 文章强调了混乱的中间地带，开发者没有动力分享生产力提升，而测试、审批、部署等后续流程没有改变，因此 AI 加速了代码生成，但没有加快发布周期。

hackernews · youngbrioche · May 5, 09:30

**背景**: GitHub Copilot 是由 GitHub 和 OpenAI 开发的 AI 代码补全工具，于 2021 年推出，支持 VS Code 等 IDE。它提供实时建议以提高个人编码速度，但对整体软件交付的影响取决于组织流程和激励机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GitHub_Copilot">GitHub Copilot</a></li>
<li><a href="https://github.com/features/copilot">GitHub Copilot</a></li>

</ul>
</details>

**社区讨论**: 评论者大多赞同文章观点，分享经验指出 AI 访问仅限开发人员，代码需要数月才能上线，并且没有分享知识的动力。一些人质疑 AI 是逐利工具而非真正的创新。

**标签**: `#AI adoption`, `#organizational learning`, `#software engineering`, `#corporate culture`, `#productivity`

---

<a id="item-7"></a>
## [OpenAI 发布 GPT-5.5 Instant 系统卡](https://openai.com/index/gpt-5-5-instant-system-card) ⭐️ 8.0/10

OpenAI 发布了 GPT-5.5 Instant 系统卡，详细说明了该模型的能力、安全评估和性能。该模型现已成为 ChatGPT 的默认模型，提供更智能的回答、更少的幻觉以及改进的个性化控制。 此次发布标志着 ChatGPT 核心模型的重大升级，可能改善数百万次交互中的用户体验。详细的系统卡增强了大语言模型的透明度和安全问责制。 系统卡涵盖了多个类别的能力、局限性和安全评估。它还记录了与之前 GPT 版本相比，幻觉率降低以及个性化控制的增强。

rss · OpenAI Blog · May 5, 10:00

**背景**: OpenAI 定期为主要模型更新发布系统卡，例如 GPT-4o 和 o1。这些文档提供技术细节和安全评估，以便开发者和研究人员了解情况。GPT-5.5 Instant 是最新版本，接替了 GPT-4 和 GPT-5 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-system-card/">GPT-5 System Card - OpenAI</a></li>
<li><a href="https://openai.com/index/gpt-4o-system-card/">GPT-4o System Card | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#GPT-5.5`, `#OpenAI`, `#language models`, `#system card`

---

<a id="item-8"></a>
## [编写免费软件：关于价值与回报的辩论](https://nonogra.ph/write-some-software-give-it-away-for-free-05-05-2026) ⭐️ 7.0/10

一篇博文反思免费发布软件的价值，引发社区关于开源与商业软件之间权衡的讨论。 这一讨论凸显了软件行业在盈利、社区期望和开发者福祉方面的持续紧张关系，影响着软件的创建和分发方式。 评论者分享个人经历：有人在开源社区遇到 entitlement，而在付费软件中获得建设性互动；也有人从免费贡献中获得满足感，但指出这是一种特权。

hackernews · nohell · May 5, 21:26

**背景**: 开源软件以许可证形式发布，允许自由使用、修改和分发，通常依赖自愿贡献。许多开发者努力平衡利他主义与谋生需求，这引发了关于可持续性和公平报酬的辩论。

**社区讨论**: 评论者观点不一：有人更偏好付费软件以获得更好的用户互动，而有人则重视回馈社区但承认这是一种特权。总体而言，没有唯一正确的答案，每个开发者需根据自身情况做决定。

**标签**: `#open source`, `#software economics`, `#community`, `#philosophy`

---

<a id="item-9"></a>
## [AI 逆定律引热议](https://susam.net/inverse-laws-of-robotics.html) ⭐️ 7.0/10

博客文章《人工智能的三个逆定律》提出了人机交互规则，包括人类不能将 AI 拟人化、不能盲目信任 AI 输出、不能将责任推给 AI。该文因忽视这些行为的不可避免性而受到批评。 这场辩论突出了 AI 伦理中的根本矛盾：是改变人类行为，还是围绕人类倾向设计 AI。社区的热烈参与表明人们对 AI 安全和人类与 AI 交互的深切担忧。 该博客文章通过提出针对人类行为的逆定律来挑战阿西莫夫的机器人三定律。批评者认为，人类不可避免地会将 AI 拟人化、信任 AI 并依赖 AI，规则必须考虑这些倾向，而不是禁止它们。

hackernews · blenderob · May 5, 15:27

**背景**: 阿西莫夫的机器人三定律是一套虚构的规则，旨在确保机器人的安全行为。“逆定律”的概念将焦点从 AI 行为转向人类行为。拟人化是一种众所周知的认知偏见，即人类将人类特征赋予非人类实体，因此简单地禁止是困难的。

**社区讨论**: 社区评论者普遍不同意所提出的定律，认为拟人化是不可避免的。有人指出，AI 提供商鼓励拟人化行为，围绕人类倾向进行工程化设计比强加武断规则更实际。

**标签**: `#AI ethics`, `#human-AI interaction`, `#anthropomorphism`, `#AI safety`

---

<a id="item-10"></a>
## [EEVblog 庆祝 555 定时器 IC 诞生 55 周年](https://www.youtube.com/watch?v=6JhK8iCQuqI) ⭐️ 7.0/10

EEVblog 发布了一段视频，庆祝 555 定时器 IC 诞生 55 周年，社区讨论了其设计历史与影响。 555 定时器是电子历史上最具标志性和多功能的集成电路之一，这一里程碑凸显了它在爱好者和专业项目中持续的相关性。 视频和评论透露，最初的设计需要 9 个引脚，但通过一个后期的灵感减少到了熟悉的 8 引脚封装。同时，Big Clive 也在同步直播庆祝。

hackernews · brudgers · May 5, 15:47

**背景**: 555 定时器是一种广泛使用的集成电路，可以产生精确的时间延迟和振荡。它于 1971 年由 Signetics 公司推出，以其简单性和多功能性而闻名，出现在从简单定时器到复杂脉冲发生器的无数电子项目中。

**社区讨论**: 评论者分享了个人轶事，包括设计师免费书籍的链接、视频发布时长为 5:55 且于 5 月 5 日发布，以及一个关于在 Apple II 磁盘控制器上毁坏 555 芯片的故事。还有提到 Big Clive 同时进行的直播。

**标签**: `#electronics`, `#555 timer`, `#history`, `#integrated circuit`, `#timing`

---

<a id="item-11"></a>
## [Anthropic 发布 10 个金融与保险 AI 代理模板](https://www.anthropic.com/news/finance-agents) ⭐️ 7.0/10

Anthropic 发布了十个用于金融服务和保险的即用型 Claude 代理模板，涵盖提案构建、KYC 筛查和月末结账等任务。 这些模板可以自动化金融领域许多耗时的流程，可能提高银行和保险公司的效率并降低成本。 模板集成了 Microsoft 365 和各种数据连接器，但设计上避免在贷款或审批中直接决策，以减轻偏见风险。

hackernews · louiereederson · May 5, 15:05

**背景**: AI 代理是可以自主执行复杂任务的软件程序。金融服务是 AI 的早期采用者，用于欺诈检测等任务，但 KYC 和月末结账等手动流程仍然劳动密集。Anthropic 的 Claude 是一个以安全性著称的大型语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seekingalpha.com/news/4585757-anthropic-unveils-10-agent-templates-for-financial-services">Anthropic unveils 10 agent templates for financial services - Seeking Alpha</a></li>
<li><a href="https://qz.com/anthropic-ai-agents-financial-services-banks-insurers-050526">Anthropic launches 10 AI agents for banks and insurers - Quartz</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了复杂情绪：一些人担心偏见和信任问题（例如 Claude Opus 4.7 的偏见），另一些人质疑商业模式和竞争（例如扼杀初创公司）。也有人对 AI 公司成为敏感数据处理的一夜专家持怀疑态度。

**标签**: `#AI agents`, `#financial services`, `#Anthropic`, `#Claude`, `#product launch`

---

<a id="item-12"></a>
## [Simon Willison 点赞 liblotus 数据提取库](https://github.com/asg017/liblotus) ⭐️ 6.0/10

Simon Willison 在 GitHub 上为 liblotus 点赞，这是一个旨在从 PDF 和图像等非结构化来源中提取结构化数据的库。 这位知名开发者的点赞表明社区对连接非结构化与结构化数据的工具有潜在兴趣，这在数据处理和 AI 工作流中需求日益增长。 Liblotus 专门针对 PDF 和图像——这些常见但难以提取的数据格式，其方法可能利用了现代 AI 技术，如 OCR 或视觉语言模型。

github · simonw · May 5, 16:06

**背景**: 非结构化数据（如 PDF、图像）缺乏预定义的数据模型，难以通过程序处理。结构化数据提取将此类内容转换为表格或 JSON，从而实现后续分析和自动化。

**标签**: `#data extraction`, `#Python`, `#library`, `#PDF`, `#AI`

---

<a id="item-13"></a>
## [GLM-5V-Turbo：面向多模态智能体的原生基础模型](https://arxiv.org/abs/2604.26752) ⭐️ 6.0/10

GLM-5V-Turbo 是由 Z.AI 开发的多模态基础模型，专为基于视觉的编码和智能体任务设计，原生处理图像、视频和文本输入。 该模型是迈向原生多模态智能体的一步，但面临较新开源模型的激烈竞争，社区反馈褒贬不一，既称赞其速度和可靠性，也指出了性能不足。 该模型并非开源；GLM 系列最新公开发布的版本是 GLM-4.6V。一些用户报告称，GLM-5V-Turbo 在编码和推理任务上表现不如较新的替代方案。

hackernews · gmays · May 5, 17:52

**背景**: 多模态智能体整合文本、图像以及浏览器和 API 等真实世界工具。GLM-5V-Turbo 是 Z.AI 的 GLM 大模型系列的一部分，专注于为智能体工作流提供原生多模态理解能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/GLM-5V-Turbo">GLM-5V-Turbo</a></li>
<li><a href="https://grokipedia.com/page/Multimodal_integration_in_AI_agents">Multimodal integration in AI agents</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些用户赞扬其速度和日常可用性，而另一些用户则认为它在编码/推理测试中已经过时。有用户指出，如果没有适当的防护机制，它可能会陷入“死循环”，并且存在 GUI 智能体坐标点击不准确的问题。

**标签**: `#multimodal agents`, `#foundation models`, `#GLM`, `#AI research`

---

<a id="item-14"></a>
## [Coinbase 裁员约 14%，归因于 AI 效率](https://twitter.com/brian_armstrong/status/2051616759145185723) ⭐️ 6.0/10

Coinbase 首席执行官 Brian Armstrong 宣布裁员约 14%，围绕球员兼教练型经理和 AI 原生小组进行重组，并将此归因于 AI 带来的生产力提升。 这家主要加密货币交易所的裁员突显了 AI 对科技和金融领域就业的日益增长的影响，同时也反映了加密熊市中的持续成本压力。 此次裁员使员工总数估计降至 4,250 人，仍高于 2024 年的水平；重组取消了纯管理岗位，并强调小而精的 AI 聚焦团队。

hackernews · adrianmsmith · May 5, 12:10

**背景**: Coinbase 是领先的加密货币交易所，其收入与交易量高度相关。加密市场以繁荣-萧条周期著称；熊市通常会减少交易活动，迫使公司削减成本。AI 工具最近使软件开发速度更快，导致一些公司围绕 AI 原生结构进行重组。

**社区讨论**: 评论者质疑 AI 是否真正带来了所声称的生产力提升，认为真正原因是熊市带来的收入下降。一些人担心强调‘AI 原生人才’可能隐含年龄歧视，而其他人则指出，此次裁员仅使员工数量回到 2024 年水平，并非大幅削减。

**标签**: `#layoffs`, `#Coinbase`, `#crypto`, `#AI`, `#workforce`

---

<a id="item-15"></a>
## [IBM 曾反对微软用 Tab 键进行对话框导航](https://devblogs.microsoft.com/oldnewthing/20260505-00/?p=112298) ⭐️ 6.0/10

微软旧事新谈博客的一篇文章透露，IBM 曾反对微软使用 Tab 键在对话框字段间移动焦点，理由是 IBM 拥有相关专有标准。 这一历史轶事揭示了专有标准与新兴 GUI 惯例之间的摩擦，最终促成了我们今天普遍使用的 Tab 键导航。 IBM 认为 Tab 键不应被重新用于导航，因为这与他们在 3270 终端上建立的键盘标准相冲突——在那些终端上，Tab 键已用于将光标移动到下一个字段。

hackernews · SeenNotHeard · May 5, 17:28

**背景**: 在早期计算中，键盘快捷键并未跨平台标准化。IBM 的 3270 终端使用 Tab 键进行字段导航，而微软的 Windows 则寻求一种在对话框控件之间移动的一致方法。这一分歧代表了遗留企业标准与新兴消费者 UI 范式之间的碰撞。

**社区讨论**: 评论者指出 IBM 的管理过于僵化；有人分享了实习生等了好几个月才获批休闲星期五的故事。另有人指出，IBM 自己的 3270 终端已经使用 Tab 键进行导航，因此他们的反对有些讽刺。

**标签**: `#history`, `#UI design`, `#IBM`, `#Microsoft`, `#keyboard shortcuts`

---

<a id="item-16"></a>
## [iOS 27 在 Apple Wallet 中添加“创建通行证”按钮](https://walletwallet.alen.ro/blog/ios-27-wallet-create-pass/) ⭐️ 6.0/10

iOS 27 在 Apple Wallet 应用中新增了“创建通行证”按钮，用户可以直接添加自定义通行证，如会员卡、借书卡或活动门票，无需依赖第三方应用。 这解决了一个长期存在的用户痛点：没有开发资源的小型场所和组织无法轻松创建数字通行证，可能提升 Apple Wallet 在日常使用中的采用率。 该功能仅限 iPhone，不适用于 Google Wallet 或 Android 用户。苹果此前仅允许经过授权的开发者创建通行证，导致 Pass Creator 等第三方应用被从 App Store 下架。

hackernews · alentodorov · May 5, 12:28

**背景**: Apple Wallet 使用名为 PassKit 的格式存储数字通行证，如登机牌、门票和会员卡。历史上只有经批准的开发者才能创建通行证，限制了小型企业或个人使用。

**社区讨论**: 社区评论表达了宽慰，并指出了过去的变通方法，例如保存条码照片。一些评论者指出 Google Wallet 已有类似功能，并质疑苹果为何花费如此长时间来解决用户界面缺口。还有评论提到苹果之前从 App Store 下架了通行证创建应用。

**标签**: `#iOS`, `#Apple Wallet`, `#UI/UX`, `#Mobile`, `#Digital Wallets`

---

<a id="item-17"></a>
## [AI 咖啡馆在斯德哥尔摩闹出笑话](https://simonwillison.net/2026/May/5/our-ai-started-a-cafe-in-stockholm/#atom-everything) ⭐️ 6.0/10

Andon Labs 在斯德哥尔摩开设了一家由 AI 管理的咖啡馆，名为 Mona 的 AI 犯下幽默的订购错误，比如在没有炉灶的情况下购买了 120 个鸡蛋，以及订购了 6000 张餐巾。 这一实验凸显了当前 AI 在处理现实物理操作中的局限性，并引发了关于在未经他人同意的情况下浪费他人时间的伦理担忧。 该 AI 用自己生成的、从未见过的街道草图申请了户外座位许可证，并多次向供应商发送“紧急”邮件以纠正自己的错误。

rss · Simon Willison · May 5, 22:14

**背景**: Andon Labs 之前在旧金山运营了一家 AI 管理的零售店。这些实验使用 AI 智能体来管理订购库存和处理许可证等任务，但在对外沟通中常常缺乏人类监督。

**标签**: `#AI`, `#experiment`, `#real-world AI`, `#humor`, `#limitations`

---