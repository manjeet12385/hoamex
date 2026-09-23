import os
import re

HEADER_HTML = '''<header class="header">
        <div style="display: flex; align-items: center; gap: 15px;">
            <button id="back-btn" style="background: none; border: none; font-size: 20px; cursor: pointer; display: block;"><i class="fa-solid fa-arrow-left"></i></button>
            <a href="index.html" class="logo">
                <div class="logo-icon">J</div>
                <div>
                    <span class="logo-text">Joamex</span>
                    <span class="logo-sub">Home Services Simplified</span>
                </div>
            </a>
        </div>
        <div class="search-container" id="header-search" style="display: none;">
            <i class="fa-solid fa-magnifying-glass search-icon"></i>
            <input type="text" placeholder="Search for services">
        </div>
        <div class="header-actions">
            <button class="location-btn"><i class="fa-solid fa-location-dot"></i> Use Current Location</button>
            <button class="partner-btn"><i class="fa-solid fa-handshake"></i> Join as Partner</button>
            <div class="icon-btn"><i class="fa-regular fa-user"></i></div>
            <div class="icon-btn" id="open-cart-btn" style="position: relative;">
                <i class="fa-solid fa-cart-shopping"></i>
                <span id="cart-badge" style="position: absolute; top: -5px; right: -5px; background: #e53935; color: white; font-size: 10px; font-weight: bold; padding: 2px 5px; border-radius: 10px; display: none;">0</span>
            </div>
        </div>
    </header>'''

FOOTER_HTML = '''<style>
.footer { background: #fff; color: #333; border-top: 1px solid #eaeaea; padding: 60px 40px; margin-top: 50px; font-family: 'Inter', sans-serif; }
.footer-container { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; }
.footer-col h3 { font-size: 18px; font-weight: 700; margin-bottom: 20px; color: #111; }
.footer-col ul { list-style: none; padding: 0; margin: 0; }
.footer-col ul li { margin-bottom: 12px; }
.footer-col ul li a { color: #666; text-decoration: none; font-size: 14px; transition: color 0.2s; }
.footer-col ul li a:hover { color: #000; }
.footer-logo { font-size: 28px; font-weight: 800; color: #000; text-decoration: none; display: block; margin-bottom: 20px; }
.footer-bottom { max-width: 1200px; margin: 40px auto 0; padding-top: 20px; border-top: 1px solid #eaeaea; display: flex; justify-content: space-between; align-items: center; font-size: 13px; color: #666; }
.social-icons a { color: #333; font-size: 18px; margin-left: 15px; text-decoration: none; }
.social-icons a:hover { color: #6366f1; }
@media (max-width: 768px) { .footer { padding: 40px 20px; } .footer-container { grid-template-columns: 1fr 1fr; gap: 30px; } .footer-bottom { flex-direction: column; gap: 20px; text-align: center; } }
@media (max-width: 480px) { .footer-container { grid-template-columns: 1fr; } }
</style>
<footer class="footer">
    <div class="footer-container">
        <div class="footer-col" style="grid-column: span 2;">
            <a href="index.html" class="footer-logo">Joamex</a>
            <p style="color: #666; font-size: 14px; line-height: 1.6; max-width: 300px;">Your trusted partner for premium home services. From grooming to appliance repair, we deliver excellence right at your doorstep.</p>
        </div>
        <div class="footer-col">
            <h3>Company</h3>
            <ul>
                <li><a href="#">About Us</a></li>
                <li><a href="#">Terms &amp; Conditions</a></li>
                <li><a href="#">Privacy Policy</a></li>
                <li><a href="#">Careers</a></li>
            </ul>
        </div>
        <div class="footer-col">
            <h3>For Customers</h3>
            <ul>
                <li><a href="#">UC Reviews</a></li>
                <li><a href="#">Categories near you</a></li>
                <li><a href="#">Blog</a></li>
                <li><a href="#">Contact Us</a></li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        <div>&copy; 2024 Joamex Technologies Ltd. All rights reserved.</div>
        <div class="social-icons">
            <a href="#"><i class="fa-brands fa-twitter"></i></a>
            <a href="#"><i class="fa-brands fa-facebook"></i></a>
            <a href="#"><i class="fa-brands fa-instagram"></i></a>
            <a href="#"><i class="fa-brands fa-linkedin"></i></a>
        </div>
    </div>
</footer>'''

folder = r'c:\Users\Divyanshi123456\Music\hoamex'
skip_files = {'index.html', 'header.html', 'footer.html'}

updated = 0
for filename in os.listdir(folder):
    if not filename.endswith('.html') or filename in skip_files:
        continue
    
    filepath = os.path.join(folder, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Replace header placeholder
    content = re.sub(
        r'<div\s+id=["\']header-placeholder["\']>\s*</div>',
        HEADER_HTML,
        content
    )
    
    # Replace footer placeholder  
    content = re.sub(
        r'<div\s+id=["\']footer-placeholder["\']>\s*</div>',
        FOOTER_HTML,
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print(f'Updated: {filename}')

print(f'\nDone! {updated} files updated.')
