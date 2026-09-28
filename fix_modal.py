import os

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('<!-- Tap Accessory Modal -->')
if idx != -1:
    end_idx = c.find('<!-- Wash basin Modal -->', idx)
    if end_idx == -1:
        end_idx = c.find('<script', idx)
    
    modal = c[idx:end_idx]
    
    with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber_fixed.html', 'r', encoding='utf-8') as f2:
        c2 = f2.read()
    
    if 'id="tap-acc-modal"' not in c2:
        insert_pos = c2.find('<script')
        if insert_pos == -1: 
            insert_pos = c2.find('</body>')
            
        c2 = c2[:insert_pos] + '\n' + modal + '\n' + c2[insert_pos:]
        
        with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber_fixed.html', 'w', encoding='utf-8') as f3:
            f3.write(c2)
        print('Modal copied!')
    else:
        print('Modal already in plumber_fixed.html')
else:
    print('Modal not found in plumber.html')
