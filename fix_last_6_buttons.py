import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Kitchen tile grouting
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Kitchen tile grouting',999)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('kitchen-grout-modal').style.display='flex'">Add</button>'''
)
content = content.replace(
    '''<div id="kitchen-grout-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">''',
    '''<div id="kitchen-grout-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">'''
)
content = content.replace(
    '''<button id="close-kitchen-grout-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>''',
    '''<button id="close-kitchen-grout-modal-btn" onclick="document.getElementById('kitchen-grout-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>'''
)

# 2. Overhead water tank installation
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Overhead water tank installation',599)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('tank-install-modal').style.display='flex'">Add</button>'''
)
content = content.replace(
    '''<div id="tank-install-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">''',
    '''<div id="tank-install-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">'''
)
content = content.replace(
    '''<button id="close-tank-install-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>''',
    '''<button id="close-tank-install-modal-btn" onclick="document.getElementById('tank-install-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>'''
)

# 3. Water tank repair
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Water tank repair',99)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('tank-repair-modal').style.display='flex'">Add</button>'''
)
content = content.replace(
    '''<div id="tank-repair-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">''',
    '''<div id="tank-repair-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">'''
)
content = content.replace(
    '''<button id="close-tank-repair-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>''',
    '''<button id="close-tank-repair-modal-btn" onclick="document.getElementById('tank-repair-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>'''
)

# 4. Underground tank cleaning
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Underground tank cleaning',1299)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('ug-tank-modal').style.display='flex'">Add</button>'''
)
content = content.replace(
    '''<div id="ug-tank-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">''',
    '''<div id="ug-tank-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">'''
)
content = content.replace(
    '''<button id="close-ug-tank-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>''',
    '''<button id="close-ug-tank-modal-btn" onclick="document.getElementById('ug-tank-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>'''
)

# 5. Water tank cleaning (loft placed)
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Water tank cleaning (loft placed)',1199)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('loft-tank-modal').style.display='flex'">Add</button>'''
)

# 6. Water meter installation
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Water meter installation',319)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('water-meter-modal').style.display='flex'">Add</button>'''
)

new_modals = """
<!-- Loft Tank Modal -->
    <div id="loft-tank-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf6; width: 100%; max-width: 500px; padding: 20px; border-radius: 12px; position: relative; max-height: 90vh; overflow-y: auto;">
            <button id="close-loft-tank-modal-btn" onclick="document.getElementById('loft-tank-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="options-modal-title" style="font-size: 24px; margin-bottom: 5px; font-weight: 700; color: #111;">Water tank cleaning (loft placed)</h3>
            <div style="position: relative; margin: 0 -5px;">
                <div id="modal-carousel-loft-tank" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; padding-left: 5px; padding-right: 5px; scrollbar-width: none; scroll-behavior: smooth;">
                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="images/new_plumber_icon.jpg" onerror="this.src='images/new_plumber_icon.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">Up to 500L</h4>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹499</div>
                    <button class="option-add-btn" onclick="addToCart('Loft Tank cleaning up to 500L',499)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>
                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="images/new_plumber_icon.jpg" onerror="this.src='images/new_plumber_icon.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">500L to 1000L</h4>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹799</div>
                    <button class="option-add-btn" onclick="addToCart('Loft Tank cleaning 500-1000L',799)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>
                </div>
            </div>
        </div>
</div>
<!-- Water Meter Modal -->
    <div id="water-meter-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf6; width: 100%; max-width: 500px; padding: 20px; border-radius: 12px; position: relative; max-height: 90vh; overflow-y: auto;">
            <button id="close-water-meter-modal-btn" onclick="document.getElementById('water-meter-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="options-modal-title" style="font-size: 24px; margin-bottom: 5px; font-weight: 700; color: #111;">Water meter installation</h3>
            <div style="position: relative; margin: 0 -5px;">
                <button id="scroll-left-meter-btn" style="position: absolute; left: -10px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-left" style="font-size: 14px;"></i></button>
                <button id="scroll-right-meter-btn" style="position: absolute; right: -10px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-right" style="font-size: 14px;"></i></button>
                <div id="modal-carousel-meter" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; padding-left: 5px; padding-right: 5px; scrollbar-width: none; scroll-behavior: smooth;">
                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="images/new_plumber_icon.jpg" onerror="this.src='images/new_plumber_icon.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">Sub-meter</h4>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹319</div>
                    <button class="option-add-btn" onclick="addToCart('Sub-meter installation',319)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>
                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="images/new_plumber_icon.jpg" onerror="this.src='images/new_plumber_icon.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">Main meter</h4>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹499</div>
                    <button class="option-add-btn" onclick="addToCart('Main meter installation',499)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>
                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="images/new_plumber_icon.jpg" onerror="this.src='images/new_plumber_icon.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">Smart meter</h4>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹799</div>
                    <button class="option-add-btn" onclick="addToCart('Smart meter installation',799)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>
                </div>
            </div>
        </div>
</div>
"""

content = content.replace("</div>\n    <style>", new_modals + "\n</div>\n    <style>")

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'w', encoding='utf-8') as f:
    f.write(content)
