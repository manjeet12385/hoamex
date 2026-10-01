import os

with open('partner.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the category grid section to include data attributes and subcategory container
old_grid = """        <div class="category-grid">
            <div class="cat-box active" onclick="selectCat(this)">
                <i class="fa-solid fa-wrench"></i>
                <span>Plumbing</span>
            </div>
            <div class="cat-box" onclick="selectCat(this)">
                <i class="fa-solid fa-bolt"></i>
                <span>Electrical</span>
            </div>
            <div class="cat-box" onclick="selectCat(this)">
                <i class="fa-solid fa-broom"></i>
                <span>Cleaning</span>
            </div>
            <div class="cat-box" onclick="selectCat(this)">
                <i class="fa-solid fa-hammer"></i>
                <span>Carpentry</span>
            </div>
            <div class="cat-box" onclick="selectCat(this)">
                <i class="fa-solid fa-paint-roller"></i>
                <span>Painting</span>
            </div>
            <div class="cat-box" onclick="selectCat(this)">
                <i class="fa-solid fa-fan"></i>
                <span>HVAC</span>
            </div>
            <div class="cat-box" onclick="selectCat(this)">
                <i class="fa-solid fa-leaf"></i>
                <span>Gardening</span>
            </div>
            <div class="cat-box" onclick="selectCat(this)">
                <i class="fa-solid fa-ellipsis"></i>
                <span>Other</span>
            </div>
        </div>"""

new_grid = """        <div class="category-grid" style="margin-bottom: 20px;">
            <div class="cat-box active" onclick="selectCat(this, 'plumbing')">
                <i class="fa-solid fa-wrench"></i>
                <span>Plumbing</span>
            </div>
            <div class="cat-box" onclick="selectCat(this, 'electrical')">
                <i class="fa-solid fa-bolt"></i>
                <span>Electrical</span>
            </div>
            <div class="cat-box" onclick="selectCat(this, 'cleaning')">
                <i class="fa-solid fa-broom"></i>
                <span>Cleaning</span>
            </div>
            <div class="cat-box" onclick="selectCat(this, 'carpentry')">
                <i class="fa-solid fa-hammer"></i>
                <span>Carpentry</span>
            </div>
            <div class="cat-box" onclick="selectCat(this, 'painting')">
                <i class="fa-solid fa-paint-roller"></i>
                <span>Painting</span>
            </div>
            <div class="cat-box" onclick="selectCat(this, 'hvac')">
                <i class="fa-solid fa-fan"></i>
                <span>HVAC</span>
            </div>
            <div class="cat-box" onclick="selectCat(this, 'gardening')">
                <i class="fa-solid fa-leaf"></i>
                <span>Gardening</span>
            </div>
            <div class="cat-box" onclick="selectCat(this, 'other')">
                <i class="fa-solid fa-ellipsis"></i>
                <span>Other</span>
            </div>
        </div>
        
        <!-- Subcategories Container -->
        <div id="subcategory-section" style="margin-bottom: 40px; padding: 20px; background: rgba(74,58,255,0.03); border: 1px solid rgba(74,58,255,0.1); border-radius: 12px;">
            <div class="section-title" style="font-size: 14px; margin-bottom: 5px;">Specific Skills (Optional)</div>
            <div class="section-desc" style="margin-bottom: 15px; font-size: 12px; color: #777;">Select the specific services you want to provide.</div>
            <div id="subcat-chips" style="display: flex; flex-wrap: wrap; gap: 10px;">
                <!-- Chips will be injected here via JS -->
            </div>
        </div>"""

if old_grid in content:
    content = content.replace(old_grid, new_grid)

# Add CSS for chips
old_css = """        /* Next Button */"""
new_css = """        /* Chips */
        .chip {
            padding: 8px 16px;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
            color: #555;
            cursor: pointer;
            transition: 0.2s;
            user-select: none;
            display: inline-flex;
            align-items: center;
        }
        .chip:hover {
            background: #f5f5f5;
        }
        .chip.selected {
            background: #4a3aff;
            color: #fff;
            border-color: #4a3aff;
            box-shadow: 0 4px 10px rgba(74,58,255,0.2);
        }
        .chip.selected i {
            margin-right: 6px;
        }
        
        /* Next Button */"""

if old_css in content:
    content = content.replace(old_css, new_css)

# Update JS logic
old_js = """    <script>
        function selectCat(element) {
            document.querySelectorAll('.cat-box').forEach(box => box.classList.remove('active'));
            element.classList.add('active');
        }
    </script>"""

new_js = """    <script>
        const subcategories = {
            'plumbing': ['Leak Repair', 'Water Tank Cleaning', 'Pipe Installation', 'Tap/Faucet Repair', 'Bathroom Fittings', 'Drain Cleaning'],
            'electrical': ['Fan Repair & Installation', 'Switchboard Repair', 'House Wiring', 'Inverter Setup', 'Lighting Installation', 'MCB/Fuse Fix'],
            'cleaning': ['Full Home Cleaning', 'Bathroom Cleaning', 'Kitchen Cleaning', 'Sofa/Carpet Cleaning', 'Water Tank Cleaning'],
            'carpentry': ['Furniture Assembly', 'IKEA Assembly', 'Wood Polish', 'Door/Window Repair', 'Custom Furniture'],
            'painting': ['Interior Painting', 'Exterior Painting', 'Wall Panels', 'Texture Painting', 'Waterproofing'],
            'hvac': ['AC Service', 'AC Repair', 'AC Installation', 'Refrigerator Repair', 'Washing Machine', 'Microwave Repair', 'Geyser Service', 'RO Purifier'],
            'gardening': ['Lawn Mowing', 'Plant Pruning', 'Fertilization', 'Pest Control for Plants', 'Landscaping'],
            'other': ['Pest Control', 'Packers & Movers', 'Mini Truck', 'Security/CCTV', 'Smart Locks', 'Welding/Fabrication', 'Solar Services']
        };

        function selectCat(element, categoryId) {
            // Highlight active category box
            document.querySelectorAll('.cat-box').forEach(box => box.classList.remove('active'));
            element.classList.add('active');
            
            // Render subcategory chips
            renderSubcategories(categoryId);
        }

        function renderSubcategories(categoryId) {
            const container = document.getElementById('subcat-chips');
            container.innerHTML = ''; // clear previous
            
            const skills = subcategories[categoryId] || [];
            if (skills.length === 0) {
                document.getElementById('subcategory-section').style.display = 'none';
                return;
            }
            
            document.getElementById('subcategory-section').style.display = 'block';
            
            skills.forEach(skill => {
                const chip = document.createElement('div');
                chip.className = 'chip';
                chip.innerHTML = skill;
                chip.onclick = function() {
                    this.classList.toggle('selected');
                    if(this.classList.contains('selected')) {
                        this.innerHTML = '<i class="fa-solid fa-check"></i> ' + skill;
                    } else {
                        this.innerHTML = skill;
                    }
                };
                container.appendChild(chip);
            });
        }

        // Initialize with default selected category
        document.addEventListener('DOMContentLoaded', () => {
            renderSubcategories('plumbing');
        });
    </script>"""

if old_js in content:
    content = content.replace(old_js, new_js)

with open('partner.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated partner.html with subcategories")
