import os
import re

for f in ['bathroom-cleaning.html', 'kitchen-cleaning.html', 'living-bedroom.html', 'full-home-cleaning.html']:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace onclick for showSection
    content = re.sub(r"onclick=\"showSection\('([^']+)'\)\"", r"onclick=\"document.getElementById('\1').scrollIntoView({behavior: 'smooth', block: 'start'})\"", content)
    
    # Remove display: none; from specific sections
    content = re.sub(r'id=\"weekly-plans\" style=\"display:\s*none;\s*', 'id=\"weekly-plans\" style=\"', content)
    content = re.sub(r'id=\"value-deals\" style=\"display:\s*none;\s*', 'id=\"value-deals\" style=\"', content)
    content = re.sub(r'id=\"one-time-service\" style=\"display:\s*none;\s*', 'id=\"one-time-service\" style=\"', content)
    content = re.sub(r'id=\"mini-services\" style=\"display:\s*none;\s*', 'id=\"mini-services\" style=\"', content)
    
    # Also remove the whole showSection function block
    content = re.sub(r'function showSection\(sectionId\)\s*\{[^}]+\}', '// Smooth scrolling is handled via inline onclick attributes.', content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")
