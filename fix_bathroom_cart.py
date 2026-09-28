import re

with open('bathroom-cleaning.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find a service block, extract its name, price, and the button
# We'll just find all <button style="...">Add</button> and try to figure out what they belong to.

blocks = content.split('<button ')
for i in range(1, len(blocks)):
    if 'Add</button>' in blocks[i] and 'addToCart' not in blocks[i] and 'onclick="document' not in blocks[i]:
        # Look backwards in the previous block to find the h3 or h4 for title
        prev = blocks[i-1]
        
        # Find title
        title_match = re.search(r'<h[34][^>]*>(.*?)</h[34]>', prev)
        if title_match:
            title = title_match.group(1).replace('<br>', ' ').strip()
        else:
            title = "Service"
            
        # Find price
        price_match = re.search(r'₹([0-9,]+)', prev)
        if price_match:
            price = price_match.group(1).replace(',', '')
        else:
            price = "0"
            
        # inject onclick
        blocks[i] = f'onclick="addToCart(\'{title}\', {price})" ' + blocks[i]

new_content = '<button '.join(blocks)

with open('bathroom-cleaning.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating bathroom-cleaning.html buttons!")
