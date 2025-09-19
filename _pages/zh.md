---
permalink: /zh/
title: "董骞 - 中文主页"
excerpt: "董骞个人中文主页，清华大学博士生"
author_profile: false
layout: null
header: false
sidebar: false
masthead: false
---

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>董骞 - 清华大学信息检索实验室</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #1a1a1a;
            background: #f8fafc;
            overflow-x: hidden;
        }

        /* 平滑滚动 */
        html {
            scroll-behavior: smooth;
        }

        /* 导航栏 */
        .navbar {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
            z-index: 1000;
            transition: all 0.3s ease;
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-logo {
            font-size: 1.25rem;
            font-weight: 700;
            color: #6366f1;
            text-decoration: none;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }

        .nav-links a {
            text-decoration: none;
            color: #4b5563;
            font-weight: 500;
            transition: color 0.3s ease;
            position: relative;
        }

        .nav-links a:hover {
            color: #6366f1;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: #6366f1;
            transition: width 0.3s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .lang-switch {
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            text-decoration: none;
            font-size: 0.875rem;
            font-weight: 500;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
        }

        .lang-switch:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(99, 102, 241, 0.3);
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            margin-top: 80px;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background:
                radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%);
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }

        .hero-content {
            text-align: center;
            color: white;
            z-index: 2;
            position: relative;
            max-width: 800px;
            padding: 0 2rem;
        }

        .hero-badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            padding: 0.5rem 1rem;
            border-radius: 50px;
            font-size: 0.875rem;
            margin-bottom: 1rem;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        .hero h1 {
            font-size: clamp(2.5rem, 8vw, 4rem);
            font-weight: 700;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #ffffff, #e0e7ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero .subtitle {
            font-size: clamp(1.2rem, 3vw, 1.5rem);
            margin-bottom: 2rem;
            opacity: 0.9;
            font-weight: 300;
        }

        .hero-intro {
            max-width: 600px;
            margin: 2rem auto 0;
            font-size: 1.1rem;
            line-height: 1.6;
            opacity: 0.9;
        }

        .hero-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 2rem;
        }

        .btn-primary {
            background: rgba(255, 255, 255, 0.2);
            color: white;
            padding: 1rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }

        .btn-primary:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-3px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
        }

        /* Sections */
        .section {
            padding: 5rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-header {
            text-align: center;
            margin-bottom: 3rem;
        }

        .section-title {
            font-size: clamp(2rem, 5vw, 2.5rem);
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 1rem;
            position: relative;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 4px;
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            border-radius: 2px;
        }

        .section-subtitle {
            font-size: 1.125rem;
            color: #6b7280;
            max-width: 600px;
            margin: 0 auto;
        }

        /* Research Interests */
        .research-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .research-card {
            background: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            border: 1px solid rgba(0, 0, 0, 0.05);
            position: relative;
            overflow: hidden;
        }

        .research-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            transform: scaleX(0);
            transition: transform 0.3s ease;
        }

        .research-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }

        .research-card:hover::before {
            transform: scaleX(1);
        }

        .research-icon {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
            font-size: 1.5rem;
            color: white;
        }

        .research-title {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: #1a1a1a;
        }

        .research-desc {
            color: #6b7280;
            line-height: 1.6;
        }

        /* Timeline */
        .timeline {
            position: relative;
            padding: 2rem 0;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(180deg, #6366f1, #8b5cf6);
            transform: translateX(-50%);
        }

        .timeline-item {
            position: relative;
            margin: 3rem 0;
            opacity: 0;
            transform: translateY(50px);
            animation: fadeInUp 0.6s ease forwards;
        }

        .timeline-item:nth-child(1) { animation-delay: 0.1s; }
        .timeline-item:nth-child(2) { animation-delay: 0.2s; }
        .timeline-item:nth-child(3) { animation-delay: 0.3s; }

        @keyframes fadeInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .timeline-content {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            width: 45%;
            position: relative;
        }

        .timeline-item:nth-child(odd) .timeline-content {
            margin-left: auto;
        }

        .timeline-dot {
            position: absolute;
            left: 50%;
            top: 2rem;
            width: 16px;
            height: 16px;
            background: #6366f1;
            border-radius: 50%;
            transform: translateX(-50%);
            border: 3px solid white;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
        }

        .timeline-date {
            color: #6366f1;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .timeline-title {
            font-size: 1.125rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: #1a1a1a;
        }

        .timeline-desc {
            color: #6b7280;
        }

        /* Contact Section */
        .contact {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 5rem 2rem;
        }

        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            max-width: 1000px;
            margin: 0 auto;
        }

        .contact-item {
            background: rgba(255, 255, 255, 0.1);
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
        }

        .contact-item:hover {
            background: rgba(255, 255, 255, 0.15);
            transform: translateY(-5px);
        }

        .contact-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            opacity: 0.9;
        }

        .contact-title {
            font-size: 1.125rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .contact a {
            color: white;
            text-decoration: none;
            opacity: 0.9;
            transition: opacity 0.3s ease;
        }

        .contact a:hover {
            opacity: 1;
        }

        /* Floating particles */
        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }

        .particle {
            position: absolute;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            animation: float-particle 20s infinite linear;
        }

        @keyframes float-particle {
            0% {
                transform: translateY(100vh) rotate(0deg);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translateY(-100vh) rotate(360deg);
                opacity: 0;
            }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .hero {
                margin-top: 60px;
            }

            .timeline::before {
                left: 30px;
            }

            .timeline-content {
                width: calc(100% - 60px);
                margin-left: 60px !important;
            }

            .timeline-dot {
                left: 30px;
            }

            .hero-buttons {
                flex-direction: column;
                align-items: center;
            }

            .research-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Loading Animation */
        .fade-in {
            opacity: 0;
            transform: translateY(30px);
            animation: fadeIn 0.8s ease forwards;
        }

        @keyframes fadeIn {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Publications Section */
        .publications-container {
            max-width: 1000px;
            margin: 0 auto;
        }

        .publication-section {
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            margin-bottom: 1.5rem;
            overflow: hidden;
        }

        .publication-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1.5rem 2rem;
            cursor: pointer;
            transition: all 0.3s ease;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
        }

        .publication-header:hover {
            background: rgba(99, 102, 241, 0.05);
        }

        .publication-header h3 {
            font-size: 1.25rem;
            font-weight: 600;
            color: #1a1a1a;
            margin: 0;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .publication-header i:first-child {
            color: #6366f1;
            font-size: 1.2rem;
        }

        .publication-header i:last-child {
            color: #6b7280;
            transition: transform 0.3s ease;
        }

        .publication-header.active i:last-child {
            transform: rotate(180deg);
        }

        .publication-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
        }

        .publication-content.active {
            max-height: 2000px;
        }

        .publication-grid {
            display: grid;
            gap: 1rem;
            padding: 1.5rem 2rem;
        }

        .publication-item {
            padding: 1rem;
            border-radius: 10px;
            background: #f8fafc;
            border-left: 4px solid #6366f1;
            transition: all 0.3s ease;
        }

        .publication-item:hover {
            background: #f1f5f9;
            transform: translateX(5px);
        }

        .publication-year {
            font-size: 0.875rem;
            font-weight: 600;
            color: #6366f1;
            margin-bottom: 0.25rem;
        }

        .publication-title {
            font-size: 1rem;
            font-weight: 500;
            color: #1a1a1a;
            margin-bottom: 0.25rem;
            line-height: 1.4;
        }

        .publication-venue {
            font-size: 0.875rem;
            color: #6b7280;
            font-style: italic;
        }

        .publication-tags {
            display: flex;
            gap: 0.5rem;
            margin-top: 0.5rem;
            flex-wrap: wrap;
        }

        .tag {
            padding: 0.2rem 0.5rem;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 500;
            text-transform: uppercase;
        }

        .tag-ccf-a {
            background: #ef4444;
            color: white;
        }

        .tag-ccf-b {
            background: #f97316;
            color: white;
        }

        .tag-ccf-c {
            background: #eab308;
            color: white;
        }

        .tag-th-a {
            background: #22c55e;
            color: white;
        }

        .tag-th-b {
            background: #3b82f6;
            color: white;
        }

        .tag-jcr-q1 {
            background: #10b981;
            color: white;
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <a href="#" class="nav-logo">董骞</a>
            <ul class="nav-links">
                <li><a href="#about">关于我</a></li>
                <li><a href="#research">研究方向</a></li>
                <li><a href="#education">教育经历</a></li>
                <li><a href="#publications">学术发表</a></li>
                <li><a href="#contact">联系方式</a></li>
            </ul>
            <a href="/" class="lang-switch">English</a>
        </div>
    </nav>

    <!-- Floating Particles -->
    <div class="particles" id="particles"></div>

    <!-- Hero Section -->
    <section class="hero" id="about">
        <div class="hero-content fade-in">
            <div class="hero-badge">
                <i class="fas fa-graduation-cap"></i> Ph.D. Candidate
            </div>
            <h1>董骞</h1>
            <p class="subtitle">
                <a href="https://www.cs.tsinghua.edu.cn/" target="_blank" style="color: white; text-decoration: none;">清华大学计算机科学与技术系</a><br>
                <a href="https://ai.thuir.cn/" target="_blank" style="color: white; text-decoration: none;">信息检索实验室 (THUIR)</a>
            </p>
            <div class="hero-intro">
                <p>
                    我目前在清华大学计算机科学与技术系，信息检索实验室（THUIR）进行攻读博士学位，预计2026年6月毕业。
                    很荣幸能够在马少平教授、刘奕群教授和艾清遥教授的指导下进行学术研究。
                    我还担任多个顶级学术会议的审稿人/程序委员会委员。
                </p>
            </div>
            <div class="hero-buttons">
                <a href="#research" class="btn-primary">
                    <i class="fas fa-microscope"></i>
                    研究方向
                </a>
                <a href="#contact" class="btn-primary">
                    <i class="fas fa-envelope"></i>
                    联系我
                </a>
                <a href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&hl=en" target="_blank" class="btn-primary">
                    <i class="fas fa-graduation-cap"></i>
                    Google Scholar
                </a>
                <a href="https://github.com/CSQianDong" target="_blank" class="btn-primary">
                    <i class="fab fa-github"></i>
                    GitHub
                </a>
                <a href="https://www.xiaohongshu.com/user/profile/64d8bdc1000000000100f445" target="_blank" class="btn-primary">
                    <i class="fas fa-heart"></i>
                    小红书
                </a>
            </div>
        </div>
    </section>

    
    <!-- Research Interests -->
    <section class="section" id="research" style="background: #f8fafc;">
        <div class="section-header fade-in">
            <h2 class="section-title">研究方向</h2>
            <p class="section-subtitle">专注于以下三个研究领域的探索与创新</p>
        </div>

        <div class="research-grid">
            <div class="research-card fade-in">
                <div class="research-icon">
                    <i class="fas fa-search"></i>
                </div>
                <h3 class="research-title">信息检索</h3>
                <p class="research-desc">
                    传统和神经网络方法用于检索和重排序，专注于提升检索系统的准确性和效率。
                    探索新的检索算法和优化技术。
                </p>
            </div>

            <div class="research-card fade-in">
                <div class="research-icon">
                    <i class="fas fa-brain"></i>
                </div>
                <h3 class="research-title">大语言模型应用</h3>
                <p class="research-desc">
                    利用信息检索技术来增强大语言模型的能力和效率，探索LLM的新应用场景，
                    提升模型性能和实用性。
                </p>
            </div>

            <div class="research-card fade-in">
                <div class="research-icon">
                    <i class="fas fa-text-width"></i>
                </div>
                <h3 class="research-title">长上下文处理</h3>
                <p class="research-desc">
                    使大语言模型能够高效有效地处理长输入和输出，突破上下文长度限制，
                    提升长文本处理能力。
                </p>
            </div>
        </div>
    </section>

    <!-- Education -->
    <section class="section" id="education" style="background: #f8fafc;">
        <div class="section-header fade-in">
            <h2 class="section-title">教育背景</h2>
        </div>

        <div class="research-grid">
            <div class="research-card fade-in">
                <div class="research-icon">
                    <i class="fas fa-laptop-code"></i>
                </div>
                <h3 class="research-title">工程学士</h3>
                <p class="research-desc">
                    <strong><a href="https://www.scut.edu.cn/sse/" target="_blank">华南理工大学软件学院</a></strong><br>
                    <strong>时间：</strong>2015.08 - 2019.06
                </p>
            </div>

            <div class="research-card fade-in">
                <div class="research-icon">
                    <i class="fas fa-flask"></i>
                </div>
                <h3 class="research-title">工程硕士</h3>
                <p class="research-desc">
                    <strong><a href="http://www.is.cas.cn/" target="_blank">中国科学院软件研究所</a></strong><br>
                    <strong>时间：</strong>2019.08 - 2022.06<br>
                </p>
            </div>

            <div class="research-card fade-in">
                <div class="research-icon">
                    <i class="fas fa-university"></i>
                </div>
                <h3 class="research-title">博士研究生</h3>
                <p class="research-desc">
                    <strong><a href="https://ai.thuir.cn/" target="_blank">清华大学计算机科学与技术系</a></strong><br>
                    <strong>时间：</strong>2022.08 - 至今<br>
                </p>
            </div>
        </div>
    </section>

    <!-- Publications Section -->
    <section class="section" id="publications" style="background: #f8fafc;">
        <div class="section-header fade-in">
            <h2 class="section-title">学术发表</h2>
            <p class="section-subtitle">代表性研究成果</p>
        </div>

        <!-- 主要作者论文 -->
        <div class="publications-container">
            <div class="publication-section">
                <div class="publication-header" onclick="togglePublication('primary-author')">
                    <i class="fas fa-star"></i>
                    <h3>主要作者论文</h3>
                    <i class="fas fa-chevron-down"></i>
                </div>
                <div class="publication-content" id="primary-author">
                    <div class="publication-grid">
                        <div class="publication-item">
                            <div class="publication-year">2025</div>
                            <div class="publication-title">SelfRACG: Enabling LLMs to Self-Express and Retrieve for Code Generation</div>
                            <div class="publication-venue">EMNLP 2025</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-b">CCF-B</span>
                                <span class="tag tag-th-a">TH-A</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2025</div>
                            <div class="publication-title">Qilin: A Multimodal Information Retrieval Dataset with APP-level User Sessions</div>
                            <div class="publication-venue">SIGIR 2025</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-a">CCF-A</span>
                                <span class="tag tag-th-a">TH-A</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2025</div>
                            <div class="publication-title">DecoupledRAG: An Efficient and Effective Retrieval Augmented Generation Framework via Cross Attention</div>
                            <div class="publication-venue">WWW 2025</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-a">CCF-A</span>
                                <span class="tag tag-th-a">TH-A</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2024</div>
                            <div class="publication-title">Unsupervised Large Language Model Alignment for Information Retrieval via Contrastive Feedback</div>
                            <div class="publication-venue">SIGIR 2024</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-a">CCF-A</span>
                                <span class="tag tag-th-a">TH-A</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2023</div>
                            <div class="publication-title">T²Ranking: A Large-scale Chinese Benchmark for Passage Ranking</div>
                            <div class="publication-venue">SIGIR 2023</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-a">CCF-A</span>
                                <span class="tag tag-th-a">TH-A</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2023</div>
                            <div class="publication-title">I³Retriever: Incorporating Implicit Interaction in Pre-trained Language Models for Passage Retrieval</div>
                            <div class="publication-venue">CIKM 2023</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-b">CCF-B</span>
                                <span class="tag tag-th-b">TH-B</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2022</div>
                            <div class="publication-title">Incorporating Explicit Knowledge in Pre-trained Language Models for Passage Re-ranking</div>
                            <div class="publication-venue">SIGIR 2022</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-a">CCF-A</span>
                                <span class="tag tag-th-a">TH-A</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2021</div>
                            <div class="publication-title">Legal Judgment Prediction via Relational Learning</div>
                            <div class="publication-venue">SIGIR 2021</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-a">CCF-A</span>
                                <span class="tag tag-th-a">TH-A</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2021</div>
                            <div class="publication-title">Disentangled Graph Recurrent Network for Document Ranking</div>
                            <div class="publication-venue">Data Science and Engineering (JCR-Q1, IF: 7.2)</div>
                            <div class="publication-tags">
                                <span class="tag tag-jcr-q1">JCR-Q1</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2021</div>
                            <div class="publication-title">Latent Graph Recurrent Network for Document Ranking</div>
                            <div class="publication-venue">DASFAA 2021</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-b">CCF-B</span>
                                <span class="tag tag-th-b">TH-B</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 合作作者论文 -->
            <div class="publication-section">
                <div class="publication-header" onclick="togglePublication('co-author')">
                    <i class="fas fa-users"></i>
                    <h3>合作作者论文</h3>
                    <i class="fas fa-chevron-down"></i>
                </div>
                <div class="publication-content" id="co-author">
                    <div class="publication-grid">
                        <div class="publication-item">
                            <div class="publication-year">2025</div>
                            <div class="publication-title">GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models</div>
                            <div class="publication-venue">Technical Report of Z.ai</div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2025</div>
                            <div class="publication-title">BLADE: Enhancing Black-Box Large Language Models with Small Domain-Specific Models</div>
                            <div class="publication-venue">AAAI 2025</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-a">CCF-A</span>
                                <span class="tag tag-th-a">TH-A</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2025</div>
                            <div class="publication-title">DELTA: Pre-train a Discriminative Encoder for Legal Case Retrieval via Structural Word Alignment</div>
                            <div class="publication-venue">AAAI 2025</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-a">CCF-A</span>
                                <span class="tag tag-th-a">TH-A</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2025</div>
                            <div class="publication-title">CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges</div>
                            <div class="publication-venue">ACL 2025</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-a">CCF-A</span>
                                <span class="tag tag-th-a">TH-A</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2025</div>
                            <div class="publication-title">LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods</div>
                            <div class="publication-venue">Survey</div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2025</div>
                            <div class="publication-title">Dynamic and Parametric Retrieval-Augmented Generation</div>
                            <div class="publication-venue">SIGIR 2025</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-a">CCF-A</span>
                                <span class="tag tag-th-a">TH-A</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2023</div>
                            <div class="publication-title">SAILER: Structure-aware Pre-trained Language Model for Legal Case Retrieval</div>
                            <div class="publication-venue">SIGIR 2023</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-a">CCF-A</span>
                                <span class="tag tag-th-a">TH-A</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2023</div>
                            <div class="publication-title">Incorporating Social-Aware User Preference for Video Recommendation</div>
                            <div class="publication-venue">WISE 2023</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-c">CCF-C</span>
                                <span class="tag tag-th-b">TH-B</span>
                            </div>
                        </div>
                        <div class="publication-item">
                            <div class="publication-year">2019</div>
                            <div class="publication-title">Emotion Recognition Based on Multi-View Body Gestures</div>
                            <div class="publication-venue">ICIP 2019</div>
                            <div class="publication-tags">
                                <span class="tag tag-ccf-c">CCF-C</span>
                                <span class="tag tag-th-b">TH-B</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>


    <!-- Contact Section -->
    <section class="contact" id="contact">
        <div class="section-header fade-in">
            <h2 class="section-title" style="color: white;">联系方式</h2>
        </div>

        <div class="contact-grid">
            <div class="contact-item fade-in">
                <div class="contact-icon">
                    <i class="fas fa-envelope"></i>
                </div>
                <h3 class="contact-title">邮箱</h3>
                <p><a href="mailto:qiandong.97@qq.com">qiandong.97@qq.com</a></p>
            </div>

            <div class="contact-item fade-in">
                <div class="contact-icon">
                    <i class="fab fa-google"></i>
                </div>
                <h3 class="contact-title">Google Scholar</h3>
                <p><a href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&hl=en" target="_blank">谷歌学术</a></p>
            </div>

            <div class="contact-item fade-in">
                <div class="contact-icon">
                    <i class="fab fa-github"></i>
                </div>
                <h3 class="contact-title">GitHub</h3>
                <p><a href="https://github.com/CSQianDong" target="_blank">CSQianDong</a></p>
            </div>
        </div>
    </section>

    <script>
        // Generate floating particles
        function createParticles() {
            const particlesContainer = document.getElementById('particles');
            const particleCount = 50;

            for (let i = 0; i < particleCount; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';

                const size = Math.random() * 4 + 2;
                particle.style.width = size + 'px';
                particle.style.height = size + 'px';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.animationDelay = Math.random() * 20 + 's';
                particle.style.animationDuration = (Math.random() * 20 + 20) + 's';

                particlesContainer.appendChild(particle);
            }
        }

        // Intersection Observer for animations
        function initAnimations() {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.animationPlayState = 'running';
                    }
                });
            }, { threshold: 0.1 });

            document.querySelectorAll('.fade-in').forEach(el => {
                el.style.animationPlayState = 'paused';
                observer.observe(el);
            });
        }

        // Smooth scrolling for navigation links
        function initSmoothScroll() {
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });
        }

        // Navbar scroll effect
        function initNavbar() {
            const navbar = document.querySelector('.navbar');
            let lastScroll = 0;

            window.addEventListener('scroll', () => {
                const currentScroll = window.pageYOffset;

                if (currentScroll > 100) {
                    navbar.style.background = 'rgba(255, 255, 255, 0.98)';
                    navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
                } else {
                    navbar.style.background = 'rgba(255, 255, 255, 0.95)';
                    navbar.style.boxShadow = 'none';
                }

                lastScroll = currentScroll;
            });
        }

        // Toggle publication sections
        function togglePublication(sectionId) {
            const content = document.getElementById(sectionId);
            const header = content.previousElementSibling;
            const icon = header.querySelector('i:last-child');

            content.classList.toggle('active');
            header.classList.toggle('active');
        }

        // Initialize everything when DOM is loaded
        document.addEventListener('DOMContentLoaded', () => {
            createParticles();
            initAnimations();
            initSmoothScroll();
            initNavbar();
        });
    </script>

    <div style="text-align: center; margin-top: 40px; padding-bottom: 20px; color: #666; font-size: 14px;">
      最后更新：{{ site.time | date: "%Y年%m月%d日" }}
    </div>
</body>
</html>