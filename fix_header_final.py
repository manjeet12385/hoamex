import re
import glob

css_path = r'c:\Users\Divyanshi123456\Music\hoamex\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix body padding-top to account for fixed header height (~70px)
# Replace any existing body padding-top value
css = re.sub(r'(body\s*\{[^}]*?)padding-top:\s*\d+px\s*;', r'\1padding-top: 75px;', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS body padding-top updated")

# Bump cache version on all HTML files
html_files = glob.glob(r'c:\Users\Divyanshi123456\Music\hoamex\*.html')
count = 0
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        new_html = re.sub(r'common\.js(?:\?v=\d+)?', 'common.js?v=3010', html)
        new_html = re.sub(r'style\.css(?:\?v=\d+)?', 'style.css?v=3010', new_html)
        if html != new_html:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_html)
            count += 1
    except:
        pass

print(f"Cache busted on {count} HTML files")
