import re

# 1. Read plumber.html
with open('plumber.html', 'r', encoding='utf-8') as f:
    plumber_content = f.read()

# 2. Extract all unique modals from recovered_modals.txt
with open('recovered_modals.txt', 'r', encoding='utf-8') as f:
    recovered = f.read()

# Extract modal blocks
modal_pattern = re.compile(r'<!--.*?Modal.*?-->\s*<div id="([a-zA-Z0-9_-]+-modal)".*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
modals_found = {}
for match in modal_pattern.finditer(recovered):
    modal_id = match.group(1)
    if modal_id not in modals_found:
        modals_found[modal_id] = match.group(0)

print(f"Found {len(modals_found)} unique modals to restore.")

# Also generate the setupModal lines
setup_lines = []
for modal_id in modals_found:
    # derive open btn id
    # wait, the open btn id is in plumber.html
    # let's just parse plumber.html to find the button id that opens this modal
    pass

# Wait, in the recovered_modals.txt, we also have the setupModal script block!
# Let's extract the LARGEST setupModal block!
script_pattern = re.compile(r'<script>\s*document\.addEventListener.*?</script>', re.DOTALL)
scripts = script_pattern.findall(recovered)
best_script = max(scripts, key=len) if scripts else ""

# 3. Append them to plumber.html
# We will append right before <style> or </body>
insertion_point = plumber_content.find('    <style>')
if insertion_point == -1:
    insertion_point = plumber_content.find('</body>')

new_content = plumber_content[:insertion_point] + '\n' + '\n'.join(modals_found.values()) + '\n\n    <style>\n    .hidden { display: none !important; }\n    .wm-options-carousel::-webkit-scrollbar { display: none; }\n    </style>\n' + best_script + '\n' + plumber_content[insertion_point:]

# Wait, plumber.html might ALREADY have <style> and <script>.
# We should REPLACE any existing <style> and <script> related to modals.
# Let's just remove existing ones first.
plumber_content = re.sub(r'<style>\s*\.hidden \{ display: none !important; \}\s*\.wm-options-carousel::-webkit-scrollbar \{ display: none; \}\s*</style>', '', plumber_content)
plumber_content = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\s*function setupModal.*?</script>', '', plumber_content, flags=re.DOTALL)

insertion_point = plumber_content.find('</body>')
new_content = plumber_content[:insertion_point] + '\n' + '\n'.join(modals_found.values()) + '\n\n    <style>\n    .hidden { display: none !important; }\n    .wm-options-carousel::-webkit-scrollbar { display: none; }\n    </style>\n' + best_script + '\n' + plumber_content[insertion_point:]

with open('plumber.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Restored modals to plumber.html")
