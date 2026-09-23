import sys

with open('chimney.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Header and Sidebar Title
html = html.replace('<title>Television Repair - Joamex</title>', '<title>Chimney - Joamex</title>')
html = html.replace('>Television Repair<', '>Chimney<')
html = html.replace('>4.82 <span style="color: #666; font-weight: 400; font-size: 14px;">(241K bookings)</span><', '>4.81 <span style="color: #666; font-weight: 400; font-size: 14px;">(2.6 M bookings)</span><')

# Replace Sidebar menu items
old_sidebar = '''                    <div class="sidebar-item active">
                        <img src="images/tools.jpg" alt="Service">
                        <span>Service</span>
                    </div>
                    <div class="sidebar-item">
                        <img src="images/tools.jpg" alt="Repair">
                        <span>Repair</span>
                    </div>
                    <div class="sidebar-item">
                        <img src="images/tools.jpg" alt="Install/Uninstall">
                        <span>Install/Uninstall</span>
                    </div>'''

new_sidebar = '''                    <div class="sidebar-item active" style="margin-bottom: 25px;">
                        <img src="images/tools.jpg" alt="Combos">
                        <span>Combos</span>
                    </div>
                    <div class="sidebar-item" style="margin-bottom: 25px;">
                        <img src="images/tools.jpg" alt="Service">
                        <span>Service</span>
                    </div>
                    <div class="sidebar-item" style="margin-bottom: 25px;">
                        <img src="images/tools.jpg" alt="Repairs">
                        <span>Repairs</span>
                    </div>
                    <div class="sidebar-item">
                        <img src="images/tools.jpg" alt="Installation/uninstallation">
                        <span>Installation/<br>uninstallation</span>
                    </div>'''

html = html.replace(old_sidebar, new_sidebar)

# Replace Center Content
start_str = '<!-- Center Content -->'
end_str = '<!-- Right Sidebar -->'
idx_start = html.find(start_str)
idx_end = html.find(end_str)

if idx_start != -1 and idx_end != -1:
    new_services = '''<!-- Center Content -->
            <div class="ac-main-content">
                <h2 class="section-heading" style="font-size: 22px; font-weight: 700; margin-bottom: 20px;">Combos</h2>
                
                <div class="plan-details-card" style="padding-top: 20px;">
                    <div style="display: flex; justify-content: space-between;">
                        <div style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; font-weight: 700; margin-bottom: 5px;">Deep chimney & stove service</h4>
                            <div class="plan-rating" style="margin-bottom: 5px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.72 <span style="color: #666; font-weight: 400;">(938 reviews)</span></div>
                            <div class="plan-price" style="font-weight: 600; font-size: 13px; margin-bottom: 10px; color: #000;">Starts at ₹1,498</div>
                            <ul class="plan-features" style="margin-top: 15px; margin-bottom: 15px;">
                                <li>Dismantling for internal servicing of motor, blowers & filters</li>
                                <li>Interior & exterior surface degreasing</li>
                            </ul>
                            <a href="#" style="color: #7d33ff; font-weight: 600; font-size: 14px; text-decoration: none;">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center;">
                            <div style="position: relative; width: 100%; border-radius: 8px; overflow: hidden; margin-bottom: -15px; background: #f8f8f8;">
                                <img src="images/kitchen.jpg" alt="Deep chimney" style="width: 100%; height: 90px; object-fit: cover;">
                            </div>
                            <button id="open-chimney-deep-modal-btn" style="position: relative; z-index: 3; padding: 8px 30px; background: #fff; border: 1px solid #e0e0e0; color: #7d33ff; font-weight: 600; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); cursor: pointer;">Add</button>
                            <span style="font-size: 12px; color: #666; margin-top: 5px;">3 options</span>
                        </div>
                    </div>
                </div>

                <div class="plan-details-card" style="padding-top: 20px; border-top: 1px solid #eee; margin-top: 20px;">
                    <div style="display: flex; justify-content: space-between;">
                        <div style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; font-weight: 700; margin-bottom: 5px;">Regular chimney & stove cleaning</h4>
                            <div class="plan-rating" style="margin-bottom: 5px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.84 <span style="color: #666; font-weight: 400;">(4K reviews)</span></div>
                            <div class="plan-price" style="font-weight: 600; font-size: 13px; margin-bottom: 10px; color: #000;">Starts at ₹548 &middot; 1 hr 25 mins</div>
                            <ul class="plan-features" style="margin-top: 15px; margin-bottom: 15px;">
                                <li>Stovetops, burners, mesh & filter cleaning with steam</li>
                                <li>Excludes motor cleaning, repair & automatic chimney cleaning</li>
                            </ul>
                            <a href="#" style="color: #7d33ff; font-weight: 600; font-size: 14px; text-decoration: none;">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center;">
                            <div style="position: relative; width: 100%; border-radius: 8px; overflow: hidden; margin-bottom: -15px; background: #f8f8f8;">
                                <img src="images/kitchen.jpg" alt="Regular chimney" style="width: 100%; height: 90px; object-fit: cover;">
                            </div>
                            <button id="open-chimney-regular-modal-btn" style="position: relative; z-index: 3; padding: 8px 30px; background: #fff; border: 1px solid #e0e0e0; color: #7d33ff; font-weight: 600; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); cursor: pointer;">Add</button>
                        </div>
                    </div>
                </div>
            </div>
            
            '''
    html = html[:idx_start] + new_services + html[idx_end:]

# Replace Modal block
start_str_modal = '    <!-- TV Check-up Modal -->'
end_str_modal = '</body>'
idx_start_modal = html.find(start_str_modal)
idx_end_modal = html.find(end_str_modal)

if idx_start_modal != -1 and idx_end_modal != -1:
    new_modal = '''    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Modals for Chimney will be added here later if needed
        });
    </script>
'''
    html = html[:idx_start_modal] + new_modal + html[idx_end_modal:]

with open('chimney.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated chimney.html successfully')
