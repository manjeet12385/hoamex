import os

file_path = "c:/Users/Divyanshi123456/Music/hoamex/plumber.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace literal backslash followed by single quote with just single quote
content = content.replace("\\'", "'")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Fixed backslashes in plumber.html")
