import os
import glob

# We will replace the <a class="modal-item"...> with a <div class="modal-item"...> for the AC link

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We need to replace the entire <a> tag structure for AC
    # The structure is roughly:
    # <a class="modal-item" href="ac-service.html" ...>
    # ...
    # </a>
    
    # Let's do a simple string replace for the opening tag
    if '<a class="modal-item" href="ac-service.html"' in content or '<a href="ac-service.html" class="modal-item"' in content:
        # replace opening tag
        content = content.replace('<a class="modal-item" href="ac-service.html" onclick="window.location.href=\'ac-service.html\'" style="text-decoration: none;">', '<div class="modal-item" onclick="window.location.href=\'ac-service.html\';" style="text-decoration: none;">')
        content = content.replace('<a class="modal-item" href="ac-service.html" style="text-decoration: none;">', '<div class="modal-item" onclick="window.location.href=\'ac-service.html\';" style="text-decoration: none;">')
        content = content.replace('<a href="ac-service.html" class="modal-item" onclick="window.location.href=\'ac-service.html\'" style="text-decoration: none;">', '<div class="modal-item" onclick="window.location.href=\'ac-service.html\';" style="text-decoration: none;">')
        
        # Now we need to replace the closing </a> but ONLY the one immediately following this.
        # Since it's tricky with simple replace, let's use regex or just replace all </a> that come right after AC</p>
        content = content.replace('<p style="margin-top: 10px;">AC</p>\n</a>', '<p style="margin-top: 10px;">AC</p>\n</div>')
        content = content.replace('<p style="margin-top: 10px;">AC</p></a>', '<p style="margin-top: 10px;">AC</p></div>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath} to use DIV instead of A tag for AC")

print("Done")
