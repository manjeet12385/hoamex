import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ('index.html', 'header.html', 'footer.html')]

# We'll define a few base templates of data blocks to inject.
# Each page will have 3 sections on the left sidebar.

data_map = {
    # AC & Appliances
    'ac-repair.html': ('AC Repair', 'images/ac.jpg', [
        ('Service', [('Foam Jet AC Service', '₹499', 'Deep cleaning with foam and jet'), ('Power Jet AC Service', '₹399', 'Water jet cleaning')]),
        ('Repair', [('AC Not Cooling', '₹299', 'Inspection and diagnosis'), ('Water Leakage', '₹199', 'Drain pipe clearing')]),
        ('Install', [('Split AC Installation', '₹1499', 'Standard wall mount'), ('Window AC Installation', '₹699', 'Basic installation')])
    ]),
    'washing-machine.html': ('Washing Machine Repair', 'images/washing_machine.jpg', [
        ('Repair', [('Not Starting/Spinning', '₹299', 'Motor or PCB check'), ('Making Noise', '₹199', 'Drum and bearing check')]),
        ('Install', [('Fully Auto Installation', '₹499', 'Inlet/outlet setup')]),
        ('Service', [('Deep Cleaning', '₹599', 'Descaling and tub clean')])
    ]),
    'fridge.html': ('Refrigerator Repair', 'images/refrigerator.jpg', [
        ('Repair', [('Not Cooling', '₹299', 'Compressor and gas check'), ('Water Leakage', '₹199', 'Drain block clearing')]),
        ('Gas Refill', [('Single Door Refill', '₹1200', 'R134a or R600a refill')]),
        ('Service', [('Deep Cleaning', '₹499', 'Interior and coil clean')])
    ]),
    
    # EPC
    'electrician.html': ('Electrician', 'images/electrician_icon.jpg', [
        ('Switches', [('Switchboard Repair', '₹99', 'Fix loose connections'), ('New Switch Installation', '₹49', 'Per switch cost')]),
        ('Wiring', [('Wiring per meter', '₹50', 'Concealed or open wiring')]),
        ('MCB', [('MCB/Fuse Replacement', '₹149', 'Single pole MCB')])
    ]),
    'plumber.html': ('Plumber', 'images/plumber.jpg', [
        ('Tap/Mixer', [('Tap Repair', '₹99', 'Spindle change'), ('Mixer Installation', '₹299', 'Wall/Sink mixer')]),
        ('Leakage', [('Pipe Leakage', '₹199', 'PVC/CPVC repair')]),
        ('Toilet', [('Flush Tank Repair', '₹149', 'Syphon or ball valve issue')])
    ]),
    'carpenter.html': ('Carpenter', 'images/carpenter_icon.jpg', [
        ('Doors', [('Door Alignment', '₹149', 'Fixing hinges'), ('Lock Replacement', '₹199', 'Cylindrical or mortise lock')]),
        ('Furniture', [('Minor Repair', '₹199', 'Fixing loose joints')]),
        ('Drill', [('Drill Hole', '₹49', 'Per hole in wall/wood')])
    ]),
    'wood-polish.html': ('Wood Polish', 'images/renovation.jpg', [
        ('PU Polish', [('PU Polish (per sqft)', '₹80', 'High gloss finish')]),
        ('Melamine', [('Melamine Polish', '₹60', 'Matte or gloss')]),
        ('Touchup', [('Minor Touchup', '₹499', 'Scratch removal')])
    ]),
    'fan-installation.html': ('Fan Installation', 'images/tools.jpg', [
        ('Ceiling Fan', [('Installation', '₹149', 'With hook checking'), ('Repair', '₹99', 'Capacitor change')]),
        ('Exhaust Fan', [('Installation', '₹99', 'Wall mount')]),
        ('Wall Fan', [('Installation', '₹149', 'Wall bracket mount')])
    ]),
    'furniture-assembly.html': ('Furniture Assembly', 'images/carpenter_icon.jpg', [
        ('Bed', [('Assembly', '₹499', 'Standard double bed')]),
        ('Wardrobe', [('Assembly', '₹699', '2-door wardrobe')]),
        ('Table', [('Assembly', '₹299', 'Study or dining table')])
    ]),
    'geyser-service.html': ('Geyser Service', 'images/plumber.jpg', [
        ('Install', [('Installation', '₹399', 'Wall mounting')]),
        ('Repair', [('Not Heating', '₹299', 'Element or thermostat issue')]),
        ('Uninstall', [('Uninstallation', '₹199', 'Safe removal')])
    ]),
    
    # Cleaning
    'full-home-cleaning.html': ('Full Home Cleaning', 'images/cleaning.jpg', [
        ('Furnished', [('1 BHK Cleaning', '₹2499', 'Deep clean including bathroom'), ('2 BHK Cleaning', '₹3499', 'Deep clean')]),
        ('Unfurnished', [('Move-in Cleaning', '₹1999', 'Empty house deep clean')]),
        ('Sofa', [('Sofa Cleaning (per seat)', '₹249', 'Shampoo and vacuum')])
    ]),
    'pest-control.html': ('Pest Control', 'images/pest_control_icon.jpg', [
        ('Cockroach', [('1 BHK Treatment', '₹899', 'Gel and spray')]),
        ('Termite', [('Inspection', '₹0', 'Free inspection')]),
        ('Bed Bugs', [('2 Visit Treatment', '₹1499', 'Spray treatment')])
    ]),
    
    # Renovation
    'full-home-renovation.html': ('Home Renovation', 'images/renovation.jpg', [
        ('Consultation', [('Design Visit', '₹499', 'Expert interior designer')]),
        ('Kitchen', [('Modular Kitchen', '₹50000', 'Starting price')]),
        ('Bathroom', [('Full Remodel', '₹30000', 'Starting price')])
    ]),
    'painting.html': ('Painting', 'images/painting_icon.jpg', [
        ('Interior', [('1 BHK Painting', '₹8000', 'Tractor emulsion')]),
        ('Exterior', [('Wall Painting', '₹12', 'Per sqft')]),
        ('Texture', [('Accent Wall', '₹3000', 'Royale play texture')])
    ]),
    
    # Beauty
    'salon-women.html': ('Salon for Women', 'images/beauty.jpg', [
        ('Waxing', [('Full Arms + Legs', '₹499', 'Honey wax'), ('Rica Wax', '₹799', 'Premium peel-off')]),
        ('Facial', [('Fruit Facial', '₹599', 'Glow treatment')]),
        ('Hair', [('Haircut', '₹299', 'Any style')])
    ]),
    'spa-women.html': ('Spa for Women', 'images/beauty.jpg', [
        ('Massage', [('Full Body Massage', '₹1299', 'Swedish massage 60 mins')]),
        ('Pain Relief', [('Deep Tissue', '₹1499', 'Targeted pain relief')]),
        ('Head', [('Head & Shoulder', '₹499', '30 mins relaxation')])
    ]),
    
    # Grooming
    'salon-men.html': ('Salon for Men', 'images/grooming.jpg', [
        ('Haircut', [('Haircut + Wash', '₹199', 'Professional styling')]),
        ('Beard', [('Beard Grooming', '₹149', 'Trimming and styling')]),
        ('Color', [('Hair Color', '₹399', 'Ammonia free')])
    ]),
    'massage-men.html': ('Massage for Men', 'images/grooming.jpg', [
        ('Massage', [('Full Body Massage', '₹999', 'Relaxing therapy')]),
        ('Head', [('Head Massage', '₹299', 'With warm oil')]),
        ('Back', [('Back & Shoulders', '₹499', 'Pain relief')])
    ])
}

html_template = '''
        <!-- Top title row -->
        <div class="top-section">
            <div>
                <h1 class="page-title">{title}</h1>
                <div class="page-rating">
                    <i class="fa-solid fa-star"></i>
                    <strong>4.82</strong>
                    <span>(3.9 M bookings)</span>
                </div>
            </div>
            <div style="background: #e8f5e9; color: #2e7d32; padding: 5px 10px; border-radius: 6px; text-align: center; border: 1px solid #c8e6c9;">
                <div style="font-size: 10px; font-weight: bold;"><i class="fa-solid fa-clock" style="margin-right: 3px;"></i> Earliest</div>
                <div style="font-size: 12px; margin-top: 2px; font-weight: bold;">Mon, 3:30 PM</div>
            </div>
        </div>

        <!-- 3-Column Layout -->
        <div class="three-col-layout">
            <!-- LEFT SIDEBAR -->
            <div class="left-sidebar">
                <div class="select-service-card">
                    <h3>Select a service</h3>
                    <div class="service-grid">
                        {sidebar_links}
                    </div>
                </div>
            </div>

            <!-- CENTER CONTENT -->
            <div class="center-content">
                <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 30px;">
                    <img src="{image}" alt="{title}" style="width: 100%; height: 250px; object-fit: cover; display: block;">
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); display: flex; align-items: center; justify-content: center;">
                        <h2 style="color: #fff; font-size: 34px; font-weight: 700; text-align: center; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); margin: 0;">{title}</h2>
                    </div>
                </div>
                {center_sections}
            </div>

            <!-- RIGHT SIDEBAR -->
            <div class="right-sidebar">
                <div class="uc-promise-card">
                    <div>
                        <h3>Joamex Promise</h3>
                        <ul>
                            <li><i class="fa-solid fa-check"></i> Verified Professionals</li>
                            <li><i class="fa-solid fa-check"></i> Hassle Free Service</li>
                            <li><i class="fa-solid fa-check"></i> Transparent Pricing</li>
                        </ul>
                    </div>
                    <img src="images/security.jpg" alt="Promise" class="promise-badge">
                </div>
                
                <div class="cart-card">
                    <i class="fa-solid fa-cart-shopping"></i>
                    <p>No items in your cart</p>
                </div>
            </div>
        </div>
'''

for file_name in html_files:
    if file_name not in data_map:
        continue # skip pages we haven't mapped (like original cctv ones, we can leave them or they are already fine)
        
    title, image, sections = data_map[file_name]
    
    sidebar_links = ""
    center_sections = ""
    
    for i, (sec_title, services) in enumerate(sections):
        sec_id = sec_title.lower().replace(' ', '-')
        # sidebar link
        sidebar_links += f'''
                        <a href="#{sec_id}" class="service-item-sidebar">
                            <div class="service-item-img">
                                <img src="{image}" alt="{sec_title}">
                            </div>
                            <span>{sec_title}</span>
                        </a>'''
        
        # center section
        services_html = ""
        for srv_name, srv_price, srv_desc in services:
            services_html += f'''
                    <div class="service-card">
                        <div class="service-card-info">
                            <h4>{srv_name}</h4>
                            <div class="service-rating">
                                <i class="fa-solid fa-star"></i>
                                <a href="#">4.85 (8K reviews)</a>
                            </div>
                            <div class="service-price">
                                <span>{srv_price}</span>
                            </div>
                            <ul class="service-features">
                                <li>{srv_desc}</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap">
                                <img src="{image}" alt="{srv_name}">
                            </div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>'''
            
        center_sections += f'''
                <div id="{sec_id}" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading">{sec_title}</h2>
                    {services_html}
                </div>'''

    final_content = html_template.format(title=title, image=image, sidebar_links=sidebar_links, center_sections=center_sections)
    
    # Read existing file, strip <style> blocks, and inject final_content into <main class="page-wrapper">
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Strip <style> ... </style>
    content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
    
    # Replace everything inside <main class="page-wrapper"> ... </main>
    content = re.sub(r'<main class="page-wrapper">.*?</main>', f'<main class="page-wrapper">{final_content}</main>', content, flags=re.DOTALL)
    
    # If there's scroll script, strip it out too, we can put it in common.js to keep things clean, but it's okay, let's just let common.js handle it
    content = re.sub(r'<script>\s*document.addEventListener\(\'DOMContentLoaded\'.*?</script>', '', content, flags=re.DOTALL)
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected real data into 18 pages and stripped inline CSS.")
