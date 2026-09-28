import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the `.spotlight-wrapper .nav-btn { display: none !important; }` block from earlier.
old_css = """.spotlight-wrapper .nav-btn {
        display: none !important; /* Hide arrow buttons on mobile to prevent overlapping */
    }"""

new_css = """.spotlight-wrapper .nav-btn {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        background: transparent !important; /* Remove the circle background */
        color: #333 !important; /* Make the arrow dark */
        box-shadow: none !important;
        width: 30px !important;
        height: 30px !important;
    }
    .spotlight-wrapper .nav-btn.prev {
        left: -5px !important;
    }
    .spotlight-wrapper .nav-btn.next {
        right: -5px !important;
    }
    .spotlight-wrapper .nav-btn i {
        font-size: 20px !important;
        filter: drop-shadow(1px 1px 2px rgba(255,255,255,0.8)); /* Add a tiny white glow so it's visible over images */
    }"""

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    content += f"\n@media screen and (max-width: 768px) {{\n{new_css}\n}}\n"

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
    f.write(content)
