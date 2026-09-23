import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add id to trigger
old_trigger = '<div class="service-item">\n                    <div class="service-icon"><img src="images/security.jpg" alt="Security"></div>\n                    <p>Home Security, Solar & Water</p>\n                </div>'
new_trigger = '<div id="security-modal-trigger" class="service-item" style="cursor: pointer;">\n                    <div class="service-icon"><img src="images/security.jpg" alt="Security"></div>\n                    <p>Home Security, Solar & Water</p>\n                </div>'

content = content.replace(old_trigger, new_trigger)

# 2. Add Modal HTML before closing script tag
modal_html = '''
    <!-- Home Security Modal -->
    <div id="security-modal" class="modal-overlay hidden">
        <div class="modal-content" style="max-width: 600px;">
            <button id="close-security-modal-btn" class="modal-close"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="modal-title">Home Security, Solar & Water</h3>

            <h4 class="modal-subtitle">Home Security</h4>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/security.jpg" alt="CCTV Camera">
                    <p>CCTV Camera Installation</p>
                </a>
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/homecare.jpg" alt="Smart Locks">
                    <p>Smart Locks & Doorbells</p>
                </a>
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/security.jpg" alt="Home Alarm">
                    <p>Home Alarm Systems</p>
                </a>
            </div>

            <h4 class="modal-subtitle">Solar Services</h4>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/ac.jpg" alt="Solar Panel">
                    <p>Solar Panel Installation</p>
                </a>
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/cleaning.jpg" alt="Solar Panel Cleaning">
                    <p>Solar Panel Cleaning</p>
                </a>
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/plumber.jpg" alt="Solar Water Heater">
                    <p>Solar Water Heater</p>
                </a>
            </div>

            <h4 class="modal-subtitle">Water Solutions</h4>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px;">
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/plumber.jpg" alt="RO Service">
                    <p>RO / Water Purifier</p>
                </a>
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/cleaning.jpg" alt="Water Tank Cleaning">
                    <p>Water Tank Cleaning</p>
                </a>
            </div>
        </div>
    </div>
'''

content = content.replace('    <script>', modal_html + '    <script>')

# 3. Add JS logic
js_logic = '''
            // Home Security Modal
            const securityTrigger = document.getElementById('security-modal-trigger');
            const securityModal = document.getElementById('security-modal');
            const closeSecurityBtn = document.getElementById('close-security-modal-btn');
            
            if (securityTrigger) securityTrigger.addEventListener('click', () => securityModal.classList.remove('hidden'));
            if (closeSecurityBtn) closeSecurityBtn.addEventListener('click', () => securityModal.classList.add('hidden'));
            
            if (securityModal) {
                securityModal.addEventListener('click', (e) => {
                    if(e.target === securityModal) securityModal.classList.add('hidden');
                });
            }
'''

content = content.replace('// Electrician Modal', js_logic + '\n            // Electrician Modal')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Security Modal added successfully")
