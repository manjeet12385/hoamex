import os
import re

for f in ['bathroom-cleaning.html', 'kitchen-cleaning.html', 'living-bedroom.html', 'full-home-cleaning.html']:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Hide default-banner
    content = re.sub(r'id="default-banner"[^>]*>', 'id="default-banner" style="display: none;">', content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Fixed default-banner in {f}')
