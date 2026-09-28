import re

def extract_services():
    with open(r'c:\Users\Divyanshi123456\Music\hoamex\index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all modal-items that are links
    # Format: <a class="modal-item" href="ac-service.html"...> ... <p>AC Repair</p> ... </a>
    matches = re.finditer(r'<a[^>]*class="modal-item"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html, re.DOTALL)
    
    services = {}
    
    for match in matches:
        href = match.group(1)
        if href == "#" or "javascript" in href:
            continue
            
        content = match.group(2)
        # extract text inside <p> or just the text
        p_match = re.search(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
        if p_match:
            name = p_match.group(1).strip()
        else:
            # remove tags
            name = re.sub(r'<[^>]+>', '', content).strip()
            
        if name and not name.startswith("See all"):
            services[name] = href

    # Some hardcoded most popular services just in case they aren't in modals
    additional = {
        'AC Repair': 'ac-repair.html',
        'AC Service': 'ac-service.html',
        'Plumber': 'plumber.html',
        'Electrician': 'electrician.html',
        'Carpenter': 'carpenter.html',
        'Home Renovation': 'full-home-renovation.html',
        'Painting': 'painting.html',
        'Massage for Men': 'massage-men.html',
        'Salon for Men': 'salon-men.html',
        'Salon for Women': 'salon-women.html',
        'Washing Machine Repair': 'washing-machine.html',
        'Refrigerator Repair': 'refrigerator.html',
        'Water Purifier (RO)': 'water-purifier.html',
        'Packers & Movers': 'packers-movers.html',
        'Driver on Demand': 'driver-on-demand.html',
        'Maid & Helper': 'maid-helper.html',
        'Cook on Demand': 'cook-on-demand.html',
        'Nanny / Babysitting': 'babysitting.html',
        'Elder Care': 'elder-care.html',
        'Bathroom Cleaning': 'bathroom-cleaning.html',
        'Full Home Cleaning': 'full-home-cleaning.html',
        'Kitchen Cleaning': 'kitchen-cleaning.html',
        'Pest Control': 'pest-control.html',
        'CCTV Installation': 'cctv-services.html',
        'Smart Locks': 'smart-locks.html',
        'Solar Cleaning': 'solar-cleaning.html'
    }
    
    services.update(additional)
    
    # Format the JS array
    js_array = "const servicesList = [\n"
    for name, link in services.items():
        # Escape quotes in name
        safe_name = name.replace("'", "\\'")
        js_array += f"            {{ name: '{safe_name}', link: '{link}' }},\n"
    js_array += "        ];"
    
    # Read common.js
    with open(r'c:\Users\Divyanshi123456\Music\hoamex\common.js', 'r', encoding='utf-8') as f:
        common_js = f.read()
        
    # Replace the old list
    old_list_pattern = r'const servicesList = \[\s*\{.*?\}\s*\];'
    common_js_new = re.sub(old_list_pattern, js_array, common_js, flags=re.DOTALL)
    
    if common_js != common_js_new:
        with open(r'c:\Users\Divyanshi123456\Music\hoamex\common.js', 'w', encoding='utf-8') as f:
            f.write(common_js_new)
        print("Updated servicesList in common.js")
    else:
        print("Could not find/update the list in common.js")

extract_services()
