import urllib.request
import re
from urllib.parse import quote, unquote
import os

queries = {
    "washing_machine.jpg": "washing machine repair service",
    "refrigerator.jpg": "refrigerator repair service",
    "electrician_icon.jpg": "electrician fixing wires",
    "carpenter_icon.jpg": "carpenter working on wood",
    "pest_control_icon.jpg": "pest control exterminator",
    "painting_icon.jpg": "house painter painting wall",
    "cctv_icon.jpg": "cctv camera installation",
    "smart_lock_icon.jpg": "smart door lock modern",
    "solar_panel_icon.jpg": "solar panel roof installation",
    "ro_purifier_icon.jpg": "water purifier kitchen",
    "packers_icon.jpg": "packers and movers boxes",
    "truck_icon.jpg": "mini truck cargo transport",
    "maid_icon.jpg": "house maid cleaning",
    "cook_icon.jpg": "personal chef cooking at home",
    "grills_icon.jpg": "metal window grill design",
    "gates_icon.jpg": "iron main gate house",
    "roofing_icon.jpg": "metal sheet roofing shed"
}

os.makedirs("images", exist_ok=True)

def download_image(query, filename):
    url = "https://html.duckduckgo.com/html/?q=" + quote(query + " high quality photo")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        matches = re.findall(r'src="//external-content\.duckduckgo\.com/iu/\?u=([^&]+)', html)
        if matches:
            for img_url in matches:
                img_url = unquote(img_url)
                if img_url.lower().endswith(('.jpg', '.jpeg', '.png')):
                    req2 = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                    img_data = urllib.request.urlopen(req2, timeout=10).read()
                    with open(os.path.join("images", filename), "wb") as f:
                        f.write(img_data)
                    return True
    except Exception as e:
        print(f"Error for {query}: {e}")
    return False

print("Downloading new images...")
for filename, query in queries.items():
    success = download_image(query, filename)
    if success:
        print(f"Downloaded {filename}")
    else:
        print(f"Failed {filename}")

# Now we need to update the HTML files to use these new images instead of the generic ones.
replacements = {
    'index.html': [
        ('alt="Washing"><p>Washing Machine', 'images/tools.jpg', 'images/washing_machine.jpg'),
        ('alt="Fridge"><p>Refrigerator', 'images/homecare.jpg', 'images/refrigerator.jpg'),
        ('alt="Electrician"><p>Electrician', 'images/tools.jpg', 'images/electrician_icon.jpg'),
        ('alt="Carpenter"><p>Carpenter', 'images/carpenter.jpg', 'images/carpenter_icon.jpg'),
        ('alt="Pest"><p>Pest Control', 'images/homecare.jpg', 'images/pest_control_icon.jpg'),
        ('alt="Paint"><p>Painting', 'images/painter.jpg', 'images/painting_icon.jpg'),
        ('alt="Packers & Movers"', 'images/tools.jpg', 'images/packers_icon.jpg'),
        ('alt="Mini Truck"', 'images/homecare.jpg', 'images/truck_icon.jpg'),
        ('alt="Maid"', 'images/cleaning.jpg', 'images/maid_icon.jpg'),
        ('alt="Cook"', 'images/kitchen.jpg', 'images/cook_icon.jpg'),
        ('alt="Grills & Railings"', 'images/fabrication.jpg', 'images/grills_icon.jpg'),
        ('alt="Gates & Doors"', 'images/tools.jpg', 'images/gates_icon.jpg'),
        ('alt="Sheds & Roofing"', 'images/homecare.jpg', 'images/roofing_icon.jpg'),
    ],
    'washing-machine.html': [('images/tools.jpg', 'images/washing_machine.jpg'), ('images/ac.jpg', 'images/washing_machine.jpg')],
    'fridge.html': [('images/homecare.jpg', 'images/refrigerator.jpg'), ('images/ac.jpg', 'images/refrigerator.jpg')],
    'electrician.html': [('images/tools.jpg', 'images/electrician_icon.jpg'), ('images/plumber.jpg', 'images/electrician_icon.jpg')],
    'carpenter.html': [('images/carpenter.jpg', 'images/carpenter_icon.jpg'), ('images/plumber.jpg', 'images/carpenter_icon.jpg')],
    'pest-control.html': [('images/homecare.jpg', 'images/pest_control_icon.jpg'), ('images/cleaning.jpg', 'images/pest_control_icon.jpg')],
    'painting.html': [('images/painter.jpg', 'images/painting_icon.jpg'), ('images/renovation.jpg', 'images/painting_icon.jpg')],
    'cctv-services.html': [('images/security.jpg', 'images/cctv_icon.jpg')],
    'smart-locks.html': [('images/tools.jpg', 'images/smart_lock_icon.jpg'), ('images/security.jpg', 'images/smart_lock_icon.jpg')],
    'solar-installation.html': [('images/ac.jpg', 'images/solar_panel_icon.jpg'), ('images/security.jpg', 'images/solar_panel_icon.jpg')],
    'ro-service.html': [('images/plumber.jpg', 'images/ro_purifier_icon.jpg'), ('images/security.jpg', 'images/ro_purifier_icon.jpg')],
    'packers-movers.html': [('images/tools.jpg', 'images/packers_icon.jpg')],
    'mini-truck.html': [('images/homecare.jpg', 'images/truck_icon.jpg')],
    'maid-helper.html': [('images/cleaning.jpg', 'images/maid_icon.jpg')],
    'cook-on-demand.html': [('images/kitchen.jpg', 'images/cook_icon.jpg')],
    'grills-railings.html': [('images/fabrication.jpg', 'images/grills_icon.jpg')],
    'gates-doors.html': [('images/tools.jpg', 'images/gates_icon.jpg')],
    'sheds-roofing.html': [('images/homecare.jpg', 'images/roofing_icon.jpg')]
}

for filename, rules in replacements.items():
    if not os.path.exists(filename): continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if filename == 'index.html':
        # special targeted replacement
        lines = content.splitlines(True)
        for i in range(len(lines)):
            for rule in rules:
                context, old_img, new_img = rule
                if context in lines[i]:
                    lines[i] = lines[i].replace(old_img, new_img)
        content = ''.join(lines)
    else:
        # bulk replace
        for old_img, new_img in rules:
            content = content.replace(old_img, new_img)
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Images replaced in HTML files.")
