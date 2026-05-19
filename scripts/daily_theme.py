#!/usr/bin/env python3
"""
Daily Theme Switcher for CSQianDong.github.io
Automatically changes the homepage color theme based on the day of the week.
Runs via GitHub Actions cron every day.
"""

import re
import datetime
import sys
import os

# 7 themes for each day of the week (Monday=0 ... Sunday=6)
THEMES = {
    0: {  # Monday - Ocean Blue
        "name": "Ocean Blue",
        "light": {
            "--global-bg-color": "#f8f9fc",
            "--global-text-color": "#1a1a2e",
            "--global-theme-color": "#4a6fa5",
            "--global-hover-color": "#3a5a8c",
            "--global-divider-color": "#e5e7eb",
            "--global-muted": "#6b7280",
            "--global-card-bg": "#ffffff",
            "--global-accent": "#6366f1",
            "--global-accent-2": "#8b5cf6",
            "--global-glow": "rgba(74, 111, 165, 0.15)",
        },
        "dark": {
            "--global-bg-color": "#0f0f1a",
            "--global-text-color": "#e0e0e8",
            "--global-theme-color": "#7b9fd4",
            "--global-hover-color": "#a3c0e8",
            "--global-divider-color": "#1e1e35",
            "--global-muted": "#9a9ab0",
            "--global-card-bg": "#1a1a2e",
            "--global-accent": "#818cf8",
            "--global-accent-2": "#a78bfa",
            "--global-glow": "rgba(123, 159, 212, 0.1)",
        },
    },
    1: {  # Tuesday - Emerald Green
        "name": "Emerald Green",
        "light": {
            "--global-bg-color": "#f6faf8",
            "--global-text-color": "#1a2e24",
            "--global-theme-color": "#059669",
            "--global-hover-color": "#047857",
            "--global-divider-color": "#d1e7dd",
            "--global-muted": "#5f7a6e",
            "--global-card-bg": "#ffffff",
            "--global-accent": "#10b981",
            "--global-accent-2": "#34d399",
            "--global-glow": "rgba(5, 150, 105, 0.12)",
        },
        "dark": {
            "--global-bg-color": "#0a1410",
            "--global-text-color": "#d4e8de",
            "--global-theme-color": "#34d399",
            "--global-hover-color": "#6ee7b7",
            "--global-divider-color": "#1a2e24",
            "--global-muted": "#7da393",
            "--global-card-bg": "#12201a",
            "--global-accent": "#10b981",
            "--global-accent-2": "#059669",
            "--global-glow": "rgba(52, 211, 153, 0.08)",
        },
    },
    2: {  # Wednesday - Sunset Orange
        "name": "Sunset Orange",
        "light": {
            "--global-bg-color": "#fffaf6",
            "--global-text-color": "#2e1f1a",
            "--global-theme-color": "#e85d04",
            "--global-hover-color": "#c44d03",
            "--global-divider-color": "#f5e6d3",
            "--global-muted": "#7a6455",
            "--global-card-bg": "#ffffff",
            "--global-accent": "#f97316",
            "--global-accent-2": "#fb923c",
            "--global-glow": "rgba(232, 93, 4, 0.1)",
        },
        "dark": {
            "--global-bg-color": "#14100c",
            "--global-text-color": "#f0e0d4",
            "--global-theme-color": "#fb923c",
            "--global-hover-color": "#fdba74",
            "--global-divider-color": "#2e2218",
            "--global-muted": "#b89a82",
            "--global-card-bg": "#1e1610",
            "--global-accent": "#f97316",
            "--global-accent-2": "#e85d04",
            "--global-glow": "rgba(251, 146, 60, 0.08)",
        },
    },
    3: {  # Thursday - Royal Purple
        "name": "Royal Purple",
        "light": {
            "--global-bg-color": "#faf8ff",
            "--global-text-color": "#1e1a2e",
            "--global-theme-color": "#7c3aed",
            "--global-hover-color": "#6d28d9",
            "--global-divider-color": "#e8e0f5",
            "--global-muted": "#6e5f8a",
            "--global-card-bg": "#ffffff",
            "--global-accent": "#8b5cf6",
            "--global-accent-2": "#a78bfa",
            "--global-glow": "rgba(124, 58, 237, 0.1)",
        },
        "dark": {
            "--global-bg-color": "#0e0a18",
            "--global-text-color": "#e4dff0",
            "--global-theme-color": "#a78bfa",
            "--global-hover-color": "#c4b5fd",
            "--global-divider-color": "#231e35",
            "--global-muted": "#9a8cb5",
            "--global-card-bg": "#16112a",
            "--global-accent": "#8b5cf6",
            "--global-accent-2": "#7c3aed",
            "--global-glow": "rgba(167, 139, 250, 0.08)",
        },
    },
    4: {  # Friday - Rose Pink
        "name": "Rose Pink",
        "light": {
            "--global-bg-color": "#fdf6f9",
            "--global-text-color": "#2e1a22",
            "--global-theme-color": "#e11d7b",
            "--global-hover-color": "#be185d",
            "--global-divider-color": "#f5d5e3",
            "--global-muted": "#7a5568",
            "--global-card-bg": "#ffffff",
            "--global-accent": "#f43f7a",
            "--global-accent-2": "#fb7185",
            "--global-glow": "rgba(225, 29, 123, 0.1)",
        },
        "dark": {
            "--global-bg-color": "#140a10",
            "--global-text-color": "#f0d4e0",
            "--global-theme-color": "#fb7185",
            "--global-hover-color": "#fda4af",
            "--global-divider-color": "#2e1a22",
            "--global-muted": "#b88296",
            "--global-card-bg": "#1e1018",
            "--global-accent": "#f43f7a",
            "--global-accent-2": "#e11d7b",
            "--global-glow": "rgba(251, 113, 133, 0.08)",
        },
    },
    5: {  # Saturday - Golden Amber
        "name": "Golden Amber",
        "light": {
            "--global-bg-color": "#fefcf3",
            "--global-text-color": "#2e2810",
            "--global-theme-color": "#d97706",
            "--global-hover-color": "#b45309",
            "--global-divider-color": "#f5edd3",
            "--global-muted": "#7a6d4a",
            "--global-card-bg": "#ffffff",
            "--global-accent": "#f59e0b",
            "--global-accent-2": "#fbbf24",
            "--global-glow": "rgba(217, 119, 6, 0.1)",
        },
        "dark": {
            "--global-bg-color": "#12100a",
            "--global-text-color": "#f0e8d0",
            "--global-theme-color": "#fbbf24",
            "--global-hover-color": "#fcd34d",
            "--global-divider-color": "#2e2810",
            "--global-muted": "#b8a878",
            "--global-card-bg": "#1c1a0e",
            "--global-accent": "#f59e0b",
            "--global-accent-2": "#d97706",
            "--global-glow": "rgba(251, 191, 36, 0.08)",
        },
    },
    6: {  # Sunday - Teal Cyan
        "name": "Teal Cyan",
        "light": {
            "--global-bg-color": "#f2fffe",
            "--global-text-color": "#0f2e2c",
            "--global-theme-color": "#0891b2",
            "--global-hover-color": "#0e7490",
            "--global-divider-color": "#ccf2f0",
            "--global-muted": "#4a7a78",
            "--global-card-bg": "#ffffff",
            "--global-accent": "#06b6d4",
            "--global-accent-2": "#22d3ee",
            "--global-glow": "rgba(8, 145, 178, 0.1)",
        },
        "dark": {
            "--global-bg-color": "#0a1214",
            "--global-text-color": "#d0f0ee",
            "--global-theme-color": "#22d3ee",
            "--global-hover-color": "#67e8f9",
            "--global-divider-color": "#152e30",
            "--global-muted": "#7ab8b5",
            "--global-card-bg": "#101e20",
            "--global-accent": "#06b6d4",
            "--global-accent-2": "#0891b2",
            "--global-glow": "rgba(34, 211, 238, 0.08)",
        },
    },
}


def generate_css_block(theme):
    """Generate CSS variable blocks for a theme."""
    light_vars = "\n".join(
        f"            {k}: {v};" for k, v in theme["light"].items()
    )
    dark_vars = "\n".join(
        f"            {k}: {v};" for k, v in theme["dark"].items()
    )

    return light_vars, dark_vars


def update_about_md(filepath, day_of_week):
    """Replace the CSS variables in about.md with today's theme."""
    theme = THEMES[day_of_week]
    light_css, dark_css = generate_css_block(theme)

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace :root { ... } block
    root_pattern = r"(:root\s*\{)[^}]*(})"
    root_replacement = f"\\1\n{light_css}\n        \\2"
    content = re.sub(root_pattern, root_replacement, content, count=1)

    # Replace [data-theme="dark"] { ... } block
    dark_pattern = r'(\[data-theme="dark"\]\s*\{)[^}]*(})'
    dark_replacement = f"\\1\n{dark_css}\n        \\2"
    content = re.sub(dark_pattern, dark_replacement, content, count=1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return theme["name"]


def main():
    # Use Beijing timezone (UTC+8) for the day calculation
    import datetime
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    beijing_tz = datetime.timezone(datetime.timedelta(hours=8))
    beijing_now = utc_now.astimezone(beijing_tz)
    day_of_week = beijing_now.weekday()  # Monday=0, Sunday=6

    # Allow override via argument
    if len(sys.argv) > 1:
        day_of_week = int(sys.argv[1]) % 7

    # Find about.md relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    about_path = os.path.join(repo_root, "_pages", "about.md")

    if not os.path.exists(about_path):
        print(f"Error: {about_path} not found!")
        sys.exit(1)

    theme_name = update_about_md(about_path, day_of_week)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(f"Theme updated to: {theme_name} ({days[day_of_week]})")
    print(f"File: {about_path}")


if __name__ == "__main__":
    main()
