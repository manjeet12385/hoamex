import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(".classList.remove('hidden')", ".style.display='flex'")
content = content.replace(".classList.add('hidden')", ".style.display='none'")

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'w', encoding='utf-8') as f:
    f.write(content)
