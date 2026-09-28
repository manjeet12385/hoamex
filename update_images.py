import os
import re

mapping = {
    'cctv-services.html': 'cctv_camera.jpg',
    'smart-locks.html': 'smart_lock.jpg',
    'home-alarm.html': 'home_alarm.jpg',
    'solar-installation.html': 'solar_panel.jpg',
    'solar-cleaning.html': 'solar_cleaning.jpg',
    'solar-water-heater.html': 'solar_water_heater.jpg',
    'ro-service.html': 'ro_purifier.jpg',
    'water-tank-cleaning.html': 'water_tank_cleaning.jpg'
}

target_images = ['cctv_icon.jpg', 'homecare.jpg', 'cleaning.jpg', 'plumber.jpg', 'ac.jpg', 'security.jpg', 'ac_repair_new.jpg', 'water_tank.jpg', 'ro_purifier_icon.jpg', 'ro_purifier.png']

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
