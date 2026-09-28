with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the broken horizontal scroll services-grid for mobile (which was causing cutoff)
# Replace the bad grid-auto-columns sliding logic with a clean 3-column grid
old_bad = """        .services-grid {
        display: grid !important;
        grid-template-rows: repeat(2, 1fr) !important;
        grid-template-columns: none !important;
        grid-auto-columns: 35% !important; /* 35% means they see almost 3 items horizontally, allowing sliding */
        grid-auto-flow: column !important;
        overflow-x: auto !important;
        scrollbar-width: none !important; /* Firefox */
        gap: 15px !important;
        padding-bottom: 15px !important;
        scroll-snap-type: x mandatory;
    }"""

new_good = """        .services-grid {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 12px !important;
        overflow-x: visible !important;
    }"""

if old_bad in css:
    css = css.replace(old_bad, new_good)
    print("Replaced bad horizontal slide with clean 3-col grid")
else:
    print("Pattern not found, trying partial match...")
    import re
    # Find and replace the bad block
    pattern = r'\.services-grid\s*\{[^}]*grid-auto-columns[^}]*\}'
    if re.search(pattern, css, re.DOTALL):
        css = re.sub(pattern, """.services-grid {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 12px !important;
        overflow-x: visible !important;
    }""", css, flags=re.DOTALL)
        print("Replaced via regex")
    else:
        print("Still not found")

# Also fix service-item text wrapping for subcategory sidebar
# "Installation/uninstall ation" - fix word-break
old_item = """.service-item {
        scroll-snap-align: start;
        border: 1px solid #eee; /* optional: adding a small border to make cards distinct while sliding */
        border-radius: 12px;
        padding: 10px;
        background: #fff;
    }"""
new_item = """.service-item {
        border-radius: 12px;
        padding: 10px;
        background: #fff;
    }
    .service-item .service-name,
    .service-item-sidebar span,
    .service-item p {
        font-size: 10px !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.3 !important;
        text-align: center !important;
    }"""

if old_item in css:
    css = css.replace(old_item, new_item)
    print("Fixed service-item text wrapping")

# Also fix service-name on home page to be smaller and wrap properly on mobile
service_name_fix = """
@media (max-width: 480px) {
    .service-name {
        font-size: 11px !important;
        word-break: break-word !important;
        line-height: 1.3 !important;
    }
    .service-icon {
        width: 55px !important;
        height: 55px !important;
    }
}
"""

if "service-name\n        font-size: 11px" not in css:
    css += "\n" + service_name_fix

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done! Services grid and text fixed.")
