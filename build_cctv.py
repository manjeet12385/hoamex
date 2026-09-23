import sys

with open('cctv-services.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_sidebar = '''                <div class="select-service-card">
                    <h3 style="margin-bottom: 20px; font-size: 11px; color: #777; border-bottom: 1px solid #eee; padding-bottom: 10px; display: inline-block; font-weight: normal;">Select a service</h3>
                    <div class="service-grid">
                        <a href="#installation" class="service-item">
                            <div class="service-item-img">
                                <img src="images/security.jpg" alt="Installation">
                            </div>
                            <span style="font-size: 10px; color: #333;">Installation</span>
                        </a>
                        <a href="#repair" class="service-item">
                            <div class="service-item-img">
                                <img src="images/security.jpg" alt="Repair">
                            </div>
                            <span style="font-size: 10px; color: #333;">Repair & Check</span>
                        </a>
                        <a href="#setup" class="service-item">
                            <div class="service-item-img">
                                <img src="images/homecare.jpg" alt="Setup">
                            </div>
                            <span style="font-size: 10px; color: #333;">DVR Setup</span>
                        </a>
                        <a href="#uninstallation" class="service-item">
                            <div class="service-item-img">
                                <img src="images/cleaning.jpg" alt="Uninstallation">
                            </div>
                            <span style="font-size: 10px; color: #333;">Uninstallation</span>
                        </a>
                        <a href="#extra" class="service-item">
                            <div class="service-item-img">
                                <img src="images/plumber.jpg" alt="Extras">
                            </div>
                            <span style="font-size: 10px; color: #333;">Extras</span>
                        </a>
                    </div>
                </div>
'''

new_center_content = '''                <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 30px;">
                    <img src="images/security.jpg" alt="CCTV Services" style="width: 100%; height: 300px; object-fit: cover; display: block;">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); display: flex; align-items: center; justify-content: center;">
                        <h2 style="color: #fff; font-size: 42px; font-weight: 700; text-align: center; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); margin: 0;">CCTV Camera<br>Services</h2>
                    </div>
                </div>

                <!-- Installation -->
                <div id="installation-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Installation</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <span style="color: #00875a; font-size: 11px; font-weight: 700; margin-bottom: 8px; display: inline-flex; align-items: center; gap: 4px; text-transform: uppercase;"><i class="fa-solid fa-bookmark" style="color: #00875a;"></i> HIGHLY RATED</span>
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">New CCTV Installation (Up to 4 Cameras)</h4>
                            <div class="service-rating" style="margin-bottom: 8px;">
                                <i class="fa-solid fa-star"></i>
                                <a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.91 (15K reviews)</a>
                            </div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;">
                                <span style="font-weight: 700; color: #000;">₹1,499</span> &bull; <span>120 mins</span>
                            </div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Wiring, mounting and DVR setup included</li>
                                <li style="margin-bottom: 6px;">Mobile app configuration for remote viewing</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;">
                                <img src="images/security.jpg" alt="Installation">
                            </div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>

                <!-- Repair -->
                <div id="repair-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Repair & Check</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">CCTV Repair / Troubleshooting</h4>
                            <div class="service-rating" style="margin-bottom: 8px;">
                                <i class="fa-solid fa-star"></i>
                                <a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.85 (8K reviews)</a>
                            </div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;">
                                <span style="font-weight: 700; color: #000;">₹499</span> &bull; <span>45 mins</span>
                            </div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Fixing no-display or offline camera issues</li>
                                <li style="margin-bottom: 6px;">Cleaning lenses for blurred vision</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;">
                                <img src="images/security.jpg" alt="Repair">
                            </div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>

                <!-- Setup -->
                <div id="setup-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">DVR Setup</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">DVR / NVR & Hard Drive Setup</h4>
                            <div class="service-rating" style="margin-bottom: 8px;">
                                <i class="fa-solid fa-star"></i>
                                <a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.78 (5K reviews)</a>
                            </div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;">
                                <span style="font-weight: 700; color: #000;">₹799</span> &bull; <span>60 mins</span>
                            </div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">New hard drive installation and formatting</li>
                                <li style="margin-bottom: 6px;">Recording and playback settings configuration</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;">
                                <img src="images/homecare.jpg" alt="DVR">
                            </div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>

                <!-- Uninstallation -->
                <div id="uninstallation-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Uninstallation</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">CCTV Uninstallation</h4>
                            <div class="service-rating" style="margin-bottom: 8px;">
                                <i class="fa-solid fa-star"></i>
                                <a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.80 (2K reviews)</a>
                            </div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;">
                                <span style="font-weight: 700; color: #000;">₹599</span> &bull; <span>45 mins</span>
                            </div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Safe removal of up to 4 cameras and DVR</li>
                                <li style="margin-bottom: 6px;">Proper packing of hardware (box not included)</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;">
                                <img src="images/cleaning.jpg" alt="Uninstallation">
                            </div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                
                <!-- Extras -->
                <div id="extra-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Extras</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Extra Wire Laying (Per Meter)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;">
                                <span style="font-weight: 700; color: #000;">₹50</span>
                            </div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">High quality coaxial + power cable (3+1)</li>
                                <li style="margin-bottom: 6px;">Neat clipping along the walls</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;">
                                <img src="images/plumber.jpg" alt="Wiring">
                            </div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''

new_script = '''            // Scroll Logic
            const sections = [
                { btn: 'installation', section: 'installation-section' },
                { btn: 'repair', section: 'repair-section' },
                { btn: 'setup', section: 'setup-section' },
                { btn: 'uninstallation', section: 'uninstallation-section' },
                { btn: 'extra', section: 'extra-section' }
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

# Find boundaries
sidebar_start = -1
sidebar_end = -1
center_start = -1
center_end = -1
script_start = -1
script_end = -1

for i, line in enumerate(lines):
    if '<div class="select-service-card">' in line:
        sidebar_start = i
    if '<!-- CENTER CONTENT -->' in line:
        sidebar_end = i - 2
        center_start = i + 1
    if '<!-- end center-content -->' in line:
        center_end = i
    if 'const sections = [' in line:
        script_start = i - 1
    if '});' in line and script_start != -1 and i > script_start:
        script_end = i + 1
        break

for i in range(len(lines)):
    if 'Spa Prime' in lines[i] and '<title>' in lines[i]:
        lines[i] = lines[i].replace('Spa Prime', 'CCTV Camera Services')
    if 'Spa Prime' in lines[i] and '<h1' in lines[i]:
        lines[i] = lines[i].replace('Spa Prime', 'CCTV Camera Services')

if sidebar_start != -1 and center_end != -1:
    final_lines = lines[:sidebar_start] + [new_sidebar] + ['            </div>\n\n'] + ['            <!-- CENTER CONTENT -->\n'] + ['            <div class="center-content">\n'] + [new_center_content] + ['            </div><!-- end center-content -->\n'] + lines[center_end+1:script_start] + [new_script] + lines[script_end:]
    
    with open('cctv-services.html', 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    print("Rewrote cctv-services.html successfully")
else:
    print("Could not find markers")
