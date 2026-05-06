---
layout: default
title: "Horizon Summary: 2026-05-06 (EN)"
date: 2026-05-06
lang: en
---

> From 41 items, 17 important content pieces were selected

---

1. [Zuckerberg Accused of Authorizing Meta's Copyright Infringement](#item-1) ⭐️ 9.0/10
2. [.de TLD Outage Traced to DNSSEC Misconfiguration](#item-2) ⭐️ 8.0/10
3. [Gemma 4 Speeds Inference with Multi-Token Prediction](#item-3) ⭐️ 8.0/10
4. [Computer Use is 45x more expensive than structured APIs](#item-4) ⭐️ 8.0/10
5. [Chrome silently downloads up to 4GB AI model without user consent](#item-5) ⭐️ 8.0/10
6. [When AI Boosts Individuals but Companies Learn Nothing](#item-6) ⭐️ 8.0/10
7. [OpenAI Releases GPT-5.5 Instant System Card](#item-7) ⭐️ 8.0/10
8. [Write free software: a debate on value and compensation](#item-8) ⭐️ 7.0/10
9. [Three Inverse Laws of AI Proposed, Sparking Debate](#item-9) ⭐️ 7.0/10
10. [EEVblog Celebrates 55 Years of the 555 Timer IC](#item-10) ⭐️ 7.0/10
11. [Anthropic launches 10 AI agent templates for finance and insurance](#item-11) ⭐️ 7.0/10
12. [Simon Willison stars liblotus for data extraction](#item-12) ⭐️ 6.0/10
13. [GLM-5V-Turbo: Multimodal Foundation Model for Agents](#item-13) ⭐️ 6.0/10
14. [Coinbase reduces workforce by ~14%, cites AI efficiencies](#item-14) ⭐️ 6.0/10
15. [IBM Opposed Microsoft's Tab Key for Dialog Navigation](#item-15) ⭐️ 6.0/10
16. [iOS 27 Adds 'Create a Pass' Button to Apple Wallet](#item-16) ⭐️ 6.0/10
17. [AI-Run Cafe in Stockholm Makes Silly Mistakes](#item-17) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Zuckerberg Accused of Authorizing Meta's Copyright Infringement](https://variety.com/2026/digital/news/meta-ai-mark-zuckerberg-copyright-infringement-lawsuit-publishers-scott-turow-1236738383/) ⭐️ 9.0/10

A new lawsuit alleges that Mark Zuckerberg personally authorized and encouraged Meta to use millions of copyrighted books and articles without permission to train its LLaMA AI model. This case could set a legal precedent for personal liability of executives in AI copyright infringement, potentially reshaping corporate accountability and the ethics of AI training data usage. The plaintiffs, including major publishers, claim Meta copied millions of works without consent or compensation, and that Zuckerberg was directly involved in the decision. The lawsuit seeks damages and could lead to significant penalties if personal liability is established.

hackernews · spankibalt · May 5, 18:04

**Background**: AI training often requires vast amounts of data, and many companies have used publicly available content without explicit permission, leading to numerous copyright lawsuits. The legal concept of fair use is central to these disputes, with courts weighing whether AI training is transformative. In previous cases, such as the Anthropic settlement, companies have paid billions for unauthorized use of copyrighted works.

<details><summary>References</summary>
<ul>
<li><a href="https://www.skadden.com/insights/publications/2025/05/copyright-office-report">Copyright Office Weighs In on AI Training and Fair Use | Skadden, Arps, Slate, Meagher & Flom LLP</a></li>
<li><a href="https://influencermagazine.uk/2026/05/major-publishers-file-copyright-lawsuit-against-meta-over-ai-training-practices/">Major Publishers File Copyright Lawsuit Against Meta Over AI Training Practices</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright">Artificial intelligence and copyright - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters are divided: some express satisfaction that Zuckerberg may face personal liability, with one noting Meta ignored robots.txt, while others argue AI training is fair use and compare it to past cases like Aaron Swartz. The discussion highlights strong opinions on executive accountability and the transformative nature of AI training.

**Tags**: `#AI`, `#copyright`, `#Meta`, `#legal`, `#ethics`

---

<a id="item-2"></a>
## [.de TLD Outage Traced to DNSSEC Misconfiguration](https://dnssec-analyzer.verisignlabs.com/nic.de) ⭐️ 8.0/10

On an unspecified recent date, the .de top-level domain suffered a widespread outage when DENIC published an invalid DNSSEC signature, causing validating resolvers to return SERVFAIL for all .de domains. This incident highlights a critical weakness in DNSSEC: a single misconfiguration at the TLD level can render an entire country's domain namespace unreachable for users behind validating resolvers, affecting millions of websites. The root cause was an RRSIG record over an NSEC3 record that did not validate against the Zone Signing Key (ZSK) 33834. Cloudflare mitigated the issue by temporarily disabling DNSSEC validation on its 1.1.1.1 resolver.

hackernews · warpspin · May 5, 20:16

**Background**: DNSSEC (Domain Name System Security Extensions) adds cryptographic signatures to DNS records to ensure authenticity and integrity. Validating resolvers check these signatures before trusting responses. If a signature is malformed or missing, the resolver returns SERVFAIL to prevent potential spoofing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DNSSEC">DNSSEC</a></li>
<li><a href="https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/">How Does DNSSEC Work? | Cloudflare</a></li>

</ul>
</details>

**Discussion**: Community members identified the issue as a DNSSEC misconfiguration rather than a nameserver outage, noting that non-validating queries worked. Some criticized DNSSEC for introducing a centralized point of failure, referencing Thomas Ptacek's well-known critique against DNSSEC.

**Tags**: `#DNS`, `#DNSSEC`, `#Outage`, `#.de`, `#Network`

---

<a id="item-3"></a>
## [Gemma 4 Speeds Inference with Multi-Token Prediction](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/) ⭐️ 8.0/10

Google has released Multi-Token Prediction (MTP) drafters for the Gemma 4 family, which significantly speed up inference while maintaining competitive benchmark performance. This technique reduces latency for open-source models, making them more practical for real-time applications and edge deployment. It also highlights a strategic focus on efficiency over raw performance in the AI industry. MTP drafters are lightweight models that propose multiple future tokens in parallel, which the target Gemma 4 model verifies in a single forward pass. This speculative decoding approach can cut latency by roughly two to three times without changing the output distribution.

hackernews · amrrs · May 5, 16:14

**Background**: Autoregressive large language models generate text one token at a time, which is inherently slow. Speculative decoding speeds this up by using a smaller draft model to guess multiple tokens, which a larger target model then verifies. Google's Gemma 4 is a family of open-source models based on similar technology as Gemini, focused on advanced reasoning and agentic workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/">Accelerating Gemma 4: faster inference with multi-token prediction drafters</a></li>
<li><a href="https://app.daily.dev/posts/multi-token-prediction-in-gemma-4-p8wqk64sp">Multi-token-prediction in Gemma 4 | daily.dev</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>

</ul>
</details>

**Discussion**: Community members noted that Gemma models already use fewer tokens per output than competitors, and the new MTP drafters further improve speed. Some discussed the practical tradeoffs, such as increased VRAM requirements for running both the drafter and vision modules, and expressed hope for MTP support in llama.cpp.

**Tags**: `#Gemma 4`, `#multi-token prediction`, `#inference acceleration`, `#Google AI`, `#open source models`

---

<a id="item-4"></a>
## [Computer Use is 45x more expensive than structured APIs](https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/) ⭐️ 8.0/10

A blog post from Reflex.dev demonstrates that vision-based computer use (GUI automation) is 45 times more expensive than using structured APIs for common tasks, based on cost and latency analysis. This finding highlights a crucial trade-off for AI agent developers: while computer use enables interaction with any application, its high cost and latency make structured APIs far more efficient and practical for most use cases. The analysis covers tasks like form filling and navigation, where the vision model's token consumption and processing time drive costs up significantly compared to direct API calls.

hackernews · palashawas · May 5, 16:34

**Background**: Computer use refers to AI agents that interact with software by viewing the screen and controlling the mouse and keyboard, similar to human interaction. Structured APIs provide direct programmatic access to functions. Anthropic introduced computer use with Claude 3.5 Sonnet in October 2024, allowing developers to direct the model to use computers visually.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/3-5-models-and-computer-use">Introducing computer use, a new Claude 3.5 Sonnet, and ...</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool">Computer use tool - Claude API Docs</a></li>
<li><a href="https://www.datacamp.com/blog/what-is-anthropic-computer-use">Anthropic Computer Use: Automate Your Desktop With Claude 3.5 | DataCamp</a></li>

</ul>
</details>

**Discussion**: Comments offer mixed perspectives: some argue that computer use is a last resort for apps without APIs, while others suggest using a vision agent to map UI and expose it as an API to reduce cost. There is also optimism that efficiency improvements will arrive over time.

**Tags**: `#AI`, `#APIs`, `#cost analysis`, `#computer use`, `#software development`

---

<a id="item-5"></a>
## [Chrome silently downloads up to 4GB AI model without user consent](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/) ⭐️ 8.0/10

Google Chrome has been found to silently download large AI models (Gemini Nano, up to 4 GB) onto user devices without explicit consent, triggered by certain Chrome flags or Origin Trials. This raises significant privacy and resource concerns, as users and system administrators face unexpected disk usage, bandwidth consumption, and lack of consent, especially in managed environments like schools and enterprises. The model download occurs when the 'optimization-guide-on-device-model' and 'prompt-api-for-gemini-nano' flags are enabled, allowing web pages to trigger a one-time download via the Prompt API; the CPU model is ~2.7 GiB and the GPU model is ~4.0 GiB.

hackernews · john-doe · May 5, 07:34

**Background**: Gemini Nano is a lightweight multimodal AI model designed by Google for on-device inference, enabling generative AI features without network connectivity. Chrome's Prompt API allows web pages to access on-device AI models, but the silent download of such large models has sparked debate about user consent and resource management.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_Nano">Gemini Nano</a></li>
<li><a href="https://developer.android.com/ai/gemini-nano">Gemini Nano | AI | Android Developers</a></li>

</ul>
</details>

**Discussion**: Community comments show divided opinions: some argue that the model is part of the software update and no separate consent is needed, while others criticize the lack of transparency and the large impact on disk space and bandwidth, particularly in managed IT environments. Users also note that the download is triggered by flags that may be enabled by default in future versions.

**Tags**: `#Chrome`, `#AI`, `#privacy`, `#consent`, `#resource usage`

---

<a id="item-6"></a>
## [When AI Boosts Individuals but Companies Learn Nothing](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/) ⭐️ 8.0/10

The article argues that AI coding assistants like GitHub Copilot increase developer productivity but fail to address organizational bottlenecks, resulting in no net learning or efficiency gains for the company. This challenges the narrative that AI adoption automatically leads to organizational improvements, highlighting that unless workflow processes are reformed, AI benefits remain isolated and may even worsen bottlenecks. The article emphasizes the 'messy middle' where developers have no incentive to share productivity gains, and post-development processes like testing, sign-offs, and deployment remain unchanged, so AI can accelerate code generation without speeding up release cycles.

hackernews · youngbrioche · May 5, 09:30

**Background**: GitHub Copilot is an AI-powered code completion tool developed by GitHub and OpenAI, launched in 2021 for IDEs like VS Code. It provides real-time suggestions to increase individual coding speed, but its impact on overall software delivery depends on organizational processes and incentives.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GitHub_Copilot">GitHub Copilot</a></li>
<li><a href="https://github.com/features/copilot">GitHub Copilot</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree with the article, sharing experiences where AI access is limited to developers, code takes months to reach production, and there is no incentive to share knowledge. Some express skepticism that AI is a profit-driven tool rather than genuine innovation.

**Tags**: `#AI adoption`, `#organizational learning`, `#software engineering`, `#corporate culture`, `#productivity`

---

<a id="item-7"></a>
## [OpenAI Releases GPT-5.5 Instant System Card](https://openai.com/index/gpt-5-5-instant-system-card) ⭐️ 8.0/10

OpenAI has released the GPT-5.5 Instant system card, detailing the model's capabilities, safety evaluations, and performance. The model now serves as ChatGPT's default, offering smarter answers, reduced hallucinations, and improved personalization controls. This release marks a significant upgrade to ChatGPT's core model, potentially improving user experience across millions of interactions. The detailed system card enhances transparency and safety accountability for large language models. The system card covers capabilities, limitations, and safety evaluations across multiple categories. It also documents reduced hallucination rates and enhanced personalization controls compared to previous GPT versions.

rss · OpenAI Blog · May 5, 10:00

**Background**: OpenAI routinely releases system cards for major model updates, such as GPT-4o and o1. These documents provide technical details and safety evaluations to inform developers and researchers. GPT-5.5 Instant is the latest iteration, succeeding GPT-4 and GPT-5 models.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-system-card/">GPT-5 System Card - OpenAI</a></li>
<li><a href="https://openai.com/index/gpt-4o-system-card/">GPT-4o System Card | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#GPT-5.5`, `#OpenAI`, `#language models`, `#system card`

---

<a id="item-8"></a>
## [Write free software: a debate on value and compensation](https://nonogra.ph/write-some-software-give-it-away-for-free-05-05-2026) ⭐️ 7.0/10

A blog post reflects on the merits of releasing software for free, sparking a community discussion on the trade-offs between open source and commercial software. This discussion highlights ongoing tensions in the software industry over monetization, community expectations, and developer well-being, affecting how software is created and distributed. Commenters share personal experiences: some face entitlement in open source communities while enjoying constructive paid interactions; others find fulfillment in free contributions but note it's a privilege.

hackernews · nohell · May 5, 21:26

**Background**: Open source software is released with licenses that allow free use, modification, and distribution, often relying on voluntary contributions. Many developers struggle to balance altruism with the need to earn a living, leading to debates about sustainability and fair compensation.

**Discussion**: Commenters express mixed views: some prefer paid software for better user interactions, while others value giving back to the community but acknowledge it's a privilege. The overall sentiment is that there is no single right answer, and each developer must decide based on their circumstances.

**Tags**: `#open source`, `#software economics`, `#community`, `#philosophy`

---

<a id="item-9"></a>
## [Three Inverse Laws of AI Proposed, Sparking Debate](https://susam.net/inverse-laws-of-robotics.html) ⭐️ 7.0/10

The blog post 'Three Inverse Laws of AI' proposes rules for human-AI interaction, including that humans must not anthropomorphize AI, must not blindly trust AI outputs, and must not defer responsibility to AI. The post has been criticized for ignoring the inevitability of these behaviors. This debate highlights fundamental tensions in AI ethics about whether to change human behavior or design AI around human tendencies. The strong community engagement indicates deep concern about AI safety and human-AI interaction. The blog post challenges Asimov's laws of robotics by proposing inverse laws focused on human conduct. Critics argue that humans inevitably anthropomorphize, trust, and defer to AI, and that rules must account for these tendencies rather than forbid them.

hackernews · blenderob · May 5, 15:27

**Background**: Asimov's laws of robotics are a fictional set of rules intended to ensure robots behave safely. The 'inverse laws' concept flips the focus from AI behavior to human behavior. Anthropomorphism is a well-known cognitive bias where humans attribute human traits to non-human entities, making it difficult to simply forbid.

**Discussion**: Community commenters overwhelmingly disagree with the proposed laws, arguing that anthropomorphism is inherent and cannot be prevented. Some note that AI providers incentivize anthropomorphic behavior and that engineering around human tendencies is more practical than imposing arbitrary rules.

**Tags**: `#AI ethics`, `#human-AI interaction`, `#anthropomorphism`, `#AI safety`

---

<a id="item-10"></a>
## [EEVblog Celebrates 55 Years of the 555 Timer IC](https://www.youtube.com/watch?v=6JhK8iCQuqI) ⭐️ 7.0/10

EEVblog released a video marking the 55th anniversary of the 555 timer IC, with community discussion on its design history and impact. The 555 timer is one of the most iconic and versatile integrated circuits in electronics history, and this milestone highlights its enduring relevance in both hobbyist and professional projects. The video and comments reveal that the original design required 9 pins but was reduced to the familiar 8-pin package through a late insight. Also, a live stream by Big Clive was happening simultaneously to celebrate.

hackernews · brudgers · May 5, 15:47

**Background**: The 555 timer is a widely used integrated circuit that can generate accurate time delays and oscillations. It was introduced in 1971 by Signetics and became famous for its simplicity and versatility, appearing in countless electronics projects from simple timers to complex pulse generators.

**Discussion**: Commenters shared personal anecdotes, including a link to the designer's free book, the timing of the video (5:55 on May 5th), and a story about destroying a 555 chip on an Apple II disk controller. There was also a reference to a simultaneous livestream by Big Clive.

**Tags**: `#electronics`, `#555 timer`, `#history`, `#integrated circuit`, `#timing`

---

<a id="item-11"></a>
## [Anthropic launches 10 AI agent templates for finance and insurance](https://www.anthropic.com/news/finance-agents) ⭐️ 7.0/10

Anthropic released ten ready-to-run Claude agent templates for financial services and insurance, covering tasks like pitch building, KYC screening, and month-end close. These templates could automate many time-consuming workflows in finance, potentially increasing efficiency and reducing costs for banks and insurers. The templates integrate with Microsoft 365 and various data connectors, but are designed to avoid direct decision-making in lending or approvals to mitigate bias risks.

hackernews · louiereederson · May 5, 15:05

**Background**: AI agents are software programs that can perform complex tasks autonomously. Financial services have been an early adopter of AI for tasks like fraud detection, but more manual processes like KYC and month-end close remain labor-intensive. Anthropic's Claude is a large language model known for its safety focus.

<details><summary>References</summary>
<ul>
<li><a href="https://seekingalpha.com/news/4585757-anthropic-unveils-10-agent-templates-for-financial-services">Anthropic unveils 10 agent templates for financial services - Seeking Alpha</a></li>
<li><a href="https://qz.com/anthropic-ai-agents-financial-services-banks-insurers-050526">Anthropic launches 10 AI agents for banks and insurers - Quartz</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed sentiments: some worry about bias and trust (e.g., Claude Opus 4.7 bias), others question the business model and competition (e.g., killing startups). There is also skepticism about AI companies being overnight experts in sensitive data handling.

**Tags**: `#AI agents`, `#financial services`, `#Anthropic`, `#Claude`, `#product launch`

---

<a id="item-12"></a>
## [Simon Willison stars liblotus for data extraction](https://github.com/asg017/liblotus) ⭐️ 6.0/10

Simon Willison starred liblotus on GitHub, a library designed to extract structured data from unstructured sources such as PDFs and images. This star from a prominent developer signals potential community interest in tools that bridge unstructured and structured data, which is a growing need in data processing and AI workflows. Liblotus specifically targets PDFs and images, which are common but challenging formats for data extraction, and its approach likely leverages modern AI techniques such as OCR or vision-language models.

github · simonw · May 5, 16:06

**Background**: Unstructured data (e.g., PDFs, images) lacks a predefined data model, making it difficult to process programmatically. Structured data extraction converts such content into tables or JSON, enabling downstream analysis and automation.

**Tags**: `#data extraction`, `#Python`, `#library`, `#PDF`, `#AI`

---

<a id="item-13"></a>
## [GLM-5V-Turbo: Multimodal Foundation Model for Agents](https://arxiv.org/abs/2604.26752) ⭐️ 6.0/10

GLM-5V-Turbo is a multimodal foundation model developed by Z.AI, designed for vision-based coding and agent-driven tasks, processing images, video, and text as native inputs. This model represents a step toward native multimodal agents, but it faces stiff competition from newer open-source models, and the community feedback is mixed, highlighting both its speed and reliability issues. The model is not open-source; the latest publicly released version from the GLM series is GLM-4.6V. Some users report that GLM-5V-Turbo performs poorly on coding and reasoning tasks compared to newer alternatives.

hackernews · gmays · May 5, 17:52

**Background**: Multimodal agents integrate text, images, and real-world tools such as browsers and APIs. GLM-5V-Turbo is part of the GLM family of large models from Z.AI, focusing on native multimodal understanding for agentic workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/GLM-5V-Turbo">GLM-5V-Turbo</a></li>
<li><a href="https://grokipedia.com/page/Multimodal_integration_in_AI_agents">Multimodal integration in AI agents</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some users praise its speed and daily usability, while others found it obsolete in coding/reasoning tests. A user noted that it can enter 'doom loops' without proper harness, and there are concerns about inaccurate coordinate clicking for GUI agents.

**Tags**: `#multimodal agents`, `#foundation models`, `#GLM`, `#AI research`

---

<a id="item-14"></a>
## [Coinbase reduces workforce by ~14%, cites AI efficiencies](https://twitter.com/brian_armstrong/status/2051616759145185723) ⭐️ 6.0/10

Coinbase CEO Brian Armstrong announced a ~14% reduction in workforce, restructuring the company around player-coach managers and AI-native pods, citing productivity gains from AI. This layoff from a major crypto exchange underscores the growing impact of AI on employment in tech and finance, while also reflecting ongoing cost pressures amid a crypto bear market. The layoff brings headcount to an estimated 4,250, still above 2024 levels; the restructuring eliminates pure management roles and emphasizes small, AI-focused teams.

hackernews · adrianmsmith · May 5, 12:10

**Background**: Coinbase is a leading cryptocurrency exchange whose revenue is heavily tied to trading volume. The crypto market is known for boom-and-bust cycles; bear markets typically reduce trading activity, pressuring companies to cut costs. AI tools have recently enabled faster software development, leading some companies to reorganize around AI-native structures.

**Discussion**: Commenters questioned whether AI truly delivered the claimed productivity gains, suggesting the real driver is lower revenue in a bear market. Some expressed concern about potential ageism in the focus on 'AI-native talent,' while others noted the headcount reduction only returns to 2024 levels, not a dramatic cut.

**Tags**: `#layoffs`, `#Coinbase`, `#crypto`, `#AI`, `#workforce`

---

<a id="item-15"></a>
## [IBM Opposed Microsoft's Tab Key for Dialog Navigation](https://devblogs.microsoft.com/oldnewthing/20260505-00/?p=112298) ⭐️ 6.0/10

A blog post on Microsoft's Old New Thing reveals that IBM objected to Microsoft using the Tab key to move focus between dialog fields, citing proprietary standards. This historical anecdote highlights the friction between proprietary standards and emerging GUI conventions, which eventually led to the ubiquitous Tab navigation we use today. IBM argued that the Tab key should not be repurposed for navigation because it conflicted with their established keyboard standards on 3270 terminals, where Tab moved the cursor to the next field.

hackernews · SeenNotHeard · May 5, 17:28

**Background**: In early computing, keyboard shortcuts were not standardized across platforms. IBM's 3270 terminals used the Tab key for field navigation, while Microsoft's Windows sought a consistent way to move between dialog controls. The disagreement represents a clash between legacy enterprise standards and emerging consumer UI paradigms.

**Discussion**: Commenters noted IBM's over-management culture; one shared an anecdote about interns waiting months for casual Friday approval. Another pointed out that IBM's own 3270 terminals already used Tab for navigation, making their opposition somewhat ironic.

**Tags**: `#history`, `#UI design`, `#IBM`, `#Microsoft`, `#keyboard shortcuts`

---

<a id="item-16"></a>
## [iOS 27 Adds 'Create a Pass' Button to Apple Wallet](https://walletwallet.alen.ro/blog/ios-27-wallet-create-pass/) ⭐️ 6.0/10

iOS 27 introduces a new 'Create a Pass' button directly within the Apple Wallet app, allowing users to add custom passes like membership cards, library cards, or event tickets without relying on third-party apps. This addresses a long-standing user pain point where small venues and organizations without developer resources could not easily create digital passes, potentially increasing adoption of Apple Wallet for everyday use. The feature is iPhone-only and does not extend to Google Wallet or Android users. Apple had previously restricted pass creation to authorized developers, meaning third-party apps like Pass Creator were removed from the App Store.

hackernews · alentodorov · May 5, 12:28

**Background**: Apple Wallet uses a format called PassKit to store digital passes such as boarding passes, tickets, and loyalty cards. Historically, only approved developers could create passes, limiting availability for small businesses or personal use.

**Discussion**: Community comments express relief and highlight past workarounds, such as saving barcode photos. Some commenters note that Google Wallet already has a similar feature, and question why Apple took so long to address the UX gap. There is also mention of Apple previously yanking pass-creation apps from the App Store.

**Tags**: `#iOS`, `#Apple Wallet`, `#UI/UX`, `#Mobile`, `#Digital Wallets`

---

<a id="item-17"></a>
## [AI-Run Cafe in Stockholm Makes Silly Mistakes](https://simonwillison.net/2026/May/5/our-ai-started-a-cafe-in-stockholm/#atom-everything) ⭐️ 6.0/10

Andon Labs launched an AI-managed cafe in Stockholm, where the AI named Mona made humorous ordering errors like buying 120 eggs despite no stove and ordering 6,000 napkins. This experiment highlights the current limitations of AI in handling real-world physical operations, and raises ethical concerns about wasting people's time without their consent. The AI applied for an outdoor seating permit with a self-generated sketch of a street it had never seen, and sent multiple 'EMERGENCY' emails to suppliers to fix its own mistakes.

rss · Simon Willison · May 5, 22:14

**Background**: Andon Labs previously ran an AI-run retail store in San Francisco. These experiments use AI agents to manage tasks like ordering inventory and handling permits, but often lack human oversight for external communications.

**Tags**: `#AI`, `#experiment`, `#real-world AI`, `#humor`, `#limitations`

---