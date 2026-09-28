import os
import re

base_dir = r'c:\Users\Divyanshi123456\Music\hoamex'
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

# We'll use a regex to catch the old logo block
old_logo_pattern = re.compile(
    r'<a[^>]*href="index\.html"[^>]*class="logo"[^>]*>.*?<div class="logo-icon">J</div>.*?<span class="logo-text">Joamex</span>.*?</a>',
    re.DOTALL
)

# And another one for plumber.html which might have different formatting
old_logo_pattern2 = re.compile(
    r'<a[^>]*href="index\.html"[^>]*>.*?<div class="logo-icon">J</div>.*?<span class="logo-text">Joamex</span>.*?</a>',
    re.DOTALL
)

new_logo = '''<a class="logo" href="index.html" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; margin-right: 15px; text-decoration: none;">
                <img src="images/logo.png" alt="Joamex Icon" style="height: 35px; border-radius: 8px;">
                <img src="images/logo-text.png" alt="Joamex Text" style="height: 12px;">
            </a>'''

count = 0
for file in html_files:
    filepath = os.path.join(base_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = old_logo_pattern.sub(new_logo, content)
    new_content = old_logo_pattern2.sub(new_logo, new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated logo in {file}")

print(f"Total files updated: {count}")
