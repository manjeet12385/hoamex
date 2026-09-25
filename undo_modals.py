import os, glob, re

def undo_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if "<!-- Modal for " not in content:
        return False

    # Extract all generated modals to map modal_id -> (title, price)
    # Our template had: <div id="{modal_id}" ...
    # And: <h3 ...>{title}</h3>
    # And the first option has: addToCart('{cart_name}',{opt_price})
    # Wait, the option button is: <button class="option-add-btn" onclick="addToCart('{cart_name}',{opt_price})"
    
    # Find all modal blocks
    modal_blocks = re.findall(r'<!-- Modal for .*?(<!-- Modal for |<style>|</body>)', content + '<!-- Modal for ', flags=re.DOTALL)
    # Actually, a better regex to extract modal info:
    modal_info = {}
    
    # Split by "<!-- Modal for "
    parts = content.split('<!-- Modal for ')
    new_content = parts[0]
    
    for part in parts[1:]:
        # Extract modal_id
        m_id = re.search(r'<div id="(modal-[^"]+)"', part)
        # Extract title
        m_title = re.search(r'<h3 class="options-modal-title"[^>]*>(.*?)</h3>', part)
        # Extract first option price
        m_price = re.search(r'onclick="addToCart\(\'(.*?)\',(\d+)\)"', part)
        
        if m_id and m_title and m_price:
            modal_id = m_id.group(1)
            title = m_title.group(1)
            price = m_price.group(2)
            # Some titles had - Option 1 appended in the cart_name, but the original cart_name was usually just the title in our script?
            # Our script did: m_title = re.search(r'<h[34]>(.*?)</h[34]>', row); title = m_title.group(1).strip()
            # Original button: addToCart('{original_cart_name}', {price})
            # Wait, original cart name was captured as m_btn.group(1). Our script DID NOT save the original cart name anywhere!
            # It just used `title` from the h4. The original cart name might be slightly different.
            # But the title is usually exactly the cart name or very close. Let's just use `title` as the cart name.
            modal_info[modal_id] = (title, price)

    # Now replace the buttons in new_content
    # <button onclick="document.getElementById('modal-slug').classList.remove('hidden')" class="add-btn">Add</button>
    def replacer(match):
        modal_id = match.group(1)
        if modal_id in modal_info:
            title, price = modal_info[modal_id]
            # If the file is festival-lights.html, price is not needed? No, addToCart always needs price.
            # Let's restore the button
            # But wait, did original use single quotes? Yes.
            # We'll use the title as the cart name.
            return f'<button class="add-btn" onclick="addToCart(\'{title}\',{price})">Add</button>'
        return match.group(0)

    new_content = re.sub(r'<button onclick="document.getElementById\(\'(modal-[^>]+)\'\)\.classList\.remove\(\'hidden\'\)" class="add-btn">Add</button>', replacer, new_content)

    # Note: Our script also might have added <style>...</style> at the bottom. 
    # Let's clean up empty lines at the end.
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

for file in glob.glob('*.html'):
    if 'fixed' in file: continue
    if undo_file(file):
        print(f"Reverted {file}")
