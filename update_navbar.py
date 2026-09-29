import glob
import re

html_files = glob.glob('*.html')

# CSS to append to style.css
premium_css = """
/* Premium Navbar Styles */
.premium-navbar {
    position: fixed !important;
    top: 15px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 95% !important;
    max-width: 1400px !important;
    z-index: 9999 !important;
    background: rgba(255, 255, 255, 0.85) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08), 0 1px 3px rgba(0,0,0,0.05) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.5) !important;
    padding: 10px 25px !important;
    transition: all 0.3s ease !important;
}

.premium-navbar:hover {
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.12), 0 2px 5px rgba(0,0,0,0.05) !important;
}

/* Make body pad top so content doesn't hide behind floating navbar */
body {
    padding-top: 100px !important;
}

/* Premium Search Bar */
.premium-navbar .search-container {
    background: rgba(245, 245, 245, 0.8) !important;
    border-radius: 30px !important;
    border: 1px solid transparent !important;
    transition: all 0.3s ease !important;
}
.premium-navbar .search-container:focus-within {
    background: #fff !important;
    border: 1px solid #ddd !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05) !important;
    transform: scale(1.02) !important;
}
.premium-navbar .search-container input {
    background: transparent !important;
}

/* Premium Partner Button */
.premium-navbar .partner-btn {
    background: linear-gradient(135deg, #43a047, #2e7d32) !important;
    border: none !important;
    border-radius: 30px !important;
    color: white !important;
    padding: 10px 20px !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 15px rgba(67, 160, 71, 0.3) !important;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
}
.premium-navbar .partner-btn:hover {
    transform: translateY(-2px) scale(1.05) !important;
    box-shadow: 0 8px 20px rgba(67, 160, 71, 0.4) !important;
}

/* Premium Location Button */
.premium-navbar .location-btn {
    background: rgba(237, 231, 246, 0.7) !important;
    color: #5e35b1 !important;
    border-radius: 30px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}
.premium-navbar .location-btn:hover {
    background: #ede7f6 !important;
    transform: translateY(-2px) !important;
}

/* Premium Icon Buttons */
.premium-navbar .icon-btn {
    border-radius: 50% !important;
    width: 45px !important;
    height: 45px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    background: transparent !important;
    border: 1px solid transparent !important;
}
.premium-navbar .icon-btn:hover {
    background: rgba(0, 0, 0, 0.04) !important;
    transform: scale(1.15) !important;
}

/* Cart Badge Enhancement */
.premium-navbar #cart-badge {
    box-shadow: 0 2px 5px rgba(229, 57, 53, 0.4) !important;
    animation: pulse-badge 2s infinite !important;
}
@keyframes pulse-badge {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}

@media (max-width: 768px) {
    .premium-navbar {
        top: 0 !important;
        width: 100% !important;
        border-radius: 0 !important;
        padding: 10px 15px !important;
    }
}
"""

with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()
    
if 'Premium Navbar Styles' not in css_content:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write('\n' + premium_css)
    print("Appended premium styles to style.css")

# Update HTML files
header_regex = re.compile(r'<header[^>]*class="header"[^>]*>', re.IGNORECASE)
header_regex2 = re.compile(r'<header class="header"[^>]*>', re.IGNORECASE)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the header opening tag
    new_header_tag = '<header class="header premium-navbar">'
    
    # Simple replacement: replace style="..." inside header
    # Let's just use regex to replace the entire <header ...> tag with <header class="header premium-navbar">
    
    # we need to be careful not to match closing tags.
    # The regex r'<header[^>]*class="header"[^>]*>' should work for <header style="..." class="header">
    if 'premium-navbar' not in content:
        content = header_regex.sub(new_header_tag, content, count=1)
        content = header_regex2.sub(new_header_tag, content, count=1)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Already updated {filepath}")

