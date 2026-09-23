import urllib.request
import re
import os
from urllib.parse import quote
import threading

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

os.makedirs("images", exist_ok=True)
count = 1

def replace_img(match):
    global count
    wrapper_class = match.group(1)
    img_tag = match.group(2)
    
    src_match = re.search(r'src="([^"]+)"', img_tag)
    alt_match = re.search(r'alt="([^"]+)"', img_tag)
    
    if src_match and alt_match:
        alt = alt_match.group(1)
        
        filename = f"real_{count}.jpg"
        filepath = os.path.join("images", filename)
        
        # Download image for this specific alt text
        query = alt + " professional service real photo -vector -clipart -illustration -cartoon"
        url = "https://www.bing.com/images/search?q=" + quote(query) + "&qft=+filterui:photo-photo"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            res_html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
            matches = re.findall(r'murl&quot;:&quot;(http[^&]+(?:jpg|jpeg|png))&quot;', res_html)
            success = False
            if matches:
                for img_url in matches:
                    try:
                        req2 = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                        img_data = urllib.request.urlopen(req2, timeout=5).read()
                        with open(filepath, "wb") as f_img:
                            f_img.write(img_data)
                        print(f"Downloaded {filename} for {alt}")
                        success = True
                        break
                    except:
                        pass
            if not success:
                print(f"Failed to download for {alt}")
        except Exception as e:
            print(f"Error {filename}: {e}")
        
        new_src = f"images/{filename}"
        count += 1
        
        new_img_tag = f'<img src="{new_src}" alt="{alt}">'
        return f'<div class="{wrapper_class}">\n                        {new_img_tag}'
    return match.group(0)

pattern = r'<div class="(spotlight-img-wrapper|noteworthy-img-wrapper|most-booked-img-wrapper|carousel-item)">\s*(<img[^>]+>)'
new_html = re.sub(pattern, replace_img, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)
