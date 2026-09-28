import glob
import re

files = glob.glob('*.html')
total_fixed = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if 'onclick="addToCart' not in content:
        continue
        
    # Split by <button 
    blocks = content.split('<button ')
    modified = False
    
    for i in range(1, len(blocks)):
        # Check if the button block has TWO onclick attributes
        # My script added: onclick="addToCart('Title', 299)" 
        # So it looks like: onclick="addToCart('Title', 299)" class="add-btn" onclick="openSomething()" ... >
        
        # We can find all onclick attributes in the button opening tag
        # The button opening tag ends at the first '>'
        tag_end = blocks[i].find('>')
        if tag_end != -1:
            tag_content = blocks[i][:tag_end]
            
            # Find all onclick="something" or onclick='something'
            onclicks = re.findall(r'onclick\s*=\s*(["\'])(.*?)\1', tag_content)
            
            if len(onclicks) >= 2:
                # We have at least two onclick attributes.
                # Remove the one that starts with addToCart
                # Replace the exact string `onclick="addToCart(X, Y)" `
                
                # Let's do a regex substitution on the tag_content
                # Matches: onclick="addToCart(.*?)" 
                new_tag_content = re.sub(r'onclick\s*=\s*["\']addToCart\([^)]+\)["\']\s*', '', tag_content)
                
                if new_tag_content != tag_content:
                    blocks[i] = new_tag_content + blocks[i][tag_end:]
                    modified = True
                    total_fixed += 1

    if modified:
        new_content = '<button '.join(blocks)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)

print(f"Fixed {total_fixed} duplicate buttons across all HTML files.")
