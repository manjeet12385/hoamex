import re
import glob

with open(r'c:\Users\Divyanshi123456\Music\hoamex\common.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the class name in the modal logic
js = js.replace(".use-location-btn", ".location-btn")

# Add the event listener to open the modal
if "location-modal" in js and "document.querySelectorAll('.location-btn').forEach(btn =>" not in js:
    js += """
// Open location modal on click
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.location-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const modal = document.getElementById('location-modal');
            if (modal) modal.style.display = 'flex';
        });
    });
});
"""
    with open(r'c:\Users\Divyanshi123456\Music\hoamex\common.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Fixed location-btn logic in common.js")

# And bust the cache just in case
html_files = glob.glob(r'c:\Users\Divyanshi123456\Music\hoamex\*.html')
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # update common.js to common.js?v=3002 to bust cache
        new_html = re.sub(r'common\.js(?:\?v=\d+)?', 'common.js?v=3002', html)
        
        if html != new_html:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_html)
    except Exception as e:
        pass
