import re

with open('washing-machine.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Add button to have an onclick handler
old_button = '<button style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>\n                        <div style="font-size: 11px; color: #64748b; margin-top: 5px;">3 options</div>'
new_button = '<button onclick="document.getElementById(\'installation-modal\').classList.remove(\'hidden\')" style="background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); position: relative; z-index: 2;">Add</button>\n                        <div style="font-size: 11px; color: #64748b; margin-top: 5px;">3 options</div>'

content = content.replace(old_button, new_button)

# 2. Add Modal HTML and CSS
modal_html = """
    <!-- Installation Modal -->
    <div class="modal-overlay hidden" id="installation-modal" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 1000; display: flex; justify-content: center; align-items: center;">
        <div class="modal-content" style="background: #fdfbf7; width: 450px; max-height: 90vh; overflow-y: auto; border-radius: 12px; position: relative;">
            <button onclick="document.getElementById('installation-modal').classList.add('hidden')" style="position: absolute; top: 15px; right: 15px; background: white; border: none; border-radius: 50%; width: 30px; height: 30px; font-size: 16px; cursor: pointer; z-index: 10; box-shadow: 0 2px 5px rgba(0,0,0,0.2);"><i class="fa-solid fa-xmark"></i></button>
            
            <div style="width: 100%; height: 220px; position: relative;">
                <img src="images/cleaning.jpg" alt="Installation" style="width: 100%; height: 100%; object-fit: cover; border-top-left-radius: 12px; border-top-right-radius: 12px;">
                <div style="position: absolute; bottom: 15px; left: 15px; right: 15px; height: 3px; background: rgba(255,255,255,0.3); border-radius: 2px;">
                    <div style="width: 30%; height: 100%; background: white; border-radius: 2px;"></div>
                </div>
            </div>
            
            <div style="padding: 20px;">
                <h2 style="font-size: 22px; font-weight: 700; color: #0f172a; margin: 0 0 8px 0;">Washing machine installation</h2>
                <div style="display: flex; align-items: center; gap: 5px; font-size: 12px; color: #64748b; margin-bottom: 20px;">
                    <i class="fa-solid fa-star" style="color: #6b21a8;"></i>
                    <span style="font-weight: 500; color: #475569;">4.81</span>
                    <span style="text-decoration: underline dashed;">(53K reviews)</span>
                </div>
                
                <div style="background: #fff7ed; padding: 15px; border-radius: 8px; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center; cursor: pointer;">
                    <div style="display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 600; color: #0f766e;">
                        <i class="fa-solid fa-shield-halved"></i>
                        <span>uccover</span>
                        <span style="color: #0f172a; font-weight: 500;">Standard rate card</span>
                    </div>
                    <i class="fa-solid fa-chevron-right" style="color: #0f172a;"></i>
                </div>
                
                <div style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 15px; position: relative;" id="slider-container">
                    
                    <div style="min-width: 140px; border: 1px solid #e2e8f0; border-radius: 8px; background: #fff; padding: 12px; display: flex; flex-direction: column;">
                        <img src="images/cleaning.jpg" alt="Top load" style="width: 100%; height: 100px; object-fit: contain; margin-bottom: 10px;">
                        <h4 style="font-size: 13px; font-weight: 600; color: #0f172a; margin: 0 0 5px 0;">Fully automatic top load</h4>
                        <div style="font-size: 10px; color: #64748b; margin-bottom: 10px; display: flex; align-items: center; gap: 4px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i> 4.81 (30K reviews)
                        </div>
                        <div style="font-size: 13px; font-weight: 600; color: #0f172a; margin-bottom: 15px;">₹399</div>
                        <button style="width: 100%; background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 0; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 13px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-top: auto;">Add</button>
                    </div>
                    
                    <div style="min-width: 140px; border: 1px solid #e2e8f0; border-radius: 8px; background: #fff; padding: 12px; display: flex; flex-direction: column;">
                        <img src="images/cleaning.jpg" alt="Front load" style="width: 100%; height: 100px; object-fit: contain; margin-bottom: 10px;">
                        <h4 style="font-size: 13px; font-weight: 600; color: #0f172a; margin: 0 0 5px 0;">Fully automatic front load</h4>
                        <div style="font-size: 10px; color: #64748b; margin-bottom: 10px; display: flex; align-items: center; gap: 4px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i> 4.80 (23K reviews)
                        </div>
                        <div style="font-size: 13px; font-weight: 600; color: #0f172a; margin-bottom: 15px;">₹399</div>
                        <button style="width: 100%; background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 0; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 13px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-top: auto;">Add</button>
                    </div>
                    
                    <div style="min-width: 140px; border: 1px solid #e2e8f0; border-radius: 8px; background: #fff; padding: 12px; display: flex; flex-direction: column; margin-right: 15px;">
                        <img src="images/cleaning.jpg" alt="Semi-automatic" style="width: 100%; height: 100px; object-fit: contain; margin-bottom: 10px;">
                        <h4 style="font-size: 13px; font-weight: 600; color: #0f172a; margin: 0 0 5px 0;">Semi-automatic</h4>
                        <div style="font-size: 10px; color: #64748b; margin-bottom: 10px; display: flex; align-items: center; gap: 4px;">
                            <i class="fa-solid fa-star" style="color: #6b21a8;"></i> 4.77 (1K reviews)
                        </div>
                        <div style="font-size: 13px; font-weight: 600; color: #0f172a; margin-bottom: 15px;">₹399</div>
                        <button style="width: 100%; background: #fff; color: #7c3aed; font-weight: 600; padding: 6px 0; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 13px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-top: auto;">Add</button>
                    </div>

                    <button style="position: absolute; right: 0; top: 50%; transform: translateY(-50%); background: white; border: 1px solid #e2e8f0; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><i class="fa-solid fa-arrow-right"></i></button>

                </div>
            </div>
        </div>
    </div>
"""

# add a small style for hidden class if not exist
if '.hidden { display: none !important; }' not in content:
    content = content.replace('</style>', '    .hidden { display: none !important; }\n    </style>')

# add modal right before closing body
content = content.replace('</body>', modal_html + '\n</body>')

with open('washing-machine.html', 'w', encoding='utf-8') as f:
    f.write(content)
