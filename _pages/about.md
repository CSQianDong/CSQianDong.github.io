---
permalink: /
title: "Qian Dong 董骞"
excerpt: "Home page"
author_profile: false
layout: bare
header: false
sidebar: false
masthead: false
redirect_from: 
  - /about/
  - /about.html
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Qian Dong</title>
    <meta name="author" content="Qian Dong">
    <meta name="description" content="Qian Dong - Ph.D. candidate at Tsinghua University, THUIR.">
    <link rel="icon" href="/images/icon.png" type="image/x-icon">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --global-bg-color: #f7f7f8;
            --global-text-color: #1a1a2e;
            --global-theme-color: #4a6fa5;
            --global-hover-color: #3a5a8c;
            --global-divider-color: #e5e7eb;
            --global-muted: #6b7280;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 1rem;
            line-height: 1.7;
            color: var(--global-text-color);
            background-color: var(--global-bg-color);
            -webkit-font-smoothing: antialiased;
        }

        a { color: var(--global-theme-color); text-decoration: none; transition: color 0.2s ease; }
        a:hover { color: var(--global-hover-color); text-decoration: none; }

        .container { max-width: 860px; margin: 0 auto; padding: 0 1.5rem; }

        /* Header */
        .post-header { margin-top: 3rem; margin-bottom: 0.5rem; }
        .post-title { font-size: 2rem; font-weight: 700; color: var(--global-text-color); line-height: 1.3; }
        .post-title .name-chinese { font-weight: 400; font-size: 1.5rem; }

        /* Profile image */
        .profile { float: right; margin: 0 0 1.5rem 2rem; width: 200px; }
        .profile img { width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }

        /* Bio text */
        .bio-text { font-size: 1rem; line-height: 1.8; color: var(--global-text-color); }
        .bio-text p { margin-bottom: 1rem; }

        /* Section headings */
        h2.section-title {
            font-size: 1.5rem; font-weight: 700; margin-top: 2.5rem; margin-bottom: 1rem;
            padding-bottom: 0.4rem; border-bottom: 2px solid var(--global-theme-color);
            color: var(--global-text-color);
        }

        /* News table */
        .news-table { width: 100%; max-height: 220px; overflow-y: auto; }
        .news-table table { width: 100%; border-collapse: collapse; }
        .news-table td { padding: 0.5rem 0.75rem; border-bottom: 1px solid var(--global-divider-color); vertical-align: top; font-size: 0.95rem; }
        .news-table td:first-child { white-space: nowrap; font-weight: 600; color: var(--global-theme-color); width: 110px; }

        /* Publication list */
        .pub-list { list-style: none; padding: 0; }
        .pub-list li { margin-bottom: 1.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid #f0f0f0; }
        .pub-list li:last-child { border-bottom: none; }
        .pub-info .title { font-weight: 600; font-size: 0.95rem; line-height: 1.45; color: var(--global-text-color); margin-bottom: 0.2rem; }
        .pub-info .authors { font-size: 0.87rem; color: var(--global-muted); margin-bottom: 0.15rem; }
        .pub-info .authors strong { color: var(--global-text-color); }
        .pub-info .venue { font-size: 0.87rem; color: var(--global-muted); font-style: italic; margin-bottom: 0.3rem; }
        .pub-info .links a {
            display: inline-block; font-size: 0.78rem; font-weight: 500;
            padding: 0.15rem 0.55rem; border: 1px solid var(--global-divider-color);
            border-radius: 4px; margin-right: 0.3rem; margin-top: 0.2rem; transition: all 0.2s;
        }
        .pub-info .links a:hover { background: var(--global-theme-color); color: #fff; border-color: var(--global-theme-color); }
        .pub-tags { display: inline-flex; gap: 0.3rem; margin-top: 0.2rem; }
        .tag { padding: 0.1rem 0.4rem; border-radius: 8px; font-size: 0.65rem; font-weight: 600; text-transform: uppercase; color: #fff; }
        .tag-ccf-a { background: #ef4444; }
        .tag-ccf-b { background: #f97316; }
        .tag-ccf-c { background: #eab308; }
        .tag-th-a { background: #22c55e; }
        .tag-th-b { background: #3b82f6; }
        .tag-jcr-q1 { background: #10b981; }

        /* Collapsible sections */
        .pub-section-header {
            display: flex; align-items: center; justify-content: space-between;
            padding: 0.75rem 0; cursor: pointer; user-select: none;
        }
        .pub-section-header h3 { font-size: 1.1rem; font-weight: 600; margin: 0; display: flex; align-items: center; gap: 0.5rem; color: var(--global-text-color); }
        .pub-section-header .toggle-icon { color: var(--global-muted); transition: transform 0.3s; font-size: 0.85rem; }
        .pub-section-header.active .toggle-icon { transform: rotate(180deg); }
        .pub-section-body { max-height: 0; overflow: hidden; transition: max-height 0.4s ease; }
        .pub-section-body.active { max-height: 8000px; }

        /* Awards / Education table */
        .info-table { width: 100%; border-collapse: collapse; }
        .info-table td { padding: 0.5rem 0.75rem; border-bottom: 1px solid var(--global-divider-color); font-size: 0.95rem; }
        .info-table td:first-child { font-weight: 600; font-style: italic; width: 100px; color: var(--global-theme-color); white-space: nowrap; }

        /* More text */
        .more-text { font-size: 1rem; line-height: 1.8; color: var(--global-muted); }

        /* Social icons */
        .social-icons { display: flex; gap: 1rem; margin-top: 1.5rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
        .social-icons a {
            display: inline-flex; align-items: center; justify-content: center;
            width: 38px; height: 38px; border-radius: 50%;
            border: 1px solid var(--global-divider-color); color: var(--global-muted);
            font-size: 1.1rem; transition: all 0.2s;
        }
        .social-icons a:hover { color: #fff; background: var(--global-theme-color); border-color: var(--global-theme-color); transform: translateY(-2px); }

        /* Footer */
        .site-footer {
            margin-top: 3rem; padding: 1.5rem 0;
            border-top: 1px solid var(--global-divider-color);
            text-align: center; font-size: 0.85rem; color: var(--global-muted);
        }

        .clearfix::after { content: ''; display: table; clear: both; }

        .lang-switch {
            display: inline-block; background: var(--global-theme-color); color: #fff;
            padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8rem; font-weight: 500;
            transition: all 0.2s; margin-left: 0.5rem;
        }
        .lang-switch:hover { background: var(--global-hover-color); color: #fff; text-decoration: none; }

        @media (max-width: 768px) {
            .profile { float: none; margin: 0 auto 1.5rem; width: 160px; text-align: center; }
        }
    </style>
</head>
<body>

<div class="container mt-5" role="main">
    <div class="post">
        <header class="post-header">
            <h1 class="post-title">
                <span class="name-english"><span style="font-weight:700;">Qian</span> Dong</span>
                (<span class="name-chinese">董骞</span>)
                <a href="/zh/" class="lang-switch">中文</a>
            </h1>
        </header>

        <article>
            <div class="profile">
                <figure>
                    <img src="/images/profile.jpg" alt="Qian Dong" loading="eager">
                </figure>
            </div>

            <div class="bio-text clearfix">
                <p>
                    I am a final-year Ph.D. student at <a href="https://ai.thuir.cn/" target="_blank">THUIR</a>,
                    <a href="https://www.cs.tsinghua.edu.cn/" target="_blank">Department of Computer Science and Technology</a>,
                    <a href="https://www.tsinghua.edu.cn/" target="_blank">Tsinghua University</a>.
                    I am fortunate to be supervised by Prof.
                    <a href="http://www.thuir.cn/group/msp/" target="_blank">Shaoping Ma</a>, Prof.
                    <a href="http://www.thuir.cn/group/YQLiu/" target="_blank">Yiqun Liu</a> and Prof.
                    <a href="http://www.thuir.cn/group/aiqy/" target="_blank">Qingyao Ai</a>.
                </p>
                <p>
                    My research interests include <strong>Information Retrieval</strong>,
                    <strong>Large Language Model Applications</strong>, and
                    <strong>Long-Context LLM</strong>.
                    I also serve as a reviewer / PC member for SIGIR, ACL, WWW, CIKM, COLING, AAAI, TOIS, etc.
                </p>
                <p>
                    <a href="mailto:qiandong.97@qq.com" title="Email"><i class="fas fa-envelope"></i></a>&nbsp;&nbsp;
                    <a href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&hl=en" target="_blank" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>&nbsp;&nbsp;
                    <a href="https://github.com/CSQianDong" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>&nbsp;&nbsp;
                    <a href="https://x.com/verymakesense" target="_blank" title="Twitter/X">
                        <svg style="width:16px;height:16px;fill:currentColor;vertical-align:middle;" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                    </a>&nbsp;&nbsp;
                    <a href="https://www.xiaohongshu.com/user/profile/64d8bdc1000000000100f445" target="_blank" title="Xiaohongshu"><img src="/images/xhs.png" alt="XHS" style="width:16px;height:16px;border-radius:50%;vertical-align:middle;"></a>
                </p>
            </div>

            <!-- Quote -->
            <div style="text-align:center;margin:2rem 0 2.5rem;padding:1.2rem 0;border-top:1px solid var(--global-divider-color);border-bottom:1px solid var(--global-divider-color);">
                <p style="font-family:Georgia,serif;font-style:italic;font-size:1.15rem;margin-bottom:0.3rem;color:var(--global-text-color);">
                    "Do not go gentle into that good night."</p>
                <p style="font-size:0.85rem;opacity:0.6;color:var(--global-text-color);margin:0;">
                    — Dylan Thomas</p>
            </div>

            <!-- News -->
            <h2 class="section-title">News</h2>
            <div class="news-table">
                <table>
                    <tr><td>Feb 2026</td><td>🚀 <a href="https://www.arxiv.org/abs/2602.15763" target="_blank">GLM-5 Technical Report</a> is released! I am one of the core contributors for model architecture.</td></tr>
                    <tr><td>Dec 2025</td><td>🚀 GLM-4.7 is released! <a href="https://z.ai/blog/glm-4.7" target="_blank">Blog</a></td></tr>
                    <tr><td>Sep 2025</td><td>🚀 GLM-4.6 is released! <a href="https://z.ai/blog/glm-4.6" target="_blank">Blog</a></td></tr>
                    <tr><td>Aug 2025</td><td>🚀 <a href="https://arxiv.org/abs/2508.06471" target="_blank">GLM-4.5 Technical Report</a> is released! I am one of the contributors for exploring sparse attention adaptation in the post-training stage.</td></tr>
                </table>
            </div>

            <!-- Selected Publications -->
            <h2 class="section-title">Selected Publications</h2>

            <h5 style="margin-bottom:1rem;">
                <a href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&hl=en" target="_blank" style="text-decoration:none;">
                    <i class="ai ai-google-scholar" style="vertical-align:middle;margin-right:4px;"></i>
                    <strong>Full Paper List on Google Scholar</strong>
                </a>
            </h5>

            <!-- Primary Author -->
            <div>
                <div class="pub-section-header active" onclick="togglePub('primary')">
                    <h3><i class="fas fa-star" style="color:var(--global-theme-color);"></i> As the Primary Author</h3>
                    <i class="fas fa-chevron-down toggle-icon"></i>
                </div>
                <div class="pub-section-body active" id="primary">
                    <ul class="pub-list">
                        <li><div class="pub-info"><div class="title">SelfRACG: Enabling LLMs to Self-Express and Retrieve for Code Generation</div><div class="authors"><strong>Qian Dong</strong>, Jia Chen, Qingyao Ai, Hongning Wang, Haitao Li, Yi Wu, Yao Hu, Yiqun Liu, Shaoping Ma</div><div class="venue">EMNLP 2025</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-b">CCF-B</span></div><div class="links"><a href="https://www.arxiv.org/abs/2507.19033" target="_blank">Paper</a></div></div></li>

                        <li><div class="pub-info"><div class="title">Qilin: A Multimodal Information Retrieval Dataset with APP-level User Sessions</div><div class="authors">Jia Chen*, <strong>Qian Dong</strong>*, Haitao Li, Xiaohui He, Yan Gao, Shaosheng Cao, Yi Wu, Ping Yang, Chen Xu, Yao Hu, Qingyao Ai, Yiqun Liu <span style="font-size:.75rem">(* Equal Contribution)</span></div><div class="venue">SIGIR 2025</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-a">CCF-A</span></div></div></li>

                        <li><div class="pub-info"><div class="title">DecoupledRAG: An Efficient and Effective Retrieval Augmented Generation Framework via Cross Attention</div><div class="authors"><strong>Qian Dong</strong>, Qingyao Ai, Hongning Wang, Yiding Liu, Haitao Li, Weihang Su, Yiqun Liu, Tat-Seng Chua, Shaoping Ma</div><div class="venue">WWW 2025</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-a">CCF-A</span></div></div></li>

                        <li><div class="pub-info"><div class="title">Unsupervised Large Language Model Alignment for Information Retrieval via Contrastive Feedback</div><div class="authors"><strong>Qian Dong</strong>, Yiding Liu, Qingyao Ai, Zhijing Wu, Haitao Li, Yiqun Liu, Shuaiqiang Wang, Dawei Yin, Shaoping Ma</div><div class="venue">SIGIR 2024</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-a">CCF-A</span></div><div class="links"><a href="https://doi.org/gss8w3" target="_blank">Paper</a></div></div></li>

                        <li><div class="pub-info"><div class="title">T<sup>2</sup>Ranking: A Large-scale Chinese Benchmark for Passage Ranking</div><div class="authors">Xiaohui Xie, <strong>Qian Dong</strong>* (Student First Author), Bingning Wang, Feiyang Lv, Ting Yao, Weinan Gan, Zhijing Wu, Xiangsheng Li, Haitao Li, Yiqun Liu, Jin Ma</div><div class="venue">SIGIR 2023</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-a">CCF-A</span></div><div class="links"><a href="https://doi.org/gsjb5w" target="_blank">Paper</a></div></div></li>

                        <li><div class="pub-info"><div class="title">I<sup>3</sup>Retriever: Incorporating Implicit Interaction in Pre-trained Language Models for Passage Retrieval</div><div class="authors"><strong>Qian Dong</strong>, Yiding Liu, Qingyao Ai, Haitao Li, Shuaiqiang Wang, Yiqun Liu, Dawei Yin, Shaoping Ma</div><div class="venue">CIKM 2023</div><div class="pub-tags"><span class="tag tag-th-b">TH-CPL-B</span><span class="tag tag-ccf-b">CCF-B</span></div><div class="links"><a href="https://doi.org/gs2pcc" target="_blank">Paper</a></div></div></li>

                        <li><div class="pub-info"><div class="title">Incorporating Explicit Knowledge in Pre-trained Language Models for Passage Re-ranking</div><div class="authors"><strong>Qian Dong</strong>, Yiding Liu, Suqi Cheng, Shuaiqiang Wang, Zhicong Cheng, Shuzi Niu, Dawei Yin</div><div class="venue">SIGIR 2022</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-a">CCF-A</span></div><div class="links"><a href="https://doi.org/gsh8px" target="_blank">Paper</a></div></div></li>

                        <li><div class="pub-info"><div class="title">Disentangled Graph Recurrent Network for Document Ranking</div><div class="authors"><strong>Qian Dong</strong>, Shuzi Niu, Tao Yuan, Yucheng Li</div><div class="venue">Data Science and Engineering — DASFAA 2021 Special Issue (JCR-Q1, IF: 7.2)</div><div class="pub-tags"><span class="tag tag-jcr-q1">JCR-Q1</span></div><div class="links"><a href="https://doi.org/gsh8pw" target="_blank">Paper</a></div></div></li>

                        <li><div class="pub-info"><div class="title">Legal Judgment Prediction via Relational Learning</div><div class="authors"><strong>Qian Dong</strong>, Shuzi Niu</div><div class="venue">SIGIR 2021</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-a">CCF-A</span></div><div class="links"><a href="https://doi.org/gq4w8t" target="_blank">Paper</a></div></div></li>

                        <li><div class="pub-info"><div class="title">Latent Graph Recurrent Network for Document Ranking</div><div class="authors"><strong>Qian Dong</strong>, Shuzi Niu</div><div class="venue">DASFAA 2021</div><div class="pub-tags"><span class="tag tag-th-b">TH-CPL-B</span><span class="tag tag-ccf-b">CCF-B</span></div><div class="links"><a href="https://doi.org/gsh8ps" target="_blank">Paper</a></div></div></li>
                    </ul>
                </div>
            </div>

            <!-- Co-author -->
            <div>
                <div class="pub-section-header" onclick="togglePub('coauthor')">
                    <h3><i class="fas fa-users" style="color:var(--global-theme-color);"></i> As a Co-author</h3>
                    <i class="fas fa-chevron-down toggle-icon"></i>
                </div>
                <div class="pub-section-body" id="coauthor">
                    <ul class="pub-list">
                        <li><div class="pub-info"><div class="title">CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges</div><div class="authors">Haitao Li, Junjie Chen, Qingyao Ai, Zhumin Chu, Yujia Zhou, <strong>Qian Dong</strong>, Yiqun Liu</div><div class="venue">ACL 2025</div><div class="pub-tags"><span class="tag tag-ccf-a">CCF-A</span></div></div></li>

                        <li><div class="pub-info"><div class="title">LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods</div><div class="authors">Haitao Li, <strong>Qian Dong</strong>, Junjie Chen, Huixue Su, Yujia Zhou, Qingyao Ai, Ziyi Ye, Yiqun Liu</div><div class="venue">Under Review</div></div></li>

                        <li><div class="pub-info"><div class="title">DELTA: Pre-train a Discriminative Encoder for Legal Case Retrieval via Structural Word Alignment</div><div class="authors">Haitao Li, Qingyao Ai, Xinyan Han, Jia Chen, <strong>Qian Dong</strong>, Yiqun Liu, Chong Chen, Qi Tian</div><div class="venue">AAAI 2025</div><div class="pub-tags"><span class="tag tag-ccf-a">CCF-A</span></div></div></li>

                        <li><div class="pub-info"><div class="title">BLADE: Enhancing Black-box Large Language Models with Small Domain-Specific Models</div><div class="authors">Haitao Li, Qingyao Ai, Jia Chen, <strong>Qian Dong</strong>, Zhijing Wu, Yiqun Liu, Chong Chen, Qi Tian</div><div class="venue">AAAI 2025</div><div class="pub-tags"><span class="tag tag-ccf-a">CCF-A</span></div></div></li>

                        <li><div class="pub-info"><div class="title">SAILER: Structure-aware Pre-trained Language Model for Legal Case Retrieval</div><div class="authors">Haitao Li, Qingyao Ai, Jia Chen, <strong>Qian Dong</strong>, Yueyue Wu, Yiqun Liu, Chong Chen, Qi Tian</div><div class="venue">SIGIR 2023</div><div class="pub-tags"><span class="tag tag-ccf-a">CCF-A</span></div><div class="links"><a href="https://doi.org/gsjb5x" target="_blank">Paper</a></div></div></li>

                        <li><div class="pub-info"><div class="title">Layout-aware Webpage Quality Assessment</div><div class="authors">Anfeng Cheng, Yiding Liu, Weibin Li, <strong>Qian Dong</strong>, Shuaiqiang Wang, Zhengjie Huang, Shikun Feng, Zhicong Cheng, Dawei Yin</div><div class="venue">arXiv 2023</div><div class="links"><a href="https://doi.org/gsh8pz" target="_blank">Paper</a></div></div></li>

                        <li><div class="pub-info"><div class="title">Incorporating Social-Aware User Preference for Video Recommendation</div><div class="authors">Xuanji Xiao, Huaqiang Dai, <strong>Qian Dong</strong>, Shuzi Niu, Yuzhen Liu, Pei Liu</div><div class="venue">WISE 2023</div><div class="pub-tags"><span class="tag tag-ccf-c">CCF-C</span></div><div class="links"><a href="https://doi.org/gs2pcb" target="_blank">Paper</a></div></div></li>

                        <li><div class="pub-info"><div class="title">Emotion Recognition Based on Multi-View Body Gestures</div><div class="authors">Zhijuan Shen, Jun Cheng, Xiping Hu, <strong>Qian Dong</strong></div><div class="venue">ICIP 2019</div><div class="pub-tags"><span class="tag tag-ccf-c">CCF-C</span></div><div class="links"><a href="https://doi.org/ghjxdq" target="_blank">Paper</a></div></div></li>
                    </ul>
                </div>
            </div>

            <!-- Education -->
            <h2 class="section-title">Education</h2>
            <table class="info-table">
                <tr><td>2022 –</td><td><strong>Ph.D. Student</strong>, Dept. of Computer Science and Technology, <a href="https://www.tsinghua.edu.cn/" target="_blank">Tsinghua University</a></td></tr>
                <tr><td>2019 – 2022</td><td><strong>M.Eng.</strong>, <a href="http://www.is.cas.cn/" target="_blank">Institute of Software, Chinese Academy of Sciences</a></td></tr>
                <tr><td>2015 – 2019</td><td><strong>B.Eng.</strong>, School of Software Engineering, <a href="https://www.scut.edu.cn/" target="_blank">South China University of Technology</a></td></tr>
            </table>

            <!-- Awards -->
            <h2 class="section-title">Honors &amp; Awards</h2>
            <table class="info-table">
                <tr><td>2021</td><td>National Scholarship (<strong>Top 1%</strong>)</td></tr>
            </table>

            <!-- More -->
            <h2 class="section-title">More About Me</h2>
            <p class="more-text">
                I'm an enthusiast of a diverse array of craft beers, ranging from crisp wheat beers to robust IPAs and everything in between. I'm always on the lookout for exceptional brews from various corners of the globe. Whether it's the refreshing notes of a Belgian Witbier, the hop-forward complexity of an IPA, or the subtle elegance of a Saison, I relish the opportunity to savor and discover the craftsmanship behind each unique flavor profile! 🍻
            </p>

            <!-- Social icons -->
            <div class="social-icons">
                <a href="mailto:qiandong.97@qq.com" title="Email"><i class="fas fa-envelope"></i></a>
                <a href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&hl=en" target="_blank" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
                <a href="https://github.com/CSQianDong" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>
                <a href="https://x.com/verymakesense" target="_blank" title="Twitter/X">
                    <svg style="width:16px;height:16px;fill:currentColor;" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                </a>
                <a href="https://www.xiaohongshu.com/user/profile/64d8bdc1000000000100f445" target="_blank" title="Xiaohongshu">
                    <img src="/images/xhs.png" alt="XHS" style="width:18px;height:18px;border-radius:50%;">
                </a>
            </div>

            <div style="text-align:center;margin:1.5rem 0;">
                <script type="text/javascript" id="clustrmaps" src="//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=a&t=n&d=J7QANnH4LJYLoOu_V6HTux3g537xFQCL00jK2z4-6jg"></script>
            </div>

        </article>
    </div>
</div>

<footer class="site-footer">
    <div class="container">
        Last updated: {{ site.time | date: "%B %d, %Y" }}
    </div>
</footer>

<!-- Dify Chatbot -->
<script>
 window.difyChatbotConfig = { token: '6CoM85G6spngdgsq' };
</script>
<script src="https://udify.app/embed.min.js" id="6CoM85G6spngdgsq" defer></script>
<style>
  #dify-chatbot-bubble-button { background-color: #4a6fa5 !important; }
  #dify-chatbot-bubble-window { width: 24rem !important; height: 40rem !important; }
</style>

<script>
function togglePub(id) {
    var body = document.getElementById(id);
    var header = body.previousElementSibling;
    body.classList.toggle('active');
    header.classList.toggle('active');
}
</script>

</body>
</html>
