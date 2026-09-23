import sys

# We'll redefine the content for each of the 5 pages with more items.

def insert_more_services(file_name, new_content):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    start_idx, end_idx = -1, -1
    for i, line in enumerate(lines):
        if '<!-- CENTER CONTENT -->' in line:
            start_idx = i + 2
        if '<!-- end center-content -->' in line:
            end_idx = i
            break
            
    if start_idx != -1 and end_idx != -1:
        # keep the banner image
        banner = []
        in_banner = False
        for i in range(start_idx, end_idx):
            if '<div style="position: relative;' in lines[i]:
                in_banner = True
            if in_banner:
                banner.append(lines[i])
                if '</div>\n\n' in lines[i] or (i < end_idx-1 and '<!--' in lines[i+1]):
                    break
        
        final_lines = lines[:start_idx] + banner + [new_content] + lines[end_idx:]
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(final_lines)

# 1. Solar Installation
sp_install_content = '''
                <!-- Residential -->
                <div id="residential-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Residential Solar Setup</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <span style="color: #00875a; font-size: 11px; font-weight: 700; margin-bottom: 8px; display: inline-flex; align-items: center; gap: 4px; text-transform: uppercase;"><i class="fa-solid fa-bookmark" style="color: #00875a;"></i> BESTSELLER</span>
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">On-Grid Solar System (1-3 kW)</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.90 (5K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹4,999 / kW</span> &bull; <span>1 Day</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Mounting structure & panel setup</li>
                                <li style="margin-bottom: 6px;">Net metering assistance included</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/ac.jpg" alt="Solar"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>

                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Off-Grid Solar System (1-3 kW)</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.85 (2K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹6,999 / kW</span> &bull; <span>2 Days</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Includes heavy duty battery bank setup</li>
                                <li style="margin-bottom: 6px;">Independent power for power-cut prone areas</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/tools.jpg" alt="Battery"></div>
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

# 2. Solar Cleaning
sp_clean_content = '''
                <!-- Deep Clean -->
                <div id="deep-clean-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Cleaning Packages</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Basic Cleaning (Up to 5 Panels)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹999</span> &bull; <span>60 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Water wash to remove dust layers</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/cleaning.jpg" alt="Clean"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>

                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <span style="color: #00875a; font-size: 11px; font-weight: 700; margin-bottom: 8px; display: inline-flex; align-items: center; gap: 4px; text-transform: uppercase;"><i class="fa-solid fa-bookmark" style="color: #00875a;"></i> HIGHLY RATED</span>
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Deep Cleaning (6 to 15 Panels)</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.92 (12K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹1,999</span> &bull; <span>120 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Eco-friendly chemical wash to remove bird droppings</li>
                                <li style="margin-bottom: 6px;">Improves power generation up to 15%</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/homecare.jpg" alt="Deep Clean"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>

                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Commercial Cleaning (Above 15 Panels)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">Starts at ₹2,999</span> &bull; <span>Half Day</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Mechanized cleaning for large setups</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/cleaning.jpg" alt="Commercial"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''

# 3. Solar Water Heater
swh_content = '''
                <!-- Repair -->
                <div id="repair-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Repair & Maintenance</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <span style="color: #00875a; font-size: 11px; font-weight: 700; margin-bottom: 8px; display: inline-flex; align-items: center; gap: 4px; text-transform: uppercase;"><i class="fa-solid fa-bookmark" style="color: #00875a;"></i> COMMON ISSUE</span>
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Heating Issue Repair</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.75 (4K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹799</span> &bull; <span>60 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Descaling of glass tubes to fix heating</li>
                                <li style="margin-bottom: 6px;">Checking thermostat and backup heater</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/plumber.jpg" alt="Repair"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>

                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Leakage / Valve Replacement</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹499</span> &bull; <span>45 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Fixing tank dripping or pressure valve issues</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/cleaning.jpg" alt="Leak"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>

                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Full New Installation (ETC / FPC)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹1,999</span> &bull; <span>180 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Mounting, assembling tubes, plumbing connections</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/tools.jpg" alt="Install"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''

# 4. RO Service
ro_content = '''
                <!-- Service -->
                <div id="service-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">RO Repair & Service</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <span style="color: #00875a; font-size: 11px; font-weight: 700; margin-bottom: 8px; display: inline-flex; align-items: center; gap: 4px; text-transform: uppercase;"><i class="fa-solid fa-bookmark" style="color: #00875a;"></i> BESTSELLER</span>
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Comprehensive RO Service</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.95 (50K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹499</span> &bull; <span>45 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Cleaning internal filters and water tank</li>
                                <li style="margin-bottom: 6px;">TDS level adjustment and checking pipes</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/plumber.jpg" alt="Service"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>

                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">RO Filter / Membrane Replacement</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.85 (15K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹1,499</span> &bull; <span>60 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">High-grade genuine filter and membrane</li>
                                <li style="margin-bottom: 6px;">Restores water taste and purity</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/homecare.jpg" alt="Filter"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>

                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">RO Uninstallation / Re-installation</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹399 / ₹599</span> &bull; <span>30 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Safe removal or mounting on wall</li>
                                <li style="margin-bottom: 6px;">Inlet/outlet plumbing connection</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/tools.jpg" alt="Install"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''

# 5. Tank Cleaning
tank_content = '''
                <!-- Cleaning -->
                <div id="cleaning-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Tank Cleaning Services</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <span style="color: #00875a; font-size: 11px; font-weight: 700; margin-bottom: 8px; display: inline-flex; align-items: center; gap: 4px; text-transform: uppercase;"><i class="fa-solid fa-bookmark" style="color: #00875a;"></i> HIGHLY RATED</span>
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Overhead Tank (Up to 1000L)</h4>
                            <div class="service-rating" style="margin-bottom: 8px;"><i class="fa-solid fa-star"></i><a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.80 (22K reviews)</a></div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹899</span> &bull; <span>60 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Mechanized 6-step deep cleaning</li>
                                <li style="margin-bottom: 6px;">UV treatment & anti-bacterial spray</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/cleaning.jpg" alt="Tank"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>

                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Large Overhead Tank (1000L - 2000L)</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹1,399</span> &bull; <span>90 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Sludge removal and high-pressure wash</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/homecare.jpg" alt="Large Tank"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>

                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700; margin-top: 5px;">Underground Sump Cleaning</h4>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;"><span style="font-weight: 700; color: #000;">₹1,799</span> &bull; <span>120 mins</span></div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Pump out dirty water, scrubbing and disinfection</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;"><img src="images/plumber.jpg" alt="Sump"></div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>
'''

insert_more_services('solar-installation.html', sp_install_content)
insert_more_services('solar-cleaning.html', sp_clean_content)
insert_more_services('solar-water-heater.html', swh_content)
insert_more_services('ro-service.html', ro_content)
insert_more_services('water-tank-cleaning.html', tank_content)
print("Updated all 5 files with extensive services!")
