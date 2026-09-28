css_code = """
/* 24/7 Support Popup */
.support-popup-overlay {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    max-width: 400px;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    z-index: 10000;
    padding: 20px;
    opacity: 0;
    visibility: hidden;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    transform: translate(-50%, 20px);
}
.support-popup-overlay.show {
    opacity: 1;
    visibility: visible;
    transform: translate(-50%, 0);
}
.support-popup-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}
.support-popup-title {
    font-size: 18px;
    font-weight: 700;
    color: #111;
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 0;
}
.support-popup-close {
    background: none;
    border: none;
    font-size: 16px;
    color: #999;
    cursor: pointer;
    padding: 0;
}
.support-popup-text {
    font-size: 13px;
    color: #666;
    line-height: 1.5;
    margin-bottom: 20px;
    margin-top: 0;
}
.support-popup-buttons {
    display: flex;
    gap: 10px;
}
.support-popup-btn {
    flex: 1;
    padding: 12px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    text-align: center;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: 0.3s;
    display: block;
}
.btn-call {
    background: #5a67d8;
    color: #fff;
}
.btn-call:hover {
    background: #4c51bf;
}
.btn-whatsapp {
    background: #48bb78;
    color: #fff;
}
.btn-whatsapp:hover {
    background: #38a169;
}
"""

js_code = """
// 24/7 Support Popup Logic
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
});
"""

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'a', encoding='utf-8') as f:
    f.write(css_code)

with open(r'c:\Users\Divyanshi123456\Music\hoamex\common.js', 'a', encoding='utf-8') as f:
    f.write(js_code)

print('Success')
