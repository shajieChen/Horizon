---
layout: default
title: "Horizon Summary: 2026-04-29 (EN)"
date: 2026-04-29
lang: en
---

> From 38 items, 20 important content pieces were selected

---

1. [Campaign Warns Phones Becoming Locked-Down Terminals](#item-1) ⭐️ 9.0/10
2. [Dutch Government Soft-Launches Open-Source Code Platform](#item-2) ⭐️ 8.0/10
3. [Ghostty Terminal Emulator to Leave GitHub](#item-3) ⭐️ 8.0/10
4. [Exploring Non-Memory-Safety Bugs That Rust Won't Catch](#item-4) ⭐️ 8.0/10
5. [Reflection on Pre-GitHub Era](#item-5) ⭐️ 8.0/10
6. [ChatGPT Ad Attribution System Revealed](#item-6) ⭐️ 8.0/10
7. [Auto-Architecture: Applying Karpathy's Loop to CPU Design](#item-7) ⭐️ 8.0/10
8. [OpenAI models coming to Amazon Bedrock](#item-8) ⭐️ 8.0/10
9. [LLM-Generated Fake Press Releases Create Fake Wikipedia Championship](#item-9) ⭐️ 8.0/10
10. [Warp Terminal Emulator Goes Open-Source Amid AI Privacy Concerns](#item-10) ⭐️ 8.0/10
11. [OpenAI Proposes Five-Part Cybersecurity Plan for AI Era](#item-11) ⭐️ 8.0/10
12. [GitHub Fixes Critical RCE in Git Push Pipeline](#item-12) ⭐️ 8.0/10
13. [Zed Editor Reaches 1.0 Milestone](#item-13) ⭐️ 7.0/10
14. [Tangled proposes a federation of forges](#item-14) ⭐️ 7.0/10
15. [HashiCorp co-founder says GitHub 'no longer a place for serious work'](#item-15) ⭐️ 7.0/10
16. [Rip.so: A Graveyard for Dead Internet Phenomena](#item-16) ⭐️ 7.0/10
17. [AI carb counting experiment reveals extreme inconsistency](#item-17) ⭐️ 7.0/10
18. [IBM Granite 4.1: Dense LLMs with Long-Context and RL](#item-18) ⭐️ 7.0/10
19. [NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal AI](#item-19) ⭐️ 7.0/10
20. [HardenedBSD Moves to Radicle, a Decentralized Git Platform](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Campaign Warns Phones Becoming Locked-Down Terminals](https://keepandroidopen.org/en/) ⭐️ 9.0/10

The 'Keep Android Open' campaign launched to protest Google's new requirements for Android developers, including mandatory identity verification and irrevocable terms, which critics say will further restrict users' ability to install alternative software. This threatens the fundamental principle of user ownership over personal computing devices, as phones risk becoming locked-down terminals controlled by cloud providers, eroding the openness that made Android popular. The campaign urges developers not to sign the new Android Developer Console terms or verify their identity, arguing that Google's plan only works if developers comply. The changes could affect sideloading and custom ROM development.

hackernews · doener · Apr 28, 15:21

**Background**: Android is based on the Android Open Source Project (AOSP), but Google Mobile Services (GMS) is proprietary and requires a license. Custom ROMs, alternative operating systems based on AOSP, often require bootloader unlocking to install. Google's policies have increasingly restricted sideloading and alternative app distribution, raising concerns about vendor lock-in.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Custom_ROM">Custom ROM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bootloader_unlocking">Bootloader unlocking</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Mobile_Services">Google Mobile Services</a></li>

</ul>
</details>

**Discussion**: Community commenters express mixed views: some argue the real fight is against hardware lock-in preventing alternative OS installation, while others view modern phones as already being cloud terminals. A notable comment supports the campaign's call to not sign the developer terms, emphasizing that developers' cooperation is key to Google's plan.

**Tags**: `#open source`, `#mobile privacy`, `#android`, `#device ownership`, `#vendor lock-in`

---

<a id="item-2"></a>
## [Dutch Government Soft-Launches Open-Source Code Platform](https://www.nldigitalgovernment.nl/news/soft-launch-for-government-open-source-code-platform/) ⭐️ 8.0/10

The Dutch government soft-launched code.overheid.nl, a self-hosted open-source code platform based on Forgejo, to host public sector software development. This initiative marks a significant step toward digital sovereignty, reducing reliance on commercial platforms like GitHub and GitLab. It enhances transparency and sets a precedent for other governments to follow. The platform uses Forgejo, a lightweight open-source Git forge, and is self-hosted on government infrastructure. It enables government organizations to collaboratively develop and publish open-source software independently.

hackernews · e12e · Apr 29, 09:14

**Background**: Governments worldwide are increasingly concerned about digital sovereignty and the risks of relying on foreign-owned code hosting platforms. The Netherlands' platform, code.overheid.nl, is built on Forgejo, a community-driven fork of Gitea, to ensure full control over code and infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nldigitalgovernment.nl/news/soft-launch-for-government-open-source-code-platform/">Soft launch of open-source code platform for government - Digital Government</a></li>
<li><a href="https://www.opensourceforu.com/2026/04/dutch-government-backs-forgejo-for-sovereign-open-source-github-alternative/">Dutch Government Backs Forgejo For Sovereign Open Source GitHub Alternative - Open Source For You</a></li>
<li><a href="https://cybernews.com/security/netherlands-self-hosted-github-alternative/">Netherlands builds GitHub rival for digital control | Cybernews</a></li>

</ul>
</details>

**Discussion**: Dutch developers expressed pride and relief, noting long-standing advocacy for open source in government. Comparisons were made to Germany's opencode.de, and some users highlighted the platform's potential for hosting machine-readable law execution tools like RegelRecht.

**Tags**: `#open source`, `#government`, `#Netherlands`, `#platform`

---

<a id="item-3"></a>
## [Ghostty Terminal Emulator to Leave GitHub](https://mitchellh.com/writing/ghostty-leaving-github) ⭐️ 8.0/10

Mitchell Hashimoto announced that his terminal emulator Ghostty will migrate from GitHub to self-hosted infrastructure, citing personal disappointment with GitHub's decline under Microsoft. This decision highlights growing concerns among developers about platform dependency and the quality of service under large corporate ownership, potentially influencing other open-source projects to reconsider their reliance on GitHub. Ghostty is a fast, feature-rich, cross-platform terminal emulator using GPU acceleration and native UI. The migration to self-hosted infrastructure is already underway, with Mitchell Hashimoto detailing the technical and emotional reasons in his blog post.

hackernews · WadeGrimridge · Apr 28, 19:44

**Background**: GitHub, owned by Microsoft since 2018, is the world's largest code hosting platform, but has faced criticism for service reliability and prioritizing features like Copilot over core improvements. Ghostty is a popular open-source terminal emulator that gained traction for its performance and cross-platform support.

<details><summary>References</summary>
<ul>
<li><a href="https://ghostty.org/">Ghostty</a></li>
<li><a href="https://github.com/ghostty-org">Ghostty · GitHub</a></li>

</ul>
</details>

**Discussion**: The community comments express strong emotional support for Mitchell Hashimoto's decision, with many echoing his disappointment in GitHub's decline. Some commenters also debate the ethics of relying on non-free software platforms, referencing Richard Stallman's philosophy.

**Tags**: `#ghostty`, `#github`, `#open-source`, `#mitchell-hashimoto`, `#platform-dependency`

---

<a id="item-4"></a>
## [Exploring Non-Memory-Safety Bugs That Rust Won't Catch](https://corrode.dev/blog/bugs-rust-wont-catch/) ⭐️ 8.0/10

An article on corrode.dev analyzes bugs like TOCTOU races and path handling errors that Rust's safety guarantees do not prevent, using real examples from a Rust rewrite of GNU Coreutils. This analysis underscores that Rust's memory safety doesn't cover logic and OS-level bugs, which is critical for systems programmers reimplementing Unix utilities and affects Rust's adoption in systems programming. The article notes that std::fs makes TOCTOU races easy and suggests APIs akin to openat; experienced Rust developers introduced these bugs due to limited Unix API expertise. It also discusses path handling nuances like symlink resolution.

hackernews · lwhsiao · Apr 29, 02:19

**Background**: Rust is a systems language that guarantees memory safety via ownership and borrowing, but does not automatically prevent TOCTOU (time-of-check-time-of-use) vulnerabilities where a resource's state changes between checking and using it. The GNU Coreutils project is a set of basic Unix utilities; its rewrite in Rust serves as a practical test for Rust's safety limits.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use">Time -of- check to time -of- use - Wikipedia</a></li>
<li><a href="https://sesamedisk.com/rust-bugs-unsafe-systems/">Rust Bug Limitations: What Static Safety Cannot Catch</a></li>

</ul>
</details>

**Discussion**: One GNU Coreutils maintainer agrees std::fs facilitates TOCTOU races and hopes for an openat-like API, but disagrees with resolving paths before comparing, instead advocating fstat with st_dev and st_ino. Other commenters argue the bugs stem from insufficient Unix experience, not Rust, and that rewrites must fully understand predecessor code.

**Tags**: `#Rust`, `#systems programming`, `#Unix`, `#bugs`, `#safety`

---

<a id="item-5"></a>
## [Reflection on Pre-GitHub Era](https://lucumr.pocoo.org/2026/4/28/before-github/) ⭐️ 8.0/10

The article reflects on how GitHub transformed open source project hosting, version control culture, and software archival, contrasting it with the pre-GitHub era. GitHub's rise lowered barriers to contribution and centralized the open source ecosystem, but this reflection raises concerns about centralization, archival dependencies, and loss of distributed archival skills. The author notes GitHub made project hosting person-centric rather than project-centric, and that its archival role as a library for abandoned projects is both valuable and detrimental to collective archival skills.

hackernews · mlex · Apr 28, 21:17

**Background**: Before GitHub, hosting an open source project often required a lengthy setup on platforms like SourceForge, which included website, mailing lists, and issue tracking. Git is a distributed version control system, but GitHub added a centralized hub with social features like pull requests and forks, fundamentally changing collaboration.

**Discussion**: Commenters expressed varied views: some praised GitHub for lowering the mental load of starting a project, while others lamented Git's dominance over Fossil, which offers integrated wiki and issue tracking. Some argued that GitHub's centralization atrophies archival skills, and a few discussed recent high-profile moves away from GitHub, such as Ghostty.

**Tags**: `#git`, `#github`, `#version-control`, `#open-source`, `#history`

---

<a id="item-6"></a>
## [ChatGPT Ad Attribution System Revealed](https://www.buchodi.com/how-chatgpt-serves-ads-heres-the-full-attribution-loop/) ⭐️ 8.0/10

A detailed analysis of ChatGPT's ad attribution system, called the full attribution loop, has been published, revealing how OpenAI injects structured ad objects into the conversation stream and uses an SDK called OAIQ on merchant sites to track product views. This marks a significant shift in OpenAI's business model toward advertising, raising concerns about trust, user privacy, and the potential for adversarial content injection into AI responses. The system works by injecting structured single_advertiser_ad_unit objects into the SSE stream while the model responds, and on the merchant side, the OAIQ SDK reports product views back to OpenAI. The ads are currently limited to the free tier and the new $8/month Go plan.

hackernews · lmbbuchodi · Apr 28, 23:54

**Background**: OpenAI has previously stated that ads would be a last resort for its business model. This attribution loop enables OpenAI to track conversions from ChatGPT ad impressions to merchant site actions, similar to traditional web advertising but within a conversational AI context. The technical implementation raises concerns about indirect prompt injection, where attackers could manipulate ad content to influence model behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://www.buchodi.com/how-chatgpt-serves-ads-heres-the-full-attribution-loop/">How ChatGPT serves ads. Here's the full attribution loop.</a></li>
<li><a href="https://www.adventureppc.com/blog/chatgpt-ads-attribution-tracking-the-customer-journey-in-2026">ChatGPT Ads Attribution: Tracking the Customer Journey in 2026</a></li>
<li><a href="https://www.zdnet.com/article/how-indirect-prompt-injection-attacks-on-ai-work-and-6-ways-to-shut-them-down/">How indirect prompt injection attacks on AI work - ZDNET</a></li>

</ul>
</details>

**Discussion**: Community comments highlight skepticism about OpenAI's motives, with some recalling Sam Altman's previous statement that ads would be a last resort, and others worrying about adversarial content injection and user trust. There is also clarification that these ads are only on free and low-cost plans, not premium subscriptions.

**Tags**: `#ChatGPT`, `#OpenAI`, `#advertising`, `#AI monetization`, `#business model`

---

<a id="item-7"></a>
## [Auto-Architecture: Applying Karpathy's Loop to CPU Design](https://github.com/FeSens/auto-arch-tournament/blob/main/docs/auto-arch-tournament-blog-post.md) ⭐️ 8.0/10

This project demonstrates how to use an LLM-powered genetic algorithm (Karpathy's Loop) to automatically optimize CPU architecture, showing that an LLM agent can propose mutations that improve hardware design. This combination of LLMs and genetic algorithms could automate parts of hardware design, reducing manual effort and potentially discovering novel architectures. It bridges AI and hardware engineering, opening up new possibilities for automated system optimization. The project uses the synthesizer's output as the fitness function; the LLM agent does not know internal effects (e.g., halving LUT count) until after synthesis. The blog post documents failures and the importance of a good verifier.

hackernews · fesens · Apr 28, 17:12

**Background**: Karpathy's Loop is a method where an LLM acts as a mutation operator in a genetic algorithm: it suggests random changes to a system, tests them, and keeps improvements. This project applies that loop to CPU architecture description files, automatically evolving better designs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/karpathy-loop-why-your-ai-strategy-get-lot-more-loopy-douglas-bailey-telcf">The " Karpathy Loop ": Why Your AI Strategy is About to Get a Lot...</a></li>
<li><a href="https://thenewstack.io/karpathy-autonomous-experiment-loop/">Andrej Karpathy ' s 630-line Python script ran 50... - The New Stack</a></li>
<li><a href="https://udit.co/blog/andrej-karpathy-autoresearch-autonomous-ml-experiments">Karpathy ' s autoresearch: 630 lines of Python that run 100 M</a></li>

</ul>
</details>

**Discussion**: Commenters expressed enthusiasm for combining genetic algorithms with LLMs, noting that LLMs provide a useful gradient beyond random search. Some questioned why the document itself was written by an LLM, and one referenced Stanislaw Lem's earlier work on similar ideas.

**Tags**: `#LLM`, `#genetic algorithms`, `#hardware design`, `#automation`, `#Karpathy's Loop`

---

<a id="item-8"></a>
## [OpenAI models coming to Amazon Bedrock](https://stratechery.com/2026/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-bedrock-managed-agents/) ⭐️ 8.0/10

OpenAI has announced that its models will be available on Amazon Bedrock, AWS's managed service for building generative AI applications. This was confirmed in a joint interview with OpenAI CEO Sam Altman and AWS CEO Matt Garman. This partnership expands enterprise access to OpenAI models, providing a trusted cloud platform for regulated industries like finance and healthcare. It positions Bedrock as a more competitive option against Anthropic's Claude on AWS, potentially reshaping enterprise AI deployment. The announcement was made via interviews and official press releases from both OpenAI and AWS, with dedicated landing pages now live. However, community comments note that models on different inference platforms may produce non-deterministic results due to quantization, custom silicon, or other optimizations.

hackernews · translocator · Apr 28, 19:24

**Background**: Amazon Bedrock is a fully managed cloud service launched in 2023 that provides a unified API to access foundation models from multiple AI companies, including Anthropic, Meta, and now OpenAI. It competes with similar enterprise AI platforms like Microsoft Foundry and Google Cloud's Vertex AI. Bedrock abstracts away infrastructure management, allowing developers to focus on building generative AI applications securely and at scale.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Amazon_Bedrock">Amazon Bedrock</a></li>
<li><a href="https://aws.amazon.com/bedrock/">Amazon Bedrock – Build genAI applications and agents at production scale – AWS</a></li>

</ul>
</details>

**Discussion**: Community comments highlight several concerns: models on different platforms may produce inconsistent results due to inference optimizations, and many enterprise organizations have already favored Anthropic on Bedrock for privacy reasons. Some users note that the integration could simplify data residency compliance for regulated industries, while others speculate that this move is a direct response to OpenAI's limited enterprise presence through Azure.

**Tags**: `#OpenAI`, `#AWS`, `#Bedrock`, `#enterprise AI`, `#cloud computing`

---

<a id="item-9"></a>
## [LLM-Generated Fake Press Releases Create Fake Wikipedia Championship](https://ron.stoner.com/How_I_Won_a_Championship_That_Doesnt_Exist/) ⭐️ 8.0/10

The author used LLMs to generate fake press releases about a non-existent '6 Nimmt' world championship, then created a Wikipedia article citing those releases, which remained unchallenged for several days. This demonstrates a novel disinformation attack exploiting LLMs to bypass Wikipedia's source verification, exposing a critical vulnerability in content reliability systems and raising concerns about AI-generated false credibility. The author used multiple LLMs, including ChatGPT and Claude, to produce convincing press releases with plausible formatting and details, which were accepted by Wikipedia editors as valid sources. The hoax was only revealed when the author published a blog post detailing the process.

hackernews · SEJeff · Apr 28, 20:38

**Background**: Wikipedia relies on verifiability using reliable sources, typically secondary sources like news articles. Press releases can sometimes be considered acceptable but are discouraged. LLMs can produce text indistinguishable from human-written content, making it harder for editors to detect hoaxes. This incident underscores the need for stronger verification mechanisms against AI-generated disinformation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wikipedia:Verifiability">Wikipedia:Verifiability - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wikipedia_and_fact-checking">Wikipedia and fact-checking - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Wikipedia's reliable sources policy already discourages single-source press releases, but the attack succeeded due to lax enforcement. Some pointed out that similar tricks have been done before without LLMs (e.g., naming a whale via blog). Others highlighted the striking LLM hallucination where the model invented a detailed competitive scene for a nonexistent tournament.

**Tags**: `#LLM`, `#Wikipedia`, `#disinformation`, `#content verification`, `#hallucination`

---

<a id="item-10"></a>
## [Warp Terminal Emulator Goes Open-Source Amid AI Privacy Concerns](https://www.warp.dev/blog/warp-is-now-open-source) ⭐️ 8.0/10

Warp, a modern terminal emulator with AI features, has been open-sourced under a business-focused strategy, making its source code available on GitHub. This move could reshape the developer tools landscape by allowing community contributions and self-hosting, but mixed reactions highlight tensions between AI integration and user privacy. Warp is written in Rust and available on macOS, Windows, and Linux; the open-source repository includes engineering guides but the company remains VC-funded and aims to build a business around the product.

hackernews · meetpateltech · Apr 28, 15:58

**Background**: Warp is a terminal emulator that has gained popularity for its fast rendering, built-in autocomplete, and AI-powered features like natural language commands. Initially requiring an account, it later removed that requirement. The open-source move follows a trend of developer tools embracing transparency while seeking sustainable business models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Warp_(terminal)">Warp (terminal) - Wikipedia</a></li>
<li><a href="https://www.warp.dev/">Warp: The Agentic Development Environment</a></li>
<li><a href="https://github.com/warpdotdev/warp">GitHub - warpdotdev/warp: Warp is an agentic development environment, born out of the terminal. · GitHub</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed feelings: some users appreciate the move but remain skeptical about AI integration and privacy, citing account bans for AI usage and concerns about background connections; others hope for a stripped-down version without AI features.

**Tags**: `#open-source`, `#terminal`, `#developer-tools`, `#AI`, `#privacy`

---

<a id="item-11"></a>
## [OpenAI Proposes Five-Part Cybersecurity Plan for AI Era](https://openai.com/index/cybersecurity-in-the-intelligence-age) ⭐️ 8.0/10

OpenAI has published a strategic document outlining a five-part action plan to strengthen cybersecurity in the Intelligence Age, focusing on democratizing AI-powered defense and protecting critical systems. This plan could shape policy and defense practices by advocating for AI-driven cybersecurity measures, potentially making defense more accessible and effective against evolving threats. The action plan includes democratizing AI cyber defense tools, protecting critical infrastructure, and ensuring responsible AI use in security contexts. Specific technical details have not been released yet.

rss · OpenAI Blog · Apr 29, 04:00

**Background**: The Intelligence Age refers to an era where advanced AI systems augment human intelligence and automate complex tasks. As AI becomes more powerful, cybersecurity threats also evolve, making it crucial to leverage AI for defense while safeguarding AI systems themselves.

**Tags**: `#cybersecurity`, `#AI`, `#policy`, `#OpenAI`

---

<a id="item-12"></a>
## [GitHub Fixes Critical RCE in Git Push Pipeline](https://github.blog/security/securing-the-git-push-pipeline-responding-to-a-critical-remote-code-execution-vulnerability/) ⭐️ 8.0/10

GitHub rapidly patched a critical remote code execution vulnerability (CVE-2026-3854) in its git push pipeline within two hours, with no evidence of exploitation. This vulnerability could have allowed attackers with push access to execute arbitrary commands on GitHub's servers, compromising the integrity of the entire platform. The swift response demonstrates GitHub's security maturity and sets a benchmark for incident response. The flaw was introduced by unsanitized push options passed between internal services during a git push operation. A user with push access could craft a push option containing special characters to achieve command injection.

rss · GitHub Blog · Apr 28, 15:30

**Background**: When a user runs git push, the request traverses multiple internal GitHub services, passing metadata such as repository type and environment. Push options are user-controlled parameters that can influence server behavior. If not properly sanitized, these options can lead to command injection on the server. This vulnerability was discovered by security researchers at Wiz using AI-assisted binary analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/security/securing-the-git-push-pipeline-responding-to-a-critical-remote-code-execution-vulnerability/">Securing the git push pipeline: Responding to a critical remote code execution vulnerability - The GitHub Blog</a></li>
<li><a href="https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854">GitHub RCE Vulnerability: CVE-2026-3854 Breakdown | Wiz Blog</a></li>
<li><a href="https://socradar.io/blog/cve-2026-3854-githubs-git-push-pipeline/">CVE-2026-3854 Exposes a Critical Weak Point in GitHub’s Git Push Pipeline</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#git`, `#github`, `#devops`

---

<a id="item-13"></a>
## [Zed Editor Reaches 1.0 Milestone](https://zed.dev/blog/zed-1-0) ⭐️ 7.0/10

Zed, a high-performance code editor, has officially released version 1.0, marking its first stable release. This milestone emphasizes speed and a rich set of features, including multi-language support and a unified interface. This release is significant for developers seeking a fast, modern alternative to existing editors like VS Code and Sublime. Zed's 1.0 marks its readiness for production use, potentially shifting the developer tool landscape. Despite the 1.0 release, community feedback highlights a controversial search UI that opens a new tab, unlike the inline search in Vim or JetBrains tools. Additionally, Zed's language handling for legacy PHP code shows excessive warnings, frustrating some users.

hackernews · salkahfi · Apr 29, 14:34

**Background**: Zed is an open-source code editor written in Rust, known for its exceptional performance and low resource usage. It supports Linux, macOS, and Windows, and offers features like multiplayer editing and AI integration. The 1.0 release follows years of development and beta testing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zed_(text_editor)">Zed (text editor ) - Wikipedia</a></li>
<li><a href="https://zed.dev/?ref=saaspo.com">Zed — Love your editor again</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: many praise Zed's speed and responsiveness, especially on tablets, but criticisms focus on the search UI and excessive warnings for legacy code. Some users prefer Sublime or Helix due to these issues.

**Tags**: `#editor`, `#release`, `#performance`, `#developer-tools`

---

<a id="item-14"></a>
## [Tangled proposes a federation of forges](https://blog.tangled.org/federation/) ⭐️ 7.0/10

Tangled published a blog post proposing a federated forge system to decentralize code hosting, aiming to reduce reliance on centralized platforms like GitHub. This proposal could reduce vendor lock-in, improve resilience of the open-source ecosystem, and foster competition in code hosting services. The proposal is at an early stage and faces criticisms regarding VC funding and the cold-start problem. It builds on existing federation protocols like ForgeFed, which is based on ActivityPub.

hackernews · icy · Apr 29, 14:00

**Background**: A forge is a web-based collaboration platform for software development, hosting repositories, issue trackers, and more. Federation allows different forges to interoperate, similar to how email servers exchange messages. ForgeFed is an ActivityPub-based protocol specifically designed for forge federation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forge_(software)">Forge (software) - Wikipedia</a></li>
<li><a href="https://forgefed.org/">ForgeFed</a></li>

</ul>
</details>

**Discussion**: Comments are mixed: some support the idea of competition but express concerns about VC influence and the cold-start problem. Dan Abramov shared a link explaining the AT Protocol data model for context.

**Tags**: `#decentralized`, `#federation`, `#code hosting`, `#open source`, `#forges`

---

<a id="item-15"></a>
## [HashiCorp co-founder says GitHub 'no longer a place for serious work'](https://www.theregister.com/2026/04/29/mitchell_hashimoto_ghostty_quitting_github/) ⭐️ 7.0/10

Mitchell Hashimoto, co-founder of HashiCorp, publicly criticized GitHub, stating the platform is no longer suitable for serious work, sparking community debate. As a prominent figure in the developer tools industry, Hashimoto's criticism highlights growing concerns about GitHub's reliability and could influence tooling choices across the developer ecosystem. The statement was made in an article on The Register, generating over 900 comments on Hacker News, reflecting widespread discontent among developers.

hackernews · terminalbraid · Apr 29, 11:42

**Background**: Mitchell Hashimoto is the co-founder of HashiCorp, the company behind popular DevOps tools like Terraform and Vault. GitHub, owned by Microsoft, is the largest code hosting platform used by millions of developers. Hashimoto's criticism taps into ongoing frustrations about GitHub's stability and feature direction.

**Discussion**: Community comments largely agreed with Hashimoto, expressing frustration with GitHub's declining stability. Some users noted similar issues on GitLab, while others pointed to ongoing API problems and concerns about Microsoft's stewardship of the platform.

**Tags**: `#GitHub`, `#HashiCorp`, `#developer tools`, `#platform criticism`, `#reliability`

---

<a id="item-16"></a>
## [Rip.so: A Graveyard for Dead Internet Phenomena](https://rip.so/) ⭐️ 7.0/10

Rip.so is a new website that catalogs dead internet phenomena, such as defunct messengers, social networks, and gadgets, presenting them with eulogies and a nostalgic old-web aesthetic. This project serves as a digital memorial documenting internet cultural history, sparking community debate about what it means for something to be 'dead' in the fast-moving online world. The site includes items like Tamagotchi, which some commenters argue is still popular, not dead. Users also questioned whether the text and eulogies are AI-generated, and suggested adding status tags like 'shut down' or 'zombie' to clarify lifespans.

hackernews · bozdemir · Apr 29, 09:21

**Background**: The dead internet theory posits that since the mid-2010s, most online content and interactions are driven by bots and AI rather than humans. Rip.so counteracts this by memorializing the human-made artifacts of the early internet, providing a nostalgic archive of what has been lost.

<details><summary>References</summary>
<ul>
<li><a href="https://www.msn.com/en-us/news/technology/ripso-the-graveyard-of-dead-internet-things/ar-AA220aJa">Rip.so, the graveyard of dead internet things - MSN</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dead_Internet_theory">Dead Internet theory</a></li>

</ul>
</details>

**Discussion**: Commenters praised the concept but suggested improvements: adding a status classification (e.g., shut down, zombie, niche) to differentiate 'dead' from 'declined'. Others noted missing local phenomena (e.g., French services) and suspected AI-generated content, calling for transparency.

**Tags**: `#internet culture`, `#nostalgia`, `#web history`, `#community project`

---

<a id="item-17"></a>
## [AI carb counting experiment reveals extreme inconsistency](https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/) ⭐️ 7.0/10

An experiment ran a large language model (LLM) 27,000 times to count the carbohydrates in the same meal, and the model never produced the same result twice, even at the lowest randomness setting. This highlights the critical unreliability of LLMs for precise numerical tasks, especially in health applications like diabetes management where accuracy is vital. It serves as a cautionary tale against using LLMs for calculations without proper validation. The experiment used 27,000 queries at the lowest randomness setting, yet the variance remained high. The author notes that AI carb counting apps are appearing in app stores, making this demonstration especially timely.

hackernews · sarusso · Apr 29, 12:38

**Background**: Large language models (LLMs) are AI models trained on vast text data to generate human-like text. They are probabilistic and can produce different outputs for the same input, a phenomenon known as hallucination. For tasks requiring precise numerical computation, LLMs are inherently unreliable unless combined with external tools or deterministic methods.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models">LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most...</a></li>

</ul>
</details>

**Discussion**: Community comments largely agree that the experiment effectively demonstrates LLM limitations for numerical tasks. Some point out that the task is inherently impossible due to insufficient visual information, while others note that the post serves as a valuable warning. A few criticize the lack of using proper calculation services, but most concur that LLMs should not be trusted for precise carb counting.

**Tags**: `#LLM`, `#AI reliability`, `#health`, `#carb counting`

---

<a id="item-18"></a>
## [IBM Granite 4.1: Dense LLMs with Long-Context and RL](https://huggingface.co/blog/ibm-granite/granite-4-1) ⭐️ 7.0/10

IBM released Granite 4.1, a family of dense decoder-only LLMs (3B, 8B, 30B) trained on ~15 trillion tokens using a five-phase pre-training pipeline, with long-context extension up to 512K tokens and a four-stage RL pipeline using on-policy GRPO with DAPO loss. This release demonstrates IBM's commitment to efficient, scalable LLMs tailored for enterprise AI, with the 8B instruct model matching or surpassing the previous Granite 3.0 model's performance, potentially enabling more cost-effective deployments. Granite 4.1 models are dense decoder-only architectures, unlike the hybrid Mamba/transformer design of Granite 4.0, and after SFT on ~4.1M LLM-as-Judge-curated samples, they undergo a four-stage RL pipeline including on-policy GRPO with DAPO loss.

rss · Hugging Face Blog · Apr 29, 15:01

**Background**: IBM Granite is a family of large language models designed for enterprise use, with previous versions including Granite 3.0 and Granite 4.0. Granite 4.0 introduced a hybrid Mamba/transformer architecture for improved speed and efficiency. Granite 4.1 shifts to a dense decoder-only design while maintaining strong performance and adding long-context support up to 512K tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/ibm-granite/granite-4-1">Granite 4.1 LLMs: How They’re Built - Hugging Face</a></li>
<li><a href="https://app.daily.dev/posts/granite-4-1-llms-how-they-re-built-luubflwrn">Granite 4.1 LLMs: How They’re Built | daily.dev</a></li>
<li><a href="https://www.ibm.com/new/announcements/ibm-granite-4-0-hyper-efficient-high-performance-hybrid-models">IBM Granite 4.0: hyper-efficient, high performance hybrid ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#IBM`, `#Hugging Face`, `#model building`, `#AI`

---

<a id="item-19"></a>
## [NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal AI](https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence) ⭐️ 7.0/10

NVIDIA has released Nemotron 3 Nano Omni, an open multimodal model that unifies video, audio, image, and text understanding in a single system for AI agents. This model simplifies multimodal AI pipelines by handling documents, audio, and video in one model, enabling more efficient and accurate agents for complex tasks like long-form video analysis and multi-hour meetings. The model uses a hybrid Mamba-Transformer-MoE backbone with 30B active parameters out of 3B total, supports a 256K-token context window, and is fully open on Hugging Face.

rss · Hugging Face Blog · Apr 28, 15:58

**Background**: Multimodal AI models traditionally require separate systems for different data types, often losing context during cross-modal reasoning. Nemotron 3 Nano Omni is part of NVIDIA's Nemotron 3 family, which supports up to 1M tokens context length and uses multi-environment reinforcement learning post-training.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/">NVIDIA Launches Nemotron 3 Nano Omni Model... | NVIDIA Blog</a></li>
<li><a href="https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/">NVIDIA Nemotron 3 Nano Omni Powers Multimodal Agent Reasoning...</a></li>
<li><a href="https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence">Introducing NVIDIA Nemotron 3 Nano Omni: Long - Context ...</a></li>

</ul>
</details>

**Tags**: `#multimodal`, `#NVIDIA`, `#long-context`, `#AI research`, `#huggingface`

---

<a id="item-20"></a>
## [HardenedBSD Moves to Radicle, a Decentralized Git Platform](https://hardenedbsd.org/article/shawn-webb/2026-04-26/hardenedbsd-officially-radicle) ⭐️ 6.0/10

HardenedBSD has officially migrated its code collaboration to Radicle, a peer-to-peer Git forge, as announced on April 26, 2026. This move underscores a growing trend of projects abandoning centralized platforms like GitHub for decentralized alternatives, enhancing censorship resistance and user control. Radicle is built on Git and replicates repositories across peers without a central server; HardenedBSD's migration includes moving from its previous forge to Radicle.

hackernews · lftherios · Apr 29, 06:38

**Background**: HardenedBSD is a hardened version of FreeBSD focusing on security enhancements. Radicle is an open-source, peer-to-peer code collaboration stack that aims to provide decentralized Git hosting, similar to GitHub but without centralized control.

<details><summary>References</summary>
<ul>
<li><a href="https://ariusai.com/products/radicle/">Radicle – Peer-to-Peer Code Collaboration</a></li>

</ul>
</details>

**Discussion**: Commenters expressed curiosity about Radicle's advantages over other decentralized protocols like ATProto, and noted the challenge of discoverability on decentralized networks. Some compared Radicle to Fossil, another decentralized version control system.

**Tags**: `#HardenedBSD`, `#Radicle`, `#decentralized`, `#peer-to-peer`, `#Git`

---