import re

with open('plumber.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the hero banner
hero_banner_replacement = """
<div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 30px; background: #e0e7ff; display: flex;">
    <div style="flex: 1; padding: 40px;">
        <span style="background: #16a34a; color: white; padding: 4px 12px; border-radius: 6px; font-size: 14px; font-weight: 600; display: inline-block; margin-bottom: 20px;">Super saver</span>
        <h2 style="color: #111; font-size: 32px; font-weight: 700; margin: 0; line-height: 1.3;">Affordable repairs<br>starting at just ₹49</h2>
    </div>
    <div style="flex: 1;">
        <img src="images/tap_icon.jpg" onerror="this.src='images/plumber.jpg'" alt="Tap Repair" style="width: 100%; height: 250px; object-fit: cover; display: block;">
    </div>
    <div style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); display: flex; gap: 8px;">
        <div style="width: 30px; height: 4px; background: white; border-radius: 2px;"></div>
        <div style="width: 30px; height: 4px; background: rgba(255,255,255,0.4); border-radius: 2px;"></div>
    </div>
</div>
"""

html = re.sub(
    r'<div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 30px;">.*?<div id="tap" style="margin-bottom: 36px; padding-top: 20px; border-top: 1px solid #eee;">',
    f'{hero_banner_replacement}\\n<div id="tap" style="margin-bottom: 36px; padding-top: 20px; border-top: 1px solid #eee;">',
    html,
    flags=re.DOTALL
)

# Replace Tap section content
tap_section_replacement = """
    <h2 class="section-heading" style="font-size:24px; margin-bottom:20px;">Tap & mixer</h2>
    <div style="display: grid; grid-template-columns: 1fr 280px; gap: 20px; margin-bottom: 20px;">
        <div class="service-card" style="margin-bottom: 0; display: flex; justify-content: space-between; align-items: flex-start; padding: 20px; border: 1px solid #eee; border-radius: 12px; background: #fff;">
            <div class="service-card-info" style="flex: 1;">
                <h4 style="font-size: 18px; font-weight: 600; color: #111; margin: 0 0 8px 0;">Combo for tap & mixer</h4>
                <div class="service-rating" style="display: flex; align-items: center; font-size: 14px; margin-bottom: 8px; color: #555;">
                    <i class="fa-solid fa-star" style="color: #7b1fa2; margin-right: 4px;"></i>
                    <a href="#" style="color: #666; text-decoration: underline; margin-left: 2px;">4.80 (297K reviews)</a>
                </div>
                <div class="service-price" style="font-size: 14px; color: #333; margin-bottom: 12px;">
                    <span style="font-weight: 600;">Starts at ₹129</span> • 30 mins
                </div>
                <a href="#" class="view-details" style="color: #6366f1; font-weight: 600; text-decoration: none; font-size: 14px;">View details</a>
            </div>
            <div style="width: 100px; display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative;">
                <div style="background: #f0fdf4; color: #16a34a; font-weight: 800; font-size: 18px; text-align: center; padding: 15px 10px; border-radius: 8px; width: 100%; border: 1px solid #bbf7d0; box-sizing: border-box;">
                    10%<br>OFF
                </div>
                <button class="add-btn" onclick="addToCart('Combo for tap & mixer', 129)" style="background: #fff; color: #6366f1; border: 1px solid #e0e7ff; box-shadow: 0 4px 6px rgba(0,0,0,0.05); padding: 8px 0; border-radius: 6px; font-weight: 600; font-size: 14px; cursor: pointer; width: 80px; position: absolute; bottom: -15px;">Add</button>
            </div>
        </div>
        
        <div style="display: flex; flex-direction: column; gap: 15px;">
            <div style="border: 1px solid #eee; border-radius: 12px; padding: 15px; display: flex; align-items: center; gap: 10px;">
                <div style="width: 24px; height: 24px; background: #e0e7ff; color: #6366f1; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: bold;">%</div>
                <div style="font-size: 12px;">
                    <span style="font-weight: 600; color: #111; display: block;">Get visitation fee off</span>
                    <span style="color: #666;">On orders above ₹499</span>
                </div>
            </div>
            <div style="border: 1px solid #eee; border-radius: 12px; padding: 15px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                    <span style="font-weight: 600; color: #111;">UC Promise</span>
                    <img src="images/logo.png" alt="Promise" style="height: 30px;">
                </div>
                <ul style="list-style: none; padding: 0; margin: 0; font-size: 13px; color: #444; line-height: 2;">
                    <li><i class="fa-solid fa-check" style="color: #111; margin-right: 8px;"></i>Verified Professionals</li>
                    <li><i class="fa-solid fa-check" style="color: #111; margin-right: 8px;"></i>Hassle Free Booking</li>
                    <li><i class="fa-solid fa-check" style="color: #111; margin-right: 8px;"></i>Transparent Pricing</li>
                </ul>
            </div>
        </div>
    </div>
"""

# Replace the old Tap repair/install block
html = re.sub(
    r'<h2 class="section-heading" style="font-size:24px; margin-bottom:20px;">Tap repair/install</h2>.*?<div class="service-card">.*?<div class="service-card-info">.*?<h4>New Tap Install</h4>.*?</div>.*?</div>.*?</div>',
    tap_section_replacement,
    html,
    flags=re.DOTALL
)

with open('plumber.html', 'w', encoding='utf-8') as f:
    f.write(html)
