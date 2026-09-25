import re

with open('ants-control.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_services = """
                <h2 style="font-size: 24px; font-weight: 700; color: #0f172a; margin-bottom: 25px;">Bed Bugs Control</h2>
                
                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Bed bugs control</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.77</span>
                            <span style="text-decoration: underline dashed;">(40K reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹1,899
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Essential pre-service inspection of the entire home</li>
                            <li>Unique 2-visit treatment to target eggs, nymphs & adult pests</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Bed Bugs Control" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                        <div style="font-size: 11px; color: #64748b; margin-top: 5px;">5 options</div>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 25px 0;">

                <h2 style="font-size: 24px; font-weight: 700; color: #0f172a; margin-bottom: 25px;">Ant Control</h2>

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Apartment ant control (with utensil removal)</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.80</span>
                            <span style="text-decoration: underline dashed;">(1K reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹1,849
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Complete ant treatment for confined spaces</li>
                            <li>Includes thorough inspection, chemical spray & hole sealing</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Apartment Ant Control" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                        <div style="font-size: 11px; color: #64748b; margin-top: 5px;">5 options</div>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px dashed #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Apartment ant control (without utensil removal)</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.83</span>
                            <span style="text-decoration: underline dashed;">(1K reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹1,549
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Complete ant treatment for confined spaces</li>
                            <li>Includes thorough inspection, chemical spray & hole sealing</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Apartment Ant Control Without Utensil Removal" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                        <div style="font-size: 11px; color: #64748b; margin-top: 5px;">5 options</div>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px dashed #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Bungalow ant control (with utensil removal)</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.66</span>
                            <span style="text-decoration: underline dashed;">(69 reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹2,398
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Extensive ant protection for larger areas</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Bungalow Ant Control" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                        <div style="font-size: 11px; color: #64748b; margin-top: 5px;">4 options</div>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px dashed #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Bungalow ant control (without utensil removal)</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.81</span>
                            <span style="text-decoration: underline dashed;">(83 reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹2,097
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Extensive ant protection for larger areas</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Bungalow Ant Control Without Utensil Removal" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                        <div style="font-size: 11px; color: #64748b; margin-top: 5px;">4 options</div>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px dashed #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Ant control &ndash; kitchen/bathroom (with utensil removal)</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.87</span>
                            <span style="text-decoration: underline dashed;">(742 reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹1,249
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Complete ant treatment for confined spaces</li>
                            <li>We'll remove utensils before the service begins</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Ant Control Kitchen Bathroom" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                        <div style="font-size: 11px; color: #64748b; margin-top: 5px;">6 options</div>
                    </div>
                </div>

                <hr style="border: none; border-top: 1px dashed #e2e8f0; margin: 25px 0;">

                <div style="display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: 10px;">
                    <div style="flex: 1; padding-right: 20px;">
                        <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Ant control &ndash; kitchen/bathroom (without utensil removal)</h3>
                        <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 10px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                            <span style="font-weight: 500; color: #475569;">4.86</span>
                            <span style="text-decoration: underline dashed;">(934 reviews)</span>
                        </div>
                        <div style="font-size: 13px; color: #0f172a; font-weight: 600; margin-bottom: 15px;">
                            Starts at ₹998
                        </div>
                        <ul style="margin: 0; padding: 0 0 0 18px; color: #475569; font-size: 13px; line-height: 1.6; margin-bottom: 15px;">
                            <li>Complete ant treatment for confined spaces</li>
                            <li>Excludes removal of utensils & objects before the service begins</li>
                        </ul>
                        <a href="#" style="color: #7c3aed; font-size: 14px; font-weight: 600; text-decoration: none;">View details</a>
                    </div>
                    <div style="width: 140px; position: relative; display: flex; flex-direction: column; align-items: center;">
                        <img src="images/cleaning.jpg" alt="Ant Control Kitchen Bathroom Without Utensil Removal" style="width: 100%; height: 110px; border-radius: 12px; object-fit: cover; margin-bottom: -15px;">
                        <button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>
                        <div style="font-size: 11px; color: #64748b; margin-top: 5px;">6 options</div>
                    </div>
                </div>
"""

# Replace the inner content of services-section
pattern = re.compile(r'(<div id="services-section" class="section-box">)(.*?)(</div>\s*</div>\s*</main>)', re.DOTALL)
new_content = pattern.sub(rf'\g<1>\n{new_services}\n\g<3>', content)

with open('ants-control.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
