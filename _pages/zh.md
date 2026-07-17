---
permalink: /zh/
title: "董骞"
excerpt: "董骞个人主页 — 清华大学计算机科学与技术博士，研究方向为可扩展模型架构。"
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
  <meta name="description" content="董骞 — 清华大学计算机科学与技术博士，研究可扩展模型架构、高效注意力与信息检索。">
  <meta name="theme-color" content="#0b0d10">
  <title>董骞 | Qian Dong</title>
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
      <a class="t-brand" href="{{ '/zh/' | relative_url }}">qian.dong</a>
      <div class="t-nav__links">
        <a href="#research">研究</a>
        <a href="#news">动态</a>
        <a href="#publications">论文</a>
        <a href="#education">教育</a>
        <a class="t-utility" href="{{ '/submit/' | relative_url }}">投稿</a>
        <a class="t-utility" href="{{ '/dm/' | relative_url }}">留言</a>
        <a class="t-lang" href="{{ '/' | relative_url }}">EN</a>
      </div>
    </nav>
  </header>

  <main class="t-main" id="main-content">
    <header class="t-hero">
      <p class="t-hero__path">~/qian-dong<span> $</span></p>
      <h1 class="t-hero__name">董骞 <span>Qian Dong</span></h1>
      <p class="t-hero__line">
        <span class="t-prompt">&gt;</span><span id="hero-rotator" data-phrases='["清华大学博士","模型架构","可扩展智能"]'>清华大学博士</span><span class="t-cursor">_</span>
      </p>
      <p class="t-hero__bio">
        清华大学计算机科学与技术博士（<a href="https://ai.thuir.cn/">THUIR</a>）。
        我的研究聚焦于算法与基础设施协同设计的<strong>模型架构</strong>，
        以扩展参数、上下文，尤其是智能。
      </p>
      <nav class="t-hero__links" aria-label="个人链接">
        <a class="t-link" href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&amp;hl=en">学术主页</a>
        <a class="t-link" href="https://github.com/CSQianDong">github</a>
        <a class="t-link" href="mailto:qiandong.97@qq.com">邮箱</a>
        <a class="t-link" href="https://www.linkedin.com/in/qian-dong-58b14a23a/">linkedin</a>
        <a class="t-link" href="https://x.com/verymakesense">x</a>
        <a class="t-link" href="https://www.xiaohongshu.com/user/profile/64d8bdc1000000000100f445">小红书</a>
      </nav>
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

    <section class="t-section reveal" id="research">
      <h2 class="t-h2"><span class="t-h2__idx">// 02</span> 研究</h2>
      <div class="t-grid">
        <article class="t-card">
          <span class="t-card__no">01</span>
          <h3 class="t-card__title">模型架构</h3>
          <p class="t-card__desc">协同设计算法与基础设施，让模型能力随规模增长的同时保持高效。</p>
        </article>
        <article class="t-card">
          <span class="t-card__no">02</span>
          <h3 class="t-card__title">高效注意力</h3>
          <p class="t-card__desc">研究稀疏注意力、索引复用等架构级方法，降低模型推理成本。</p>
        </article>
        <article class="t-card">
          <span class="t-card__no">03</span>
          <h3 class="t-card__title">上下文扩展</h3>
          <p class="t-card__desc">在模型质量、显存、吞吐与时延之间取得平衡，扩展有效上下文。</p>
        </article>
        <article class="t-card">
          <span class="t-card__no">04</span>
          <h3 class="t-card__title">信息检索</h3>
          <p class="t-card__desc">研究排序与检索增强生成，让模型高效连接到正确的信息。</p>
        </article>
      </div>
    </section>

    <section class="t-section reveal" id="news">
      <h2 class="t-h2"><span class="t-h2__idx">// 03</span> 最新动态</h2>
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
        <li><span class="t-news__date">2024.07</span><p><strong>RLCF</strong> 被 SIGIR 2024 接收，通过无监督对比反馈对齐信息检索大模型。</p></li>
        <li><span class="t-news__date">2023.10</span><p><strong>I³Retriever</strong> 被 CIKM 2023 接收，将隐式查询—文档交互融入检索器。</p></li>
        <li><span class="t-news__date">2023.07</span><p><strong>T²Ranking</strong> 被 SIGIR 2023 接收，发布大规模中文段落排序基准。</p></li>
        <li><span class="t-news__date">2022.07</span><p><strong>KERM</strong> 被 SIGIR 2022 接收，将显式知识融入预训练模型用于段落重排序。</p></li>
        <li><span class="t-news__date">2022.02</span><p><strong>DGRe</strong> 发表于 Data Science and Engineering。</p></li>
        <li><span class="t-news__date">2021.07</span><p><strong>R-FORMER</strong> 被 SIGIR 2021 接收。</p></li>
        <li><span class="t-news__date">2021.04</span><p><strong>LGRe</strong> 被 DASFAA 2021 接收。</p></li>
      </ul>
    </section>

    <section class="t-section reveal" id="publications">
      <h2 class="t-h2"><span class="t-h2__idx">// 04</span> 论文</h2>
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
      <h2 class="t-h2"><span class="t-h2__idx">// 05</span> 教育背景</h2>
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
      <h2 class="t-h2"><span class="t-h2__idx">// 06</span> 荣誉奖项</h2>
      <div class="t-tags">
        <span class="t-tag t-tag--star">国家奖学金 · Top 1% · 2021</span>
      </div>
    </section>

    <section class="t-section reveal" id="more">
      <h2 class="t-h2"><span class="t-h2__idx">// 07</span> 研究之外</h2>
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
