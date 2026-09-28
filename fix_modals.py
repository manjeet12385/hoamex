import re

# 1. Update style.css for responsive modal grid
with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

responsive_modal_css = """
@media screen and (max-width: 768px) {
    .modal-grid {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 15px !important;
        justify-content: center !important;
    }
    .modal-item {
        width: 100% !important;
        margin-bottom: 0 !important;
    }
    .modal-item img {
        width: 65px !important;
        height: 65px !important;
    }
    .modal-subtitle {
        font-size: 16px !important;
    }
}
@media screen and (max-width: 480px) {
    .modal-grid {
        grid-template-columns: repeat(2, 1fr) !important;
    }
}
"""
css_content += responsive_modal_css
with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)


# 2. Update app.js to use style.display='flex' instead of classList
with open(r'c:\Users\Divyanshi123456\Music\hoamex\app.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

js_content = js_content.replace(".classList.remove('hidden')", ".style.display = 'flex'")
js_content = js_content.replace(".classList.add('hidden')", ".style.display = 'none'")

with open(r'c:\Users\Divyanshi123456\Music\hoamex\app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
