const fs = require('fs');
let content = fs.readFileSync('fan-installation', 'utf8');

// 1. Replace the onclick for Ceiling fan
content = content.replace(
    `<button class="add-btn" onclick="addToCart('Ceiling fan installation/replacement',248)">Add</button>`,
    `<button class="add-btn" onclick="document.getElementById('ceiling-fan-modal').style.display='flex'">Add</button>`
);

// 2. Replace the onclick for Exhaust fan
content = content.replace(
    `<button class="add-btn" onclick="addToCart('Exhaust fan installation/replacement',248)">Add</button>`,
    `<button class="add-btn" onclick="document.getElementById('exhaust-fan-modal').style.display='flex'">Add</button>`
);

const modals = `
    <!-- Ceiling Fan Modal -->
    <div id="ceiling-fan-modal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 1000; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf9; width: 100%; max-width: 500px; padding: 0; overflow: hidden; border-radius: 12px; position: relative;">
            <button class="modal-close" onclick="document.getElementById('ceiling-fan-modal').style.display='none'" style="position: absolute; z-index: 10; background: white; border: none; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; top: 15px; right: 15px; cursor: pointer;"><i class="fa-solid fa-xmark"></i></button>
            
            <div class="options-modal-body" style="padding: 24px;">
                <h3 class="options-modal-title" style="font-size: 22px; margin-bottom: 5px; font-weight: 700;">Ceiling fan installation/replacement</h3>
                <div class="options-rating" style="margin-bottom: 15px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.89 <span style="color: #666; font-weight: 400;">(29K reviews)</span></div>
                
                <div style="background: #fff9f0; padding: 12px; border-radius: 8px; margin-bottom: 20px; font-size: 13px; font-weight: 600; color: #333; display: flex; align-items: center;">
                    <i class="fa-solid fa-shield" style="color: #00875a; margin-right: 8px;"></i> uc cover &nbsp; <span style="font-weight: 400;">Standard rate card</span>
                </div>

                <div class="vertical-options-list">
                    <!-- Option 1 -->
                    <div class="vertical-option-row">
                        <div class="vertical-option-info">
                            <h4>Installation</h4>
                            <div class="option-rating"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.88 (17K reviews)</div>
                            <div class="option-price">₹248 &bull; <span style="color: #777; font-weight: 400;">10 mins</span></div>
                        </div>
                        <div class="vertical-option-media">
                            <img src="images/new_fan_installation_icon.jpg" alt="Installation">
                            <button onclick="addToCart('Ceiling fan installation', 248); document.getElementById('ceiling-fan-modal').style.display='none';">Add</button>
                        </div>
                    </div>
                    <!-- Option 2 -->
                    <div class="vertical-option-row">
                        <div class="vertical-option-info">
                            <h4>Replacement</h4>
                            <div class="option-rating"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.90 (12K reviews)</div>
                            <div class="option-price">₹298 &bull; <span style="color: #777; font-weight: 400;">10 mins</span></div>
                        </div>
                        <div class="vertical-option-media">
                            <img src="images/new_fan_installation_icon.jpg" alt="Replacement">
                            <button onclick="addToCart('Ceiling fan replacement', 298); document.getElementById('ceiling-fan-modal').style.display='none';">Add</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Exhaust Fan Modal -->
    <div id="exhaust-fan-modal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 1000; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf9; width: 100%; max-width: 500px; padding: 0; overflow: hidden; border-radius: 12px; position: relative;">
            <button class="modal-close" onclick="document.getElementById('exhaust-fan-modal').style.display='none'" style="position: absolute; z-index: 10; background: white; border: none; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; top: 15px; right: 15px; cursor: pointer;"><i class="fa-solid fa-xmark"></i></button>
            
            <div class="options-modal-body" style="padding: 24px;">
                <h3 class="options-modal-title" style="font-size: 22px; margin-bottom: 5px; font-weight: 700;">Exhaust fan installation/replacement</h3>
                <div class="options-rating" style="margin-bottom: 15px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.84 <span style="color: #666; font-weight: 400;">(8K reviews)</span></div>
                
                <div style="background: #fff9f0; padding: 12px; border-radius: 8px; margin-bottom: 20px; font-size: 13px; font-weight: 600; color: #333; display: flex; align-items: center;">
                    <i class="fa-solid fa-shield" style="color: #00875a; margin-right: 8px;"></i> uc cover &nbsp; <span style="font-weight: 400;">Standard rate card</span>
                </div>

                <div class="vertical-options-list">
                    <!-- Option 1 -->
                    <div class="vertical-option-row">
                        <div class="vertical-option-info">
                            <h4>Exhaust/wall fan installation</h4>
                            <div class="option-rating"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.82 (5K reviews)</div>
                            <div class="option-price">₹248 &bull; <span style="color: #777; font-weight: 400;">10 mins</span></div>
                        </div>
                        <div class="vertical-option-media">
                            <img src="images/new_fan_installation_icon.jpg" alt="Installation">
                            <button onclick="addToCart('Exhaust/wall fan installation', 248); document.getElementById('exhaust-fan-modal').style.display='none';">Add</button>
                        </div>
                    </div>
                    <!-- Option 2 -->
                    <div class="vertical-option-row">
                        <div class="vertical-option-info">
                            <h4>Replacement</h4>
                            <div class="option-rating"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.87 (3K reviews)</div>
                            <div class="option-price">₹298 &bull; <span style="color: #777; font-weight: 400;">30 mins</span></div>
                        </div>
                        <div class="vertical-option-media">
                            <img src="images/new_fan_installation_icon.jpg" alt="Replacement">
                            <button onclick="addToCart('Exhaust fan replacement', 298); document.getElementById('exhaust-fan-modal').style.display='none';">Add</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
`;

if (!content.includes('id="ceiling-fan-modal"')) {
    content = content.replace('<!-- Cart Sidebar -->', modals + '\n    <!-- Cart Sidebar -->');
}

fs.writeFileSync('fan-installation', content);
