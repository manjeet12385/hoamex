import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Add to the max-width: 768px section
mobile_additions = """
    .home-services {
        display: none !important;
    }
    .services-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 15px !important;
    }
    .service-icon img {
        width: 60px !important; /* Make icons slightly smaller for 2-column grid to fit well */
        height: 60px !important;
    }
"""

# Append just inside the existing `@media screen and (max-width: 768px) {` block
# Let's just append it to the end of the file in a new block to be safe.
new_block = f"""
@media screen and (max-width: 768px) {{
{mobile_additions}
}}
"""

content += new_block

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
    f.write(content)
