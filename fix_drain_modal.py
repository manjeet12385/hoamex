import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber_fixed.html', 'r', encoding='utf-8') as f:
    c = f.read()

if 'drain-block-modal' not in c:
    with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f2:
        c2 = f2.read()
    idx = c2.find('<div id="drain-block-modal"')
    end_idx = c2.find('<!-- Kitchen Grouting Modal -->', idx)
    modal = c2[idx:end_idx]
    
    insert_pos = c.find('<script')
    if insert_pos == -1: insert_pos = c.find('</body>')
    c = c[:insert_pos] + '\n' + modal + '\n' + c[insert_pos:]
    print('Modal copied')

pattern = r'<button class="add-btn" onclick="addToCart\(\'Drain blockage removal\',199\)">Add</button>'
rep = r'<button class="add-btn" onclick="document.getElementById(\'drain-block-modal\').classList.remove(\'hidden\')">Add</button>'
c = re.sub(pattern, rep, c)

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber_fixed.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Button fixed')
