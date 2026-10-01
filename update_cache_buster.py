import os
import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace common.js?v=xxxx with common.js?v=9999
    new_content = re.sub(r'common\.js\?v=\d+', 'common.js?v=9999', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)

print("Updated cache buster to v=9999")
