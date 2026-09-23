import urllib.request
import re
from urllib.parse import quote, unquote
import os
import random

queries = {
    "spotlight_1.jpg": "bathroom cleaning service professional",
    "spotlight_2.jpg": "full home cleaning service",
    "spotlight_3.jpg": "sofa cleaning service professional",
    "spotlight_4.jpg": "pest control professional",
    "spotlight_5.jpg": "termite control professional",
    "spotlight_6.jpg": "bed bug control professional",
    
    "noteworthy_1.jpg": "water purifier repair service",
    "noteworthy_2.jpg": "geyser repair service",
    "noteworthy_3.jpg": "washing machine repair service",
    "noteworthy_4.jpg": "refrigerator repair service",
    "noteworthy_5.jpg": "microwave repair service",
    "noteworthy_6.jpg": "tv repair service",
    "noteworthy_7.jpg": "ro water purifier service",
    "noteworthy_8.jpg": "kitchen chimney repair service",
    "noteworthy_9.jpg": "inverter repair service",
    
    "booked_1.jpg": "ac repair technician",
    "booked_2.jpg": "haircut men salon",
    "booked_3.jpg": "foam jet ac service",
    "booked_4.jpg": "water purifier installation",
    "booked_5.jpg": "roll on waxing salon",
    
    "salon_1.jpg": "waxing salon woman",
    "salon_2.jpg": "pedicure woman salon",
    "salon_3.jpg": "face cleanup salon",
    "salon_4.jpg": "spatula waxing salon",
    
    "spa_1.jpg": "leg massage therapy spa",
    "spa_2.jpg": "comfort therapy massage spa",
    "spa_3.jpg": "stress relief massage spa",
    "spa_4.jpg": "full body massage scrub",
    "spa_5.jpg": "back relief massage spa",
    
    "clean_1.jpg": "dining table cleaning",
    "clean_2.jpg": "apartment termite control",
    "clean_3.jpg": "cockroach control kitchen",
    "clean_4.jpg": "cockroach pest control",
    "clean_5.jpg": "bed bug exterminator",
    
    "salon_men_1.jpg": "haircut men professional",
    "salon_men_2.jpg": "haircut boy professional",
    "salon_men_3.jpg": "head neck shoulder massage men",
    "salon_men_4.jpg": "pedicure men salon",
    "salon_men_5.jpg": "express pedicure men salon"
}

os.makedirs("images", exist_ok=True)

def download_image(query, filename):
    url = "https://html.duckduckgo.com/html/?q=" + quote(query + " stock photo")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        matches = re.findall(r'src="//external-content\.duckduckgo\.com/iu/\?u=([^&]+)', html)
        if matches:
            for img_url in matches:
                img_url = unquote(img_url)
                if img_url.lower().endswith(('.jpg', '.jpeg', '.png')):
                    req2 = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                    img_data = urllib.request.urlopen(req2, timeout=10).read()
                    with open(os.path.join("images", filename), "wb") as f:
                        f.write(img_data)
                    return True
    except Exception as e:
        print(f"Error for {query}: {e}")
    return False

for filename, query in queries.items():
    success = download_image(query, filename)
    if not success:
        print(f"Failed {filename}")
