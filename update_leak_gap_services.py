import re

html_content = """
                <h2 id="bedroom" style="font-size: 24px; font-weight: 700; color: #0f172a; margin-bottom: 25px;">Bedroom & Living Areas</h2>
                
                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Door frame gap sealing</h3>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            ₹449 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">45 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Seals gaps around door frames to block dust & pests</li>
                            <li>White acrylic sealant; can be painted when dry</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Door frame gap sealing" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Window frame gap sealing (Paintable)</h3>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            ₹549 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">60 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Fills window-frame gaps from installation/settling; blocks dust and pests</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Window frame gap sealing (Paintable)" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Window frame gap sealing (Waterproof)</h3>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            ₹549 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">60 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Seals exterior gaps around window frames to block water & dust</li>
                            <li>Weatherproof & waterproof clear silicone sealant</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Window frame gap sealing (Waterproof)" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Cabinet to wall gap sealing</h3>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            ₹449 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">45 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Seals cabinet-to-wall gaps to block dust & pest entry</li>
                            <li>White acrylic sealant; can be painted when dry</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Cabinet to wall gap sealing" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Cupboard to wall gap sealing</h3>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            ₹449 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">45 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Seals cupboard-to-wall gaps to block dust & pest entry</li>
                            <li>White acrylic sealant; can be painted when dry</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Cupboard to wall gap sealing" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Skirting gap sealing</h3>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            ₹599 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">60 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Seals skirting-to-wall gaps to block dust & pest entry</li>
                            <li>White acrylic sealant; can be painted when dry</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Skirting gap sealing" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                    </div>
                </div>

                <hr style="border: none; border-top: 2px solid #f1f5f9; margin: 40px 0;">

                <h2 id="kitchen" style="font-size: 24px; font-weight: 700; color: #0f172a; margin-bottom: 25px;">Kitchen</h2>

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Kitchen sink sealing</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.65</span>
                            <span style="text-decoration: underline dashed;">(85 reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            ₹549 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">60 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Seals sink-to-wall gap to stop seepage; waterproof silicone, dries clear</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Kitchen sink sealing" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
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
                            <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Kitchen sink & slab sealing</h3>
                            <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                                <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                                <span style="font-weight: 500; color: #475569;">4.73</span>
                                <span style="text-decoration: underline dashed;">(32 reviews)</span>
                            </div>
                            <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                                ₹1,499 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">2 hrs</span>
                            </div>
                            <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                                <li>Seals all critical gaps on kitchen countertop; stops water & pests</li>
                                <li>Covers sink, countertop & hob joints with waterproof silicone</li>
                            </ul>
                            <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                        </div>
                        <div style="width: 100px;">
                            <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 8px 0; width: 100%; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">Add</button>
                        </div>
                    </div>
                </div>

                <hr style="border: none; border-top: 2px solid #f1f5f9; margin: 40px 0;">

                <h2 id="bathroom" style="font-size: 24px; font-weight: 700; color: #0f172a; margin-bottom: 25px;">Bathroom</h2>

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">WC / Toilet base sealing</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.75</span>
                            <span style="text-decoration: underline dashed;">(28 reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            ₹399 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">45 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Seals toilet base to stop water seepage; waterproof silicone, dries clear</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="WC Toilet base sealing" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Wash basin sealing</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.69</span>
                            <span style="text-decoration: underline dashed;">(18 reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            ₹399 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">45 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Seals basin-to-wall gap to stop seepage and leaks; waterproof, dries clear</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Wash basin sealing" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Shower cubicle sealing</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.96</span>
                            <span style="text-decoration: underline dashed;">(14 reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            ₹549 &nbsp;&bull;&nbsp; <span style="font-weight: 400; color: #64748b;">60 mins</span>
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Seals glass-to-wall gap to stop leaks; waterproof silicone, dries clear</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Shower cubicle sealing" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                    </div>
                </div>
"""

import re
with open('leak-gap.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(<div id="services-section" class="section-box">)(.*?)(</div>\s*</div>\s*</main>)', re.DOTALL)
new_content = pattern.sub(rf'\g<1>\n{html_content}\n\g<3>', content)

with open('leak-gap.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
