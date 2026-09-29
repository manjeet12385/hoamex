import glob, re
from collections import Counter

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    items = re.findall(r"addToCart\s*\(\s*['\"]([^'\"]+)['\"]", content)
    counts = Counter(items)
    duplicates = {item: count for item, count in counts.items() if count > 1}
    
    if duplicates:
        print(f'Duplicates in {f}:')
        for item, count in duplicates.items():
            print(f'  - "{item}" appears {count} times')
