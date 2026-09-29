import glob, re
from collections import Counter

def clean_html_tags(text):
    return re.sub(r'<[^>]+>', '', text).strip()

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all addToCart calls
    matches = list(re.finditer(r"addToCart\s*\(\s*['\"]([^'\"]+)['\"]\s*,\s*(\d+)\s*\)", content))
    
    items = [m.group(1) for m in matches]
    counts = Counter(items)
    duplicates = set(item for item, count in counts.items() if count > 1)
    
    if not duplicates:
        return False
        
    print(f"Fixing {filename}...")
    
    new_content = ""
    last_idx = 0
    
    for m in matches:
        item_name = m.group(1)
        price = m.group(2)
        start, end = m.span()
        
        new_content += content[last_idx:start]
        
        if item_name in duplicates:
            # Look backwards for the nearest h2 or h3
            search_area = content[:start]
            h_match = list(re.finditer(r"<(h[23])[^>]*>(.*?)</\1>", search_area))
            
            if h_match:
                # Get the last heading before this button
                last_heading = h_match[-1].group(2)
                heading_text = clean_html_tags(last_heading).strip()
                
                # Make sure heading_text isn't empty or the same as item_name
                if heading_text and heading_text.lower() not in item_name.lower():
                    # Create unique name
                    unique_name = f"{heading_text} - {item_name}"
                    # Replace in the addToCart call
                    new_call = f"addToCart('{unique_name}', {price})"
                    new_content += new_call
                    print(f"  Changed '{item_name}' -> '{unique_name}'")
                else:
                    new_content += content[start:end]
            else:
                new_content += content[start:end]
        else:
            new_content += content[start:end]
            
        last_idx = end
        
    new_content += content[last_idx:]
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

total_fixed = 0
for f in glob.glob('*.html'):
    if fix_file(f):
        total_fixed += 1

print(f"Total files fixed: {total_fixed}")
