import os
import re

base_dir = r'c:\Users\Divyanshi123456\Music\hoamex'

# 1. Update index.html specifically for the Logistics modal
index_path = os.path.join(base_dir, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

logistics_replacements = {
    'href="packers-movers.html" style="text-decoration: none;">\n<img alt="Packers &amp; Movers" src="images/packers_icon.jpg"/>': 'href="packers-movers.html" style="text-decoration: none;">\n<img alt="Packers &amp; Movers" src="images/packers_movers.jpg"/>',
    'href="mini-truck.html" style="text-decoration: none;">\n<img alt="Mini Truck" src="images/truck_icon.jpg"/>': 'href="mini-truck.html" style="text-decoration: none;">\n<img alt="Mini Truck" src="images/mini_truck.jpg"/>',
    'href="driver-on-demand.html" style="text-decoration: none;">\n<img alt="Driver" src="images/carpenter.jpg"/>': 'href="driver-on-demand.html" style="text-decoration: none;">\n<img alt="Driver" src="images/driver.jpg"/>',
    'href="maid-helper.html" style="text-decoration: none;">\n<img alt="Maid" src="images/maid_icon.jpg"/>': 'href="maid-helper.html" style="text-decoration: none;">\n<img alt="Maid" src="images/maid.jpg"/>',
    'href="cook-on-demand.html" style="text-decoration: none;">\n<img alt="Cook" src="images/cook_icon.jpg"/>': 'href="cook-on-demand.html" style="text-decoration: none;">\n<img alt="Cook" src="images/cook.jpg"/>',
    'href="elder-care.html" style="text-decoration: none;">\n<img alt="Elder Care" src="images/homecare.jpg"/>': 'href="elder-care.html" style="text-decoration: none;">\n<img alt="Elder Care" src="images/elder_care.jpg"/>',
    'href="babysitting.html" style="text-decoration: none;">\n<img alt="Babysitting" src="images/grooming.jpg"/>': 'href="babysitting.html" style="text-decoration: none;">\n<img alt="Babysitting" src="images/nanny.jpg"/>'
}

for old, new in logistics_replacements.items():
    index_content = index_content.replace(old, new)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)
print("Updated index.html")

# 2. Update individual pages
page_mapping = {
    'packers-movers.html': ('packers_movers.jpg', ['packers_icon.jpg', 'tools.jpg']),
    'mini-truck.html': ('mini_truck.jpg', ['truck_icon.jpg', 'tools.jpg']),
    'driver-on-demand.html': ('driver.jpg', ['carpenter.jpg', 'tools.jpg']),
    'maid-helper.html': ('maid.jpg', ['maid_icon.jpg', 'cleaning.jpg']),
    'cook-on-demand.html': ('cook.jpg', ['cook_icon.jpg', 'kitchen.jpg']),
    'elder-care.html': ('elder_care.jpg', ['homecare.jpg', 'tools.jpg']),
    'babysitting.html': ('nanny.jpg', ['grooming.jpg', 'tools.jpg'])
}

for filename, (new_img, old_imgs) in page_mapping.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f'File not found: {filename}')
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old_img in old_imgs:
        content = content.replace(f'src="images/{old_img}"', f'src="images/{new_img}"')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {filename}')
