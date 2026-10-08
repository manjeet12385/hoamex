const fs = require('fs');
let content = fs.readFileSync('bathroom-cleaning', 'utf8');

// 1. Add onclick to the Balcony cleaning Add button
content = content.replace(
    `<button style="position: absolute; bottom: -15px; left: 50%; transform: translateX(-50%); background: #fff; color: #7c3aed; font-weight: 600; padding: 8px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.05); z-index: 2;">Add</button>`,
    `<button onclick="document.getElementById('balcony-modal').style.display='flex'" style="position: absolute; bottom: -15px; left: 50%; transform: translateX(-50%); background: #fff; color: #7c3aed; font-weight: 600; padding: 8px 30px; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 14px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.05); z-index: 2;">Add</button>`
);

// We'll reuse the ac-options-carousel style logic
const modalStyles = `
    .balcony-options-carousel {
        display: flex;
        gap: 15px;
        overflow-x: auto;
        padding-bottom: 10px;
        scrollbar-width: none;
        scroll-behavior: smooth;
    }
    .balcony-options-carousel::-webkit-scrollbar {
        display: none;
    }
    .balcony-option-card {
        min-width: 160px;
        flex: 1;
        border: 1px solid #eaeaea;
        border-radius: 8px;
        padding: 12px;
        background: #fff;
        display: flex;
        flex-direction: column;
    }
    .balcony-option-img {
        width: 100%;
        height: 100px;
        border-radius: 6px;
        object-fit: cover;
        margin-bottom: 10px;
    }
    .balcony-option-title {
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 5px;
        color: #111;
        line-height: 1.3;
        height: 36px; /* reserve space for 2 lines */
    }
    .balcony-option-rating {
        font-size: 12px;
        color: #555;
        margin-bottom: 8px;
    }
    .balcony-option-price {
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 15px;
        color: #111;
    }
    .balcony-option-add {
        width: 100%;
        padding: 8px;
        background: #fff;
        border: 1px solid #e0e0e0;
        color: #a855f7;
        font-weight: 600;
        border-radius: 6px;
        cursor: pointer;
        font-size: 14px;
        margin-top: auto;
    }
`;

if (!content.includes('balcony-options-carousel')) {
    content = content.replace('</style>', modalStyles + '\n    </style>');
}

const modalHTML = `
    <!-- Balcony Modal -->
    <div id="balcony-modal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 1000; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf9; width: 100%; max-width: 500px; padding: 0; overflow: hidden; border-radius: 12px; position: relative;">
            
            <div style="position: relative; width: 100%; height: 180px; background: #333;">
                <button class="modal-close" onclick="document.getElementById('balcony-modal').style.display='none'" style="position: absolute; z-index: 10; background: rgba(0,0,0,0.3); color: white; border: none; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; top: 15px; right: 15px; cursor: pointer;"><i class="fa-solid fa-xmark"></i></button>
                <img src="images/cleaning.jpg" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.6;">
                <div style="padding: 24px; position: relative; z-index: 2; height: 100%; display: flex; flex-direction: column; justify-content: center; color: white;">
                    <h2 style="font-size: 24px; font-weight: 700; margin: 0 0 8px 0; text-shadow: 0 1px 3px rgba(0,0,0,0.8);">A deeper clean<br>for your balcony</h2>
                    <p style="margin: 0; font-size: 14px; opacity: 0.9; text-shadow: 0 1px 2px rgba(0,0,0,0.8);">Remove built-up dirt with<br>machine scrubbing</p>
                </div>
            </div>
            
            <div class="options-modal-body" style="padding: 24px;">
                <h3 class="options-modal-title" style="font-size: 20px; margin-bottom: 5px; font-weight: 700;">Balcony cleaning</h3>
                <div class="options-rating" style="margin-bottom: 20px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.80 <span style="color: #666; font-weight: 400; text-decoration: underline; text-decoration-style: dotted;">(60K reviews)</span></div>

                <div style="position: relative; margin-bottom: 10px;">
                    <button class="ac-scroll-btn ac-scroll-right" style="position: absolute; top: 50%; right: -15px; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;" onclick="document.getElementById('balcony-carousel').scrollBy(150, 0)"><i class="fa-solid fa-arrow-right" style="font-size: 12px;"></i></button>
                    
                    <div id="balcony-carousel" class="balcony-options-carousel">
                        
                        <!-- Small -->
                        <div class="balcony-option-card">
                            <img src="images/cleaning.jpg" class="balcony-option-img" alt="Small Balcony">
                            <div class="balcony-option-title">Small (Up to 6 ft<br>long)</div>
                            <div class="balcony-option-rating"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.80 <span style="color: #666;">(46K reviews)</span></div>
                            <div class="balcony-option-price">₹549</div>
                            <button class="balcony-option-add" onclick="addToCart('Balcony cleaning - Small', 549); document.getElementById('balcony-modal').style.display='none';">Add</button>
                        </div>

                        <!-- Large -->
                        <div class="balcony-option-card">
                            <img src="images/cleaning.jpg" class="balcony-option-img" alt="Large Balcony">
                            <div class="balcony-option-title">Large (Up to 20 ft<br>long)</div>
                            <div class="balcony-option-rating"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.79 <span style="color: #666;">(15K reviews)</span></div>
                            <div class="balcony-option-price">₹799</div>
                            <button class="balcony-option-add" onclick="addToCart('Balcony cleaning - Large', 799); document.getElementById('balcony-modal').style.display='none';">Add</button>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
`;

if (!content.includes('id="balcony-modal"')) {
    content = content.replace('<!-- Cart Sidebar -->', modalHTML + '\n    <!-- Cart Sidebar -->');
}

fs.writeFileSync('bathroom-cleaning', content);
