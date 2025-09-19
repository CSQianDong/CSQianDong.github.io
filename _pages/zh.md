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

        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px) rotateX(0deg); }
            50% { transform: translateY(-10px) rotateX(2deg); }
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
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.05));
            color: white;
            padding: 1rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(255, 255, 255, 0.2);
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            position: relative;
            overflow: hidden;
            box-shadow:
                0 8px 32px rgba(0, 0, 0, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
        }

        .btn-primary::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
            transition: left 0.6s ease;
        }

        .btn-primary:hover::before {
            left: 100%;
        }

        .btn-primary:hover {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.25), rgba(255, 255, 255, 0.1));
            transform: translateY(-5px) scale(1.02);
            box-shadow:
                0 20px 40px rgba(0, 0, 0, 0.3),
                0 0 30px rgba(99, 102, 241, 0.4),
                inset 0 1px 0 rgba(255, 255, 255, 0.3);
            border-color: rgba(255, 255, 255, 0.4);
        }

        .btn-primary:active {
            transform: translateY(-2px) scale(0.98);
        }

        /* Neon glow effect for buttons */
        .btn-primary.neon {
            border-color: rgba(99, 102, 241, 0.6);
            box-shadow:
                0 8px 32px rgba(0, 0, 0, 0.1),
                0 0 20px rgba(99, 102, 241, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
        }

        .btn-primary.neon:hover {
            box-shadow:
                0 20px 40px rgba(0, 0, 0, 0.3),
                0 0 40px rgba(99, 102, 241, 0.6),
                0 0 60px rgba(147, 51, 234, 0.4),
                inset 0 1px 0 rgba(255, 255, 255, 0.3);
            animation: neonPulse 2s ease-in-out infinite alternate;
        }

        @keyframes neonPulse {
            from {
                box-shadow:
                    0 20px 40px rgba(0, 0, 0, 0.3),
                    0 0 40px rgba(99, 102, 241, 0.6),
                    0 0 60px rgba(147, 51, 234, 0.4),
                    inset 0 1px 0 rgba(255, 255, 255, 0.3);
            }
            to {
                box-shadow:
                    0 20px 40px rgba(0, 0, 0, 0.3),
                    0 0 50px rgba(99, 102, 241, 0.8),
                    0 0 80px rgba(147, 51, 234, 0.6),
                    inset 0 1px 0 rgba(255, 255, 255, 0.3);
            }
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
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.7));
            backdrop-filter: blur(20px);
            padding: 2rem;
            border-radius: 20px;
            box-shadow:
                0 10px 30px rgba(0, 0, 0, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.3);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 1px solid rgba(255, 255, 255, 0.2);
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
            background: linear-gradient(90deg, #6366f1, #8b5cf6, #ec4899);
            transform: scaleX(0);
            transition: transform 0.4s ease;
            border-radius: 2px;
        }

        .research-card::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.1) 0%, transparent 70%);
            opacity: 0;
            transition: opacity 0.4s ease;
            pointer-events: none;
        }

        .research-card:hover {
            transform: translateY(-15px) scale(1.02);
            box-shadow:
                0 25px 50px rgba(0, 0, 0, 0.2),
                0 0 30px rgba(99, 102, 241, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.4);
            border-color: rgba(99, 102, 241, 0.3);
        }

        .research-card:hover::before {
            transform: scaleX(1);
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.6);
        }

        .research-card:hover::after {
            opacity: 1;
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
            position: relative;
            overflow: hidden;
            box-shadow:
                0 8px 25px rgba(99, 102, 241, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .research-icon::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.3), transparent);
            transform: translateX(-100%);
            transition: transform 0.6s ease;
        }

        .research-card:hover .research-icon {
            transform: scale(1.1) rotate(5deg);
            box-shadow:
                0 15px 35px rgba(99, 102, 241, 0.4),
                0 0 25px rgba(99, 102, 241, 0.5),
                inset 0 1px 0 rgba(255, 255, 255, 0.3);
        }

        .research-card:hover .research-icon::before {
            transform: translateX(100%);
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
            background: transparent;
            padding: 2.5rem 2rem;
            border-radius: 20px;
            text-align: center;
            backdrop-filter: blur(0px);
            border: 1px solid transparent;
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            cursor: pointer;
            position: relative;
            overflow: hidden;
            box-shadow: none;
        }

        .contact-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transform: translateX(-100%);
            transition: transform 0.6s;
        }

        .contact-item:hover::before {
            transform: translateX(100%);
        }

        .contact-item:hover {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1));
            backdrop-filter: blur(20px);
            border-color: rgba(255, 255, 255, 0.3);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
            transform: translateY(-8px) scale(1.02);
        }

        .contact-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            opacity: 0.7;
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            filter: drop-shadow(0 0px 0px rgba(0, 0, 0, 0));
        }

        .contact-item:hover .contact-icon {
            margin-bottom: 0.5rem;
            transform: scale(1.15);
            opacity: 1;
            filter: drop-shadow(0 6px 12px rgba(0, 0, 0, 0.3));
        }

        .contact-title {
            font-size: 1.125rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        }

        .contact-item:hover .contact-title {
            opacity: 1;
            transform: translateY(0);
        }

        .contact-item p {
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) 0.1s;
            font-weight: 500;
        }

        .contact-item:hover p {
            opacity: 1;
            transform: translateY(0);
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

        /* Enhanced Particles System */
        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
            overflow: hidden;
        }

        .particle {
            position: absolute;
            border-radius: 50%;
            pointer-events: none;
            mix-blend-mode: screen;
            transition: all 0.3s ease;
        }

        .particle-basic {
            background: rgba(255, 255, 255, 0.3);
            animation: floatBasic linear infinite;
        }

        .particle-interactive {
            background: radial-gradient(circle, rgba(99, 102, 241, 0.6) 0%, rgba(99, 102, 241, 0) 70%);
            animation: floatInteractive linear infinite;
            cursor: none;
        }

        .particle-glow {
            background: radial-gradient(circle, rgba(147, 51, 234, 0.4) 0%, rgba(147, 51, 234, 0) 60%);
            box-shadow: 0 0 15px rgba(147, 51, 234, 0.3);
            animation: floatGlow ease-in-out infinite;
        }

        .particle-mouse {
            position: fixed;
            width: 8px;
            height: 8px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.8) 0%, rgba(99, 102, 241, 0) 70%);
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            mix-blend-mode: screen;
            transition: transform 0.1s ease;
        }

        @keyframes floatBasic {
            from {
                transform: translateY(100vh) translateX(0) scale(0);
                opacity: 0;
            }
            10% {
                opacity: 0.6;
                transform: translateY(90vh) translateX(10px) scale(1);
            }
            90% {
                opacity: 0.6;
                transform: translateY(10vh) translateX(80px) scale(1);
            }
            to {
                transform: translateY(-100vh) translateX(100px) scale(0);
                opacity: 0;
            }
        }

        @keyframes floatInteractive {
            0% {
                transform: translateY(100vh) translateX(0) rotate(0deg) scale(0);
                opacity: 0;
            }
            10% {
                opacity: 0.8;
                transform: translateY(90vh) translateX(20px) rotate(72deg) scale(1);
            }
            25% {
                transform: translateY(75vh) translateX(-30px) rotate(144deg) scale(1.2);
            }
            50% {
                transform: translateY(50vh) translateX(40px) rotate(216deg) scale(0.8);
            }
            75% {
                transform: translateY(25vh) translateX(-20px) rotate(288deg) scale(1.1);
            }
            90% {
                opacity: 0.8;
                transform: translateY(10vh) translateX(30px) rotate(360deg) scale(1);
            }
            100% {
                transform: translateY(-100vh) translateX(60px) rotate(432deg) scale(0);
                opacity: 0;
            }
        }

        @keyframes floatGlow {
            0%, 100% {
                transform: translateY(0) translateX(0) scale(1);
                opacity: 0.3;
            }
            25% {
                transform: translateY(-20px) translateX(15px) scale(1.1);
                opacity: 0.5;
            }
            50% {
                transform: translateY(-10px) translateX(-10px) scale(0.9);
                opacity: 0.4;
            }
            75% {
                transform: translateY(-30px) translateX(20px) scale(1.05);
                opacity: 0.45;
            }
        }

        /* Connection lines for nearby particles */
        .particle-connection {
            position: absolute;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.2), transparent);
            transform-origin: left center;
            pointer-events: none;
            z-index: 2;
            opacity: 0;
            transition: opacity 0.3s ease;
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
                    我目前在清华大学计算机科学与技术系，信息检索实验室（THUIR）攻读博士学位，预计2026年6月毕业。
                    很荣幸能够在马少平教授、刘奕群教授和艾清遥教授的指导下进行学术研究。
                    我还担任多个顶级学术会议的审稿人/程序委员会委员。
                </p>
            </div>
            <div class="hero-buttons">
                <a href="#research" class="btn-primary neon">
                    <i class="fas fa-microscope"></i>
                    研究方向
                </a>
                <a href="#contact" class="btn-primary neon">
                    <i class="fas fa-envelope"></i>
                    联系我
                </a>
                <a href="https://scholar.google.com/citations?user=m88SZGgAAAAJ&hl=en" target="_blank" class="btn-primary neon">
                    <i class="fas fa-graduation-cap"></i>
                    Google Scholar
                </a>
                <a href="https://github.com/CSQianDong" target="_blank" class="btn-primary neon">
                    <i class="fab fa-github"></i>
                    GitHub
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
                    <i class="fas fa-envelope" style="font-size: 2.5rem;"></i>
                </div>
                <p><a href="mailto:qiandong.97@qq.com">qiandong.97@qq.com</a></p>
            </div>

            <div class="contact-item fade-in">
                <div class="contact-icon">
                    <img src="/images/xhs.png" alt="小红书" style="width: 50px; height: 50px; border-radius: 50%;">
                </div>
                <p><a href="https://www.xiaohongshu.com/user/profile/64d8bdc1000000000100f445" target="_blank">🎃量子之心</a></p>
            </div>

            <div class="contact-item fade-in">
                <div class="contact-icon">
                    <svg style="width: 40px; height: 40px; fill: white;" viewBox="0 0 24 24">
                        <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                    </svg>
                </div>
                <p><a href="https://x.com/verymakesense" target="_blank">@verymakesense</a></p>
            </div>
        </div>
    </section>

    <script>
        // Enhanced Interactive Particles System
        function createParticles() {
            const particlesContainer = document.getElementById('particles');
            const particles = [];
            const mouseParticle = document.createElement('div');
            mouseParticle.className = 'particle-mouse';
            document.body.appendChild(mouseParticle);

            // Create different types of particles
            const particleConfigs = [
                { type: 'basic', count: 30, sizeRange: [2, 5], speedRange: [15, 25] },
                { type: 'interactive', count: 15, sizeRange: [6, 12], speedRange: [20, 35] },
                { type: 'glow', count: 8, sizeRange: [8, 16], speedRange: [8, 15] }
            ];

            particleConfigs.forEach(config => {
                for (let i = 0; i < config.count; i++) {
                    const particle = document.createElement('div');
                    particle.className = `particle particle-${config.type}`;

                    const size = Math.random() * (config.sizeRange[1] - config.sizeRange[0]) + config.sizeRange[0];
                    particle.style.width = size + 'px';
                    particle.style.height = size + 'px';
                    particle.style.left = Math.random() * 100 + '%';
                    particle.style.animationDelay = Math.random() * config.speedRange[1] + 's';
                    particle.style.animationDuration = (Math.random() * (config.speedRange[1] - config.speedRange[0]) + config.speedRange[0]) + 's';

                    particlesContainer.appendChild(particle);
                    particles.push({
                        element: particle,
                        x: parseFloat(particle.style.left),
                        y: Math.random() * 100,
                        vx: (Math.random() - 0.5) * 0.5,
                        vy: (Math.random() - 0.5) * 0.5,
                        size: size
                    });
                }
            });

            // Mouse interaction
            let mouseX = 0;
            let mouseY = 0;
            let isMouseMoving = false;
            let mouseTimeout;

            document.addEventListener('mousemove', (e) => {
                mouseX = e.clientX;
                mouseY = e.clientY;
                isMouseMoving = true;

                // Update mouse particle position
                mouseParticle.style.left = mouseX - 4 + 'px';
                mouseParticle.style.top = mouseY - 4 + 'px';

                clearTimeout(mouseTimeout);
                mouseTimeout = setTimeout(() => {
                    isMouseMoving = false;
                    mouseParticle.style.transform = 'scale(0)';
                }, 100);

                // Interact with nearby particles
                particles.forEach(particle => {
                    const rect = particle.element.getBoundingClientRect();
                    const particleX = rect.left + rect.width / 2;
                    const particleY = rect.top + rect.height / 2;

                    const distance = Math.sqrt(
                        Math.pow(mouseX - particleX, 2) +
                        Math.pow(mouseY - particleY, 2)
                    );

                    if (distance < 100) {
                        const force = (100 - distance) / 100;
                        const angle = Math.atan2(particleY - mouseY, particleX - mouseX);

                        particle.element.style.transform = `translate(${Math.cos(angle) * force * 20}px, ${Math.sin(angle) * force * 20}px) scale(${1 + force * 0.5})`;
                        particle.element.style.opacity = Math.min(1, parseFloat(particle.element.style.opacity || 0.6) + force * 0.4);

                        // Create connection lines
                        if (distance < 80 && Math.random() > 0.7) {
                            createConnectionLine(mouseX, mouseY, particleX, particleY, force);
                        }
                    } else {
                        particle.element.style.transform = '';
                        particle.element.style.opacity = '';
                    }
                });
            });

            // Create connection lines between particles
            function createConnectionLine(x1, y1, x2, y2, opacity) {
                const line = document.createElement('div');
                line.className = 'particle-connection';

                const distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
                const angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;

                line.style.width = distance + 'px';
                line.style.left = x1 + 'px';
                line.style.top = y1 + 'px';
                line.style.transform = `rotate(${angle}deg)`;
                line.style.opacity = opacity * 0.6;

                document.body.appendChild(line);

                setTimeout(() => {
                    line.style.opacity = '0';
                    setTimeout(() => line.remove(), 300);
                }, 100);
            }

            // Particle collision detection
            function updateParticles() {
                particles.forEach((particle, i) => {
                    particles.forEach((otherParticle, j) => {
                        if (i !== j) {
                            const dx = particle.x - otherParticle.x;
                            const dy = particle.y - otherParticle.y;
                            const distance = Math.sqrt(dx * dx + dy * dy);

                            if (distance < 5) {
                                const force = (5 - distance) / 5;
                                particle.vx += dx * force * 0.01;
                                particle.vy += dy * force * 0.01;
                            }
                        }
                    });

                    // Update position
                    particle.x += particle.vx;
                    particle.y += particle.vy;

                    // Boundary check
                    if (particle.x < 0 || particle.x > 100) particle.vx *= -1;
                    if (particle.y < 0 || particle.y > 100) particle.vy *= -1;

                    // Apply friction
                    particle.vx *= 0.99;
                    particle.vy *= 0.99;
                });

                requestAnimationFrame(updateParticles);
            }

            updateParticles();
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