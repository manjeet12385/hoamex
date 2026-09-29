import os
import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<div class="modal-item" onclick="window.location.href=\'ac-service.html\';" style="text-decoration: none;">' in content:
        content = content.replace('<div class="modal-item" onclick="window.location.href=\'ac-service.html\';" style="text-decoration: none;">', '<a class="modal-item" href="ac-service.html" style="text-decoration: none;">')
        content = content.replace('<p style="margin-top: 10px;">AC</p>\n</div>', '<p style="margin-top: 10px;">AC</p>\n</a>')
        content = content.replace('<p style="margin-top: 10px;">AC</p></div>', '<p style="margin-top: 10px;">AC</p></a>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Reverted {filepath}")

print("Done")
