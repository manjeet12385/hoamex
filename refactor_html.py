import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ('header.html', 'footer.html')]

for file_name in html_files:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace header
    content = re.sub(r'<header.*?</header>', '<div id="header-placeholder"></div>', content, flags=re.DOTALL | re.IGNORECASE)
    
    # 2. Add scripts before </body> if not present
    if '<script src="common.js"></script>' not in content:
        content = content.replace('</body>', '    <script src="common.js"></script>\n    <script src="cart.js"></script>\n</body>')
    
    # 3. Add Cart sidebar HTML before common.js
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
    
print("Updated all HTML files with header-placeholder, scripts, and cart sidebar.")
