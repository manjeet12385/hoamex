import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\cart.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the duplicate add to cart issue
# If the button has an inline onclick for addToCart, don't execute the listener logic
content = content.replace("if (onclickAttr.includes('modal')) return;", "if (onclickAttr.includes('modal') || onclickAttr.includes('addToCart')) return;")

# Also provide a fallback image in global addToCart in case querySelector fails or doesn't find it
# First find the global window.addToCart function block
new_add_to_cart = """    window.addToCart = function(title, price) {
        let imgSrc = 'images/new_plumber_icon.jpg'; // fallback
        try {
            // Escape quotes if present to avoid syntax errors
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

content = re.sub(
    r'window\.addToCart\s*=\s*function\(title,\s*price\)\s*\{[^}]*cart\.push[^}]*openCart\(\);\s*\};',
    new_add_to_cart,
    content,
    flags=re.DOTALL
)

with open(r'c:\Users\Divyanshi123456\Music\hoamex\cart.js', 'w', encoding='utf-8') as f:
    f.write(content)
