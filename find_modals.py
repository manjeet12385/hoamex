import re
content = open('recovered_modals.txt', 'r', encoding='utf-8').read()
modals = re.findall(r'<div id="(.*?)" class="modal-overlay', content)
print(list(set(modals)))
