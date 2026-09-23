import re

with open('plumber.html', 'r', encoding='utf-8') as f:
    html = f.read()

tap_content = html.split('<div id="pipe"')[0]

rest_content = """
<div id="toilet" style="margin-bottom: 36px; padding-top: 20px; border-top: 1px solid #eee;">
    <h2 class="section-heading" style="font-size:24px; margin-bottom:20px;">Toilet</h2>
    <div class="service-card">
        <div class="service-card-info">
            <h4>Toilet Repair</h4>
            <div class="service-rating">
                <i class="fa-solid fa-star"></i>
                <a href="#">4.85 (8K reviews)</a>
            </div>
            <div class="service-price">
                <span>₹199</span>
            </div>
            <ul class="service-features">
                <li>Flush or leak repair</li>
            </ul>
            <a href="#" class="view-details">View details</a>
        </div>
        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="service-img-wrap">
                <img src="images/toilet_icon.jpg" onerror="this.src='images/plumber.jpg'" alt="Toilet Repair">
            </div>
            <button class="add-btn" onclick="addToCart('Toilet Repair', 199)">Add</button>
        </div>
    </div>
</div>

<div id="bath" style="margin-bottom: 36px; padding-top: 20px; border-top: 1px solid #eee;">
    <h2 class="section-heading" style="font-size:24px; margin-bottom:20px;">Bath & shower</h2>
    <div class="service-card">
        <div class="service-card-info">
            <h4>Shower Installation</h4>
            <div class="service-rating">
                <i class="fa-solid fa-star"></i>
                <a href="#">4.85 (8K reviews)</a>
            </div>
            <div class="service-price">
                <span>₹249</span>
            </div>
            <ul class="service-features">
                <li>Shower head or mixer</li>
            </ul>
            <a href="#" class="view-details">View details</a>
        </div>
        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="service-img-wrap">
                <img src="images/bath_icon.jpg" onerror="this.src='images/plumber.jpg'" alt="Shower Install">
            </div>
            <button class="add-btn" onclick="addToCart('Shower Installation', 249)">Add</button>
        </div>
    </div>
</div>

<div id="accessories" style="margin-bottom: 36px; padding-top: 20px; border-top: 1px solid #eee;">
    <h2 class="section-heading" style="font-size:24px; margin-bottom:20px;">Bath accessories</h2>
    <div class="service-card">
        <div class="service-card-info">
            <h4>Accessory Fitting</h4>
            <div class="service-rating">
                <i class="fa-solid fa-star"></i>
                <a href="#">4.85 (8K reviews)</a>
            </div>
            <div class="service-price">
                <span>₹99</span>
            </div>
            <ul class="service-features">
                <li>Towel ring, soap dish</li>
            </ul>
            <a href="#" class="view-details">View details</a>
        </div>
        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="service-img-wrap">
                <img src="images/accessories_icon.jpg" onerror="this.src='images/plumber.jpg'" alt="Accessory Fitting">
            </div>
            <button class="add-btn" onclick="addToCart('Accessory Fitting', 99)">Add</button>
        </div>
    </div>
</div>

<div id="basin" style="margin-bottom: 36px; padding-top: 20px; border-top: 1px solid #eee;">
    <h2 class="section-heading" style="font-size:24px; margin-bottom:20px;">Basin & sink</h2>
    <div class="service-card">
        <div class="service-card-info">
            <h4>Wash Basin Installation</h4>
            <div class="service-rating">
                <i class="fa-solid fa-star"></i>
                <a href="#">4.85 (8K reviews)</a>
            </div>
            <div class="service-price">
                <span>₹349</span>
            </div>
            <ul class="service-features">
                <li>Install or repair basin</li>
            </ul>
            <a href="#" class="view-details">View details</a>
        </div>
        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="service-img-wrap">
                <img src="images/basin_icon.jpg" onerror="this.src='images/plumber.jpg'" alt="Wash Basin">
            </div>
            <button class="add-btn" onclick="addToCart('Wash Basin Install', 349)">Add</button>
        </div>
    </div>
</div>

<div id="drainage" style="margin-bottom: 36px; padding-top: 20px; border-top: 1px solid #eee;">
    <h2 class="section-heading" style="font-size:24px; margin-bottom:20px;">Drainage & blockage</h2>
    <div class="service-card">
        <div class="service-card-info">
            <h4>Blockage Removal</h4>
            <div class="service-rating">
                <i class="fa-solid fa-star"></i>
                <a href="#">4.85 (8K reviews)</a>
            </div>
            <div class="service-price">
                <span>₹299</span>
            </div>
            <ul class="service-features">
                <li>Clear pipes or drains</li>
            </ul>
            <a href="#" class="view-details">View details</a>
        </div>
        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="service-img-wrap">
                <img src="images/drainage_icon.jpg" onerror="this.src='images/plumber.jpg'" alt="Blockage">
            </div>
            <button class="add-btn" onclick="addToCart('Blockage Removal', 299)">Add</button>
        </div>
    </div>
</div>

<div id="appliance" style="margin-bottom: 36px; padding-top: 20px; border-top: 1px solid #eee;">
    <h2 class="section-heading" style="font-size:24px; margin-bottom:20px;">Appliance connections</h2>
    <div class="service-card">
        <div class="service-card-info">
            <h4>Washing Machine Connection</h4>
            <div class="service-rating">
                <i class="fa-solid fa-star"></i>
                <a href="#">4.85 (8K reviews)</a>
            </div>
            <div class="service-price">
                <span>₹199</span>
            </div>
            <ul class="service-features">
                <li>Inlet/outlet connection</li>
            </ul>
            <a href="#" class="view-details">View details</a>
        </div>
        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="service-img-wrap">
                <img src="images/appliance_icon.jpg" onerror="this.src='images/plumber.jpg'" alt="Appliance">
            </div>
            <button class="add-btn" onclick="addToCart('Washing Machine Connection', 199)">Add</button>
        </div>
    </div>
</div>

<div id="tank" style="margin-bottom: 36px; padding-top: 20px; border-top: 1px solid #eee;">
    <h2 class="section-heading" style="font-size:24px; margin-bottom:20px;">Water tank & motor</h2>
    <div class="service-card">
        <div class="service-card-info">
            <h4>Motor Installation</h4>
            <div class="service-rating">
                <i class="fa-solid fa-star"></i>
                <a href="#">4.85 (8K reviews)</a>
            </div>
            <div class="service-price">
                <span>₹399</span>
            </div>
            <ul class="service-features">
                <li>Install water pump</li>
            </ul>
            <a href="#" class="view-details">View details</a>
        </div>
        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div class="service-img-wrap">
                <img src="images/tank_icon.jpg" onerror="this.src='images/plumber.jpg'" alt="Tank Motor">
            </div>
            <button class="add-btn" onclick="addToCart('Motor Installation', 399)">Add</button>
        </div>
    </div>
</div>

<div id="consultation" style="margin-bottom: 36px; padding-top: 20px; border-top: 1px solid #eee;">
    <h2 class="section-heading" style="font-size:24px; margin-bottom:20px;">At home consultation</h2>
    <div style="background: linear-gradient(135deg, #e0e7ff 0%, #f3e8ff 100%); padding: 25px; border-radius: 12px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <span style="background: #000; color: #fff; padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: bold; margin-bottom: 10px; display: inline-block;">Consultation</span>
            <h3 style="margin: 0 0 10px 0; font-size: 22px; color: #111;">Expert Plumber Consultation</h3>
            <p style="margin: 0; color: #444; font-size: 14px; max-width: 300px;">Get professional advice and inspection for your plumbing needs.</p>
        </div>
        <img src="images/plumber.jpg" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 4px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
    </div>
    <div class="service-card">
        <div class="service-card-info">
            <h4>Book a consultation</h4>
            <div class="service-rating">
                <i class="fa-solid fa-star"></i>
                <a href="#">4.89 (15K reviews)</a>
            </div>
            <div class="service-price">
                <span>₹99</span>
            </div>
            <ul class="service-features">
                <li>Expert inspection</li>
            </ul>
            <a href="#" class="view-details">View details</a>
        </div>
        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <button class="add-btn" onclick="addToCart('Plumber Consultation', 99)">Add</button>
        </div>
    </div>
</div>
            </div> <!-- End center content -->
"""

footer_start = html.find('<div class="right-sidebar">')
if footer_start != -1:
    footer_content = html[footer_start:]
else:
    footer_content = '</div>\n</div>\n</div>\n</body>\n</html>'

final_html = tap_content + rest_content + footer_content
with open('plumber.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
