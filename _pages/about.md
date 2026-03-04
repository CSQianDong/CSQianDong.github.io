---
permalink: /
title: "Qian Dong 董骞"
excerpt: "Home page"
author_profile: false
layout: null
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
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Qian Dong - THUIR, Tsinghua University</title>
    <link rel="icon" href="/images/icon.png" type="image/x-icon">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6; color: #1a1a1a; background: #f8fafc; overflow-x: hidden;
        }
        html { scroll-behavior: smooth; }

        /* Navbar */
        .navbar {
            position: fixed; top: 0; width: 100%;
            background: rgba(255,255,255,.95); backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(0,0,0,.1); z-index: 1000; transition: all .3s ease;
        }
        .nav-container {
            max-width: 1200px; margin: 0 auto; padding: 1rem 2rem;
            display: flex; justify-content: space-between; align-items: center;
        }
        .nav-logo { font-size: 1.25rem; font-weight: 700; color: #6366f1; text-decoration: none; }
        .nav-links { display: flex; gap: 2rem; list-style: none; }
        .nav-links a {
            text-decoration: none; color: #4b5563; font-weight: 500;
            transition: color .3s; position: relative;
        }
        .nav-links a:hover { color: #6366f1; }
        .nav-links a::after {
            content: ''; position: absolute; bottom: -5px; left: 0;
            width: 0; height: 2px; background: #6366f1; transition: width .3s;
        }
        .nav-links a:hover::after { width: 100%; }
        .lang-switch {
            background: linear-gradient(135deg,#6366f1,#8b5cf6);
            color: #fff; padding: .5rem 1rem; border-radius: 20px;
            text-decoration: none; font-size: .875rem; font-weight: 500;
            transition: all .3s; border: none; cursor: pointer;
        }
        .lang-switch:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(99,102,241,.3); }

        /* Hero */
        .hero {
            min-height: 100vh; background: linear-gradient(135deg,#667eea 0%,#764ba2 100%);
            display: flex; align-items: center; justify-content: center;
            position: relative; overflow: hidden; padding-top: 80px;
        }
        .hero::before {
            content: ''; position: absolute; inset: 0;
            background: radial-gradient(circle at 20% 80%,rgba(120,119,198,.3) 0%,transparent 50%),
                        radial-gradient(circle at 80% 20%,rgba(255,119,198,.3) 0%,transparent 50%);
        }
        .hero-content {
            text-align: center; color: #fff; z-index: 2;
            position: relative; max-width: 820px; padding: 0 2rem;
        }
        .hero-avatar {
            width: 140px; height: 140px; border-radius: 50%;
            border: 4px solid rgba(255,255,255,.4);
            box-shadow: 0 8px 32px rgba(0,0,0,.2);
            margin-bottom: 1.5rem; object-fit: cover;
        }
        .hero-badge {
            display: inline-block; background: rgba(255,255,255,.2);
            padding: .5rem 1rem; border-radius: 50px; font-size: .875rem;
            margin-bottom: 1rem; backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,.3);
        }
        .hero h1 { font-size: clamp(2.5rem,8vw,3.5rem); font-weight: 700; margin-bottom: .5rem; }
        .hero .subtitle {
            font-size: clamp(1.1rem,3vw,1.35rem); margin-bottom: 1.5rem;
            opacity: .92; font-weight: 300;
        }
        .hero .subtitle a { color: #fff; text-decoration: none; }
        .hero-intro {
            max-width: 660px; margin: 0 auto 2rem; font-size: 1.05rem;
            line-height: 1.7; opacity: .9; text-align: left;
        }
        .hero-intro a { color: #fff; text-decoration: underline; }
        .hero-buttons { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
        .btn-primary {
            background: linear-gradient(135deg,rgba(255,255,255,.15),rgba(255,255,255,.05));
            color: #fff; padding: .85rem 1.6rem; border-radius: 50px;
            text-decoration: none; font-weight: 600;
            transition: all .4s cubic-bezier(.175,.885,.32,1.275);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(255,255,255,.2);
            display: inline-flex; align-items: center; gap: .5rem;
            box-shadow: 0 8px 32px rgba(0,0,0,.1), inset 0 1px 0 rgba(255,255,255,.2);
        }
        .btn-primary:hover {
            background: linear-gradient(135deg,rgba(255,255,255,.25),rgba(255,255,255,.1));
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0,0,0,.3), 0 0 30px rgba(99,102,241,.4);
            border-color: rgba(255,255,255,.4);
        }

        /* Sections */
        .section { padding: 5rem 2rem; max-width: 1200px; margin: 0 auto; }
        .section-header { text-align: center; margin-bottom: 3rem; }
        .section-title {
            font-size: clamp(2rem,5vw,2.5rem); font-weight: 700;
            color: #1a1a1a; margin-bottom: 1rem; position: relative;
        }
        .section-title::after {
            content: ''; position: absolute; bottom: -10px; left: 50%;
            transform: translateX(-50%); width: 60px; height: 4px;
            background: linear-gradient(90deg,#6366f1,#8b5cf6); border-radius: 2px;
        }
        .section-subtitle { font-size: 1.125rem; color: #6b7280; max-width: 600px; margin: 0 auto; }

        /* Cards */
        .card-grid {
            display: grid; grid-template-columns: repeat(auto-fit,minmax(300px,1fr));
            gap: 2rem; margin-top: 2rem;
        }
        .card {
            background: linear-gradient(135deg,rgba(255,255,255,.9),rgba(255,255,255,.7));
            backdrop-filter: blur(20px); padding: 2rem; border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,.1), inset 0 1px 0 rgba(255,255,255,.3);
            transition: all .4s cubic-bezier(.175,.885,.32,1.275);
            border: 1px solid rgba(255,255,255,.2); position: relative; overflow: hidden;
        }
        .card::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
            background: linear-gradient(90deg,#6366f1,#8b5cf6,#ec4899);
            transform: scaleX(0); transition: transform .4s;
        }
        .card:hover { transform: translateY(-10px) scale(1.01); box-shadow: 0 25px 50px rgba(0,0,0,.15); }
        .card:hover::before { transform: scaleX(1); }
        .card-icon {
            width: 55px; height: 55px;
            background: linear-gradient(135deg,#6366f1,#8b5cf6);
            border-radius: 14px; display: flex; align-items: center; justify-content: center;
            margin-bottom: 1.2rem; font-size: 1.4rem; color: #fff;
            box-shadow: 0 8px 25px rgba(99,102,241,.3); transition: all .4s;
        }
        .card:hover .card-icon { transform: scale(1.1) rotate(5deg); }
        .card h3 { font-size: 1.2rem; font-weight: 600; margin-bottom: .75rem; }
        .card p { color: #6b7280; line-height: 1.6; }
        .card a { color: #6366f1; text-decoration: none; }
        .card a:hover { text-decoration: underline; }

        /* News */
        .news-table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
        .news-table td { padding: .75rem 1rem; border-bottom: 1px solid #e5e7eb; vertical-align: top; font-size: .95rem; }
        .news-table td:first-child { white-space: nowrap; font-weight: 600; color: #6366f1; width: 110px; }
        .news-table a { color: #6366f1; text-decoration: none; }
        .news-table a:hover { text-decoration: underline; }

        /* Publications */
        .pub-container { max-width: 960px; margin: 0 auto; }
        .pub-section {
            background: #fff; border-radius: 16px;
            box-shadow: 0 8px 30px rgba(0,0,0,.08); margin-bottom: 1.5rem; overflow: hidden;
        }
        .pub-header {
            display: flex; align-items: center; justify-content: space-between;
            padding: 1.25rem 1.75rem; cursor: pointer; transition: all .3s;
            border-bottom: 1px solid rgba(0,0,0,.05); user-select: none;
        }
        .pub-header:hover { background: rgba(99,102,241,.05); }
        .pub-header h3 { font-size: 1.2rem; font-weight: 600; margin: 0; display: flex; align-items: center; gap: .5rem; }
        .pub-header .toggle-icon { color: #6b7280; transition: transform .3s; font-size: .9rem; }
        .pub-header.active .toggle-icon { transform: rotate(180deg); }
        .pub-body { max-height: 0; overflow: hidden; transition: max-height .4s ease; }
        .pub-body.active { max-height: 5000px; }
        .pub-list { padding: 1rem 1.75rem 1.5rem; display: grid; gap: 1rem; }
        .pub-item {
            padding: 1rem 1.25rem; border-radius: 12px;
            background: #f8fafc; border-left: 4px solid #6366f1; transition: all .3s;
        }
        .pub-item:hover { background: #f1f5f9; transform: translateX(4px); }
        .pub-year { font-size: .8rem; font-weight: 700; color: #6366f1; margin-bottom: .2rem; }
        .pub-title { font-size: .95rem; font-weight: 600; color: #1a1a1a; line-height: 1.45; }
        .pub-authors { font-size: .85rem; color: #6b7280; margin-top: .25rem; }
        .pub-authors strong { color: #1a1a1a; }
        .pub-venue { font-size: .85rem; color: #6b7280; font-style: italic; margin-top: .15rem; }
        .pub-tags { display: flex; gap: .4rem; margin-top: .4rem; flex-wrap: wrap; align-items: center; }
        .tag { padding: .15rem .5rem; border-radius: 10px; font-size: .7rem; font-weight: 600; text-transform: uppercase; color: #fff; }
        .tag-ccf-a { background: #ef4444; }
        .tag-ccf-b { background: #f97316; }
        .tag-ccf-c { background: #eab308; }
        .tag-th-a { background: #22c55e; }
        .tag-th-b { background: #3b82f6; }
        .tag-jcr-q1 { background: #10b981; }
        .pub-link { font-size: .8rem; color: #6366f1; text-decoration: none; font-weight: 500; margin-left: .25rem; }
        .pub-link:hover { text-decoration: underline; }

        /* Awards */
        .awards-table { width: 100%; max-width: 700px; margin: 1.5rem auto 0; border-collapse: collapse; }
        .awards-table td { padding: .75rem 1rem; border-bottom: 1px solid #e5e7eb; font-size: .95rem; }
        .awards-table td:first-child { font-weight: 600; font-style: italic; width: 80px; }

        /* More */
        .more-text {
            max-width: 750px; margin: 0 auto; font-size: 1.05rem;
            line-height: 1.8; color: #4b5563; text-align: center;
        }

        /* Contact */
        .contact-section {
            background: linear-gradient(135deg,#667eea 0%,#764ba2 100%);
            color: #fff; padding: 5rem 2rem;
        }
        .contact-grid {
            display: grid; grid-template-columns: repeat(auto-fit,minmax(160px,1fr));
            gap: 1.5rem; max-width: 900px; margin: 2rem auto 0;
        }
        .contact-item {
            padding: 2rem 1.5rem; border-radius: 18px; text-align: center;
            border: 1px solid transparent; transition: all .5s cubic-bezier(.175,.885,.32,1.275);
            cursor: pointer; text-decoration: none; color: #fff; display: block;
        }
        .contact-item:hover {
            background: rgba(255,255,255,.15); backdrop-filter: blur(20px);
            border-color: rgba(255,255,255,.3); box-shadow: 0 12px 40px rgba(0,0,0,.2);
            transform: translateY(-6px);
        }
        .contact-icon { font-size: 2.2rem; margin-bottom: .75rem; opacity: .8; transition: all .4s; }
        .contact-item:hover .contact-icon { opacity: 1; transform: scale(1.1); }
        .contact-item p { font-weight: 500; font-size: .9rem; }

        /* Form */
        .contact-form-wrap {
            max-width: 560px; margin: 2.5rem auto 0; padding: 2rem;
            border-radius: 16px; background: rgba(255,255,255,.12);
            backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,.2);
        }
        .contact-form-wrap h3 { text-align: center; margin-bottom: 1.5rem; font-weight: 600; }
        .contact-form-wrap label { display: block; margin-bottom: .4rem; font-weight: 500; font-size: .9rem; }
        .contact-form-wrap input, .contact-form-wrap textarea {
            width: 100%; padding: .75rem 1rem; border-radius: 10px;
            border: 1px solid rgba(255,255,255,.3); background: rgba(255,255,255,.1);
            color: #fff; font-size: .95rem; margin-bottom: 1rem; font-family: inherit; transition: all .3s;
        }
        .contact-form-wrap input:focus, .contact-form-wrap textarea:focus {
            outline: none; border-color: rgba(255,255,255,.6);
            box-shadow: 0 0 0 3px rgba(255,255,255,.15);
        }
        .contact-form-wrap input::placeholder, .contact-form-wrap textarea::placeholder { color: rgba(255,255,255,.5); }
        .contact-form-wrap textarea { min-height: 100px; resize: vertical; }
        .form-btn {
            display: block; width: 100%; padding: .85rem;
            background: rgba(255,255,255,.2); border: 2px solid rgba(255,255,255,.3);
            color: #fff; font-size: 1rem; font-weight: 600; border-radius: 50px;
            cursor: pointer; transition: all .3s;
        }
        .form-btn:hover { background: rgba(255,255,255,.3); transform: translateY(-2px); }

        /* Particles */
        .particles { position: fixed; inset: 0; pointer-events: none; z-index: 1; overflow: hidden; }
        .particle { position: absolute; border-radius: 50%; pointer-events: none; mix-blend-mode: screen; }
        .particle-basic { background: rgba(255,255,255,.3); animation: floatUp linear infinite; }
        @keyframes floatUp {
            0% { transform: translateY(100vh) scale(0); opacity: 0; }
            10% { opacity: .6; transform: translateY(90vh) scale(1); }
            90% { opacity: .6; }
            100% { transform: translateY(-10vh) scale(0); opacity: 0; }
        }

        /* Fade-in */
        .fade-in { opacity: 0; transform: translateY(30px); transition: all .8s ease; }
        .fade-in.visible { opacity: 1; transform: translateY(0); }

        /* Responsive */
        @media (max-width: 768px) {
            .nav-links { display: none; }
            .hero { padding-top: 70px; }
            .card-grid { grid-template-columns: 1fr; }
            .hero-buttons { flex-direction: column; align-items: center; }
            .contact-grid { grid-template-columns: repeat(2,1fr); }
        }
        @media (max-width: 480px) { .contact-grid { grid-template-columns: 1fr; } }

        .footer-text { text-align: center; padding: 2rem; color: rgba(255,255,255,.6); font-size: .85rem; }
    </style>
</head>
<body>

<!-- Navigation -->
<nav class="navbar">
    <div class="nav-container">
        <a href="#" class="nav-logo">Qian Dong</a>
        <ul class="nav-links">
            <li><a href="#about">About</a></li>
            <li><a href="#research">Research</a></li>
            <li><a href="#education">Education</a></li>
            <li><a href="#publications">Publications</a></li>
            <li><a href="#awards">Awards</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
        <a href="/zh/" class="lang-switch">中文</a>
    </div>
</nav>

<!-- Particles -->
<div class="particles" id="particles"></div>

<!-- Hero -->
<section class="hero" id="about">
    <div class="hero-content fade-in">
        <img src="/images/profile.jpg" alt="Qian Dong" class="hero-avatar">
        <div class="hero-badge"><i class="fas fa-graduation-cap"></i> Ph.D. Candidate</div>
        <h1>Qian Dong 董骞</h1>
        <p class="subtitle">
            <a href="https://www.cs.tsinghua.edu.cn/" target="_blank">Department of Computer Science and Technology, Tsinghua University</a><br>
            <a href="https://ai.thuir.cn/" target="_blank">THUIR — Information Retrieval Lab</a>
        </p>
        <div class="hero-intro">
            <p>I am a final-year Ph.D. student at <a href="https://ai.thuir.cn/" target="_blank">THUIR</a>, Tsinghua University. I am fortunate to be supervised by Prof. <a href="http://www.thuir.cn/group/~msp/" target="_blank">Shaoping Ma</a>, Prof. <a href="http://www.thuir.cn/group/~YQLiu/" target="_blank">Yiqun Liu</a> and Prof. <a href="http://www.thuir.cn/group/~aiqy/" target="_blank">Qingyao Ai</a>. I also serve as a reviewer / PC member for SIGIR, ACL, WWW, CIKM, COLING, AAAI, TOIS, etc.</p>
        </div>
        <div class="hero-buttons">
            <a href="#research" class="btn-primary"><i class="fas fa-microscope"></i> Research</a>
            <a href="#contact" class="btn-primary"><i class="fas fa-envelope"></i> Contact</a>
            <a href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&hl=en" target="_blank" class="btn-primary"><i class="fas fa-graduation-cap"></i> Google Scholar</a>
            <a href="https://github.com/CSQianDong" target="_blank" class="btn-primary"><i class="fab fa-github"></i> GitHub</a>
        </div>
    </div>
</section>

<!-- News -->
<section class="section" id="news" style="background:#f8fafc;">
    <div class="section-header fade-in">
        <h2 class="section-title">News</h2>
    </div>
    <div style="max-width:800px;margin:0 auto;" class="fade-in">
        <table class="news-table">
            <tr><td>2026.02</td><td>🚀 <a href="https://www.arxiv.org/abs/2602.15763" target="_blank">GLM-5 Technical Report</a> is released! I am one of the core contributors for model architecture.</td></tr>
        </table>
    </div>
</section>

<!-- Research Interests -->
<section class="section" id="research" style="background:#f8fafc;">
    <div class="section-header fade-in">
        <h2 class="section-title">Research Interests</h2>
        <p class="section-subtitle">My work focuses on three interconnected areas</p>
    </div>
    <div class="card-grid">
        <div class="card fade-in">
            <div class="card-icon"><i class="fas fa-search"></i></div>
            <h3>Information Retrieval</h3>
            <p>Traditional and neural approaches for retrieval and reranking, advancing search accuracy and efficiency.</p>
        </div>
        <div class="card fade-in">
            <div class="card-icon"><i class="fas fa-brain"></i></div>
            <h3>LLM Applications</h3>
            <p>Leveraging IR techniques to enhance the capabilities and efficiency of large language models.</p>
        </div>
        <div class="card fade-in">
            <div class="card-icon"><i class="fas fa-text-width"></i></div>
            <h3>Long-Context LLM</h3>
            <p>Adapting LLMs to efficiently and effectively handle long inputs and outputs, pushing context boundaries.</p>
        </div>
    </div>
</section>

<!-- Education -->
<section class="section" id="education" style="background:#f8fafc;">
    <div class="section-header fade-in">
        <h2 class="section-title">Education</h2>
    </div>
    <div class="card-grid">
        <div class="card fade-in">
            <div class="card-icon"><i class="fas fa-university"></i></div>
            <h3>Ph.D. Student</h3>
            <p><strong><a href="https://www.cs.tsinghua.edu.cn/" target="_blank">Tsinghua University</a></strong><br>
            Dept. of Computer Science and Technology<br>
            <strong>Aug 2022 – Present</strong></p>
        </div>
        <div class="card fade-in">
            <div class="card-icon"><i class="fas fa-flask"></i></div>
            <h3>M.Eng.</h3>
            <p><strong><a href="http://www.is.cas.cn/" target="_blank">Institute of Software, CAS</a></strong><br>
            Supervised by Prof. <a href="https://people.ucas.ac.cn/~0058210" target="_blank">Shuzi Niu</a><br>
            <strong>Aug 2019 – Jun 2022</strong></p>
        </div>
        <div class="card fade-in">
            <div class="card-icon"><i class="fas fa-laptop-code"></i></div>
            <h3>B.Eng.</h3>
            <p><strong><a href="https://www.scut.edu.cn/" target="_blank">South China University of Technology</a></strong><br>
            School of Software Engineering<br>
            <strong>Aug 2015 – Jun 2019</strong></p>
        </div>
    </div>
</section>

<!-- Publications -->
<section class="section" id="publications" style="background:#f8fafc;">
    <div class="section-header fade-in">
        <h2 class="section-title">Publications</h2>
        <p class="section-subtitle">Click to expand each section</p>
    </div>
    <div class="pub-container fade-in">

        <!-- Primary Author -->
        <div class="pub-section">
            <div class="pub-header" onclick="togglePub('primary')">
                <h3><i class="fas fa-star" style="color:#6366f1;margin-right:.4rem"></i> As the Primary Author</h3>
                <i class="fas fa-chevron-down toggle-icon"></i>
            </div>
            <div class="pub-body" id="primary">
                <div class="pub-list">
                    <div class="pub-item"><div class="pub-year">2025</div><div class="pub-title">SelfRACG: Enabling LLMs to Self-Express and Retrieve for Code Generation</div><div class="pub-authors"><strong>Qian Dong</strong>, Jia Chen, Qingyao Ai, Hongning Wang, Haitao Li, Yi Wu, Yao Hu, Yiqun Liu, Shaoping Ma</div><div class="pub-venue">EMNLP 2025</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-b">CCF-B</span><a class="pub-link" href="https://www.arxiv.org/abs/2507.19033" target="_blank">[Paper]</a></div></div>

                    <div class="pub-item"><div class="pub-year">2025</div><div class="pub-title">Qilin: A Multimodal Information Retrieval Dataset with APP-level User Sessions</div><div class="pub-authors">Jia Chen<sup>★</sup>, <strong>Qian Dong</strong><sup>★</sup>, Haitao Li, Xiaohui He, Yan Gao, Shaosheng Cao, Yi Wu, Ping Yang, Chen Xu, Yao Hu, Qingyao Ai, Yiqun Liu <span style="font-size:.75rem">(★Equal Contribution)</span></div><div class="pub-venue">SIGIR 2025</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-a">CCF-A</span></div></div>

                    <div class="pub-item"><div class="pub-year">2025</div><div class="pub-title">DecoupledRAG: An Efficient and Effective Retrieval Augmented Generation Framework via Cross Attention</div><div class="pub-authors"><strong>Qian Dong</strong>, Qingyao Ai, Hongning Wang, Yiding Liu, Haitao Li, Weihang Su, Yiqun Liu, Tat-Seng Chua, Shaoping Ma</div><div class="pub-venue">WWW 2025</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-a">CCF-A</span></div></div>

                    <div class="pub-item"><div class="pub-year">2024</div><div class="pub-title">Unsupervised Large Language Model Alignment for Information Retrieval via Contrastive Feedback</div><div class="pub-authors"><strong>Qian Dong</strong>, Yiding Liu, Qingyao Ai, Zhijing Wu, Haitao Li, Yiqun Liu, Shuaiqiang Wang, Dawei Yin, Shaoping Ma</div><div class="pub-venue">SIGIR 2024</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-a">CCF-A</span><a class="pub-link" href="https://doi.org/gss8w3" target="_blank">[Paper]</a></div></div>

                    <div class="pub-item"><div class="pub-year">2023</div><div class="pub-title">T<sup>2</sup>Ranking: A Large-scale Chinese Benchmark for Passage Ranking</div><div class="pub-authors">Xiaohui Xie, <strong>Qian Dong</strong><sup>★</sup>, Bingning Wang, Feiyang Lv, Ting Yao, Weinan Gan, Zhijing Wu, Xiangsheng Li, Haitao Li, Yiqun Liu, Jin Ma <span style="font-size:.75rem">(★Student First Author)</span></div><div class="pub-venue">SIGIR 2023</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-a">CCF-A</span><a class="pub-link" href="https://doi.org/gsjb5w" target="_blank">[Paper]</a></div></div>

                    <div class="pub-item"><div class="pub-year">2023</div><div class="pub-title">I<sup>3</sup>Retriever: Incorporating Implicit Interaction in Pre-trained Language Models for Passage Retrieval</div><div class="pub-authors"><strong>Qian Dong</strong>, Yiding Liu, Qingyao Ai, Haitao Li, Shuaiqiang Wang, Yiqun Liu, Dawei Yin, Shaoping Ma</div><div class="pub-venue">CIKM 2023</div><div class="pub-tags"><span class="tag tag-th-b">TH-CPL-B</span><span class="tag tag-ccf-b">CCF-B</span><a class="pub-link" href="https://doi.org/gs2pcc" target="_blank">[Paper]</a></div></div>

                    <div class="pub-item"><div class="pub-year">2022</div><div class="pub-title">Incorporating Explicit Knowledge in Pre-trained Language Models for Passage Re-ranking</div><div class="pub-authors"><strong>Qian Dong</strong>, Yiding Liu, Suqi Cheng, Shuaiqiang Wang, Zhicong Cheng, Shuzi Niu, Dawei Yin</div><div class="pub-venue">SIGIR 2022</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-a">CCF-A</span><a class="pub-link" href="https://doi.org/gsh8px" target="_blank">[Paper]</a></div></div>

                    <div class="pub-item"><div class="pub-year">2022</div><div class="pub-title">Disentangled Graph Recurrent Network for Document Ranking</div><div class="pub-authors"><strong>Qian Dong</strong>, Shuzi Niu, Tao Yuan, Yucheng Li</div><div class="pub-venue">Data Science and Engineering — DASFAA 2021 Special Issue (JCR-Q1, IF: 7.2)</div><div class="pub-tags"><span class="tag tag-jcr-q1">JCR-Q1</span><a class="pub-link" href="https://doi.org/gsh8pw" target="_blank">[Paper]</a></div></div>

                    <div class="pub-item"><div class="pub-year">2021</div><div class="pub-title">Legal Judgment Prediction via Relational Learning</div><div class="pub-authors"><strong>Qian Dong</strong>, Shuzi Niu</div><div class="pub-venue">SIGIR 2021</div><div class="pub-tags"><span class="tag tag-th-a">TH-CPL-A</span><span class="tag tag-ccf-a">CCF-A</span><a class="pub-link" href="https://doi.org/gq4w8t" target="_blank">[Paper]</a></div></div>

                    <div class="pub-item"><div class="pub-year">2021</div><div class="pub-title">Latent Graph Recurrent Network for Document Ranking</div><div class="pub-authors"><strong>Qian Dong</strong>, Shuzi Niu</div><div class="pub-venue">DASFAA 2021</div><div class="pub-tags"><span class="tag tag-th-b">TH-CPL-B</span><span class="tag tag-ccf-b">CCF-B</span><a class="pub-link" href="https://doi.org/gsh8ps" target="_blank">[Paper]</a></div></div>
                </div>
            </div>
        </div>

        <!-- Co-author -->
        <div class="pub-section">
            <div class="pub-header" onclick="togglePub('coauthor')">
                <h3><i class="fas fa-users" style="color:#6366f1;margin-right:.4rem"></i> As a Co-author</h3>
                <i class="fas fa-chevron-down toggle-icon"></i>
            </div>
            <div class="pub-body" id="coauthor">
                <div class="pub-list">
                    <div class="pub-item"><div class="pub-year">2025</div><div class="pub-title">CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges</div><div class="pub-authors">Haitao Li, Junjie Chen, Qingyao Ai, Zhumin Chu, Yujia Zhou, <strong>Qian Dong</strong>, Yiqun Liu</div><div class="pub-venue">ACL 2025</div><div class="pub-tags"><span class="tag tag-ccf-a">CCF-A</span></div></div>

                    <div class="pub-item"><div class="pub-year">2025</div><div class="pub-title">LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods</div><div class="pub-authors">Haitao Li, <strong>Qian Dong</strong>, Junjie Chen, Huixue Su, Yujia Zhou, Qingyao Ai, Ziyi Ye, Yiqun Liu</div><div class="pub-venue">Under Review</div></div>

                    <div class="pub-item"><div class="pub-year">2025</div><div class="pub-title">DELTA: Pre-train a Discriminative Encoder for Legal Case Retrieval via Structural Word Alignment</div><div class="pub-authors">Haitao Li, Qingyao Ai, Xinyan Han, Jia Chen, <strong>Qian Dong</strong>, Yiqun Liu, Chong Chen, Qi Tian</div><div class="pub-venue">AAAI 2025</div><div class="pub-tags"><span class="tag tag-ccf-a">CCF-A</span></div></div>

                    <div class="pub-item"><div class="pub-year">2025</div><div class="pub-title">BLADE: Enhancing Black-box Large Language Models with Small Domain-Specific Models</div><div class="pub-authors">Haitao Li, Qingyao Ai, Jia Chen, <strong>Qian Dong</strong>, Zhijing Wu, Yiqun Liu, Chong Chen, Qi Tian</div><div class="pub-venue">AAAI 2025</div><div class="pub-tags"><span class="tag tag-ccf-a">CCF-A</span></div></div>

                    <div class="pub-item"><div class="pub-year">2023</div><div class="pub-title">SAILER: Structure-aware Pre-trained Language Model for Legal Case Retrieval</div><div class="pub-authors">Haitao Li, Qingyao Ai, Jia Chen, <strong>Qian Dong</strong>, Yueyue Wu, Yiqun Liu, Chong Chen, Qi Tian</div><div class="pub-venue">SIGIR 2023</div><div class="pub-tags"><span class="tag tag-ccf-a">CCF-A</span><a class="pub-link" href="https://doi.org/gsjb5x" target="_blank">[Paper]</a></div></div>

                    <div class="pub-item"><div class="pub-year">2023</div><div class="pub-title">Layout-aware Webpage Quality Assessment</div><div class="pub-authors">Anfeng Cheng, Yiding Liu, Weibin Li, <strong>Qian Dong</strong>, Shuaiqiang Wang, Zhengjie Huang, Shikun Feng, Zhicong Cheng, Dawei Yin</div><div class="pub-venue">arXiv</div><div class="pub-tags"><a class="pub-link" href="https://doi.org/gsh8pz" target="_blank">[Paper]</a></div></div>

                    <div class="pub-item"><div class="pub-year">2023</div><div class="pub-title">Incorporating Social-Aware User Preference for Video Recommendation</div><div class="pub-authors">Xuanji Xiao, Huaqiang Dai, <strong>Qian Dong</strong>, Shuzi Niu, Yuzhen Liu, Pei Liu</div><div class="pub-venue">WISE 2023</div><div class="pub-tags"><span class="tag tag-ccf-c">CCF-C</span><a class="pub-link" href="https://doi.org/gs2pcb" target="_blank">[Paper]</a></div></div>

                    <div class="pub-item"><div class="pub-year">2019</div><div class="pub-title">Emotion Recognition Based on Multi-View Body Gestures</div><div class="pub-authors">Zhijuan Shen, Jun Cheng, Xiping Hu, <strong>Qian Dong</strong></div><div class="pub-venue">ICIP 2019</div><div class="pub-tags"><span class="tag tag-ccf-c">CCF-C</span><a class="pub-link" href="https://doi.org/ghjxdq" target="_blank">[Paper]</a></div></div>
                </div>
            </div>
        </div>

    </div>
</section>

<!-- Awards -->
<section class="section" id="awards" style="background:#f8fafc;">
    <div class="section-header fade-in">
        <h2 class="section-title">Honors &amp; Awards</h2>
    </div>
    <div class="fade-in">
        <table class="awards-table">
            <tr><td>2021</td><td>National Scholarship (<strong>Top 1%</strong>)</td></tr>
        </table>
    </div>
</section>

<!-- More -->
<section class="section" style="background:#f8fafc;">
    <div class="section-header fade-in">
        <h2 class="section-title">More About Me</h2>
    </div>
    <p class="more-text fade-in">
        I'm an enthusiast of a diverse array of craft beers, ranging from crisp wheat beers to robust IPAs and everything in between. I'm always on the lookout for exceptional brews from various corners of the globe. Whether it's the refreshing notes of a Belgian Witbier, the hop-forward complexity of an IPA, or the subtle elegance of a Saison, I relish the opportunity to savor and discover the craftsmanship behind each unique flavor profile! 🍻
    </p>
</section>

<!-- Contact -->
<section class="contact-section" id="contact">
    <div class="section-header fade-in">
        <h2 class="section-title" style="color:#fff;">Contact</h2>
    </div>
    <div class="contact-grid fade-in">
        <a href="mailto:qiandong.97@qq.com" class="contact-item">
            <div class="contact-icon"><i class="fas fa-envelope"></i></div>
            <p>qiandong.97@qq.com</p>
        </a>
        <a href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&hl=en" target="_blank" class="contact-item">
            <div class="contact-icon"><i class="fas fa-graduation-cap"></i></div>
            <p>Google Scholar</p>
        </a>
        <a href="https://github.com/CSQianDong" target="_blank" class="contact-item">
            <div class="contact-icon"><i class="fab fa-github"></i></div>
            <p>GitHub</p>
        </a>
        <a href="https://x.com/verymakesense" target="_blank" class="contact-item">
            <div class="contact-icon">
                <svg style="width:32px;height:32px;fill:#fff;" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
            </div>
            <p>@verymakesense</p>
        </a>
        <a href="https://www.xiaohongshu.com/user/profile/64d8bdc1000000000100f445" target="_blank" class="contact-item">
            <div class="contact-icon">
                <img src="/images/xhs.png" alt="Xiaohongshu" style="width:40px;height:40px;border-radius:50%;">
            </div>
            <p>Xiaohongshu</p>
        </a>
    </div>

    <div class="contact-form-wrap fade-in">
        <h3>👋 Get in Touch</h3>
        <form action="https://formspree.io/f/mnnpaqvk" method="POST">
            <label for="cf-name">Name</label>
            <input type="text" id="cf-name" name="name" placeholder="Your name" required>
            <label for="cf-email">Email</label>
            <input type="email" id="cf-email" name="email" placeholder="your@email.com" required>
            <label for="cf-msg">Message</label>
            <textarea id="cf-msg" name="message" placeholder="Hello Qian..." required></textarea>
            <button type="submit" class="form-btn">Send Message</button>
        </form>
    </div>

    <div style="text-align:center;margin-top:2rem;">
        <script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=a&t=n&d=J7QANnH4LJYLoOu_V6HTux3g537xFQCL00jK2z4-6jg'></script>
    </div>

    <div class="footer-text">Last updated: {{ site.time | date: "%B %d, %Y" }}</div>
</section>

<!-- Dify Chatbot -->
<script>
 window.difyChatbotConfig = { token: '6CoM85G6spngdgsq' };
</script>
<script src="https://udify.app/embed.min.js" id="6CoM85G6spngdgsq" defer></script>
<style>
  #dify-chatbot-bubble-button { background-color: #1C64F2 !important; }
  #dify-chatbot-bubble-window { width: 24rem !important; height: 40rem !important; }
</style>

<script>
// Particles
(function(){
    var c=document.getElementById('particles');
    for(var i=0;i<35;i++){
        var p=document.createElement('div');
        p.className='particle particle-basic';
        var s=Math.random()*4+2;
        p.style.cssText='width:'+s+'px;height:'+s+'px;left:'+Math.random()*100+'%;animation-delay:'+Math.random()*20+'s;animation-duration:'+(Math.random()*12+14)+'s;';
        c.appendChild(p);
    }
})();

// Scroll fade-in
var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){ if(e.isIntersecting) e.target.classList.add('visible'); });
},{threshold:.12});
document.querySelectorAll('.fade-in').forEach(function(el){obs.observe(el);});

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click',function(e){
        e.preventDefault();
        var t=document.querySelector(this.getAttribute('href'));
        if(t) t.scrollIntoView({behavior:'smooth',block:'start'});
    });
});

// Navbar scroll
(function(){
    var nb=document.querySelector('.navbar');
    window.addEventListener('scroll',function(){
        if(window.pageYOffset>100){
            nb.style.background='rgba(255,255,255,.98)';
            nb.style.boxShadow='0 2px 20px rgba(0,0,0,.1)';
        } else {
            nb.style.background='rgba(255,255,255,.95)';
            nb.style.boxShadow='none';
        }
    });
})();

// Publication toggle
function togglePub(id){
    var body=document.getElementById(id);
    var header=body.previousElementSibling;
    body.classList.toggle('active');
    header.classList.toggle('active');
}
</script>

</body>
</html>
