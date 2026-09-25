import os, glob, re

for file in glob.glob('*.html'):
    if 'fixed' in file: continue # skip backup files
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    rows = content.split('<div class="svc-row">')[1:]
    for row in rows:
        if 'options-text' in row and 'onclick="addToCart' in row:
            m = re.search(r'<h4>(.*?)</h4>', row)
            if m:
                title = m.group(1).strip()
                opt_m = re.search(r'<div class="options-text">(.*?)</div>', row)
                opt_text = opt_m.group(1) if opt_m else 'options'
                print(f'[{file}] {title} ({opt_text})')
