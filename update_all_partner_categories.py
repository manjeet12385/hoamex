import os
import re

with open('partner.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Generate new category HTML
categories = [
    {"id": "ac_appliance", "icon": "fa-snowflake", "label": "Appliances"},
    {"id": "plumber", "icon": "fa-wrench", "label": "Plumbing"},
    {"id": "electrician", "icon": "fa-bolt", "label": "Electrical"},
    {"id": "carpenter", "icon": "fa-hammer", "label": "Carpentry"},
    {"id": "cleaning", "icon": "fa-broom", "label": "Cleaning"},
    {"id": "pest_control", "icon": "fa-bug", "label": "Pest Control"},
    {"id": "beauty_women", "icon": "fa-spa", "label": "Salon (Women)"},
    {"id": "beauty_men", "icon": "fa-user-tie", "label": "Salon (Men)"},
    {"id": "painting", "icon": "fa-paint-roller", "label": "Painting"},
    {"id": "packers", "icon": "fa-truck-fast", "label": "Packers & Movers"},
    {"id": "security", "icon": "fa-shield-halved", "label": "Security"},
    {"id": "solar_water", "icon": "fa-solar-panel", "label": "Solar & Water"},
    {"id": "helpers", "icon": "fa-hand-holding-heart", "label": "Helpers & Care"},
    {"id": "fabrication", "icon": "fa-helmet-safety", "label": "Fabrication"}
]

new_grid_html = '<div class="category-grid" style="margin-bottom: 20px;">\n'
for i, cat in enumerate(categories):
    active = ' active' if i == 0 else ''
    new_grid_html += f"""            <div class="cat-box{active}" onclick="selectCat(this, '{cat['id']}')">
                <i class="fa-solid {cat['icon']}"></i>
                <span style="font-size:12px; text-align:center;">{cat['label']}</span>
            </div>\n"""
new_grid_html += '        </div>'

# Regex to replace the old category grid
content = re.sub(r'<div class="category-grid".*?</div>\s*<!-- Subcategories Container -->', new_grid_html + '\n        \n        <!-- Subcategories Container -->', content, flags=re.DOTALL)

# Generate new JS logic
new_js_logic = """    <script>
        const subcategories = {
            'ac_appliance': ['AC Service', 'AC Repair', 'Refrigerator', 'Washing Machine', 'Microwave', 'RO / Water Purifier', 'Geyser Service', 'Television', 'Chimney'],
            'plumber': ['Leak/Gap Repair', 'Water Tank Cleaning', 'Pipe Fitting', 'Bathroom Fittings', 'Drain Cleaning'],
            'electrician': ['Fan Installation', 'Switchboard Repair', 'Wiring', 'Inverter Setup', 'Lighting'],
            'carpenter': ['Furniture Assembly', 'IKEA Assembly', 'Wood Polish', 'Door/Window Repair'],
            'cleaning': ['Full Home Cleaning', 'Bathroom Cleaning', 'Kitchen Cleaning', 'Sofa/Carpet Cleaning'],
            'pest_control': ['Cockroach Control', 'Ants Control', 'Termite Control', 'General Pest Control'],
            'beauty_women': ['Salon for Women', 'Spa for Women', 'Hair Studio', 'Makeup', 'Massage Royale'],
            'beauty_men': ['Salon for Men', 'Spa for Men', 'Massage Men', 'Men\\'s Grooming'],
            'painting': ['Interior Painting', 'Exterior Painting', 'Wall Panels', 'Texture Painting', 'Waterproofing'],
            'packers': ['Packers & Movers', 'Mini Truck / Logistics', 'Driver on Demand'],
            'security': ['CCTV Services', 'Smart Locks', 'Home Alarm'],
            'solar_water': ['Solar Installation', 'Solar Cleaning', 'Solar Water Heater', 'Water Solutions'],
            'helpers': ['Maid Helper', 'Cook on Demand', 'Babysitting', 'Elder Care'],
            'fabrication': ['Gates & Doors', 'Grills & Railings', 'Welding Repair', 'Sheds & Roofing']
        };

        function selectCat(element, categoryId) {
            document.querySelectorAll('.cat-box').forEach(box => box.classList.remove('active'));
            element.classList.add('active');
            renderSubcategories(categoryId);
        }

        function renderSubcategories(categoryId) {
            const container = document.getElementById('subcat-chips');
            container.innerHTML = ''; 
            
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

        document.addEventListener('DOMContentLoaded', () => {
            renderSubcategories('ac_appliance');
        });
    </script>"""

content = re.sub(r'<script>\s*const subcategories =.*?</script>', new_js_logic, content, flags=re.DOTALL)

with open('partner.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated partner.html with all categories")
