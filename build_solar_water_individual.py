import sys

with open('cctv-services.html', 'r', encoding='utf-8') as f:
    template_lines = f.readlines()

def build_page(file_name, title, banner_title, sidebar_items, sections_content, js_sections, bg_img='cleaning.jpg'):
    # Find markers in the template
    sidebar_start, sidebar_end, center_start, center_end, script_start, script_end = -1, -1, -1, -1, -1, -1
    for i, line in enumerate(template_lines):
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
                    <img src="images/{bg_img}" alt="{title}" style="width: 100%; height: 300px; object-fit: cover; display: block;">
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
    header_lines = template_lines[:sidebar_start]
    for i in range(len(header_lines)):
        if 'CCTV Camera Services' in header_lines[i]:
            header_lines[i] = header_lines[i].replace('CCTV Camera Services', title)
            
    final_lines = header_lines + [sidebar_html, '            </div>\n\n            <!-- CENTER CONTENT -->\n            <div class="center-content">\n', center_html, '            </div><!-- end center-content -->\n'] + template_lines[center_end+1:script_start] + [js_html] + template_lines[script_end:]
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)

# 1. Solar Panel Installation
sp_install_sidebar = [('residential', 'Residential', 'ac.jpg'), ('commercial', 'Commercial', 'tools.jpg'), ('inverter', 'Inverter', 'security.jpg')]
sp_install_content = '''
                <!-- Residential -->
                <div id="residential-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Residential Solar Setup</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Rooftop Solar Installation (1-3 kW)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹5,999 / kW</span> &bull; <span>1 Day</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Mounting structure and panel installation</li>
                                <li style="margin-bottom: 6px;">Wiring and basic inverter setup</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/ac.jpg" alt="Solar"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <!-- Inverter -->
                <div id="inverter-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Inverter Integration</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Hybrid Inverter Setup</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹1,499</span> &bull; <span>3 Hours</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Connecting panels to hybrid inverter and grid</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/security.jpg" alt="Inverter"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('solar-installation.html', 'Solar Panel Installation', 'Solar Panel<br>Installation', sp_install_sidebar, sp_install_content, [('residential', 'residential-section'), ('inverter', 'inverter-section')], 'ac.jpg')

# 2. Solar Panel Cleaning
sp_clean_sidebar = [('deep-clean', 'Deep Cleaning', 'cleaning.jpg'), ('chemical', 'Chemical Wash', 'homecare.jpg')]
sp_clean_content = '''
                <!-- Deep Clean -->
                <div id="deep-clean-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Cleaning Packages</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Deep Cleaning (Up to 10 Panels)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹1,999</span> &bull; <span>120 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Eco-friendly soft wash to remove dust and bird droppings</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/cleaning.jpg" alt="Clean"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('solar-cleaning.html', 'Solar Panel Cleaning', 'Professional Panel<br>Cleaning', sp_clean_sidebar, sp_clean_content, [('deep-clean', 'deep-clean-section')], 'cleaning.jpg')

# 3. Solar Water Heater
swh_sidebar = [('repair', 'Repair', 'plumber.jpg'), ('install', 'Installation', 'tools.jpg')]
swh_content = '''
                <!-- Repair -->
                <div id="repair-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Repair & Service</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Water Heater Repair</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹799</span> &bull; <span>60 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Fixing leaks, replacing glass tubes and checking valves</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/plumber.jpg" alt="Repair"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('solar-water-heater.html', 'Solar Water Heater', 'Solar Water Heater<br>Services', swh_sidebar, swh_content, [('repair', 'repair-section')], 'plumber.jpg')

# 4. RO Service
ro_sidebar = [('service', 'Service', 'plumber.jpg'), ('repair', 'Repair', 'tools.jpg'), ('install', 'Install', 'homecare.jpg')]
ro_content = '''
                <!-- Service -->
                <div id="service-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">RO Servicing</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Comprehensive RO Service</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹499</span> &bull; <span>45 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Pre-filter replacement and tank cleaning</li>
                                <li style="margin-bottom: 6px;">TDS checking and tuning</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/plumber.jpg" alt="Service"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('ro-service.html', 'RO / Water Purifier', 'Pure Drinking<br>Water', ro_sidebar, ro_content, [('service', 'service-section')], 'plumber.jpg')

# 5. Tank Cleaning
tank_sidebar = [('cleaning', 'Cleaning', 'cleaning.jpg'), ('underground', 'Underground', 'tools.jpg')]
tank_content = '''
                <!-- Cleaning -->
                <div id="cleaning-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Tank Cleaning</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Water Tank Cleaning (Up to 1000L)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹899</span> &bull; <span>90 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Mechanized 6-step cleaning with antibacterial spray</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/cleaning.jpg" alt="Tank"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('water-tank-cleaning.html', 'Water Tank Cleaning', 'Hygienic Tank<br>Cleaning', tank_sidebar, tank_content, [('cleaning', 'cleaning-section')], 'cleaning.jpg')


# 6. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_lines = f.readlines()

in_modal = False
for i in range(len(idx_lines)):
    if 'id="security-modal"' in idx_lines[i]:
        in_modal = True
    if in_modal:
        if '>Solar Panel Installation<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="solar-services.html#installation-section"', 'href="solar-installation.html"')
        elif '>Solar Panel Cleaning<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="solar-services.html#cleaning-section"', 'href="solar-cleaning.html"')
        elif '>Solar Water Heater<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="solar-services.html#water-heater-section"', 'href="solar-water-heater.html"')
        elif '>RO / Water Purifier<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="water-solutions.html#ro-service-section"', 'href="ro-service.html"')
        elif '>Water Tank Cleaning<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="water-solutions.html#tank-cleaning-section"', 'href="water-tank-cleaning.html"')
    
    if in_modal and '</div>' in idx_lines[i] and '<!-- end modal -->' in idx_lines[i+1] if i+1 < len(idx_lines) else False:
        in_modal = False

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(idx_lines)
    
print("Successfully generated all 5 pages and updated index.html")
