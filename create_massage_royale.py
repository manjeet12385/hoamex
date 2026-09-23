import shutil

def create_massage_royale():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Massage for Men Royale - Joamex</title>
    <link rel="stylesheet" href="style.css?v=8">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; margin: 0; background: #fff; }
        .header { display: flex; align-items: center; justify-content: space-between; padding: 12px 30px; border-bottom: 1px solid #eee; background: white; position: sticky; top: 0; z-index: 100; }
        .logo { display: flex; align-items: center; gap: 8px; text-decoration: none; color: inherit; }
        .logo-icon { background: #f5a623; color: white; font-weight: 700; font-size: 16px; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; border-radius: 6px; }
        .logo-text { font-weight: 700; font-size: 18px; color: #222; }
        .logo-sub { font-size: 11px; color: #999; display: block; }
        .search-container { flex: 1; max-width: 400px; margin: 0 30px; position: relative; }
        .search-container input { width: 100%; padding: 9px 15px 9px 38px; border: 1px solid #ddd; border-radius: 8px; font-size: 14px; outline: none; box-sizing: border-box; }
        .search-icon { position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: #999; }
        .header-actions { display: flex; align-items: center; gap: 12px; }
        .location-btn { background: none; border: none; color: #555; cursor: pointer; font-size: 13px; display: flex; align-items: center; gap: 5px; }
        .partner-btn { background: #00875a; color: white; border: none; padding: 9px 16px; border-radius: 8px; cursor: pointer; font-size: 13px; font-weight: 600; display: flex; align-items: center; gap: 6px; }
        .icon-btn { width: 36px; height: 36px; border-radius: 50%; border: 1px solid #eee; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #555; }

        /* Page Layout */
        .page-wrapper { max-width: 1200px; margin: 0 auto; padding: 30px 20px; }
        .top-section { display: flex; align-items: flex-start; gap: 20px; margin-bottom: 40px; }
        .page-title { font-size: 32px; font-weight: 700; line-height: 1.2; margin: 0 0 8px 0; }
        .page-rating { display: flex; align-items: center; gap: 5px; font-size: 14px; color: #333; }
        .page-rating i { color: #7d33ff; }
        .page-rating span { color: #666; }

        /* 3-column layout */
        .three-col-layout { display: grid; grid-template-columns: 260px 1fr 220px; gap: 24px; align-items: start; }

        /* Left sidebar */
        .left-sidebar { position: sticky; top: 80px; }
        .select-service-card { border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px; }
        .select-service-card h3 { font-size: 13px; color: #64748b; font-weight: 500; margin: 0 0 14px 0; }
        .service-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
        .service-item { text-align: center; cursor: pointer; text-decoration: none; color: inherit; }
        .service-item-img { width: 52px; height: 52px; border-radius: 8px; overflow: hidden; margin: 0 auto 6px; background: #f8f9fa; display: flex; align-items: center; justify-content: center; }
        .service-item-img img { width: 100%; height: 100%; object-fit: cover; }
        .service-item span { font-size: 11px; font-weight: 500; line-height: 1.3; display: block; }

        /* Center content */
        .center-content {}

        /* Banner */
        .uc-difference-banner { background: #e8e8e8; border-radius: 14px; padding: 30px 30px 30px 30px; margin-bottom: 30px; position: relative; display: flex; align-items: center; justify-content: space-between; overflow: hidden; min-height: 300px; background-size: cover; background-position: center; color: white;}
        .uc-difference-banner::before {
            content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); z-index: 1;
        }
        .banner-text { position: relative; z-index: 2; width: 100%; text-align: center; }
        .banner-text h2 { font-size: 42px; font-weight: 700; margin: 0; }
        .banner-dots { position: absolute; bottom: 12px; left: 30px; display: flex; gap: 6px; z-index: 2; }
        .banner-dots span { width: 28px; height: 4px; border-radius: 2px; background: rgba(255,255,255,0.4); }
        .banner-dots span.active { background: rgba(255,255,255,1); }

        /* Service sections */
        .section-heading { font-size: 22px; font-weight: 700; margin: 0 0 16px 0; }
        .service-card { border: 1px solid #eee; border-radius: 12px; padding: 20px; display: flex; justify-content: space-between; gap: 16px; margin-bottom: 16px; }
        .service-card-info { flex: 1; }
        .service-card-info h4 { font-size: 17px; font-weight: 700; margin: 0 0 6px 0; }
        .service-rating { font-size: 13px; color: #666; margin-bottom: 4px; }
        .service-rating i { color: #7d33ff; }
        .service-rating a { color: #7d33ff; text-decoration: underline dotted; }
        .service-price { font-size: 14px; font-weight: 600; margin-bottom: 12px; color: #111; }
        .service-price span { font-size: 13px; font-weight: 400; color: #666; }
        .service-features { list-style: none; padding: 0; margin: 0 0 12px 0; }
        .service-features li { font-size: 13px; color: #666; padding: 3px 0; padding-left: 14px; position: relative; }
        .service-features li::before { content: '•'; position: absolute; left: 0; color: #999; }
        .view-details { color: #7d33ff; font-size: 13px; font-weight: 600; text-decoration: none; }
        .service-card-img { width: 110px; display: flex; flex-direction: column; align-items: center; flex-shrink: 0; }
        .service-img-wrap { width: 100px; height: 100px; border-radius: 10px; overflow: hidden; margin-bottom: -14px; position: relative; z-index: 1; }
        .service-img-wrap img { width: 100%; height: 100%; object-fit: cover; }
        .add-btn { padding: 8px 28px; background: white; border: 1px solid #ddd; color: #7d33ff; font-weight: 700; border-radius: 8px; cursor: pointer; font-size: 14px; position: relative; z-index: 2; box-shadow: 0 2px 6px rgba(0,0,0,0.08); width: 100%; }
        .add-btn:hover { background: #f5f0ff; }

        /* Right sidebar */
        .right-sidebar { position: sticky; top: 80px; }
        .uc-promise-card { border: 1px solid #eee; border-radius: 10px; padding: 18px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: flex-start; }
        .uc-promise-card h3 { font-size: 15px; font-weight: 700; margin: 0 0 10px 0; }
        .uc-promise-card ul { list-style: none; padding: 0; margin: 0; }
        .uc-promise-card ul li { font-size: 13px; color: #555; margin-bottom: 6px; display: flex; align-items: center; gap: 7px; }
        .uc-promise-card ul li i { color: #00875a; font-size: 12px; }
        .promise-badge { width: 52px; height: 52px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
        .cart-card { border: 1px solid #eee; border-radius: 10px; padding: 20px; text-align: center; color: #999; }
        .cart-card i { font-size: 28px; margin-bottom: 8px; display: block; }
        .cart-card p { font-size: 13px; margin: 0; }
    </style>
</head>
<body>

    <!-- Header -->
    <header class="header">
        <a href="index.html" class="logo">
            <span class="logo-icon">J</span>
            <div>
                <span class="logo-text">Joamex</span>
                <span class="logo-sub">Home Services Simplified</span>
            </div>
        </a>
        <div class="search-container">
            <i class="fa-solid fa-magnifying-glass search-icon"></i>
            <input type="text" placeholder="Search for 'Massage'">
        </div>
        <div class="header-actions">
            <button class="location-btn"><i class="fa-solid fa-location-dot"></i> Use Current Location</button>
            <button class="partner-btn"><i class="fa-solid fa-handshake"></i> Join as Partner</button>
            <div class="icon-btn"><i class="fa-regular fa-user"></i></div>
            <div class="icon-btn"><i class="fa-solid fa-cart-shopping"></i></div>
        </div>
    </header>

    <!-- Main -->
    <main class="page-wrapper">

        <!-- Top title row -->
        <div class="top-section" style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
                <h1 class="page-title" style="font-size: 32px; margin-bottom: 5px;">Massage<br>for Men Royale</h1>
                <div class="page-rating">
                    <i class="fa-solid fa-star" style="color: #000;"></i>
                    <strong>4.88</strong>
                    <span>(632K bookings)</span>
                </div>
            </div>
            <div style="background: #e8f5e9; color: #2e7d32; padding: 5px 10px; border-radius: 6px; text-align: center; border: 1px solid #c8e6c9;">
                <div style="font-size: 10px; font-weight: bold;"><i class="fa-solid fa-clock" style="margin-right: 3px;"></i> Earliest</div>
                <div style="font-size: 12px; margin-top: 2px; font-weight: bold;">Mon, 1:30 PM</div>
            </div>
        </div>

        <!-- 3-Column Layout -->
        <div class="three-col-layout">

            <!-- LEFT SIDEBAR: Select a service -->
            <div class="left-sidebar">
                <div class="select-service-card">
                    <h3 style="margin-bottom: 20px; font-size: 11px; color: #777; border-bottom: 1px solid #eee; padding-bottom: 10px; display: inline-block; font-weight: normal;">Select a service</h3>
                    <div class="service-grid">
                        <a href="#pain-relief" class="service-item">
                            <div class="service-item-img">
                                <img src="images/beauty.jpg" alt="Pain relief">
                            </div>
                            <span style="font-size: 10px; color: #333;">Pain relief</span>
                        </a>
                        <a href="#stress-relief" class="service-item">
                            <div class="service-item-img">
                                <img src="images/beauty.jpg" alt="Stress relief">
                            </div>
                            <span style="font-size: 10px; color: #333;">Stress relief</span>
                        </a>
                        <a href="#sports-therapy" class="service-item">
                            <div class="service-item-img">
                                <img src="images/beauty.jpg" alt="Sports therapy">
                            </div>
                            <span style="font-size: 10px; color: #333;">Sports therapy</span>
                        </a>
                        <a href="#signature-therapy" class="service-item">
                            <div class="service-item-img">
                                <img src="images/beauty.jpg" alt="Signature therapy">
                            </div>
                            <span style="font-size: 10px; color: #333;">Signature therapy</span>
                        </a>
                        <a href="#add-ons" class="service-item">
                            <div class="service-item-img">
                                <img src="images/beauty.jpg" alt="Add-ons">
                            </div>
                            <span style="font-size: 10px; color: #333;">Add-ons</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- CENTER CONTENT -->
            <div class="center-content">
                
                <!-- Banner -->
                <div class="uc-difference-banner" style="background-image: url('images/beauty.jpg'); border-radius: 8px;">
                    <div class="banner-text">
                        <h2>Where massage meets luxury</h2>
                    </div>
                    <div class="banner-dots">
                        <span class="active"></span>
                        <span></span>
                        <span></span>
                    </div>
                </div>

                <!-- Pain relief -->
                <div id="pain-relief-section" style="margin-bottom: 36px; padding-top: 20px;">
                    <h2 class="section-heading" style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">Pain relief</h2>
                    
                    <div class="service-card" style="border-bottom: 1px solid #eee; padding-bottom: 25px; margin-bottom: 25px; align-items: stretch; position: relative;">
                        <div class="service-card-info" style="flex: 1; padding-right: 20px;">
                            <h4 style="font-size: 18px; margin-bottom: 5px; font-weight: 700;">Deep Tissue Massage (60 mins)</h4>
                            <div class="service-rating" style="margin-bottom: 8px;">
                                <i class="fa-solid fa-star"></i>
                                <a href="#" style="color: #666; text-decoration: underline dotted; font-size: 13px;">4.85 (42K reviews)</a>
                            </div>
                            <div class="service-price" style="margin-bottom: 15px; font-size: 13px; color: #444;">
                                <span style="font-weight: 700; color: #000;">₹999</span> &bull; <span>60 mins</span>
                            </div>
                            <ul class="service-features" style="margin-bottom: 15px; font-size: 13px; color: #555;">
                                <li style="margin-bottom: 6px;">Deep pressure to relieve severe tension and muscle pain</li>
                            </ul>
                            <a href="#" class="view-details">View details</a>
                        </div>
                        <div style="width: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div class="service-img-wrap" style="width: 120px; height: 120px; border-radius: 12px; margin-bottom: -15px;">
                                <img src="images/beauty.jpg" alt="Deep tissue massage">
                            </div>
                            <button class="add-btn">Add</button>
                        </div>
                    </div>
                </div>

            </div><!-- end center-content -->

            <!-- RIGHT SIDEBAR -->
            <div class="right-sidebar">
                <div class="uc-promise-card">
                    <div>
                        <h3>Joamex Promise</h3>
                        <ul>
                            <li><i class="fa-solid fa-check"></i> Verified Professionals</li>
                            <li><i class="fa-solid fa-check"></i> Hassle Free Service</li>
                            <li><i class="fa-solid fa-check"></i> Transparent Pricing</li>
                        </ul>
                    </div>
                    <img src="images/beauty.jpg" alt="Promise" class="promise-badge">
                </div>
                
                <div class="cart-card">
                    <i class="fa-solid fa-cart-shopping"></i>
                    <p>No items in your cart</p>
                </div>
            </div>

        </div><!-- end 3-column-layout -->

    </main>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Scroll Logic
            const sections = [
                { btn: 'pain-relief', section: 'pain-relief-section' },
            ];

            sections.forEach(s => {
                const trigger = document.querySelector(`a[href="#${s.btn}"]`);
                const section = document.getElementById(s.section);
                if(trigger && section) {
                    trigger.addEventListener('click', (e) => {
                        e.preventDefault();
                        section.scrollIntoView({ behavior: 'smooth' });
                    });
                }
            });
        });
    </script>
</body>
</html>
"""
    with open("massage-royale.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    create_massage_royale()
