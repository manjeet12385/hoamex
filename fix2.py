import os
import re

for f in ['bathroom-cleaning.html', 'kitchen-cleaning.html', 'living-bedroom.html', 'full-home-cleaning.html']:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove escaped quotes from previous mistake
    content = content.replace(r'onclick=\"', 'onclick="')
    content = content.replace(r'})\"', '})"')
    
    # Fix the remaining showSection calls with setTimeout
    content = re.sub(
        r'onclick="showSection\(\'[^\']+\'\);\s*setTimeout\(\(\)\s*=>\s*document\.getElementById\(\'([^\']+)\'\)\.scrollIntoView\([^)]+\),\s*\d+\);"|onclick="showSection\(\'[^\']+\'\);"',
        r'onclick="document.getElementById(\'\1\').scrollIntoView({behavior: \'smooth\', block: \'start\'})"',
        content
    )

    # Some remaining ones: onclick="showSection('complete-kitchen-cleaning')"
    content = re.sub(
        r'onclick="showSection\(\'([^\']+)\'\)"',
        r'onclick="document.getElementById(\'\1\').scrollIntoView({behavior: \'smooth\', block: \'start\'})"',
        content
    )

    # Make sections visible
    content = re.sub(r'id="([^"]+)" style="display:\s*none;\s*', r'id="\1" style="', content)

    # Also remove showSection definition
    content = re.sub(r'function showSection\(sectionId\)\s*\{[^}]+\}', '// Smooth scrolling is handled via inline onclick attributes.', content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Fixed {f}")
