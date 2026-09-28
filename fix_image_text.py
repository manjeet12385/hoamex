import re
import glob

html_files = glob.glob(r'c:\Users\Divyanshi123456\Music\hoamex\*.html')

count = 0
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Replace color: #333 with color: #fff and add text-shadow
        # Pattern looks for position: absolute and color: #333 in the same style attribute
        pattern = r'(style="[^"]*?position:\s*absolute;[^"]*?)(color:\s*#333;?)([^"]*?")'
        
        # Replacement function
        def repl(match):
            return match.group(1) + "color: #fff; text-shadow: 0px 2px 5px rgba(0,0,0,0.9);" + match.group(3)
            
        new_html = re.sub(pattern, repl, html)
        
        if html != new_html:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_html)
            count += 1
    except Exception as e:
        print(f"Error on {file}: {e}")

print(f"Updated {count} files with readable text-shadows over images.")
