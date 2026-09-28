import re
import glob

html_files = glob.glob(r'c:\Users\Divyanshi123456\Music\hoamex\*.html')
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # update common.js to common.js?v=2002 to bust cache
        new_html = re.sub(r'common\.js(?:\?v=\d+)?', 'common.js?v=2002', html)
        
        if html != new_html:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_html)
    except Exception as e:
        pass
