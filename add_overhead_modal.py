import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace button trigger
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Overhead tank cleaning (open placed)',899)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('overhead-cleaning-modal').style.display='flex'">Add</button>'''
)

# Insert modal
new_modal = """
<!-- Overhead Cleaning Modal -->
    <div id="overhead-cleaning-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf6; width: 100%; max-width: 500px; padding: 20px; border-radius: 12px; position: relative; max-height: 90vh; overflow-y: auto;">
            <button id="close-overhead-cleaning-modal-btn" onclick="document.getElementById('overhead-cleaning-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="options-modal-title" style="font-size: 24px; margin-bottom: 5px; font-weight: 700; color: #111;">Overhead tank cleaning (open placed)</h3>
            <div style="position: relative; margin: 0 -5px;">
                <div id="modal-carousel-overhead-cleaning" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; padding-left: 5px; padding-right: 5px; scrollbar-width: none; scroll-behavior: smooth;">
                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="images/new_plumber_icon.jpg" onerror="this.src='images/new_plumber_icon.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">Up to 1000L</h4>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹899</div>
                    <button class="option-add-btn" onclick="addToCart('Overhead Tank cleaning up to 1000L',899)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>
                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="images/new_plumber_icon.jpg" onerror="this.src='images/new_plumber_icon.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">1000L to 3000L</h4>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹1499</div>
                    <button class="option-add-btn" onclick="addToCart('Overhead Tank cleaning 1000-3000L',1499)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>
                </div>
            </div>
        </div>
</div>
"""
content = content.replace("</div>\n    <style>", new_modal + "\n</div>\n    <style>")

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'w', encoding='utf-8') as f:
    f.write(content)
