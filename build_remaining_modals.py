import os

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Make triggers
idx_content = idx_content.replace(
    '<div class="service-item">\n                    <div class="service-icon"><img src="images/ac.jpg" alt="AC"></div>\n                    <p>AC, Appliance & Repair</p>\n                </div>',
    '<div id="ac-modal-trigger" class="service-item" style="cursor: pointer;">\n                    <div class="service-icon"><img src="images/ac.jpg" alt="AC"></div>\n                    <p>AC, Appliance & Repair</p>\n                </div>'
)
idx_content = idx_content.replace(
    '<div class="service-item">\n                    <div class="service-icon"><img src="images/plumber.jpg" alt="Plumber"></div>\n                    <p>Electrician, Plumber & Carpenter</p>\n                </div>',
    '<div id="epc-modal-trigger" class="service-item" style="cursor: pointer;">\n                    <div class="service-icon"><img src="images/plumber.jpg" alt="Plumber"></div>\n                    <p>Electrician, Plumber & Carpenter</p>\n                </div>'
)
idx_content = idx_content.replace(
    '<div class="service-item">\n                    <div class="service-icon"><img src="images/cleaning.jpg" alt="Cleaning"></div>\n                    <p>Cleaning, Pest Control & Safety</p>\n                </div>',
    '<div id="cleaning-modal-trigger" class="service-item" style="cursor: pointer;">\n                    <div class="service-icon"><img src="images/cleaning.jpg" alt="Cleaning"></div>\n                    <p>Cleaning, Pest Control & Safety</p>\n                </div>'
)
idx_content = idx_content.replace(
    '<div class="service-item">\n                    <div class="service-icon"><img src="images/renovation.jpg" alt="Renovation"></div>\n                    <p>Home Renovation & Interior</p>\n                </div>',
    '<div id="reno-modal-trigger" class="service-item" style="cursor: pointer;">\n                    <div class="service-icon"><img src="images/renovation.jpg" alt="Renovation"></div>\n                    <p>Home Renovation & Interior</p>\n                </div>'
)
idx_content = idx_content.replace(
    '<div class="service-item">\n                    <div class="service-icon"><img src="images/beauty.jpg" alt="Beauty"></div>\n                    <p>Women\'s Beauty & Spa</p>\n                </div>',
    '<div id="beauty-modal-trigger" class="service-item" style="cursor: pointer;">\n                    <div class="service-icon"><img src="images/beauty.jpg" alt="Beauty"></div>\n                    <p>Women\'s Beauty & Spa</p>\n                </div>'
)
idx_content = idx_content.replace(
    '<div class="service-item">\n                    <div class="service-icon"><img src="images/grooming.jpg" alt="Grooming"></div>\n                    <p>Men\'s Grooming & Massage</p>\n                </div>',
    '<div id="grooming-modal-trigger" class="service-item" style="cursor: pointer;">\n                    <div class="service-icon"><img src="images/grooming.jpg" alt="Grooming"></div>\n                    <p>Men\'s Grooming & Massage</p>\n                </div>'
)

new_modals = '''
    <!-- AC Modal -->
    <div id="ac-modal" class="modal-overlay hidden">
        <div class="modal-content" style="max-width: 600px;">
            <button id="close-ac-modal-btn" class="modal-close"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="modal-title">AC, Appliance & Repair</h3>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/ac.jpg" alt="AC"><p>AC Repair</p></a>
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/tools.jpg" alt="Washing"><p>Washing Machine</p></a>
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/homecare.jpg" alt="Fridge"><p>Refrigerator</p></a>
            </div>
        </div>
    </div>

    <!-- EPC Modal -->
    <div id="epc-modal" class="modal-overlay hidden">
        <div class="modal-content" style="max-width: 600px;">
            <button id="close-epc-modal-btn" class="modal-close"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="modal-title">Electrician, Plumber & Carpenter</h3>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/plumber.jpg" alt="Plumber"><p>Plumber</p></a>
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/tools.jpg" alt="Electrician"><p>Electrician</p></a>
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/carpenter.jpg" alt="Carpenter"><p>Carpenter</p></a>
            </div>
        </div>
    </div>

    <!-- Cleaning Modal -->
    <div id="cleaning-modal" class="modal-overlay hidden">
        <div class="modal-content" style="max-width: 600px;">
            <button id="close-cleaning-modal-btn" class="modal-close"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="modal-title">Cleaning, Pest Control & Safety</h3>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/cleaning.jpg" alt="Cleaning"><p>Full Home Cleaning</p></a>
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/homecare.jpg" alt="Pest"><p>Pest Control</p></a>
            </div>
        </div>
    </div>

    <!-- Reno Modal -->
    <div id="reno-modal" class="modal-overlay hidden">
        <div class="modal-content" style="max-width: 600px;">
            <button id="close-reno-modal-btn" class="modal-close"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="modal-title">Home Renovation & Interior</h3>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/renovation.jpg" alt="Reno"><p>Full Home Renovation</p></a>
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/painter.jpg" alt="Paint"><p>Painting</p></a>
            </div>
        </div>
    </div>

    <!-- Beauty Modal -->
    <div id="beauty-modal" class="modal-overlay hidden">
        <div class="modal-content" style="max-width: 600px;">
            <button id="close-beauty-modal-btn" class="modal-close"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="modal-title">Women's Beauty & Spa</h3>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/beauty.jpg" alt="Beauty"><p>Salon for Women</p></a>
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/grooming.jpg" alt="Spa"><p>Spa for Women</p></a>
            </div>
        </div>
    </div>

    <!-- Grooming Modal -->
    <div id="grooming-modal" class="modal-overlay hidden">
        <div class="modal-content" style="max-width: 600px;">
            <button id="close-grooming-modal-btn" class="modal-close"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="modal-title">Men's Grooming & Massage</h3>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/grooming.jpg" alt="Men"><p>Salon for Men</p></a>
                <a href="#" class="modal-item" style="text-decoration: none;"><img src="images/beauty.jpg" alt="Massage"><p>Massage for Men</p></a>
            </div>
        </div>
    </div>
'''

idx_lines = idx_content.splitlines(True)
script_idx = -1
for i in range(len(idx_lines)):
    if '<script src="app.js?v=7"></script>' in idx_lines[i] or '<script src="common.js"></script>' in idx_lines[i]:
        script_idx = i
        break

if script_idx != -1:
    idx_lines.insert(script_idx, new_modals)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(idx_lines)
else:
    print("Failed to find script tag in index.html")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_lines = f.readlines()

new_js = '''
    const modalsToSetup = [
        {trigger: 'ac-modal-trigger', modal: 'ac-modal', close: 'close-ac-modal-btn'},
        {trigger: 'epc-modal-trigger', modal: 'epc-modal', close: 'close-epc-modal-btn'},
        {trigger: 'cleaning-modal-trigger', modal: 'cleaning-modal', close: 'close-cleaning-modal-btn'},
        {trigger: 'reno-modal-trigger', modal: 'reno-modal', close: 'close-reno-modal-btn'},
        {trigger: 'beauty-modal-trigger', modal: 'beauty-modal', close: 'close-beauty-modal-btn'},
        {trigger: 'grooming-modal-trigger', modal: 'grooming-modal', close: 'close-grooming-modal-btn'}
    ];

    modalsToSetup.forEach(m => {
        const trigger = document.getElementById(m.trigger);
        const modal = document.getElementById(m.modal);
        const closeBtn = document.getElementById(m.close);
        
        if (trigger && modal && closeBtn) {
            trigger.addEventListener('click', () => modal.classList.remove('hidden'));
            closeBtn.addEventListener('click', () => modal.classList.add('hidden'));
            modal.addEventListener('click', (e) => {
                if (e.target === modal) modal.classList.add('hidden');
            });
        }
    });
'''

for i in range(len(app_lines)-1, -1, -1):
    if '});' in app_lines[i]:
        app_lines.insert(i, new_js)
        with open('app.js', 'w', encoding='utf-8') as f:
            f.writelines(app_lines)
        break
        
print("Successfully generated all missing modals and JS")
