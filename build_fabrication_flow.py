import sys
import re

# 1. Update index.html for modal trigger and HTML
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

fabrication_modal_html = '''
    <!-- Fabrication Modal -->
    <div id="fabrication-modal" class="modal-overlay hidden">
        <div class="modal-content" style="max-width: 600px;">
            <button id="close-fabrication-modal-btn" class="modal-close"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="modal-title">Fabrication, Grills & Roofing</h3>

            <h4 class="modal-subtitle">Window Grills & Balcony Railings</h4>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="grills-railings.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/fabrication.jpg" alt="Grills & Railings">
                    <p>Window Grills & Balcony Railings</p>
                </a>
            </div>

            <h4 class="modal-subtitle">Gates & Doors</h4>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="gates-doors.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/tools.jpg" alt="Gates & Doors">
                    <p>Gates & Doors</p>
                </a>
            </div>

            <h4 class="modal-subtitle">Sheds & Roofing</h4>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="sheds-roofing.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/homecare.jpg" alt="Sheds & Roofing">
                    <p>Sheds & Roofing</p>
                </a>
            </div>

            <h4 class="modal-subtitle">Welding & Repair Services</h4>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px;">
                <a href="welding-repair.html" class="modal-item" style="text-decoration: none;">
                    <img src="images/plumber.jpg" alt="Welding & Repair">
                    <p>Welding & Repair</p>
                </a>
            </div>
        </div>
    </div>
'''

# Find the trigger div and replace it
# It looks like:
# <div class="service-item">
#     <div class="service-icon"><img src="images/fabrication.jpg" alt="Fabrication"></div>
#     <p>Fabrication, Grills & Roofing</p>
# </div>
idx_lines = idx_content.splitlines(True)
for i in range(len(idx_lines)):
    if '<div class="service-item">' in idx_lines[i] and 'Fabrication, Grills & Roofing' in idx_lines[i+2]:
        idx_lines[i] = '                <div id="fabrication-modal-trigger" class="service-item" style="cursor: pointer;">\n'
        break

script_idx = -1
for i in range(len(idx_lines)):
    if '<script src="app.js?v=7"></script>' in idx_lines[i]:
        script_idx = i
        break

if script_idx != -1:
    idx_lines.insert(script_idx, fabrication_modal_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(idx_lines)
    print("Updated index.html")
else:
    print("Failed to find script tag in index.html")


# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_lines = f.readlines()

fabrication_js = '''
    // Fabrication Modal Logic
    const fabricationTrigger = document.getElementById('fabrication-modal-trigger');
    const fabricationModal = document.getElementById('fabrication-modal');
    const closeFabricationBtn = document.getElementById('close-fabrication-modal-btn');

    if (fabricationTrigger && fabricationModal && closeFabricationBtn) {
        fabricationTrigger.addEventListener('click', () => {
            fabricationModal.classList.remove('hidden');
        });

        closeFabricationBtn.addEventListener('click', () => {
            fabricationModal.classList.add('hidden');
        });

        fabricationModal.addEventListener('click', (e) => {
            if (e.target === fabricationModal) {
                fabricationModal.classList.add('hidden');
            }
        });
    }
'''

for i in range(len(app_lines)-1, -1, -1):
    if '});' in app_lines[i]:
        app_lines.insert(i, fabrication_js)
        with open('app.js', 'w', encoding='utf-8') as f:
            f.writelines(app_lines)
        print("Updated app.js")
        break


# 3. Build the 4 pages
with open('cctv-services.html', 'r', encoding='utf-8') as f:
    template_lines = f.readlines()

def build_page(file_name, title, banner_title, sidebar_items, sections_content, js_sections, bg_img='fabrication.jpg'):
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
    
    center_html = f'''                <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 30px;">
                    <img src="images/{bg_img}" alt="{title}" style="width: 100%; height: 300px; object-fit: cover; display: block;">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); display: flex; align-items: center; justify-content: center;">
                        <h2 style="color: #fff; font-size: 42px; font-weight: 700; text-align: center; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); margin: 0;">{banner_title}</h2>
                    </div>
                </div>\n\n'''
    center_html += sections_content
    
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

    header_lines = template_lines[:sidebar_start]
    for i in range(len(header_lines)):
        if 'CCTV Camera Services' in header_lines[i]:
            header_lines[i] = header_lines[i].replace('CCTV Camera Services', title)
            
    final_lines = header_lines + [sidebar_html, '            </div>\n\n            <!-- CENTER CONTENT -->\n            <div class="center-content">\n', center_html, '            </div><!-- end center-content -->\n'] + template_lines[center_end+1:script_start] + [js_html] + template_lines[script_end:]
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)

# Grills & Railings
grills_sidebar = [('ms', 'MS Grills', 'fabrication.jpg'), ('ss', 'SS Railing', 'tools.jpg'), ('safety', 'Safety Net', 'homecare.jpg')]
grills_content = '''
                <div id="ms-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">MS Grill Fabrication</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <span style="color: #00875a; font-size: 11px; font-weight: 700; margin-bottom: 8px; display: inline-flex; align-items: center; gap: 4px; text-transform: uppercase;"><i class="fa-solid fa-bookmark" style="color: #00875a;"></i> HIGHLY RATED</span>
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Window Safety Grills (MS)</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.85 (3K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹150 / sq. ft</span> &bull; <span>Starts</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Custom designs using mild steel</li>
                                <li style="margin-bottom: 6px;">Includes primer and basic paint</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/fabrication.jpg" alt="MS Grill"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="ss-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">SS Railing</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Stainless Steel Balcony / Stair Railing</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹450 / running ft</span> &bull; <span>Starts</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Rust-free 304 grade stainless steel</li>
                                <li style="margin-bottom: 6px;">Options with tough glass available</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/tools.jpg" alt="SS Railing"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="safety-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Balcony Safety</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Balcony Safety Net / Full Grill</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹2,500</span> &bull; <span>Base Price</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Secure balconies for kids and pets</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/homecare.jpg" alt="Safety"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('grills-railings.html', 'Window Grills & Balcony Railings', 'Custom Grills &<br>Railings', grills_sidebar, grills_content, [('ms', 'ms-section'), ('ss', 'ss-section'), ('safety', 'safety-section')], 'fabrication.jpg')


# Gates & Doors
gates_sidebar = [('iron', 'Iron Gate', 'tools.jpg'), ('shutter', 'Rolling Shutter', 'fabrication.jpg'), ('collapsible', 'Collapsible', 'homecare.jpg')]
gates_content = '''
                <div id="iron-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Main Entrance Gates</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Heavy Iron Gate Fabrication</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹250 / kg</span> &bull; <span>Fabrication</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Custom heavy duty sliding or swing gates</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/tools.jpg" alt="Iron Gate"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="shutter-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Rolling Shutters</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Rolling Shutter Installation / Repair</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹1,499</span> &bull; <span>Repair Starts</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Spring replacement, greasing and alignment</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/fabrication.jpg" alt="Shutter"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="collapsible-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Collapsible Gates</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Channel Gate Installation</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹200 / sq. ft</span> &bull; <span>Starts</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Sliding collapsible gates for shop fronts / homes</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/homecare.jpg" alt="Collapsible"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('gates-doors.html', 'Gates & Doors', 'Iron Gates &<br>Shutters', gates_sidebar, gates_content, [('iron', 'iron-section'), ('shutter', 'shutter-section'), ('collapsible', 'collapsible-section')], 'tools.jpg')


# Sheds & Roofing
sheds_sidebar = [('parking', 'Parking Shed', 'homecare.jpg'), ('tin', 'Tin Roofing', 'fabrication.jpg'), ('terrace', 'Terrace Shed', 'tools.jpg')]
sheds_content = '''
                <div id="parking-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Parking Sheds</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Car Parking Shed (Polycarbonate)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹250 / sq. ft</span> &bull; <span>Starts</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">MS frame structure with transparent/tinted sheets</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/homecare.jpg" alt="Parking"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="tin-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Tin / Asbestos Roofing</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Tin Sheet Roofing</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹180 / sq. ft</span> &bull; <span>Starts</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Cost-effective roofing for godowns or open areas</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/fabrication.jpg" alt="Tin"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="terrace-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Terrace Sheds</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Fabricated Terrace Room/Shed</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹300 / sq. ft</span> &bull; <span>Starts</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Sturdy MS frame covered with GI sheets</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/tools.jpg" alt="Terrace"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('sheds-roofing.html', 'Sheds & Roofing', 'Durable Roofing<br>Solutions', sheds_sidebar, sheds_content, [('parking', 'parking-section'), ('tin', 'tin-section'), ('terrace', 'terrace-section')], 'homecare.jpg')


# Welding & Repair
welding_sidebar = [('welding', 'Welding', 'plumber.jpg'), ('latch', 'Lock / Latch', 'tools.jpg')]
welding_content = '''
                <div id="welding-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">General Welding</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">General Welding Work / Repair</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹499</span> &bull; <span>Visiting charge</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Joining broken iron joints, grills or gates</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/plumber.jpg" alt="Welding"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="latch-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Latch & Fittings</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Lock / Latch Fixing on Iron Gate</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹399</span> &bull; <span>Labor Only</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Welding new aldrops, handles or hinges</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/tools.jpg" alt="Latch"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('welding-repair.html', 'Welding & Repair Services', 'Quick Welding<br>& Repairs', welding_sidebar, welding_content, [('welding', 'welding-section'), ('latch', 'latch-section')], 'plumber.jpg')

print("Created 4 fabrication pages")
