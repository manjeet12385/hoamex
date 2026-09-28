import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace `.stats-container { flex-direction: column; gap: 20px; }` with a row version.
# Since it might be hard to regex perfectly, I will just append an override to the end of the file.

new_css = """
@media screen and (max-width: 768px) {
    .stats-container {
        flex-direction: row !important;
        justify-content: space-around !important;
        align-items: center !important;
        flex-wrap: wrap !important;
        gap: 10px !important;
    }
    .stat-item {
        flex: 1;
        min-width: 30%;
        text-align: center;
    }
    .stat-value {
        font-size: 18px !important;
    }
    .stat-label {
        font-size: 11px !important;
    }
}
"""

content += new_css

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
    f.write(content)
