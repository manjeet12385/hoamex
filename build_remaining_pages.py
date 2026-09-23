import sys

with open('cctv-services.html', 'r', encoding='utf-8') as f:
    template = f.read()

pages_to_build = [
    # AC & Appliance
    ('ac-repair.html', 'AC Repair'), ('washing-machine.html', 'Washing Machine'), ('fridge.html', 'Refrigerator'),
    # EPC
    ('plumber.html', 'Plumber Services'), ('electrician.html', 'Electrician'), ('carpenter.html', 'Carpenter'),
    # Cleaning
    ('full-home-cleaning.html', 'Full Home Cleaning'), ('pest-control.html', 'Pest Control'),
    # Reno
    ('full-home-renovation.html', 'Full Home Renovation'), ('painting.html', 'Painting'),
    # Beauty
    ('salon-women.html', 'Salon for Women'), ('spa-women.html', 'Spa for Women'),
    # Grooming
    ('salon-men.html', 'Salon for Men'), ('massage-men.html', 'Massage for Men')
]

for filename, title in pages_to_build:
    new_html = template.replace('CCTV Camera Services', title)
    new_html = new_html.replace('CCTV Camera Installation', title + ' Services')
    # strip existing header out and replace with common placeholder to respect Phase 1 logic
    import re
    new_html = re.sub(r'<header.*?</header>', '<div id="header-placeholder"></div>', new_html, flags=re.DOTALL | re.IGNORECASE)
    if '<script src="common.js"></script>' not in new_html:
        new_html = new_html.replace('</body>', '    <script src="common.js"></script>\n    <script src="cart.js"></script>\n</body>')
    with open(filename, 'w', encoding='utf-8') as out:
        out.write(new_html)

# Update index.html links for the newly created modals
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Update AC modal links
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/ac.jpg" alt="AC"><p>AC Repair</p></a>',
                  '<a href="ac-repair.html" class="modal-item" style="text-decoration: none;"><img src="images/ac.jpg" alt="AC"><p>AC Repair</p></a>')
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/tools.jpg" alt="Washing"><p>Washing Machine</p></a>',
                  '<a href="washing-machine.html" class="modal-item" style="text-decoration: none;"><img src="images/tools.jpg" alt="Washing"><p>Washing Machine</p></a>')
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/homecare.jpg" alt="Fridge"><p>Refrigerator</p></a>',
                  '<a href="fridge.html" class="modal-item" style="text-decoration: none;"><img src="images/homecare.jpg" alt="Fridge"><p>Refrigerator</p></a>')

# Update EPC
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/plumber.jpg" alt="Plumber"><p>Plumber</p></a>',
                  '<a href="plumber.html" class="modal-item" style="text-decoration: none;"><img src="images/plumber.jpg" alt="Plumber"><p>Plumber</p></a>')
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/tools.jpg" alt="Electrician"><p>Electrician</p></a>',
                  '<a href="electrician.html" class="modal-item" style="text-decoration: none;"><img src="images/tools.jpg" alt="Electrician"><p>Electrician</p></a>')
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/carpenter.jpg" alt="Carpenter"><p>Carpenter</p></a>',
                  '<a href="carpenter.html" class="modal-item" style="text-decoration: none;"><img src="images/carpenter.jpg" alt="Carpenter"><p>Carpenter</p></a>')

# Update Cleaning
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/cleaning.jpg" alt="Cleaning"><p>Full Home Cleaning</p></a>',
                  '<a href="full-home-cleaning.html" class="modal-item" style="text-decoration: none;"><img src="images/cleaning.jpg" alt="Cleaning"><p>Full Home Cleaning</p></a>')
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/homecare.jpg" alt="Pest"><p>Pest Control</p></a>',
                  '<a href="pest-control.html" class="modal-item" style="text-decoration: none;"><img src="images/homecare.jpg" alt="Pest"><p>Pest Control</p></a>')

# Update Reno
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/renovation.jpg" alt="Reno"><p>Full Home Renovation</p></a>',
                  '<a href="full-home-renovation.html" class="modal-item" style="text-decoration: none;"><img src="images/renovation.jpg" alt="Reno"><p>Full Home Renovation</p></a>')
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/painter.jpg" alt="Paint"><p>Painting</p></a>',
                  '<a href="painting.html" class="modal-item" style="text-decoration: none;"><img src="images/painter.jpg" alt="Paint"><p>Painting</p></a>')

# Update Beauty
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/beauty.jpg" alt="Beauty"><p>Salon for Women</p></a>',
                  '<a href="salon-women.html" class="modal-item" style="text-decoration: none;"><img src="images/beauty.jpg" alt="Beauty"><p>Salon for Women</p></a>')
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/grooming.jpg" alt="Spa"><p>Spa for Women</p></a>',
                  '<a href="spa-women.html" class="modal-item" style="text-decoration: none;"><img src="images/grooming.jpg" alt="Spa"><p>Spa for Women</p></a>')

# Update Grooming
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/grooming.jpg" alt="Men"><p>Salon for Men</p></a>',
                  '<a href="salon-men.html" class="modal-item" style="text-decoration: none;"><img src="images/grooming.jpg" alt="Men"><p>Salon for Men</p></a>')
idx = idx.replace('<a href="#" class="modal-item" style="text-decoration: none;"><img src="images/beauty.jpg" alt="Massage"><p>Massage for Men</p></a>',
                  '<a href="massage-men.html" class="modal-item" style="text-decoration: none;"><img src="images/beauty.jpg" alt="Massage"><p>Massage for Men</p></a>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

# also run the refactor_html.py logic on the new files so they get the cart sidebar
import os
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ('header.html', 'footer.html')]
for file_name in html_files:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'id="cart-sidebar"' not in content:
        cart_html = '''
    <!-- Cart Sidebar -->
    <div id="cart-sidebar" class="modal-overlay hidden" style="z-index: 1000;">
        <div class="modal-content" style="max-width: 400px; height: 100%; position: absolute; right: 0; top: 0; border-radius: 0; display: flex; flex-direction: column; background: #fff;">
            <button id="close-cart-btn" class="modal-close" style="right: auto; left: -40px; top: 15px; color: white; background: rgba(0,0,0,0.5);"><i class="fa-solid fa-xmark"></i></button>
            <div style="padding: 20px; border-bottom: 1px solid #eee;">
                <h2 style="margin: 0; font-size: 20px;">Your Cart</h2>
            </div>
            <div id="cart-items-container" style="flex: 1; overflow-y: auto; padding: 20px;">
                <!-- Items will be injected here -->
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
        content = content.replace('</body>', cart_html + '\n</body>')
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(content)

print("Generated all 14 placeholder pages and linked them.")
