import re
import glob

# 1. ADD CSS
with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

location_css = """
/* Location Modal Styles */
#location-modal {
    display: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.5);
    z-index: 10000;
    align-items: center;
    justify-content: center;
}
.location-modal-box {
    background: #fdfaf6;
    width: 500px;
    max-width: 90%;
    border-radius: 16px;
    padding: 24px;
    position: relative;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}
.loc-modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
.loc-modal-header h2 {
    font-size: 18px;
    display: flex;
    align-items: center;
    gap: 10px;
    color: #1a1c23;
}
.loc-modal-header h2 i {
    color: #4f46e5;
    font-size: 20px;
}
.loc-close-btn {
    background: #f1ede8;
    border: none;
    width: 32px; height: 32px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 16px;
    color: #666;
}
.loc-gps-box {
    display: flex;
    align-items: center;
    gap: 15px;
    background: #f0f0f9;
    padding: 12px 16px;
    border-radius: 12px;
    cursor: pointer;
    border: 1px solid #e5e5f1;
    transition: all 0.2s;
}
.loc-gps-box:hover {
    background: #e6e6f5;
}
.loc-gps-icon {
    width: 44px; height: 44px;
    background: #4f46e5;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    font-size: 18px;
}
.loc-gps-text {
    flex: 1;
}
.loc-gps-text h4 {
    color: #3b32a8;
    margin: 0 0 4px 0;
    font-size: 15px;
}
.loc-gps-text p {
    color: #6c63ff;
    margin: 0;
    font-size: 12px;
}
.loc-divider {
    text-align: center;
    margin: 24px 0;
    position: relative;
}
.loc-divider::before {
    content: '';
    position: absolute;
    left: 0; top: 50%;
    width: 100%; height: 1px;
    background: #e5e7eb;
    z-index: 1;
}
.loc-divider span {
    background: #fdfaf6;
    padding: 0 10px;
    color: #9ca3af;
    font-size: 12px;
    font-weight: 600;
    position: relative;
    z-index: 2;
    letter-spacing: 0.5px;
}
.loc-input-box {
    display: flex;
    align-items: center;
    gap: 10px;
    background: white;
    border: 1px solid #e5e7eb;
    padding: 12px 16px;
    border-radius: 12px;
}
.loc-input-box i {
    color: #9ca3af;
    font-size: 16px;
}
.loc-input-box input {
    border: none;
    outline: none;
    flex: 1;
    font-size: 14px;
    background: transparent;
}
"""

if "Location Modal Styles" not in css:
    css += "\n" + location_css
    with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
        f.write(css)

# 2. HTML INJECTION
html_modal = """
    <!-- Location Modal -->
    <div id="location-modal">
        <div class="location-modal-box">
            <div class="loc-modal-header">
                <h2><i class="fa-solid fa-location-dot"></i> Select Your Location</h2>
                <button class="loc-close-btn" onclick="document.getElementById('location-modal').style.display='none'"><i class="fa-solid fa-xmark"></i></button>
            </div>
            
            <div class="loc-gps-box" onclick="triggerGpsLocation()">
                <div class="loc-gps-icon">
                    <i class="fa-solid fa-location-arrow"></i>
                </div>
                <div class="loc-gps-text">
                    <h4>Use Current Location</h4>
                    <p>Using GPS for accurate address</p>
                </div>
            </div>
            
            <div class="loc-divider">
                <span>OR ENTER MANUALLY</span>
            </div>
            
            <div class="loc-input-box">
                <i class="fa-solid fa-magnifying-glass"></i>
                <input type="text" id="manual-loc-input" placeholder="Type area, street, city or 6-digit pincode" onkeypress="if(event.key === 'Enter') setManualLocation()">
            </div>
        </div>
    </div>
"""

html_files = glob.glob(r'c:\Users\Divyanshi123456\Music\hoamex\*.html')
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Bust common cache
        new_html = re.sub(r'common\.js(?:\?v=\d+)?', 'common.js?v=3001', html)
        
        if 'id="location-modal"' not in new_html:
            new_html = new_html.replace('</body>', html_modal + '\n</body>')
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)
    except:
        pass

# 3. UPDATE common.js LOGIC
with open(r'c:\Users\Divyanshi123456\Music\hoamex\common.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make locationBtn open the modal instead of triggering GPS
js = js.replace("locationBtn.addEventListener('click', () => {", "locationBtn.addEventListener('click', () => {\ndocument.getElementById('location-modal').style.display = 'flex';\n});\n/*")
js = js.replace("locationBtn.innerHTML = `<i class=\"fa-solid fa-location-dot\"></i> ${city}`;", "locationBtn.innerHTML = `<i class=\"fa-solid fa-location-dot\"></i> ${city}`;\ndocument.getElementById('location-modal').style.display = 'none';")

# Add the global functions for the modal
new_js = """
// Global Location Modal Functions
window.triggerGpsLocation = function() {
    const locationBtn = document.querySelector('.use-location-btn');
    if (!locationBtn) return;
    
    locationBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Locating...';
    
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`)
                    .then(response => response.json())
                    .then(data => {
                        const city = data.address.city || data.address.town || data.address.state_district || 'Unknown Location';
                        locationBtn.innerHTML = `<i class="fa-solid fa-location-dot"></i> ${city}`;
                        document.getElementById('location-modal').style.display = 'none';
                        localStorage.setItem('user_location', city);
                    })
                    .catch(() => {
                        locationBtn.innerHTML = '<i class="fa-solid fa-location-dot"></i> Use Current Location';
                        alert('Could not determine city from coordinates.');
                    });
            },
            (error) => {
                locationBtn.innerHTML = '<i class="fa-solid fa-location-dot"></i> Use Current Location';
                alert('Location access denied or unavailable.');
            }
        );
    } else {
        alert('Geolocation is not supported by your browser.');
    }
};

window.setManualLocation = function() {
    const input = document.getElementById('manual-loc-input').value.trim();
    if (input) {
        const locationBtn = document.querySelector('.use-location-btn');
        if (locationBtn) {
            locationBtn.innerHTML = `<i class="fa-solid fa-location-dot"></i> ${input}`;
            localStorage.setItem('user_location', input);
        }
        document.getElementById('location-modal').style.display = 'none';
    }
};

// Check for saved location on load
document.addEventListener('DOMContentLoaded', () => {
    const savedLoc = localStorage.getItem('user_location');
    if (savedLoc) {
        const locationBtn = document.querySelector('.use-location-btn');
        if (locationBtn) {
            locationBtn.innerHTML = `<i class="fa-solid fa-location-dot"></i> ${savedLoc}`;
        }
    }
});
"""

if "window.triggerGpsLocation" not in js:
    js += "\n" + new_js
    with open(r'c:\Users\Divyanshi123456\Music\hoamex\common.js', 'w', encoding='utf-8') as f:
        f.write(js)

print("Location modal implemented!")
