import sys

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_lines = f.readlines()

logistics_modal_html = '''
    <!-- Logistics Modal -->
    <div id="logistics-modal" class="modal-overlay hidden">
        <div class="modal-content" style="max-width: 600px;">
            <button id="close-logistics-modal-btn" class="modal-close"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="modal-title">Home Care, Support & Logistics</h3>

            <h4 class="modal-subtitle">Logistics & Moving</h4>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/tools.jpg" alt="Packers & Movers">
                    <p>Packers & Movers</p>
                </a>
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/homecare.jpg" alt="Mini Truck">
                    <p>Mini Truck on Rent</p>
                </a>
            </div>

            <h4 class="modal-subtitle">Daily Home Support</h4>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px; margin-bottom: 25px;">
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/carpenter.jpg" alt="Driver">
                    <p>Driver on Demand</p>
                </a>
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/cleaning.jpg" alt="Maid">
                    <p>Maid / Helper</p>
                </a>
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/kitchen.jpg" alt="Cook">
                    <p>Cook on Demand</p>
                </a>
            </div>

            <h4 class="modal-subtitle">Specialized Care</h4>
            <div class="modal-grid" style="justify-content: flex-start; gap: 20px;">
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/beauty.jpg" alt="Elder Care">
                    <p>Elder / Patient Care</p>
                </a>
                <a href="#" class="modal-item" style="text-decoration: none;">
                    <img src="images/grooming.jpg" alt="Babysitting">
                    <p>Babysitting / Nanny</p>
                </a>
            </div>
        </div>
    </div>
'''

for i in range(len(idx_lines)):
    if '<div class="service-item">' in idx_lines[i] and 'Home Care, Support & Logistics' in idx_lines[i+2]:
        idx_lines[i] = '                <div id="logistics-modal-trigger" class="service-item" style="cursor: pointer;">\n'
        break

# find script tag to insert before
script_idx = -1
for i in range(len(idx_lines)):
    if '<script src="app.js?v=7"></script>' in idx_lines[i]:
        script_idx = i
        break

if script_idx != -1:
    idx_lines.insert(script_idx, logistics_modal_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(idx_lines)
    print("Updated index.html")
else:
    print("Failed to find script tag in index.html")


# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_lines = f.readlines()

logistics_js = '''
    // Logistics Modal Logic
    const logisticsTrigger = document.getElementById('logistics-modal-trigger');
    const logisticsModal = document.getElementById('logistics-modal');
    const closeLogisticsBtn = document.getElementById('close-logistics-modal-btn');

    if (logisticsTrigger && logisticsModal && closeLogisticsBtn) {
        logisticsTrigger.addEventListener('click', () => {
            logisticsModal.classList.remove('hidden');
        });

        closeLogisticsBtn.addEventListener('click', () => {
            logisticsModal.classList.add('hidden');
        });

        logisticsModal.addEventListener('click', (e) => {
            if (e.target === logisticsModal) {
                logisticsModal.classList.add('hidden');
            }
        });
    }
'''

# insert right before the last });
for i in range(len(app_lines)-1, -1, -1):
    if '});' in app_lines[i]:
        app_lines.insert(i, logistics_js)
        with open('app.js', 'w', encoding='utf-8') as f:
            f.writelines(app_lines)
        print("Updated app.js")
        break
