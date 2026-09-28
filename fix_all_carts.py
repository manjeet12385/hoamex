import glob
import re

files = glob.glob('*.html')

total_buttons_fixed = 0

for f in files:
    # Skip non-service files
    if f in ['index.html', 'checkout.html', 'footer.html', 'header.html', 'categories.html']:
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if '<button ' not in content:
        continue
        
    blocks = content.split('<button ')
    modified = False
    
    for i in range(1, len(blocks)):
        # Look for buttons that say "Add" or "ADD"
        if re.search(r'>\s*(Add|ADD)\s*</button>', blocks[i], re.IGNORECASE) and 'addToCart' not in blocks[i] and 'onclick="document' not in blocks[i]:
            prev = blocks[i-1]
            
            # Find title
            # Try to find nearest h3, h4, or h5, or div with class containing title/name
            # A common pattern is `<h3 ...>Title</h3>`
            title_match = re.findall(r'<h[345][^>]*>(.*?)</h[345]>', prev)
            if not title_match:
                # Try finding a div with strong or some title class
                title_match = re.findall(r'<div[^>]*class="[^"]*title[^"]*"[^>]*>(.*?)</div>', prev, re.IGNORECASE)
            
            if title_match:
                # Get the last matched title, which is closest to the button
                title_raw = title_match[-1]
                # Clean up HTML tags inside title (like <br>, <span>, etc.)
                title = re.sub(r'<[^>]+>', ' ', title_raw).strip()
            else:
                # Fallback to file name based title
                title = f.replace('.html', '').replace('-', ' ').title() + " Service"
                
            # Find price
            # We look for the last occurrence of ₹ or Rs. in the previous block
            price_match = re.findall(r'(?:₹|Rs\.?)\s*([0-9,]+)', prev)
            if price_match:
                price_str = price_match[-1].replace(',', '')
                price = int(price_str)
            else:
                price = 299 # Default placeholder price
                
            # inject onclick
            # Escape single quotes in title
            safe_title = title.replace("'", "\\'")
            blocks[i] = f'onclick="addToCart(\'{safe_title}\', {price})" ' + blocks[i]
            modified = True
            total_buttons_fixed += 1
            
    if modified:
        new_content = '<button '.join(blocks)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
            
print(f"Done! Fixed {total_buttons_fixed} buttons across all files.")
