---
permalink: /dm/
title: "Direct Message"
author_profile: false
layout: bare
header: false
sidebar: false
masthead: false
---

<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>DM - Qian Dong</title>
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
        .input-group { margin-bottom: 1.25rem; }
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
        .input-wrapper input, .input-wrapper textarea, .input-wrapper select {
            flex: 1; border: none; outline: none; padding: 0.85rem;
            font-size: 0.95rem; background: var(--card); color: var(--text);
            font-family: inherit; resize: none;
        }
        .input-wrapper input::placeholder, .input-wrapper textarea::placeholder { color: var(--muted); }
        .input-wrapper select { cursor: pointer; -webkit-appearance: none; -moz-appearance: none; appearance: none; }
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
        .optional-label { font-size: 0.75rem; color: var(--muted); font-weight: 400; margin-left: 0.3rem; }
        .required-star { color: var(--error); margin-left: 0.15rem; }
        .privacy-note {
            margin-top: 1.5rem; padding: 0.75rem 1rem; background: var(--bg);
            border-radius: 8px; font-size: 0.8rem; color: var(--muted); line-height: 1.5;
        }
        .privacy-note i { margin-right: 0.3rem; }
    </style>
</head>
<body>

<div class="container">
    <div class="top-bar">
        <button class="theme-toggle" onclick="toggleTheme()" title="Toggle dark mode"><i class="fas fa-moon"></i></button>
    </div>
    <div class="card">
        <div class="header">
            <h1>✉️ Direct Message</h1>
            <p>Want to reach <a href="/">Qian Dong</a>? Leave your info below and I'll get back to you.</p>
        </div>

        <form id="dmForm" onsubmit="return handleSubmit(event)">
            <div class="input-group">
                <label for="dm-name">Name <span class="required-star">*</span></label>
                <div class="input-wrapper">
                    <div class="icon"><i class="fas fa-user"></i></div>
                    <input type="text" id="dm-name" name="name"
                           placeholder="Your name" required autocomplete="name">
                </div>
            </div>

            <div class="input-group">
                <label for="dm-email">Email <span class="required-star">*</span></label>
                <div class="input-wrapper">
                    <div class="icon"><i class="fas fa-envelope"></i></div>
                    <input type="email" id="dm-email" name="email"
                           placeholder="your@email.com" required autocomplete="email">
                </div>
            </div>

            <div class="input-group">
                <label for="dm-wechat">WeChat <span class="optional-label">(optional)</span></label>
                <div class="input-wrapper">
                    <div class="icon"><i class="fab fa-weixin"></i></div>
                    <input type="text" id="dm-wechat" name="wechat"
                           placeholder="WeChat ID" autocomplete="off">
                </div>
            </div>

            <div class="input-group">
                <label for="dm-purpose">Purpose <span class="required-star">*</span></label>
                <div class="input-wrapper">
                    <div class="icon"><i class="fas fa-bullseye"></i></div>
                    <select id="dm-purpose" name="purpose" required>
                        <option value="" disabled selected>Select a purpose</option>
                        <option value="Academic Collaboration">Academic Collaboration</option>
                        <option value="Industry Opportunity">Industry Opportunity</option>
                        <option value="Research Discussion">Research Discussion</option>
                        <option value="Other">Other</option>
                    </select>
                </div>
            </div>

            <div class="input-group">
                <label for="dm-message">Message <span class="optional-label">(optional)</span></label>
                <div class="input-wrapper">
                    <div class="icon"><i class="fas fa-comment-dots"></i></div>
                    <textarea id="dm-message" name="message" rows="3"
                              placeholder="Anything you'd like to say..."></textarea>
                </div>
            </div>

            <button type="submit" class="btn" id="submitBtn">
                <i class="fas fa-paper-plane"></i>&nbsp; Send Message
            </button>
        </form>
        <div class="msg" id="msg"></div>

        <div class="privacy-note">
            <i class="fas fa-lock"></i> Your information is sent securely and will only be used to get in touch with you.
        </div>
    </div>

    <div class="footer">
        <a href="/">← Back to homepage</a>
    </div>
</div>

<script>
var FEISHU_WEBHOOK = 'https://open.feishu.cn/open-apis/bot/v2/hook/365126e4-aaae-4ff6-9e2a-2a6820d7bcee';
var COOLDOWN_KEY = 'dm_last_submit';
var COOLDOWN_MS = 3600000; // 1 hour cooldown

function handleSubmit(e) {
    e.preventDefault();
    var btn = document.getElementById('submitBtn');
    var msg = document.getElementById('msg');

    var name = document.getElementById('dm-name').value.trim();
    var email = document.getElementById('dm-email').value.trim();
    var wechat = document.getElementById('dm-wechat').value.trim();
    var purpose = document.getElementById('dm-purpose').value;
    var message = document.getElementById('dm-message').value.trim();

    if (!name || !email || !purpose) {
        msg.className = 'msg error';
        msg.textContent = '❌ Please fill in all required fields.';
        return false;
    }

    // Simple email validation
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        msg.className = 'msg error';
        msg.textContent = '❌ Please enter a valid email address.';
        return false;
    }

    // Rate limit: 1 message per hour
    var lastSubmit = parseInt(localStorage.getItem(COOLDOWN_KEY) || '0');
    if (Date.now() - lastSubmit < COOLDOWN_MS) {
        var minutesLeft = Math.ceil((COOLDOWN_MS - (Date.now() - lastSubmit)) / 60000);
        msg.className = 'msg error';
        msg.textContent = '⏳ Please wait ' + minutesLeft + ' min before sending another message.';
        return false;
    }

    btn.disabled = true;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>&nbsp; Sending...';
    msg.textContent = '';

    var fields = [
        '**👤 Name：**' + name,
        '**📧 Email：**' + email
    ];
    if (wechat) fields.push('**💬 WeChat：**' + wechat);
    fields.push('**🎯 Purpose：**' + purpose);
    if (message) fields.push('**📝 Message：**\n' + message);
    fields.push('**🕐 Time：**' + new Date().toLocaleString('en-US', { timeZone: 'Asia/Shanghai' }) + ' (CST)');

    var payload = {
        msg_type: 'interactive',
        card: {
            header: {
                title: { tag: 'plain_text', content: '✉️ New DM — ' + purpose },
                template: 'green'
            },
            elements: [
                {
                    tag: 'div',
                    text: {
                        tag: 'lark_md',
                        content: fields.join('\n')
                    }
                },
                {
                    tag: 'action',
                    actions: [
                        {
                            tag: 'button',
                            text: { tag: 'plain_text', content: '📧 Reply via Email' },
                            url: 'mailto:' + email + '?subject=Re: ' + encodeURIComponent(purpose),
                            type: 'primary'
                        }
                    ]
                }
            ]
        }
    };

    fetch(FEISHU_WEBHOOK, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    }).then(function(resp) {
        return resp.json();
    }).then(function(data) {
        if (data.code === 0 || data.StatusCode === 0) {
            localStorage.setItem(COOLDOWN_KEY, Date.now().toString());
            msg.className = 'msg success';
            msg.textContent = '✅ Message sent! I\'ll get back to you soon 🎉';
            document.getElementById('dmForm').reset();
            setTimeout(function() { msg.textContent = ''; }, 5000);
        } else {
            msg.className = 'msg error';
            msg.textContent = '❌ Failed to send. Please try again later.';
            console.error('Feishu webhook error:', data);
        }
    }).catch(function(err) {
        msg.className = 'msg error';
        msg.textContent = '❌ Network error. Please check your connection.';
        console.error('Network error:', err);
    }).finally(function() {
        btn.disabled = false;
        btn.innerHTML = '<i class="fas fa-paper-plane"></i>&nbsp; Send Message';
    });

    return false;
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
})();
</script>

</body>
</html>
