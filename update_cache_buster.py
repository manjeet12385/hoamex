import glob
import re

files = glob.glob('*.html')
total = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = re.sub(r'style\.css\?v=\d+', 'style.css?v=3015', content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        total += 1

print(f"Updated cache buster in {total} files!")


