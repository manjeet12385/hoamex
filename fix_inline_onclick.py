import os
import glob

# We will look through index.html and any other html file and add an inline onclick to any modal-item

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<a class="modal-item" href="ac-service.html"' in content or '<a href="ac-service.html" class="modal-item"' in content:
        # replace to include onclick
        content = content.replace('<a class="modal-item" href="ac-service.html"', '<a class="modal-item" href="ac-service.html" onclick="window.location.href=\'ac-service.html\'"')
        content = content.replace('<a href="ac-service.html" class="modal-item"', '<a href="ac-service.html" class="modal-item" onclick="window.location.href=\'ac-service.html\'"')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath} with inline onclick for AC")

print("Done")
