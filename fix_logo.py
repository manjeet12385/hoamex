import glob

count = 0
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace the broken style inside the logo image
    old_str = '<img src="images/logo.png" alt="Joamex Icon" style="min-height: 40px; height: auto; border-radius: 8px;">'
    new_str = '<img src="images/logo.png" alt="Joamex Icon" style="height: 35px; border-radius: 8px;">'
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        count += 1
        
print(f'Fixed broken logo in {count} files')
