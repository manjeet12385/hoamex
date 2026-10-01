import os

with open('common.js', 'r', encoding='utf-8') as f:
    content = f.read()

modal_html = """
// -----------------------------------------------------------
// Partner Login Modal System
// -----------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
    // 1. Inject Modal HTML into the body if not exists
    if (!document.getElementById('partner-login-modal')) {
        const modalHTML = `
            <div id="partner-login-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 10000; align-items: center; justify-content: center; backdrop-filter: blur(5px);">
                <div style="background: #0d1117; width: 90%; max-width: 900px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.5); animation: modalPop 0.3s ease-out; position: relative; display: flex; flex-direction: row; height: 500px;">
                    
                    <button id="close-partner-modal" style="position: absolute; top: 15px; right: 15px; background: rgba(255,255,255,0.1); border: none; border-radius: 50%; font-size: 18px; color: #fff; cursor: pointer; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; z-index: 10;">&times;</button>
                    
                    <!-- Left Side -->
                    <div style="flex: 1; background: linear-gradient(135deg, #091316 0%, #060a0d 100%); padding: 40px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; border-right: 1px solid rgba(255,255,255,0.05);">
                        <div style="margin-bottom: 30px; position: relative;">
                            <!-- Mock graphic for the green layers -->
                            <div style="width: 150px; height: 150px; position: relative;">
                                <div style="position: absolute; top: 20%; left: 15%; width: 70%; height: 70%; border: 2px solid #1a5d3c; transform: rotateX(60deg) rotateZ(-45deg); border-radius: 8px; box-shadow: 0 0 20px rgba(26,93,60,0.3);"></div>
                                <div style="position: absolute; top: 35%; left: 15%; width: 70%; height: 70%; border: 2px solid #1f8a55; transform: rotateX(60deg) rotateZ(-45deg); border-radius: 8px; box-shadow: 0 0 30px rgba(31,138,85,0.4);"></div>
                                <div style="position: absolute; top: 50%; left: 15%; width: 70%; height: 70%; border: 2px solid #23a566; transform: rotateX(60deg) rotateZ(-45deg); border-radius: 8px; box-shadow: 0 0 40px rgba(35,165,102,0.5);"></div>
                                <div style="position: absolute; top: 35%; left: 40%; width: 30px; height: 40px; background: rgba(35,165,102,0.2); backdrop-filter: blur(4px); border-radius: 6px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(35,165,102,0.5); z-index: 5;">
                                    <i class="fa-solid fa-user" style="color: #23a566; font-size: 14px;"></i>
                                </div>
                            </div>
                        </div>
                        <h2 style="color: #fff; font-size: 28px; font-weight: 700; margin: 0 0 15px 0;">Partner Portal</h2>
                        <p style="color: #8b949e; font-size: 14px; line-height: 1.6; max-width: 280px; margin: 0;">Manage your service business, track earnings, and deliver excellence with our professional toolkit.</p>
                    </div>
                    
                    <!-- Right Side -->
                    <div style="flex: 1.2; background: #0a0c10; padding: 50px 40px; display: flex; flex-direction: column; justify-content: center;">
                        <h3 style="color: #fff; font-size: 24px; font-weight: 700; margin: 0 0 10px 0;">Partner Login</h3>
                        <p style="color: #8b949e; font-size: 14px; margin: 0 0 30px 0;">Enter your details for quick OTP access to your workspace.</p>
                        
                        <div style="margin-bottom: 20px;">
                            <label style="display: block; color: #fff; font-size: 12px; font-weight: 600; margin-bottom: 8px;">Email Address</label>
                            <input type="email" placeholder="partner@business.com" style="width: 100%; padding: 14px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box; transition: 0.2s;" onfocus="this.style.borderColor='#5e35b1'" onblur="this.style.borderColor='#30363d'">
                        </div>
                        
                        <button id="partner-otp-btn" style="width: 100%; background: #5e35b1; color: #fff; border: none; padding: 14px; border-radius: 8px; font-weight: 600; font-size: 14px; cursor: pointer; transition: 0.2s; margin-bottom: 25px;" onmouseover="this.style.background='#6e45c1'" onmouseout="this.style.background='#5e35b1'">Get OTP Code &rarr;</button>
                        
                        <div style="background: rgba(22,27,34,0.5); border: 1px solid #30363d; border-radius: 8px; padding: 15px; display: flex; gap: 15px; align-items: flex-start; margin-bottom: 30px;">
                            <div style="background: #23a566; color: #fff; width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 10px; margin-top: 2px; flex-shrink: 0;"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <h4 style="color: #fff; font-size: 13px; font-weight: 600; margin: 0 0 5px 0;">Instant Access</h4>
                                <p style="color: #8b949e; font-size: 12px; margin: 0; line-height: 1.5;">Secure login via one-time passcodes. No passwords required.</p>
                            </div>
                        </div>
                        
                        <div style="text-align: center; margin-bottom: 20px;">
                            <p style="color: #8b949e; font-size: 13px; margin: 0;">New Partner? <a href="partner.html" style="color: #58a6ff; text-decoration: none; font-weight: 600;">Apply Now</a></p>
                        </div>
                        
                        <div style="text-align: center; margin-top: auto;">
                            <span style="color: #484f58; font-size: 11px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase;"><i class="fa-solid fa-shield-halved"></i> PARTNER SECURITY 2.0</span>
                        </div>
                    </div>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', modalHTML);
    }
    
    // 2. Attach click events to partner buttons
    const attachPartnerModalEvents = () => {
        document.querySelectorAll('.partner-btn').forEach(btn => {
            if (!btn.hasAttribute('data-partner-modal-attached')) {
                btn.setAttribute('data-partner-modal-attached', 'true');
                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    document.getElementById('partner-login-modal').style.display = 'flex';
                });
            }
        });
        
        const closeBtn = document.getElementById('close-partner-modal');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                document.getElementById('partner-login-modal').style.display = 'none';
            });
        }

        const otpBtn = document.getElementById('partner-otp-btn');
        if (otpBtn && !otpBtn.hasAttribute('data-otp-attached')) {
            otpBtn.setAttribute('data-otp-attached', 'true');
            otpBtn.addEventListener('click', () => {
                const emailInput = otpBtn.previousElementSibling.querySelector('input');
                if (emailInput && emailInput.value) {
                    alert('OTP has been sent to ' + emailInput.value);
                } else {
                    alert('Please enter a valid email address first.');
                }
            });
        }
    };
    
    attachPartnerModalEvents();
    
    // Re-run in case of dynamic injection
    setTimeout(attachPartnerModalEvents, 1000);
});
"""

if "Partner Login Modal System" not in content:
    with open('common.js', 'a', encoding='utf-8') as f:
        f.write("\n" + modal_html)
