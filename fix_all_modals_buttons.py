import os
import re
import glob

def fix_buttons():
    # Regex to find onclick="addToCart(...)" inside a button that also has id="open-...-btn"
    # Actually, it's easier to find button tags with both, and just remove the onclick part.
    
    html_files = glob.glob('*.html')
    count = 0
    
    # Matches <button ... onclick="addToCart('...')" ... id="open-...-btn" ...>
    # Note that onclick might be before or after id.
    
    def replacement_func(match):
        # Full button string
        btn = match.group(0)
        # Check if it has an id that starts with open- and ends with -btn
        if re.search(r'id="open-[a-zA-Z0-9-]*(-options-btn|-modal-btn)"', btn):
            # Remove onclick attribute completely
            new_btn = re.sub(r'\s*onclick="addToCart\([^)]+\)"', '', btn)
            return new_btn
        return btn

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all buttons that contain onclick="addToCart(..."
        new_content = re.sub(r'<button\b[^>]*onclick="addToCart\([^>]+>', replacement_func, content)
        
        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed issues in {file}")
            count += 1
            
    print(f"Total files fixed: {count}")

if __name__ == '__main__':
    fix_buttons()
