import glob

files = glob.glob('*.html')
total = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to add premium-navbar to the class list of the header.
    if '<header' in content:
        # Find the header tag
        if 'class="header"' in content:
            new_content = content.replace('class="header"', 'class="header premium-navbar"')
            if new_content != content:
                with open(f, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                total += 1
        elif "class='header'" in content:
            new_content = content.replace("class='header'", "class='header premium-navbar'")
            if new_content != content:
                with open(f, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                total += 1

print(f"Updated {total} files to use premium-navbar!")
