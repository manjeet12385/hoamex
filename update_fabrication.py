import os

mapping = {
    'grills-railings.html': 'window_grills.jpg',
    'gates-doors.html': 'gates_doors.jpg',
    'sheds-roofing.html': 'sheds_roofing.jpg',
    'welding-repair.html': 'welding_repair.jpg'
}

target_images = ['grills_icon.jpg', 'gates_icon.jpg', 'roofing_icon.jpg', 'plumber.jpg', 'fabrication.jpg']

base_dir = r'c:\Users\Divyanshi123456\Music\hoamex'

for filename, new_image in mapping.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f'File not found: {filename}')
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old_img in target_images:
        content = content.replace(f'src="images/{old_img}"', f'src="images/{new_image}"')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Updated {filename}')
