import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Reduce body padding-top in mobile
content = content.replace('padding-top: 170px !important; /* Adjust for taller header */', 'padding-top: 120px !important; /* Adjust for taller header */')

# Reduce .main-content margin in my latest media query for mobile
# I will just append it to the file so it overrides safely.
new_css = """
@media screen and (max-width: 768px) {
    .main-content {
        margin: 10px auto !important;
        padding: 0 10px !important;
    }
}
"""

content += new_css

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
    f.write(content)
