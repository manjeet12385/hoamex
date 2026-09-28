import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\cart.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update the event listener to include .option-add-btn
js = js.replace("document.querySelectorAll('.add-btn').forEach(btn => {", "document.querySelectorAll('.add-btn, .option-add-btn').forEach(btn => {")

# 2. Update the card selector in the event listener
old_card_selector = "const card = e.target.closest('.service-card') || e.target.closest('.svc-row');"
new_card_selector = "const card = e.target.closest('.service-card') || e.target.closest('.svc-row') || e.target.closest('.plan-card') || e.target.closest('.option-card') || e.target.closest('.most-booked-item');"
js = js.replace(old_card_selector, new_card_selector)

# 3. Update the titleEl selector
js = js.replace("const titleEl = card.querySelector('h4');", "const titleEl = card.querySelector('h4, h3');")

# 4. Update the priceEl selector
old_price_selector = "const priceEl = card.querySelector('.service-price span') || card.querySelector('.price span');"
new_price_selector = "const priceEl = card.querySelector('.service-price span, .price span, .plan-price, .option-price');"
js = js.replace(old_price_selector, new_price_selector)

# 5. Update syncButtonsOnPage selector
js = js.replace("document.querySelectorAll('.add-btn').forEach(btn => {", "document.querySelectorAll('.add-btn, .option-add-btn').forEach(btn => {")

# 6. Update sync card selector
old_sync_card = "const card = btn.closest('.service-card') || btn.closest('.svc-row');"
new_sync_card = "const card = btn.closest('.service-card') || btn.closest('.svc-row') || btn.closest('.plan-card') || btn.closest('.option-card') || btn.closest('.most-booked-item');"
js = js.replace(old_sync_card, new_sync_card)

# 7. Update sync title selector
js = js.replace("const titleEl = card.querySelector('h4');", "const titleEl = card.querySelector('h4, h3');")

with open(r'c:\Users\Divyanshi123456\Music\hoamex\cart.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated cart.js to support more card classes")
