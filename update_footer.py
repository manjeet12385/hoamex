import os
import re

base_dir = r'c:\Users\Divyanshi123456\Music\hoamex'

new_footer = """<footer class="footer" style="padding: 60px 0 0; background-color: #fdfaf6; color: #333; font-family: 'Inter', sans-serif;">
    <div class="footer-container">
        
        <!-- Col 1: Brand -->
        <div class="footer-col">
            <a href="index.html" style="display: inline-flex; flex-direction: column; align-items: flex-start; text-decoration: none; margin-bottom: 20px;">
                <img src="images/logo.png" alt="Joamex Icon" style="height: 45px; border-radius: 8px;">
                <img src="images/logo-text.png" alt="Joamex Text" style="height: 14px; margin-top: 5px;">
            </a>
            <p style="color: #555; font-size: 14px; line-height: 1.6; max-width: 250px;">
                Your one-stop destination for all home service needs. From cleaning to electrical works, we've got you covered with verified professionals.
            </p>
        </div>
        
        <!-- Col 2: Company -->
        <div class="footer-col">
            <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 20px; color: #111;">Company</h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="margin-bottom: 12px;"><a href="about-us.html" style="color: #555; text-decoration: none; font-size: 14px;">About Us</a></li>
                <li style="margin-bottom: 12px;"><a href="terms.html" style="color: #555; text-decoration: none; font-size: 14px;">Terms &amp; Conditions</a></li>
                <li style="margin-bottom: 12px;"><a href="privacy.html" style="color: #555; text-decoration: none; font-size: 14px;">Privacy Policy</a></li>
                <li style="margin-bottom: 12px;"><a href="#" onclick="document.getElementById('cities-section').style.display = document.getElementById('cities-section').style.display === 'none' ? 'block' : 'none'; event.preventDefault();" style="color: #555; text-decoration: none; font-size: 14px;">Cities We Serve ▼</a></li>
            </ul>
        </div>

        <!-- Col 3: For Customers -->
        <div class="footer-col">
            <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 20px; color: #111;">For Customers</h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="margin-bottom: 12px;"><a href="reviews.html" style="color: #555; text-decoration: none; font-size: 14px;">Reviews</a></li>
                <li style="margin-bottom: 12px;"><a href="contact.html" style="color: #555; text-decoration: none; font-size: 14px;">Contact Us</a></li>
                <li style="margin-bottom: 12px;"><a href="categories.html" style="color: #555; text-decoration: none; font-size: 14px;">Services We Offer</a></li>
            </ul>
        </div>
        
        <!-- Col 4: For Professionals -->
        <div class="footer-col">
            <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 20px; color: #111;">For Professionals</h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="margin-bottom: 12px;"><a href="partner.html" style="color: #555; text-decoration: none; font-size: 14px;">Join as a Service Partner</a></li>
            </ul>
        </div>

        <!-- Col 5: Social Media & Quick Contact -->
        <div class="footer-col">
            <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 15px; color: #111;">Social Media</h3>
            <div style="display: flex; gap: 10px; margin-bottom: 25px;">
                <a href="https://twitter.com/joamex" style="display: flex; align-items: center; justify-content: center; width: 34px; height: 34px; border-radius: 50%; background-color: #4ea4f9; color: white; text-decoration: none;"><i class="fa-brands fa-twitter"></i></a>
                <a href="https://www.facebook.com/vonexperts.in" style="display: flex; align-items: center; justify-content: center; width: 34px; height: 34px; border-radius: 50%; background-color: #3b5998; color: white; text-decoration: none;"><i class="fa-brands fa-facebook-f"></i></a>
                <a href="https://www.instagram.com/joamex.in/" style="display: flex; align-items: center; justify-content: center; width: 34px; height: 34px; border-radius: 50%; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white; text-decoration: none;"><i class="fa-brands fa-instagram"></i></a>
                <a href="https://www.linkedin.com/authwall?trk=bf&trkInfo=AQFx4WC" style="display: flex; align-items: center; justify-content: center; width: 34px; height: 34px; border-radius: 50%; background-color: #0e76a8; color: white; text-decoration: none;"><i class="fa-brands fa-linkedin-in"></i></a>
                <a href="https://youtube.com/@joamex" style="display: flex; align-items: center; justify-content: center; width: 34px; height: 34px; border-radius: 50%; background-color: #ff0000; color: white; text-decoration: none;"><i class="fa-brands fa-youtube"></i></a>
            </div>
            
            <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 15px; color: #111;">Quick Contact</h3>
            <div style="display: flex; gap: 10px;">
                <a href="https://wa.me/919014380344" style="display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 50%; background-color: #25d366; color: white; text-decoration: none; font-size: 20px;"><i class="fa-brands fa-whatsapp"></i></a>
                <a href="tel:+919014380344" style="display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 50%; background-color: #5c6bc0; color: white; text-decoration: none; font-size: 18px;"><i class="fa-solid fa-phone"></i></a>
            </div>
        </div>
    </div>
    
    <!-- Cities Expandable Section -->
    <div id="cities-section" style="display: none; background-color: #fdfaf6; padding: 0 20px 40px;">
        <div style="max-width: 1200px; margin: 0 auto; border-top: 1px solid #ebe9e4; padding-top: 30px;">
            <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 25px; color: #111;">Cities We Serve</h3>
            <div class="cities-grid">
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <a href="categories.html" style="color: #555; text-decoration: none;">Bengaluru</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Kolkata</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Nagpur</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Kanpur</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Guntur</a>
                </div>
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <a href="categories.html" style="color: #555; text-decoration: none;">Hyderabad</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Jaipur</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Vizag</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Nashik</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Nellore</a>
                </div>
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <a href="categories.html" style="color: #555; text-decoration: none;">Mumbai</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Surat</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Bhopal</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Mysore</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Warangal</a>
                </div>
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <a href="categories.html" style="color: #555; text-decoration: none;">Delhi NCR</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Lucknow</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Thiruvananthapuram</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Vijayawada</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Khammam</a>
                </div>
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <a href="categories.html" style="color: #555; text-decoration: none;">Chennai</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Indore</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Chandigarh</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Ludhiana</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Karimnagar</a>
                </div>
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <a href="categories.html" style="color: #555; text-decoration: none;">Pune</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Coimbatore</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Vadodara</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Madurai</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Nizamabad</a>
                </div>
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <a href="categories.html" style="color: #555; text-decoration: none;">Ahmedabad</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Kochi</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Patna</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Rajkot</a>
                    <a href="categories.html" style="color: #555; text-decoration: none;">Mahbubnagar</a>
                </div>
            </div>
        </div>
    </div>
    
    <div class="footer-bottom" style="background-color: #e9e6e0; padding: 25px; text-align: center; color: #666; font-size: 14px; border-top: 1px solid #d5d3ce;">
        <div style="margin-bottom: 5px;">&copy; 2026 Joamex | All Rights Reserved</div>
        <div>managed by <strong style="color: #111; font-weight: 700;">Indian Export Webmart</strong></div>
    </div>
</footer>"""

html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]
footer_pattern = re.compile(r'<footer class="footer".*?</footer>', re.DOTALL)

for file in html_files:
    filepath = os.path.join(base_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = footer_pattern.sub(new_footer, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {file}")
