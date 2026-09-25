import re

with open('washing-machine.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title
content = content.replace('<title>Termite Control - Joamex</title>', '<title>Washing Machine - Joamex</title>')

# 2. Update Left Header
new_left_header = """
            <div class="kitchen-header">
                <div>
                    <h1 class="kitchen-title">Washing<br>Machine ...</h1>
                    <div style="display: flex; align-items: center; gap: 5px; font-size: 13px; color: #0f172a; margin-top: 10px;">
                        <i class="fa-solid fa-star" style="color: #0f172a;"></i>
                        <span style="font-weight: 700;">4.78</span>
                        <span style="text-decoration: underline dashed; color: #64748b;">(3.6 M bookings)</span>
                    </div>
                </div>
                <div class="instant-badge" style="background: #15803d; color: white;">
                    <div class="instant-top" style="color: white; border-bottom: none;"><i class="fa-solid fa-bolt"></i> Instant</div>
                    <div class="instant-bottom" style="background: white; color: #15803d; border-radius: 4px; padding: 2px 6px;">In 24 mins</div>
                </div>
            </div>

            <div style="background: #fff7ed; padding: 15px; border-radius: 12px; margin-top: 25px; display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 10px; font-size: 12px; color: #475569; font-weight: 500;">
                    <i class="fa-solid fa-shield-halved" style="color: #475569; font-size: 14px;"></i>
                    Up to 180 days warranty
                </div>
                <i class="fa-solid fa-chevron-right" style="color: #0f172a; font-size: 14px;"></i>
            </div>

            <button class="view-services-btn" style="margin-top: 25px;">View Services</button>
"""
pattern_left = re.compile(r'<div class="kitchen-header">.*?<button class="view-services-btn".*?</button>', re.DOTALL)
content = pattern_left.sub(new_left_header, content)

# 3. Remove Banner (Video/Large banner on right side) since we only want "Select your service"
# Wait, the screenshot shows "Select your service" and then a large video frame with "The Deep Cleaning It Deserves", then the services.
# Let's replace the whole right side content!
new_right_content = """
        <!-- Right Content -->
        <div class="kitchen-right">
            
            <!-- Services Section -->
            <div id="services-section" class="section-box" style="padding-top: 40px;">
                <h2 style="font-size: 24px; font-weight: 700; color: #0f172a; margin-bottom: 25px;">Select your service</h2>
                
                <div style="position: relative; width: 100%; border-radius: 12px; overflow: hidden; margin-bottom: 25px; background: #000; aspect-ratio: 16/9;">
                    <img src="images/cleaning.jpg" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.6;">
                    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-size: 20px; font-weight: 600;">
                        The Deep Cleaning It Deserves
                    </div>
                    <div style="position: absolute; bottom: 15px; right: 15px; color: white;">
                        <i class="fa-solid fa-volume-xmark"></i>
                    </div>
                    <div style="position: absolute; bottom: 10px; left: 15px; right: 40px; height: 3px; background: rgba(255,255,255,0.3); border-radius: 2px;">
                        <div style="width: 30%; height: 100%; background: white; border-radius: 2px;"></div>
                    </div>
                </div>

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Washing machine jet service</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.77</span>
                            <span style="text-decoration: underline dashed;">(3K reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹1,099 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">1 hr 30 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Improves wash quality, fabric care, and machine performance</li>
                            <li>Available for top-load & front-load machines, except Bosch & Siemens</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: flex-end;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-top: 10px;">Add</button>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px dashed #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Washing machine check-up</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.79</span>
                            <span style="text-decoration: underline dashed;">(83K reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹199 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">60 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Complete check-up to identify issues before repair</li>
                            <li>We share a quote and get it approved by you before the repair begins</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Washing machine check-up" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                    </div>
                </div>

            </div>
        </div>
"""
pattern_right = re.compile(r'<!-- Right Content -->.*?</div>\s*</div>\s*</main>', re.DOTALL)
content = pattern_right.sub(new_right_content + '\n    </main>', content)

with open('washing-machine.html', 'w', encoding='utf-8') as f:
    f.write(content)
