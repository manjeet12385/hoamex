import sys

with open('security-solar-water.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Define the new sidebar and center content
new_sidebar = '''                <div class="select-service-card">
                    <h3 style="margin-bottom: 20px; font-size: 11px; color: #777; border-bottom: 1px solid #eee; padding-bottom: 10px; display: inline-block; font-weight: normal;">Select a service</h3>
                    <div class="service-grid">
                        <a href="#cctv" class="service-item">
                            <div class="service-item-img">
                                <img src="images/security.jpg" alt="CCTV">
                            </div>
                            <span style="font-size: 10px; color: #333;">CCTV</span>
                        </a>
                        <a href="#smart-locks" class="service-item">
                            <div class="service-item-img">
                                <img src="images/homecare.jpg" alt="Smart Locks">
                            </div>
                            <span style="font-size: 10px; color: #333;">Smart Locks</span>
                        </a>
                        <a href="#solar-panel" class="service-item">
                            <div class="service-item-img">
                                <img src="images/ac.jpg" alt="Solar Panel">
                            </div>
                            <span style="font-size: 10px; color: #333;">Solar Panel</span>
                        </a>
                        <a href="#ro-service" class="service-item">
                            <div class="service-item-img">
                                <img src="images/plumber.jpg" alt="RO Service">
                            </div>
                            <span style="font-size: 10px; color: #333;">RO Service</span>
                        </a>
                        <a href="#water-tank" class="service-item">
                            <div class="service-item-img">
                                <img src="images/cleaning.jpg" alt="Water Tank">
                            </div>
                            <span style="font-size: 10px; color: #333;">Water Tank</span>
                        </a>
                    </div>
                </div>
'''

new_center_content = '''                <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 30px;">
                    <img src="images/security.jpg" alt="Home Security" style="width: 100%; height: 300px; object-fit: cover; display: block;">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.3); display: flex; align-items: center; justify-content: center;">
                        <h2 style="color: #fff; font-size: 42px; font-weight: 700; text-align: center; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); margin: 0;">Secure & Power<br>Your Home</h2>
                    </div>
                </div>

                <!-- CCTV -->
                <div id="cctv-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">CCTV Camera</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <span style="color: #00875a; font-size: 11px; font-weight: 700; margin-bottom: 8px; display: inline-flex; align-items: center; gap: 4px; text-transform: uppercase;"><i class="fa-solid fa-bookmark" style="color: #00875a;"></i> BESTSELLER</span>
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">CCTV Installation (Up to 4 cameras)</h4>
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
                                <img src="images/security.jpg" alt="CCTV">
                            </div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>

                <!-- Smart Locks -->
                <div id="smart-locks-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Smart Locks</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Smart Lock Installation</h4>
                            <div class="service-rating" style="margin-bottom: 8px;">
                                <i class="fa-solid fa-star"></i>
                                <a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.85 (8K reviews)</a>
                            </div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;">
                                <span style="font-weight: 700; color: #000;">₹999</span> &bull; <span>60 mins</span>
                            </div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Compatible with wooden & metal doors</li>
                                <li style="margin-bottom: 6px;">Fingerprint, RFID & PIN setup</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;">
                                <img src="images/homecare.jpg" alt="Smart Lock">
                            </div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>

                <!-- Solar Panel -->
                <div id="solar-panel-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Solar Services</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Solar Panel Cleaning</h4>
                            <div class="service-rating" style="margin-bottom: 8px;">
                                <i class="fa-solid fa-star"></i>
                                <a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.78 (11K reviews)</a>
                            </div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;">
                                <span style="font-weight: 700; color: #000;">₹1,999</span> &bull; <span>180 mins</span>
                            </div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Deep cleaning with specialized eco-friendly liquid</li>
                                <li style="margin-bottom: 6px;">Boosts efficiency up to 15%</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;">
                                <img src="images/cleaning.jpg" alt="Solar Cleaning">
                            </div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>

                <!-- RO Service -->
                <div id="ro-service-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Water Solutions</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <span style="color: #00875a; font-size: 11px; font-weight: 700; margin-bottom: 8px; display: inline-flex; align-items: center; gap: 4px; text-transform: uppercase;"><i class="fa-solid fa-bookmark" style="color: #00875a;"></i> HIGHLY RATED</span>
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Comprehensive RO Service</h4>
                            <div class="service-rating" style="margin-bottom: 8px;">
                                <i class="fa-solid fa-star"></i>
                                <a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.95 (50K reviews)</a>
                            </div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;">
                                <span style="font-weight: 700; color: #000;">₹499</span> &bull; <span>45 mins</span>
                            </div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Filter check and internal tank cleaning</li>
                                <li style="margin-bottom: 6px;">TDS level adjustment</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;">
                                <img src="images/plumber.jpg" alt="RO Service">
                            </div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>

                <!-- Water Tank -->
                <div id="water-tank-section" style="margin-bottom: 36px; padding-top: 20px;">
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Water Tank Cleaning (Up to 1000L)</h4>
                            <div class="service-rating" style="margin-bottom: 8px;">
                                <i class="fa-solid fa-star"></i>
                                <a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.80 (22K reviews)</a>
                            </div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;">
                                <span style="font-weight: 700; color: #000;">₹899</span> &bull; <span>90 mins</span>
                            </div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">6-step mechanized cleaning process</li>
                                <li style="margin-bottom: 6px;">Anti-bacterial spray application</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;">
                                <img src="images/cleaning.jpg" alt="Water Tank">
                            </div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''

new_script = '''            // Scroll Logic
            const sections = [
                { btn: 'cctv', section: 'cctv-section' },
                { btn: 'smart-locks', section: 'smart-locks-section' },
                { btn: 'solar-panel', section: 'solar-panel-section' },
                { btn: 'ro-service', section: 'ro-service-section' },
                { btn: 'water-tank', section: 'water-tank-section' }
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

# Also fix the top-section (Title)
for i in range(len(lines)):
    if 'Spa Prime' in lines[i] and '<title>' in lines[i]:
        lines[i] = lines[i].replace('Spa Prime', 'Home Security, Solar & Water')
    if 'Spa Prime' in lines[i] and '<h1' in lines[i]:
        lines[i] = lines[i].replace('Spa Prime', 'Home Security, Solar & Water')

if sidebar_start != -1 and center_end != -1:
    final_lines = lines[:sidebar_start] + [new_sidebar] + ['            </div>\n\n'] + ['            <!-- CENTER CONTENT -->\n'] + ['            <div class="center-content">\n'] + [new_center_content] + ['            </div><!-- end center-content -->\n'] + lines[center_end+1:script_start] + [new_script] + lines[script_end:]
    
    with open('security-solar-water.html', 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    print("Rewrote security-solar-water.html successfully")
else:
    print("Could not find markers")
