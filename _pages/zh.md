---
permalink: /zh/
title: "董骞"
excerpt: "董骞个人主页 — 从事算法与基础设施协同设计的模型架构研究。"
author_profile: false
layout: bare
header: false
sidebar: false
masthead: false
---

{::nomarkdown}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="Qian Dong">
  <meta name="description" content="董骞 — 从事可扩展模型架构、高效注意力，以及算法与基础设施协同设计研究。">
  <meta name="theme-color" content="#080b12">
  <title>董骞 | 模型架构</title>
  <link rel="icon" href="{{ '/images/icon.png' | relative_url }}" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{{ '/assets/css/home.css' | relative_url }}">
</head>
<body>
  <a class="t-skip" href="#main-content">跳到正文</a>

  <header class="t-nav">
    <nav class="t-nav__inner" aria-label="主导航">
      <a class="t-brand" href="{{ '/zh/' | relative_url }}">qian.dong / arch</a>
      <div class="t-nav__links">
        <a href="#architecture">架构工作</a>
        <a href="#research">研究</a>
        <a href="#publications">论文</a>
        <a href="#news">动态</a>
        <a href="#education">教育</a>
        <a class="t-utility" href="{{ '/submit/' | relative_url }}">投稿</a>
        <a class="t-utility" href="{{ '/dm/' | relative_url }}">留言</a>
        <a class="t-lang" href="{{ '/' | relative_url }}">EN</a>
      </div>
    </nav>
  </header>

  <main class="t-main" id="main-content">
    <header class="t-hero">
      <p class="t-hero__path">~/model-architecture/qian-dong<span> $</span></p>
      <div class="t-hero__grid">
        <div class="t-hero__copy">
          <p class="t-hero__eyebrow"><span>模型架构</span> 算法 × 基础设施</p>
          <h1 class="t-hero__name">董骞 <span>Qian Dong</span></h1>
          <p class="t-hero__line">
            <span class="t-prompt">&gt;</span><span class="t-hero__role">模型架构研究</span>
          </p>
          <p class="t-hero__bio">
            清华大学计算机科学与技术博士（<a href="https://ai.thuir.cn/">THUIR</a>）。
            我通过算法与基础设施协同设计，构建
            <strong>扩展参数、上下文与智能的模型架构</strong>。
          </p>
          <nav class="t-hero__links" aria-label="个人链接">
            <a class="t-link" href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&amp;hl=en">学术主页</a>
            <a class="t-link" href="https://github.com/CSQianDong">github</a>
            <a class="t-link" href="mailto:qiandong.97@qq.com">邮箱</a>
            <a class="t-link" href="https://x.com/verymakesense">x</a>
            <a class="t-link" href="https://www.xiaohongshu.com/user/profile/64d8bdc1000000000100f445">小红书</a>
          </nav>
        </div>

        <figure class="arch-map">
          <figcaption class="arch-map__head"><span>architecture_map / v1</span><span>active</span></figcaption>
          <svg viewBox="0 0 420 280" role="img" aria-labelledby="arch-map-title-zh">
            <title id="arch-map-title-zh">模型架构连接算法、基础设施、参数、上下文与智能</title>
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
          <div class="arch-map__legend"><span>参数 ↑</span><span>上下文 ↑</span><span>智能 ↑</span></div>
        </figure>
      </div>
    </header>

    <section class="t-section reveal" id="about">
      <h2 class="t-h2"><span class="t-h2__idx">// 01</span> 关于</h2>
      <div class="t-prose">
        <p>
          我于 2026 年 6 月获得
          <a href="https://www.tsinghua.edu.cn/">清华大学</a>计算机科学与技术博士学位，
          博士期间在<a href="https://ai.thuir.cn/">信息检索实验室（THUIR）</a>开展研究。
          很荣幸得到<a href="http://www.thuir.cn/group/msp/">马少平</a>教授、
          <a href="http://www.thuir.cn/group/YQLiu/">刘奕群</a>教授和
          <a href="http://www.thuir.cn/group/aiqy/">艾清遥</a>教授的指导。
          我的研究关注高效、可扩展的模型架构，以及让这些架构真正落地的系统基础设施。
        </p>
      </div>
    </section>

    <section class="t-section reveal" id="architecture">
      <h2 class="t-h2"><span class="t-h2__idx">// 02</span> 架构工作</h2>
      <p class="t-section__lead">代表性工作：在真实系统约束下做模型架构设计。</p>
      <div class="arch-work">
        <a class="arch-work__item" href="https://www.arxiv.org/abs/2602.15763">
          <span class="arch-work__meta">基础模型 · 2026</span>
          <h3>GLM-5 架构</h3>
          <p>GLM-5 模型架构核心贡献者之一。</p>
          <span class="arch-work__link">技术报告 ↗</span>
        </a>
        <a class="arch-work__item" href="https://arxiv.org/abs/2603.12201">
          <span class="arch-work__meta">高效注意力 · 2026</span>
          <h3>IndexCache</h3>
          <p>跨层复用稀疏注意力索引，降低索引计算开销。</p>
          <span class="arch-work__link">论文 ↗</span>
        </a>
        <article class="arch-work__item">
          <span class="arch-work__meta">交叉注意力 · 2025</span>
          <h3>DecoupledRAG</h3>
          <p>通过交叉注意力架构解耦上下文编码与知识访问。</p>
          <span class="arch-work__link">WWW 2025</span>
        </article>
      </div>
    </section>

    <section class="t-section reveal" id="research">
      <h2 class="t-h2"><span class="t-h2__idx">// 03</span> 研究方向</h2>
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
          <h3 class="t-card__title">模型架构</h3>
          <p class="t-card__desc">协同设计算法与基础设施，让模型能力随规模增长的同时保持高效。</p>
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
          <h3 class="t-card__title">高效注意力</h3>
          <p class="t-card__desc">研究稀疏注意力、索引复用等架构级方法，降低模型推理成本。</p>
        </article>
        <article class="t-card">
          <span class="t-card__no">03</span>
          <svg class="t-card__diagram" viewBox="0 0 104 52" aria-hidden="true">
            <path class="diagram-dim" d="M2 8h34M2 20h48M2 32h62M2 44h76"></path>
            <path class="diagram-line" d="M36 8 78 26M50 20l28 6M64 32l14-6M78 44V26"></path>
            <rect class="diagram-fill" x="78" y="13" width="24" height="26" rx="4"></rect>
          </svg>
          <h3 class="t-card__title">上下文扩展</h3>
          <p class="t-card__desc">在模型质量、显存、吞吐与时延之间取得平衡，扩展有效上下文。</p>
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
          <h3 class="t-card__title">信息检索</h3>
          <p class="t-card__desc">研究排序与检索增强生成，让模型高效连接到正确的信息。</p>
        </article>
      </div>
    </section>

    <section class="t-section reveal" id="news">
      <h2 class="t-h2"><span class="t-h2__idx">// 04</span> 最新动态</h2>
      <ul class="t-news">
        <li><span class="t-news__date">2026.06</span><p>博士毕业，获得清华大学<strong>计算机科学与技术博士学位</strong>。</p></li>
        <li><span class="t-news__date">2026.03</span><p><a href="https://arxiv.org/abs/2603.12201"><strong>IndexCache</strong></a> 发布，通过跨层索引复用加速稀疏注意力。</p></li>
        <li><span class="t-news__date">2026.02</span><p><a href="https://www.arxiv.org/abs/2602.15763">GLM-5 技术报告</a>发布，我是模型架构核心贡献者之一。</p></li>
        <li><span class="t-news__date">2025.12</span><p><strong>GLM-4.7</strong> 发布，详情请见我们的<a href="https://z.ai/blog/glm-4.7">博客</a>。</p></li>
        <li><span class="t-news__date">2025.11</span><p><strong>SelfRACG</strong> 被 EMNLP 2025 接收，让大模型自主表达检索查询以提升代码生成。</p></li>
        <li><span class="t-news__date">2025.09</span><p><strong>GLM-4.6</strong> 发布，详情请见我们的<a href="https://z.ai/blog/glm-4.6">博客</a>。</p></li>
        <li><span class="t-news__date">2025.08</span><p><a href="https://arxiv.org/abs/2508.06471">GLM-4.5 技术报告</a>发布，我参与了后训练阶段的稀疏注意力适配研究。</p></li>
        <li><span class="t-news__date">2025.07</span><p><strong>Qilin</strong> 被 SIGIR 2025 接收，构建了包含真实 App 级用户会话的多模态检索数据集。</p></li>
        <li><span class="t-news__date">2025.04</span><p><strong>DecoupledRAG</strong> 被 WWW 2025 接收，通过交叉注意力解耦上下文与知识。</p></li>
      </ul>
      <details class="t-news-archive">
        <summary>更早动态 · 2021–2024</summary>
        <ul class="t-news">
        <li><span class="t-news__date">2024.07</span><p><strong>RLCF</strong> 被 SIGIR 2024 接收，通过无监督对比反馈对齐信息检索大模型。</p></li>
        <li><span class="t-news__date">2023.10</span><p><strong>I³Retriever</strong> 被 CIKM 2023 接收，将隐式查询—文档交互融入检索器。</p></li>
        <li><span class="t-news__date">2023.07</span><p><strong>T²Ranking</strong> 被 SIGIR 2023 接收，发布大规模中文段落排序基准。</p></li>
        <li><span class="t-news__date">2022.07</span><p><strong>KERM</strong> 被 SIGIR 2022 接收，将显式知识融入预训练模型用于段落重排序。</p></li>
        <li><span class="t-news__date">2022.02</span><p><strong>DGRe</strong> 发表于 Data Science and Engineering。</p></li>
        <li><span class="t-news__date">2021.07</span><p><strong>R-FORMER</strong> 被 SIGIR 2021 接收。</p></li>
        <li><span class="t-news__date">2021.04</span><p><strong>LGRe</strong> 被 DASFAA 2021 接收。</p></li>
        </ul>
      </details>
    </section>

    <section class="t-section reveal" id="publications">
      <h2 class="t-h2"><span class="t-h2__idx">// 05</span> 论文</h2>
      <div class="t-callout">
        <div class="t-callout__text">
          <h3>完整论文列表见 Google Scholar</h3>
          <p>研究工作涵盖模型架构、信息检索、检索增强生成与大语言模型。</p>
        </div>
        <a class="t-btn" href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&amp;hl=en">→ google scholar</a>
      </div>

      <div class="t-pub-groups">
        <details class="t-pub-group">
          <summary>代表性论文 · 主要作者（10）</summary>
          <ul class="t-pub-list">
            <li class="t-pub"><h3 class="t-pub__title">SelfRACG: Enabling LLMs to Self-Express and Retrieve for Code Generation</h3><p class="t-pub__meta"><span>EMNLP 2025</span><span class="t-badge">TH-CPL-A</span><span class="t-badge">CCF-B</span><a href="https://www.arxiv.org/abs/2507.19033">论文 ↗</a></p></li>
            <li class="t-pub"><h3 class="t-pub__title">Qilin: A Multimodal Information Retrieval Dataset with APP-level User Sessions</h3><p class="t-pub__meta"><span>SIGIR 2025</span><span class="t-badge">TH-CPL-A</span><span class="t-badge">CCF-A</span></p></li>
            <li class="t-pub"><h3 class="t-pub__title">DecoupledRAG: An Efficient and Effective Retrieval Augmented Generation Framework via Cross Attention</h3><p class="t-pub__meta"><span>WWW 2025</span><span class="t-badge">TH-CPL-A</span><span class="t-badge">CCF-A</span></p></li>
            <li class="t-pub"><h3 class="t-pub__title">Unsupervised Large Language Model Alignment for Information Retrieval via Contrastive Feedback</h3><p class="t-pub__meta"><span>SIGIR 2024</span><span class="t-badge">CCF-A</span><a href="https://doi.org/gss8w3">论文 ↗</a></p></li>
            <li class="t-pub"><h3 class="t-pub__title">T²Ranking: A Large-scale Chinese Benchmark for Passage Ranking</h3><p class="t-pub__meta"><span>SIGIR 2023</span><span class="t-badge">CCF-A</span><a href="https://doi.org/gsjb5w">论文 ↗</a></p></li>
            <li class="t-pub"><h3 class="t-pub__title">I³Retriever: Incorporating Implicit Interaction in Pre-trained Language Models for Passage Retrieval</h3><p class="t-pub__meta"><span>CIKM 2023</span><span class="t-badge">CCF-B</span><a href="https://doi.org/gs2pcc">论文 ↗</a></p></li>
            <li class="t-pub"><h3 class="t-pub__title">Incorporating Explicit Knowledge in Pre-trained Language Models for Passage Re-ranking</h3><p class="t-pub__meta"><span>SIGIR 2022</span><span class="t-badge">CCF-A</span><a href="https://doi.org/gsh8px">论文 ↗</a></p></li>
            <li class="t-pub"><h3 class="t-pub__title">Disentangled Graph Recurrent Network for Document Ranking</h3><p class="t-pub__meta"><span>Data Science and Engineering</span><span class="t-badge">JCR-Q1</span><a href="https://doi.org/gsh8pw">论文 ↗</a></p></li>
            <li class="t-pub"><h3 class="t-pub__title">Legal Judgment Prediction via Relational Learning</h3><p class="t-pub__meta"><span>SIGIR 2021</span><span class="t-badge">CCF-A</span><a href="https://doi.org/gq4w8t">论文 ↗</a></p></li>
            <li class="t-pub"><h3 class="t-pub__title">Latent Graph Recurrent Network for Document Ranking</h3><p class="t-pub__meta"><span>DASFAA 2021</span><span class="t-badge">CCF-B</span><a href="https://doi.org/gsh8ps">论文 ↗</a></p></li>
          </ul>
        </details>

        <details class="t-pub-group">
          <summary>代表性论文 · 合作作者（9）</summary>
          <ul class="t-pub-list">
            <li class="t-pub"><h3 class="t-pub__title">IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse</h3><p class="t-pub__meta"><span>arXiv 2026</span><a href="https://arxiv.org/abs/2603.12201">论文 ↗</a></p></li>
            <li class="t-pub"><h3 class="t-pub__title">CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges</h3><p class="t-pub__meta"><span>ACL 2025</span><span class="t-badge">CCF-A</span></p></li>
            <li class="t-pub"><h3 class="t-pub__title">LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods</h3><p class="t-pub__meta"><span>Under Review</span></p></li>
            <li class="t-pub"><h3 class="t-pub__title">DELTA: Pre-train a Discriminative Encoder for Legal Case Retrieval via Structural Word Alignment</h3><p class="t-pub__meta"><span>AAAI 2025</span><span class="t-badge">CCF-A</span></p></li>
            <li class="t-pub"><h3 class="t-pub__title">BLADE: Enhancing Black-box Large Language Models with Small Domain-Specific Models</h3><p class="t-pub__meta"><span>AAAI 2025</span><span class="t-badge">CCF-A</span></p></li>
            <li class="t-pub"><h3 class="t-pub__title">SAILER: Structure-aware Pre-trained Language Model for Legal Case Retrieval</h3><p class="t-pub__meta"><span>SIGIR 2023</span><span class="t-badge">CCF-A</span><a href="https://doi.org/gsjb5x">论文 ↗</a></p></li>
            <li class="t-pub"><h3 class="t-pub__title">Layout-aware Webpage Quality Assessment</h3><p class="t-pub__meta"><span>arXiv 2023</span><a href="https://doi.org/gsh8pz">论文 ↗</a></p></li>
            <li class="t-pub"><h3 class="t-pub__title">Incorporating Social-Aware User Preference for Video Recommendation</h3><p class="t-pub__meta"><span>WISE 2023</span><span class="t-badge">CCF-C</span><a href="https://doi.org/gs2pcb">论文 ↗</a></p></li>
            <li class="t-pub"><h3 class="t-pub__title">Emotion Recognition Based on Multi-View Body Gestures</h3><p class="t-pub__meta"><span>ICIP 2019</span><span class="t-badge">CCF-C</span><a href="https://doi.org/ghjxdq">论文 ↗</a></p></li>
          </ul>
        </details>
      </div>
    </section>

    <section class="t-section reveal" id="education">
      <h2 class="t-h2"><span class="t-h2__idx">// 06</span> 教育背景</h2>
      <ul class="t-log">
        <li class="t-log__item">
          <span class="t-log__date">2022 — 2026</span>
          <div>
            <span class="t-log__org">清华大学</span>
            <span class="t-log__role">博士</span>
            <p>计算机科学与技术 · THUIR</p>
          </div>
        </li>
        <li class="t-log__item">
          <span class="t-log__date">2019 — 2022</span>
          <div>
            <span class="t-log__org">中国科学院软件研究所</span>
            <span class="t-log__role">工程硕士</span>
            <p>计算机技术</p>
          </div>
        </li>
        <li class="t-log__item">
          <span class="t-log__date">2015 — 2019</span>
          <div>
            <span class="t-log__org">华南理工大学 <span class="t-dim">SCUT</span></span>
            <span class="t-log__role">工程学士</span>
            <p>软件工程</p>
          </div>
        </li>
      </ul>
    </section>

    <section class="t-section reveal" id="honors">
      <h2 class="t-h2"><span class="t-h2__idx">// 07</span> 荣誉奖项</h2>
      <div class="t-tags">
        <span class="t-tag t-tag--star">国家奖学金 · Top 1% · 2021</span>
      </div>
    </section>

    <section class="t-section reveal" id="more">
      <h2 class="t-h2"><span class="t-h2__idx">// 08</span> 研究之外</h2>
      <p class="t-note">
        工作之外，我喜欢探索<strong>精酿啤酒</strong>：
        从清爽的小麦啤、酒花浓郁的 IPA，到比利时白啤与赛松。🍻
      </p>
    </section>
  </main>

  <footer class="t-footer">
    <span>© {{ site.time | date: "%Y" }} 董骞 · </span>
    <span>最后更新于 {{ site.time | date: "%Y-%m-%d" }}</span>
  </footer>

  <script>
    window.difyChatbotConfig = { token: "6CoM85G6spngdgsq" };
  </script>
  <script src="https://udify.app/embed.min.js" id="6CoM85G6spngdgsq" defer></script>
  <script src="{{ '/assets/js/home.js' | relative_url }}" defer></script>
</body>
</html>
{:/nomarkdown}
