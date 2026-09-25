import os
import re

html_file = r'c:\Users\Divyanshi123456\Music\hoamex\electrician.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the onclick of Plug replacement Add button
content = re.sub(
    r'<button class="add-btn" onclick="addToCart\(\'Plug replacement\', 69\)"',
    r'<button class="add-btn" onclick="document.getElementById(\'plug-replacement-modal\').style.display=\'flex\'"',
    content
)

# Modal HTML to inject
modal_html = """
    <!-- Plug replacement Modal -->
    <div id="plug-replacement-modal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 1000; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf9; width: 100%; max-width: 450px; padding: 0; overflow: hidden; border-radius: 12px; position: relative;">
            <button id="close-plug-replacement-modal-btn" class="modal-close" style="position: absolute; z-index: 10; background: white; border: none; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; top: 15px; right: 15px; cursor: pointer;"><i class="fa-solid fa-xmark"></i></button>
            
            <div class="options-modal-body" style="padding: 24px;">
                <h3 class="options-modal-title" style="font-size: 24px; margin-bottom: 5px; font-weight: 700;">Plug replacement</h3>
                <div class="options-rating" style="margin-bottom: 20px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.82 <span style="color: #666; font-weight: 400; text-decoration: underline; text-decoration-style: dotted;">(15K reviews)</span></div>

                <div style="position: relative;">
                    <div id="modal-carousel-plug-replacement" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; scrollbar-width: none; scroll-behavior: smooth;">
                    
                        <div class="option-card" style="min-width: 150px; flex: 1; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 16px; display: flex; flex-direction: column; background: #fff;">
                            <div style="width: 100%; height: 100px; margin-bottom: 15px; background: #f8f8f8; border-radius: 6px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                                <img src="images/plug_regular.png" onerror="this.src='images/plug.png'" style="width: 80%; height: 80%; object-fit: contain;">
                            </div>
                            <h4 style="font-size: 15px; margin-bottom: 5px; font-weight: 600;">Regular Plug Replacement</h4>
                            <div class="option-rating" style="font-size: 12px; margin-bottom: 10px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.81 <span style="color: #666;">(3K reviews)</span></div>
                            <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 15px;">₹89</div>
                            <button class="option-add-btn" onclick="addToCart('Regular Plug Replacement', 89); document.getElementById('plug-replacement-modal').style.display='none';" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #a855f7; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 14px;">Add</button>
                        </div>

                        <div class="option-card" style="min-width: 150px; flex: 1; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 16px; display: flex; flex-direction: column; background: #fff;">
                            <div style="width: 100%; height: 100px; margin-bottom: 15px; background: #f8f8f8; border-radius: 6px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                                <img src="images/plug_power.png" onerror="this.src='images/plug.png'" style="width: 80%; height: 80%; object-fit: contain;">
                            </div>
                            <h4 style="font-size: 15px; margin-bottom: 5px; font-weight: 600;">Power Plug Replacement</h4>
                            <div class="option-rating" style="font-size: 12px; margin-bottom: 10px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.83 <span style="color: #666;">(12K reviews)</span></div>
                            <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 15px;">₹109</div>
                            <button class="option-add-btn" onclick="addToCart('Power Plug Replacement', 109); document.getElementById('plug-replacement-modal').style.display='none';" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #a855f7; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 14px;">Add</button>
                        </div>
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('close-plug-replacement-modal-btn').addEventListener('click', function() {
            document.getElementById('plug-replacement-modal').style.display = 'none';
        });
        document.getElementById('plug-replacement-modal').addEventListener('click', function(e) {
            if (e.target === this) {
                this.style.display = 'none';
            }
        });
    </script>
"""

# Insert modal before Cart Sidebar
content = content.replace('<!-- Cart Sidebar -->', modal_html + '\n    <!-- Cart Sidebar -->')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
