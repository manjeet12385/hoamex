import os
import glob

html_files = glob.glob('*.html')

sticky_icons = """
    <!-- Sticky Contact Icons -->
    <div class="sticky-contact-icons" style="position: fixed; left: 15px; top: 50%; transform: translateY(-50%); z-index: 9999; display: flex; flex-direction: column; gap: 15px;">
        <a href="https://wa.me/919014380344" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 50px; height: 50px; border-radius: 50%; background-color: #25d366; color: white; text-decoration: none; font-size: 28px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
            <i class="fa-brands fa-whatsapp"></i>
        </a>
        <a href="tel:+919014380344" style="display: flex; align-items: center; justify-content: center; width: 50px; height: 50px; border-radius: 50%; background-color: #5c6bc0; color: white; text-decoration: none; font-size: 24px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
            <i class="fa-solid fa-phone"></i>
        </a>
    </div>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<!-- Sticky Contact Icons -->' not in content:
        content = content.replace('</body>', sticky_icons + '\n</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added to {filepath}")
    else:
        print(f"Already exists in {filepath}")
