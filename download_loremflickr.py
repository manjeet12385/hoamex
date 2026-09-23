import urllib.request
import os

queries = {
    "washing_machine.jpg": "washing,machine",
    "refrigerator.jpg": "refrigerator",
    "electrician_icon.jpg": "electrician",
    "carpenter_icon.jpg": "carpenter",
    "pest_control_icon.jpg": "pest,bug",
    "painting_icon.jpg": "painter",
    "cctv_icon.jpg": "cctv,camera",
    "smart_lock_icon.jpg": "smart,lock",
    "solar_panel_icon.jpg": "solar,panel",
    "ro_purifier_icon.jpg": "water,purifier",
    "packers_icon.jpg": "boxes,moving",
    "truck_icon.jpg": "truck",
    "maid_icon.jpg": "maid,cleaning",
    "cook_icon.jpg": "chef,cooking",
    "grills_icon.jpg": "grill,window",
    "gates_icon.jpg": "iron,gate",
    "roofing_icon.jpg": "roofing"
}

os.makedirs("images", exist_ok=True)

for filename, keywords in queries.items():
    url = f"https://loremflickr.com/400/400/{keywords}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        img_data = urllib.request.urlopen(req, timeout=10).read()
        with open(os.path.join("images", filename), "wb") as f:
            f.write(img_data)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed {filename}: {e}")
