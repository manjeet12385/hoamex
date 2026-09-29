import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    images = set(re.findall(r'src=[\"\']images/([^\"\']+)[\"\']', content))
    
    mismatches = []
    
    for img in images:
        if img == 'beauty.jpg': continue
        if 'plumb' in img and not ('plumber' in f or 'water' in f or 'tile' in f or 'bathroom' in f):
            mismatches.append(img + ' (Plumber img)')
        if 'ac_' in img and not ('ac-' in f or 'appliance' in f):
            mismatches.append(img + ' (AC img)')
        if 'kitchen' in img and not ('kitchen' in f or 'cook' in f or 'chimney' in f or 'microwave' in f or 'fridge' in f or 'refrigerator' in f or 'ro' in f or 'water' in f or 'tile' in f or 'appliance' in f):
            mismatches.append(img + ' (Kitchen img)')
            
    if mismatches:
        print(f'{f} uses: {mismatches}')
