---
permalink: /
title: "Qian Dong 董骞"
excerpt: "Qian Dong — Research Engineer on the Scaling Team at Tencent HY, working on model architecture."
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
  <meta name="description" content="Qian Dong — Research Engineer on the Scaling Team at Tencent HY, working on scalable model architectures.">
  <meta name="theme-color" content="#0b0d10">
  <title>Qian Dong 董骞</title>
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
      <a class="t-brand" href="{{ '/' | relative_url }}">qian.dong</a>
      <div class="t-nav__links">
        <a href="#research">research</a>
        <a href="#news">news</a>
        <a href="#publications">publications</a>
        <a class="t-utility" href="{{ '/submit/' | relative_url }}">submit</a>
        <a class="t-utility" href="{{ '/dm/' | relative_url }}">dm</a>
        <a class="t-lang" href="{{ '/zh/' | relative_url }}">中文</a>
      </div>
    </nav>
  </header>

  <main class="t-main" id="main-content">
    <header class="t-hero">
      <p class="t-hero__path">~/qian-dong<span> $</span></p>
      <h1 class="t-hero__name">Qian Dong <span>董骞</span></h1>
      <p class="t-hero__line">
        <span class="t-prompt">&gt;</span><span id="hero-rotator" data-phrases='["Research Engineer @ Tencent HY","Model Architecture","Scalable Intelligence"]'>Research Engineer @ Tencent HY</span><span class="t-cursor">_</span>
      </p>
      <p class="t-hero__bio">
        Research Engineer on the Scaling Team at
        <a href="https://hy.tencent.ai/">Tencent HY</a>, working on
        <strong>model architecture</strong>. I received my Ph.D. in Computer Science
        and Technology from Tsinghua University.
      </p>
      <nav class="t-hero__links" aria-label="Profile links">
        <a class="t-link" href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&amp;hl=en">scholar</a>
        <a class="t-link" href="https://github.com/CSQianDong">github</a>
        <a class="t-link" href="mailto:qiandong.97@qq.com">email</a>
        <a class="t-link" href="https://www.linkedin.com/in/qian-dong-58b14a23a/">linkedin</a>
        <a class="t-link" href="https://x.com/verymakesense">x</a>
        <a class="t-link" href="https://www.xiaohongshu.com/user/profile/64d8bdc1000000000100f445">xiaohongshu</a>
      </nav>
    </header>

    <section class="t-section reveal" id="about">
      <h2 class="t-h2"><span class="t-h2__idx">// 01</span> about</h2>
      <div class="t-prose">
        <p>
          I am a Research Engineer on the Scaling Team at
          <a href="https://hy.tencent.ai/">Tencent HY</a>, where I work on model
          architecture.
          I received my Ph.D. in Computer Science and Technology from
          <a href="https://www.tsinghua.edu.cn/">Tsinghua University</a> in June 2026.
          I was fortunate to be advised by Prof.
          <a href="http://www.thuir.cn/group/msp/">Shaoping Ma</a>, Prof.
          <a href="http://www.thuir.cn/group/YQLiu/">Yiqun Liu</a>, and Prof.
          <a href="http://www.thuir.cn/group/aiqy/">Qingyao Ai</a>. My research
          focuses on efficient, scalable model architectures and the systems that
          make them practical.
        </p>
      </div>
    </section>

    <section class="t-section reveal" id="research">
      <h2 class="t-h2"><span class="t-h2__idx">// 02</span> research</h2>
      <div class="t-grid">
        <article class="t-card">
          <span class="t-card__no">01</span>
          <h3 class="t-card__title">Model Architecture</h3>
          <p class="t-card__desc">Co-designing algorithms and infrastructure for capable models that remain efficient at scale.</p>
        </article>
        <article class="t-card">
          <span class="t-card__no">02</span>
          <h3 class="t-card__title">Efficient Attention</h3>
          <p class="t-card__desc">Sparse attention, linear attention, and architecture-level techniques for reducing inference cost.</p>
        </article>
        <article class="t-card">
          <span class="t-card__no">03</span>
          <h3 class="t-card__title">Scalable Context</h3>
          <p class="t-card__desc">Extending useful context while balancing model quality, memory, throughput, and latency.</p>
        </article>
        <article class="t-card">
          <span class="t-card__no">04</span>
          <h3 class="t-card__title">Low-Precision Training</h3>
          <p class="t-card__desc">Developing stable low-precision methods that reduce training cost while preserving model quality at scale.</p>
        </article>
      </div>
    </section>

    <section class="t-section reveal" id="news">
      <h2 class="t-h2"><span class="t-h2__idx">// 03</span> news</h2>
      <ul class="t-news">
        <li><span class="t-news__date">2026.08</span><p><a href="https://hy.tencent.ai/research/hy4-preview"><strong>Hy4 preview</strong></a> was released. As one of its model-architecture contributors, I helped bring our research <a href="https://arxiv.org/abs/2603.12201"><strong>IndexCache</strong></a> into production in Hy4, enabling a cost-efficient 1M-token context.</p></li>
        <li><span class="t-news__date">2026.06</span><p>I received my <strong>Ph.D. in Computer Science and Technology</strong> from Tsinghua University.</p></li>
        <li><span class="t-news__date">2026.03</span><p><a href="https://arxiv.org/abs/2603.12201"><strong>IndexCache</strong></a> was released, accelerating sparse attention via cross-layer index reuse.</p></li>
        <li><span class="t-news__date">2026.02</span><p>The <a href="https://www.arxiv.org/abs/2602.15763">GLM-5 Technical Report</a> was released. I am one of the core contributors to model architecture.</p></li>
        <li><span class="t-news__date">2025.12</span><p><strong>GLM-4.7</strong> was released. See our <a href="https://z.ai/blog/glm-4.7">blog</a> for details.</p></li>
        <li><span class="t-news__date">2025.09</span><p><strong>GLM-4.6</strong> was released. See our <a href="https://z.ai/blog/glm-4.6">blog</a> for details.</p></li>
        <li><span class="t-news__date">2025.08</span><p>The <a href="https://arxiv.org/abs/2508.06471">GLM-4.5 Technical Report</a> was released. I contributed to sparse-attention adaptation during post-training.</p></li>
      </ul>
    </section>

    <section class="t-section reveal" id="publications">
      <h2 class="t-h2"><span class="t-h2__idx">// 04</span> publications</h2>
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

    <section class="t-section reveal" id="more">
      <h2 class="t-h2"><span class="t-h2__idx">// 05</span> beyond research</h2>
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
