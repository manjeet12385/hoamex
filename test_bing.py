import urllib.request
import re
from urllib.parse import quote

query = "cockroach control real service"
url = "https://www.bing.com/images/search?q=" + quote(query)
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
    matches = re.findall(r'murl&quot;:&quot;(http[^&]+(?:jpg|jpeg|png))&quot;', html)
    if matches:
        print("Success!", matches[0])
    else:
        print("No matches")
except Exception as e:
    print(e)
