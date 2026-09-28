const fs = require('fs');
let content = fs.readFileSync('ac-service.html', 'utf8');

// 1. Replace the onclick for the Foam-jet AC service "Add" button
content = content.replace(
    `<button class="add-btn" style="padding: 8px 30px;">Add</button>`,
    `<button class="add-btn" style="padding: 8px 30px;" onclick="document.getElementById('foam-jet-modal').style.display='flex'">Add</button>`
);

const modalStyles = `
    .ac-options-carousel {
        display: flex;
        gap: 12px;
        overflow-x: auto;
        padding-bottom: 10px;
        scrollbar-width: none;
        scroll-behavior: smooth;
    }
    .ac-options-carousel::-webkit-scrollbar {
        display: none;
    }
    .ac-option-card {
        min-width: 140px;
        flex: 0 0 auto;
        border: 1px solid #eaeaea;
        border-radius: 8px;
        padding: 16px;
        background: #fff;
        position: relative;
    }
    .ac-option-card.bestseller {
        border: 1px solid #a855f7;
    }
    .bestseller-badge {
        position: absolute;
        top: -10px;
        left: 12px;
        background: #4b0082;
        color: white;
        font-size: 11px;
        font-weight: 600;
        padding: 2px 8px;
        border-radius: 4px;
    }
    .ac-option-title {
        font-size: 15px;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .ac-option-price-row {
        display: flex;
        align-items: baseline;
        gap: 6px;
        margin-bottom: 2px;
    }
    .ac-option-price {
        font-size: 14px;
        font-weight: 600;
    }
    .ac-option-strike {
        font-size: 12px;
        color: #888;
        text-decoration: line-through;
    }
    .ac-option-per-ac {
        font-size: 12px;
        color: #555;
        margin-bottom: 6px;
    }
    .ac-option-discount {
        font-size: 12px;
        color: #00875a;
        font-weight: 600;
        margin-bottom: 15px;
    }
    .ac-option-add {
        width: 100%;
        padding: 6px;
        background: #fff;
        border: 1px solid #e0e0e0;
        color: #a855f7;
        font-weight: 600;
        border-radius: 6px;
        cursor: pointer;
        font-size: 14px;
    }
    .ac-scroll-btn {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: white;
        border: 1px solid #eee;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        z-index: 5;
    }
    .ac-scroll-left { left: -15px; }
    .ac-scroll-right { right: -15px; }
`;

if (!content.includes('ac-options-carousel')) {
    content = content.replace('</style>', modalStyles + '\n    </style>');
}

const modalHTML = `
    <!-- Foam Jet Modal -->
    <div id="foam-jet-modal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); z-index: 1000; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf9; width: 100%; max-width: 500px; padding: 0; overflow: hidden; border-radius: 12px; position: relative;">
            
            <div style="position: relative; width: 100%; height: 160px; background: #e9e4dc;">
                <button class="modal-close" onclick="document.getElementById('foam-jet-modal').style.display='none'" style="position: absolute; z-index: 10; background: rgba(0,0,0,0.3); color: white; border: none; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; top: 15px; right: 15px; cursor: pointer;"><i class="fa-solid fa-xmark"></i></button>
                <div style="padding: 24px; position: relative; z-index: 2; height: 100%; display: flex; flex-direction: column; justify-content: center;">
                    <h2 style="font-size: 24px; font-weight: 700; margin: 0 0 5px 0;">Foam-jet<br>AC service</h2>
                    <p style="margin: 0; color: #555; font-size: 14px;">Deep cleans AC coils<br>for better cooling</p>
                </div>
                <img src="images/cleaning.jpg" style="position: absolute; right: 0; top: 0; height: 100%; width: 50%; object-fit: cover; border-top-right-radius: 12px;">
            </div>
            
            <div class="options-modal-body" style="padding: 24px;">
                <h3 class="options-modal-title" style="font-size: 20px; margin-bottom: 5px; font-weight: 700;">Foam-jet AC service</h3>
                <div class="options-rating" style="margin-bottom: 5px;"><i class="fa-solid fa-star" style="color: #6366f1;"></i> 4.75 <span style="color: #666; font-weight: 400; text-decoration: underline; text-decoration-style: dotted;">(2.9M reviews)</span></div>
                <div style="color: #00875a; font-weight: 600; font-size: 13px; margin-bottom: 20px;"><i class="fa-solid fa-tag"></i> Add more & save up to 25%</div>

                <div style="position: relative; margin-bottom: 10px;">
                    <button class="ac-scroll-btn ac-scroll-left" onclick="document.getElementById('ac-carousel').scrollBy(-150, 0)"><i class="fa-solid fa-arrow-left" style="font-size: 12px;"></i></button>
                    <button class="ac-scroll-btn ac-scroll-right" onclick="document.getElementById('ac-carousel').scrollBy(150, 0)"><i class="fa-solid fa-arrow-right" style="font-size: 12px;"></i></button>
                    
                    <div id="ac-carousel" class="ac-options-carousel">
                        
                        <!-- 1 AC -->
                        <div class="ac-option-card">
                            <div class="ac-option-title">1 AC</div>
                            <div class="ac-option-price-row">
                                <span class="ac-option-price">₹599</span>
                            </div>
                            <div class="ac-option-per-ac">&nbsp;</div>
                            <div class="ac-option-discount">&nbsp;</div>
                            <button class="ac-option-add" onclick="addToCart('Foam-jet AC service - 1 AC', 599); document.getElementById('foam-jet-modal').style.display='none';">Add</button>
                        </div>

                        <!-- 2 ACs -->
                        <div class="ac-option-card bestseller">
                            <div class="bestseller-badge">Bestseller</div>
                            <div class="ac-option-title">2 ACs</div>
                            <div class="ac-option-price-row">
                                <span class="ac-option-price">₹1098</span>
                                <span class="ac-option-strike">₹1198</span>
                            </div>
                            <div class="ac-option-per-ac">(₹549/AC)</div>
                            <div class="ac-option-discount">8% off</div>
                            <button class="ac-option-add" onclick="addToCart('Foam-jet AC service - 2 ACs', 1098); document.getElementById('foam-jet-modal').style.display='none';">Add</button>
                        </div>

                        <!-- 3 ACs -->
                        <div class="ac-option-card">
                            <div class="ac-option-title">3 ACs</div>
                            <div class="ac-option-price-row">
                                <span class="ac-option-price">₹1497</span>
                                <span class="ac-option-strike">₹1797</span>
                            </div>
                            <div class="ac-option-per-ac">(₹499/AC)</div>
                            <div class="ac-option-discount">17% off</div>
                            <button class="ac-option-add" onclick="addToCart('Foam-jet AC service - 3 ACs', 1497); document.getElementById('foam-jet-modal').style.display='none';">Add</button>
                        </div>

                        <!-- 4 ACs -->
                        <div class="ac-option-card">
                            <div class="ac-option-title">4 ACs</div>
                            <div class="ac-option-price-row">
                                <span class="ac-option-price">₹1796</span>
                                <span class="ac-option-strike">₹2396</span>
                            </div>
                            <div class="ac-option-per-ac">(₹449/AC)</div>
                            <div class="ac-option-discount">25% off</div>
                            <button class="ac-option-add" onclick="addToCart('Foam-jet AC service - 4 ACs', 1796); document.getElementById('foam-jet-modal').style.display='none';">Add</button>
                        </div>

                        <!-- 5 ACs -->
                        <div class="ac-option-card">
                            <div class="ac-option-title">5 ACs</div>
                            <div class="ac-option-price-row">
                                <span class="ac-option-price">₹2245</span>
                                <span class="ac-option-strike">₹2995</span>
                            </div>
                            <div class="ac-option-per-ac">(₹449/AC)</div>
                            <div class="ac-option-discount">25% off</div>
                            <button class="ac-option-add" onclick="addToCart('Foam-jet AC service - 5 ACs', 2245); document.getElementById('foam-jet-modal').style.display='none';">Add</button>
                        </div>

                        <!-- 6 ACs -->
                        <div class="ac-option-card">
                            <div class="ac-option-title">6 ACs</div>
                            <div class="ac-option-price-row">
                                <span class="ac-option-price">₹2694</span>
                                <span class="ac-option-strike">₹3594</span>
                            </div>
                            <div class="ac-option-per-ac">(₹449/AC)</div>
                            <div class="ac-option-discount">25% off</div>
                            <button class="ac-option-add" onclick="addToCart('Foam-jet AC service - 6 ACs', 2694); document.getElementById('foam-jet-modal').style.display='none';">Add</button>
                        </div>
                        
                        <!-- 7 ACs -->
                        <div class="ac-option-card">
                            <div class="ac-option-title">7 ACs</div>
                            <div class="ac-option-price-row">
                                <span class="ac-option-price">₹3143</span>
                                <span class="ac-option-strike">₹4193</span>
                            </div>
                            <div class="ac-option-per-ac">(₹449/AC)</div>
                            <div class="ac-option-discount">25% off</div>
                            <button class="ac-option-add" onclick="addToCart('Foam-jet AC service - 7 ACs', 3143); document.getElementById('foam-jet-modal').style.display='none';">Add</button>
                        </div>
                        
                        <!-- 8 ACs -->
                        <div class="ac-option-card">
                            <div class="ac-option-title">8 ACs</div>
                            <div class="ac-option-price-row">
                                <span class="ac-option-price">₹3592</span>
                                <span class="ac-option-strike">₹4792</span>
                            </div>
                            <div class="ac-option-per-ac">(₹449/AC)</div>
                            <div class="ac-option-discount">25% off</div>
                            <button class="ac-option-add" onclick="addToCart('Foam-jet AC service - 8 ACs', 3592); document.getElementById('foam-jet-modal').style.display='none';">Add</button>
                        </div>

                        <!-- 9 ACs -->
                        <div class="ac-option-card">
                            <div class="ac-option-title">9 ACs</div>
                            <div class="ac-option-price-row">
                                <span class="ac-option-price">₹4041</span>
                                <span class="ac-option-strike">₹5391</span>
                            </div>
                            <div class="ac-option-per-ac">(₹449/AC)</div>
                            <div class="ac-option-discount">25% off</div>
                            <button class="ac-option-add" onclick="addToCart('Foam-jet AC service - 9 ACs', 4041); document.getElementById('foam-jet-modal').style.display='none';">Add</button>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
`;

if (!content.includes('id="foam-jet-modal"')) {
    content = content.replace('<!-- Cart Sidebar -->', modalHTML + '\n    <!-- Cart Sidebar -->');
}

fs.writeFileSync('ac-service.html', content);
