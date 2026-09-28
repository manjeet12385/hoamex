with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the old sticky rule that was added and conflicts
bad_rule = """.header {
        position: sticky !important;
        top: 0 !important;
        z-index: 10000 !important;
        background-color: #ffffff !important;
    }"""

css = css.replace(bad_rule, "")

# Remove the old "Persistent Fixed Header" block that uses sticky
old_block = """/* Persistent Fixed Header */
.header {
    position: sticky;
    top: 0;
    z-index: 9999;
    background: #fff;
    width: 100%;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}
/* Ensure body content starts below header */
body {
    padding-top: 70px; /* adjust based on header height */
}"""

css = css.replace(old_block, "")

# Now ensure the FIRST .header block has position: fixed
import re
first_header_match = re.search(r'(\.header \{[^}]*?)position:\s*\w+;', css, re.DOTALL)
if first_header_match:
    css = css[:first_header_match.start(1)] + first_header_match.group(1).replace(
        '', '') + css[first_header_match.end():]

# Replace the base .header block entirely to be safe
css = re.sub(
    r'\.header \{\s*display: flex;\s*align-items: center;\s*justify-content: space-between;\s*padding: 15px 40px;\s*background-color: #ffffff;\s*border-bottom: 1px solid rgba\(0,0,0,0.05\);\s*position: fixed;\s*width: 100%;\s*top: 0;\s*left: 0;\s*z-index: 10000;\s*\}',
    """.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 15px 40px;
    background-color: #ffffff;
    border-bottom: 1px solid rgba(0,0,0,0.05);
    position: fixed !important;
    width: 100% !important;
    top: 0 !important;
    left: 0 !important;
    z-index: 10000 !important;
}""",
    css
)

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done! Removed conflicting sticky rules, kept position:fixed !important")
