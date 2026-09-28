import os
import re

base_dir = r'c:\Users\Divyanshi123456\Music\hoamex'

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Joamex</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
    <style>
        .page-header {{
            background: #f8f9fa;
            padding: 80px 20px 40px;
            text-align: center;
        }}
        .page-title {{
            font-size: 36px;
            font-weight: 800;
            color: #111;
            margin-bottom: 20px;
        }}
        .content-container {{
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
            font-size: 16px;
            line-height: 1.8;
            color: #444;
            min-height: 40vh;
        }}
        h2 {{
            color: #222;
            margin-top: 30px;
            margin-bottom: 15px;
        }}
    </style>
</head>
<body>
    <header class="header">
        <div style="display: flex; align-items: center; gap: 15px;">
            <button id="back-btn" style="background: none; border: none; font-size: 20px; cursor: pointer; display: none;"><i class="fa-solid fa-arrow-left"></i></button>
            <a class="logo" href="index.html" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; margin-right: 15px; text-decoration: none;">
                <img src="images/logo.png" alt="Joamex Icon" style="height: 35px; border-radius: 8px;">
                <img src="images/logo-text.png" alt="Joamex Text" style="height: 12px;">
            </a>
        </div>
        <div class="search-container" id="header-search" style="display: block;">
            <i class="fa-solid fa-magnifying-glass search-icon"></i>
            <input placeholder="Search for services" type="text"/>
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
    </header>

    <div class="page-header" style="margin-top: 80px;">
        <h1 class="page-title">{title}</h1>
    </div>

    <div class="content-container">
        {content}
    </div>

    <!-- The updated footer will be injected by update_footer.py -->
    <footer class="footer"></footer>
    
    <script src="common.js?v=2001"></script>
    <script src="cart.js"></script>
</body>
</html>
"""

pages = {
    'privacy.html': {
        'title': 'Privacy Policy',
        'content': '''<h2>Information We Collect</h2>
        <p>We collect information you provide directly to us, such as when you create or modify your account, request on-demand services, contact customer support, or otherwise communicate with us. This information may include: name, email, phone number, postal address, profile picture, payment method, items requested (for delivery services), and other information you choose to provide.</p>
        <h2>How We Use Your Information</h2>
        <p>We may use the information we collect about you to provide, maintain, and improve our services.</p>'''
    },
    'terms.html': {
        'title': 'Terms & Conditions',
        'content': '''<h2>Acceptance of Terms</h2>
        <p>By accessing and using our services, you agree to be bound by these terms and conditions. If you do not agree with any part of these terms, you may not use our services.</p>
        <h2>Service Usage</h2>
        <p>You agree to use our services only for lawful purposes and in a way that does not infringe the rights of, restrict or inhibit anyone else's use and enjoyment of the website.</p>'''
    },
    'about-us.html': {
        'title': 'About Us',
        'content': '''<h2>Our Mission</h2>
        <p>At Joamex, we believe in making home services accessible, reliable, and premium. Our mission is to connect skilled professionals with customers looking for high-quality services at their doorstep.</p>
        <h2>Our Journey</h2>
        <p>Started in 2024, we have quickly grown to become a trusted name in home services, from beauty and wellness to home repairs and cleaning.</p>'''
    },
    'careers.html': {
        'title': 'Careers',
        'content': '''<h2>Join Our Team</h2>
        <p>We are always looking for passionate and talented individuals to join our growing team. If you want to make an impact in the home services industry, explore our open positions.</p>
        <p>Currently, there are no open positions. Please check back later.</p>'''
    },
    'reviews.html': {
        'title': 'Joamex Reviews',
        'content': '''<h2>What Our Customers Say</h2>
        <p>"Joamex has completely transformed how I manage my home. The professionals are always on time and do a fantastic job!" - Sarah M.</p>
        <p>"The best salon at home service I have ever experienced. Highly recommended!" - Priya K.</p>'''
    },
    'categories.html': {
        'title': 'Categories Near You',
        'content': '''<h2>Explore Our Services</h2>
        <p>We offer a wide range of services including:</p>
        <ul>
            <li>Women's Salon & Spa</li>
            <li>Men's Grooming & Massage</li>
            <li>AC & Appliance Repair</li>
            <li>Home Cleaning</li>
            <li>Plumbing, Electrical, & Carpentry</li>
            <li>Packers & Movers</li>
        </ul>'''
    },
    'blog.html': {
        'title': 'Joamex Blog',
        'content': '''<h2>Latest Updates</h2>
        <p>Welcome to the Joamex blog. Here you will find tips on home maintenance, beauty hacks, and updates about our latest services and offers.</p>'''
    },
    'contact.html': {
        'title': 'Contact Us',
        'content': '''<h2>Get In Touch</h2>
        <p>If you have any questions, feedback, or need assistance, our support team is here to help.</p>
        <p><strong>Email:</strong> support@joamex.com</p>
        <p><strong>Phone:</strong> 1-800-JOAMEX-HELP</p>
        <p><strong>Address:</strong> 123 Service Avenue, Mumbai</p>'''
    },
    'partner.html': {
        'title': 'Join as a Service Partner',
        'content': '''<h2>Grow Your Business with Joamex</h2>
        <p>Are you an experienced professional looking to expand your client base? Join Joamex today and get access to hundreds of verified leads every month.</p>
        <h2>Benefits</h2>
        <ul>
            <li>Flexible working hours</li>
            <li>Direct payouts</li>
            <li>Premium clientele</li>
        </ul>
        <p>Please contact support@joamex.com to start your onboarding process.</p>'''
    }
}

for filename, data in pages.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(template.format(**data))
    print(f"Created {filename}")
