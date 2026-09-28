import re, glob
css_path = r'c:\Users\Divyanshi123456\Music\hoamex\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add sticky/fixed header rule if not present
header_rule = """
/* Persistent Fixed Header */
.header {
    position: sticky;
    top: 0;
    z-index: 9999;
    background: #fff;
    width: 100%;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}
/* Ensure body content starts below header */
body {
    padding-top: 70px; /* adjust based on header height */
}
"""
if "Persistent Fixed Header" not in css:
    css += "\n" + header_rule
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print('Injected fixed header CSS')
else:
    print('Fixed header CSS already present')
