import os

with open('common.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_logic = """// 24/7 Support Popup Logic
document.addEventListener('DOMContentLoaded', () => {
    const popupHtml = `
    <div class="support-popup-overlay" id="support-popup">
        <div class="support-popup-header">
            <h3 class="support-popup-title">🎧 24/7 Free Support</h3>
            <button class="support-popup-close" id="support-popup-close"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <p class="support-popup-text">
            Have any questions or doubts? Contact our 24/7 free support team for immediate assistance. Directly WhatsApp or Call us.
        </p>
        <div class="support-popup-buttons">
            <a href="tel:+919014380344" class="support-popup-btn btn-call">Call Now</a>
            <a href="https://wa.me/919014380344" target="_blank" class="support-popup-btn btn-whatsapp">WhatsApp</a>
        </div>
    </div>
    `;

    document.body.insertAdjacentHTML('beforeend', popupHtml);
    
    const popup = document.getElementById('support-popup');
    const closeBtn = document.getElementById('support-popup-close');

    // Show popup after 3 seconds
    setTimeout(() => {
        if (!sessionStorage.getItem('supportPopupClosed')) {
            popup.classList.add('show');
        }
    }, 3000);

    closeBtn.addEventListener('click', () => {
        popup.classList.remove('show');
        sessionStorage.setItem('supportPopupClosed', 'true');
    });
});"""

new_logic = """// 24/7 Support Footer Logic
document.addEventListener('DOMContentLoaded', () => {
    // Remove the old popup if it exists in HTML
    const oldPopup = document.getElementById('support-popup');
    if (oldPopup) oldPopup.remove();

    const supportHtml = `
    <div style="background: #ffffff; padding: 30px; border-radius: 12px; border: 1px solid #eaeaea; margin-top: 40px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
        <h3 style="font-size: 22px; font-weight: 800; margin-bottom: 12px; color: #111; display: flex; align-items: center; gap: 10px;">🎧 24/7 Free Support</h3>
        <p style="color: #555; font-size: 15px; margin-bottom: 20px; line-height: 1.6;">
            Have any questions or doubts? Contact our 24/7 free support team for immediate assistance. Directly WhatsApp or Call us.
        </p>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <a href="tel:+919014380344" style="flex: 1; min-width: 150px; background: #6366f1; color: #fff; padding: 14px 20px; text-align: center; border-radius: 8px; font-weight: 600; text-decoration: none; transition: 0.2s; font-size: 16px;" onmouseover="this.style.background='#4f46e5'" onmouseout="this.style.background='#6366f1'">Call Now</a>
            <a href="https://wa.me/919014380344" target="_blank" style="flex: 1; min-width: 150px; background: #25d366; color: #fff; padding: 14px 20px; text-align: center; border-radius: 8px; font-weight: 600; text-decoration: none; transition: 0.2s; font-size: 16px;" onmouseover="this.style.background='#1da851'" onmouseout="this.style.background='#25d366'">WhatsApp</a>
        </div>
    </div>
    `;

    // Insert into the footer
    const footer = document.querySelector('.footer');
    const footerBottom = document.querySelector('.footer-bottom');
    const citiesSection = document.getElementById('cities-section');
    
    if (footer) {
        const wrapper = document.createElement('div');
        wrapper.style.maxWidth = '1200px';
        wrapper.style.margin = '0 auto';
        wrapper.style.padding = '0 20px';
        wrapper.innerHTML = supportHtml;
        
        // Insert before cities section or footer-bottom
        if (citiesSection) {
            footer.insertBefore(wrapper, citiesSection);
        } else if (footerBottom) {
            footer.insertBefore(wrapper, footerBottom);
        } else {
            footer.appendChild(wrapper);
        }
    }
});"""

if old_logic in content:
    content = content.replace(old_logic, new_logic)
    with open('common.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully moved support to footer.")
else:
    print("Could not find the exact old logic block in common.js")
