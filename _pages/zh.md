---
permalink: /zh/
title: "董骞 - 中文主页"
excerpt: "董骞个人中文主页，清华大学博士生"
author_profile: false
layout: splash
---

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>董骞 - 清华大学博士生</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }

        .hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 100px 20px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="50" cy="50" r="1" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
            opacity: 0.3;
        }

        .hero-content {
            position: relative;
            z-index: 1;
            max-width: 800px;
            margin: 0 auto;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            font-weight: 700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .hero .subtitle {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }

        .lang-switch {
            margin-top: 2rem;
        }

        .lang-switch a {
            display: inline-block;
            background: rgba(255,255,255,0.2);
            color: white;
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 30px;
            border: 2px solid rgba(255,255,255,0.3);
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }

        .lang-switch a:hover {
            background: rgba(255,255,255,0.3);
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .section {
            background: white;
            margin: 40px 0;
            padding: 60px 40px;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .section:hover {
            transform: translateY(-5px);
        }

        .section h2 {
            color: #667eea;
            font-size: 2.5rem;
            margin-bottom: 2rem;
            text-align: center;
            position: relative;
        }

        .section h2::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 2px;
        }

        .timeline {
            position: relative;
            padding: 20px 0;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            width: 2px;
            height: 100%;
            background: linear-gradient(180deg, #667eea, #764ba2);
        }

        .timeline-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 40px 0;
            position: relative;
        }

        .timeline-item:nth-child(odd) {
            flex-direction: row-reverse;
        }

        .timeline-content {
            width: 45%;
            background: #f8f9fa;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            position: relative;
        }

        .timeline-content::before {
            content: '';
            position: absolute;
            top: 50%;
            width: 20px;
            height: 20px;
            background: #667eea;
            border-radius: 50%;
            transform: translateY(-50%);
        }

        .timeline-item:nth-child(odd) .timeline-content::before {
            right: -60px;
        }

        .timeline-item:nth-child(even) .timeline-content::before {
            left: -60px;
        }

        .timeline-dot {
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            width: 16px;
            height: 16px;
            background: #667eea;
            border-radius: 50%;
            border: 3px solid white;
            z-index: 1;
        }

        .timeline-date {
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }

        .timeline-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 10px;
            color: #333;
        }

        .timeline-desc {
            color: #666;
            line-height: 1.6;
        }

        .research-interests {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .interest-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            transform: perspective(1000px) rotateX(0deg);
            transition: all 0.3s ease;
        }

        .interest-card:hover {
            transform: perspective(1000px) rotateX(-5deg) translateY(-10px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }

        .interest-icon {
            font-size: 3rem;
            margin-bottom: 20px;
        }

        .interest-title {
            font-size: 1.5rem;
            margin-bottom: 15px;
            font-weight: 600;
        }

        .interest-desc {
            opacity: 0.9;
            line-height: 1.6;
        }

        .contact {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
        }

        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .contact-item {
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }

        .contact-item:hover {
            background: rgba(255,255,255,0.2);
            transform: translateY(-5px);
        }

        .contact-icon {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }

        .contact-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 10px;
        }

        .contact-desc {
            opacity: 0.9;
        }

        .contact a {
            color: white;
            text-decoration: none;
            transition: opacity 0.3s ease;
        }

        .contact a:hover {
            opacity: 0.8;
        }

        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }

            .hero .subtitle {
                font-size: 1.2rem;
            }

            .section {
                margin: 20px 0;
                padding: 40px 20px;
            }

            .timeline::before {
                left: 30px;
            }

            .timeline-item {
                flex-direction: column !important;
                align-items: flex-start;
                padding-left: 60px;
            }

            .timeline-content {
                width: 100%;
            }

            .timeline-content::before {
                left: -50px !important;
                right: auto !important;
            }

            .timeline-dot {
                left: 30px;
            }
        }
    </style>
</head>
<body>
    <section class="hero">
        <div class="hero-content">
            <h1>董骞 (Qian Dong)</h1>
            <p class="subtitle">清华大学计算机科学与技术系博士生</p>
            <div class="lang-switch">
                <a href="/">English Version</a>
            </div>
        </div>
    </section>

    <div class="container">
        <section class="section">
            <h2>个人简介</h2>
            <p style="text-align: center; font-size: 1.2rem; line-height: 1.8; max-width: 800px; margin: 0 auto;">
                我目前是清华大学计算机科学与技术系四年级博士生，在清华大学智能信息检索实验室（THUIR）进行学术研究。
                我很荣幸能够在马少平教授、刘奕群教授和艾清遥教授的指导下进行学术研究。
                我的研究方向主要涵盖信息检索、大语言模型应用和长上下文处理等领域。
                我还担任多个顶级学术会议的审稿人/程序委员会委员，包括SIGIR、ACL、WWW、CIKM、COLING、AAAI、TOIS等。
            </p>

            <div class="research-interests">
                <div class="interest-card">
                    <div class="interest-icon">
                        <i class="fas fa-search"></i>
                    </div>
                    <div class="interest-title">信息检索</div>
                    <div class="interest-desc">
                        传统和神经网络方法用于检索和重排序，专注于提升检索系统的准确性和效率。
                    </div>
                </div>

                <div class="interest-card">
                    <div class="interest-icon">
                        <i class="fas fa-brain"></i>
                    </div>
                    <div class="interest-title">大语言模型应用</div>
                    <div class="interest-desc">
                        利用信息检索技术来增强大语言模型的能力和效率，探索LLM的新应用场景。
                    </div>
                </div>

                <div class="interest-card">
                    <div class="interest-icon">
                        <i class="fas fa-text-width"></i>
                    </div>
                    <div class="interest-title">长上下文处理</div>
                    <div class="interest-desc">
                        使大语言模型能够高效有效地处理长输入和输出，突破上下文长度限制。
                    </div>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>教育背景</h2>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-content">
                        <div class="timeline-date">2022.08 - 至今</div>
                        <div class="timeline-title">博士研究生</div>
                        <div class="timeline-desc">
                            清华大学计算机科学与技术系，中国。<br>
                            <strong>导师：</strong>马少平教授、刘奕群教授、艾清遥教授
                        </div>
                    </div>
                    <div class="timeline-dot"></div>
                </div>

                <div class="timeline-item">
                    <div class="timeline-content">
                        <div class="timeline-date">2019.08 - 2022.06</div>
                        <div class="timeline-title">工程硕士</div>
                        <div class="timeline-desc">
                            中国科学院软件研究所，中国。<br>
                            <strong>导师：</strong>牛树梓教授
                        </div>
                    </div>
                    <div class="timeline-dot"></div>
                </div>

                <div class="timeline-item">
                    <div class="timeline-content">
                        <div class="timeline-date">2015.08 - 2019.06</div>
                        <div class="timeline-title">工程学士</div>
                        <div class="timeline-desc">
                            华南理工大学软件学院，中国。
                        </div>
                    </div>
                    <div class="timeline-dot"></div>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>工作经历</h2>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-content">
                        <div class="timeline-date">2024.11 - 至今</div>
                        <div class="timeline-title">研究实习生</div>
                        <div class="timeline-desc">
                            小红书公司，中国。<br>
                            合作导师：陈佳
                        </div>
                    </div>
                    <div class="timeline-dot"></div>
                </div>

                <div class="timeline-item">
                    <div class="timeline-content">
                        <div class="timeline-date">2024.08 - 2024.10</div>
                        <div class="timeline-title">访问学者</div>
                        <div class="timeline-desc">
                            新加坡国立大学，NExT++研究中心，新加坡。<br>
                            合作导师：蔡达成教授
                        </div>
                    </div>
                    <div class="timeline-dot"></div>
                </div>

                <div class="timeline-item">
                    <div class="timeline-content">
                        <div class="timeline-date">2021.07 - 2024.10</div>
                        <div class="timeline-title">研究实习生</div>
                        <div class="timeline-desc">
                            百度公司，搜索科学团队，中国。<br>
                            合作导师：刘一丁
                        </div>
                    </div>
                    <div class="timeline-dot"></div>
                </div>
            </div>
        </section>

        <section class="section contact">
            <h2>联系方式</h2>
            <div class="contact-grid">
                <div class="contact-item">
                    <div class="contact-icon">
                        <i class="fas fa-envelope"></i>
                    </div>
                    <div class="contact-title">邮箱</div>
                    <div class="contact-desc">
                        <a href="mailto:qiandong.97@qq.com">qiandong.97@qq.com</a>
                    </div>
                </div>

                <div class="contact-item">
                    <div class="contact-icon">
                        <i class="fas fa-map-marker-alt"></i>
                    </div>
                    <div class="contact-title">位置</div>
                    <div class="contact-desc">中国北京</div>
                </div>

                <div class="contact-item">
                    <div class="contact-icon">
                        <i class="fab fa-google"></i>
                    </div>
                    <div class="contact-title">Google Scholar</div>
                    <div class="contact-desc">
                        <a href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&hl=en" target="_blank">学术主页</a>
                    </div>
                </div>

                <div class="contact-item">
                    <div class="contact-icon">
                        <i class="fab fa-github"></i>
                    </div>
                    <div class="contact-title">GitHub</div>
                    <div class="contact-desc">
                        <a href="https://github.com/CSQianDong" target="_blank">CSQianDong</a>
                    </div>
                </div>

                <div class="contact-item">
                    <div class="contact-icon">
                        <i class="fas fa-file-alt"></i>
                    </div>
                    <div class="contact-title">中文简历</div>
                    <div class="contact-desc">
                        <a href="https://dongqian.bj.cn/files/chinese_cv.pdf" target="_blank">下载简历</a>
                    </div>
                </div>
            </div>

            <div style="margin-top: 40px;">
                <a href="/" class="lang-switch" style="margin-top: 0;">
                    切换到英文版
                </a>
            </div>
        </section>
    </div>
</body>
</html>