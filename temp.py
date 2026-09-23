from bs4 import BeautifulSoup
import re

with open('c:/Users/Divyanshi123456/Music/hoamex/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

items = soup.find_all('div', class_='most-booked-item')

for item in items:
    # Check if a button with class add-btn already exists in this item
    if item.find('button', class_='add-btn'):
        continue
    
    title_tag = item.find('h4')
    price_tag = item.find('p', class_='service-price')
    
    if title_tag and price_tag:
        title = title_tag.get_text(strip=True)
        price_str = price_tag.get_text(strip=True).replace('₹', '').replace(',', '')
        
        # We can't safely extract the number if it's not well-formed, but usually it's just the amount.
        match = re.search(r'\d+', price_str)
        if match:
            price_val = match.group(0)
            
            # Create a new button tag
            button = soup.new_tag('button', attrs={
                'class': 'add-btn',
                'onclick': f"addToCart('{title}', {price_val})",
                'style': 'margin-top: auto;'
            })
            button.string = 'Book now'
            
            # Append it to the item
            item.append(button)

# Save the updated HTML
with open('c:/Users/Divyanshi123456/Music/hoamex/index.html', 'w', encoding='utf-8') as f:
    # formatting might change slightly, so we use str(soup) instead of soup.prettify() to keep original as much as possible
    f.write(str(soup))
