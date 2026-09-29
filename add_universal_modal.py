import os

js_code = """
// -----------------------------------------------------------
// Universal "View Details" Modal System for Joamex
// -----------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
    // 1. Inject Modal HTML into the body if not exists
    if (!document.getElementById('universal-details-modal')) {
        const modalHTML = `
            <div id="universal-details-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 10000; align-items: center; justify-content: center; backdrop-filter: blur(5px);">
                <div style="background: white; width: 90%; max-width: 450px; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.2); animation: modalPop 0.3s ease-out; position: relative; max-height: 85vh; display: flex; flex-direction: column;">
                    <div style="padding: 20px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; background: #fdfaf6;">
                        <h3 id="udm-title" style="margin: 0; font-size: 18px; font-weight: 700; color: #111;">Service Details</h3>
                        <button onclick="document.getElementById('universal-details-modal').style.display='none'" style="background: none; border: none; font-size: 24px; color: #666; cursor: pointer; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">&times;</button>
                    </div>
                    <div style="padding: 20px; overflow-y: auto; flex: 1;">
                        <div style="background: #e8f5e9; color: #2e7d32; padding: 10px; border-radius: 8px; font-size: 13px; font-weight: 600; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;">
                            <i class="fa-solid fa-shield-halved"></i> 30-Day Joamex Guarantee | Verified Professionals
                        </div>
                        
                        <h4 style="margin: 0 0 12px 0; font-size: 16px; color: #333; display: flex; align-items: center;"><i class="fa-solid fa-circle-check" style="color: #4CAF50; margin-right: 8px; font-size: 18px;"></i> What's included</h4>
                        <ul id="udm-included" style="margin: 0 0 25px 0; padding-left: 20px; color: #555; font-size: 14px; line-height: 1.6;">
                            <li>Complete diagnostic and inspection</li>
                            <li>Basic cleaning of the service area</li>
                            <li>Tool and labor charges for basic fix</li>
                        </ul>
                        
                        <h4 style="margin: 0 0 12px 0; font-size: 16px; color: #333; display: flex; align-items: center;"><i class="fa-solid fa-circle-xmark" style="color: #f44336; margin-right: 8px; font-size: 18px;"></i> What's excluded</h4>
                        <ul id="udm-excluded" style="margin: 0 0 25px 0; padding-left: 20px; color: #555; font-size: 14px; line-height: 1.6;">
                            <li>Spare parts cost (will be quoted if needed)</li>
                            <li>Any major civil or masonry work</li>
                        </ul>
                        
                        <h4 style="margin: 0 0 12px 0; font-size: 16px; color: #333; display: flex; align-items: center;"><i class="fa-solid fa-list-ol" style="color: #2196F3; margin-right: 8px; font-size: 18px;"></i> Process</h4>
                        <ol id="udm-process" style="margin: 0 0 10px 0; padding-left: 20px; color: #555; font-size: 14px; line-height: 1.6;">
                            <li>Inspection & Issue Identification</li>
                            <li>Quotation for parts (if any)</li>
                            <li>Repair/Service Execution</li>
                            <li>Final Testing & Cleanup</li>
                        </ol>
                    </div>
                    <div style="padding: 15px 20px; border-top: 1px solid #eee; background: #fff; text-align: center;">
                        <button onclick="document.getElementById('universal-details-modal').style.display='none'" style="width: 100%; background: #000; color: #fff; border: none; padding: 14px; border-radius: 8px; font-weight: 700; font-size: 16px; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#333'" onmouseout="this.style.background='#000'">Got it</button>
                    </div>
                </div>
            </div>
            <style>
                @keyframes modalPop {
                    0% { opacity: 0; transform: scale(0.9) translateY(20px); }
                    100% { opacity: 1; transform: scale(1) translateY(0); }
                }
            </style>
        `;
        document.body.insertAdjacentHTML('beforeend', modalHTML);
    }

    // 2. Attach click events to all "View details" links
    const updateDetailsLinks = () => {
        document.querySelectorAll('a').forEach(link => {
            const text = link.textContent.toLowerCase();
            if (text.includes('view detail')) {
                // Check if we haven't attached listener yet
                if (!link.hasAttribute('data-modal-attached')) {
                    link.setAttribute('data-modal-attached', 'true');
                    link.addEventListener('click', function(e) {
                        e.preventDefault();
                        
                        // Try to find the service title near this button
                        let title = 'Service Details';
                        
                        // Strategy 1: It's inside .service-card-info -> h4
                        let cardInfo = this.closest('.service-card-info');
                        if (cardInfo) {
                            let h4 = cardInfo.querySelector('h4, h3');
                            if (h4) title = h4.textContent.trim();
                        } else {
                            // Strategy 2: It's inside .service-details or something, go up a few levels and find h3/h4
                            let parent = this.parentElement;
                            while (parent && parent.tagName !== 'BODY') {
                                let heading = parent.querySelector('h3, h4');
                                if (heading && heading !== this) {
                                    title = heading.textContent.trim();
                                    break;
                                }
                                parent = parent.parentElement;
                            }
                        }
                        
                        document.getElementById('udm-title').textContent = title;
                        
                        // Show modal
                        const modal = document.getElementById('universal-details-modal');
                        modal.style.display = 'flex';
                    });
                }
            }
        });
    };
    
    // Initial call
    updateDetailsLinks();
    
    // Re-run in case of dynamic injection
    setTimeout(updateDetailsLinks, 1000);
    setTimeout(updateDetailsLinks, 3000);
});
"""

with open('common.js', 'a', encoding='utf-8') as f:
    f.write('\n' + js_code)
print("Updated common.js with Universal View Details Modal")
