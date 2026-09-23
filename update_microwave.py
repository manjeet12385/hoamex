import sys
with open('chimney.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace title
html = html.replace('<title>Chimney repair - Urban Company</title>', '<title>Microwave repair - Urban Company</title>')
html = html.replace('Home / Delhi / Chimney repair', 'Home / Delhi / Microwave repair')
html = html.replace('Chimney repair</h1>', 'Microwave repair</h1>')
html = html.replace('4.69 (39K bookings)', '4.84 (821K bookings)')

# Keep the hero image as is (images/kitchen.jpg or tools.jpg), let's replace it with images/tools.jpg
html = html.replace('<img src="images/kitchen.jpg" alt="Chimney repair banner"', '<img src="images/tools.jpg" alt="Microwave repair banner"')

start_str = '<!-- Center Content -->'
end_str = '<!-- Right Sidebar -->'
idx_start = html.find(start_str)
idx_end = html.find(end_str)

if idx_start != -1 and idx_end != -1:
    new_content = '''<!-- Center Content -->
            <div class="ac-main-content">
                <div class="plan-details-card" style="padding-top: 20px;">
                    <h4 style="font-size: 20px; font-weight: 700; margin-bottom: 5px;">Microwave check-up</h4>
                    <div class="plan-rating" style="margin-bottom: 15px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.84 <span style="color: #666; font-weight: 400;">(61K reviews)</span></div>
                    
                    <div style="background: #f8f9fa; border-radius: 8px; padding: 12px 15px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; cursor: pointer; border: 1px solid #eee;">
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #00875a; font-weight: 700; font-size: 14px;"><i class="fa-solid fa-shield-halved"></i> UC cover</span>
                            <span style="font-size: 13px; color: #444;">Standard rate card</span>
                        </div>
                        <i class="fa-solid fa-chevron-right" style="color: #666; font-size: 12px;"></i>
                    </div>

                    <div style="position: relative; margin: 0 -5px;">
                        <div id="modal-carousel-checkup" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; padding-left: 5px; padding-right: 5px; scrollbar-width: none; scroll-behavior: smooth;">
                        
                            <div class="option-card" style="min-width: 140px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; display: flex; flex-direction: column; position: relative;">
                                <h4 style="font-size: 14px; margin-bottom: 5px; height: 20px;">Not heating</h4>
                                <div class="option-rating" style="font-size: 11px; margin-bottom: 5px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.85 <span style="color: #666;">(44K reviews)</span></div>
                                <div class="option-price" style="font-size: 13px; font-weight: 600; margin-bottom: 10px;">₹199</div>
                                <button class="option-add-btn" style="width: 100%; padding: 6px; background: #fff; border: 1px solid #e0e0e0; color: #7d33ff; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 13px;">Add</button>
                            </div>

                            <div class="option-card" style="min-width: 140px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; display: flex; flex-direction: column; position: relative;">
                                <h4 style="font-size: 14px; margin-bottom: 5px; height: 20px;">Not working</h4>
                                <div class="option-rating" style="font-size: 11px; margin-bottom: 5px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.81 <span style="color: #666;">(36K reviews)</span></div>
                                <div class="option-price" style="font-size: 13px; font-weight: 600; margin-bottom: 10px;">₹199</div>
                                <button class="option-add-btn" style="width: 100%; padding: 6px; background: #fff; border: 1px solid #e0e0e0; color: #7d33ff; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 13px;">Add</button>
                            </div>

                            <div class="option-card" style="min-width: 140px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; display: flex; flex-direction: column; position: relative;">
                                <h4 style="font-size: 14px; margin-bottom: 5px; height: 20px;">Unknown issue</h4>
                                <div class="option-rating" style="font-size: 11px; margin-bottom: 5px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.81 <span style="color: #666;">(24K reviews)</span></div>
                                <div class="option-price" style="font-size: 13px; font-weight: 600; margin-bottom: 10px;">₹199</div>
                                <div style="position: absolute; right: 15px; bottom: 12px;">
                                    <button style="width: 28px; height: 28px; border-radius: 50%; background: #f8f8f8; border: 1px solid #eee; display: flex; align-items: center; justify-content: center; cursor: pointer;"><i class="fa-solid fa-arrow-right" style="font-size: 12px; color: #333;"></i></button>
                                </div>
                                <button class="option-add-btn" style="width: 100%; padding: 6px; background: #fff; border: 1px solid #e0e0e0; color: #7d33ff; font-weight: 600; border-radius: 8px; cursor: pointer; font-size: 13px;">Add</button>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            '''
    html = html[:idx_start] + new_content + html[idx_end:]

# Remove modals and scripts from the end of chimney
modal_start = html.find('<!-- Deep Chimney Service Modal -->')
if modal_start != -1:
    body_end = html.find('</body>')
    html = html[:modal_start] + '</body>\n</html>\n'

with open('microwave.html', 'w', encoding='utf-8') as f:
    f.write(html)
