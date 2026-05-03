---
layout: default
title: "Horizon Summary: 2026-05-03 (EN)"
date: 2026-05-03
lang: en
---

> From 30 items, 13 important content pieces were selected

---

1. [VS Code Auto-Adds 'Co-Authored-by Copilot' to All Commits](#item-1) ⭐️ 9.0/10
2. [Dav2d: The Fastest Decoder for AV2 Video Codec](#item-2) ⭐️ 8.0/10
3. [NetHack 5.0.0: Landmark Update Brings Lua Scripting and Breaks Save Compatibility](#item-3) ⭐️ 8.0/10
4. [California to ticket driverless cars for traffic violations](#item-4) ⭐️ 8.0/10
5. [Six-Year Journey Perfecting Maps on Apple Watch](#item-5) ⭐️ 7.0/10
6. [Ladybird Browser April 2026 Newsletter Highlights Progress](#item-6) ⭐️ 7.0/10
7. [Tesla Owner Wins $10K Judgment Over FSD Lies, Tesla Appeals](#item-7) ⭐️ 7.0/10
8. [macOS VM Performance: How Fast and How Small?](#item-8) ⭐️ 7.0/10
9. [Roblox Stock Plunges 18% on Child Safety Communication Restrictions](#item-9) ⭐️ 7.0/10
10. [Uber plans to use drivers' cars as sensor grid for AVs](#item-10) ⭐️ 7.0/10
11. [Proposed DO_NOT_TRACK Environment Variable Revives Privacy Debates](#item-11) ⭐️ 6.0/10
12. [Open Design: Using Coding Agents for Design](#item-12) ⭐️ 6.0/10
13. [Why Windows Has Both TMP and TEMP Variables](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [VS Code Auto-Adds 'Co-Authored-by Copilot' to All Commits](https://github.com/microsoft/vscode/pull/310226) ⭐️ 9.0/10

Microsoft's VS Code introduced a default behavior change that automatically appends 'Co-Authored-by Copilot' to all git commit messages, regardless of whether Copilot was actually used, via a pull request that altered the configuration schema default from 'off' to 'all'. This change raises serious ethical and legal concerns because git commit records are considered technical and legal documents; falsifying co-authorship to inflate AI usage metrics undermines developer trust and could have legal implications. The PR changed the default value of the 'addAICoAuthor' setting to 'all', but the runtime fallback in extensions/git/src/repository.ts still defaults to 'off', creating an inconsistency that could lead to unexpected behavior.

hackernews · indrora · May 2, 19:57

**Background**: Git commit messages often include 'Co-authored-by' trailers to credit multiple contributors. VS Code's Copilot integration allows adding these trailers automatically when Copilot generates code. However, the default being 'all' means even without any Copilot usage, commits will falsely claim Copilot co-authorship, which can distort contribution records and violate attribution norms.

**Discussion**: Commenters express strong disapproval, comparing the change to falsifying legal records and accusing Microsoft of prioritizing AI promotion over user trust. One commenter notes that Copilot itself commented on the PR pointing out the inconsistency, but the comment was ignored. Another user who approved the PR apologized for enabling it by default without sufficient validation.

**Tags**: `#VS Code`, `#Copilot`, `#ethics`, `#git`, `#Microsoft`

---

<a id="item-2"></a>
## [Dav2d: The Fastest Decoder for AV2 Video Codec](https://code.videolan.org/videolan/dav2d) ⭐️ 8.0/10

VideoLAN has published dav2d, an early open-source CPU decoder for the next-generation AV2 video codec, claiming it to be the fastest AV2 decoder on all platforms. Dav2d enables efficient software playback of AV2 content, which promises 30% lower bitrate than AV1, significantly improving streaming quality and reducing bandwidth costs. Dav2d is developed by the same team behind dav1d, focusing on correctness first with future performance optimizations planned for x86, ARM, and RISC-V architectures.

hackernews · dabinat · May 2, 17:32

**Background**: AV2 is the successor to AV1, an open and royalty-free video coding format developed by the Alliance for Open Media. It uses improved compression techniques to deliver better quality at lower bitrates. Dav2d serves as the CPU decoder counterpart to dav1d, which is widely used for AV1 playback.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AV2_(video_coding_format)">AV2 (video coding format)</a></li>
<li><a href="https://www.phoronix.com/news/Dav2d-Open-Source-AV2-Decode">VideoLAN Publishes Dav2d For Open-Source AV2 Decoder</a></li>
<li><a href="https://videocardz.com/newz/videolan-publishes-dav2d-an-early-cpu-decoder-for-av2-video-codec">VideoLAN publishes dav2d, an early CPU decoder for AV2 video ...</a></li>

</ul>
</details>

**Discussion**: The community is excited about AV2's potential, noting a 30% bitrate reduction over AV1 and hoping for a better encoder timeline than AV1. Some users express impatience with web friction (bot checks, cookies) but overall sentiment is positive toward the decoder's release.

**Tags**: `#av2`, `#video-codec`, `#decoder`, `#open-source`, `#video-encoding`

---

<a id="item-3"></a>
## [NetHack 5.0.0: Landmark Update Brings Lua Scripting and Breaks Save Compatibility](https://nethack.org/v500/release.html) ⭐️ 8.0/10

NetHack 5.0.0 has been released, replacing the legacy yacc/lex-based level and dungeon compilers with Lua scripting, and breaking compatibility with all previous saved games and bones files. This is a major technical overhaul of a legendary roguelike after decades, enabling more flexible modding and development; the save incompatibility marks the end of an era for long-time players. The new Lua-based system processes level and dungeon data at runtime instead of build-time; saved games and bones files from any previous version (including 3.7) will not work with 5.0.0.

hackernews · rsaarelm · May 2, 18:03

**Background**: NetHack is a classic open-source roguelike dating back to 1987, known for its deep gameplay, permadeath, and procedural generation. It traditionally used yacc/lex-based tools for level generation and relied on ASCII graphics. Lua is a lightweight scripting language often embedded in games for customization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NetHack">NetHack - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lua">Lua - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community is excited but nostalgic; one player laments losing a 17-year-old save file just before finishing, while others praise the technical modernization and look forward to new possibilities. There is also discussion about 3D client updates.

**Tags**: `#NetHack`, `#roguelike`, `#Lua`, `#game development`, `#open source`

---

<a id="item-4"></a>
## [California to ticket driverless cars for traffic violations](https://www.bbc.com/news/articles/clypjx3rg2go) ⭐️ 8.0/10

California announced it will begin issuing traffic tickets to driverless cars that violate traffic laws, holding autonomous vehicle operators accountable. This regulatory move addresses a key gap in accountability for autonomous vehicles, potentially shaping how AVs are tested and operated nationwide. The ticketing applies to driverless cars operating on public roads, and violations will be tracked to ensure compliance with traffic laws.

hackernews · geox · May 2, 17:59

**Background**: Autonomous vehicles (AVs) are self-driving cars that use sensors and AI to navigate without human input. In California, AVs have been operating on public roads under pilot programs, but until now, traffic violations were often not enforced against driverless vehicles due to the absence of a human driver to ticket.

**Discussion**: Community comments express a mix of support and skepticism. Some users argue that ticketing is a step towards accountability, while others question whether ticketing is the right approach and suggest alternative regulations such as fines or operational bans for frequent violators.

**Tags**: `#autonomous vehicles`, `#regulation`, `#traffic enforcement`, `#Waymo`, `#public safety`

---

<a id="item-5"></a>
## [Six-Year Journey Perfecting Maps on Apple Watch](https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/) ⭐️ 7.0/10

Developer David Smith published a blog post detailing his six-year effort to create a custom maps app for Apple Watch using pre-rendered topographic tiles, culminating in a cartographer-designed basemap. This demonstrates the potential for high-quality, specialized map experiences on Apple Watch, a device often limited by built-in Maps. It inspires developers to push boundaries despite platform constraints. The app uses pre-rendered image tiles instead of dynamic rendering, requiring separate downloads for different zoom levels and rotations. The developer commissioned a cartographer to create a basemap optimized for Apple's Liquid Glass design language.

hackernews · valzevul · May 2, 21:14

**Background**: On Apple Watch, rendering detailed maps in real-time is challenging due to limited hardware and power constraints. Traditional tile-based mapping involves serving small image tiles that can be cached. However, pre-rendered topographic tiles offer better aesthetics and detail than Apple Maps' built-in hiking data, but lack dynamic updates.

<details><summary>References</summary>
<ul>
<li><a href="https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/">Six Years Perfecting Maps on watchOS - david-smith.org</a></li>
<li><a href="https://app.daily.dev/posts/six-years-perfecting-maps-on-watchos-gbhh0hkdn">Six Years Perfecting Maps on watchOS | daily.dev</a></li>

</ul>
</details>

**Discussion**: Commenters praised the attention to detail and evolution of the app, with some lamenting the lack of a first-party hiking map on Apple Watch. Others noted the technical approach of using commissioned cartography and static tiles, which limits interactivity but yields beautiful results.

**Tags**: `#watchOS`, `#maps`, `#cartography`, `#app development`, `#Apple Watch`

---

<a id="item-6"></a>
## [Ladybird Browser April 2026 Newsletter Highlights Progress](https://ladybird.org/newsletter/2026-04-30/) ⭐️ 7.0/10

The April 2026 Ladybird newsletter reports fixes for CSS Doom rendering and Strava login, along with other standards compliance improvements. Reddit is now reportedly working in the browser. Ladybird is a privacy-focused, open-source browser being built from scratch, and steady progress like these fixes shows it is moving toward a usable alpha. This could provide a viable alternative for users who want a browser independent of Chrome or WebKit. The project aims for an alpha release in 2026, beta in 2027, and stable release in 2028. The browser is funded by donations and sponsors including Cloudflare, FUTO, Shopify, and 37signals.

hackernews · richardboegli · May 2, 20:46

**Background**: Ladybird is an open-source web browser originally part of SerenityOS, now a standalone project under the Ladybird Browser Initiative, a non-profit. It aims to be a truly independent browser with its own rendering engine, focusing on privacy and standards compliance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_browser">Ladybird browser</a></li>
<li><a href="https://grokipedia.com/page/Ladybird_web_browser">Ladybird (web browser)</a></li>

</ul>
</details>

**Discussion**: Commenters are impressed with the usability, comparing it to gaming emulator updates and noting that Reddit now works. There is also mention of a similar no-JavaScript browser project from Dioxus. One commenter expresses surprise that Strava checks battery level.

**Tags**: `#browser`, `#open-source`, `#web development`, `#ladybird`, `#rendering`

---

<a id="item-7"></a>
## [Tesla Owner Wins $10K Judgment Over FSD Lies, Tesla Appeals](https://electrek.co/2026/05/02/this-tesla-owner-won-10k-in-court-for-teslas-fsd-lies-tesla-is-still-fighting-him/) ⭐️ 7.0/10

A Tesla owner won a $10,000 court judgment against Tesla for misleading claims about Full Self-Driving (FSD) capabilities, but Tesla is actively fighting the ruling. The case highlights ongoing legal challenges over Tesla's autonomous driving promises. This case could set a precedent for consumer protection in autonomous driving claims, potentially leading to more lawsuits and forcing Tesla to be more cautious with its marketing. It underscores growing skepticism and legal scrutiny of Tesla's FSD technology. The $10,000 award is relatively small, but Tesla's continued fight suggests the company is concerned about establishing a legal benchmark that could open the floodgates to class-action suits. The case involves claims that Tesla's FSD functionality was falsely advertised as fully autonomous.

hackernews · breve · May 2, 22:45

**Background**: Tesla markets its 'Full Self-Driving' (FSD) software as capable of navigating roads autonomously, but critics and regulators argue the name is misleading because the system still requires driver supervision and is not truly autonomous. US courts are increasingly examining whether such claims constitute fraud or deceptive trade practices under consumer protection laws like the Lemon Law and the Beverly Song Act in California.

**Discussion**: Community comments show strong skepticism toward Tesla's FSD claims, with one user recovering $250,000 under California lemon law for similar issues. Others note Tesla is fighting not just the judgment but the precedent it could set, and predict the owner may never see the money without dramatic enforcement actions.

**Tags**: `#Tesla`, `#FSD`, `#legal`, `#autonomous driving`, `#consumer protection`

---

<a id="item-8"></a>
## [macOS VM Performance: How Fast and How Small?](https://eclecticlight.co/2026/05/02/how-fast-is-a-macos-vm-and-how-small-could-it-be/) ⭐️ 7.0/10

An analysis tested macOS VM performance on Apple Silicon, showing that a VM with 2 cores and 4GB RAM can handle lightweight tasks efficiently using only about 3.1GB of memory. This provides practical guidance for optimizing resource allocation in macOS VMs, which is valuable for developers and users running virtualized environments on Apple Silicon Macs. The analysis stepped down from 4 cores/8GB to 2 cores/4GB, showing memory usage decreased from 5GB to 3.1GB while maintaining normal performance. Memory per core includes page cache and concurrency handling overhead.

hackernews · moosia · May 2, 09:30

**Background**: macOS virtualization on Apple Silicon uses the Virtualization framework, which allows running macOS VMs with configurable CPU and memory. However, GPU passthrough (especially for compute) remains limited, as noted in community comments.

**Discussion**: Commenters appreciated the practical benchmarks, noting that memory tied to cores explains the observed usage. One user mentioned difficulty with GPU acceleration for PyTorch in VMs, and another pointed out that Docker on macOS via VMs is inefficient.

**Tags**: `#macOS`, `#virtualization`, `#performance`, `#VM`, `#Apple Silicon`

---

<a id="item-9"></a>
## [Roblox Stock Plunges 18% on Child Safety Communication Restrictions](https://www.cnbc.com/2026/05/01/roblox-rblx-stock-child-safety-earnings.html) ⭐️ 7.0/10

Roblox implemented age-based communication restrictions dividing users into six age groups and banning most cross-group chat, leading to an 18% stock drop after the company lowered its 2026 bookings forecast due to expected impact on user engagement and monetization. This event highlights the tension between child safety and platform growth, as safety measures can reduce user activity and revenue in the short term but may be necessary for long-term viability, especially for platforms with large underage user bases. The age groups are under 9, 9–12, 13–15, 16–17, 18–20, and 21+, with users only able to communicate with others within one age band of their own. Roblox also introduced mandatory face verification for chat, which has been criticized for privacy concerns and usability issues.

hackernews · 1vuio0pswjnm7 · May 2, 17:10

**Background**: Roblox is a popular online gaming platform where users create and play games, with a large proportion of young users. The company has faced scrutiny over child safety, leading to these new measures. Age verification and communication restrictions are common approaches to protect minors, but they can disrupt the social dynamics that drive engagement on such platforms.

**Discussion**: Community commentators are divided: some criticize the measures as heavy-handed and damaging to the social experience, while others argue that long-term safety is worth short-term revenue loss. A key point is that the age-based chat restrictions break many games' social features, and face verification raises privacy and human rights concerns.

**Tags**: `#safety measures`, `#platform design`, `#stock market`, `#age verification`, `#social gaming`

---

<a id="item-10"></a>
## [Uber plans to use drivers' cars as sensor grid for AVs](https://techcrunch.com/2026/05/01/uber-wants-to-turn-its-millions-of-drivers-into-a-sensor-grid-for-self-driving-companies/) ⭐️ 7.0/10

Uber announced a long-term plan to outfit its human drivers' vehicles with sensors, creating a massive data grid to supply real-world driving data to autonomous vehicle companies, including those it has invested in. If successful, this could accelerate AV development by providing cheaper or more diverse data, but it raises concerns about driver consent, compensation, privacy, and regulatory hurdles. The community is skeptical about the claimed data bottleneck. Uber aims to eventually install LIDAR and other sensors on privately-owned driver vehicles, but the timeline is unclear and regulatory clarity on data sharing is a prerequisite. The program also includes 'shadow mode,' letting AV companies test their models against millions of real Uber trips without deploying physical fleets.

hackernews · nickvec · May 2, 15:38

**Background**: Autonomous vehicle development relies heavily on large amounts of real-world driving data to train AI models. Companies like Waymo collect their own data, often using expensive sensor-laden vehicles. Uber's proposal would leverage its existing driver network as a cost-effective data source, but critics argue that the real bottleneck is not data volume but handling rare edge cases and transient situations.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/05/01/uber-wants-to-turn-its-millions-of-drivers-into-a-sensor-grid-for-self-driving-companies/">Uber wants to turn its millions of drivers into a sensor grid ...</a></li>
<li><a href="https://pulse24.ai/news/2026/5/2/13/uber-plans-driver-sensor-grid">Uber Plans Driver Sensor Grid - pulse24.ai</a></li>
<li><a href="https://newsgab.com/uber-wants-drivers-as-sensor-grid-for-self-driving-firms/">Uber Wants Drivers To Act As A Sensor Grid For Self-driving ...</a></li>

</ul>
</details>

**Discussion**: The community is highly skeptical. Commenters like Animats argued that more mapping data won't help with transient problems, and that Google StreetView data may suffice. Others questioned the feasibility of installing expensive LIDAR on private cars, noted that AV companies already have data, and pointed out conflicts of interest with Uber taking equity in the same AV firms it supplies.

**Tags**: `#self-driving`, `#Uber`, `#data collection`, `#autonomous vehicles`, `#sensors`

---

<a id="item-11"></a>
## [Proposed DO_NOT_TRACK Environment Variable Revives Privacy Debates](https://donottrack.sh/) ⭐️ 6.0/10

A new project at donottrack.sh proposes standardizing a DO_NOT_TRACK environment variable to allow users to globally opt out of telemetry and tracking in CLI and TUI applications, but the initiative faces skepticism due to the historical failure of the DNT browser header. If adopted, this could simplify privacy controls for developers and users across many command-line tools, but the lack of enforcement and past abandonment of DNT suggest it may suffer similar fate without strong industry backing. The proposal centralizes existing per-tool environment variables like HF_HUB_DISABLE_TELEMETRY into a single DO_NOT_TRACK flag, but community members note that a similar attempt years ago went nowhere and that opt-in defaults remain problematic.

hackernews · RubyGuy · May 2, 17:40

**Background**: Environment variables like DO_NOT_TRACK are a convention to signal telemetry preferences to applications. The earlier Do Not Track (DNT) HTTP header, intended to let users opt out of web tracking, was abandoned by W3C and removed from major browsers by 2025 due to non-compliance and lack of legal enforcement. The new proposal aims to replicate the concept for command-line tools, but faces similar challenges of voluntary adoption.

<details><summary>References</summary>
<ul>
<li><a href="https://donottrack.sh/">DO_NOT_TRACK</a></li>
<li><a href="https://en.wikipedia.org/wiki/Do_Not_Track">Do Not Track - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments express significant skepticism: a user notes a similar proposal years ago went nowhere, another criticizes the implied default of 'CONSENT_TO_TRACK=1', and one suggests that any tool supporting the spec publicly is likely a honeypot that collects telemetry without explicit opt-in. Practical difficulties are also highlighted, such as the need for multiple env vars to truly stop telemetry (e.g., HF_HUB_OFFLINE=1 in addition to HF_HUB_DISABLE_TELEMETRY).

**Tags**: `#privacy`, `#telemetry`, `#environment-variables`, `#developer-tools`

---

<a id="item-12"></a>
## [Open Design: Using Coding Agents for Design](https://github.com/nexu-io/open-design) ⭐️ 6.0/10

A GitHub repository called Open Design proposes using AI coding agents as a design engine for creating UI layouts, pitch decks, and other design artifacts. The concept has sparked debate in the community about the quality and efficiency of AI-generated design. This approach could lower the barrier to producing professional-looking designs, especially for non-designers. However, the community skepticism highlights concerns about token inefficiency, generic outputs, and the risk of devaluing genuine design work. The repository outlines conceptual ideas but lacks concrete implementation demonstrations; users have noted that the README reads like a sales pitch. Comments also point out that Claude's approach in the demo is token-inefficient compared to alternatives like ChatGPT image generation.

hackernews · steveharing1 · May 2, 12:16

**Background**: AI coding agents are tools that use large language models to autonomously write and refine code based on natural language prompts. 'Vibe coding' is a term for using such agents to rapidly generate frontend code, but the community is divided on whether this approach produces high-quality, maintainable design versus merely churning out generic output.

<details><summary>References</summary>
<ul>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>
<li><a href="https://zencoder.ai/">Zencoder | The AI Coding Agent</a></li>
<li><a href="https://kilo.ai/">Kilo - Kilo: The Open Source AI Coding Agent for VS Code , JetBrains...</a></li>

</ul>
</details>

**Discussion**: Commenters broadly express skepticism: jshaqaw warns that AI-generated design becomes worthless background noise; ricardobeat criticizes the 'Claude-salesman' writing style; Saline9515 complains about token waste and praises ChatGPT for efficiency; lmeyerov asks about productive workflows; MSaiRam10 calls the README a sales deck and questions the high star count.

**Tags**: `#AI`, `#design`, `#coding agents`, `#GitHub`, `#Hacker News`

---

<a id="item-13"></a>
## [Why Windows Has Both TMP and TEMP Variables](https://devblogs.microsoft.com/oldnewthing/20150417-00/?p=44213) ⭐️ 6.0/10

Raymond Chen's 2015 blog post explains that the coexistence of TMP and TEMP environment variables in Windows stems from historical practices in CP/M and early MS-DOS, where different programs used different variable names for temporary file directories. This minor inconsistency illustrates how legacy decisions from the 1970s and 1980s persist in modern operating systems, affecting software compatibility and system configuration for developers and power users. The article notes that CP/M had no standard variable name, so programs hardcoded either 'TMP' or 'TEMP', and MS-DOS later inherited both. The 8.3 filename convention may have influenced adoption of the three-letter 'TMP'.

hackernews · ankitg12 · May 2, 08:23

**Background**: CP/M was a dominant operating system for microcomputers in the late 1970s and early 1980s, developed by Gary Kildall. MS-DOS, created by Microsoft for the IBM PC, borrowed many concepts from CP/M, including environment variables. The lack of a single standard led to the duplication seen today.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CP/M_operating_system">CP/M operating system</a></li>
<li><a href="https://en.wikipedia.org/wiki/MS-DOS">MS-DOS - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted that CP/M programs were often configured by patching binary files, and one corrected the initial date of CP/M to 1974 not 1973. They also drew parallels to inconsistent HTTP proxy environment variables on Unix and remarked that such early decisions tend to persist indefinitely.

**Tags**: `#environment variables`, `#Windows`, `#history`, `#CP/M`, `#MS-DOS`

---