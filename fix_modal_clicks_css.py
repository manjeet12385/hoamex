import os

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n\n/* Ensure clicks on modal items fall exactly on the a tag */\n.modal-item * { pointer-events: none; }\n')

print("Added pointer-events: none to modal-item children")
