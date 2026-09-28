import os
import re

file_path = "c:/Users/Divyanshi123456/Music/hoamex/plumber.html"
if not os.path.exists(file_path):
    print("File not found")
else:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    cart_html = """
    <!-- Cart Sidebar -->
    <div class="modal-overlay hidden" id="cart-sidebar" style="z-index: 1000;">
        <div class="modal-content" style="max-width: 400px; height: 100%; position: absolute; right: 0; top: 0; border-radius: 0; display: flex; flex-direction: column; background: #fff;">
            <button class="modal-close" id="close-cart-btn" style="right: auto; left: -40px; top: 15px; color: white; background: rgba(0,0,0,0.5);"><i class="fa-solid fa-xmark"></i></button>
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
    """

    if 'id="cart-sidebar"' not in content:
        # Append to the end of the file
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(cart_html)
        print("Added cart-sidebar to plumber.html")
    else:
        print("cart-sidebar already exists in plumber.html")
