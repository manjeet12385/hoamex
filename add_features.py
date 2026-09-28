import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\common.js', 'r', encoding='utf-8') as f:
    content = f.read()

new_features = """
// Advanced Features for Location and Search
if (!window.hoamexFeaturesLoaded) {
    window.hoamexFeaturesLoaded = true;
    document.addEventListener('DOMContentLoaded', () => {
        
        // --- 1. Location Button Feature ---
        const locBtns = document.querySelectorAll('.location-btn');
        locBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const originalText = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Locating...';
                
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(position => {
                        const lat = position.coords.latitude;
                        const lon = position.coords.longitude;
                        // Use Nominatim reverse geocoding API
                        fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`)
                            .then(res => res.json())
                            .then(data => {
                                let locationStr = "Location Found";
                                if (data && data.address) {
                                    locationStr = data.address.city || data.address.town || data.address.state_district || data.address.state || "Location Found";
                                }
                                btn.innerHTML = `<i class="fa-solid fa-location-dot"></i> ${locationStr}`;
                            })
                            .catch(() => {
                                btn.innerHTML = '<i class="fa-solid fa-location-dot"></i> New Delhi'; // Fallback
                            });
                    }, error => {
                        btn.innerHTML = '<i class="fa-solid fa-location-dot"></i> Location Denied';
                        setTimeout(() => {
                            btn.innerHTML = originalText;
                        }, 3000);
                    });
                } else {
                    btn.innerHTML = '<i class="fa-solid fa-location-dot"></i> Not Supported';
                }
            });
        });

        // --- 2. Live Search Feature ---
        const servicesList = [
            { name: 'AC Repair', link: 'ac-repair.html' },
            { name: 'AC Service', link: 'ac-service.html' },
            { name: 'Plumber', link: 'plumber.html' },
            { name: 'Electrician', link: 'electrician.html' },
            { name: 'Carpenter', link: 'carpenter.html' },
            { name: 'Cleaning & Pest Control', link: 'cleaning.html' },
            { name: 'Home Renovation', link: 'full-home-renovation.html' },
            { name: 'Painting', link: 'painting.html' },
            { name: 'Massage for Men', link: 'massage-men.html' },
            { name: 'Salon for Men', link: 'salon-men.html' },
            { name: 'Salon for Women', link: 'salon-women.html' },
            { name: 'Washing Machine Repair', link: 'washing-machine.html' },
            { name: 'Refrigerator Repair', link: 'refrigerator.html' },
            { name: 'Water Purifier (RO)', link: 'water-purifier.html' },
            { name: 'Packers & Movers', link: 'packers-movers.html' },
            { name: 'Driver on Demand', link: 'driver-on-demand.html' },
            { name: 'Maid & Helper', link: 'maid-helper.html' },
            { name: 'Cook on Demand', link: 'cook-on-demand.html' },
            { name: 'Nanny / Babysitting', link: 'babysitting.html' },
            { name: 'Elder Care', link: 'elder-care.html' }
        ];

        const searchInputs = document.querySelectorAll('.search-container input');
        searchInputs.forEach(input => {
            const container = input.closest('.search-container');
            if (!container) return;
            
            container.style.position = 'relative';

            const dropdown = document.createElement('div');
            dropdown.className = 'search-dropdown';
            dropdown.style.cssText = 'position: absolute; top: 100%; left: 0; right: 0; background: #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-radius: 8px; z-index: 1000; max-height: 300px; overflow-y: auto; display: none; margin-top: 5px; border: 1px solid #eee; text-align: left;';
            container.appendChild(dropdown);

            input.addEventListener('input', (e) => {
                const val = e.target.value.toLowerCase().trim();
                if (val.length === 0) {
                    dropdown.style.display = 'none';
                    return;
                }

                const matches = servicesList.filter(s => s.name.toLowerCase().includes(val));
                
                if (matches.length > 0) {
                    dropdown.innerHTML = matches.map(m => `
                        <a href="${m.link}" style="display: block; padding: 12px 15px; color: #333; text-decoration: none; border-bottom: 1px solid #f5f5f5; font-size: 14px; transition: background 0.2s;" onmouseover="this.style.background='#f9f9f9'" onmouseout="this.style.background='transparent'">
                            <i class="fa-solid fa-magnifying-glass" style="color: #999; margin-right: 8px;"></i> ${m.name}
                        </a>
                    `).join('');
                    dropdown.style.display = 'block';
                } else {
                    dropdown.innerHTML = '<div style="padding: 12px 15px; color: #999; font-size: 14px; text-align: center;">No services found</div>';
                    dropdown.style.display = 'block';
                }
            });

            // Hide dropdown when clicking outside
            document.addEventListener('click', (e) => {
                if (!container.contains(e.target)) {
                    dropdown.style.display = 'none';
                }
            });
            
            // Show dropdown again if focused and has value
            input.addEventListener('focus', (e) => {
                if (e.target.value.trim().length > 0) {
                    dropdown.style.display = 'block';
                }
            });
        });
    });
}
"""

if "window.hoamexFeaturesLoaded" not in content:
    content += "\n" + new_features
    with open(r'c:\Users\Divyanshi123456\Music\hoamex\common.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Features added to common.js")
else:
    print("Features already exist in common.js")
