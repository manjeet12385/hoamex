import re
with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = re.findall(r'<button class="add-btn" onclick="([^"]+)">Add</button>', c)
for m in matches:
    if 'modal' in m:
        print(m)
