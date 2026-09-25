#!/usr/bin/env python3
"""
Fix electrician.html: Replace all direct addToCart buttons with option modals.
"""

import re

with open('electrician.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------------------
# Define all services that currently use addToCart directly and need modals
# Format: (service_id, title, rating_text, options: [(name, price, rating, reviews)])
# -------------------------------------------------------------------------
SERVICES = [
    {
        "id": "new-switchbox",
        "title": "New switchbox installation",
        "rating": "4.79",
        "reviews": "99K",
        "old_onclick": "addToCart('New switchbox installation', 149)",
        "options": [
            {"name": "Single Module", "price": 149, "rating": "4.78", "reviews": "22K"},
            {"name": "Double Module", "price": 199, "rating": "4.79", "reviews": "41K"},
            {"name": "Triple Module", "price": 249, "rating": "4.80", "reviews": "28K"},
            {"name": "4+ Module (Large)", "price": 299, "rating": "4.77", "reviews": "8K"},
        ]
    },
    {
        "id": "fan-repair",
        "title": "Fan repair",
        "rating": "4.80",
        "reviews": "201K",
        "old_onclick": "addToCart('Fan repair', 149)",
        "options": [
            {"name": "Ceiling Fan Repair", "price": 149, "rating": "4.80", "reviews": "120K"},
            {"name": "Exhaust Fan Repair", "price": 149, "rating": "4.79", "reviews": "51K"},
            {"name": "Pedestal/Tower Fan Repair", "price": 199, "rating": "4.81", "reviews": "30K"},
        ]
    },
    {
        "id": "ceiling-fan-install",
        "title": "Regular ceiling fan installation",
        "rating": "4.85",
        "reviews": "97K",
        "old_onclick": "addToCart('Regular ceiling fan installation', 99)",
        "options": [
            {"name": "Standard Installation", "price": 99, "rating": "4.85", "reviews": "60K"},
            {"name": "With Hook & Rod", "price": 149, "rating": "4.84", "reviews": "27K"},
            {"name": "High Ceiling (8ft+)", "price": 199, "rating": "4.86", "reviews": "10K"},
        ]
    },
    {
        "id": "decorative-fan",
        "title": "Decorative fan installation",
        "rating": "4.77",
        "reviews": "1K",
        "old_onclick": "addToCart('Decorative fan installation', 99)",
        "options": [
            {"name": "Designer Fan (upto 5ft)", "price": 99, "rating": "4.76", "reviews": "450"},
            {"name": "BLDC Designer Fan", "price": 149, "rating": "4.78", "reviews": "320"},
            {"name": "Large Designer Fan (5ft+)", "price": 199, "rating": "4.79", "reviews": "230"},
        ]
    },
    {
        "id": "exhaust-fan",
        "title": "Exhaust/pedestal/tower fan installation",
        "rating": "4.81",
        "reviews": "40K",
        "old_onclick": "addToCart('Exhaust/pedestal/tower fan installation', 99)",
        "options": [
            {"name": "Exhaust Fan", "price": 99, "rating": "4.82", "reviews": "25K"},
            {"name": "Pedestal Fan", "price": 99, "rating": "4.80", "reviews": "10K"},
            {"name": "Tower Fan", "price": 149, "rating": "4.79", "reviews": "5K"},
        ]
    },
    {
        "id": "fancy-light",
        "title": "Fancy light installation/replacement",
        "rating": "4.82",
        "reviews": "60K",
        "old_onclick": "addToCart('Fancy light installation/replacement', 149)",
        "options": [
            {"name": "LED Strip Light", "price": 149, "rating": "4.81", "reviews": "30K"},
            {"name": "Spot/Recessed Light", "price": 149, "rating": "4.82", "reviews": "20K"},
            {"name": "Wall Light (Sconce)", "price": 199, "rating": "4.83", "reviews": "10K"},
        ]
    },
    {
        "id": "tubelight",
        "title": "Tubelight repair & Installation",
        "rating": "4.86",
        "reviews": "132K",
        "old_onclick": "addToCart('Tubelight repair &amp; Installation', 99)",
        "options": [
            {"name": "T8 Tubelight Repair", "price": 99, "rating": "4.87", "reviews": "60K"},
            {"name": "LED Tubelight Installation", "price": 99, "rating": "4.86", "reviews": "45K"},
            {"name": "Batten Light Installation", "price": 119, "rating": "4.85", "reviews": "27K"},
        ]
    },
    {
        "id": "bulb-install",
        "title": "Bulb installation/replacement",
        "rating": "4.84",
        "reviews": "51K",
        "old_onclick": "addToCart('Bulb installation/replacement', 49)",
        "options": [
            {"name": "Single Bulb", "price": 49, "rating": "4.84", "reviews": "30K"},
            {"name": "2-4 Bulbs", "price": 79, "rating": "4.85", "reviews": "15K"},
            {"name": "5+ Bulbs", "price": 99, "rating": "4.83", "reviews": "6K"},
        ]
    },
    {
        "id": "ceiling-light",
        "title": "Ceiling light installation",
        "rating": "4.82",
        "reviews": "82K",
        "old_onclick": "addToCart('Ceiling light installation', 89)",
        "options": [
            {"name": "Surface Mounted Light", "price": 89, "rating": "4.82", "reviews": "50K"},
            {"name": "Recessed/False Ceiling Light", "price": 129, "rating": "4.81", "reviews": "32K"},
        ]
    },
    {
        "id": "hanging-light",
        "title": "Hanging light installation",
        "rating": "4.80",
        "reviews": "17K",
        "old_onclick": "addToCart('Hanging light installation', 199)",
        "options": [
            {"name": "Pendant Light (Single)", "price": 199, "rating": "4.80", "reviews": "8K"},
            {"name": "Pendant Light (Cluster)", "price": 299, "rating": "4.79", "reviews": "6K"},
            {"name": "Hanging Lantern", "price": 249, "rating": "4.81", "reviews": "3K"},
        ]
    },
    {
        "id": "internal-wiring",
        "title": "New internal wiring (per 5m)",
        "rating": "4.73",
        "reviews": "19K",
        "old_onclick": "addToCart('New internal wiring (per 5m)', 199)",
        "options": [
            {"name": "2-Wire (Lighting)", "price": 199, "rating": "4.74", "reviews": "10K"},
            {"name": "3-Wire (Power)", "price": 249, "rating": "4.72", "reviews": "9K"},
        ]
    },
    {
        "id": "doorbell-regular",
        "title": "Regular doorbell installation",
        "rating": "4.84",
        "reviews": "20K",
        "old_onclick": "addToCart('Regular doorbell installation', 99)",
        "options": [
            {"name": "Wired Doorbell", "price": 99, "rating": "4.84", "reviews": "14K"},
            {"name": "Wireless Doorbell", "price": 129, "rating": "4.83", "reviews": "6K"},
        ]
    },
    {
        "id": "video-doorbell",
        "title": "Video doorbell installation",
        "rating": "4.71",
        "reviews": "1K",
        "old_onclick": "addToCart('Video doorbell installation', 600)",
        "options": [
            {"name": "Wired Video Doorbell", "price": 600, "rating": "4.72", "reviews": "650"},
            {"name": "Wireless Video Doorbell", "price": 699, "rating": "4.70", "reviews": "350"},
        ]
    },
    {
        "id": "mcb-repair",
        "title": "MCB/fuse repair",
        "rating": "4.77",
        "reviews": "19K",
        "old_onclick": "addToCart('MCB/fuse repair', 149)",
        "options": [
            {"name": "Single MCB Repair", "price": 149, "rating": "4.77", "reviews": "8K"},
            {"name": "Double MCB Repair", "price": 199, "rating": "4.78", "reviews": "6K"},
            {"name": "RCCB/RCBO Repair", "price": 249, "rating": "4.76", "reviews": "3K"},
            {"name": "Distribution Board Repair", "price": 349, "rating": "4.77", "reviews": "2K"},
        ]
    },
    {
        "id": "mcb-replacement",
        "title": "MCB/fuse replacement",
        "rating": "4.79",
        "reviews": "14K",
        "old_onclick": "addToCart('MCB/fuse replacement', 149)",
        "options": [
            {"name": "6A/10A MCB", "price": 149, "rating": "4.79", "reviews": "5K"},
            {"name": "16A/20A MCB", "price": 179, "rating": "4.79", "reviews": "5K"},
            {"name": "32A/40A MCB", "price": 219, "rating": "4.80", "reviews": "3K"},
            {"name": "RCCB Replacement", "price": 399, "rating": "4.78", "reviews": "1K"},
        ]
    },
    {
        "id": "tv-installation",
        "title": "TV installation",
        "rating": "4.85",
        "reviews": "43K",
        "old_onclick": "addToCart('TV installation', 399)",
        "options": [
            {"name": "Below 32 inch", "price": 399, "rating": "4.85", "reviews": "10K"},
            {"name": "32-43 inch", "price": 449, "rating": "4.86", "reviews": "15K"},
            {"name": "44-55 inch", "price": 499, "rating": "4.84", "reviews": "12K"},
            {"name": "56-65 inch", "price": 599, "rating": "4.85", "reviews": "5K"},
            {"name": "65 inch+", "price": 699, "rating": "4.84", "reviews": "1K"},
        ]
    },
    {
        "id": "tv-uninstallation",
        "title": "TV uninstallation",
        "rating": "4.87",
        "reviews": "6K",
        "old_onclick": "addToCart('TV uninstallation', 249)",
        "options": [
            {"name": "Below 43 inch", "price": 249, "rating": "4.87", "reviews": "2K"},
            {"name": "44-55 inch", "price": 299, "rating": "4.88", "reviews": "2K"},
            {"name": "56-65 inch", "price": 349, "rating": "4.86", "reviews": "1.5K"},
            {"name": "65 inch+", "price": 399, "rating": "4.87", "reviews": "500"},
        ]
    },
    {
        "id": "inverter-install",
        "title": "Inverter installation",
        "rating": "4.74",
        "reviews": "9K",
        "old_onclick": "addToCart('Inverter installation', 485)",
        "options": [
            {"name": "Single Battery Inverter", "price": 485, "rating": "4.74", "reviews": "6K"},
            {"name": "Double Battery Inverter", "price": 599, "rating": "4.74", "reviews": "3K"},
        ]
    },
]

def make_option_card(svc_id, opt):
    """Generate HTML for a single option card inside the modal."""
    return f'''
                        <div class="option-card" style="min-width: 150px; flex: 1; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 16px; display: flex; flex-direction: column; background: #fff;">
                            <div style="width: 100%; height: 100px; margin-bottom: 15px; background: #f8f8f8; border-radius: 6px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                                <i class="fa-solid fa-bolt" style="font-size: 36px; color: #6366f1; opacity: 0.5;"></i>
                            </div>
                            <h4 style="font-size: 15px; margin-bottom: 5px; font-weight: 600;">{opt['name']}</h4>
                            <div class="option-rating" style="font-size: 12px; margin-bottom: 10px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> {opt['rating']} <span style="color: #666;">({opt['reviews']} reviews)</span></div>
                            <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 15px;">₹{opt['price']}</div>
                            <button class="option-add-btn" onclick="addToCart('{opt['name']}', {opt['price']}); document.getElementById('{svc_id}-modal').style.display='none';" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #a855f7; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 14px;">Add</button>
                        </div>'''

def make_modal(svc):
    svc_id = svc['id']
    opts_html = ''.join(make_option_card(svc_id, o) for o in svc['options'])
    scroll_btns = f'''<button id="scroll-left-{svc_id}-btn" style="position: absolute; left: -15px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-left" style="font-size: 14px;"></i></button>
                    <button id="scroll-right-{svc_id}-btn" style="position: absolute; right: -15px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-right" style="font-size: 14px;"></i></button>
                    '''
    modal_html = f'''
    <!-- {svc['title']} Modal -->
    <div id="{svc_id}-modal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 1000; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf9; width: 100%; max-width: 600px; padding: 0; overflow: hidden; border-radius: 12px; position: relative;">
            <button id="close-{svc_id}-modal-btn" class="modal-close" style="position: absolute; z-index: 10; background: white; border: none; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; top: 15px; right: 15px; cursor: pointer;"><i class="fa-solid fa-xmark"></i></button>
            
            <div class="options-modal-body" style="padding: 24px;">
                <h3 class="options-modal-title" style="font-size: 24px; margin-bottom: 5px; font-weight: 700;">{svc['title']}</h3>
                <div class="options-rating" style="margin-bottom: 20px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> {svc['rating']} <span style="color: #666; font-weight: 400; text-decoration: underline; text-decoration-style: dotted;">({svc['reviews']} reviews)</span></div>

                <div style="position: relative;">
                    {scroll_btns}
                    <div id="modal-carousel-{svc_id}" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; scrollbar-width: none; scroll-behavior: smooth;">
                    {opts_html}
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('close-{svc_id}-modal-btn').addEventListener('click', function() {{
            document.getElementById('{svc_id}-modal').style.display = 'none';
        }});
        document.getElementById('{svc_id}-modal').addEventListener('click', function(e) {{
            if (e.target === this) {{
                this.style.display = 'none';
            }}
        }});
        document.getElementById('scroll-left-{svc_id}-btn').addEventListener('click', function() {{
            document.getElementById('modal-carousel-{svc_id}').scrollBy({{ left: -200, behavior: 'smooth' }});
        }});
        document.getElementById('scroll-right-{svc_id}-btn').addEventListener('click', function() {{
            document.getElementById('modal-carousel-{svc_id}').scrollBy({{ left: 200, behavior: 'smooth' }});
        }});
    </script>
'''
    return modal_html

# ---- Step 1: Replace the button onclick attributes ----
for svc in SERVICES:
    old_onclick = svc['old_onclick']
    new_onclick = f"document.getElementById('{svc['id']}-modal').style.display='flex'"
    # Match exact onclick attribute
    old_pattern = f'onclick="{old_onclick}"'
    new_pattern = f'onclick="{new_onclick}"'
    if old_pattern in content:
        content = content.replace(old_pattern, new_pattern, 1)
        print(f"[OK] Replaced button onclick for: {svc['title']}")
    else:
        print(f"[WARN] Could not find button for: {svc['title']} | Looking for: {old_pattern}")

# ---- Step 2: Insert all modals before cart-sidebar ----
all_modals = ''
for svc in SERVICES:
    all_modals += make_modal(svc)

# Insert before cart-sidebar div
cart_marker = '    <!-- Cart Sidebar -->'
if cart_marker in content:
    content = content.replace(cart_marker, all_modals + '\n    <!-- Cart Sidebar -->', 1)
    print(f"\n[OK] Inserted {len(SERVICES)} modals before cart sidebar")
else:
    print("[ERROR] Could not find cart sidebar marker!")

with open('electrician.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n[DONE] electrician.html updated successfully.")
