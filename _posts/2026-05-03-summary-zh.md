---
layout: default
title: "Horizon Summary: 2026-05-03 (ZH)"
date: 2026-05-03
lang: zh
---

> From 30 items, 13 important content pieces were selected

---

1. [VS Code 自动为所有提交添加“Co-Authored-by Copilot”](#item-1) ⭐️ 9.0/10
2. [Dav2d：AV2 视频编码标准最快的解码器](#item-2) ⭐️ 8.0/10
3. [NetHack 5.0.0 里程碑更新：引入 Lua 脚本，破坏存档兼容性](#item-3) ⭐️ 8.0/10
4. [加州将对违规自动驾驶汽车开罚单](#item-4) ⭐️ 8.0/10
5. [六年磨一剑：Apple Watch 自定义地图应用](#item-5) ⭐️ 7.0/10
6. [Ladybird 浏览器 2026 年 4 月通讯展示进展](#item-6) ⭐️ 7.0/10
7. [特斯拉车主因 FSD 虚假宣传胜诉获赔 1 万美元，特斯拉继续上诉](#item-7) ⭐️ 7.0/10
8. [macOS 虚拟机性能：多快多小？](#item-8) ⭐️ 7.0/10
9. [罗布乐思因儿童安全通信限制股价暴跌 18%](#item-9) ⭐️ 7.0/10
10. [Uber 计划将司机车辆用作自动驾驶传感器网格](#item-10) ⭐️ 7.0/10
11. [DO_NOT_TRACK 环境变量提案再掀隐私讨论](#item-11) ⭐️ 6.0/10
12. [开放设计：用编码代理做设计](#item-12) ⭐️ 6.0/10
13. [Windows 为何同时存在 TMP 和 TEMP 变量](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [VS Code 自动为所有提交添加“Co-Authored-by Copilot”](https://github.com/microsoft/vscode/pull/310226) ⭐️ 9.0/10

这一变更引发了严重的道德和法律担忧，因为 git 提交记录被视为技术和法律文件；为了夸大 AI 使用数据而伪造合著者身份，损害了开发者的信任，并可能带来法律后果。 该 PR 将“addAICoAuthor”设置的默认值改为“all”，但 extensions/git/src/repository.ts 中的运行时回退仍默认为“off”，导致不一致，可能引发意外行为。

hackernews · indrora · May 2, 19:57

**背景**: Git 提交消息通常包含“Co-authored-by”尾注以标注多个贡献者。VS Code 的 Copilot 集成允许在 Copilot 生成代码时自动添加这些尾注。但是，默认值为“all”意味着即使没有使用 Copilot，提交也会错误地声明 Copilot 合著，这可能扭曲贡献记录并违反归属规范。

**社区讨论**: 评论者表示强烈不满，将这一变更比作伪造法律记录，并指责微软将推广 AI 置于用户信任之上。一位评论者指出，Copilot 本人在 PR 中评论指出不一致，但该评论被忽略。另一位批准该 PR 的用户为未经充分验证就默认启用这一功能而道歉。

**标签**: `#VS Code`, `#Copilot`, `#ethics`, `#git`, `#Microsoft`

---

<a id="item-2"></a>
## [Dav2d：AV2 视频编码标准最快的解码器](https://code.videolan.org/videolan/dav2d) ⭐️ 8.0/10

VideoLAN 发布了 dav2d，这是一个针对下一代 AV2 视频编码标准开发的早期开源 CPU 解码器，声称是所有平台上最快的 AV2 解码器。 Dav2d 能够高效地软件播放 AV2 内容，AV2 相比 AV1 可降低 30%的比特率，从而显著提升流媒体质量并降低带宽成本。 Dav2d 由 dav1d 的同一团队开发，首先确保解码正确性，未来计划针对 x86、ARM 和 RISC-V 架构进行性能优化。

hackernews · dabinat · May 2, 17:32

**背景**: AV2 是 AV1 的后继者，由开放媒体联盟（AOMedia）开发，是一种开放免版税的视频编码格式。它采用改进的压缩技术，在更低的比特率下提供更好的画质。Dav2d 扮演着类似于 dav1d 的角色，后者被广泛用于 AV1 的播放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AV2_(video_coding_format)">AV2 (video coding format)</a></li>
<li><a href="https://www.phoronix.com/news/Dav2d-Open-Source-AV2-Decode">VideoLAN Publishes Dav2d For Open-Source AV2 Decoder</a></li>
<li><a href="https://videocardz.com/newz/videolan-publishes-dav2d-an-early-cpu-decoder-for-av2-video-codec">VideoLAN publishes dav2d, an early CPU decoder for AV2 video ...</a></li>

</ul>
</details>

**社区讨论**: 社区对 AV2 的潜力感到兴奋，指出其相比 AV1 可降低 30%比特率，并希望编码器的开发进度能比 AV1 更快。一些用户对网页上的繁琐验证（机器人检测、Cookie 提示）表示不耐烦，但总体上对解码器的发布持积极态度。

**标签**: `#av2`, `#video-codec`, `#decoder`, `#open-source`, `#video-encoding`

---

<a id="item-3"></a>
## [NetHack 5.0.0 里程碑更新：引入 Lua 脚本，破坏存档兼容性](https://nethack.org/v500/release.html) ⭐️ 8.0/10

NetHack 5.0.0 已发布，用 Lua 脚本替代了基于 yacc/lex 的旧式关卡和地牢编译器，并且不再兼容所有旧版存档和骨头文件。 这是传奇 Roguelike 游戏时隔数十年的一次重大技术革新，为实现更灵活的 mod 和开发铺平了道路；存档不兼容标志着一个时代的终结。 新的基于 Lua 的系统在运行时而非构建时处理关卡和地牢数据；任何旧版本（包括 3.7）的存档和骨头文件均无法用于 5.0.0。

hackernews · rsaarelm · May 2, 18:03

**背景**: NetHack 是一款经典的开放源代码 Roguelike 游戏，起源于 1987 年，以其深邃的游戏性、永久死亡机制和程序生成而闻名。它传统上使用基于 yacc/lex 的工具来生成关卡，并依赖 ASCII 图形。Lua 是一种轻量级脚本语言，常被嵌入到游戏中以实现自定义功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NetHack">NetHack - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lua">Lua - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区既兴奋又怀旧；一位玩家惋惜在即将通关前失去了保存了 17 年的存档文件，而其他人则称赞技术现代化并期待新的可能性。还有关于 3D 客户端更新的讨论。

**标签**: `#NetHack`, `#roguelike`, `#Lua`, `#game development`, `#open source`

---

<a id="item-4"></a>
## [加州将对违规自动驾驶汽车开罚单](https://www.bbc.com/news/articles/clypjx3rg2go) ⭐️ 8.0/10

加州宣布将对违反交通法规的无人驾驶汽车开罚单，让自动驾驶汽车运营商承担责任。 这一监管举措弥补了自动驾驶汽车问责制的一个关键空白，可能影响全国范围内自动驾驶汽车的测试和运营方式。 该罚单适用于在公共道路上行驶的无人驾驶汽车，违规行为将被记录以确保遵守交通法规。

hackernews · geox · May 2, 17:59

**背景**: 自动驾驶汽车是一种使用传感器和人工智能在无需人类操控的情况下导航的车辆。在加州，自动驾驶汽车一直在试点项目中在公共道路上行驶，但此前，由于没有人类驾驶员可被开罚单，交通违规行为往往无法对无人驾驶车辆执行。

**社区讨论**: 社区评论表达了支持与怀疑的混合态度。一些用户认为开罚单是迈向问责的一步，而另一些人则质疑开罚单是否是正确的方法，并建议对频繁违规者采用罚款或运营禁令等替代监管措施。

**标签**: `#autonomous vehicles`, `#regulation`, `#traffic enforcement`, `#Waymo`, `#public safety`

---

<a id="item-5"></a>
## [六年磨一剑：Apple Watch 自定义地图应用](https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/) ⭐️ 7.0/10

开发者 David Smith 发表博客文章，详细描述了他六年来的努力，利用预渲染地形瓦片为 Apple Watch 打造自定义地图应用，最终采用了制图师设计的底图。 这展示了在 Apple Watch 上实现高质量、专业化地图体验的潜力，而该设备内置的地图应用往往受限。它激励开发者突破平台限制。 该应用使用预渲染图像瓦片而非动态渲染，需要为不同缩放级别和旋转方向分别下载。开发者聘请了制图师，为 Apple 的 Liquid Glass 设计语言优化了底图。

hackernews · valzevul · May 2, 21:14

**背景**: 在 Apple Watch 上，由于硬件和功耗限制，实时渲染详细地图具有挑战性。传统的基于瓦片的地图服务会提供可缓存的小图像瓦片。然而，预渲染地形瓦片在美观和细节上优于 Apple Maps 内置的徒步数据，但缺乏动态更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/">Six Years Perfecting Maps on watchOS - david-smith.org</a></li>
<li><a href="https://app.daily.dev/posts/six-years-perfecting-maps-on-watchos-gbhh0hkdn">Six Years Perfecting Maps on watchOS | daily.dev</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了该应用的细节关注和演进，有人对 Apple Watch 缺乏第一方徒步地图表示遗憾。其他人注意到使用委托制图和静态瓦片的技术方法，虽然限制了交互性，但产生了美观的效果。

**标签**: `#watchOS`, `#maps`, `#cartography`, `#app development`, `#Apple Watch`

---

<a id="item-6"></a>
## [Ladybird 浏览器 2026 年 4 月通讯展示进展](https://ladybird.org/newsletter/2026-04-30/) ⭐️ 7.0/10

2026 年 4 月的 Ladybird 通讯报告了 CSS Doom 渲染和 Strava 登录的修复，以及其他标准合规性改进。据报道，Reddit 现在可以在浏览器中运行。 Ladybird 是一个从头构建、注重隐私的开源浏览器，此类修复的稳定进展表明它正朝着可用的 alpha 版本迈进。这可能为希望拥有独立于 Chrome 或 WebKit 的浏览器的用户提供一个可行的选择。 该项目计划于 2026 年发布 alpha 版本，2027 年发布 beta 版本，2028 年发布稳定版本。该浏览器由捐赠和赞助商资助，包括 Cloudflare、FUTO、Shopify 和 37signals。

hackernews · richardboegli · May 2, 20:46

**背景**: Ladybird 是一个开源 Web 浏览器，最初是 SerenityOS 的一部分，现在是非营利组织 Ladybird Browser Initiative 旗下的独立项目。它旨在成为一个拥有自己渲染引擎的真正独立浏览器，专注于隐私和标准合规性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_browser">Ladybird browser</a></li>
<li><a href="https://grokipedia.com/page/Ladybird_web_browser">Ladybird (web browser)</a></li>

</ul>
</details>

**社区讨论**: 评论者对可用性印象深刻，将其比作游戏模拟器更新，并注意到 Reddit 现在可以运行。还提到了 Dioxus 的一个类似的无 JavaScript 浏览器项目。一位评论者惊讶地发现 Strava 检查电池电量。

**标签**: `#browser`, `#open-source`, `#web development`, `#ladybird`, `#rendering`

---

<a id="item-7"></a>
## [特斯拉车主因 FSD 虚假宣传胜诉获赔 1 万美元，特斯拉继续上诉](https://electrek.co/2026/05/02/this-tesla-owner-won-10k-in-court-for-teslas-fsd-lies-tesla-is-still-fighting-him/) ⭐️ 7.0/10

一位特斯拉车主因特斯拉在完全自动驾驶（FSD）功能上的误导性宣传，赢得法庭判决并获得 1 万美元赔偿，但特斯拉仍在积极上诉。该案凸显了围绕特斯拉自动驾驶承诺的持续法律挑战。 此案可能为自动驾驶领域的消费者保护树立先例，可能引发更多诉讼，并迫使特斯拉在营销上更加谨慎。它凸显了业界对特斯拉 FSD 技术日益增长的怀疑和法律审查。 虽然 1 万美元的赔偿金额相对较小，但特斯拉的持续抗争表明，公司担心这会成为法律标杆，从而引发集体诉讼浪潮。该案涉及特斯拉将 FSD 功能虚假宣传为完全自主驾驶的指控。

hackernews · breve · May 2, 22:45

**背景**: 特斯拉将其“完全自动驾驶”（FSD）软件宣传为能够自主导航，但批评者和监管机构认为该名称具有误导性，因为该系统仍需要驾驶员监督，并非真正意义上的自动驾驶。美国法院正越来越多地审查此类声明是否构成欺诈或违反消费者保护法（如加州柠檬法和 Beverly Song 法案）的不公平贸易行为。

**社区讨论**: 社区评论对特斯拉的 FSD 声明表示强烈怀疑，有用户根据加州柠檬法因类似问题追回了 25 万美元。其他人指出，特斯拉不仅是在挑战判决，更是在抵制可能形成的判例，并预测如果不采取戏剧性的执法行动，车主可能永远拿不到这笔钱。

**标签**: `#Tesla`, `#FSD`, `#legal`, `#autonomous driving`, `#consumer protection`

---

<a id="item-8"></a>
## [macOS 虚拟机性能：多快多小？](https://eclecticlight.co/2026/05/02/how-fast-is-a-macos-vm-and-how-small-could-it-be/) ⭐️ 7.0/10

一项分析测试了 Apple Silicon 上 macOS 虚拟机的性能，显示配置 2 个核心和 4GB 内存的虚拟机可以高效处理轻量级任务，仅使用约 3.1GB 内存。 这为优化 macOS 虚拟机的资源分配提供了实用指导，对于在 Apple Silicon Mac 上运行虚拟化环境的开发者和用户很有价值。 分析从 4 核/8GB 逐步降至 2 核/4GB，显示内存使用从 5GB 降至 3.1GB，同时保持正常性能。每核内存包括页缓存和并发处理开销。

hackernews · moosia · May 2, 09:30

**背景**: Apple Silicon 上的 macOS 虚拟化使用 Virtualization 框架，允许配置 CPU 和内存运行 macOS 虚拟机。但 GPU 透传（特别是计算用途）仍然受限，如社区评论中所指出的。

**社区讨论**: 评论者赞赏实用的基准测试，指出每核内存占用解释了观察到的使用情况。一位用户提到在虚拟机中为 PyTorch 获取 GPU 加速几乎不可能，另一位指出在 macOS 上通过虚拟机运行 Docker 效率低下。

**标签**: `#macOS`, `#virtualization`, `#performance`, `#VM`, `#Apple Silicon`

---

<a id="item-9"></a>
## [罗布乐思因儿童安全通信限制股价暴跌 18%](https://www.cnbc.com/2026/05/01/roblox-rblx-stock-child-safety-earnings.html) ⭐️ 7.0/10

罗布乐思实施了基于年龄的通信限制，将用户分为六个年龄组，并禁止大多数跨组聊天，导致该公司下调了 2026 年预订量预期，股价因此暴跌 18%。 这一事件凸显了儿童安全与平台增长之间的张力，安全措施短期内可能降低用户活跃度和收入，但对于拥有大量未成年用户基础的平台而言，长期生存又至关重要。 年龄组分为 9 岁以下、9-12 岁、13-15 岁、16-17 岁、18-20 岁和 21 岁以上，用户只能与相差一个年龄组内的用户通信。罗布乐思还引入了聊天的强制面部验证，因隐私问题和可用性问题受到批评。

hackernews · 1vuio0pswjnm7 · May 2, 17:10

**背景**: 罗布乐思是一个流行的在线游戏平台，用户可以创建和玩游戏，其中年轻用户占比很高。该公司因儿童安全问题受到审查，从而采取了这些新措施。年龄验证和通信限制是保护未成年人的常见方法，但可能会破坏驱动平台参与度的社交动态。

**社区讨论**: 社区评论者意见不一：一些人批评这些措施过于严厉，破坏了社交体验；另一些人则认为长期安全值得短期收入损失。一个关键点是，基于年龄的聊天限制破坏了许多游戏的社交功能，而面部验证引发了隐私和人权方面的担忧。

**标签**: `#safety measures`, `#platform design`, `#stock market`, `#age verification`, `#social gaming`

---

<a id="item-10"></a>
## [Uber 计划将司机车辆用作自动驾驶传感器网格](https://techcrunch.com/2026/05/01/uber-wants-to-turn-its-millions-of-drivers-into-a-sensor-grid-for-self-driving-companies/) ⭐️ 7.0/10

Uber 宣布了一项长期计划，将为其人类司机的车辆配备传感器，构建一个庞大的数据网格，为自动驾驶公司提供真实驾驶数据，包括其投资的公司。 如果成功，这可能通过提供更便宜或更多样化的数据来加速自动驾驶发展，但也引发了关于司机同意、报酬、隐私和监管障碍的担忧。社区对所称的数据瓶颈持怀疑态度。 Uber 最终目标是在私人拥有的司机车辆上安装激光雷达等传感器，但时间表不明确，数据共享的监管明确性是先决条件。该计划还包括‘影子模式’，允许自动驾驶公司在不部署实际车队的情况下，针对数百万真实的 Uber 行程测试其模型。

hackernews · nickvec · May 2, 15:38

**背景**: 自动驾驶开发极度依赖大量真实驾驶数据来训练 AI 模型。Waymo 等公司通常使用搭载昂贵传感器的车辆自行收集数据。Uber 的提议是利用其现有的司机网络作为成本效益高的数据源，但批评者认为真正的瓶颈并非数据量，而是处理罕见的边缘情况和瞬时情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/05/01/uber-wants-to-turn-its-millions-of-drivers-into-a-sensor-grid-for-self-driving-companies/">Uber wants to turn its millions of drivers into a sensor grid ...</a></li>
<li><a href="https://pulse24.ai/news/2026/5/2/13/uber-plans-driver-sensor-grid">Uber Plans Driver Sensor Grid - pulse24.ai</a></li>
<li><a href="https://newsgab.com/uber-wants-drivers-as-sensor-grid-for-self-driving-firms/">Uber Wants Drivers To Act As A Sensor Grid For Self-driving ...</a></li>

</ul>
</details>

**社区讨论**: 社区高度怀疑。Animats 等评论者认为，更多地图数据无助于解决瞬时问题，谷歌街景数据可能已经足够。其他人质疑在私家车上安装昂贵激光雷达的可行性，指出自动驾驶公司已有数据，并指出 Uber 在其供应的自动驾驶公司中持有股权存在利益冲突。

**标签**: `#self-driving`, `#Uber`, `#data collection`, `#autonomous vehicles`, `#sensors`

---

<a id="item-11"></a>
## [DO_NOT_TRACK 环境变量提案再掀隐私讨论](https://donottrack.sh/) ⭐️ 6.0/10

donottrack.sh 网站上的一个新项目提议将 DO_NOT_TRACK 环境变量标准化，使用户能全局退出 CLI 和 TUI 应用中的遥测与跟踪，但该倡议因 DNT 浏览器头部的历史失败而面临质疑。 如果被采纳，这可能简化众多命令行工具对开发者和用户的隐私控制，但缺乏强制执行以及 DNT 过去的放弃表明，如果没有强大的行业支持，它可能面临类似命运。 该提案将现有的每个工具的环境变量（如 HF_HUB_DISABLE_TELEMETRY）集中到一个单一的 DO_NOT_TRACK 标志中，但社区成员指出多年前的类似尝试无果而终，且默认选择加入的问题仍然存在。

hackernews · RubyGuy · May 2, 17:40

**背景**: 像 DO_NOT_TRACK 这样的环境变量是一种向应用程序传达遥测偏好的约定。早期的 Do Not Track (DNT) HTTP 头部旨在让用户选择退出网络跟踪，但由于不遵守和缺乏法律强制执行，被 W3C 放弃，并在 2025 年前被主流浏览器移除。新提案旨在为命令行工具复制这一概念，但面临类似的自愿采纳挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://donottrack.sh/">DO_NOT_TRACK</a></li>
<li><a href="https://en.wikipedia.org/wiki/Do_Not_Track">Do Not Track - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了显著的怀疑：一位用户提到多年前类似的提案无果而终，另一位批评隐含的默认'CONSENT_TO_TRACK=1'，还有一位暗示任何公开支持该规范的工具很可能是一个蜜罐，会在没有明确选择加入的情况下收集遥测数据。实用困难也被强调，例如需要多个环境变量才能真正停止遥测（如除了 HF_HUB_DISABLE_TELEMETRY 外还需要 HF_HUB_OFFLINE=1）。

**标签**: `#privacy`, `#telemetry`, `#environment-variables`, `#developer-tools`

---

<a id="item-12"></a>
## [开放设计：用编码代理做设计](https://github.com/nexu-io/open-design) ⭐️ 6.0/10

一个名为 Open Design 的 GitHub 仓库提议使用 AI 编码代理作为设计引擎来创建 UI 布局、演示文稿等设计产物。该概念在社区中引发了关于 AI 生成设计质量和效率的辩论。 这种方法可能降低制作专业外观设计的门槛，特别是对非设计师而言。但社区的怀疑态度凸显了对 token 效率低下、输出同质化以及贬低真正设计作品价值的担忧。 该仓库概述了概念性想法，但缺乏具体的实现演示；用户注意到 README 读起来像销售宣传。评论还指出，与 ChatGPT 图像生成等替代方案相比，演示中的 Claude 方法 token 效率低下。

hackernews · steveharing1 · May 2, 12:16

**背景**: AI 编码代理是使用大型语言模型根据自然语言提示自主编写和优化代码的工具。'Vibe coding'一词用于描述使用此类代理快速生成前端代码，但社区对于这种方法是否产生高质量、可维护的设计，还是仅仅输出通用内容存在分歧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>
<li><a href="https://zencoder.ai/">Zencoder | The AI Coding Agent</a></li>
<li><a href="https://kilo.ai/">Kilo - Kilo: The Open Source AI Coding Agent for VS Code , JetBrains...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍表示怀疑：jshaqaw 警告 AI 生成的设计会变成无价值的背景噪音；ricardobeat 批评'Claude 推销员'式的写作风格；Saline9515 抱怨 token 浪费并称赞 ChatGPT 的效率；lmeyerov 询问高效的工作流程；MSaiRam10 称 README 为销售演示，并质疑高星标数。

**标签**: `#AI`, `#design`, `#coding agents`, `#GitHub`, `#Hacker News`

---

<a id="item-13"></a>
## [Windows 为何同时存在 TMP 和 TEMP 变量](https://devblogs.microsoft.com/oldnewthing/20150417-00/?p=44213) ⭐️ 6.0/10

Raymond Chen 在 2015 年的博客文章解释，Windows 中同时存在 TMP 和 TEMP 环境变量源于 CP/M 和早期 MS-DOS 的历史实践，当时不同程序使用不同的变量名来指定临时文件目录。 这一微小不一致性说明了上世纪七八十年代的遗留决策如何延续至现代操作系统，影响开发者和高级用户的软件兼容性与系统配置。 文章指出，CP/M 没有标准变量名，于是程序硬编码为'TMP'或'TEMP'，MS-DOS 后来继承了这两者。8.3 文件名约定可能促使了三个字母的'TMP'被采用。

hackernews · ankitg12 · May 2, 08:23

**背景**: CP/M 是由 Gary Kildall 开发的操作系统，在 20 世纪 70 年代末到 80 年代初主导了微型计算机市场。微软为 IBM PC 创建的 MS-DOS 借鉴了 CP/M 的许多概念，包括环境变量。单一标准的缺失导致了今天看到的重复现象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CP/M_operating_system">CP/M operating system</a></li>
<li><a href="https://en.wikipedia.org/wiki/MS-DOS">MS-DOS - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，CP/M 程序常通过修补二进制文件来配置，其中一位更正了 CP/M 的初始年份是 1974 年而非 1973 年。他们还类比了 Unix 上 HTTP 代理环境变量的不一致，并评论说这类早期决策往往永久延续。

**标签**: `#environment variables`, `#Windows`, `#history`, `#CP/M`, `#MS-DOS`

---