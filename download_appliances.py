import urllib.request
import os

pages = [
    'washing-machine.html',
    'refrigerator.html',
    'television.html',
    'chimney.html',
    'microwave.html',
    'water-purifier.html'
]

base_url = 'https://hoamex.vercel.app/'

for page in pages:
    try:
        print(f"Downloading {page} from Vercel...")
        urllib.request.urlretrieve(base_url + page, page)
        print(f"Successfully downloaded {page}")
    except Exception as e:
        print(f"Error downloading {page}: {e}")

print("All downloads complete.")
