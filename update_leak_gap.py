import re

with open('leak-gap.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Page Title
content = content.replace('<title>Ants & Bed Bugs Control - Joamex</title>', '<title>Leak & Gap Sealing - Joamex</title>')

# 2. Left Header
new_kitchen_header = """
            <div class="kitchen-header">
                <div>
                    <h1 class="kitchen-title">Leak &<br>gap ...</h1>
                </div>
                <div class="instant-badge">
                    <div class="instant-top"><i class="fa-solid fa-clock"></i> Earliest</div>
                    <div class="instant-bottom">Thu, 6:30 PM</div>
                </div>
            </div>

            <div style="border: 1px solid #e2e8f0; border-radius: 12px; padding: 15px; background: #fff; margin-top: 20px;">
                <div style="font-size: 11px; color: #475569; font-weight: 600; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
                    Select a service <hr style="flex: 1; border: none; border-top: 1px solid #e2e8f0; margin: 0;">
                </div>
                <div style="display: flex; gap: 15px; justify-content: space-between;">
                    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px;">
                        <img src="images/cleaning.jpg" alt="Bedroom & Living Areas" style="width: 50px; height: 50px; border-radius: 8px; object-fit: cover;">
                        <span style="font-size: 10px; font-weight: 500; color: #0f172a; line-height: 1.2;">Bedroom & Living<br>Areas</span>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px;">
                        <img src="images/cleaning.jpg" alt="Kitchen" style="width: 50px; height: 50px; border-radius: 8px; object-fit: cover;">
                        <span style="font-size: 10px; font-weight: 500; color: #0f172a; line-height: 1.2;">Kitchen</span>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px;">
                        <img src="images/cleaning.jpg" alt="Bathroom" style="width: 50px; height: 50px; border-radius: 8px; object-fit: cover;">
                        <span style="font-size: 10px; font-weight: 500; color: #0f172a; line-height: 1.2;">Bathroom</span>
                    </div>
                </div>
            </div>
"""
# Replace from <div class="kitchen-header"> to <button class="view-services-btn"...</button>
pattern_left = re.compile(r'<div class="kitchen-header">.*?<button class="view-services-btn".*?</button>', re.DOTALL)
content = pattern_left.sub(new_kitchen_header, content)

# 3. Banner
new_banner_text = """
                <div class="banner-text-bottom" style="color: #0f172a; left: 40px; bottom: 40px; text-shadow: none;">
                    <h1 style="font-size: 42px; font-weight: 700; margin: 0 0 15px 0; line-height: 1.2; text-shadow: none;">Close gaps.<br>Cut the risk.</h1>
                    <p style="font-size: 22px; color: #475569; margin: 0; line-height: 1.4; font-weight: 500;">Protect your home from<br>pests, dampness & grime.</p>
                </div>
"""
pattern_banner = re.compile(r'<div class="banner-text-bottom">.*?</div>', re.DOTALL)
content = pattern_banner.sub(new_banner_text, content)

# Remove the services since we don't have screenshot for them yet (Optional, I'll just leave them or clear them)
# Let's keep them empty for now or just remove them to be clean
pattern_services = re.compile(r'<div id="services-section" class="section-box">.*?</div>\s*</div>\s*</main>', re.DOTALL)
content = pattern_services.sub('<div id="services-section" class="section-box">\n</div>\n</div>\n</main>', content)


with open('leak-gap.html', 'w', encoding='utf-8') as f:
    f.write(content)
