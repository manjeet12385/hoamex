import re

modal_html = """
    <!-- Railing Rope Modal -->
    <div id="railing-rope-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf6; width: 100%; max-width: 500px; padding: 20px; border-radius: 12px; position: relative; max-height: 90vh; overflow-y: auto;">
            <button id="close-railing-rope-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>
            <div style="height: 180px; width: calc(100% + 40px); margin: -20px -20px 20px -20px; overflow: hidden; border-radius: 12px 12px 0 0;">
                <img src="images/renovation.jpg" onerror="this.src='images/plumber.jpg'" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <h3 class="options-modal-title" style="font-size: 24px; margin-bottom: 5px; font-weight: 700; color: #111;">Railing lights installation (Rope)</h3>
            <p style="font-size: 14px; color: #555; margin-bottom: 25px;"><i class="fa-solid fa-star" style="color: #555;"></i> 4.55 (800 reviews)</p>
            <div style="position: relative; margin: 0 -5px;">
                <button id="scroll-left-railing-rope-btn" style="position: absolute; left: -10px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-left" style="font-size: 14px;"></i></button>
                <button id="scroll-right-railing-rope-btn" style="position: absolute; right: -10px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-right" style="font-size: 14px;"></i></button>
                <div id="modal-carousel-railing-rope" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; padding-left: 5px; padding-right: 5px; scrollbar-width: none; scroll-behavior: smooth;">
                    <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                        <h4 style="font-size: 16px; margin-bottom: 5px; color: #111;">2 Rope lights</h4>
                        <div class="option-rating" style="font-size: 12px; margin-bottom: 8px;"><i class="fa-solid fa-star" style="color: #555;"></i> 4.59 <span style="color: #777;">(609 reviews)</span></div>
                        <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 15px;">₹248</div>
                        <button class="option-add-btn" onclick="addToCart('Railing lights installation (Rope) - 2 lights',248)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                    </div>
                    <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                        <h4 style="font-size: 16px; margin-bottom: 5px; color: #111;">4 Rope lights</h4>
                        <div class="option-rating" style="font-size: 12px; margin-bottom: 8px;"><i class="fa-solid fa-star" style="color: #555;"></i> 4.43 <span style="color: #777;">(191 reviews)</span></div>
                        <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 15px;">₹495</div>
                        <button class="option-add-btn" onclick="addToCart('Railing lights installation (Rope) - 4 lights',495)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

with open('festival-lights.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace button
target_button = """<button class="add-btn" onclick="addToCart('Railing lights installation (Rope)',248)">Add</button>"""
new_button = """<button id="open-railing-rope-modal-btn" class="add-btn">Add</button>"""
content = content.replace(target_button, new_button)

# Append modal
if '<style>' in content:
    content = content.replace('<style>', modal_html + '\n    <style>')
else:
    if '</body>' in content:
        content = content.replace('</body>', modal_html + '\n</body>')
    else:
        content += modal_html

# Append script line
script_line = "\n            setupModal('open-railing-rope-modal-btn', 'railing-rope-modal', 'close-railing-rope-modal-btn', 'modal-carousel-railing-rope', 'scroll-left-railing-rope-btn', 'scroll-right-railing-rope-btn');"
content = content.replace("        });\n    </script>", script_line + "\n        });\n    </script>")

with open('festival-lights.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated festival-lights.html")
