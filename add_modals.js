const fs = require('fs');
let content = fs.readFileSync('fan-installation.html', 'utf8');

// 1. Replace the onclick for Decorative ceiling fan
content = content.replace(
    `<button class="add-btn" onclick="addToCart('Decorative ceiling fan installation/replacement',469)">Add</button>`,
    `<button class="add-btn" onclick="document.getElementById('decorative-fan-modal').style.display='flex'">Add</button>`
);

// 2. Replace the onclick for Smart fan
content = content.replace(
    `<button class="add-btn" onclick="addToCart('Smart fan installation/replacement',298)">Add</button>`,
    `<button class="add-btn" onclick="document.getElementById('smart-fan-modal').style.display='flex'">Add</button>`
);

const modalStyles = `
    .vertical-option-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 0;
        border-bottom: 1px solid #f0f0f0;
    }
    .vertical-option-row:last-child {
        border-bottom: none;
    }
    .vertical-option-info h4 {
        font-size: 15px;
        margin: 0 0 4px 0;
        font-weight: 600;
        color: #111;
    }
    .vertical-option-info .option-rating {
        font-size: 12px;
        color: #555;
        margin-bottom: 6px;
    }
    .vertical-option-info .option-price {
        font-size: 13px;
        font-weight: 600;
        color: #111;
    }
    .vertical-option-media {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        width: 100px;
    }
    .vertical-option-media img {
        width: 80px;
        height: 80px;
        border-radius: 8px;
        object-fit: cover;
        margin-bottom: -15px;
        z-index: 1;
        margin-right: 15px;
    }
    .vertical-option-media button {
        width: 70px;
        padding: 6px 0;
        background: white;
        border: 1px solid #e0e0e0;
        color: #6366f1;
        border-radius: 6px;
        font-weight: 600;
        font-size: 13px;
        cursor: pointer;
        z-index: 2;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-right: 20px;
    }
`;

if (!content.includes('vertical-option-row')) {
    content = content.replace('</style>', modalStyles + '\n    </style>');
}

const modals = `
    <!-- Decorative Fan Modal -->
    <div id="decorative-fan-modal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 1000; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf9; width: 100%; max-width: 500px; padding: 0; overflow: hidden; border-radius: 12px; position: relative;">
            <button class="modal-close" onclick="document.getElementById('decorative-fan-modal').style.display='none'" style="position: absolute; z-index: 10; background: white; border: none; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; top: 15px; right: 15px; cursor: pointer;"><i class="fa-solid fa-xmark"></i></button>
            
            <div class="options-modal-body" style="padding: 24px;">
                <h3 class="options-modal-title" style="font-size: 22px; margin-bottom: 5px; font-weight: 700;">Decorative ceiling fan installation/replacement</h3>
                <div class="options-rating" style="margin-bottom: 15px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.80 <span style="color: #666; font-weight: 400;">(473 reviews)</span></div>
                
                <div style="background: #fff9f0; padding: 12px; border-radius: 8px; margin-bottom: 20px; font-size: 13px; font-weight: 600; color: #333; display: flex; align-items: center;">
                    <i class="fa-solid fa-shield" style="color: #00875a; margin-right: 8px;"></i> uc cover &nbsp; <span style="font-weight: 400;">Standard rate card</span>
                </div>

                <div class="vertical-options-list">
                    <!-- Option 1 -->
                    <div class="vertical-option-row">
                        <div class="vertical-option-info">
                            <h4>Installation</h4>
                            <div class="option-rating"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.86 (298 reviews)</div>
                            <div class="option-price">₹469 &bull; <span style="color: #777; font-weight: 400;">10 mins</span></div>
                        </div>
                        <div class="vertical-option-media">
                            <img src="images/new_fan_installation_icon.jpg" alt="Installation">
                            <button onclick="addToCart('Decorative ceiling fan installation', 469); document.getElementById('decorative-fan-modal').style.display='none';">Add</button>
                        </div>
                    </div>
                    <!-- Option 2 -->
                    <div class="vertical-option-row">
                        <div class="vertical-option-info">
                            <h4>Replacement</h4>
                            <div class="option-rating"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.70 (175 reviews)</div>
                            <div class="option-price">₹519 &bull; <span style="color: #777; font-weight: 400;">10 mins</span></div>
                        </div>
                        <div class="vertical-option-media">
                            <img src="images/new_fan_installation_icon.jpg" alt="Replacement">
                            <button onclick="addToCart('Decorative ceiling fan replacement', 519); document.getElementById('decorative-fan-modal').style.display='none';">Add</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Smart Fan Modal -->
    <div id="smart-fan-modal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 1000; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf9; width: 100%; max-width: 500px; padding: 0; overflow: hidden; border-radius: 12px; position: relative;">
            <button class="modal-close" onclick="document.getElementById('smart-fan-modal').style.display='none'" style="position: absolute; z-index: 10; background: white; border: none; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; top: 15px; right: 15px; cursor: pointer;"><i class="fa-solid fa-xmark"></i></button>
            
            <div class="options-modal-body" style="padding: 24px;">
                <h3 class="options-modal-title" style="font-size: 22px; margin-bottom: 5px; font-weight: 700;">Smart fan installation/replacement</h3>
                <div class="options-rating" style="margin-bottom: 15px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.85 <span style="color: #666; font-weight: 400;">(10K reviews)</span></div>
                
                <div style="background: #fff9f0; padding: 12px; border-radius: 8px; margin-bottom: 20px; font-size: 13px; font-weight: 600; color: #333; display: flex; align-items: center;">
                    <i class="fa-solid fa-shield" style="color: #00875a; margin-right: 8px;"></i> uc cover &nbsp; <span style="font-weight: 400;">Standard rate card</span>
                </div>

                <div class="vertical-options-list">
                    <!-- Option 1 -->
                    <div class="vertical-option-row">
                        <div class="vertical-option-info">
                            <h4>Installation</h4>
                            <div class="option-rating"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.83 (6K reviews)</div>
                            <div class="option-price">₹298 &bull; <span style="color: #777; font-weight: 400;">10 mins</span></div>
                        </div>
                        <div class="vertical-option-media">
                            <button onclick="addToCart('Smart fan installation', 298); document.getElementById('smart-fan-modal').style.display='none';" style="margin-bottom:0; margin-right:20px;">Add</button>
                        </div>
                    </div>
                    <!-- Option 2 -->
                    <div class="vertical-option-row">
                        <div class="vertical-option-info">
                            <h4>Replacement</h4>
                            <div class="option-rating"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.88 (4K reviews)</div>
                            <div class="option-price">₹349 &bull; <span style="color: #777; font-weight: 400;">10 mins</span></div>
                        </div>
                        <div class="vertical-option-media">
                            <button onclick="addToCart('Smart fan replacement', 349); document.getElementById('smart-fan-modal').style.display='none';" style="margin-bottom:0; margin-right:20px;">Add</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
`;

if (!content.includes('id="decorative-fan-modal"')) {
    content = content.replace('<!-- Cart Sidebar -->', modals + '\n    <!-- Cart Sidebar -->');
}

fs.writeFileSync('fan-installation.html', content);
