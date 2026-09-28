import os

file_path = "c:/Users/Divyanshi123456/Music/hoamex/salon-luxe.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the specific occurrences
content = content.replace(
    'onclick="document.getElementById(\'spatula-wax-modal\').style.display=\'none\'"',
    'onclick="addToCart(\'Spatula Waxing\', 1259); document.getElementById(\'spatula-wax-modal\').style.display=\'none\'"'
)

content = content.replace(
    'onclick="document.getElementById(\'spatula-wax-modal\').classList.add(\'hidden\')"',
    'onclick="addToCart(\'Moroccon honey\', 1039); document.getElementById(\'spatula-wax-modal\').style.display=\'none\'"'
)

content = content.replace(
    'onclick="document.getElementById(\'rollon-wax-modal\').style.display=\'none\'"',
    'onclick="addToCart(\'Roll-on Waxing\', 1949); document.getElementById(\'rollon-wax-modal\').style.display=\'none\'"'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated salon-luxe.html")
