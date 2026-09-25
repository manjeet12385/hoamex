import os, glob, re

modal_template = """
    <!-- Modal for {title} -->
    <div id="{modal_id}" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf6; width: 100%; max-width: 500px; padding: 20px; border-radius: 12px; position: relative; max-height: 90vh; overflow-y: auto;">
            <button onclick="document.getElementById('{modal_id}').classList.add('hidden')" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>
            <h3 class="options-modal-title" style="font-size: 24px; margin-bottom: 25px; font-weight: 700; color: #111;">{title}</h3>
            <div style="position: relative; margin: 0 -5px;">
                <button onclick="document.getElementById('{carousel_id}').scrollBy({{left: -175, behavior: 'smooth'}})" style="position: absolute; left: -10px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-left" style="font-size: 14px;"></i></button>
                <button onclick="document.getElementById('{carousel_id}').scrollBy({{left: 175, behavior: 'smooth'}})" style="position: absolute; right: -10px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-right" style="font-size: 14px;"></i></button>
                <div id="{carousel_id}" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; padding-left: 5px; padding-right: 5px; scrollbar-width: none; scroll-behavior: smooth;">
{options_html}
                </div>
            </div>
        </div>
    </div>
"""

option_template = """
                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="{img_src}" onerror="this.src='images/plumber.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">{opt_name}</h4>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹{opt_price}</div>
                    <button class="option-add-btn" onclick="addToCart('{cart_name}',{opt_price})" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>"""

def generate_slug(title):
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')
    return slug

for file in glob.glob('*.html'):
    if 'fixed' in file: continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modals_to_append = []
    
    parts = content.split('<div class="svc-row">')
    new_parts = [parts[0]]
    modified = False
    
    for i in range(1, len(parts)):
        row = parts[i]
        
        if 'onclick="addToCart' in row and 'class="options-text"' in row:
            m_title = re.search(r'<h[34]>(.*?)</h[34]>', row)
            m_btn = re.search(r'<button class="add-btn".*?onclick="addToCart\(\'(.*?)\'\s*,\s*(\d+)\)".*?>Add</button>', row)
            m_opt = re.search(r'<(p|div) class="options-text">(?:\((.*?)\)|(.*?))</(p|div)>', row)
            m_img = re.search(r'<img class="svc-img" src="(.*?)"', row)
            
            if m_title and m_btn and m_opt:
                title = m_title.group(1).strip()
                base_price = int(m_btn.group(2))
                
                opt_str = m_opt.group(2) or m_opt.group(3)
                opt_num_m = re.search(r'(\d+)', opt_str)
                num_options = int(opt_num_m.group(1)) if opt_num_m else 2
                
                img_src = m_img.group(1) if m_img else "images/plumber.jpg"
                
                slug = generate_slug(title)
                modal_id = f"modal-{slug}"
                carousel_id = f"carousel-{slug}"
                
                new_btn = f'<button onclick="document.getElementById(\'{modal_id}\').classList.remove(\'hidden\')" class="add-btn">Add</button>'
                row = row.replace(m_btn.group(0), new_btn)
                modified = True
                
                options_html = ""
                for j in range(num_options):
                    opt_name = f"Option {j+1}"
                    opt_price = base_price + (j * 100)
                    cart_name = f"{title} - {opt_name}"
                    options_html += option_template.format(
                        img_src=img_src, opt_name=opt_name, opt_price=opt_price, cart_name=cart_name
                    )
                
                modal_html = modal_template.format(
                    title=title, modal_id=modal_id, carousel_id=carousel_id, options_html=options_html
                )
                modals_to_append.append(modal_html)
                
        new_parts.append(row)
        
    if modified:
        new_content = '<div class="svc-row">'.join(new_parts)
        
        if '.wm-options-carousel::-webkit-scrollbar' not in new_content:
            style_str = "\n<style>\n.hidden { display: none !important; }\n.wm-options-carousel::-webkit-scrollbar { display: none; }\n</style>\n"
            if '</body>' in new_content:
                new_content = new_content.replace('</body>', style_str + '</body>')
            else:
                new_content += style_str
        
        modals_str = "\n".join(modals_to_append)
        if '</body>' in new_content:
            new_content = new_content.replace('</body>', modals_str + '\n</body>')
        else:
            new_content += modals_str
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated {file} with {len(modals_to_append)} modals.")
