import glob

count = 0
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We are looking for: style="width: 100%; display: block; object-fit: cover;" without a height
    search_str = 'style="width: 100%; display: block; object-fit: cover;"'
    replace_str = 'style="width: 100%; height: 250px; display: block; object-fit: cover; object-position: center;"'
    
    if search_str in content:
        content = content.replace(search_str, replace_str)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed banner height in {f}")
        count += 1

print(f"Total files updated: {count}")
