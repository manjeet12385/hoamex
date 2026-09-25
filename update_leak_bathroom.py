import re

new_services = """
                <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Bathtub sealing</h3>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            ₹549 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">60 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Seals tub-wall joint to stop leaks; waterproof silicone, dries clear</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Bathtub sealing" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 25px 0;">

                <div style="margin-bottom: 25px;">
                    <div style="display: flex; gap: 10px; margin-bottom: 15px;">
                        <img src="images/cleaning.jpg" style="flex: 2; height: 180px; border-radius: 12px; object-fit: cover;">
                        <div style="flex: 1; display: flex; flex-direction: column; gap: 10px;">
                            <img src="images/cleaning.jpg" style="height: 85px; width: 100%; border-radius: 12px; object-fit: cover;">
                            <img src="images/cleaning.jpg" style="height: 85px; width: 100%; border-radius: 12px; object-fit: cover;">
                        </div>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div style="flex: 1; padding-right: 20px;">
                            <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Basin, toilet base & shower cubicle sealing</h3>
                            <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                                ₹1,199 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">1 hr 30 mins</span>
                            </div>
                            <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                                <li>Seals all critical leaks in bathroom with waterproof silicone</li>
                                <li>Covers 1 WC, 1 wash basin & 1 shower cubicle/ bathtub</li>
                            </ul>
                            <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                        </div>
                        <div style="width: 100px;">
                            <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 8px 0; width: 100%; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">Add</button>
                        </div>
                    </div>
                </div>
"""

with open('leak-gap.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will find the end of the services section and insert it before the closing divs
pattern = re.compile(r'(<div id="services-section" class="section-box">.*?)(</div>\s*</div>\s*</main>)', re.DOTALL)
new_content = pattern.sub(rf'\g<1>\n{new_services}\n\g<2>', content)

with open('leak-gap.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
