import os
import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

new_epc_modal = '''
    <!-- EPC Modal -->
    <div id="epc-modal" class="modal-overlay hidden">
        <div class="modal-content" style="max-width: 600px;">
            <button id="close-epc-modal-btn" class="modal-close"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="modal-title">Electrician, Plumber & Carpenter</h3>
            
            <h4 class="modal-subtitle">Repairs</h4>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="electrician.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/electrician_icon.jpg" alt="Electrician"><p>Electrician</p>
                </a>
                <a href="plumber.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/plumber.jpg" alt="Plumber"><p>Plumber</p>
                </a>
                <a href="carpenter.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/carpenter_icon.jpg" alt="Carpenter"><p>Carpenter</p>
                </a>
                <a href="wood-polish.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/renovation.jpg" alt="Wood Polish"><p>Wood & Furniture Polish</p>
                </a>
            </div>

            <h4 class="modal-subtitle">Installations & other services</h4>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px;">
                <a href="fan-installation.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/tools.jpg" alt="Fan"><p>Fan Installation</p>
                </a>
                <a href="furniture-assembly.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/carpenter_icon.jpg" alt="Assembly"><p>Furniture Assembly</p>
                </a>
                <a href="geyser-service.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/plumber.jpg" alt="Geyser"><p>Geyser Service & Repair</p>
                </a>
                <a href="ikea-assembly.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/tools.jpg" alt="IKEA"><p>IKEA Furniture Assembly</p>
                </a>
                <a href="tile-grouting.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/cleaning.jpg" alt="Tile"><p>Tile Grouting & Sealant</p>
                </a>
                <a href="festival-lights.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/electrician_icon.jpg" alt="Lights"><p>Festival Lights Installation</p>
                </a>
                <a href="wall-panels.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/renovation.jpg" alt="Panels"><p>Wall Panels by Revamp</p>
                </a>
            </div>
        </div>
    </div>
'''

# Find existing epc-modal and replace it
# It looks like <!-- EPC Modal --> ... </div>
idx_content = re.sub(r'<!-- EPC Modal -->.*?</div>\s*</div>\s*</div>', new_epc_modal, idx_content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

# 2. Build the generic pages
with open('cctv-services.html', 'r', encoding='utf-8') as f:
    template = f.read()
    
# Remove existing header from template because it might be hardcoded in cctv
template = re.sub(r'<header.*?</header>', '<div id="header-placeholder"></div>', template, flags=re.DOTALL | re.IGNORECASE)
if '<script src="common.js"></script>' not in template:
    template = template.replace('</body>', '    <script src="common.js"></script>\n    <script src="cart.js"></script>\n</body>')
if 'id="cart-sidebar"' not in template:
    cart_html = '''
    <!-- Cart Sidebar -->
    <div id="cart-sidebar" class="modal-overlay hidden" style="z-index: 1000;">
        <div class="modal-content" style="max-width: 400px; height: 100%; position: absolute; right: 0; top: 0; border-radius: 0; display: flex; flex-direction: column; background: #fff;">
            <button id="close-cart-btn" class="modal-close" style="right: auto; left: -40px; top: 15px; color: white; background: rgba(0,0,0,0.5);"><i class="fa-solid fa-xmark"></i></button>
            <div style="padding: 20px; border-bottom: 1px solid #eee;">
                <h2 style="margin: 0; font-size: 20px;">Your Cart</h2>
            </div>
            <div id="cart-items-container" style="flex: 1; overflow-y: auto; padding: 20px;">
            </div>
            <div style="padding: 20px; border-top: 1px solid #eee; background: #f9f9f9;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 15px; font-weight: bold; font-size: 18px;">
                    <span>Total:</span>
                    <span id="cart-total-price">₹0</span>
                </div>
                <button id="checkout-btn" style="width: 100%; padding: 15px; background: #000; color: #fff; border: none; border-radius: 8px; font-size: 16px; font-weight: bold; cursor: pointer;">Proceed to Checkout</button>
            </div>
        </div>
    </div>
'''
    template = template.replace('</body>', cart_html + '\n</body>')

pages = [
    ('electrician.html', 'Electrician Services'),
    ('plumber.html', 'Plumbing Services'),
    ('carpenter.html', 'Carpenter Services'),
    ('wood-polish.html', 'Wood & Furniture Polish'),
    ('fan-installation.html', 'Fan Installation'),
    ('furniture-assembly.html', 'Furniture Assembly'),
    ('geyser-service.html', 'Geyser Service & Repair'),
    ('ikea-assembly.html', 'IKEA Furniture Assembly'),
    ('tile-grouting.html', 'Tile Grouting & Sealant'),
    ('festival-lights.html', 'Festival Lights Installation'),
    ('wall-panels.html', 'Wall Panels by Revamp')
]

for filename, title in pages:
    new_html = template.replace('CCTV Camera Services', title)
    new_html = new_html.replace('CCTV Camera Installation', title)
    with open(filename, 'w', encoding='utf-8') as out:
        out.write(new_html)
        
print("Updated index.html and generated 11 EPC pages.")
