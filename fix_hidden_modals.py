import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the modal overlays by removing the 'hidden' class and adding style="display: none;"
# This prevents the opacity: 0 conflict
content = content.replace('class="modal-overlay hidden"', 'class="modal-overlay" style="display: none; z-index: 10000;"')

# There might also be cases where it's 'hidden modal-overlay'
content = content.replace('class="hidden modal-overlay"', 'class="modal-overlay" style="display: none; z-index: 10000;"')

# And remove it from the cart sidebar if present
content = content.replace('id="cart-sidebar" class="modal-overlay hidden"', 'id="cart-sidebar" class="modal-overlay" style="display: none; z-index: 10000;"')

with open(r'c:\Users\Divyanshi123456\Music\hoamex\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
