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


# 1. Packers & Movers
pm_sidebar = [('local', 'Local', 'tools.jpg'), ('outstation', 'Outstation', 'homecare.jpg')]
pm_content = '''
                <div id="local-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Within City Shifting</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <span style="color: #00875a; font-size: 11px; font-weight: 700; margin-bottom: 8px; display: inline-flex; align-items: center; gap: 4px; text-transform: uppercase;"><i class="fa-solid fa-bookmark" style="color: #00875a;"></i> BESTSELLER</span>
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">1 BHK / 2 BHK Shifting</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.8 (8K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">Starts at ₹3,500</span> &bull; <span>4-6 Hours</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Multi-layer safe packing</li>
                                <li style="margin-bottom: 6px;">Loading, transport, and unloading</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/tools.jpg" alt="1BHK"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="outstation-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Between Cities</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Outstation Home Shifting</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">Starts at ₹10,000</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Dedicated truck or shared transport</li>
                                <li style="margin-bottom: 6px;">Insurance coverage available</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/homecare.jpg" alt="Outstation"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('packers-movers.html', 'Packers & Movers', 'Professional Packers<br>& Movers', pm_sidebar, pm_content, [('local', 'local-section'), ('outstation', 'outstation-section')], 'tools.jpg')


# 2. Mini Truck
truck_sidebar = [('truck', 'Mini Truck', 'homecare.jpg'), ('labor', 'Labor', 'carpenter.jpg')]
truck_content = '''
                <div id="truck-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Truck Booking</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Tata Ace / Chota Hathi</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹499 base + ₹25/km</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Ideal for 1 RK or heavy furniture/appliances</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/homecare.jpg" alt="Tata Ace"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="labor-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Helper / Labor</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Loading / Unloading Helper</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹399 per person</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Helps in ground-to-floor lifting</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/carpenter.jpg" alt="Labor"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('mini-truck.html', 'Mini Truck on Rent', 'Instant Mini<br>Truck Rental', truck_sidebar, truck_content, [('truck', 'truck-section'), ('labor', 'labor-section')], 'homecare.jpg')


# 3. Driver on Demand
driver_sidebar = [('local', 'Local', 'carpenter.jpg'), ('outstation', 'Outstation', 'security.jpg')]
driver_content = '''
                <div id="local-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Local Driver</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Hourly Driver (Within City)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹399</span> &bull; <span>4 Hours</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Verified, experienced driver for your personal car</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/carpenter.jpg" alt="Local"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="outstation-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Outstation Driver</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Round Trip Driver</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹999 / day</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Safe driving for long highway trips</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/security.jpg" alt="Outstation"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('driver-on-demand.html', 'Driver on Demand', 'Professional Drivers<br>On Demand', driver_sidebar, driver_content, [('local', 'local-section'), ('outstation', 'outstation-section')], 'carpenter.jpg')


# 4. Maid / Helper
maid_sidebar = [('cleaning', 'Cleaning', 'cleaning.jpg'), ('monthly', 'Monthly', 'homecare.jpg')]
maid_content = '''
                <div id="cleaning-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">One-Time Help</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Deep Cleaning Help</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹599</span> &bull; <span>3 Hours</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">General dusting, sweeping, mopping, utensil washing</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/cleaning.jpg" alt="Cleaning"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="monthly-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Monthly Subscription</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Daily Sweeping & Utensils (Trial)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹1,499</span> &bull; <span>1 Week</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Daily visits by verified local maid</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/homecare.jpg" alt="Monthly"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('maid-helper.html', 'Maid / Helper', 'Trusted Maids &<br>Helpers', maid_sidebar, maid_content, [('cleaning', 'cleaning-section'), ('monthly', 'monthly-section')], 'cleaning.jpg')


# 5. Cook on Demand
cook_sidebar = [('one-time', 'One-Time', 'kitchen.jpg'), ('daily', 'Daily Cook', 'homecare.jpg')]
cook_content = '''
                <div id="onetime-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Party / One-Time</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">One Time Meal Prep (Upto 10 Pax)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹999</span> &bull; <span>3 Hours</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Multi-cuisine preparation for house parties</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/kitchen.jpg" alt="Cook"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="daily-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Monthly Subscription</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Daily Cook (Breakfast + Dinner Trial)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹2,999</span> &bull; <span>1 Week</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">2 meals a day for 4-5 members</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/homecare.jpg" alt="Daily Cook"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('cook-on-demand.html', 'Cook on Demand', 'Delicious Meals<br>At Home', cook_sidebar, cook_content, [('one-time', 'onetime-section'), ('daily', 'daily-section')], 'kitchen.jpg')


# 6. Elder / Patient Care
elder_sidebar = [('attendant', 'Attendant', 'beauty.jpg'), ('nursing', 'Nursing', 'tools.jpg')]
elder_content = '''
                <div id="attendant-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Care Attendants</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">12-Hour Care Attendant (Day/Night)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹899</span> &bull; <span>12 Hrs</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Assistance with feeding, mobility, and hygiene</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/beauty.jpg" alt="Care"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="nursing-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Nursing Procedures</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Nursing Visit (Injection / Dressing)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹299</span> &bull; <span>30 Mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Certified nurse for medical procedures</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/tools.jpg" alt="Nursing"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('elder-care.html', 'Elder / Patient Care', 'Compassionate Care<br>At Home', elder_sidebar, elder_content, [('attendant', 'attendant-section'), ('nursing', 'nursing-section')], 'beauty.jpg')


# 7. Babysitting / Nanny
nanny_sidebar = [('babysitting', 'Babysitting', 'grooming.jpg'), ('newborn', 'Newborn Care', 'beauty.jpg')]
nanny_content = '''
                <div id="babysitting-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Nanny Services</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Hourly Babysitter</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹499</span> &bull; <span>Min 4 Hours</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Engaging toddlers in activities & feeding</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/grooming.jpg" alt="Babysitter"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
                <div id="newborn-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Newborn Care</h2>
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Newborn Care Specialist (Japa Maid)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹1,299</span> &bull; <span>Per Day</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Specialized care for infants and mother</li>
                            </ul>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/beauty.jpg" alt="Newborn"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''
build_page('babysitting.html', 'Babysitting / Nanny', 'Expert Child<br>Care', nanny_sidebar, nanny_content, [('babysitting', 'babysitting-section'), ('newborn', 'newborn-section')], 'grooming.jpg')


# Update index.html links
with open('index.html', 'r', encoding='utf-8') as f:
    idx_lines = f.readlines()

in_modal = False
for i in range(len(idx_lines)):
    if 'id="logistics-modal"' in idx_lines[i]:
        in_modal = True
    if in_modal:
        if '>Packers & Movers<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="#"', 'href="packers-movers.html"')
        elif '>Mini Truck on Rent<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="#"', 'href="mini-truck.html"')
        elif '>Driver on Demand<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="#"', 'href="driver-on-demand.html"')
        elif '>Maid / Helper<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="#"', 'href="maid-helper.html"')
        elif '>Cook on Demand<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="#"', 'href="cook-on-demand.html"')
        elif '>Elder / Patient Care<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="#"', 'href="elder-care.html"')
        elif '>Babysitting / Nanny<' in idx_lines[i]:
            idx_lines[i-2] = idx_lines[i-2].replace('href="#"', 'href="babysitting.html"')
            
    if in_modal and '</div>' in idx_lines[i] and '<!-- Logistics Modal -->' not in ''.join(idx_lines[max(0, i-5):i]):
        if 'id="close-logistics-modal-btn"' not in ''.join(idx_lines[max(0, i-10):i]):
            pass
            # simplistic check, wait for the outer modal div to close
            # We know the modal is relatively self-contained

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(idx_lines)

print("Created 7 pages and updated index.html")
