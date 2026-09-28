import re
with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber_fixed.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = re.findall(r'<button class="add-btn" onclick="([^"]+)">Add</button>', c)
for m in set(matches):
    print(m)

print('\nCheck modal classes:')
if 'drain-block-modal' in c:
    idx = c.find('drain-block-modal')
    print(c[idx-50:idx+50])
else:
    print('drain-block-modal NOT found')
