import glob
import re

count = 0
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = ''
    i = 0
    while i < len(content):
        # find button
        btn_start = content.find('<button', i)
        if btn_start == -1:
            new_content += content[i:]
            break
        btn_end = content.find('>', btn_start)
        btn_str = content[btn_start:btn_end+1]
        
        # Check text after the button
        after_btn = content[btn_end+1:btn_end+150]
        
        # If it's a button that adds to cart AND is followed by "options" (indicating it should open a modal instead of adding directly)
        # Note: We must NOT do this if the button itself is closing a modal (e.g. style.display='none')
        if 'addToCart' in btn_str and 'options' in after_btn.lower() and 'display=' not in btn_str:
            # Remove onclick attribute completely
            btn_str = re.sub(r'\s*onclick=\"[^\"]*addToCart[^\"]*\"', '', btn_str)
            btn_str = re.sub(r"\s*onclick=\'[^\']*addToCart[^\']*\'", '', btn_str)
        
        new_content += content[i:btn_start] + btn_str
        i = btn_end + 1
        
    if content != new_content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Fixed left-over bugs in {f}')
        count += 1

print(f'Total fixed: {count}')
