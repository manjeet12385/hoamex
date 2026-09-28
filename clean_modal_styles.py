import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any occurrence of "display: flex;" inside modal-overlay tags with nothing
# Actually, it's safer to just regex replace the style attribute for modal-overlays.
# A simple way: find all modal-overlays and replace 'display: flex;' with ''
# Let's do a targeted regex replace on the div tags that have class="modal-overlay"

def fix_modal_style(match):
    tag = match.group(0)
    # Remove all "display: none;" and "display: flex;" from the tag
    tag = tag.replace('display: none;', '').replace('display: flex;', '')
    # Add display: none; right after style="
    tag = tag.replace('style="', 'style="display: none;')
    return tag

# Find all <div id="..." class="modal-overlay"...>
content = re.sub(r'<div[^>]*class="modal-overlay"[^>]*>', fix_modal_style, content)

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'w', encoding='utf-8') as f:
    f.write(content)
