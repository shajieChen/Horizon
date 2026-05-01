---
layout: default
title: "Horizon Summary: 2026-05-01 (EN)"
date: 2026-05-01
lang: en
---

> From 19 items, 16 important content pieces were selected

---

1. [CopyFail disclosure controversy: kernel security team blamed](#item-1) ⭐️ 9.0/10
2. [Malware Disguised as Dependency Hits PyTorch Lightning](#item-2) ⭐️ 9.0/10
3. [Rivian allows full internet disablement in vehicles](#item-3) ⭐️ 8.0/10
4. [Mark Klein Exposed NSA's Room 641A to EFF](#item-4) ⭐️ 8.0/10
5. [Claude Code penalizes OpenClaw mentions: session drops or overcharge](#item-5) ⭐️ 8.0/10
6. [Belgium Reverses Nuclear Phase-Out, Keeps Plants Running](#item-6) ⭐️ 8.0/10
7. [Spain's Parliament to Act Against LaLiga's Overbroad IP Blocks](#item-7) ⭐️ 8.0/10
8. [UK AI Security Institute Evaluates GPT-5.5 Cyber Capabilities](#item-8) ⭐️ 8.0/10
9. [Andrew Kelley: LLM-assisted PRs have a detectable 'digital smell'](#item-9) ⭐️ 8.0/10
10. [Building a Game Boy Emulator in F#](#item-10) ⭐️ 7.0/10
11. [honker: Durable queues, pub/sub, and cron inside SQLite](#item-11) ⭐️ 7.0/10
12. [Codex CLI 0.128.0 adds /goal autonomous looping](#item-12) ⭐️ 7.0/10
13. [We need RSS for sharing abundant vibe-coded apps](#item-13) ⭐️ 7.0/10
14. [Zig's Strict Anti-LLM Contribution Policy Explained](#item-14) ⭐️ 7.0/10
15. [How an Oil Refinery Works: Distillation to Final Products](#item-15) ⭐️ 6.0/10
16. [Aggregator for 28 US Gov Auction Sites Launched](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [CopyFail disclosure controversy: kernel security team blamed](https://www.openwall.com/lists/oss-security/2026/04/30/10) ⭐️ 9.0/10

The CopyFail vulnerability (CVE-2026-31431) was publicly disclosed with a working exploit on the oss-security mailing list before distribution maintainers were notified, sparking criticism of the Linux kernel security team's disclosure process. This failure could allow attackers to exploit shared hosting environments, and it highlights systemic issues in how kernel vulnerabilities are coordinated with downstream distributors, potentially affecting millions of Linux systems. The vulnerability is a local privilege escalation in the Linux kernel crypto API (AF_ALG), affecting kernels built between 2017 and the patch availability. A proof-of-concept Python script was shared before distributions could ship fixes.

hackernews · ori_b · Apr 30, 16:43

**Background**: The Linux kernel security vulnerability coordination process traditionally relies on reporters to optionally bring vulnerabilities to the linux-distros mailing list for advance notification to distributions. This places the burden on reporters, who may not be familiar with the process, while the kernel security team does not proactively notify downstream distributors. The CopyFail case exemplifies this broken communication.

<details><summary>References</summary>
<ul>
<li><a href="https://www.openwall.com/lists/oss-security/2026/04/29/23">oss-security - CVE-2026-31431: CopyFail : linux local privilege scalation</a></li>
<li><a href="https://cert.europa.eu/publications/security-advisories/2026-005/">CERT-EU - High Vulnerability in the Linux Kernel (" Copy Fail ")</a></li>

</ul>
</details>

**Discussion**: Commenters strongly criticized the kernel security team for not notifying distributions, arguing that the reporter should not be blamed. One user shared an eBPF-based mitigation workaround, while another suggested default filesystem mount options like nosuid and nodev to reduce impact.

**Tags**: `#Linux kernel`, `#vulnerability disclosure`, `#security`, `#CopyFail`, `#distribution maintainers`

---

<a id="item-2"></a>
## [Malware Disguised as Dependency Hits PyTorch Lightning](https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/) ⭐️ 9.0/10

A malware named Shai-Hulud was discovered embedded in a dependency of the PyTorch Lightning AI training library, targeting systems that install the malicious package. This attack underscores the growing supply chain vulnerabilities in open-source AI tools, potentially affecting thousands of projects that rely on PyTorch Lightning and raising concerns about dependency security. Security researchers identified the malware after noticing suspicious behavior; within a day, over 2,200 repositories contained a distinctive string from the malware, suggesting widespread automated propagation.

hackernews · j12y · Apr 30, 16:09

**Background**: PyTorch Lightning is a high-level interface for PyTorch, widely used to simplify deep learning training code. A supply chain attack occurs when malicious code is introduced through a trusted third-party component, such as a library dependency, compromising downstream users.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PyTorch_Lightning">PyTorch Lightning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack</a></li>

</ul>
</details>

**Discussion**: Commenters noted an apparent increase in supply chain attacks recently, with some advocating for minimal dependencies. Others observed the rapid creation of repositories containing the malware's string, emphasizing the scale of automated exploitation.

**Tags**: `#security`, `#supply chain attack`, `#PyTorch Lightning`, `#malware`, `#open source`

---

<a id="item-3"></a>
## [Rivian allows full internet disablement in vehicles](https://rivian.com/support/article/can-i-disable-all-data-collection-from-my-vehicle) ⭐️ 8.0/10

Rivian has introduced a new setting that allows owners to disable all internet connectivity in their vehicles, including cellular and Wi-Fi, effectively turning off the telematics control unit and stopping data collection. This move addresses growing privacy concerns about automakers collecting excessive personal data, but it raises questions about how safety recalls and over-the-air updates will be handled if connectivity is disabled. Disabling connectivity means the vehicle will no longer receive over-the-air updates, including critical safety enhancements, and it is unclear if dealers can still perform updates via physical connections like J2534 passthrough devices.

hackernews · Cider9986 · Apr 30, 20:27

**Background**: Modern vehicles are equipped with a telematics control unit (TCU) that connects to the internet for data collection and over-the-air (OTA) software updates. OTA updates allow automakers to remotely fix bugs, add features, or address safety issues without a dealer visit. Traditionally, software updates required a physical connection, but OTA has become standard in electric vehicles.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Over-the-air_update">Over - the - air update - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Telematic_control_unit">Telematic control unit</a></li>
<li><a href="https://www.cinch.co.uk/guides/car-maintenance/over-the-air-car-updates">OTA updates in cars – what are over - the - air updates ? - cinch</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed reactions: bri3d worried about safety recalls if OTA is disabled and questioned if dealers can update modules otherwise. Cider9986 highlighted a Mozilla study showing other automakers collect intrusive data like sexual activity. jryio and jamilbk praised Rivian for offering an official privacy option, with jamilbk noting he previously had to physically disconnect the antenna.

**Tags**: `#privacy`, `#automotive`, `#IoT`, `#consumer rights`, `#OTA updates`

---

<a id="item-4"></a>
## [Mark Klein Exposed NSA's Room 641A to EFF](https://thereader.mitpress.mit.edu/the-whistleblower-who-uncovered-the-nsas-big-brother-machine/) ⭐️ 8.0/10

A book excerpt reveals how AT&T technician Mark Klein contacted the Electronic Frontier Foundation (EFF) in 2006 to disclose the existence of Room 641A, a secret NSA surveillance facility inside an AT&T building in San Francisco. This whistleblowing event helped the public understand the scale of government mass surveillance and led to the landmark lawsuit Hepting v. AT&T, which shaped U.S. privacy law and public debate on surveillance. Room 641A contained a Narus STA 6400 device capable of deep packet inspection, allowing the NSA to intercept and analyze internet traffic at high speeds. Klein risked his career to provide documents to the EFF.

hackernews · the-mitr · Apr 30, 16:41

**Background**: Room 641A was a telecommunication interception facility operated by AT&T for the NSA, part of a mass surveillance program that began in 2003. It was located at 611 Folsom Street in San Francisco. Mark Klein, an AT&T technician, discovered the room and later leaked internal documents to the EFF, revealing the government's warrantless wiretapping program.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Room_641A">Room 641A - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Narus_Inc.">Narus Inc. - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters largely praised Klein as a hero, with some noting their own proximity to similar surveillance infrastructure. One user corrected historical inaccuracies about the pre-9/11 wall between foreign and domestic surveillance, while another offered a skeptical view that technological advances inevitably erode freedom.

**Tags**: `#NSA`, `#surveillance`, `#whistleblower`, `#privacy`, `#civil liberties`

---

<a id="item-5"></a>
## [Claude Code penalizes OpenClaw mentions: session drops or overcharge](https://twitter.com/theo/status/2049645973350363168) ⭐️ 8.0/10

Claude Code has been reported to abruptly terminate sessions or impose excessive usage charges when users include the term 'OpenClaw' in git commit messages or other contexts. Multiple users independently reproduced this behavior, demonstrating a direct causal link. This behavior raises serious concerns about potential censorship or anti-competitive practices in AI tools, undermining user trust. It also highlights growing tensions between proprietary AI services like Claude and open-source alternatives like OpenClaw. In a controlled test, a user created a fresh git repository, committed a message containing 'openclaw.inbound_meta.v1', and then ran 'claude -p hi' — resulting in immediate disconnection and session usage hitting 100%. Another user reported that even linking to openclaw.ai in a chat triggered the same response.

hackernews · elmean · Apr 30, 14:36

**Background**: OpenClaw is a free, open-source AI agent that competes with Anthropic's Claude products. Claude Code is a command-line tool that uses AI to assist with coding tasks. The reported blocking may stem from Anthropic attempting to protect its service from load or usage driven by OpenClaw, though such tactics are controversial.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://openclaw.ai/">OpenClaw — Personal AI Assistant</a></li>

</ul>
</details>

**Discussion**: Community comments show a mix of frustration and analysis. Several users reproduced the issue, while others speculated about internal company pressures. One commenter noted that OpenClaw-driven load might be seen as an existential threat, prompting such heavy-handed measures.

**Tags**: `#AI ethics`, `#Claude`, `#censorship`, `#usage limits`

---

<a id="item-6"></a>
## [Belgium Reverses Nuclear Phase-Out, Keeps Plants Running](https://dpa-international.com/general-news/urn:newsml:dpa.com:20090101:260430-930-14717/) ⭐️ 8.0/10

Belgium has reversed its nuclear phase-out policy, deciding to continue operating its existing nuclear power plants instead of decommissioning them. The government plans to acquire all nuclear assets from French utility Engie, effectively nationalizing the reactors. This shift marks a significant change in European energy policy, as countries reconsider nuclear power for climate goals and energy security. It could encourage other nations to extend nuclear plant lifetimes, impacting global energy transition efforts. Belgium had a phase-out law from 2003 requiring reactor closures, but recent geopolitical events and climate targets prompted the reversal. The government will take over the reactors from Engie, with the deal ensuring continued low-carbon electricity generation.

hackernews · mpweiher · Apr 30, 12:17

**Background**: Nuclear power provides baseload electricity with low carbon emissions, but decommissioning is costly and takes decades. Many countries planned phase-outs after the Fukushima disaster, but rising emissions targets and energy security concerns—especially after Russia's invasion of Ukraine—have led some to reconsider. Belgium's decision aligns with broader EU efforts to support both nuclear and renewables.

<details><summary>References</summary>
<ul>
<li><a href="https://www.politico.eu/article/belgium-eyes-nuclear-takeover-to-keep-reactors-running/">Belgium eyes nuclear takeover to keep reactors running</a></li>
<li><a href="https://brusselssignal.eu/2026/04/belgium-takes-over-entire-nuclear-fleet-from-engie-in-surprise-move/">Belgium takes over entire nuclear fleet from Engie in ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nuclear_decommissioning">Nuclear decommissioning - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Comments reflect a split: strong pro-nuclear advocates argue that opposing nuclear in a climate crisis is a historical mistake, while others raise concerns about waste storage and cost. Some note broader EU policy supporting both nuclear and renewables, with one comment highlighting that Germany still hasn't found a permanent waste storage site.

**Tags**: `#nuclear energy`, `#climate policy`, `#Belgium`, `#energy transition`, `#nuclear power`

---

<a id="item-7"></a>
## [Spain's Parliament to Act Against LaLiga's Overbroad IP Blocks](https://www.democrata.es/en/politics/congress-and-senate/congress-will-act-against-massive-ip-blockages-by-laliga/) ⭐️ 8.0/10

Spain's Congress has announced it will take parliamentary action against LaLiga's court-ordered IP blocking, which inadvertently blocked legitimate websites using shared Cloudflare IP addresses. This marks a significant policy shift, as parliamentary intervention could lead to legal reforms that limit overreaching IP blocking and protect net neutrality, affecting how copyright enforcement balances with internet freedom. LaLiga's blocking targeted IPs associated with illegal streaming during matches, but many were shared Cloudflare IPs, causing widespread collateral damage to unrelated sites. The parliamentary action signals that lawmakers recognize the need for a stopping principle in such enforcement.

hackernews · akyuu · Apr 30, 15:31

**Background**: IP-level blocking is a blunt instrument; when multiple domains share the same IP (e.g., via CDNs like Cloudflare), blocking that IP affects all those domains. LaLiga obtained a court order to block IPs during matches to combat piracy, but this resulted in legitimate services becoming unavailable. Similar issues have been observed in other countries, such as Italy's Piracy Shield.

<details><summary>References</summary>
<ul>
<li><a href="https://dn.org/collateral-damage-of-isp-level-dns-blocking-orders/">Collateral Damage of ISP-Level DNS Blocking Orders - dn.org</a></li>
<li><a href="https://vercel.com/blog/update-on-spain-and-laliga-blocks-of-the-internet">Update on Spain and LALIGA blocks of the internet - Vercel – Vercel</a></li>
<li><a href="https://labs.ripe.net/author/antonio-prado/live-event-blocking-at-scale-effectiveness-vs-collateral-damage-in-italys-piracy-shield/">Live-Event Blocking at Scale: Effectiveness vs. Collateral ...</a></li>

</ul>
</details>

**Discussion**: Comments on Hacker News express relief and frustration: users like dbbk (running an event ticketing business) report unacceptable downtime, and pier25 notes the blocking didn't solve piracy. Others discuss the lack of a stopping principle and the need for better oversight.

**Tags**: `#internet freedom`, `#IP blocking`, `#net neutrality`, `#Spain`, `#LaLiga`

---

<a id="item-8"></a>
## [UK AI Security Institute Evaluates GPT-5.5 Cyber Capabilities](https://simonwillison.net/2026/Apr/30/gpt-55-cyber-capabilities/#atom-everything) ⭐️ 8.0/10

The UK AI Security Institute (AISI) published an evaluation of OpenAI's GPT-5.5 model, finding its cybersecurity capabilities comparable to Anthropic's Claude Mythos. Unlike Mythos, GPT-5.5 is generally available to the public. This independent assessment provides crucial transparency regarding the cybersecurity risks of advanced AI models. GPT-5.5's public availability means a broader range of actors could potentially exploit its cyber capabilities. The evaluation focused on the models' ability to identify security vulnerabilities. Claude Mythos had been tested previously but was not released to the public due to safety concerns.

rss · Simon Willison · Apr 30, 23:03

**Background**: The AI Security Institute (AISI) is a UK government research organization established to assess risks from advanced AI and inform policy. It has access agreements with major AI labs to test models before release. Claude Mythos is a powerful AI model from Anthropic that was previewed to select companies in 2026 but not widely released. GPT-5.5 is OpenAI's latest generation model with enhanced capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UK_AI_Security_Institute">UK AI Security Institute</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model ) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#ai`, `#openai`, `#llms`, `#ai-security-research`, `#gpt-5.5`

---

<a id="item-9"></a>
## [Andrew Kelley: LLM-assisted PRs have a detectable 'digital smell'](https://simonwillison.net/2026/Apr/30/andrew-kelley/#atom-everything) ⭐️ 8.0/10

Andrew Kelley, creator of the Zig programming language, argues that LLM-assisted pull requests are identifiable through distinct error patterns and a characteristic 'digital smell' that is obvious to those who don't use them. This perspective challenges the common belief that AI-assisted code is indistinguishable from human-written code, impacting code review practices and open-source contribution policies. Kelley compares the phenomenon to a smoker entering a room, noting that those who avoid LLMs can easily detect its use. He adds that while he does not prohibit using LLMs elsewhere, he does not want them in his project's contributions.

rss · Simon Willison · Apr 30, 21:24

**Background**: Zig is a system programming language designed as a modern alternative to C, created by Andrew Kelley in 2016. 'Agentic coding' refers to the use of autonomous AI agents that plan, write, test, and modify code with minimal human intervention, often leveraging large language models (LLMs).

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>
<li><a href="https://ziglang.org/">Home Zig Programming Language</a></li>

</ul>
</details>

**Tags**: `#zig`, `#llms`, `#AI-assisted coding`, `#open source`, `#code review`

---

<a id="item-10"></a>
## [Building a Game Boy Emulator in F#](https://nickkossolapov.github.io/fame-boy/building-a-game-boy-emulator-in-fsharp/) ⭐️ 7.0/10

A developer created a fully functional Game Boy emulator using F#, sharing the design decisions and challenges encountered when applying functional programming to low-level hardware emulation. This project demonstrates that functional languages like F# can be used for performance-sensitive emulation tasks, challenging the dominance of imperative approaches. It also provides an educational resource for learning F# through a real-world project. The emulator, named 'Fame Boy', uses discriminated unions for opcodes and register access patterns typical of F# idioms. The author noted trade-offs between functional purity and imperative-style speed optimizations.

hackernews · elvis70 · Apr 30, 17:14

**Background**: F# is a multi-paradigm language on .NET that emphasizes functional programming. Game Boy emulators simulate the hardware of the original handheld console, requiring accurate CPU instruction execution, graphics rendering, and input handling. Traditionally, such emulators are written in C or C++ for performance, making a functional implementation noteworthy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F_Sharp_(programming_language)">F Sharp (programming language) - Wikipedia</a></li>
<li><a href="https://github.com/gbdev/awesome-gbdev">GitHub - gbdev/awesome-gbdev: A curated list of Game Boy ...</a></li>

</ul>
</details>

**Discussion**: Commenters praised the project's educational value and noted that emulators are a great way to learn a language. Some suggested performance improvements like marking discriminated unions as structs, while others discussed F#'s ecosystem limitations compared to C#.

**Tags**: `#F#`, `#emulator`, `#Game Boy`, `#functional programming`, `#.NET`

---

<a id="item-11"></a>
## [honker: Durable queues, pub/sub, and cron inside SQLite](https://honker.dev/) ⭐️ 7.0/10

honker is a new SQLite extension and language bindings that bring Postgres-style NOTIFY/LISTEN semantics to SQLite, enabling durable pub/sub, task queues, event streams, and a cron scheduler without needing a separate broker. This project challenges the conventional need for separate queue systems like Redis or Celery for SQLite-backed apps, potentially simplifying architectures for single-writer applications. It demonstrates a creative use of SQLite's polling mechanism for real-time patterns. honker polls SQLite's PRAGMA data_version every millisecond, a ~3µs read that detects commits across any connection, enabling cross-process notification without kernel file watchers. It supports durable queues, streams, pub/sub, and a cron scheduler, all inside a single SQLite file.

hackernews · ferriswil · Apr 30, 14:43

**Background**: SQLite is a single-writer database commonly used in embedded and single-process applications. For inter-process or inter-thread communication, developers typically add external message brokers like Redis or RabbitMQ. Polling is a technique where an application repeatedly checks for changes; honker uses a very lightweight polling method to avoid busy-wait penalties.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/russellromney/honker">GitHub - russellromney/honker: SQLite extension + bindings for Postgres NOTIFY/LISTEN semantics with durable queues, streams, pub/sub, and scheduler · GitHub</a></li>
<li><a href="https://github.com/litements/litequeue">GitHub - litements/litequeue: Queue built on top of SQLite · GitHub</a></li>
<li><a href="https://dev.to/minnzen/building-a-durable-message-queue-on-sqlite-for-ai-agent-orchestration-335m">Building a Durable Message Queue on SQLite for AI Agent Orchestration - DEV Community</a></li>

</ul>
</details>

**Discussion**: Comments raise concerns about polling overhead and the single-writer limitation, with some arguing that a ring buffer and futex might be more efficient. Others question why not implement similar logic in the application layer given SQLite's constraints. Overall, the community finds the approach interesting but debatable for production use.

**Tags**: `#SQLite`, `#message-queues`, `#polling`, `#database`, `#pub-sub`

---

<a id="item-12"></a>
## [Codex CLI 0.128.0 adds /goal autonomous looping](https://simonwillison.net/2026/Apr/30/codex-goals/#atom-everything) ⭐️ 7.0/10

OpenAI's Codex CLI version 0.128.0 introduces the /goal command, which enables the agent to autonomously loop through tasks until the goal is completed or the token budget is exhausted. This feature brings a Ralph-loop-like autonomous coding capability to Codex CLI, significantly reducing manual oversight for complex multi-step tasks and making AI-driven development more efficient. The /goal command is primarily implemented via two prompt templates: goals/continuation.md and goals/budget_limit.md, which are automatically injected at the end of each turn. The agent evaluates goal completion after each loop iteration.

rss · Simon Willison · Apr 30, 23:23

**Background**: The Ralph loop is an open-source autonomous coding loop pattern that allows AI agents to recursively run sessions until a goal is met. Inspired by The Simpsons character Ralph Wiggum, it has become popular for enabling continuous, self-healing development cycles. Codex CLI is OpenAI's command-line coding agent that assists with software development tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://ralphwiggum.org/">Ralph Wiggum – Autonomous Recursive Coding Loop</a></li>
<li><a href="https://medium.com/@tentenco/what-is-ralph-loop-a-new-era-of-autonomous-coding-96a4bb3e2ac8">What is Ralph Loop? A New Era of Autonomous Coding</a></li>
<li><a href="https://ralphify.co/docs/how-it-works/">How Autonomous AI Coding Loops Work — The Ralph Loop ...</a></li>

</ul>
</details>

**Tags**: `#AI coding assistant`, `#Codex CLI`, `#autonomous coding`, `#tool update`

---

<a id="item-13"></a>
## [We need RSS for sharing abundant vibe-coded apps](https://simonwillison.net/2026/Apr/30/rss-vibe-coded-apps/#atom-everything) ⭐️ 7.0/10

Matt Webb proposed using RSS feeds to syndicate vibe-coded micro-apps, treating app publishing like blogging. Simon Willison implemented an Atom feed for his tools page, populated from tools.simonwillison.net. This proposal addresses the need for discoverability and distribution of AI-generated micro-apps, which are becoming more personal and frequent. It could lead to a new ecosystem of syndicated app feeds, making it easy for users to subscribe and install tools. Willison used Claude to add an Atom feed to his /elsewhere/tools/ page, which is populated from tools.simonwillison.net. The feed includes an 'Install' button for each item, as suggested by Webb.

rss · Simon Willison · Apr 30, 18:38

**Background**: Vibe coding is a software development practice where AI assistants like Claude or Codex help write code, focusing on directing the mission rather than writing syntax. RSS and Atom are web feed formats that allow users to subscribe to updates from websites, commonly used for blogs and news. This proposal applies the same concept to micro-apps.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Atom_(web_standard)">Atom (web standard) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#rss`, `#vibe-coding`, `#atom`, `#micro-apps`, `#ai-assisted coding`

---

<a id="item-14"></a>
## [Zig's Strict Anti-LLM Contribution Policy Explained](https://simonwillison.net/2026/Apr/30/zig-anti-ai/#atom-everything) ⭐️ 7.0/10

Zig enforces a stringent policy banning all LLM-generated content in issues, pull requests, and comments, including translations. The prominent Zig-based project Bun, acquired by Anthropic, has created a fork of Zig with 4x faster compilation but will not upstream it due to this policy. This policy highlights a growing tension in open source over AI-assisted contributions, prioritizing contributor development over code volume. It could influence how other projects balance innovation, community building, and AI usage. Zig's code of conduct explicitly bans LLMs for issues, PRs, and comments, even for translation. Zig's VP of Community, Loris Cro, frames the policy as 'contributor poker,' where the project invests in growing contributors rather than just accepting contributions.

rss · Simon Willison · Apr 30, 01:24

**Background**: Zig is a general-purpose systems programming language aimed at improving on C, known for manual memory management and compile-time features. Bun is a fast all-in-one JavaScript runtime written in Zig, recently acquired by Anthropic. The contrast between Zig's strict policy and Bun's AI-heavy approach illustrates divergent philosophies in open source.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Zig`, `#open source`, `#AI policy`, `#LLM`, `#Bun`

---

<a id="item-15"></a>
## [How an Oil Refinery Works: Distillation to Final Products](https://www.construction-physics.com/p/how-an-oil-refinery-works) ⭐️ 6.0/10

A new illustrated article explains the step-by-step process of oil refining, from crude oil distillation to final product processing, with detailed diagrams. It covers key unit operations such as fractional distillation and catalytic cracking. This article matters because it demystifies a critical industrial process that underpins much of the global economy, though it is not directly related to software engineering or AI/ML. It provides accessible technical knowledge for a general audience. The article covers fractional distillation, catalytic cracking, and other conversion processes, but does not address energy efficiency or the 'primary energy fallacy' mentioned by commenters. It focuses on the technical flow from crude oil to final products.

hackernews · chmaynard · Apr 30, 13:54

**Background**: An oil refinery converts crude oil, a complex mixture of hydrocarbons, into useful products like gasoline, diesel, and jet fuel. The primary separation process is fractional distillation, where crude oil is heated and its components are separated by boiling point in a distillation column. Heavier fractions like gas oil undergo catalytic cracking, where large hydrocarbon molecules are broken into smaller ones, yielding more gasoline. The article illustrates these processes with diagrams.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fractional_distillation">Fractional distillation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Catalytic_cracking">Catalytic cracking</a></li>

</ul>
</details>

**Discussion**: Commenters shared personal experiences, such as a user whose father works at the world's largest refinery in Jamnagar. Some pointed out that the article fails to address energy waste (the 'primary energy fallacy'), while others shared links to related resources like the SimRefinery game. The discussion shows high community interest in the topic.

**Tags**: `#oil refinery`, `#industrial processes`, `#energy`, `#engineering`

---

<a id="item-16"></a>
## [Aggregator for 28 US Gov Auction Sites Launched](https://bidprowl.com/) ⭐️ 6.0/10

A developer launched BidProwl, a search engine that aggregates listings from 28 US government auction websites into a single unified interface. This tool simplifies finding government surplus and seized property auctions, saving users time and effort, though it faces competition from a similar project called GovAuctions. Users report server load issues preventing state pages from loading, and the site does not filter out already finished auctions, showing winning bids on listed items.

hackernews · scarsam · Apr 30, 12:24

**Background**: US government auction sites sell surplus property and items seized via civil asset forfeiture. Aggregators like BidProwl scrape multiple sites to provide a centralized search, but technical challenges like server stability and data freshness are common.

**Discussion**: Comments note BidProwl appears to be a clone of the earlier GovAuctions project. There are server issues and missing finished auction filters. Some users question how much of the inventory comes from civil asset forfeiture.

**Tags**: `#government auctions`, `#data aggregation`, `#open data`, `#web scraping`

---