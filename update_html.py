import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

def get_keyword(alt):
    alt = alt.lower()
    if 'massage' in alt or 'therapy' in alt: return 'massage'
    if 'waxing' in alt or 'pedicure' in alt or 'cleanup' in alt: return 'salon'
    if 'cleaning' in alt or 'clean' in alt: return 'cleaning'
    if 'pest' in alt or 'termite' in alt or 'cockroach' in alt or 'bug' in alt: return 'pest'
    if 'repair' in alt or 'service' in alt or 'purifier' in alt or 'ac' in alt: return 'repair'
    if 'haircut' in alt: return 'haircut'
    return 'lifestyle'

count = 1

def replace_img(match):
    global count
    wrapper_class = match.group(1)
    img_tag = match.group(2)
    
    # Extract src and alt
    src_match = re.search(r'src="([^"]+)"', img_tag)
    alt_match = re.search(r'alt="([^"]+)"', img_tag)
    
    if src_match and alt_match:
        src = src_match.group(1)
        alt = alt_match.group(1)
        
        kw = get_keyword(alt)
        new_src = f"https://loremflickr.com/600/400/{kw}?lock={count}"
        count += 1
        
        new_img_tag = f'<img src="{new_src}" alt="{alt}">'
        return f'<div class="{wrapper_class}">\n                            {new_img_tag}'
    return match.group(0)

# Replace images inside specific wrappers
pattern = r'<div class="(spotlight-img-wrapper|noteworthy-img-wrapper|most-booked-img-wrapper)">\s*(<img[^>]+>)'

new_html = re.sub(pattern, replace_img, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print(f"Replaced {count - 1} images.")
