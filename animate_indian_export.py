import glob

html_files = glob.glob('*.html')

old_text = '<div>managed by <strong style="color: #111; font-weight: 700;">Indian Export Webmart</strong></div>'

new_text = """<div style="margin-top: 10px; padding: 6px 16px; border-radius: 30px; background: #fff; border: 1px solid #eaeaea; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.06); transition: 0.3s; cursor: default;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 15px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.06)'">
    <span style="font-size: 13px; color: #777;">managed by</span>
    <strong class="animated-brand-text" style="color: transparent; background: linear-gradient(90deg, #ff007f, #7928ca, #00d2ff, #f9cb28, #ff007f); background-size: 200% auto; -webkit-background-clip: text; background-clip: text; font-weight: 900; font-size: 15px; letter-spacing: 0.5px; animation: shineText 3s linear infinite;">
        Indian Export Webmart
    </strong>
    <i class="fa-solid fa-sparkles" style="color: #f9cb28; font-size: 14px; animation: pulseSparkle 1.5s infinite;"></i>
    <style>
        @keyframes shineText {
            to { background-position: 200% center; }
        }
        @keyframes pulseSparkle {
            0%, 100% { transform: scale(1) rotate(0deg); opacity: 0.8; }
            50% { transform: scale(1.3) rotate(15deg); opacity: 1; text-shadow: 0 0 10px rgba(249, 203, 40, 0.8); }
        }
    </style>
</div>"""

updated_count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1
        print(f"Updated {filepath}")

print(f"Total files updated: {updated_count}")
