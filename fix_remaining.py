import glob

count = 0
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = ''
    i = 0
    while i < len(content):
        # find button
        btn_start = content.find('<button ', i)
        if btn_start == -1:
            new_content += content[i:]
            break
        btn_end = content.find('>', btn_start)
        btn_str = content[btn_start:btn_end+1]
        
        # Check if it has addToCart and an id indicating it opens a modal
        if 'addToCart' in btn_str and ('modal' in btn_str or 'options' in btn_str) and 'id=' in btn_str:
            # find onclick
            onclick_idx = btn_str.find('onclick="')
            if onclick_idx != -1:
                onclick_end = btn_str.find('"', onclick_idx + 9)
                if onclick_end != -1:
                    btn_str = btn_str[:onclick_idx] + btn_str[onclick_end+1:]
        
        new_content += content[i:btn_start] + btn_str
        i = btn_end + 1
        
    if content != new_content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Fixed missing in {f}')
        count += 1

print(f'Total fixed: {count}')
