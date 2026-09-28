import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\app.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("triggerId: 'homecare-btn'", "triggerId: 'logistics-modal-trigger'")
content = content.replace("triggerId: 'security-btn'", "triggerId: 'security-modal-trigger'")

with open(r'c:\Users\Divyanshi123456\Music\hoamex\app.js', 'w', encoding='utf-8') as f:
    f.write(content)
