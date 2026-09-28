import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
out = []
first = False

for line in lines:
    if re.search(r'<!-- .* Modal -->', line):
        if not first:
            first = True
        else:
            out.append('</div>')
    elif line.strip() == '<style>':
        out.append('</div>')
    out.append(line)

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
