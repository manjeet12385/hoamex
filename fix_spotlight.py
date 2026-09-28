import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Add spotlight fixes for mobile
new_css = """
@media screen and (max-width: 768px) {
    .spotlight-card {
        min-width: 85% !important;
        padding: 20px !important;
        height: auto !important;
        min-height: 180px !important;
    }
    .spotlight-card h4 {
        font-size: 18px !important;
        max-width: 100% !important;
    }
    .spotlight-card p {
        font-size: 14px !important;
        max-width: 100% !important;
    }
    .spotlight-wrapper .nav-btn {
        display: none !important; /* Hide arrow buttons on mobile to prevent overlapping */
    }
}
"""

content += new_css

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
    f.write(content)
