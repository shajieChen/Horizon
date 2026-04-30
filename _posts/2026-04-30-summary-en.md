---
layout: default
title: "Horizon Summary: 2026-04-30 (EN)"
date: 2026-04-30
lang: en
---

> From 35 items, 20 important content pieces were selected

---

1. [Zed 1.0 Released: High-Performance Rust Code Editor](#item-1) ⭐️ 8.0/10
2. [Critical Linux AF_ALG Vulnerability CVE-2026-31431](#item-2) ⭐️ 8.0/10
3. [Open-Source Stethoscope Costs $2.50–$5 to Produce](#item-3) ⭐️ 8.0/10
4. [Ramp Sheets AI Vulnerability Enables Data Exfiltration](#item-4) ⭐️ 8.0/10
5. [Proposal: Federated Code Forges to End Vendor Lock-in](#item-5) ⭐️ 8.0/10
6. [Kyoto cherry blossoms bloom earliest in 1,200 years](#item-6) ⭐️ 8.0/10
7. [Online age verification: a privacy battlefield](#item-7) ⭐️ 8.0/10
8. [Mistral releases Medium 3.5, a 120B dense model](#item-8) ⭐️ 8.0/10
9. [LLM 0.32a0 Introduces Message-Based Model Refactor](#item-9) ⭐️ 8.0/10
10. [OpenAI expands Stargate infrastructure for AGI](#item-10) ⭐️ 8.0/10
11. [OpenAI Proposes Plan for AI-Driven Cybersecurity](#item-11) ⭐️ 8.0/10
12. [AI evals are becoming the new compute bottleneck](#item-12) ⭐️ 8.0/10
13. [IBM Granite 4.1 LLMs: Architecture and Training Deep Dive](#item-13) ⭐️ 8.0/10
14. [HERMES.md bug causes extra billing in Claude Code](#item-14) ⭐️ 7.0/10
15. [FastCGI Superior to HTTP for Reverse Proxies](#item-15) ⭐️ 7.0/10
16. [Why Lisp and Scheme Beat Haskell for the Author](#item-16) ⭐️ 7.0/10
17. [Maryland bans surveillance pricing in grocery stores](#item-17) ⭐️ 7.0/10
18. [DOS 1.0 Source Code Transcribed from Printouts](#item-18) ⭐️ 7.0/10
19. [Dutch government soft-launches open-source code platform](#item-19) ⭐️ 7.0/10
20. [OpenTrafficMap: Low-Cost V2X Traffic Visualization](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Zed 1.0 Released: High-Performance Rust Code Editor](https://zed.dev/blog/zed-1-0) ⭐️ 8.0/10

Zed, the Rust-based code editor, has reached its 1.0 milestone, marking its stable release after extensive development. Zed 1.0 represents a new generation of high-performance editors that leverage modern systems programming languages like Rust, offering faster startup and editing compared to traditional editors. It could challenge established editors like Sublime Text and VS Code. The editor is open-source, built in Rust, and supports Linux, macOS, and Windows. However, the license agreement has raised concerns about data usage rights.

hackernews · salkahfi · Apr 29, 14:34

**Background**: Zed is a high-performance multiplayer code editor written in Rust, initially released in early access before reaching 1.0. Rust is a systems programming language known for memory safety and performance, making it ideal for building fast editors that can handle large codebases efficiently.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zed_(text_editor)">Zed (text editor ) - Wikipedia</a></li>
<li><a href="https://zed.dev/">Zed — Love your editor again</a></li>

</ul>
</details>

**Discussion**: Community reactions vary: some praise Zed's performance and innovation, while others criticize the licensing terms regarding customer data. A user notes that complaints are common but Zed's technology is groundbreaking. Another user prefers Sublime Text for legacy projects due to compatibility issues.

**Tags**: `#zed`, `#code editor`, `#rust`, `#release`, `#software`

---

<a id="item-2"></a>
## [Critical Linux AF_ALG Vulnerability CVE-2026-31431](https://copy.fail/) ⭐️ 8.0/10

A critical Linux kernel AF_ALG vulnerability (CVE-2026-31431) allows unprivileged users to gain root access via a 732-byte exploit called Copy Fail. Vendors like Red Hat, Debian, and Ubuntu have rated it as moderate severity and deferred patches, leading to community frustration. This vulnerability enables reliable local privilege escalation to root on every major Linux distribution without needing a race window or kernel-specific offsets. It highlights the inherent danger of the AF_ALG interface, which exposes a large attack surface to unprivileged userspace. The exploit is a straight-line logic flaw that neither requires a race condition nor kernel-specific offsets; mitigation involves disabling the algif_aead kernel module via modprobe configuration. The vulnerability stems from the AF_ALG socket type, which exposes kernel crypto routines to unprivileged users.

hackernews · unsnap_biceps · Apr 29, 18:13

**Background**: AF_ALG is a Linux kernel socket interface added in version 2.6.38 that allows userspace programs to access kernel cryptographic operations. It is considered complex and largely unnecessary because userspace already has its own crypto libraries. CVE-2026-31431 is a privilege escalation vulnerability in the AEAD (Authenticated Encryption with Associated Data) handling of AF_ALG, discovered by researchers at Xint and assigned the nickname 'Copy Fail'.

<details><summary>References</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-31431">NVD - CVE - 2026 - 31431</a></li>
<li><a href="https://github.com/painoob/Copy-Fail-Exploit-CVE-2026-31431">GitHub - painoob/Copy-Fail- Exploit - CVE - 2026 - 31431 : Most Linux...</a></li>

</ul>
</details>

**Discussion**: A kernel developer working on crypto code expressed frustration that AF_ALG exploits keep recurring, calling the interface unnecessary and overly complex. Community members noted that vendors have downplayed the severity, with Red Hat marking it as 'Moderate' and 'Fix deferred', and confusion around the disclosure process was mentioned. One commenter also pointed out the risk of autonomous AI agents running as regular users on affected systems.

**Tags**: `#security`, `#linux`, `#kernel`, `#cve`, `#exploit`

---

<a id="item-3"></a>
## [Open-Source Stethoscope Costs $2.50–$5 to Produce](https://github.com/GliaX/Stethoscope) ⭐️ 8.0/10

A new open-source stethoscope design, available on GitHub, can be produced for $2.50 to $5, making it affordable for low-resource settings. This low-cost design has the potential to improve medical diagnostics in underserved areas where traditional stethoscopes are too expensive. The stethoscope is designed for 3D printing and uses easily sourced materials, but some community members question its acoustic performance compared to professional models.

hackernews · 0x54MUR41 · Apr 29, 14:47

**Background**: Traditional stethoscopes can cost over $100, putting them out of reach for many clinics in developing countries. Open-source hardware projects like this aim to democratize medical tools by providing freely available designs that can be locally manufactured.

**Discussion**: Community comments express skepticism about the acoustic frequency response graphs, noting they appear to match professional stethoscopes too closely. Some users point out that cheap metal stethoscopes are available for $7, while others share an interview with the researchers explaining the project's motivations.

**Tags**: `#open-source`, `#healthcare`, `#hardware`, `#stethoscope`, `#3D-printing`

---

<a id="item-4"></a>
## [Ramp Sheets AI Vulnerability Enables Data Exfiltration](https://www.promptarmor.com/resources/ramps-sheets-ai-exfiltrates-financials) ⭐️ 8.0/10

A prompt injection vulnerability in Ramp's Sheets AI allows attackers to exfiltrate sensitive financial data by injecting malicious instructions. The flaw was responsibly disclosed by PromptArmor and reportedly fixed by Ramp on May 16, 2026. This exploit demonstrates how AI agents that execute natural-language instructions can reintroduce classic security risks, especially when handling sensitive financial data. It highlights the urgent need for robust input validation and agent isolation in LLM-powered applications. The attack leverages prompt injection, where adversarial text tricks the AI into performing unauthorized actions, such as exfiltrating spreadsheet data. PromptArmor had to contact Ramp three times before receiving a response, and the fix date in the disclosure (May 16, 2026) may be a typo for March.

hackernews · takira · Apr 29, 17:44

**Background**: Prompt injection is a vulnerability where an attacker crafts input that overrides or alters an AI model's instructions, similar to SQL injection. Ramp Sheets is an AI-powered spreadsheet tool designed for finance teams, integrating large language models to automate tasks. As LLM agents gain access to sensitive data, prompt injection becomes a critical security concern.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/prompt-injection">What Is a Prompt Injection Attack? | IBM</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>
<li><a href="https://labs.ramp.com/sheets">Ramp Sheets</a></li>

</ul>
</details>

**Discussion**: Comments highlight the irony that after decades of preventing arbitrary code execution, AI agents now naively execute arbitrary data as instructions. There is skepticism about Ramp's slow response and the fix date, with one user questioning why Ramp builds a sheets product at all.

**Tags**: `#security`, `#AI`, `#prompt injection`, `#vulnerability`, `#Ramp`

---

<a id="item-5"></a>
## [Proposal: Federated Code Forges to End Vendor Lock-in](https://blog.tangled.org/federation/) ⭐️ 8.0/10

A blog post titled 'We need a federation of forges' proposes creating a federated network of code forges, similar to email or Mastodon, to reduce vendor lock-in and centralization in code hosting. This proposal addresses the growing dominance of a single platform like GitHub, fostering competition and interoperability that could benefit the entire open-source ecosystem by reducing dependency on any one provider. The post highlights challenges such as defederation, political disputes, and the difficulty of bootstrapping without venture capital, while existing projects like ForgeFed already work on federating features like repository stars across Forgejo instances.

hackernews · icy · Apr 29, 14:00

**Background**: Code forges are web-based platforms like GitHub and GitLab that host source code and provide collaboration tools. Federation, as seen in email and Mastodon, allows independent instances to interoperate without central control, but implementing it for forges involves complex technical and social hurdles.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forge_(software)">Forge (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo - Wikipedia</a></li>
<li><a href="https://nlnet.nl/project/Federated-Forgejo/">NLnet; Federated software forges with Forgejo</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism about repeating Mastodon's problems (defederation, pointless debates), but also support for competition and hope for meaningful adoption. Some mention alternative approaches like AT Protocol or Fossil's integrated model.

**Tags**: `#federation`, `#open source`, `#forges`, `#GitHub alternative`, `#decentralization`

---

<a id="item-6"></a>
## [Kyoto cherry blossoms bloom earliest in 1,200 years](https://jivx.com/kyoto-bloom) ⭐️ 8.0/10

Historical records show that Kyoto's cherry blossoms reached their peak bloom on March 26, 2021, the earliest date in over 1,200 years of record-keeping. This unique long-term dataset provides stark evidence of climate change's impact on phenology, affecting ecosystems, agriculture, and cultural events like hanami (cherry blossom viewing). The record is based on data dating back to 812 AD, making it one of the longest continuous phenological records in the world. The earlier bloom is primarily attributed to rising spring temperatures due to global warming.

hackernews · momentmaker · Apr 29, 19:32

**Background**: Phenology is the study of seasonal biological events, such as flowering and migration. Cherry blossom dates are highly sensitive to temperature, so historical records serve as a proxy for past climate. The Kyoto cherry blossom record is a well-known benchmark in climate science.

<details><summary>References</summary>
<ul>
<li><a href="https://ourworldindata.org/grapher/date-of-the-peak-cherry-tree-blossom-in-kyoto">Day of the year with peak cherry tree blossom in Kyoto, Japan - Our World in Data</a></li>
<li><a href="https://www.bbc.com/news/world-asia-56574142">Japan's cherry blossom 'earliest peak since 812'</a></li>
<li><a href="https://en.wikipedia.org/wiki/Phenology">Phenology</a></li>

</ul>
</details>

**Discussion**: Commenters expressed awe at the 1,200-year dataset and concern over rapidly shifting bloom dates. Some noted earlier blooms in their own gardens, while one user linked to the original data source. A few questioned why mainstream media coverage of climate change has diminished.

**Tags**: `#climate change`, `#cherry blossoms`, `#historical data`, `#Kyoto`, `#environmental impact`

---

<a id="item-7"></a>
## [Online age verification: a privacy battlefield](https://x.com/GlennMeder/status/2049088498163216560) ⭐️ 8.0/10

A viral social media post argues that mandatory online age verification poses unacceptable risks to anonymity and privacy, sparking a heated debate with over 700 points and 458 comments. This debate touches on fundamental tensions between protecting minors online and preserving civil liberties, with implications for global internet governance and the engineering of identity systems. Key methods discussed include RTA headers, credit card checks, photo ID matching, and privacy-preserving zero-knowledge proof systems; commenters warn that widespread age surveillance could normalize identity fraud and surveillance.

hackernews · Cider9986 · Apr 29, 15:49

**Background**: Online age verification is a mechanism to restrict access to age-sensitive content, often mandated by laws like the UK's Online Safety Act. Common methods range from simple self-declaration to biometric checks, but privacy advocates argue that many approaches undermine anonymity and could centralize sensitive data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c1k81lj8nvpo">Online Safety Act: Which sites will require UK age verification ?</a></li>
<li><a href="http://newamerica.org/oti/briefs/exploring-privacy-preserving-age-verification/">Exploring Privacy-Preserving Age Verification: A Close Look at Zero-Knowledge Proofs</a></li>
<li><a href="https://www.cs.columbia.edu/~smb/papers/age-verify.pdf">Privacy-Preserving Age Verification—and Its Limitations Steven M. Bellovin *</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong opposition to mandatory age verification, citing parents' responsibility, inevitable circumvention by teens, and increased identity fraud. Some advocated for privacy-preserving alternatives like anonymous credential systems or RTA headers, but doubted that policymakers would adopt them due to ulterior surveillance motives.

**Tags**: `#age verification`, `#privacy`, `#internet governance`, `#anonymity`, `#parental controls`

---

<a id="item-8"></a>
## [Mistral releases Medium 3.5, a 120B dense model](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5) ⭐️ 8.0/10

Mistral AI has released Mistral Medium 3.5, a dense 120-billion-parameter model that can run at Q4 quantization in about 70GB of VRAM, making it more accessible than many larger competitors. This model demonstrates that a smaller dense model can compete with much larger MoE models, lowering the hardware barrier for running high-performance LLMs locally and broadening access for developers and researchers. Mistral Medium 3.5 is a 120B dense model, meaning all parameters are active for every token, unlike Mixture-of-Experts models that only use a subset. This results in higher VRAM efficiency per parameter but slower inference compared to sparse models.

hackernews · meetpateltech · Apr 29, 15:17

**Background**: Dense large language models activate all parameters for every input, providing a uniform computational load but requiring more memory per inference step. In contrast, Mixture-of-Experts (MoE) models route tokens to specialized sub-networks, offering faster generation at the cost of higher peak memory and more complex deployment. Mistral's Medium 3.5 is part of its model family, which also includes the 7B and Large models, and is designed to balance performance and accessibility.

<details><summary>References</summary>
<ul>
<li><a href="https://maxkruse.github.io/vitepress-llm-recommends/model-types/dense/">Dense Models | AI Model Guide</a></li>
<li><a href="https://huggingface.co/mistralai/Mistral-7B-v0.1">mistralai/ Mistral -7B-v0.1 · Hugging Face</a></li>
<li><a href="https://maximilian-schwarzmueller.com/articles/understanding-mixture-of-experts-moe-llms/">Mixture of Experts (MoE) vs Dense LLMs</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some praise the model's VRAM efficiency and competitive performance, while others note that models like DeepSeek v4 Flash (quantized to 2-bit) run faster on consumer hardware and serve as strong alternatives. There is also discussion about Mistral's restrictive CSP headers limiting web testing.

**Tags**: `#AI`, `#language models`, `#Mistral`, `#open-source`

---

<a id="item-9"></a>
## [LLM 0.32a0 Introduces Message-Based Model Refactor](https://simonwillison.net/2026/Apr/29/llm/#atom-everything) ⭐️ 8.0/10

LLM 0.32a0, an alpha release, refactors the core abstraction from prompt-response to a message-based model, allowing inputs as a sequence of messages and responses as a stream of typed parts, while maintaining full backwards compatibility. This refactor significantly improves LLM's ability to represent modern LLM capabilities like multi-modal inputs, structured outputs, and tool calls, benefiting its extensive plugin ecosystem and thousands of users who rely on it as a unified interface to diverse models. The two key changes are: model inputs can now be represented as a sequence of conversational messages, and model responses can be composed of a stream of differently typed parts (e.g., text, image, tool calls). The release is an alpha version, meaning it's experimental but aims for stable API post-testing.

rss · Simon Willison · Apr 29, 19:01

**Background**: LLM is a CLI tool and Python library created by Simon Willison that provides a unified interface to hundreds of large language models via a plugin system. Originally designed for simple text prompts and responses, it has evolved over time to support attachments (images, audio, video), structured JSON output via schemas, and tool calling. This refactor adapts the core abstraction to better match how modern LLMs communicate—via message sequences and typed response streams—which is already the standard in major APIs like OpenAI's Chat Completions.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2025/May/27/llm-tools/">Large Language Models can run tools in your terminal with LLM 0.26</a></li>
<li><a href="https://uuithub.com/simonw/llm">GitHub simonw/ llm LLM Context</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Python`, `#refactor`, `#CLI tool`, `#AI`

---

<a id="item-10"></a>
## [OpenAI expands Stargate infrastructure for AGI](https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age) ⭐️ 8.0/10

OpenAI announced scaling of the Stargate Project, adding new data center capacity to build compute infrastructure for artificial general intelligence (AGI). This massive infrastructure investment signals a major commitment to AGI development and positions the United States at the forefront of AI infrastructure innovation. The Stargate Project aims to invest $500 billion over four years to build AI infrastructure across the United States, announced in January 2025 with partners like SoftBank and Oracle.

rss · OpenAI Blog · Apr 29, 15:00

**Background**: AGI is a theoretical type of AI that can match or surpass human intelligence across all cognitive tasks. The Stargate Project is a dedicated initiative to create the necessary computational capacity for OpenAI's AGI research, reflecting the immense compute demands of advanced AI models.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/announcing-the-stargate-project/">Announcing The Stargate Project | OpenAI</a></li>
<li><a href="https://www.linkedin.com/pulse/stargate-project-500-billion-leap-ai-infrastructure-shiva-bhavani-qgghc">Stargate Project: A $500 Billion Leap in AI Infrastructure</a></li>
<li><a href="https://introl.com/blog/openai-stargate-500-billion-ai-infrastructure-2025">What $500 billion in AI infrastructure actually looks like | Introl Blog</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#AGI`, `#data centers`, `#compute scaling`, `#OpenAI`

---

<a id="item-11"></a>
## [OpenAI Proposes Plan for AI-Driven Cybersecurity](https://openai.com/index/cybersecurity-in-the-intelligence-age) ⭐️ 8.0/10

OpenAI published a five-part action plan titled 'Cybersecurity in the Intelligence Age' on April 29, 2025, calling for democratizing AI-powered cyber defense and protecting critical infrastructure. This proposal from a leading AI organization signals a strategic shift toward using AI offensively and defensively in cybersecurity, potentially influencing global policy and private-sector practices. The plan emphasizes democratizing access to AI defense tools, protecting critical systems like power grids, and fostering international cooperation. It builds on OpenAI's earlier 'Industrial Policy for the Intelligence Age' framework.

rss · OpenAI Blog · Apr 29, 04:00

**Background**: The 'Intelligence Age' is a term used by OpenAI to describe the era where AI becomes as transformative as electricity. Cybersecurity threats are growing in sophistication, and AI can both enhance attacks and defenses. OpenAI's plan aims to ensure that AI benefits security rather than undermining it.

<details><summary>References</summary>
<ul>
<li><a href="https://cdn.openai.com/pdf/561e7512-253e-424b-9734-ef4098440601/Industrial+Policy+for+the+Intelligence+Age.pdf">[PDF] Industrial Policy for the Intelligence Age: Ideas to Keep People First</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#AI safety`, `#OpenAI`, `#policy`, `#critical infrastructure`

---

<a id="item-12"></a>
## [AI evals are becoming the new compute bottleneck](https://huggingface.co/blog/evaleval/eval-costs-bottleneck) ⭐️ 8.0/10

A Hugging Face blog post highlights that evaluating AI models is becoming increasingly costly and time-consuming, emerging as a new computational bottleneck alongside training. This shift means that evaluation, not just training, will constrain the pace of AI development, potentially slowing down research and deployment as resources are diverted to testing. The post notes that running full evaluation suites for large models can require tens of thousands of GPU hours, rivaling the cost of training smaller models.

rss · Hugging Face Blog · Apr 29, 16:45

**Background**: In AI development, model training has long been the primary compute bottleneck, but evaluation—testing models on benchmarks—was often considered a minor cost. As models grow, evaluation requires running many complex tasks across multiple benchmarks, each needing significant compute. This trend is making evaluation a major cost factor that researchers must plan for.

**Tags**: `#AI`, `#evaluation`, `#compute bottleneck`, `#machine learning`, `#efficiency`

---

<a id="item-13"></a>
## [IBM Granite 4.1 LLMs: Architecture and Training Deep Dive](https://huggingface.co/blog/ibm-granite/granite-4-1) ⭐️ 8.0/10

IBM has released Granite 4.1, a family of dense decoder-only LLMs (3B, 8B, 30B) trained on ~15T tokens with multi-stage pre-training and long-context extension up to 512K tokens. This release demonstrates IBM's continued investment in efficient, enterprise-grade LLMs with competitive instruction-following and tool-calling capabilities, without relying on long chains of thought, which is important for predictable latency in production. The models use decoder-only dense transformer architecture with Grouped Query Attention (GQA), Rotary Position Embeddings (RoPE), SwiGLU activations, RMSNorm, and shared input/output embeddings.

rss · Hugging Face Blog · Apr 29, 15:01

**Background**: Large language models (LLMs) are AI models trained on vast text data to generate human-like text. IBM's Granite series targets enterprise use cases, and Granite 4.1 builds on the hybrid Mamba/transformer architecture of Granite 4.0, returning to a dense transformer design.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/ibm-granite/granite-4-1">Granite 4 . 1 LLMs: How They’re Built</a></li>
<li><a href="https://research.ibm.com/blog/granite-4-1-ai-foundation-models">Introducing the IBM Granite 4.1 family of models - IBM Research</a></li>
<li><a href="https://www.ibm.com/granite">Granite - IBM</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#IBM`, `#AI`, `#model architecture`, `#training`

---

<a id="item-14"></a>
## [HERMES.md bug causes extra billing in Claude Code](https://github.com/anthropics/claude-code/issues/53262) ⭐️ 7.0/10

A bug in Anthropic's Claude Code causes commit messages containing 'HERMES.md' to route requests to extra usage billing, resulting in unexpected charges. Anthropic later announced full refunds and additional usage credits for affected users. This incident highlights serious billing integrity issues in popular AI developer tools, eroding user trust. It also demonstrates the importance of robust refund policies and rapid community response for SaaS companies. The bug triggers on any commit message containing the string 'HERMES.md', causing unintended extra charges. Anthropic initially denied refunds citing a policy against compensating for technical errors, but later reversed course under community pressure.

hackernews · homebrewer · Apr 29, 18:54

**Background**: Claude Code is Anthropic's agentic coding tool that helps developers write code, run commands, and manage git workflows. HERMES.md is a file associated with the Hermes agent project, which can delegate tasks to Claude Code. The bug likely arises from how Claude Code's billing routing parses commit messages, treating 'HERMES.md' as a special trigger.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NousResearch/hermes-agent/blob/main/skills/autonomous-ai-agents/claude-code/SKILL.md">hermes-agent/skills/autonomous-ai-agents/claude-code/SKILL.md at main · NousResearch/hermes-agent</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-claude-code">Claude Code — Delegate coding to Claude Code CLI (features, PRs) | Hermes Agent</a></li>

</ul>
</details>

**Discussion**: Community members expressed outrage at Anthropic's initial refusal to issue refunds for their own technical error, calling it unprecedented for a legitimate business. After Anthropic's Thariq announced full refunds and credits, sentiment shifted to cautious appreciation, though some users reported ongoing support issues.

**Tags**: `#bug`, `#billing`, `#Claude Code`, `#Anthropic`, `#AI tools`

---

<a id="item-15"></a>
## [FastCGI Superior to HTTP for Reverse Proxies](https://www.agwa.name/blog/post/fastcgi_is_the_better_protocol_for_reverse_proxies) ⭐️ 7.0/10

A blog post argues that FastCGI is a better protocol than HTTP for reverse proxies due to lower overhead and simpler design. Community discussion adds historical context and mentions alternative protocols like SCGI and WAS. This challenges the widespread use of HTTP for reverse proxying, potentially leading to performance improvements in web server architectures. It also highlights the trade-offs between protocol complexity and simplicity that affect real-world adoption. FastCGI uses a binary protocol with multiplexing and avoids HTTP header parsing overhead, but lacks support for modern features like WebSockets. SCGI is a simpler alternative designed for easier parsing, while WAS introduces a control socket and pipes for efficient data transfer.

hackernews · agwa · Apr 29, 16:16

**Background**: FastCGI is a protocol for web servers to communicate with application servers, improving on CGI by allowing persistent processes. It is commonly used with Nginx and PHP-FPM for high-performance web applications. SCGI (Simple Common Gateway Interface) is a similar protocol designed to be easier to parse than FastCGI, while WAS (Web Application Socket) adds a control socket and pipes for splice() operations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.digitalocean.com/community/tutorials/understanding-and-implementing-fastcgi-proxying-in-nginx">Understanding and Implementing FastCGI Proxying in... | DigitalOcean</a></li>
<li><a href="https://en.wikipedia.org/wiki/Simple_Common_Gateway_Interface">Simple Common Gateway Interface - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters generally agree with the article's premise but note that HTTP won due to simplicity and ubiquity. Some advocate for WAS as a further improvement, praising its use of splice() for zero-copy data transfer. Others express frustration with the proliferation of custom HTTP headers for client IP forwarding.

**Tags**: `#FastCGI`, `#reverse proxy`, `#web protocols`, `#HTTP`, `#SCGI`

---

<a id="item-16"></a>
## [Why Lisp and Scheme Beat Haskell for the Author](https://jointhefreeworld.org/blog/articles/lisps/why-i-still-reach-for-scheme-instead-of-haskell/index.html) ⭐️ 7.0/10

A blog post explains the author's preference for Lisp and Scheme over Haskell, citing interactive debugging and powerful macros as key advantages, which has sparked community discussion. This comparison highlights enduring trade-offs between dynamic and statically typed functional languages, influencing developer productivity and language adoption decisions. The author emphasizes that Lisp allows on-the-fly code changes in production, while Haskell's strong type system imposes more upfront reasoning. However, Scheme lacks the extensive enterprise ecosystem found on the JVM.

hackernews · jjba23 · Apr 29, 08:43

**Background**: Lisp macros are full-blown procedures that operate on code represented as lists, enabling compile-time code transformation and language extension. Haskell, by contrast, relies on a sophisticated type system and pure functions to achieve safety and composability. The debate reflects a long-standing tension between flexibility and safety in language design.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lisp_macros">Lisp macros</a></li>
<li><a href="https://en.wikibooks.org/wiki/Scheme_Programming/Macros">Scheme Programming/Macros - Wikibooks, open books for an open world</a></li>

</ul>
</details>

**Discussion**: Commenters discussed the practical use of macros (e.g., only rarely needed) and the difficulty of debugging in production with Lisp. Some noted the article resembles a 2012 post, while others suggested Clojure as a modern alternative with a richer ecosystem.

**Tags**: `#Lisp`, `#Scheme`, `#Haskell`, `#programming languages`, `#software engineering`

---

<a id="item-17"></a>
## [Maryland bans surveillance pricing in grocery stores](https://www.theguardian.com/technology/2026/apr/29/maryland-grocery-stores-ban-surveillance-pricing) ⭐️ 7.0/10

Maryland Governor Wes Moore signed a law banning surveillance-based dynamic pricing in grocery stores, making Maryland the first U.S. state to enact such a ban. This law sets a precedent for consumer privacy protections against personalized pricing that uses personal data to determine willingness to pay, potentially influencing other states and federal policy. The law bans setting higher prices through surveillance pricing but does not prohibit offering individualized discounts, which critics argue could create a loophole. It also lacks a private right of action, relying instead on the Attorney General for enforcement.

hackernews · 01-_- · Apr 29, 16:50

**Background**: Surveillance pricing is a form of dynamic pricing where personal data such as location, browsing history, and shopping patterns are used to infer a consumer's willingness to pay, potentially leading to price discrimination. The Federal Trade Commission has studied this practice, finding that some companies set different prices based on granular consumer data. This law specifically targets grocery stores, a sector where such pricing could disproportionately affect essential goods.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Surveillance_pricing">Surveillance pricing</a></li>
<li><a href="https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-surveillance-pricing-study-indicates-wide-range-personal-data-used-set-individualized-consumer">FTC Surveillance Pricing Study Indicates Wide Range of Personal Data Used to Set Individualized Consumer Prices | Federal Trade Commission</a></li>
<li><a href="https://www.msn.com/en-us/politics/government/maryland-moves-to-ban-dynamic-pricing-statewide/ar-AA21Cras">Maryland moves to ban ' dynamic pricing ' statewide</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the law's effectiveness, pointing to potential loopholes such as reversing price increases into discounts. Some raised concerns about adversarial pricing and the need for consumer agents to navigate price transparency. Others noted the absence of a private right of action as a limitation.

**Tags**: `#surveillance pricing`, `#privacy`, `#legislation`, `#dynamic pricing`, `#consumer rights`

---

<a id="item-18"></a>
## [DOS 1.0 Source Code Transcribed from Printouts](https://github.com/DOS-History/Paterson-Listings) ⭐️ 7.0/10

A GitHub repository has published a transcription of the original DOS 1.0 source code from Tim Paterson's printouts, using OCR and CRC-based self-error checking to ensure accuracy. This transcription provides historians and developers with unprecedented access to examine the foundational code of MS-DOS, which shaped the PC industry, and allows scrutiny of historical claims about the OS's origins. The transcription project, led by Joshua Scarsbrook, utilized OCR on scanned paper printouts and leveraged CRC checksums printed in the margins to automatically verify accuracy. The code is available for browsing on GitHub.

hackernews · s2l · Apr 29, 11:25

**Background**: MS-DOS 1.0 was released by Microsoft in 1981 for the IBM PC, derived from 86-DOS which Tim Paterson wrote for Seattle Computer Products. Optical character recognition (OCR) converts images of text into machine-readable code, a technology now common but applied here to historical artifacts. The presence of CRC checksums in the printouts allowed for automated error checking during transcription.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optical_character_recognition">Optical character recognition</a></li>
<li><a href="https://en.wikipedia.org/wiki/MS-DOS">MS-DOS</a></li>
<li><a href="https://www.zdnet.com/article/microsoft-open-sources-dos-1-0-much-more-than-the-code/">Microsoft finally open sources DOS 1.0 - and it's so much more than the code | ZDNET</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the official Microsoft announcement with additional links, praise the OCR methodology using CRC checksums, and note that this enables examination of the historical debate about whether CP/M code was included in early DOS. One user also recalled a possible connection to the original Seattle Computer Gazelle machine.

**Tags**: `#DOS`, `#source code`, `#history`, `#OCR`, `#Microsoft`

---

<a id="item-19"></a>
## [Dutch government soft-launches open-source code platform](https://www.nldigitalgovernment.nl/news/soft-launch-for-government-open-source-code-platform/) ⭐️ 7.0/10

The Dutch government soft-launched code.overheid.nl, an open-source code platform for public sector projects, moving away from GitHub. This move promotes transparency and control over government-developed software, setting a precedent for public sector open-source adoption across Europe. The platform already hosts projects like RegelRecht, which encodes Dutch law into machine-readable YAML for deterministic decision logic with a full explanation trail.

hackernews · e12e · Apr 29, 09:14

**Background**: Governments often rely on proprietary platforms like GitHub for code hosting, which can raise concerns about data sovereignty and vendor lock-in. By creating their own open-source platform, the Dutch government can ensure transparency, security, and reuse of public sector code.

**Discussion**: Commenters expressed general approval, with Dutch users noting they had long advocated for such a move. Some discussed the RegelRecht project and compared the initiative to Germany's OpenCode platform.

**Tags**: `#open source`, `#government`, `#Netherlands`, `#code platform`, `#digital government`

---

<a id="item-20"></a>
## [OpenTrafficMap: Low-Cost V2X Traffic Visualization](https://opentrafficmap.org/) ⭐️ 6.0/10

OpenTrafficMap is an open-source project that uses V2X messages from sub-£20 hardware to visualize traffic data on a modern OpenStreetMap-based interface. By drastically reducing the cost of V2X hardware, this project makes traffic data collection accessible to hobbyists and communities, potentially expanding coverage and enabling new citizen-science applications. The hardware uses 802.11p (DSRC) to receive Cooperative Awareness Messages (CAM) and Signal Phase and Timing (SPAT) messages, but currently coverage is limited and does not work in the USA.

hackernews · moooo99 · Apr 29, 19:49

**Background**: Vehicle-to-everything (V2X) communication allows vehicles to interact with other vehicles, infrastructure, and pedestrians. 802.11p is a standard for wireless access in vehicular environments, and OpenStreetMap (OSM) is a free, editable map of the world created by volunteers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vehicle-to-everything">Vehicle-to-everything - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenStreetMap">OpenStreetMap</a></li>

</ul>
</details>

**Discussion**: Commenters were impressed by the sub-£20 hardware cost, noting that 802.11p hardware is typically expensive. They praised the modern OSM-based UI but pointed out a lack of detailed information and that the service does not appear to work in the USA. One commenter wondered about potential vehicle tracking implications.

**Tags**: `#traffic`, `#V2X`, `#openstreetmap`, `#IoT`, `#open data`

---