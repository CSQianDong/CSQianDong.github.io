---
permalink: /submit/
title: "论文投稿"
author_profile: false
layout: bare
header: false
sidebar: false
masthead: false
---

<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>论文投稿 - 董骞</title>
    <link rel="icon" href="/images/icon.png" type="image/x-icon">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #f7f7f8;
            --text: #1a1a2e;
            --theme: #4a6fa5;
            --hover: #3a5a8c;
            --divider: #e5e7eb;
            --muted: #6b7280;
            --card: #ffffff;
            --success: #22c55e;
            --error: #ef4444;
        }
        [data-theme="dark"] {
            --bg: #1a1a2e;
            --text: #e0e0e8;
            --theme: #7b9fd4;
            --hover: #a3c0e8;
            --divider: #2e2e45;
            --muted: #9a9ab0;
            --card: #22223a;
            --success: #4ade80;
            --error: #f87171;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', -apple-system, sans-serif;
            background: var(--bg); color: var(--text);
            min-height: 100vh; display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            transition: background-color 0.3s, color 0.3s;
            padding: 2rem;
        }
        .container { max-width: 520px; width: 100%; }
        .card {
            background: var(--card); border-radius: 16px;
            padding: 2.5rem; box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border: 1px solid var(--divider);
        }
        .header { text-align: center; margin-bottom: 2rem; }
        .header h1 { font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem; }
        .header p { color: var(--muted); font-size: 0.9rem; line-height: 1.6; }
        .header a { color: var(--theme); text-decoration: none; }
        .header a:hover { color: var(--hover); }
        .input-group { margin-bottom: 1.5rem; }
        .input-group label { display: block; font-size: 0.85rem; font-weight: 600; margin-bottom: 0.5rem; color: var(--text); }
        .input-wrapper {
            display: flex; border: 2px solid var(--divider); border-radius: 10px;
            overflow: hidden; transition: border-color 0.2s;
        }
        .input-wrapper:focus-within { border-color: var(--theme); }
        .input-wrapper .icon {
            display: flex; align-items: center; justify-content: center;
            width: 48px; background: var(--bg); color: var(--muted); font-size: 1rem; flex-shrink: 0;
        }
        .input-wrapper input {
            flex: 1; border: none; outline: none; padding: 0.85rem;
            font-size: 0.95rem; background: var(--card); color: var(--text);
            font-family: inherit;
        }
        .input-wrapper input::placeholder { color: var(--muted); }
        .btn {
            width: 100%; padding: 0.9rem; border: none; border-radius: 10px;
            background: var(--theme); color: #fff; font-size: 1rem; font-weight: 600;
            cursor: pointer; transition: all 0.2s; font-family: inherit;
        }
        .btn:hover { background: var(--hover); transform: translateY(-1px); }
        .btn:active { transform: translateY(0); }
        .btn:disabled { opacity: 0.6; cursor: not-allowed; transform: none; }
        .msg { text-align: center; margin-top: 1rem; font-size: 0.9rem; min-height: 1.5em; }
        .msg.success { color: var(--success); }
        .msg.error { color: var(--error); }
        .recent { margin-top: 2rem; }
        .recent h3 { font-size: 0.9rem; font-weight: 600; margin-bottom: 0.75rem; color: var(--muted); }
        .recent-list { list-style: none; }
        .recent-list li {
            padding: 0.6rem 0; border-bottom: 1px solid var(--divider);
            font-size: 0.85rem; color: var(--muted); display: flex; justify-content: space-between; align-items: center;
        }
        .recent-list li:last-child { border-bottom: none; }
        .recent-list .arxiv-id { color: var(--theme); font-weight: 500; }
        .recent-list .time { font-size: 0.75rem; }
        .footer {
            text-align: center; margin-top: 2rem; font-size: 0.8rem; color: var(--muted);
        }
        .footer a { color: var(--theme); text-decoration: none; }
        .top-bar {
            display: flex; justify-content: flex-end; margin-bottom: 1rem;
        }
        .theme-toggle {
            width: 36px; height: 36px; border-radius: 50%;
            border: 1px solid var(--divider); background: transparent;
            color: var(--muted); cursor: pointer; font-size: 1.1rem;
            display: flex; align-items: center; justify-content: center;
            transition: all 0.3s;
        }
        .theme-toggle:hover { color: var(--theme); border-color: var(--theme); }
        .count-badge {
            display: inline-block; background: var(--theme); color: #fff;
            font-size: 0.7rem; font-weight: 700; padding: 0.15rem 0.5rem;
            border-radius: 10px; margin-left: 0.5rem;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="top-bar">
        <button class="theme-toggle" onclick="toggleTheme()" title="切换深色模式"><i class="fas fa-moon"></i></button>
    </div>
    <div class="card">
        <div class="header">
            <h1>📄 论文投稿</h1>
            <p>欢迎向 <a href="https://www.xiaohongshu.com/user/profile/64d8bdc1000000000100f445" target="_blank">🎃量子之心</a> 投稿！<br>
            粘贴 arXiv 链接，我会尽快解读分享 ✨</p>
        </div>

        <form id="submitForm" onsubmit="return handleSubmit(event)">
            <div class="input-group">
                <label for="arxiv-url">arXiv 论文链接</label>
                <div class="input-wrapper">
                    <div class="icon"><i class="fas fa-link"></i></div>
                    <input type="text" id="arxiv-url" name="url"
                           placeholder="https://arxiv.org/abs/2401.12345"
                           required autocomplete="off">
                </div>
            </div>
            <button type="submit" class="btn" id="submitBtn">
                <i class="fas fa-paper-plane"></i>&nbsp; 提交投稿
            </button>
        </form>
        <div class="msg" id="msg"></div>

        <div class="recent" id="recentSection" style="display:none;">
            <h3>📋 最近投稿 <span class="count-badge" id="countBadge">0</span></h3>
            <ul class="recent-list" id="recentList"></ul>
        </div>
    </div>

    <div class="footer">
        <a href="/">← 返回主页</a>
    </div>
</div>

<script>
// LocalStorage based submission (no backend needed, data stored in browser)
// The actual collection happens via Google Form hidden iframe
var GOOGLE_FORM_URL = '';  // Will be set after creating Google Form
var STORAGE_KEY = 'arxiv_submissions';

function getSubmissions() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]'); } catch(e) { return []; }
}

function saveSubmission(url) {
    var subs = getSubmissions();
    var match = url.match(/(\d{4}\.\d{4,5})/);
    subs.unshift({ id: match ? match[1] : url, url: url, time: new Date().toLocaleString('zh-CN') });
    if (subs.length > 10) subs = subs.slice(0, 10);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(subs));
    renderRecent();
}

function renderRecent() {
    var subs = getSubmissions();
    var section = document.getElementById('recentSection');
    var list = document.getElementById('recentList');
    var badge = document.getElementById('countBadge');
    if (subs.length === 0) { section.style.display = 'none'; return; }
    section.style.display = 'block';
    badge.textContent = subs.length;
    list.innerHTML = subs.map(function(s) {
        return '<li><span class="arxiv-id">' + s.id + '</span><span class="time">' + s.time + '</span></li>';
    }).join('');
}

function validateArxiv(url) {
    url = url.trim();
    // Accept various arxiv URL formats and plain IDs
    return /arxiv\.org\/(abs|pdf|html)\/\d{4}\.\d{4,5}/i.test(url) ||
           /^\d{4}\.\d{4,5}(v\d+)?$/.test(url);
}

function normalizeUrl(url) {
    url = url.trim();
    if (/^\d{4}\.\d{4,5}/.test(url)) return 'https://arxiv.org/abs/' + url;
    return url;
}

function handleSubmit(e) {
    e.preventDefault();
    var input = document.getElementById('arxiv-url');
    var btn = document.getElementById('submitBtn');
    var msg = document.getElementById('msg');
    var url = input.value.trim();

    if (!validateArxiv(url)) {
        msg.className = 'msg error';
        msg.textContent = '❌ 请输入有效的 arXiv 链接，如 https://arxiv.org/abs/2401.12345';
        return false;
    }

    url = normalizeUrl(url);
    btn.disabled = true;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>&nbsp; 提交中...';

    // Submit via Google Form (if configured) or just save locally
    if (GOOGLE_FORM_URL) {
        submitToGoogleForm(url);
    }

    // Always save locally and show success
    setTimeout(function() {
        saveSubmission(url);
        msg.className = 'msg success';
        msg.textContent = '✅ 投稿成功！感谢你的推荐 🎉';
        input.value = '';
        btn.disabled = false;
        btn.innerHTML = '<i class="fas fa-paper-plane"></i>&nbsp; 提交投稿';
        setTimeout(function() { msg.textContent = ''; }, 3000);
    }, 500);

    return false;
}

function submitToGoogleForm(url) {
    if (!GOOGLE_FORM_URL) return;
    var iframe = document.createElement('iframe');
    iframe.name = 'hidden_iframe';
    iframe.style.display = 'none';
    document.body.appendChild(iframe);

    var form = document.createElement('form');
    form.method = 'POST';
    form.action = GOOGLE_FORM_URL;
    form.target = 'hidden_iframe';
    var input = document.createElement('input');
    input.name = 'entry.0';  // Will update with actual field ID
    input.value = url;
    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();

    setTimeout(function() {
        document.body.removeChild(form);
        document.body.removeChild(iframe);
    }, 2000);
}

// Theme toggle (synced with main site)
function toggleTheme() {
    var html = document.documentElement;
    var btn = document.querySelector('.theme-toggle i');
    if (html.getAttribute('data-theme') === 'dark') {
        html.removeAttribute('data-theme');
        btn.className = 'fas fa-moon';
        localStorage.setItem('theme', 'light');
    } else {
        html.setAttribute('data-theme', 'dark');
        btn.className = 'fas fa-sun';
        localStorage.setItem('theme', 'dark');
    }
}
(function() {
    var saved = localStorage.getItem('theme');
    if (saved === 'dark' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.setAttribute('data-theme', 'dark');
        document.addEventListener('DOMContentLoaded', function() {
            var btn = document.querySelector('.theme-toggle i');
            if (btn) btn.className = 'fas fa-sun';
        });
    }
    renderRecent();
})();
</script>

</body>
</html>
