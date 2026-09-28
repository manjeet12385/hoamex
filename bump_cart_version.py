import re
import glob

html_files = glob.glob(r'c:\Users\Divyanshi123456\Music\hoamex\*.html')
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # update cart.js to cart.js?v=11 to bust cache
        new_html = re.sub(r'cart\.js(?:\?v=\d+)?', 'cart.js?v=11', html)
        
        if html != new_html:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_html)
    except Exception as e:
        print(f"Error processing {file}: {e}")
