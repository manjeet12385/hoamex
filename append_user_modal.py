with open('common.js', 'a', encoding='utf-8') as f:
    f.write('''

// User Login Modal System
function injectUserModal() {
    if (!document.getElementById('user-login-modal')) {
        const modalHTML = `
            <div id="user-login-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 10000; align-items: center; justify-content: center; backdrop-filter: blur(5px);">
                <div style="background: #0d1117; width: 400px; border-radius: 16px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.4); border: 1px solid #30363d; position: relative; font-family: 'Inter', sans-serif;">
                    <button id="close-user-modal" style="position: absolute; top: 15px; right: 15px; background: transparent; border: none; color: #8b949e; font-size: 20px; cursor: pointer; transition: 0.2s; z-index: 10;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#8b949e'">&times;</button>
                    
                    <div style="padding: 40px 30px;">
                        <!-- Step 1: Login -->
                        <div id="user-login-step" style="display: flex; flex-direction: column; height: 100%; justify-content: center;">
                            <h3 style="color: #fff; font-size: 24px; font-weight: 700; margin: 0 0 10px 0;">Customer Login</h3>
                            <p style="color: #8b949e; font-size: 14px; margin: 0 0 30px 0; line-height: 1.5;">Enter your phone number to view your bookings.</p>
                            
                            <div style="margin-bottom: 25px; position: relative;">
                                <div style="position: absolute; top: 15px; left: 15px; color: #8b949e; font-weight: 600;">+91</div>
                                <input type="text" id="user-phone-input" placeholder="Enter mobile number" style="width: 100%; background: #161b22; border: 1px solid #30363d; padding: 14px 15px 14px 50px; border-radius: 8px; color: #fff; font-size: 15px; outline: none; transition: 0.2s; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                            </div>
                            
                            <button id="user-otp-btn" style="width: 100%; background: #4a3aff; color: #fff; border: none; padding: 14px; border-radius: 8px; font-weight: 600; font-size: 15px; cursor: pointer; transition: 0.2s; margin-bottom: 20px;" onmouseover="this.style.background='#3d2fd1'" onmouseout="this.style.background='#4a3aff'">Send OTP</button>
                        </div>

                        <!-- Step 2: OTP Verify -->
                        <div id="user-otp-step" style="display: none; flex-direction: column; height: 100%; justify-content: center;">
                            <a href="#" id="user-back-to-login" style="color: #8b949e; text-decoration: none; font-size: 13px; margin-bottom: 20px; display: inline-block;">&larr; Back</a>
                            <h3 style="color: #fff; font-size: 24px; font-weight: 700; margin: 0 0 10px 0;">Verify Phone</h3>
                            <p style="color: #8b949e; font-size: 14px; margin: 0 0 30px 0;">Code sent to <span id="user-otp-sent-phone" style="color: #fff;"></span></p>
                            
                            <div style="display: flex; gap: 10px; margin-bottom: 30px; justify-content: space-between;">
                                <input type="text" maxlength="1" class="user-otp-box" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none;">
                                <input type="text" maxlength="1" class="user-otp-box" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none;">
                                <input type="text" maxlength="1" class="user-otp-box" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none;">
                                <input type="text" maxlength="1" class="user-otp-box" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none;">
                            </div>

                            <button id="user-verify-otp-btn" style="width: 100%; background: #4a3aff; color: #fff; border: none; padding: 14px; border-radius: 8px; font-weight: 600; font-size: 15px; cursor: pointer; transition: 0.2s;">Verify & Login</button>
                        </div>
                    </div>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', modalHTML);
    }
    
    // Attach events
    const loginBtn = document.getElementById('user-login-btn');
    if(loginBtn) {
        loginBtn.onclick = () => document.getElementById('user-login-modal').style.display = 'flex';
    }
    const closeBtn = document.getElementById('close-user-modal');
    if(closeBtn) {
        closeBtn.onclick = () => document.getElementById('user-login-modal').style.display = 'none';
    }
    const sendOtp = document.getElementById('user-otp-btn');
    if(sendOtp) {
        sendOtp.onclick = () => {
            const phone = document.getElementById('user-phone-input').value;
            if(phone.length >= 10) {
                document.getElementById('user-login-step').style.display = 'none';
                document.getElementById('user-otp-step').style.display = 'flex';
                document.getElementById('user-otp-sent-phone').innerText = '+91 ' + phone;
            } else {
                alert('Enter valid 10-digit phone number');
            }
        };
    }
    const backBtn = document.getElementById('user-back-to-login');
    if(backBtn) {
        backBtn.onclick = (e) => {
            e.preventDefault();
            document.getElementById('user-otp-step').style.display = 'none';
            document.getElementById('user-login-step').style.display = 'flex';
        };
    }
    const verifyBtn = document.getElementById('user-verify-otp-btn');
    if(verifyBtn) {
        verifyBtn.onclick = () => {
            const phone = document.getElementById('user-phone-input').value;
            localStorage.setItem('userPhone', phone);
            alert('Verified successfully! Redirecting to dashboard...');
            window.location.href = 'user-dashboard.html';
        };
    }
    
    // Auto focus OTP
    const otpInputs = document.querySelectorAll('.user-otp-box');
    otpInputs.forEach((input, index) => {
        input.addEventListener('input', function() {
            if(this.value.length === 1 && index < otpInputs.length - 1) otpInputs[index + 1].focus();
        });
        input.addEventListener('keydown', function(e) {
            if (e.key === 'Backspace' && this.value === '' && index > 0) otpInputs[index - 1].focus();
        });
    });
}

document.addEventListener('DOMContentLoaded', () => {
    setTimeout(injectUserModal, 500);
});
''')
