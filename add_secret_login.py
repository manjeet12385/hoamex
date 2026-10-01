import os
import glob

# 1. Modify HTML files
html_files = glob.glob("*.html")
replaced_count = 0
for file in html_files:
    if file == "admin.html":
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "&copy; 2026 Joamex" in content and '<span id="secret-admin"' not in content:
        content = content.replace(
            "&copy; 2026 Joamex", 
            "&copy; 2026 <span id=\"secret-admin\" style=\"user-select:none;\">Joamex</span>"
        )
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        replaced_count += 1

print(f"Added secret span to {replaced_count} HTML files.")

# 2. Append Javascript to common.js
js_code = """

// --- Secret Admin Trick ---
document.addEventListener('DOMContentLoaded', () => {
    const secretTrigger = document.getElementById('secret-admin');
    if(secretTrigger) {
        let clickCount = 0;
        let clickTimer;
        
        secretTrigger.addEventListener('click', (e) => {
            clickCount++;
            
            if(clickCount === 1) {
                clickTimer = setTimeout(() => {
                    clickCount = 0; // reset if not clicked 5 times within 2 seconds
                }, 2000);
            }
            
            if(clickCount === 5) {
                clearTimeout(clickTimer);
                clickCount = 0;
                // Add a cool little transition effect before redirecting
                document.body.style.transition = "opacity 0.5s ease";
                document.body.style.opacity = "0";
                setTimeout(() => {
                    window.location.href = "admin.html";
                }, 500);
            }
        });
    }
});
"""

if os.path.exists("common.js"):
    with open("common.js", "r", encoding='utf-8') as f:
        common_content = f.read()
    
    if "Secret Admin Trick" not in common_content:
        with open("common.js", "a", encoding='utf-8') as f:
            f.write(js_code)
        print("Added secret trick to common.js")
    else:
        print("Secret trick already in common.js")

