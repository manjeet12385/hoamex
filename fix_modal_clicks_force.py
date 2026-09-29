import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace `<a class="modal-item" href="...` with `<div class="modal-item" onclick="window.location.href='...';" style="cursor: pointer; text-decoration: none;">`
# And then carefully replace the closing `</a>` that corresponds to it.

# Step 1: Find all modal items
blocks = re.split(r'(<a class="modal-item"[^>]*>)', content)
new_content = ""

for i in range(len(blocks)):
    if '<a class="modal-item"' in blocks[i]:
        # Extract href
        href_match = re.search(r'href="([^"]+)"', blocks[i])
        if href_match:
            href = href_match.group(1)
            # Create div equivalent
            blocks[i] = f'<div class="modal-item" onclick="window.location.href=\'{href}\';" style="cursor: pointer; text-decoration: none;">'
            
            # Now we must find the NEXT </a> in blocks[i+1] and change it to </div>
            # Since blocks[i+1] contains the inner HTML and the closing tag up to the next split,
            # we just replace the first </a> with </div>
            blocks[i+1] = blocks[i+1].replace('</a>', '</div>', 1)

new_content = "".join(blocks)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Converted all modal items to divs with onclick.")
