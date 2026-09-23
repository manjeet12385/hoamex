import sys

with open('cctv-services.html', 'r', encoding='utf-8') as f:
    cctv_lines = f.readlines()

def build_page(file_name, title, banner_title, sidebar_items, sections_content, js_sections):
    # Find markers in the template
    sidebar_start, sidebar_end, center_start, center_end, script_start, script_end = -1, -1, -1, -1, -1, -1
    for i, line in enumerate(cctv_lines):
        if '<div class="select-service-card">' in line: sidebar_start = i
        if '<!-- CENTER CONTENT -->' in line:
            sidebar_end = i - 2
            center_start = i + 1
        if '<!-- end center-content -->' in line: center_end = i
        if 'const sections = [' in line: script_start = i - 1
        if '});' in line and script_start != -1 and i > script_start:
            script_end = i + 1
            break
            
    # Build sidebar
    sidebar_html = '                <div class="select-service-card">\n'
    sidebar_html += '                    <h3 style="margin-bottom: 20px; font-size: 11px; color: #777; border-bottom: 1px solid #eee; padding-bottom: 10px; display: inline-block; font-weight: normal;">Select a service</h3>\n'
    sidebar_html += '                    <div class="service-grid">\n'
    for s_id, label, img in sidebar_items:
        sidebar_html += f'''                        <a href="#{s_id}" class="service-item">
                            <div class="service-item-img">
                                <img src="images/{img}" alt="{label}">
                            </div>
                            <span style="font-size: 10px; color: #333;">{label}</span>
                        </a>\n'''
    sidebar_html += '                    </div>\n                </div>\n'
    
    # Build center content
    center_html = f'''                <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 30px;">
                    <img src="images/homecare.jpg" alt="{title}" style="width: 100%; height: 300px; object-fit: cover; display: block;">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); display: flex; align-items: center; justify-content: center;">
                        <h2 style="color: #fff; font-size: 42px; font-weight: 700; text-align: center; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); margin: 0;">{banner_title}</h2>
                    </div>
                </div>\n\n'''
    center_html += sections_content
    
    # Build JS
    js_html = '            // Scroll Logic\n            const sections = [\n'
    js_html += ',\n'.join([f"                {{ btn: '{btn}', section: '{sec}' }}" for btn, sec in js_sections])
    js_html += '''
            ];

            sections.forEach(({ btn, section }) => {
                const btnEl = document.querySelector(`a[href="#${btn}"]`);
                const sectionEl = document.getElementById(section);
                if (btnEl && sectionEl) {
                    btnEl.addEventListener('click', (e) => {
                        e.preventDefault();
                        sectionEl.scrollIntoView({ behavior: 'smooth' });
                    });
                }
            });
'''

    # Modify header title
    header_lines = cctv_lines[:sidebar_start]
    for i in range(len(header_lines)):
        if 'CCTV Camera Services' in header_lines[i]:
            header_lines[i] = header_lines[i].replace('CCTV Camera Services', title)
            
    final_lines = header_lines + [sidebar_html, '            </div>\n\n            <!-- CENTER CONTENT -->\n            <div class="center-content">\n', center_html, '            </div><!-- end center-content -->\n'] + cctv_lines[center_end+1:script_start] + [js_html] + cctv_lines[script_end:]
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)

# 1. Smart Locks
smart_sidebar = [
    ('installation', 'Installation', 'homecare.jpg'),
    ('repair', 'Repair', 'tools.jpg'),
    ('doorbell', 'Doorbells', 'security.jpg'),
    ('uninstall', 'Uninstall', 'cleaning.jpg')
]
smart_content = '''
                <!-- Installation -->
                <div id="installation-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Installation</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <span style="color: #00875a; font-size: 11px; font-weight: 700; margin-bottom: 8px; display: inline-flex; align-items: center; gap: 4px; text-transform: uppercase;"><i class="fa-solid fa-bookmark" style="color: #00875a;"></i> HIGHLY RATED</span>
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Smart Lock Installation</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.85 (8K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹999</span> &bull; <span>60 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Compatible with wooden & metal doors</li>
                                <li style="margin-bottom: 6px;">Fingerprint, RFID & PIN setup</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/homecare.jpg" alt="Installation"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <!-- Repair -->
                <div id="repair-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Repair & Check</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Smart Lock Repair</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.75 (3K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹499</span> &bull; <span>45 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Fixing keypad or biometric issues</li>
                                <li style="margin-bottom: 6px;">Motor alignment and battery check</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/tools.jpg" alt="Repair"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <!-- Doorbells -->
                <div id="doorbell-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Video Doorbells</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Video Doorbell Installation</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.80 (5K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹799</span> &bull; <span>60 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Mounting doorbell and wiring to chime</li>
                                <li style="margin-bottom: 6px;">Connecting to home Wi-Fi and mobile app</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/security.jpg" alt="Doorbell"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
smart_js = [('installation', 'installation-section'), ('repair', 'repair-section'), ('doorbell', 'doorbell-section'), ('uninstall', 'repair-section')]
build_page('smart-locks.html', 'Smart Locks & Doorbells', 'Smart Locks &<br>Doorbells', smart_sidebar, smart_content, smart_js)

# 2. Home Alarm Systems
alarm_sidebar = [
    ('installation', 'Installation', 'security.jpg'),
    ('repair', 'Repair', 'tools.jpg'),
    ('sensors', 'Sensors', 'homecare.jpg')
]
alarm_content = '''
                <!-- Installation -->
                <div id="installation-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Installation</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <span style="color: #00875a; font-size: 11px; font-weight: 700; margin-bottom: 8px; display: inline-flex; align-items: center; gap: 4px; text-transform: uppercase;"><i class="fa-solid fa-bookmark" style="color: #00875a;"></i> HIGHLY RATED</span>
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Home Alarm System Setup</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.85 (3K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹1,299</span> &bull; <span>90 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Hub, keypad, and siren installation</li>
                                <li style="margin-bottom: 6px;">Includes up to 5 door/window sensors</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/security.jpg" alt="Installation"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <!-- Repair -->
                <div id="repair-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Repair & Check</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Alarm Troubleshooting</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.75 (1K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹599</span> &bull; <span>60 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Fixing false alarms and connection issues</li>
                                <li style="margin-bottom: 6px;">Battery replacement (batteries extra)</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/tools.jpg" alt="Repair"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
alarm_js = [('installation', 'installation-section'), ('repair', 'repair-section'), ('sensors', 'installation-section')]
build_page('home-alarm.html', 'Home Alarm Systems', 'Home Alarm<br>Systems', alarm_sidebar, alarm_content, alarm_js)

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_lines = f.readlines()

in_modal = False
for i in range(len(idx_lines)):
    if 'id="security-modal"' in idx_lines[i]:
        in_modal = True
    if in_modal:
        if '>Smart Locks & Doorbells<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="security-solar-water.html#smart-locks-section"', 'href="smart-locks.html"')
        elif '>Home Alarm Systems<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="security-solar-water.html"', 'href="home-alarm.html"')
    
    if in_modal and '</div>' in idx_lines[i] and '<!-- end modal -->' in idx_lines[i+1] if i+1 < len(idx_lines) else False:
        in_modal = False

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(idx_lines)
    
print("Successfully generated smart-locks.html and home-alarm.html and updated index.html")
