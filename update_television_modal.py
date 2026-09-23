import sys

with open('television.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_str = '    <!-- Single Door Refrigerator Modal -->'
end_str = '</body>'
idx_start = html.find(start_str)
idx_end = html.find(end_str)

if idx_start != -1 and idx_end != -1:
    new_content = '''    <!-- TV Check-up Modal -->
    <div id="tv-checkup-modal" class="modal-overlay hidden">
        <div class="modal-content options-modal-content" style="max-width: 500px; padding: 0; overflow: hidden; border-radius: 12px;">
            <button id="close-tv-checkup-modal-btn" class="modal-close" style="z-index: 10; background: white; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; top: 15px; right: 15px;"><i class="fa-solid fa-xmark"></i></button>
            <div class="options-modal-banner" style="position: relative; height: 200px;">
                <img src="images/real_33.jpg" alt="TV check-up" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            
            <div class="options-modal-body" style="padding: 20px;">
                <h3 class="options-modal-title" style="font-size: 22px; margin-bottom: 5px; font-weight: 700;">TV check-up</h3>
                <div class="options-rating" style="margin-bottom: 15px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.77 <span style="color: #666; font-weight: 400;">(164K reviews)</span></div>

                <div style="background: #f8f9fa; border-radius: 8px; padding: 12px 15px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; cursor: pointer; border: 1px solid #eee;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="color: #00875a; font-weight: 700; font-size: 14px;"><i class="fa-solid fa-shield-halved"></i> UC cover</span>
                        <span style="font-size: 13px; color: #444;">Standard rate card</span>
                    </div>
                    <i class="fa-solid fa-chevron-right" style="color: #666; font-size: 12px;"></i>
                </div>

                <div style="position: relative; margin: 0 -5px;">
                    <button id="scroll-left-tv-btn" style="position: absolute; left: -15px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-left" style="font-size: 14px;"></i></button>
                    <button id="scroll-right-tv-btn" style="position: absolute; right: -15px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; border-radius: 50%; background: white; border: 1px solid #eee; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 5;"><i class="fa-solid fa-arrow-right" style="font-size: 14px;"></i></button>
                    
                    <div id="modal-carousel-tv" class="wm-options-carousel" style="display: flex; gap: 15px; overflow-x: auto; padding-bottom: 10px; padding-left: 5px; padding-right: 5px; scrollbar-width: none; scroll-behavior: smooth;">
                    
                    <div class="option-card" style="min-width: 150px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px;">
                        <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px;">Display issue</h4>
                        <div class="option-rating" style="font-size: 12px; margin-bottom: 8px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.78 <span>(79K reviews)</span></div>
                        <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹249</div>
                        <button class="option-add-btn" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7d33ff; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                    </div>
                    
                    <div class="option-card" style="min-width: 150px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px;">
                        <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px;">Power issue</h4>
                        <div class="option-rating" style="font-size: 12px; margin-bottom: 8px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.76 <span>(23K reviews)</span></div>
                        <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹249</div>
                        <button class="option-add-btn" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7d33ff; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                    </div>

                    <div class="option-card" style="min-width: 150px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px;">
                        <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px;">Unknown issue</h4>
                        <div class="option-rating" style="font-size: 12px; margin-bottom: 8px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.77 <span>(41K reviews)</span></div>
                        <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹249</div>
                        <button class="option-add-btn" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7d33ff; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                    </div>

                    <div class="option-card" style="min-width: 150px; border: 1px solid #eee; border-radius: 8px; overflow: hidden; padding: 12px;">
                        <h4 style="font-size: 14px; margin-bottom: 5px; height: 34px;">Sound issue</h4>
                        <div class="option-rating" style="font-size: 12px; margin-bottom: 8px;"><i class="fa-solid fa-star" style="color: #7d33ff;"></i> 4.75 <span>(12K reviews)</span></div>
                        <div class="option-price" style="font-size: 14px; font-weight: 600; margin-bottom: 10px;">₹249</div>
                        <button class="option-add-btn" style="width: 100%; padding: 8px; background: #fff; border: 1px solid #e0e0e0; color: #7d33ff; font-weight: 600; border-radius: 8px; cursor: pointer;">Add</button>
                    </div>

                    </div>
                </div>
                <div style="margin-top: 20px;"><h3 style="font-size: 18px; font-weight: 700; margin-bottom: 15px;">Our process</h3></div>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            function setupModal(openBtnId, modalId, closeBtnId) {
                const openBtn = document.getElementById(openBtnId);
                const modal = document.getElementById(modalId);
                const closeBtn = document.getElementById(closeBtnId);

                if (openBtn && modal && closeBtn) {
                    openBtn.addEventListener('click', () => {
                        modal.classList.remove('hidden');
                    });
                    closeBtn.addEventListener('click', () => {
                        modal.classList.add('hidden');
                    });
                    modal.addEventListener('click', (e) => {
                        if (e.target === modal) {
                            modal.classList.add('hidden');
                        }
                    });
                }
            }

            setupModal('open-tv-checkup-modal-btn', 'tv-checkup-modal', 'close-tv-checkup-modal-btn');

            // Carousel Scrolling Logic for TV checkup
            const carousel = document.getElementById('modal-carousel-tv');
            const leftBtn = document.getElementById('scroll-left-tv-btn');
            const rightBtn = document.getElementById('scroll-right-tv-btn');

            if (carousel && leftBtn && rightBtn) {
                leftBtn.addEventListener('click', () => {
                    carousel.scrollBy({ left: -165, behavior: 'smooth' });
                });
                rightBtn.addEventListener('click', () => {
                    carousel.scrollBy({ left: 165, behavior: 'smooth' });
                });
            }
        });
    </script>
'''
    html = html[:idx_start] + new_content + html[idx_end:]
    with open('television.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Replaced Modal Content successfully')
else:
    print('Could not find start or end tags')
