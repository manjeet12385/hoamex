import re
import glob

# 1. Update cart.js
with open(r'c:\Users\Divyanshi123456\Music\hoamex\cart.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("cartSidebar.classList.remove('hidden')", "cartSidebar.style.display = 'flex'")
content = content.replace("cartSidebar.classList.add('hidden')", "cartSidebar.style.display = 'none'")

with open(r'c:\Users\Divyanshi123456\Music\hoamex\cart.js', 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Update version of cart.js in all html files to force reload
html_files = glob.glob(r'c:\Users\Divyanshi123456\Music\hoamex\*.html')
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # update cart.js to cart.js?v=9 (or if it has a v=, update it)
        # Using a simple string replace for common patterns
        new_html = re.sub(r'cart\.js(?:\?v=\d+)?', 'cart.js?v=10', html)
        
        if html != new_html:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_html)
    except Exception as e:
        print(f"Error processing {file}: {e}")
