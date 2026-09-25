    <!-- Towel Holder Installation Modal -->
    <div id="towel-holder-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf6; width: 100%; max-width: 500px; padding: 20px; border-radius: 12px; position: relative; max-height: 90vh; overflow-y: auto;">
            <button id="close-towel-holder-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>
            
            <h3 class="options-modal-title" style="font-size: 24px; margin-bottom: 5px; font-weight: 700; color: #111;">Towel holder installation</h3>
            <div class="options-rating" style="margin-bottom: 25px; font-size: 13px; color: #555;"><i class="fa-solid fa-star" style="color: #111;"></i> 4.71 <span style="color: #777; font-weight: 400;">(15K reviews)</span></div>

            <div style="position: relative; margin: 0 -5px;">
                <button id="scroll-left-towel-btn" style="position: absolute; left: -10px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-left" style="font-size: 14px;"></i></button>
                <button id="scroll-right-towel-btn" style="position: absolute; right: -10px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-right" style="font-size: 14px;"></i></button>
                
                <div id="modal-carousel-towel" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; padding-left: 5px; padding-right: 5px; scrollbar-width: none; scroll-behavior: smooth;">
                
                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="images/accessories_icon.jpg" onerror="this.src='images/plumber.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">Towel rack</h4>
                    <div class="option-rating" style="font-size: 12px; margin-bottom: 8px;"><i class="fa-solid fa-star" style="color: #555;"></i> 4.75 <span style="color: #777;">(8K reviews)</span></div>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹149</div>
                    <button class="option-add-btn" onclick="addToCart('Towel rack installation',149)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>
                
                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="images/accessories_icon.jpg" onerror="this.src='images/plumber.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">Holding rod</h4>
                    <div class="option-rating" style="font-size: 12px; margin-bottom: 8px;"><i class="fa-solid fa-star" style="color: #555;"></i> 4.68 <span style="color: #777;">(4K reviews)</span></div>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹99</div>
                    <button class="option-add-btn" onclick="addToCart('Holding rod installation',99)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>

                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="images/accessories_icon.jpg" onerror="this.src='images/plumber.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">Small holder</h4>
                    <div class="option-rating" style="font-size: 12px; margin-bottom: 8px;"><i class="fa-solid fa-star" style="color: #555;"></i> 4.70 <span style="color: #777;">(3K reviews)</span></div>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹99</div>
                    <button class="option-add-btn" onclick="addToCart('Small holder installation',99)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>

                </div>
            </div>
        </div>
    </div>

    <style>
    .hidden { display: none !important; }
    .wm-options-carousel::-webkit-scrollbar { display: none; }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            function setupModal(openBtnId, modalId, closeBtnId, carouselId, leftBtnId, rightBtnId) {
                const openBtn = document.getElementById(openBtnId);
                const modal = document.getElementById(modalId);
                const closeBtn = document.getElementById(closeBtnId);

                if (openBtn && modal && closeBtn) {
                    openBtn.addEventListener('click', () => modal.classList.remove('hidden'));
                    closeBtn.addEventListener('click', () => modal.classList.add('hidden'));
                    modal.addEventListener('click', (e) => {
                        if (e.target === modal) modal.classList.add('hidden');
                    });
                }

                const carousel = document.getElementById(carouselId);
                const leftBtn = document.getElementById(leftBtnId);
                const rightBtn = document.getElementById(rightBtnId);

                if (carousel && leftBtn && rightBtn) {
                    leftBtn.addEventListener('click', () => carousel.scrollBy({ left: -175, behavior: 'smooth' }));
                    rightBtn.addEventListener('click', () => carousel.scrollBy({ left: 175, behavior: 'smooth' }));
                }
            }

            setupModal('open-tap-repair-modal-btn', 'tap-repair-modal', 'close-tap-repair-modal-btn', 'modal-carousel-tap', 'scroll-left-tap-btn', 'scroll-right-tap-btn');
            setupModal('open-tap-acc-modal-btn', 'tap-acc-modal', 'close-tap-acc-modal-btn', 'modal-carousel-acc', 'scroll-left-acc-btn', 'scroll-right-acc-btn');
            setupModal('open-tap-inst-modal-btn', 'tap-inst-modal', 'close-tap-inst-modal-btn', 'modal-carousel-inst', 'scroll-left-inst-btn', 'scroll-right-inst-btn');
            setupModal('open-jet-spray-modal-btn', 'jet-spray-modal', 'close-jet-spray-modal-btn', 'modal-carousel-jet', 'scroll-left-jet-btn', 'scroll-right-jet-btn');
            setupModal('open-flush-tank-modal-btn', 'flush-tank-modal', 'close-flush-tank-modal-btn', 'modal-carousel-flush', 'scroll-left-flush-btn', 'scroll-right-flush-btn');
            setupModal('open-indian-toilet-modal-btn', 'indian-toilet-modal', 'close-indian-toilet-modal-btn', 'modal-carousel-ind', 'scroll-left-ind-btn', 'scroll-right-ind-btn');
            setupModal('open-wall-mounted-modal-btn', 'wall-mounted-modal', 'close-wall-mounted-modal-btn', 'modal-carousel-wall', 'scroll-left-wall-btn', 'scroll-right-wall-btn');
            setupModal('open-floor-mounted-modal-btn', 'floor-mounted-modal', 'close-floor-mounted-modal-btn', 'modal-carousel-floor', 'scroll-left-floor-btn', 'scroll-right-floor-btn');
            setupModal('open-shower-inst-modal-btn', 'shower-inst-modal', 'close-shower-inst-modal-btn', 'modal-carousel-shower', 'scroll-left-shower-btn', 'scroll-right-shower-btn');
            setupModal('open-towel-holder-modal-btn', 'towel-holder-modal', 'close-towel-holder-modal-btn', 'modal-carousel-towel', 'scroll-left-towel-btn', 'scroll-right-towel-btn');
        });
    </script>
---NEXT---
    <style>
    .hidden { display: none !important; }
    .wm-options-carousel::-webkit-scrollbar { display: none; }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            function setupModal(openBtnId, modalId, closeBtnId, carouselId, leftBtnId, rightBtnId) {
                const openBtn = document.getElementById(openBtnId);
                const modal = document.getElementById(modalId);
                const closeBtn = document.getElementById(closeBtnId);

                if (openBtn && modal && closeBtn) {
                    openBtn.addEventListener('click', () => modal.classList.remove('hidden'));
                    closeBtn.addEventListener('click', () => modal.classList.add('hidden'));
                    modal.addEventListener('click', (e) => {
                        if (e.target === modal) modal.classList.add('hidden');
                    });
                }

                const carousel = document.getElementById(carouselId);
                const leftBtn = document.getElementById(leftBtnId);
                const rightBtn = document.getElementById(rightBtnId);

                if (carousel && leftBtn && rightBtn) {
                    leftBtn.addEventListener('click', () => carousel.scrollBy({ left: -175, behavior: 'smooth' }));
                    rightBtn.addEventListener('click', () => carousel.scrollBy({ left: 175, behavior: 'smooth' }));
                }
            }

            setupModal('open-tap-repair-modal-btn', 'tap-repair-modal', 'close-tap-repair-modal-btn', 'modal-carousel-tap', 'scroll-left-tap-btn', 'scroll-right-tap-btn');
            setupModal('open-tap-acc-modal-btn', 'tap-acc-modal', 'close-tap-acc-modal-btn', 'modal-carousel-acc', 'scroll-left-acc-btn', 'scroll-right-acc-btn');
            setupModal('open-tap-inst-modal-btn', 'tap-inst-modal', 'close-tap-inst-modal-btn', 'modal-carousel-inst', 'scroll-left-inst-btn', 'scroll-right-inst-btn');
            setupModal('open-jet-spray-modal-btn', 'jet-spray-modal', 'close-jet-spray-modal-btn', 'modal-carousel-jet', 'scroll-left-jet-btn', 'scroll-right-jet-btn');
            setupModal('open-flush-tank-modal-btn', 'flush-tank-modal', 'close-flush-tank-modal-btn', 'modal-carousel-flush', 'scroll-left-flush-btn', 'scroll-right-flush-btn');
            setupModal('open-indian-toilet-modal-btn', 'indian-toilet-modal', 'close-indian-toilet-modal-btn', 'modal-carousel-ind', 'scroll-left-ind-btn', 'scroll-right-ind-btn');
            setupModal('open-wall-mounted-modal-btn', 'wall-mounted-modal', 'close-wall-mounted-modal-btn', 'modal-carousel-wall', 'scroll-left-wall-btn', 'scroll-right-wall-btn');
            setupModal('open-floor-mounted-modal-btn', 'floor-mounted-modal', 'close-floor-mounted-modal-btn', 'modal-carousel-floor', 'scroll-left-floor-btn', 'scroll-right-floor-btn');
            setupModal('open-shower-inst-modal-btn', 'shower-inst-modal', 'close-shower-inst-modal-btn', 'modal-carousel-shower', 'scroll-left-shower-btn', 'scroll-right-shower-btn');
        });
    </script>
---NEXT---
    <!-- Waste Coupling Modal -->
    <div id="waste-coupling-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">
        <div class="modal-content options-modal-content" style="background: #fcfbf6; width: 100%; max-width: 500px; padding: 20px; border-radius: 12px; position: relative; max-height: 90vh; overflow-y: auto;">
            <button id="close-waste-coupling-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>
            
            <h3 class="options-modal-title" style="font-size: 24px; margin-bottom: 5px; font-weight: 700; color: #111;">Waste coupling installation</h3>
            <div class="options-rating" style="margin-bottom: 25px; font-size: 13px; color: #555;"><i class="fa-solid fa-star" style="color: #111;"></i> 4.81 <span style="color: #777; font-weight: 400;">(12K reviews)</span></div>

            <div style="position: relative; margin: 0 -5px;">
                <button id="scroll-left-waste-btn" style="position: absolute; left: -10px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-left" style="font-size: 14px;"></i></button>
                <button id="scroll-right-waste-btn" style="position: absolute; right: -10px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-right" style="font-size: 14px;"></i></button>
                
                <div id="modal-carousel-waste" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; padding-left: 5px; padding-right: 5px; scrollbar-width: none; scroll-behavior: smooth;">
                
                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="images/basin_icon.jpg" onerror="this.src='images/plumber.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">Bottle trap basin</h4>
                    <div class="option-rating" style="font-size: 12px; margin-bottom: 8px;"><i class="fa-solid fa-star" style="color: #555;"></i> 4.79 <span style="color: #777;">(2K reviews)</span></div>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹219</div>
                    <button class="option-add-btn" onclick="addToCart('Bottle trap basin',219)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>
                
                <div class="option-card" style="min-width: 160px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px; background: #fff8ee;">
                    <img src="images/basin_icon.jpg" onerror="this.src='images/plumber.jpg'" style="width: 100%; height: 90px; object-fit: contain; margin-bottom: 10px;">
                    <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px; color: #111;">Waste pipe basin</h4>
                    <div class="option-rating" style="font-size: 12px; margin-bottom: 8px;"><i class="fa-solid fa-star" style="color: #555;"></i> 4.81 <span style="color: #777;">(9K reviews)</span></div>
                    <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹149</div>
                    <button class="option-add-btn" onclick="addToCart('Waste pipe basin',149)" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7b1fa2; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                </div>

                </div>
            </div>
        </div>
    </div>

    <style>
    .hidden { display: none !important; }
    .wm-options-carousel::-webkit-scrollbar { display: none; }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            function setupModal(openBtnId, modalId, closeBtnId, carouselId, leftBtnId, rightBtnId) {
                const openBtn = document.getElementById(openBtnId);
                const modal = document.getElementById(modalId);
                const closeBtn = document.getElementById(closeBtnId);

                if (openBtn && modal && closeBtn) {
                    openBtn.addEventListener('click', () => modal.classList.remove('hidden'));
                    closeBtn.addEventListener('click', () => modal.classList.add('hidden'));
                    modal.addEventListener('click', (e) => {
                        if (e.target === modal) modal.classList.add('hidden');
                    });
                }

                const carousel = document.getElementById(carouselId);
                const leftBtn = document.getElementById(leftBtnId);
                const rightBtn = document.getElementById(rightBtnId);

                if (carousel && leftBtn && rightBtn) {
                    leftBtn.addEventListener('click', () => carousel.scrollBy({ left: -175, behavior: 'smooth' }));
                    rightBtn.addEventListener('click', () => carousel.scrollBy({ left: 175, behavior: 'smooth' }));
                }
            }

            setupModal('open-tap-repair-modal-btn', 'tap-repair-modal', 'close-tap-repair-modal-btn', 'modal-carousel-tap', 'scroll-left-tap-btn', 'scroll-right-tap-btn');
            setupModal('open-tap-acc-modal-btn', 'tap-acc-modal', 'close-tap-acc-modal-btn', 'modal-carousel-acc', 'scroll-left-acc-btn', 'scroll-right-acc-btn');
            setupModal('open-tap-inst-modal-btn', 'tap-inst-modal', 'close-tap-inst-modal-btn', 'modal-carousel-inst', 'scroll-left-inst-btn', 'scroll-right-inst-btn');
            setupModal('open-jet-spray-modal-btn', 'jet-spray-modal', 'close-jet-spray-modal-btn', 'modal-carousel-jet', 'scroll-left-jet-btn', 'scroll-right-jet-btn');
            setupModal('open-flush-tank-modal-btn', 'flush-tank-modal', 'close-flush-tank-modal-btn', 'modal-carousel-flush', 'scroll-left-flush-btn', 'scroll-right-flush-btn');
            setupModal('open-indian-toilet-modal-btn', 'indian-toilet-modal', 'close-indian-toilet-modal-btn', 'modal-carousel-ind', 'scroll-left-ind-btn', 'scroll-right-ind-btn');
            setupModal('open-wall-mounted-modal-btn', 'wall-mounted-modal', 'close-wall-mounted-modal-btn', 'modal-carousel-wall', 'scroll-left-wall-btn', 'scroll-right-wall-btn');
            setupModal('open-floor-mounted-modal-btn', 'floor-mounted-modal', 'close-floor-mounted-modal-btn', 'modal-carousel-floor', 'scroll-left-floor-btn', 'scroll-right-floor-btn');
            setupModal('open-shower-inst-modal-btn', 'shower-inst-modal', 'close-shower-inst-modal-btn', 'modal-carousel-shower', 'scroll-left-shower-btn', 'scroll-right-shower-btn');
            setupModal('open-towel-holder-modal-btn', 'towel-holder-modal', 'close-towel-holder-modal-btn', 'modal-carousel-towel', 'scroll-left-towel-btn', 'scroll-right-towel-btn');
            setupModal('open-shelf-inst-modal-btn', 'shelf-inst-modal', 'close-shelf-inst-modal-btn', 'modal-carousel-shelf', 'scroll-left-shelf-btn', 'scroll-right-shelf-btn');
            setupModal('open-basin-leak-modal-btn', 'basin-leak-modal', 'close-basin-leak-modal-btn', 'modal-carousel-basin-leak', 'scroll-left-basin-leak-btn', 'scroll-right-basin-leak-btn');
            setupModal('open-waste-coupling-modal-btn', 'waste-coupling-modal', 'close-waste-coupling-modal-btn', 'modal-carousel-waste', 'scroll-left-waste-btn', 'scroll-right-waste-btn');
        });
    </script>
---NEXT---
    <style>
    .hidden { display: none !important; }
    .wm-options-carousel::-webkit-scrollbar { display: none; }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            function setupModal(openBtnId, modalId, closeBtnId, carouselId, leftBtnId, rightBtnId) {
                const openBtn = document.getElementById(openBtnId);
                const modal = document.getElementById(modalId);
                const closeBtn = document.getElementById(closeBtnId);

                if (openBtn && modal && closeBtn) {
                    openBtn.addEventListener('click', () => modal.classList.remove('hidden'));
                    closeBtn.addEventListener('click', () => modal.classList.add('hidden'));
                    modal.addEventListener('click', (e) => {
                        if (e.target === modal) modal.classList.add('hidden');
                    });
                }

                const carousel = document.getElementById(carouselId);
                const leftBtn = document.getElementById(leftBtnId);
                const rightBtn = document.getElementById(rightBtnId);

                if (carousel && leftBtn && rightBtn) {
                    leftBtn.addEventListener('click', () => carousel.scrollBy({ left: -175, behavior: 'smooth' }));
                    rightBtn.addEventListener('click', () => carousel.scrollBy({ left: 175, behavior: 'smooth' }));
                }
            }

            setupModal('open-tap-repair-modal-btn', 'tap-repair-modal', 'close-tap-repair-modal-btn', 'modal-carousel-tap', 'scroll-left-tap-btn', 'scroll-right-tap-btn');
            setupModal('open-tap-acc-modal-btn', 'tap-acc-modal', 'close-tap-acc-modal-btn', 'modal-carousel-acc', 'scroll-left-acc-btn', 'scroll-right-acc-btn');
            setupModal('open-tap-inst-modal-btn', 'tap-inst-modal', 'close-tap-inst-modal-btn', 'modal-carousel-inst', 'scroll-left-inst-btn', 'scroll-right-inst-btn');
            setupModal('open-jet-spray-modal-btn', 'jet-spray-modal', 'close-jet-spray-modal-btn', 'modal-carousel-jet', 'scroll-left-jet-btn', 'scroll-right-jet-btn');
            setupModal('open-flush-tank-modal-btn', 'flush-tank-modal', 'close-flush-tank-modal-btn', 'modal-carousel-flush', 'scroll-left-flush-btn', 'scroll-right-flush-btn');
            setupModal('open-indian-toilet-modal-btn', 'indian-toilet-modal', 'close-indian-toilet-modal-btn', 'modal-carousel-ind', 'scroll-left-ind-btn', 'scroll-right-ind-btn');
            setupModal('open-wall-mounted-modal-btn', 'wall-mounted-modal', 'close-wall-mounted-modal-btn', 'modal-carousel-wall', 'scroll-left-wall-btn', 'scroll-right-wall-btn');
            setupModal('open-floor-mounted-modal-btn', 'floor-mounted-modal', 'close-floor-mounted-modal-btn', 'modal-carousel-floor', 'scroll-left-floor-btn', 'scroll-right-floor-btn');
            setupModal('open-shower-inst-modal-btn', 'shower-inst-modal', 'close-shower-inst-modal-btn', 'modal-carousel-shower', 'scroll-left-shower-btn', 'scroll-right-shower-btn');
            setupModal('open-towel-holder-modal-btn', 'towel-holder-modal', 'close-towel-holder-modal-btn', 'modal-carousel-towel', 'scroll-left-towel-btn', 'scroll-right-towel-btn');
            setupModal('open-shelf-inst-modal-btn', 'shelf-inst-modal', 'close-shelf-inst-modal-btn', 'modal-carousel-shelf', 'scroll-left-shelf-btn', 'scroll-right-shelf-btn');
            setupModal('open-basin-leak-modal-btn', 'basin-leak-modal', 'close-basin-leak-modal-btn', 'modal-carousel-basin-leak', 'scroll-left-basin-leak-btn', 'scroll-right-basin-leak-btn');
        });
    </script>
---NEXT---
python -c "
import json
with open(r'C:\Users\Divyanshi123456\.gemini\antigravity-ide\brain\3801f661-c7a3-437b-b9c2-dc560cdd437d\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if 'def setupModal(' in line or 'tap-repair-modal' in line:
            obj = json.loads(line)
            if 'tool_calls' in obj:
                for call in obj['tool_calls']:
                    args = call.get('args', {})
                    for val in args.values():
                        if isinstance(val, str) and 'tap-repair-modal' in val:
                            with open('recovered_script.py', 'a', encoding='utf-8') as out:
                                out.write(val + '\n---NEXT---\n')
"
---NEXT---
