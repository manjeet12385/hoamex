import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the problematic body padding on mobile that pushes everything down
content = re.sub(r'body\s*\{\s*padding-top:\s*120px\s*!important;\s*/\*\s*Adjust for taller header\s*\*/\s*\}', '', content)
# Also try matching without the comment just in case
content = re.sub(r'body\s*\{\s*padding-top:\s*120px\s*!important;\s*\}', '', content)

# 2. Add position: sticky to .header on mobile so it naturally stays at top without needing body padding
# I'll append this to the end of the file in a media query
mobile_header_fix = """
@media screen and (max-width: 768px) {
    .header {
        position: sticky !important;
        top: 0 !important;
        z-index: 10000 !important;
        background-color: #ffffff !important;
    }
    body {
        padding-top: 0 !important;
    }
}
"""

content += mobile_header_fix

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
    f.write(content)
