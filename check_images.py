import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    images = set(re.findall(r'src=["\']images/([^"\']+)["\']', content))
    
    mismatches = []
    
    # We want to ignore the 'promise-badge' which might use 'beauty.jpg' everywhere globally.
    # Actually, using 'beauty.jpg' for 'Joamex Promise' on a plumber page is weird, it should be a generic badge.
    
    # Let's print all images used in all files briefly to see global trends
    print(f"--- {f} ---")
    for img in images:
        # basic check
        if 'beauty' in img and not ('salon' in f or 'beauty' in f or 'spa' in f or 'makeup' in f or 'massage' in f or 'grooming' in f):
            mismatches.append(img + " (Beauty img in non-beauty page)")
        if 'plumb' in img and not ('plumber' in f or 'water' in f):
            mismatches.append(img + " (Plumber img in non-plumber page)")
        if 'ac_' in img and not ('ac-' in f):
            mismatches.append(img + " (AC img in non-ac page)")
        if 'kitchen' in img and not ('kitchen' in f or 'cook' in f or 'chimney' in f or 'microwave' in f or 'fridge' in f or 'refrigerator' in f or 'ro' in f or 'water' in f or 'tile' in f):
            mismatches.append(img + " (Kitchen img in non-kitchen page)")
            
    if mismatches:
        for m in mismatches:
            print(f"  MISMATCH: {m}")
