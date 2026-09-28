import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\cart.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the addToCart logic at the end
old_block = """    window.addToCart = function(title, price) {
        let imgSrc = '';
        const imgEl = document.querySelector(`img[alt="${title}"]`);
        if (imgEl) {
            imgSrc = imgEl.src;
        }
        cart.push({ title, price, imgSrc, id: Date.now() });
        saveCart();
        updateCartUI();
        openCart();
    };"""

new_block = """    window.addToCart = function(title, price) {
        let imgSrc = 'images/new_plumber_icon.jpg'; // fallback
        try {
            const safeTitle = title.replace(/"/g, '\\\\\"');
            const imgEl = document.querySelector(`img[alt="${safeTitle}"]`);
            if (imgEl && imgEl.src) {
                imgSrc = imgEl.src;
            }
        } catch(e) {}
        cart.push({ title, price, imgSrc, id: Date.now() });
        saveCart();
        updateCartUI();
        openCart();
    };"""

content = content.replace(old_block, new_block)

with open(r'c:\Users\Divyanshi123456\Music\hoamex\cart.js', 'w', encoding='utf-8') as f:
    f.write(content)
