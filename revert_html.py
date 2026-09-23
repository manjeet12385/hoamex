import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

def get_placeholder(alt):
    alt = alt.lower()
    if 'massage' in alt or 'grooming' in alt or 'haircut' in alt: return 'images/grooming.jpg'
    if 'waxing' in alt or 'pedicure' in alt or 'cleanup' in alt or 'spa' in alt or 'beauty' in alt: return 'images/beauty.jpg'
    if 'cleaning' in alt or 'clean' in alt: return 'images/cleaning.jpg'
    if 'pest' in alt or 'termite' in alt or 'cockroach' in alt or 'bug' in alt: return 'images/cleaning.jpg'
    if 'purifier' in alt or 'plumb' in alt or 'water' in alt or 'geyser' in alt: return 'images/plumber.jpg'
    if 'ac ' in alt or 'air' in alt: return 'images/ac.jpg'
    if 'repair' in alt or 'machine' in alt or 'tv ' in alt or 'microwave' in alt or 'refrigerator' in alt: return 'images/tools.jpg'
    if 'paint' in alt: return 'images/painter.jpg'
    if 'kitchen' in alt: return 'images/kitchen.jpg'
    if 'carpenter' in alt or 'sofa' in alt: return 'images/carpenter.jpg'
    return 'images/homecare.jpg'

def replace_img(match):
    wrapper_class = match.group(1)
    img_tag = match.group(2)
    
    src_match = re.search(r'src="([^"]+)"', img_tag)
    alt_match = re.search(r'alt="([^"]+)"', img_tag)
    
    if src_match and alt_match:
        alt = alt_match.group(1)
        new_src = get_placeholder(alt)
        
        # Add spaces based on wrapper to maintain exact indentation
        if wrapper_class == "carousel-item":
            new_img_tag = f'<img src="{new_src}" alt="{alt}">'
            return f'<div class="{wrapper_class}">\n                        {new_img_tag}'
        else:
            new_img_tag = f'<img src="{new_src}" alt="{alt}">'
            return f'<div class="{wrapper_class}">\n                            {new_img_tag}'
    return match.group(0)

pattern = r'<div class="(spotlight-img-wrapper|noteworthy-img-wrapper|most-booked-img-wrapper|carousel-item)">\s*(<img[^>]+>)'
new_html = re.sub(pattern, replace_img, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)
