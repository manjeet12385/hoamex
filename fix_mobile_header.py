import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the problematic rules in the old media query
content = content.replace('.search-container {\n        display: none !important; /* Hide search bar on mobile */\n    }', '')
content = content.replace('.location-btn span, .partner-btn {\n        display: none !important; /* Hide text, keep icons if possible, or hide partner btn */\n    }', '')
content = content.replace('body {\n        padding-top: 130px; /* Adjust for taller header */\n    }', 'body {\n        padding-top: 170px !important; /* Adjust for taller header */\n    }')

# Ensure search-container is explicitly displayed in my new media query block
content = content.replace('.search-container {\n        width: 100%;\n        order: 3; /* Move below logo and buttons */\n    }', '.search-container {\n        display: flex !important;\n        width: 100%;\n        order: 3;\n        margin-top: 10px;\n    }')

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
    f.write(content)
