import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the previous `.services-grid` definition in my mobile_tweaks script with the sliding version.
old_css = """    .services-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 15px !important;
    }"""

new_css = """    .services-grid {
        display: grid !important;
        grid-template-rows: repeat(2, 1fr) !important;
        grid-template-columns: none !important;
        grid-auto-columns: 35% !important; /* 35% means they see almost 3 items horizontally, allowing sliding */
        grid-auto-flow: column !important;
        overflow-x: auto !important;
        scrollbar-width: none !important; /* Firefox */
        gap: 15px !important;
        padding-bottom: 15px !important;
        scroll-snap-type: x mandatory;
    }
    .services-grid::-webkit-scrollbar {
        display: none !important; /* Chrome/Safari */
    }
    .service-item {
        scroll-snap-align: start;
        border: 1px solid #eee; /* optional: adding a small border to make cards distinct while sliding */
        border-radius: 12px;
        padding: 10px;
        background: #fff;
    }"""

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    # Fallback if the string wasn't exactly matched
    content += f"""
@media screen and (max-width: 768px) {{
{new_css}
}}
"""

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
    f.write(content)
