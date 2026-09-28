import os

base_dir = r'c:\Users\Divyanshi123456\Music\hoamex'
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

scripts_to_add = '\n<script src="common.js?v=2001"></script>\n<script src="cart.js"></script>\n'

count = 0
for file in html_files:
    filepath = os.path.join(base_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'common.js' not in content and '</body>' in content:
        new_content = content.replace('</body>', scripts_to_add + '</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'Added to {file}')

print(f'Total updated: {count}')
