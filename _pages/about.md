---
permalink: /
title: "Qian Dong 董骞"
excerpt: "Qian Dong — model architecture researcher working at the intersection of algorithms and infrastructure."
author_profile: false
layout: bare
header: false
sidebar: false
masthead: false
redirect_from:
  - /about/
  - /about.html
---

{::nomarkdown}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="Qian Dong">
  <meta name="description" content="Qian Dong — model architecture researcher working on scalable architectures, efficient attention, and algorithm–infrastructure co-design.">
  <meta name="theme-color" content="#080b12">
  <title>Qian Dong — Model Architecture</title>
  <link rel="icon" href="{{ '/images/icon.png' | relative_url }}" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{{ '/assets/css/home.css' | relative_url }}">
</head>
<body>
  <a class="t-skip" href="#main-content">Skip to content</a>

  <header class="t-nav">
    <nav class="t-nav__inner" aria-label="Primary navigation">
      <a class="t-brand" href="{{ '/' | relative_url }}">qian.dong / arch</a>
      <div class="t-nav__links">
        <a href="#architecture">architecture</a>
        <a href="#research">research</a>
        <a href="#publications">publications</a>
        <a href="#news">news</a>
        <a href="#education">education</a>
        <a class="t-utility" href="{{ '/submit/' | relative_url }}">submit</a>
        <a class="t-utility" href="{{ '/dm/' | relative_url }}">dm</a>
        <a class="t-lang" href="{{ '/zh/' | relative_url }}">中文</a>
      </div>
    </nav>
  </header>

  <main class="t-main" id="main-content">
    <header class="t-hero">
      <p class="t-hero__path">~/model-architecture/qian-dong<span> $</span></p>
      <div class="t-hero__grid">
        <div class="t-hero__copy">
          <p class="t-hero__eyebrow"><span>model architecture</span> algo × infra</p>
          <h1 class="t-hero__name">Qian Dong <span>董骞</span></h1>
          <p class="t-hero__line">
            <span class="t-prompt">&gt;</span><span class="t-hero__role">Model Architecture Researcher</span>
          </p>
          <p class="t-hero__bio">
            Ph.D. in Computer Science and Technology from Tsinghua University
            (<a href="https://ai.thuir.cn/">THUIR</a>). I design
            <strong>model architectures that scale parameters, context, and intelligence</strong>
            by co-designing algorithms with the infrastructure that makes them efficient.
          </p>
          <nav class="t-hero__links" aria-label="Profile links">
            <a class="t-link" href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&amp;hl=en">scholar</a>
            <a class="t-link" href="https://github.com/CSQianDong">github</a>
            <a class="t-link" href="mailto:qiandong.97@qq.com">email</a>
            <a class="t-link" href="https://www.linkedin.com/in/qian-dong-58b14a23a/">linkedin</a>
            <a class="t-link" href="https://x.com/verymakesense">x</a>
          </nav>
        </div>

        <figure class="arch-map">
          <figcaption class="arch-map__head"><span>architecture_map / v1</span><span>active</span></figcaption>
          <svg viewBox="0 0 420 280" role="img" aria-labelledby="arch-map-title">
            <title id="arch-map-title">Model architecture connecting algorithms, infrastructure, parameters, context, and intelligence</title>
            <defs>
              <pattern id="arch-grid" width="18" height="18" patternUnits="userSpaceOnUse">
                <path d="M18 0H0V18" fill="none" stroke="currentColor" stroke-width="0.5" opacity="0.16"></path>
              </pattern>
            </defs>
            <rect class="arch-map__grid" width="420" height="280" rx="12" fill="url(#arch-grid)"></rect>
            <g aria-hidden="true">
              <line class="arch-map__edge arch-map__edge--accent" x1="210" y1="140" x2="74" y2="48"></line>
              <line class="arch-map__edge arch-map__edge--accent" x1="210" y1="140" x2="346" y2="48"></line>
              <line class="arch-map__edge" x1="210" y1="140" x2="70" y2="234"></line>
              <line class="arch-map__edge" x1="210" y1="140" x2="210" y2="240"></line>
              <line class="arch-map__edge" x1="210" y1="140" x2="350" y2="234"></line>
            </g>
            <rect class="arch-map__halo" x="124" y="97" width="172" height="86" rx="16"></rect>
            <g class="arch-map__node arch-map__node--algo" transform="translate(16 28)">
              <rect width="116" height="40" rx="8"></rect>
              <text x="58" y="25">ALGORITHM</text>
            </g>
            <g class="arch-map__node arch-map__node--infra" transform="translate(288 28)">
              <rect width="116" height="40" rx="8"></rect>
              <text x="58" y="25">INFRASTRUCTURE</text>
            </g>
            <g class="arch-map__node arch-map__node--core" transform="translate(130 103)">
              <rect width="160" height="74" rx="13"></rect>
              <text x="80" y="31">MODEL</text>
              <text x="80" y="49">ARCHITECTURE</text>
            </g>
            <g class="arch-map__node" transform="translate(12 214)">
              <rect width="116" height="40" rx="8"></rect>
              <text x="58" y="25">PARAMETERS</text>
            </g>
            <g class="arch-map__node" transform="translate(152 220)">
              <rect width="116" height="40" rx="8"></rect>
              <text x="58" y="25">CONTEXT</text>
            </g>
            <g class="arch-map__node" transform="translate(292 214)">
              <rect width="116" height="40" rx="8"></rect>
              <text x="58" y="25">INTELLIGENCE</text>
            </g>
          </svg>
          <div class="arch-map__legend"><span>parameters ↑</span><span>context ↑</span><span>intelligence ↑</span></div>
        </figure>
      </div>
    </header>

    <section class="t-section reveal" id="about">
      <h2 class="t-h2"><span class="t-h2__idx">// 01</span> about</h2>
      <div class="t-prose">
        <p>
          I received my Ph.D. in Computer Science and Technology from
          <a href="https://www.tsinghua.edu.cn/">Tsinghua University</a> in June 2026,
          where I was a member of <a href="https://ai.thuir.cn/">THUIR</a>. I was
          fortunate to be advised by Prof.
          <a href="http://www.thuir.cn/group/msp/">Shaoping Ma</a>, Prof.
          <a href="http://www.thuir.cn/group/YQLiu/">Yiqun Liu</a>, and Prof.
          <a href="http://www.thuir.cn/group/aiqy/">Qingyao Ai</a>. My research
          focuses on efficient, scalable model architectures and the systems that
          make them practical.
        </p>
      </div>
    </section>

    <section class="t-section reveal" id="architecture">
      <h2 class="t-h2"><span class="t-h2__idx">// 02</span> architecture work</h2>
      <p class="t-section__lead">Selected work where architecture decisions meet real systems constraints.</p>
      <div class="arch-work">
        <a class="arch-work__item" href="https://www.arxiv.org/abs/2602.15763">
          <span class="arch-work__meta">foundation model · 2026</span>
          <h3>GLM-5 Architecture</h3>
          <p>Core contributor to the model architecture behind GLM-5.</p>
          <span class="arch-work__link">technical report ↗</span>
        </a>
        <a class="arch-work__item" href="https://arxiv.org/abs/2603.12201">
          <span class="arch-work__meta">efficient attention · 2026</span>
          <h3>IndexCache</h3>
          <p>Reuse sparse-attention indices across layers to reduce indexing overhead.</p>
          <span class="arch-work__link">paper ↗</span>
        </a>
        <article class="arch-work__item">
          <span class="arch-work__meta">cross-attention · 2025</span>
          <h3>DecoupledRAG</h3>
          <p>Decouple context encoding and knowledge access through a cross-attention architecture.</p>
          <span class="arch-work__link">WWW 2025</span>
        </article>
      </div>
    </section>

    <section class="t-section reveal" id="research">
      <h2 class="t-h2"><span class="t-h2__idx">// 03</span> research directions</h2>
      <div class="t-grid">
        <article class="t-card">
          <span class="t-card__no">01</span>
          <svg class="t-card__diagram" viewBox="0 0 104 52" aria-hidden="true">
            <rect class="diagram-dim" x="1" y="14" width="20" height="24" rx="3"></rect>
            <path class="diagram-line" d="M21 26h18"></path>
            <rect class="diagram-fill" x="39" y="8" width="26" height="36" rx="4"></rect>
            <circle class="diagram-line" cx="52" cy="26" r="4"></circle>
            <path class="diagram-line" d="M65 26h18"></path>
            <rect class="diagram-dim" x="83" y="14" width="20" height="24" rx="3"></rect>
          </svg>
          <h3 class="t-card__title">Model Architecture</h3>
          <p class="t-card__desc">Co-designing algorithms and infrastructure for capable models that remain efficient at scale.</p>
        </article>
        <article class="t-card">
          <span class="t-card__no">02</span>
          <svg class="t-card__diagram" viewBox="0 0 104 52" aria-hidden="true">
            <g class="diagram-dim">
              <rect x="2" y="2" width="12" height="12" rx="2"></rect><rect x="18" y="2" width="12" height="12" rx="2"></rect><rect x="34" y="2" width="12" height="12" rx="2"></rect>
              <rect x="2" y="18" width="12" height="12" rx="2"></rect><rect x="18" y="18" width="12" height="12" rx="2"></rect><rect x="34" y="18" width="12" height="12" rx="2"></rect>
              <rect x="2" y="34" width="12" height="12" rx="2"></rect><rect x="18" y="34" width="12" height="12" rx="2"></rect><rect x="34" y="34" width="12" height="12" rx="2"></rect>
            </g>
            <rect class="diagram-fill" x="2" y="2" width="12" height="12" rx="2"></rect>
            <rect class="diagram-fill" x="18" y="18" width="12" height="12" rx="2"></rect>
            <rect class="diagram-fill" x="34" y="34" width="12" height="12" rx="2"></rect>
            <path class="diagram-line" d="M54 26h18m0 0-5-5m5 5-5 5"></path>
            <rect class="diagram-fill" x="78" y="14" width="24" height="24" rx="4"></rect>
          </svg>
          <h3 class="t-card__title">Efficient Attention</h3>
          <p class="t-card__desc">Sparse attention, index reuse, and architecture-level techniques for reducing inference cost.</p>
        </article>
        <article class="t-card">
          <span class="t-card__no">03</span>
          <svg class="t-card__diagram" viewBox="0 0 104 52" aria-hidden="true">
            <path class="diagram-dim" d="M2 8h34M2 20h48M2 32h62M2 44h76"></path>
            <path class="diagram-line" d="M36 8 78 26M50 20l28 6M64 32l14-6M78 44V26"></path>
            <rect class="diagram-fill" x="78" y="13" width="24" height="26" rx="4"></rect>
          </svg>
          <h3 class="t-card__title">Scalable Context</h3>
          <p class="t-card__desc">Extending useful context while balancing model quality, memory, throughput, and latency.</p>
        </article>
        <article class="t-card">
          <span class="t-card__no">04</span>
          <svg class="t-card__diagram" viewBox="0 0 104 52" aria-hidden="true">
            <circle class="diagram-fill" cx="10" cy="26" r="8"></circle>
            <path class="diagram-line" d="M18 26h18"></path>
            <rect class="diagram-fill" x="36" y="12" width="30" height="28" rx="4"></rect>
            <path class="diagram-line" d="M66 19h16M66 33h16"></path>
            <rect class="diagram-dim" x="82" y="10" width="20" height="14" rx="3"></rect>
            <rect class="diagram-dim" x="82" y="28" width="20" height="14" rx="3"></rect>
          </svg>
          <h3 class="t-card__title">Information Retrieval</h3>
          <p class="t-card__desc">Ranking and retrieval-augmented generation that connect models with the right information.</p>
        </article>
      </div>
    </section>

    <section class="t-section reveal" id="news">
      <h2 class="t-h2"><span class="t-h2__idx">// 04</span> news</h2>
      <ul class="t-news">
        <li><span class="t-news__date">2026.06</span><p>I received my <strong>Ph.D. in Computer Science and Technology</strong> from Tsinghua University.</p></li>
        <li><span class="t-news__date">2026.03</span><p><a href="https://arxiv.org/abs/2603.12201"><strong>IndexCache</strong></a> was released, accelerating sparse attention via cross-layer index reuse.</p></li>
        <li><span class="t-news__date">2026.02</span><p>The <a href="https://www.arxiv.org/abs/2602.15763">GLM-5 Technical Report</a> was released. I am one of the core contributors to model architecture.</p></li>
        <li><span class="t-news__date">2025.12</span><p><strong>GLM-4.7</strong> was released. See our <a href="https://z.ai/blog/glm-4.7">blog</a> for details.</p></li>
        <li><span class="t-news__date">2025.11</span><p><strong>SelfRACG</strong> was accepted to EMNLP 2025, enabling LLMs to self-express retrieval queries for better code generation.</p></li>
        <li><span class="t-news__date">2025.09</span><p><strong>GLM-4.6</strong> was released. See our <a href="https://z.ai/blog/glm-4.6">blog</a> for details.</p></li>
        <li><span class="t-news__date">2025.08</span><p>The <a href="https://arxiv.org/abs/2508.06471">GLM-4.5 Technical Report</a> was released. I contributed to sparse-attention adaptation during post-training.</p></li>
        <li><span class="t-news__date">2025.07</span><p><strong>Qilin</strong> was accepted to SIGIR 2025, introducing a multimodal IR dataset with app-level user sessions.</p></li>
        <li><span class="t-news__date">2025.04</span><p><strong>DecoupledRAG</strong> was accepted to WWW 2025, decoupling context and knowledge via cross-attention for efficient RAG.</p></li>
      </ul>
      <details class="t-news-archive">
        <summary>earlier updates · 2021–2024</summary>
        <ul class="t-news">
        <li><span class="t-news__date">2024.07</span><p><strong>RLCF</strong> was accepted to SIGIR 2024, aligning LLMs for information retrieval through unsupervised contrastive feedback.</p></li>
        <li><span class="t-news__date">2023.10</span><p><strong>I³Retriever</strong> was accepted to CIKM 2023, incorporating implicit query-document interaction into retrievers.</p></li>
        <li><span class="t-news__date">2023.07</span><p><strong>T²Ranking</strong> was accepted to SIGIR 2023 as a large-scale Chinese passage-ranking benchmark.</p></li>
        <li><span class="t-news__date">2022.07</span><p><strong>KERM</strong> was accepted to SIGIR 2022, incorporating explicit knowledge into pre-trained models for passage re-ranking.</p></li>
        <li><span class="t-news__date">2022.02</span><p><strong>DGRe</strong> was published in Data Science and Engineering.</p></li>
        <li><span class="t-news__date">2021.07</span><p><strong>R-FORMER</strong> was accepted to SIGIR 2021.</p></li>
        <li><span class="t-news__date">2021.04</span><p><strong>LGRe</strong> was accepted to DASFAA 2021.</p></li>
        </ul>
      </details>
    </section>

    <section class="t-section reveal" id="publications">
      <h2 class="t-h2"><span class="t-h2__idx">// 05</span> publications</h2>
      <div class="t-callout">
        <div class="t-callout__text">
          <h3>Full publication list on Google Scholar</h3>
          <p>Peer-reviewed work across model architecture, retrieval, RAG, and language models.</p>
        </div>
        <a class="t-btn" href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&amp;hl=en">→ google scholar</a>
      </div>

      <div class="t-pub-groups">
        <details class="t-pub-group">
          <summary>selected papers · primary author (10)</summary>
          <ul class="t-pub-list">
            <li class="t-pub">
              <h3 class="t-pub__title">SelfRACG: Enabling LLMs to Self-Express and Retrieve for Code Generation</h3>
              <p class="t-pub__authors"><strong>Qian Dong</strong>, Jia Chen, Qingyao Ai, Hongning Wang, Haitao Li, Yi Wu, Yao Hu, Yiqun Liu, Shaoping Ma</p>
              <p class="t-pub__meta"><span>EMNLP 2025</span><span class="t-badge">TH-CPL-A</span><span class="t-badge">CCF-B</span><a href="https://www.arxiv.org/abs/2507.19033">paper ↗</a></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">Qilin: A Multimodal Information Retrieval Dataset with APP-level User Sessions</h3>
              <p class="t-pub__authors">Jia Chen*, <strong>Qian Dong</strong>*, Haitao Li, Xiaohui He, Yan Gao, Shaosheng Cao, Yi Wu, Ping Yang, Chen Xu, Yao Hu, Qingyao Ai, Yiqun Liu (* equal contribution)</p>
              <p class="t-pub__meta"><span>SIGIR 2025</span><span class="t-badge">TH-CPL-A</span><span class="t-badge">CCF-A</span></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">DecoupledRAG: An Efficient and Effective Retrieval Augmented Generation Framework via Cross Attention</h3>
              <p class="t-pub__authors"><strong>Qian Dong</strong>, Qingyao Ai, Hongning Wang, Yiding Liu, Haitao Li, Weihang Su, Yiqun Liu, Tat-Seng Chua, Shaoping Ma</p>
              <p class="t-pub__meta"><span>WWW 2025</span><span class="t-badge">TH-CPL-A</span><span class="t-badge">CCF-A</span></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">Unsupervised Large Language Model Alignment for Information Retrieval via Contrastive Feedback</h3>
              <p class="t-pub__authors"><strong>Qian Dong</strong>, Yiding Liu, Qingyao Ai, Zhijing Wu, Haitao Li, Yiqun Liu, Shuaiqiang Wang, Dawei Yin, Shaoping Ma</p>
              <p class="t-pub__meta"><span>SIGIR 2024</span><span class="t-badge">TH-CPL-A</span><span class="t-badge">CCF-A</span><a href="https://doi.org/gss8w3">paper ↗</a></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">T²Ranking: A Large-scale Chinese Benchmark for Passage Ranking</h3>
              <p class="t-pub__authors">Xiaohui Xie, <strong>Qian Dong</strong>* (student first author), Bingning Wang, Feiyang Lv, Ting Yao, Weinan Gan, Zhijing Wu, Xiangsheng Li, Haitao Li, Yiqun Liu, Jin Ma</p>
              <p class="t-pub__meta"><span>SIGIR 2023</span><span class="t-badge">TH-CPL-A</span><span class="t-badge">CCF-A</span><a href="https://doi.org/gsjb5w">paper ↗</a></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">I³Retriever: Incorporating Implicit Interaction in Pre-trained Language Models for Passage Retrieval</h3>
              <p class="t-pub__authors"><strong>Qian Dong</strong>, Yiding Liu, Qingyao Ai, Haitao Li, Shuaiqiang Wang, Yiqun Liu, Dawei Yin, Shaoping Ma</p>
              <p class="t-pub__meta"><span>CIKM 2023</span><span class="t-badge">TH-CPL-B</span><span class="t-badge">CCF-B</span><a href="https://doi.org/gs2pcc">paper ↗</a></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">Incorporating Explicit Knowledge in Pre-trained Language Models for Passage Re-ranking</h3>
              <p class="t-pub__authors"><strong>Qian Dong</strong>, Yiding Liu, Suqi Cheng, Shuaiqiang Wang, Zhicong Cheng, Shuzi Niu, Dawei Yin</p>
              <p class="t-pub__meta"><span>SIGIR 2022</span><span class="t-badge">TH-CPL-A</span><span class="t-badge">CCF-A</span><a href="https://doi.org/gsh8px">paper ↗</a></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">Disentangled Graph Recurrent Network for Document Ranking</h3>
              <p class="t-pub__authors"><strong>Qian Dong</strong>, Shuzi Niu, Tao Yuan, Yucheng Li</p>
              <p class="t-pub__meta"><span>Data Science and Engineering</span><span class="t-badge">JCR-Q1</span><a href="https://doi.org/gsh8pw">paper ↗</a></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">Legal Judgment Prediction via Relational Learning</h3>
              <p class="t-pub__authors"><strong>Qian Dong</strong>, Shuzi Niu</p>
              <p class="t-pub__meta"><span>SIGIR 2021</span><span class="t-badge">TH-CPL-A</span><span class="t-badge">CCF-A</span><a href="https://doi.org/gq4w8t">paper ↗</a></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">Latent Graph Recurrent Network for Document Ranking</h3>
              <p class="t-pub__authors"><strong>Qian Dong</strong>, Shuzi Niu</p>
              <p class="t-pub__meta"><span>DASFAA 2021</span><span class="t-badge">TH-CPL-B</span><span class="t-badge">CCF-B</span><a href="https://doi.org/gsh8ps">paper ↗</a></p>
            </li>
          </ul>
        </details>

        <details class="t-pub-group">
          <summary>selected papers · co-author (9)</summary>
          <ul class="t-pub-list">
            <li class="t-pub">
              <h3 class="t-pub__title">IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse</h3>
              <p class="t-pub__authors">Yushi Bai, <strong>Qian Dong</strong>, Ting Jiang, Xin Lv, Zhengxiao Du, Aohan Zeng, Jie Tang, Juanzi Li</p>
              <p class="t-pub__meta"><span>arXiv 2026</span><a href="https://arxiv.org/abs/2603.12201">paper ↗</a></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges</h3>
              <p class="t-pub__authors">Haitao Li, Junjie Chen, Qingyao Ai, Zhumin Chu, Yujia Zhou, <strong>Qian Dong</strong>, Yiqun Liu</p>
              <p class="t-pub__meta"><span>ACL 2025</span><span class="t-badge">CCF-A</span></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods</h3>
              <p class="t-pub__authors">Haitao Li, <strong>Qian Dong</strong>, Junjie Chen, Huixue Su, Yujia Zhou, Qingyao Ai, Ziyi Ye, Yiqun Liu</p>
              <p class="t-pub__meta"><span>under review</span></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">DELTA: Pre-train a Discriminative Encoder for Legal Case Retrieval via Structural Word Alignment</h3>
              <p class="t-pub__authors">Haitao Li, Qingyao Ai, Xinyan Han, Jia Chen, <strong>Qian Dong</strong>, Yiqun Liu, Chong Chen, Qi Tian</p>
              <p class="t-pub__meta"><span>AAAI 2025</span><span class="t-badge">CCF-A</span></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">BLADE: Enhancing Black-box Large Language Models with Small Domain-Specific Models</h3>
              <p class="t-pub__authors">Haitao Li, Qingyao Ai, Jia Chen, <strong>Qian Dong</strong>, Zhijing Wu, Yiqun Liu, Chong Chen, Qi Tian</p>
              <p class="t-pub__meta"><span>AAAI 2025</span><span class="t-badge">CCF-A</span></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">SAILER: Structure-aware Pre-trained Language Model for Legal Case Retrieval</h3>
              <p class="t-pub__authors">Haitao Li, Qingyao Ai, Jia Chen, <strong>Qian Dong</strong>, Yueyue Wu, Yiqun Liu, Chong Chen, Qi Tian</p>
              <p class="t-pub__meta"><span>SIGIR 2023</span><span class="t-badge">CCF-A</span><a href="https://doi.org/gsjb5x">paper ↗</a></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">Layout-aware Webpage Quality Assessment</h3>
              <p class="t-pub__authors">Anfeng Cheng, Yiding Liu, Weibin Li, <strong>Qian Dong</strong>, Shuaiqiang Wang, Zhengjie Huang, Shikun Feng, Zhicong Cheng, Dawei Yin</p>
              <p class="t-pub__meta"><span>arXiv 2023</span><a href="https://doi.org/gsh8pz">paper ↗</a></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">Incorporating Social-Aware User Preference for Video Recommendation</h3>
              <p class="t-pub__authors">Xuanji Xiao, Huaqiang Dai, <strong>Qian Dong</strong>, Shuzi Niu, Yuzhen Liu, Pei Liu</p>
              <p class="t-pub__meta"><span>WISE 2023</span><span class="t-badge">CCF-C</span><a href="https://doi.org/gs2pcb">paper ↗</a></p>
            </li>
            <li class="t-pub">
              <h3 class="t-pub__title">Emotion Recognition Based on Multi-View Body Gestures</h3>
              <p class="t-pub__authors">Zhijuan Shen, Jun Cheng, Xiping Hu, <strong>Qian Dong</strong></p>
              <p class="t-pub__meta"><span>ICIP 2019</span><span class="t-badge">CCF-C</span><a href="https://doi.org/ghjxdq">paper ↗</a></p>
            </li>
          </ul>
        </details>
      </div>
    </section>

    <section class="t-section reveal" id="education">
      <h2 class="t-h2"><span class="t-h2__idx">// 06</span> education</h2>
      <ul class="t-log">
        <li class="t-log__item">
          <span class="t-log__date">2022 — 2026</span>
          <div>
            <span class="t-log__org">Tsinghua University</span>
            <span class="t-log__role">Ph.D.</span>
            <p>Computer Science and Technology · THUIR</p>
          </div>
        </li>
        <li class="t-log__item">
          <span class="t-log__date">2019 — 2022</span>
          <div>
            <span class="t-log__org">Chinese Academy of Sciences</span>
            <span class="t-log__role">M.Eng.</span>
            <p>Institute of Software</p>
          </div>
        </li>
        <li class="t-log__item">
          <span class="t-log__date">2015 — 2019</span>
          <div>
            <span class="t-log__org">South China University of Technology <span class="t-dim">SCUT</span></span>
            <span class="t-log__role">B.Eng.</span>
            <p>Software Engineering</p>
          </div>
        </li>
      </ul>
    </section>

    <section class="t-section reveal" id="honors">
      <h2 class="t-h2"><span class="t-h2__idx">// 07</span> honors &amp; awards</h2>
      <div class="t-tags">
        <span class="t-tag t-tag--star">National Scholarship · Top 1% · 2021</span>
      </div>
    </section>

    <section class="t-section reveal" id="more">
      <h2 class="t-h2"><span class="t-h2__idx">// 08</span> beyond research</h2>
      <p class="t-note">
        Away from models and systems, I enjoy exploring <strong>craft beer</strong> —
        from crisp wheat beers and hop-forward IPAs to Belgian witbiers and saisons. 🍻
      </p>
      <div class="t-map">
        <script id="clustrmaps" src="https://cdn.clustrmaps.com/map_v2.js?cl=ffffff&amp;w=a&amp;t=n&amp;d=J7QANnH4LJYLoOu_V6HTux3g537xFQCL00jK2z4-6jg"></script>
      </div>
    </section>
  </main>

  <footer class="t-footer">
    <span>© {{ site.time | date: "%Y" }} Qian Dong · </span>
    <span>Last updated {{ site.time | date: "%B %d, %Y" }}</span>
  </footer>

  <script>
    window.difyChatbotConfig = { token: "6CoM85G6spngdgsq" };
  </script>
  <script src="https://udify.app/embed.min.js" id="6CoM85G6spngdgsq" defer></script>
  <script src="{{ '/assets/js/home.js' | relative_url }}" defer></script>
</body>
</html>
{:/nomarkdown}
