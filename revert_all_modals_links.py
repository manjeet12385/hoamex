import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Reverse the onclick injection for modal items
new_content = re.sub(r'\s*onclick="window\.location\.href=\'([^\']+)\';"', '', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Reverted inline onclicks from index.html")
