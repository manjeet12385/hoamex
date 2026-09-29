import glob

count = 0
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '<h4 style="font-size: 14px; margin-bottom: 5px; height: 35px;">' in content:
        content = content.replace('<h4 style="font-size: 14px; margin-bottom: 5px; height: 35px;">', '<h4 style="font-size: 14px; margin-bottom: 5px; min-height: 35px; height: auto;">')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        count += 1
        print(f"Fixed {f}")
        
    elif 'height: 35px;' in content:
        # maybe there are variations
        pass

print(f"Total files updated: {count}")
