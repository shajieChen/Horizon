---
layout: default
title: "Horizon Summary: 2026-04-29 (EN)"
date: 2026-04-29
lang: en
---

> From 39 items, 16 important content pieces were selected

---

1. [Ghostty leaves GitHub: Mitchell Hashimoto moves away](#item-1) ⭐️ 9.0/10
2. [OpenAI models to be available on Amazon Bedrock](#item-2) ⭐️ 9.0/10
3. [Critical GitHub RCE Vulnerability CVE-2026-3854](#item-3) ⭐️ 9.0/10
4. [Google Pushes Android Towards Walled Garden, Curtailing User Control](#item-4) ⭐️ 9.0/10
5. [Talkie: A 13B Vintage Language Model Trained on Pre-1931 Text](#item-5) ⭐️ 9.0/10
6. [Reflecting on Software Development Before GitHub](#item-6) ⭐️ 8.0/10
7. [Who owns AI coding agent output?](#item-7) ⭐️ 8.0/10
8. [Warp terminal emulator goes open source](#item-8) ⭐️ 8.0/10
9. [UAE announces exit from OPEC](#item-9) ⭐️ 8.0/10
10. [GitHub Availability Update Faces Community Skepticism](#item-10) ⭐️ 8.0/10
11. [Waymo Launches in Portland](#item-11) ⭐️ 8.0/10
12. [Pip 26.1 Introduces Lockfiles and Dependency Cooldowns](#item-12) ⭐️ 8.0/10
13. [NVIDIA Releases Nemotron 3 Nano Omni Multimodal Model](#item-13) ⭐️ 8.0/10
14. [ChatGPT introduces ads with full attribution loop](#item-14) ⭐️ 7.0/10
15. [LocalSend: Open-Source Cross-Platform AirDrop Alternative](#item-15) ⭐️ 7.0/10
16. [Claude.ai and API suffer elevated errors and outages](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Ghostty leaves GitHub: Mitchell Hashimoto moves away](https://mitchellh.com/writing/ghostty-leaving-github) ⭐️ 9.0/10

Mitchell Hashimoto, creator of the Ghostty terminal emulator, announced the project is leaving GitHub due to dissatisfaction with the platform's direction and declining quality. The migration to a self-hosted forge is underway. This move by a prominent developer signals growing discontent among open-source communities about platform dependency on GitHub, especially after its acquisition by Microsoft and perceived quality degradation. It could encourage other projects to reconsider their reliance on centralized platforms. Ghostty is a fast, GPU-accelerated terminal emulator that was open-sourced in late 2024. Hashimoto expressed emotional attachment to GitHub but cited its declining reliability and direction as reasons for leaving.

hackernews · WadeGrimridge · Apr 28, 19:44

**Background**: GitHub is a widely used code hosting platform owned by Microsoft, on which many open-source projects rely, leading to concerns about vendor lock-in. Ghostty is a high-performance terminal emulator created by Mitchell Hashimoto, co-founder of HashiCorp, known for its native UI and GPU acceleration.

<details><summary>References</summary>
<ul>
<li><a href="https://ghostty.org/">Ghostty</a></li>
<li><a href="https://github.com/ghostty-org/ghostty">GitHub - ghostty -org/ ghostty : Ghostty is a fast, feature-rich, and...</a></li>

</ul>
</details>

**Discussion**: Comments show mixed reactions: some empathize with Hashimoto's emotional struggle, while others argue that GitHub's proprietary nature was always suspect and that the move was predictable. There is discussion about GitHub's decline and alternatives, with one user suggesting Hashimoto could turn GitHub around as CEO.

**Tags**: `#GitHub`, `#open source`, `#platform dependency`, `#developer community`, `#Ghostty`

---

<a id="item-2"></a>
## [OpenAI models to be available on Amazon Bedrock](https://stratechery.com/2026/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-bedrock-managed-agents/) ⭐️ 9.0/10

OpenAI and AWS announced that OpenAI's models will be available on Amazon Bedrock, expanding enterprise access. This marks a major partnership shift as OpenAI previously relied primarily on Microsoft Azure. This move significantly increases enterprise adoption of OpenAI models by offering them through a trusted cloud platform, directly competing with Anthropic's existing Bedrock presence. It could reshape the landscape of AI model deployment in regulated industries. OpenAI models will be accessible via Bedrock's managed API alongside other foundation models, with data residency and security features. The partnership involves running OpenAI models on AWS infrastructure, potentially addressing enterprise privacy concerns.

hackernews · translocator · Apr 28, 19:24

**Background**: Amazon Bedrock is a fully managed service by AWS that provides a unified API to access foundation models from multiple AI companies, launched in 2023. It competes with platforms like Microsoft Azure AI Foundry and Google Cloud Vertex AI. Previously, Anthropic's Claude models were a key offering on Bedrock, and adding OpenAI diversifies the model selection.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Amazon_Bedrock">Amazon Bedrock</a></li>
<li><a href="https://aws.amazon.com/bedrock/">Amazon Bedrock – Build genAI applications and agents at production scale – AWS</a></li>

</ul>
</details>

**Discussion**: Commenters noted that many enterprises chose Bedrock for Anthropic due to trust and data privacy concerns with OpenAI. Some expressed skepticism about non-determinism across inference platforms, while others saw this as a strategic move by OpenAI to catch up in enterprise deployment.

**Tags**: `#OpenAI`, `#Amazon Bedrock`, `#AI models`, `#AWS`, `#cloud AI`

---

<a id="item-3"></a>
## [Critical GitHub RCE Vulnerability CVE-2026-3854](https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854) ⭐️ 9.0/10

A critical remote code execution (RCE) vulnerability in GitHub Enterprise Server, tracked as CVE-2026-3854, allows attackers to execute arbitrary code by sending a malicious git push with unsanitized push options. The flaw was discovered and disclosed by Wiz researchers, and a fix was released in GHES version 3.19.3 on March 10, 2026. This vulnerability is critical because it enables unauthenticated remote code execution on GitHub Enterprise Server instances, potentially compromising entire enterprise codebases. With 88% of instances still unpatched as of late April 2026, the attack surface remains large, posing a significant risk to organizations relying on self-hosted GitHub. The vulnerability originates in babeld, a component that forwards push requests, where push options are copied directly into the X-Stat header without sanitizing semicolons, leading to command injection. The fix was included in GHES 3.19.3, and users are urged to upgrade immediately.

hackernews · bo0tzz · Apr 28, 16:15

**Background**: Git push options are standard git protocol features that allow users to pass arbitrary strings with `git push -o` for server-side hints. In GitHub Enterprise Server, babeld encodes these options as numbered fields in internal requests. The lack of sanitization on semicolons allows attackers to inject arbitrary headers or commands, leading to RCE.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854">GitHub RCE Vulnerability: CVE-2026-3854 Breakdown | Wiz Blog</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-3854">CVE-2026-3854 Detail - NVD</a></li>
<li><a href="https://securityaffairs.com/191434/security/cve-2026-3854-github-flaw-enables-remote-code-execution.html">CVE-2026-3854 GitHub flaw enables remote code execution</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the severity of the vulnerability, with one user noting that 88% of on-premises instances remain unpatched seven weeks after the fix. Others discuss the use of AI-augmented reversing in the discovery, and some express concern about GitHub's security track record, questioning alternatives.

**Tags**: `#security`, `#vulnerability`, `#github`, `#rce`, `#CVE`

---

<a id="item-4"></a>
## [Google Pushes Android Towards Walled Garden, Curtailing User Control](https://keepandroidopen.org/en/) ⭐️ 9.0/10

Google is reportedly planning to enforce stricter controls on Android, requiring app developers to register with Google and pay fees, with changes potentially taking effect in September 2026. This effectively moves Android from an open ecosystem to a walled garden similar to iOS. This undermines Android's core value proposition of openness, which has attracted millions of users and developers seeking freedom and customization. If realized, it could reduce user control, stifle innovation, and lead to a less competitive mobile market. The reported changes include a silent update that would block apps from developers who have not registered with Google, signed a contract, and paid the required fees. This primarily affects apps distributed outside of Google Play, potentially sideloading forces developers into Google's ecosystem.

hackernews · doener · Apr 28, 15:21

**Background**: Android is based on the Android Open Source Project (AOSP), which is free and open-source software. However, most Android devices include proprietary Google Mobile Services (GMS), which require certification from Google. A walled garden is a closed ecosystem where the provider controls access to content and applications, limiting user freedom.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Android_(operating_system)">Android (operating system) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Mobile_Services">Google Mobile Services - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Closed_platform">Closed platform - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments reveal strong opposition, with some users stating they chose Android for its openness and are now considering switching to iOS. Others argue that true openness requires alternatives beyond Google's ecosystem, and a few express skepticism about the technical feasibility of the reported changes.

**Tags**: `#android`, `#open-source`, `#google`, `#walled-garden`, `#user-rights`

---

<a id="item-5"></a>
## [Talkie: A 13B Vintage Language Model Trained on Pre-1931 Text](https://simonwillison.net/2026/Apr/28/talkie/#atom-everything) ⭐️ 9.0/10

Researchers Nick Levine, David Duvenaud, and Alec Radford released talkie-1930-13b, a 13B parameter language model trained exclusively on 260B tokens of pre-1931 English text, along with an instruction-tuned chat variant, both under Apache 2.0 license. This model enables research into historical NLP, such as how well a model trapped in 1930 can predict future events or invent ideas beyond its knowledge cutoff, and provides a legally clean, out-of-copyright training data paradigm that could spur open-source development. The base model (53.1 GB) and instruction-tuned model (26.6 GB) are on Hugging Face; the chat model was fine-tuned using synthetic instruction-response pairs from historical references and modern LLMs (Claude Sonnet 4.6 as judge, Claude Opus 4.6 for synthetic chats), raising concerns about anachronistic contamination.

rss · Simon Willison · Apr 28, 02:47

**Background**: Language models are AI systems trained on vast text corpora to generate and understand human language. Training exclusively on historical text from before a certain date creates a 'time capsule' model with a fixed knowledge cutoff. The 1931 cutoff is legally significant in the US because works published before that year are generally in the public domain. Key researchers include Alec Radford, known for work on GPT and Whisper.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Apr/28/talkie/">Introducing talkie: a 13B vintage language model from 1930</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-04-28-talkie-a-13b-vintage-language-model-trained-exclusively-on-pre-1931-historical-text-and-cultural-val">Talkie: A 13B Vintage AI Model Trained on Pre-1931 Text | AIToolly</a></li>

</ul>
</details>

**Tags**: `#language model`, `#NLP`, `#historical text`, `#open source`, `#research`

---

<a id="item-6"></a>
## [Reflecting on Software Development Before GitHub](https://lucumr.pocoo.org/2026/4/28/before-github/) ⭐️ 8.0/10

The article reflects on the era before GitHub, highlighting how GitHub revolutionized open source by lowering the barrier to sharing code and fostering community around individuals rather than projects. Understanding GitHub's impact helps developers appreciate how modern collaboration tools evolved, and it sparks debate about centralization, archival practices, and alternatives like Fossil. The article notes that GitHub popularized per-person repositories, making it trivial to start a project without the overhead of SourceForge's project registration. It also emphasizes GitHub's role as a library that preserved abandoned projects.

hackernews · mlex · Apr 28, 21:17

**Background**: Before GitHub, open source hosting required formal project creation on platforms like SourceForge, with separate setup for version control, mailing lists, and issue trackers. GitHub unified these into a single, easy-to-use platform with Git, enabling fork-based collaboration and social coding.

**Discussion**: Commenters praised GitHub's reduction of mental load for starting projects, but some lamented Git's dominance over Fossil, which offers integrated wiki, forum, and issue tracking. Others warned that GitHub's centralization atrophies community archival skills.

**Tags**: `#GitHub`, `#version control`, `#open source`, `#software engineering history`

---

<a id="item-7"></a>
## [Who owns AI coding agent output?](https://legallayer.substack.com/p/who-owns-the-claude-code-wrote) ⭐️ 8.0/10

A Substack article by Legallayer explores unresolved copyright ownership questions for code generated by AI coding agents like Claude Code, drawing parallels to earlier image-generation cases. This issue affects millions of developers using AI coding agents; unclear ownership could create legal risks for commercial software and open-source projects. The US Copyright Office stated in January 2025 that works predominantly generated by AI without meaningful human authorship are not eligible for copyright, but the Supreme Court's denial of certiorari in the Thaler appeal did not settle the issue nationwide.

hackernews · senaevren · Apr 28, 11:24

**Background**: Claude Code is an agentic coding tool from Anthropic that can understand codebases, edit files, and run commands. AI coding agents are increasingly used in software development, raising legal questions about who owns the generated code, similar to earlier debates over AI-generated images.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://codegen.com/blog/best-ai-coding-agents/">Best AI Coding Agents in 2026: Ranked and Compared</a></li>

</ul>
</details>

**Discussion**: Commenters compared the situation to the Zarya of the Dawn case for Midjourney, noting that prompting an AI agent is more like prompting an image generator than writing code manually. Some expressed concern about copyright 'washing' in open-source, while others debated the legal significance of the Supreme Court's denial of certiorari.

**Tags**: `#AI`, `#copyright`, `#coding agents`, `#legal`, `#software engineering`

---

<a id="item-8"></a>
## [Warp terminal emulator goes open source](https://www.warp.dev/blog/warp-is-now-open-source) ⭐️ 8.0/10

Warp, a modern terminal emulator for macOS, Windows, and Linux, has been open-sourced under a proprietary license, allowing the community to view and contribute to its codebase. Open-sourcing a widely-used developer tool like Warp can accelerate innovation and community trust, though the business-driven motivation and bundled AI features have drawn mixed reactions from users. Warp is written in Rust and known for its modern UI and AI features; however, the app size is reportedly around 850 MB, and some users hope for a lightweight version without AI and code editing capabilities.

hackernews · meetpateltech · Apr 28, 15:58

**Background**: Warp is a proprietary terminal emulator first released in 2021, competing with tools like iTerm2 and Hyper. It gained popularity for its speed, Rust-based architecture, and integrated AI assistant. The decision to open-source is aimed at accelerating development and building a sustainable business around the platform.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Warp_(terminal)">Warp (terminal) - Wikipedia</a></li>
<li><a href="https://www.warp.dev/">Warp: The Agentic Development Environment</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: while many appreciate the move to open source, some express concerns about bloat and the inclusion of AI features, hoping for a stripped-down version. Others note the business-driven strategy behind the decision.

**Tags**: `#open-source`, `#terminal`, `#Warp`, `#developer-tools`

---

<a id="item-9"></a>
## [UAE announces exit from OPEC](https://www.ft.com/content/8c354f2d-3e66-47f1-aad4-9b4aa30e386d) ⭐️ 8.0/10

The United Arab Emirates has announced that it will withdraw from OPEC, effective April 28, 2026, according to a Reuters report. This move weakens OPEC's influence and signals a deepening rift between the UAE and Saudi Arabia, reshaping global oil market dynamics and Gulf geopolitics. The decision comes amid strained Saudi-Emirati relations and a reported request by the UAE for Pakistan to repay a $3.5 billion loan early. Community comments also suggest an emerging Emirati-Israeli axis balancing Saudi and Iranian hegemony.

hackernews · bazzmt · Apr 28, 13:02

**Background**: OPEC is a cartel of oil-producing nations that coordinates production to influence global prices. The UAE has been a key member but has often clashed with Saudi Arabia over output quotas. This exit could undermine OPEC's cohesion and pricing power.

**Discussion**: Commenters analyze the geopolitical shift, noting an Emirati-Israeli axis forming to counter Saudi dominance and Iranian influence. Some highlight the historical problem of cartel cheating, while others see this as a win for US energy strategy. The discussion is deep and provides valuable context.

**Tags**: `#geopolitics`, `#OPEC`, `#oil markets`, `#international relations`

---

<a id="item-10"></a>
## [GitHub Availability Update Faces Community Skepticism](https://github.blog/news-insights/company-news/an-update-on-github-availability/) ⭐️ 8.0/10

GitHub published an update stating that its priorities are availability, then capacity, then new features, but the community is skeptical given ongoing reliability issues and a history of prioritizing Azure migration over features. This matters because GitHub is a critical platform for millions of developers worldwide, and persistent reliability problems can erode trust and productivity; the company's stated priorities now contradict earlier actions and community experience. The update follows 12 months of dire uptime according to community members, and the lack of transparent data (e.g., unlabeled graphs) further fuels skepticism; GitHub also mentions working on a multi-cloud path, which some interpret as an implicit acknowledgement of Azure limitations.

hackernews · GitHub Blog · Apr 28, 10:05

**Background**: GitHub is a popular code hosting and collaboration platform owned by Microsoft. In recent years, it has faced increasing reliability challenges, partly due to rapid user growth and the demands of AI agents generating repositories. The company previously announced a move to Azure, but the latest post signals a shift in priorities.

**Discussion**: The community is highly critical, with comments calling the update 'hard to read with a straight face' and pointing out incomplete pull request lists on the website. Some users note the irony of Microsoft suggesting Azure unreliability by mentioning a multi-cloud path, while others confirm that agents are placing extra pressure on GitHub.

**Tags**: `#github`, `#availability`, `#reliability`, `#cloud`, `#community-feedback`

---

<a id="item-11"></a>
## [Waymo Launches in Portland](https://waymo.com/blog/shorts/waymo-in-portland/) ⭐️ 8.0/10

Waymo announced the launch of its autonomous ride-hailing service in Portland, Oregon, expanding its operations to a new city. This expansion marks a significant milestone in the deployment of autonomous vehicles and could provide an alternative to public transit, especially amid budget cuts to Portland's TriMet system. The service will operate within a geofenced area using Waymo's sensor-heavy approach, though specific details on service boundaries and launch dates were not provided.

hackernews · xnx · Apr 28, 18:08

**Background**: Waymo is a leading autonomous driving company that has been operating commercial robotaxi services in Phoenix and San Francisco. Its vehicles rely on a combination of LIDAR, cameras, and radar for safe navigation within predefined areas.

**Discussion**: Commenters expressed cautious optimism, with some noting Portland's public transit budget crisis makes Waymo a timely alternative. Others compared Waymo favorably to Tesla's FSD, while concerns about vehicle appearance and integration were raised.

**Tags**: `#autonomous vehicles`, `#Waymo`, `#Portland`, `#transportation`, `#self-driving`

---

<a id="item-12"></a>
## [Pip 26.1 Introduces Lockfiles and Dependency Cooldowns](https://simonwillison.net/2026/Apr/28/pip-261/#atom-everything) ⭐️ 8.0/10

Pip 26.1 adds experimental support for lockfiles via the new `pip lock` command, which generates a `pylock.toml` file pinning all dependencies, and introduces dependency cooldowns through the `--uploaded-prior-to` option. Additionally, this release drops support for Python 3.9. Lockfiles bring deterministic, reproducible installations to pip, a critical feature for deployment and CI/CD pipelines. Dependency cooldowns help mitigate supply-chain attacks by ensuring only packages older than a specified duration are installed, giving time for malware detection. The lockfile format is `pylock.toml`, and the cooldown option accepts ISO 8601 duration format (e.g., `P4D` for four days). The `pip lock` command currently only supports locking packages for the `pip install` command, not for `--upgrade` or other modes. These features are experimental and may change.

rss · Simon Willison · Apr 28, 05:23

**Background**: Pip is the default package installer for Python, used by millions of developers to manage dependencies. Lockfiles are common in other package managers (e.g., npm's package-lock.json) to freeze exact versions for reproducible builds. Dependency cooldowns are a security best practice where a waiting period is enforced after a package is uploaded before it can be installed, reducing the window for attackers to exploit malicious releases.

<details><summary>References</summary>
<ul>
<li><a href="https://pip.pypa.io/en/stable/cli/pip_lock/">pip lock - pip documentation v26.0.1</a></li>
<li><a href="https://ichard26.github.io/blog/2026/04/whats-new-in-pip-26.1/">What's new in pip 26.1 - lockfiles and dependency cooldowns! | Richard Si</a></li>

</ul>
</details>

**Tags**: `#pip`, `#python`, `#package management`, `#lockfiles`

---

<a id="item-13"></a>
## [NVIDIA Releases Nemotron 3 Nano Omni Multimodal Model](https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence) ⭐️ 8.0/10

NVIDIA has introduced the Nemotron 3 Nano Omni, a multimodal AI model capable of processing long-context documents, audio, and video for AI agents. This release extends the Nemotron family’s reach into multimodal AI, enabling more capable and efficient AI agents that can reason across different data types in a single context. The model supports long-context retrieval, structured extraction, table and chart reading, and multi-page reasoning, all in one pass.

rss · Hugging Face Blog · Apr 28, 15:58

**Background**: NVIDIA's Nemotron model family includes open models with open weights, training data, and recipes, designed for building specialized AI agents. The Nemotron 3 Nano is a 30B-3B A3B model balancing efficiency and accuracy. This new Omni variant adds multimodal capabilities for documents, audio, and video.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence">Introducing NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal ...</a></li>
<li><a href="https://developer.nvidia.com/nemotron">Nemotron AI Models | NVIDIA Developer</a></li>
<li><a href="https://huggingface.co/blog/nvidia/nemotron-3-nano-efficient-open-intelligent-models">Nemotron 3 Nano \- A new Standard for Efficient, Open, and Intelligent...</a></li>

</ul>
</details>

**Tags**: `#multimodal`, `#NVIDIA`, `#long-context`, `#AI models`

---

<a id="item-14"></a>
## [ChatGPT introduces ads with full attribution loop](https://www.buchodi.com/how-chatgpt-serves-ads-heres-the-full-attribution-loop/) ⭐️ 7.0/10

ChatGPT now displays advertisements that include a complete attribution loop, allowing tracking of ad performance from impression to conversion. This shift marks a significant change in OpenAI's business model, moving away from subscription-only revenue toward advertising, which could influence how users interact with AI chatbots and raise privacy concerns. The attribution loop tracks users across multiple touchpoints, potentially using identifiers like IP addresses and cookies, though OpenAI has not disclosed full technical specifics.

hackernews · lmbbuchodi · Apr 28, 23:54

**Background**: An attribution loop is a marketing concept that tracks the customer journey from initial ad exposure to final conversion, allowing advertisers to measure effectiveness. OpenAI had previously considered ads a last resort, but the company may be seeking additional revenue sources amid high operational costs.

<details><summary>References</summary>
<ul>
<li><a href="https://theconversation.com/you-probably-wouldnt-notice-if-an-ai-chatbot-slipped-ads-into-its-responses-276010">You probably wouldn't notice if an AI chatbot slipped ads into its responses</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed feelings: some users recall Sam Altman's earlier statement that ads would be a last resort, while others worry about adversarial content and SEO manipulation. Some suggest the ads may be easy to block if served as distinct events.

**Tags**: `#OpenAI`, `#ChatGPT`, `#advertising`, `#business model`, `#AI ethics`

---

<a id="item-15"></a>
## [LocalSend: Open-Source Cross-Platform AirDrop Alternative](https://github.com/localsend/localsend) ⭐️ 7.0/10

LocalSend is a free, open-source app that enables secure file sharing between nearby devices over a local network without internet, supporting Windows, macOS, Linux, Android, and iOS. It provides a privacy-focused, cross-platform alternative to Apple's AirDrop, empowering users to share files offline without relying on cloud services. LocalSend uses LAN multicast groups and on-the-fly TLS/SSL certificate generation for encryption, but requires devices to be on the same local network, unlike AirDrop which can create its own network.

hackernews · bilsbie · Apr 28, 11:54

**Background**: Apple's AirDrop uses Bluetooth and Wi-Fi to create a peer-to-peer network automatically, allowing file transfers even without a shared Wi-Fi network. LocalSend, being LAN-based, cannot do this out of the box, though workarounds like tethering exist.

<details><summary>References</summary>
<ul>
<li><a href="https://localsend.org/">LocalSend : Share files to nearby devices</a></li>
<li><a href="https://github.com/localsend/localsend">GitHub - localsend / localsend : An open - source cross-platform...</a></li>
<li><a href="https://blog.blackwing.dev/localsend-a-privacy-first-airdrop-alternative">Localsend : A Privacy-First Airdrop Alternative (2026)</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that LocalSend's reliance on a pre-existing LAN is a key limitation compared to AirDrop, though some users find it more reliable. Alternatives like Sendme (using Iroh P2P relay) are mentioned as solutions without network constraints.

**Tags**: `#open-source`, `#file-sharing`, `#cross-platform`, `#air-drop-alternative`, `#networking`

---

<a id="item-16"></a>
## [Claude.ai and API suffer elevated errors and outages](https://status.claude.com/incidents/9l93x2ht4s5w) ⭐️ 7.0/10

Claude.ai and its API experienced elevated errors and downtime, severely impacting availability for users including enterprise customers. This incident highlights critical reliability issues for Anthropic's platform, with enterprise users reporting significant business impact and frustration over support. User reports indicate uptime measured at only one 9 (99%) over the last 90 days, and some organizations spend over $200,000 per month on Anthropic's enterprise tier.

hackernews · shorsher · Apr 28, 18:01

**Discussion**: Enterprise users expressed strong dissatisfaction, citing frequent outages and poor support. One user noted that their executive team is furious over spending $200k/month for low reliability. Another highlighted the uptime has dropped to one 9, and a third user emphasized the need for multi-model strategies.

**Tags**: `#claude`, `#api`, `#reliability`, `#outage`, `#anthropic`

---