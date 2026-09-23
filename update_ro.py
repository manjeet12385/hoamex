import sys
with open('microwave.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Header replacements
html = html.replace('<title>Microwave repair - Urban Company</title>', '<title>Water Purifier - Urban Company</title>')
html = html.replace('Home / Delhi / Microwave repair', 'Home / Delhi / Water Purifier')
html = html.replace('Microwave repair</h1>', 'Water Purifier</h1>')
html = html.replace('4.84 (821K bookings)', '4.79 (2.4 M bookings)')

# Keep the hero image area but maybe change the image src if we have a specific one, or just use images/plumber.jpg
html = html.replace('<img src="images/tools.jpg" alt="Microwave repair banner"', '<img src="images/plumber.jpg" alt="Water purifier banner"')

# Change Microwave check-up section to Water Purifier Service & Installation
start_str = '<!-- Center Content -->'
end_str = '<!-- Right Sidebar -->'
idx_start = html.find(start_str)
idx_end = html.find(end_str)

if idx_start != -1 and idx_end != -1:
    new_content = '''<!-- Center Content -->
            <div class="ac-main-content">
                <div class="plan-details-card" style="padding-top: 20px;">
                    <h4 style="font-size: 20px; font-weight: 700; margin-bottom: 5px;">Water Purifier Service & Installation</h4>
                    <div class="plan-rating" style="margin-bottom: 15px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.79 <span style="color: #666; font-weight: 400;">(200K reviews)</span></div>
                    
                    <div style="background: #f8f9fa; border-radius: 8px; padding: 12px 15px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; cursor: pointer; border: 1px solid #eee;">
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #00875a; font-weight: 700; font-size: 14px;"><i class="fa-solid fa-shield-halved"></i> UC cover</span>
                            <span style="font-size: 13px; color: #444;">Standard rate card</span>
                        </div>
                        <i class="fa-solid fa-chevron-right" style="color: #666; font-size: 12px;"></i>
                    </div>

                    <div style="position: relative; margin: 0 -5px;">
                        <button id="scroll-left-checkup-btn" style="position: absolute; left: -15px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-left" style="font-size: 14px;"></i></button>
                        <button id="scroll-right-checkup-btn" style="position: absolute; right: -15px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-right" style="font-size: 14px;"></i></button>
                        
                        <div id="modal-carousel-checkup" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; padding-left: 5px; padding-right: 5px; scrollbar-width: none; scroll-behavior: smooth;">
                        
                            <div class="option-card" style="min-width: 140px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; display: flex; flex-direction: column; position: relative;">
                                <h4 style="font-size: 14px; margin-bottom: 5px; height: 35px;">Wall-mounted RO installation</h4>
                                <div class="option-rating" style="font-size: 11px; margin-bottom: 5px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.78 <span style="color: #666;">(2K reviews)</span></div>
                                <div class="option-price" style="font-size: 13px; font-weight: 600; margin-bottom: 10px;">₹499</div>
                                <button class="option-add-btn" style="width: 100%; padding: 6px; background: #fff; border: 1px solid #e0e0e0; color: #7d33ff; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 13px;">Add</button>
                            </div>

                            <div class="option-card" style="min-width: 140px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; display: flex; flex-direction: column; position: relative;">
                                <h4 style="font-size: 14px; margin-bottom: 5px; height: 35px;">Under the counter RO installation</h4>
                                <div class="option-rating" style="font-size: 11px; margin-bottom: 5px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.78 <span style="color: #666;">(1K reviews)</span></div>
                                <div class="option-price" style="font-size: 13px; font-weight: 600; margin-bottom: 10px;">₹549</div>
                                <button class="option-add-btn" style="width: 100%; padding: 6px; background: #fff; border: 1px solid #e0e0e0; color: #7d33ff; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 13px;">Add</button>
                            </div>

                            <div class="option-card" style="min-width: 140px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; display: flex; flex-direction: column; position: relative;">
                                <h4 style="font-size: 14px; margin-bottom: 5px; height: 35px;">RO Uninstallation</h4>
                                <div class="option-rating" style="font-size: 11px; margin-bottom: 5px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.86 <span style="color: #666;">(15K reviews)</span></div>
                                <div class="option-price" style="font-size: 13px; font-weight: 600; margin-bottom: 10px;">₹449</div>
                                <button class="option-add-btn" style="width: 100%; padding: 6px; background: #fff; border: 1px solid #e0e0e0; color: #7d33ff; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 13px;">Add</button>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            '''
    html = html[:idx_start] + new_content + html[idx_end:]

with open('water-purifier.html', 'w', encoding='utf-8') as f:
    f.write(html)
