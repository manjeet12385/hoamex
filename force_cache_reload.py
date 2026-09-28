import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Force cache invalidation by updating version queries
content = content.replace('app.js?v=7', 'app.js?v=8')
content = content.replace('style.css?v=1000', 'style.css?v=1001')

with open(r'c:\Users\Divyanshi123456\Music\hoamex\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
