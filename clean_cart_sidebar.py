import re
import glob

html_files = glob.glob(r'c:\Users\Divyanshi123456\Music\hoamex\*.html')
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # We need to find the cart-sidebar div and fix it.
        # It usually looks like: <div class="modal-overlay" id="cart-sidebar">
        # or with duplicate styles. Let's just use regex to replace the entire start tag of cart-sidebar.
        
        # Match <div ... id="cart-sidebar" ... >
        # Be careful not to match too much.
        new_html = re.sub(
            r'<div[^>]*id="cart-sidebar"[^>]*>', 
            '<div class="modal-overlay" id="cart-sidebar" style="display: none; z-index: 10000;">', 
            html
        )
        
        if html != new_html:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_html)
    except Exception as e:
        print(f"Error processing {file}: {e}")
