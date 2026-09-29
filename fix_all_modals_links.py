import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    full_tag = match.group(0)
    href_val = match.group(1)
    
    # Skip if onclick already exists
    if 'onclick' in full_tag:
        return full_tag
        
    # Inject onclick right after href
    return full_tag.replace(f'href="{href_val}"', f'href="{href_val}" onclick="window.location.href=\'{href_val}\';"')

# Match <a ... class="modal-item" ... href="something.html" ...>
new_content = re.sub(r'<a\s+(?:[^>]*?\s+)?class="modal-item"[^>]*?\s+href="([^"]+)"[^>]*>', replacer, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html with inline onclick for all modal items")
