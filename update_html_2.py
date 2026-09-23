import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

count = 43

def replace_img(match):
    global count
    wrapper_class = match.group(1)
    img_tag = match.group(2)
    
    src_match = re.search(r'src="([^"]+)"', img_tag)
    alt_match = re.search(r'alt="([^"]+)"', img_tag)
    
    if src_match and alt_match:
        alt = alt_match.group(1)
        kw = 'repair' if 'Plumb' in alt or 'repair' in alt else 'home'
        new_src = f"https://loremflickr.com/600/400/{kw}?lock={count}"
        count += 1
        
        new_img_tag = f'<img src="{new_src}" alt="{alt}">'
        return f'<div class="{wrapper_class}">\n                        {new_img_tag}'
    return match.group(0)

pattern = r'<div class="(carousel-item)">\s*(<img[^>]+>)'
new_html = re.sub(pattern, replace_img, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Updated top carousel.")
