import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure all modals use inline display:none and don't have the .hidden class
content = content.replace('class="modal-overlay hidden" style="', 'class="modal-overlay" style="display: none; ')
content = content.replace('class="modal-overlay hidden"', 'class="modal-overlay" style="display: none;"')

# Just to be 100% sure we didn't double up display: none
content = content.replace('display: none; display: none;', 'display: none;')
content = content.replace('display: none; display: flex;', 'display: flex;')

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'w', encoding='utf-8') as f:
    f.write(content)
