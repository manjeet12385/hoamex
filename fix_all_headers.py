import re
import glob

html_files = glob.glob(r'c:\Users\Divyanshi123456\Music\hoamex\*.html')
fixed_count = 0
already_count = 0

FIXED_STYLE = 'position: fixed; top: 0; left: 0; width: 100%; z-index: 9999; background: #fff; box-shadow: 0 2px 8px rgba(0,0,0,0.08);'

for file in html_files:
    # Skip header.html itself
    if file.endswith('header.html') or file.endswith('footer.html'):
        continue
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()

        # Check if header already has position: fixed
        if 'position: fixed' in html and '<header' in html:
            # Check if it's in the header tag
            header_match = re.search(r'<header[^>]*>', html)
            if header_match and 'position: fixed' in header_match.group(0):
                already_count += 1
                continue

        # Find <header ...> tag and inject position: fixed into its style attribute
        def fix_header_tag(match):
            tag = match.group(0)
            if 'style="' in tag:
                # Add to existing style
                if 'position: fixed' in tag:
                    return tag  # already fixed
                tag = tag.replace('style="', f'style="{FIXED_STYLE} ', 1)
            else:
                # Add new style attribute
                tag = tag.replace('<header', f'<header style="{FIXED_STYLE}"', 1)
            return tag

        new_html = re.sub(r'<header[^>]*>', fix_header_tag, html, count=1)

        if html != new_html:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_html)
            fixed_count += 1

    except Exception as e:
        print(f"Error on {file}: {e}")

print(f"Fixed {fixed_count} pages with position:fixed header")
print(f"Already fixed: {already_count} pages")
