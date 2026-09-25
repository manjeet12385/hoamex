import os
import re

html_file = r'c:\Users\Divyanshi123456\Music\hoamex\electrician.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Define start and end markers
start_marker = "<!-- Switchboard repair Modal -->"
end_marker = "<!-- Cart Sidebar -->"

# Extract everything before and after
start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

new_modal = """<!-- Switchboard repair Modal -->
    <div id="switchboard-repair-modal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 1000; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf9; width: 100%; max-width: 600px; padding: 0; overflow: hidden; border-radius: 12px; position: relative;">
            <button id="close-switchboard-repair-modal-btn" class="modal-close" style="position: absolute; z-index: 10; background: white; border: none; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; top: 15px; right: 15px; cursor: pointer;"><i class="fa-solid fa-xmark"></i></button>
            
            <div class="options-modal-body" style="padding: 24px;">
                <h3 class="options-modal-title" style="font-size: 24px; margin-bottom: 5px; font-weight: 700;">Full switchboard repair/replace</h3>
                <div class="options-rating" style="margin-bottom: 5px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.83 <span style="color: #666; font-weight: 400; text-decoration: underline; text-decoration-style: dotted;">(55K reviews)</span></div>
                <div style="color: #00875a; font-weight: 600; font-size: 13px; margin-bottom: 20px;"><i class="fa-solid fa-tag"></i> 10% off above ₹300</div>

                <div style="position: relative;">
                    <button id="scroll-left-switchboard-btn" style="position: absolute; left: -15px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-left" style="font-size: 14px;"></i></button>
                    <button id="scroll-right-switchboard-btn" style="position: absolute; right: -15px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-right" style="font-size: 14px;"></i></button>
                    
                    <div id="modal-carousel-switchboard-repair" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; scrollbar-width: none; scroll-behavior: smooth;">
                    
                        <div class="option-card" style="min-width: 150px; flex: 1; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 16px; display: flex; flex-direction: column; background: #fff;">
                            <div style="width: 100%; height: 100px; margin-bottom: 15px; background: #f8f8f8; border-radius: 6px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                                <img src="images/switch_small.png" onerror="this.src='images/switch-repair.png'" style="width: 80%; height: 80%; object-fit: contain;">
                            </div>
                            <h4 style="font-size: 15px; margin-bottom: 5px; font-weight: 600;">Small (upto 2 modules)</h4>
                            <div class="option-rating" style="font-size: 12px; margin-bottom: 10px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.82 <span style="color: #666;">(17K reviews)</span></div>
                            <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 15px;">₹149</div>
                            <button class="option-add-btn" onclick="addToCart('Small Switchboard (upto 2 modules)', 149); document.getElementById('switchboard-repair-modal').style.display='none';" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #a855f7; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 14px;">Add</button>
                        </div>

                        <div class="option-card" style="min-width: 150px; flex: 1; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 16px; display: flex; flex-direction: column; background: #fff;">
                            <div style="width: 100%; height: 100px; margin-bottom: 15px; background: #f8f8f8; border-radius: 6px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                                <img src="images/switch_medium.png" onerror="this.src='images/switch-repair.png'" style="width: 80%; height: 80%; object-fit: contain;">
                            </div>
                            <h4 style="font-size: 15px; margin-bottom: 5px; font-weight: 600;">Medium (4-6 modules)</h4>
                            <div class="option-rating" style="font-size: 12px; margin-bottom: 10px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.82 <span style="color: #666;">(30K reviews)</span></div>
                            <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 15px;">₹179</div>
                            <button class="option-add-btn" onclick="addToCart('Medium Switchboard (4-6 modules)', 179); document.getElementById('switchboard-repair-modal').style.display='none';" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #a855f7; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 14px;">Add</button>
                        </div>
                        
                        <div class="option-card" style="min-width: 150px; flex: 1; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 16px; display: flex; flex-direction: column; background: #fff;">
                            <div style="width: 100%; height: 100px; margin-bottom: 15px; background: #f8f8f8; border-radius: 6px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                                <img src="images/switch_large.png" onerror="this.src='images/switch-repair.png'" style="width: 80%; height: 80%; object-fit: contain;">
                            </div>
                            <h4 style="font-size: 15px; margin-bottom: 5px; font-weight: 600;">Large (8-12 modules)</h4>
                            <div class="option-rating" style="font-size: 12px; margin-bottom: 10px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.81 <span style="color: #666;">(602 reviews)</span></div>
                            <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 15px;">₹219</div>
                            <button class="option-add-btn" onclick="addToCart('Large Switchboard (8-12 modules)', 219); document.getElementById('switchboard-repair-modal').style.display='none';" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #a855f7; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 14px;">Add</button>
                        </div>
                        
                        <div class="option-card" style="min-width: 150px; flex: 1; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 16px; display: flex; flex-direction: column; background: #fff;">
                            <div style="width: 100%; height: 100px; margin-bottom: 15px; background: #f8f8f8; border-radius: 6px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                                <img src="images/switch_xlarge.png" onerror="this.src='images/switch-repair.png'" style="width: 80%; height: 80%; object-fit: contain;">
                            </div>
                            <h4 style="font-size: 15px; margin-bottom: 5px; font-weight: 600;">Extra Large (12+ modules)</h4>
                            <div class="option-rating" style="font-size: 12px; margin-bottom: 10px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.87 <span style="color: #666;">(123 reviews)</span></div>
                            <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 15px;">₹249</div>
                            <button class="option-add-btn" onclick="addToCart('Extra Large Switchboard (12+ modules)', 249); document.getElementById('switchboard-repair-modal').style.display='none';" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #a855f7; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 14px;">Add</button>
                        </div>

                        <div class="option-card" style="min-width: 150px; flex: 1; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 16px; display: flex; flex-direction: column; background: #fff;">
                            <div style="width: 100%; height: 100px; margin-bottom: 15px; background: #f8f8f8; border-radius: 6px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                                <img src="images/switch_power_ac.png" onerror="this.src='images/switch-repair.png'" style="width: 80%; height: 80%; object-fit: contain;">
                            </div>
                            <h4 style="font-size: 15px; margin-bottom: 5px; font-weight: 600;">Power / AC Switchboard</h4>
                            <div class="option-rating" style="font-size: 12px; margin-bottom: 10px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.86 <span style="color: #666;">(8K reviews)</span></div>
                            <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 15px;">₹249</div>
                            <button class="option-add-btn" onclick="addToCart('Power / AC Switchboard', 249); document.getElementById('switchboard-repair-modal').style.display='none';" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #a855f7; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 14px;">Add</button>
                        </div>
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('close-switchboard-repair-modal-btn').addEventListener('click', function() {
            document.getElementById('switchboard-repair-modal').style.display = 'none';
        });
        document.getElementById('switchboard-repair-modal').addEventListener('click', function(e) {
            if (e.target === this) {
                this.style.display = 'none';
            }
        });
        document.getElementById('scroll-left-switchboard-btn').addEventListener('click', function() {
            document.getElementById('modal-carousel-switchboard-repair').scrollBy({ left: -200, behavior: 'smooth' });
        });
        document.getElementById('scroll-right-switchboard-btn').addEventListener('click', function() {
            document.getElementById('modal-carousel-switchboard-repair').scrollBy({ left: 200, behavior: 'smooth' });
        });
    </script>
    
    """

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_modal + content[end_idx:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Done")
else:
    print(f"Markers not found: start_idx={start_idx}, end_idx={end_idx}")
