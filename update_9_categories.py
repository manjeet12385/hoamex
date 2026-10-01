import os
import re

with open('partner.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Generate new category HTML with 9 categories
categories = [
    {"id": "appliances", "icon": "fa-snowflake", "label": "AC, Appliance & Repair"},
    {"id": "epc", "icon": "fa-tools", "label": "Electrician, Plumber & Carpenter"},
    {"id": "cleaning_pest", "icon": "fa-broom", "label": "Cleaning, Pest Control & Safety"},
    {"id": "renovation", "icon": "fa-house-chimney", "label": "Home Renovation & Interior"},
    {"id": "fabrication", "icon": "fa-hammer", "label": "Fabrication, Grills & Roofing"},
    {"id": "women_spa", "icon": "fa-spa", "label": "Women's Beauty & Spa"},
    {"id": "men_spa", "icon": "fa-user-tie", "label": "Men's Grooming & Massage"},
    {"id": "home_care", "icon": "fa-hand-holding-heart", "label": "Home Care, Support & Logistics"},
    {"id": "security_solar", "icon": "fa-shield-halved", "label": "Home Security, Solar & Water"}
]

# Note: Using grid-template-columns: repeat(3, 1fr) for 9 items (3x3 grid)
new_grid_html = '<div class="category-grid" style="grid-template-columns: repeat(3, 1fr); margin-bottom: 20px;">\n'
for i, cat in enumerate(categories):
    active = ' active' if i == 0 else ''
    new_grid_html += f"""            <div class="cat-box{active}" onclick="selectCat(this, '{cat['id']}')">
                <i class="fa-solid {cat['icon']}"></i>
                <span style="font-size:12px; text-align:center;">{cat['label']}</span>
            </div>\n"""
new_grid_html += '        </div>'

content = re.sub(r'<div class="category-grid".*?</div>\s*<!-- Subcategories Container -->', new_grid_html + '\n        \n        <!-- Subcategories Container -->', content, flags=re.DOTALL)

# Generate new JS logic
new_js_logic = """    <script>
        const subcategories = {
            'appliances': ['AC Service', 'AC Repair', 'Refrigerator', 'Washing Machine', 'Microwave', 'RO / Water Purifier', 'Geyser Service', 'Television', 'Chimney'],
            'epc': ['Fan Repair', 'Switchboard Repair', 'Wiring', 'Leak Repair', 'Water Tank Cleaning', 'Pipe Fitting', 'Bathroom Fittings', 'Furniture Assembly', 'IKEA Assembly', 'Wood Polish'],
            'cleaning_pest': ['Full Home Cleaning', 'Bathroom Cleaning', 'Kitchen Cleaning', 'Sofa/Carpet Cleaning', 'Cockroach Control', 'Ants Control', 'Termite Control', 'General Pest Control'],
            'renovation': ['Interior Painting', 'Exterior Painting', 'Wall Panels', 'Texture Painting', 'Waterproofing', 'Tile Grouting'],
            'fabrication': ['Gates & Doors', 'Grills & Railings', 'Welding Repair', 'Sheds & Roofing'],
            'women_spa': ['Salon for Women', 'Spa for Women', 'Hair Studio', 'Makeup', 'Massage Royale'],
            'men_spa': ['Salon for Men', 'Spa for Men', 'Massage Men', 'Men\\'s Grooming'],
            'home_care': ['Maid Helper', 'Cook on Demand', 'Babysitting', 'Elder Care', 'Packers & Movers', 'Mini Truck / Logistics', 'Driver on Demand'],
            'security_solar': ['CCTV Services', 'Smart Locks', 'Home Alarm', 'Solar Installation', 'Solar Cleaning', 'Solar Water Heater', 'Water Solutions']
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
            renderSubcategories('appliances');
        });
    </script>"""

content = re.sub(r'<script>\s*const subcategories =.*?</script>', new_js_logic, content, flags=re.DOTALL)

with open('partner.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated partner.html with 9 combined categories")
