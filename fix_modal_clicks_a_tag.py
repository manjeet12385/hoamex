import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <div class="modal-item" onclick="window.location.href='ac-service.html';" style="...">
# with <a class="modal-item" href="ac-service.html" onclick="window.location.href='ac-service.html'; return false;" style="...">

def repl(match):
    href = match.group(1)
    return f'<a class="modal-item" href="{href}" onclick="window.location.href=\'{href}\'; return false;" style="cursor: pointer; text-decoration: none;">'

new_content = re.sub(r'<div class="modal-item" onclick="window\.location\.href=\'([^\']+)\';" style="cursor: pointer; text-decoration: none;">', repl, content)

# But wait, earlier I also replaced </a> with </div>.
# I need to change the matching </div> back to </a>.
# Since .modal-item is exclusively used here, I can just change all </div> that close a modal item.
# It's safer to just do a global replace for all modal items and then run a script to fix closing tags.

# Actually, the user's issue is clearly caching. The current HTML is 100% valid.
# But I will apply this to ensure maximum compatibility.

# To handle the closing tag, we will split by the new opening tag.
blocks = re.split(r'(<a class="modal-item"[^>]*>)', new_content)
for i in range(1, len(blocks), 2):
    # blocks[i] is the opening tag
    # blocks[i+1] is the content until the next split
    # we need to replace the FIRST </div> in blocks[i+1] with </a>
    blocks[i+1] = blocks[i+1].replace('</div>', '</a>', 1)

new_content = "".join(blocks)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Restored <a> tags with explicit onclick and return false.")
