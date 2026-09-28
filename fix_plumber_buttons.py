import os
import re

file_path = "c:/Users/Divyanshi123456/Music/hoamex/plumber.html"
if not os.path.exists(file_path):
    print("File not found")
else:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    modal_map = {
        "Tap repair": "tap-repair-modal",
        "Tap accessory installation": "tap-acc-modal",
        "Tap installation/replacement": "tap-inst-modal",
        "Jet spray installation/replacement": "jet-spray-modal",
        "Flush tank repair/replacement": "flush-tank-modal",
        "Indian toilet unblocking": "indian-toilet-modal",
        "Wall mounted western toilet": "wall-mounted-modal",
        "Floor mounted western toilet": "floor-mounted-modal",
        "Shower installation/repair": "shower-inst-modal",
        "Towel holder": "towel-holder-modal",
        "Shelf installation": "shelf-inst-modal",
        "Washbasin leakage/blockage": "basin-leak-modal",
        "Waste coupling": "waste-coupling-modal",
        "Drain blockage": "drain-block-modal",
        "Kitchen sink grouting": "kitchen-grout-modal",
        "Water tank installation": "tank-install-modal",
        "Water tank repair": "tank-repair-modal",
        "Underground tank cleaning": "ug-tank-modal"
    }

    for svc, modal_id in modal_map.items():
        # We need to find the specific block for the service to replace the button
        # The structure is:
        # <h4>Service Name</h4>
        # ... some lines ...
        # <button class="add-btn" onclick="addToCart(...)">Add</button>
        # <div class="options-text">X options</div>
        
        # Regex to capture the block and replace the button's onclick
        pattern = re.compile(
            r'(<h4>' + re.escape(svc) + r'</h4>.*?<button class="add-btn") onclick="addToCart[^"]+"(>Add</button>\s*<div class="options-text")',
            re.DOTALL
        )
        
        replacement = r'\1 onclick="document.getElementById(\'' + modal_id + r'\').classList.remove(\'hidden\')"\2'
        
        content = pattern.sub(replacement, content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("Updated plumber.html buttons to open modals")
