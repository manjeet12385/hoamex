import os

with open('common.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the start of Right Side
old_right_start = """<!-- Right Side -->
                    <div style="flex: 1.2; background: #0a0c10; padding: 50px 40px; display: flex; flex-direction: column; justify-content: center;">
                        <h3 style="color: #fff; font-size: 24px; font-weight: 700; margin: 0 0 10px 0;">Partner Login</h3>"""

new_right_start = """<!-- Right Side -->
                    <div style="flex: 1.2; background: #0a0c10; padding: 50px 40px; display: flex; flex-direction: column; justify-content: center; position: relative;">
                        <!-- Step 1: Login -->
                        <div id="partner-login-step" style="display: flex; flex-direction: column; height: 100%; justify-content: center;">
                            <h3 style="color: #fff; font-size: 24px; font-weight: 700; margin: 0 0 10px 0;">Partner Login</h3>"""

content = content.replace(old_right_start, new_right_start)

# Replace the end of Right Side to add Step 2
old_right_end = """<div style="text-align: center; margin-top: auto;">
                            <span style="color: #484f58; font-size: 11px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase;"><i class="fa-solid fa-shield-halved"></i> PARTNER SECURITY 2.0</span>
                        </div>
                    </div>"""

new_right_end = """<div style="text-align: center; margin-top: auto;">
                                <span style="color: #484f58; font-size: 11px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase;"><i class="fa-solid fa-shield-halved"></i> PARTNER SECURITY 2.0</span>
                            </div>
                        </div>

                        <!-- Step 2: OTP Verification -->
                        <div id="partner-otp-step" style="display: none; flex-direction: column; height: 100%; justify-content: center;">
                            <a href="#" id="back-to-login" style="color: #8b949e; text-decoration: none; font-size: 13px; margin-bottom: 20px; display: inline-block;">&larr; Back to Login</a>
                            <h3 style="color: #fff; font-size: 28px; font-weight: 700; margin: 0 0 10px 0;">OTP Verification</h3>
                            <p style="color: #8b949e; font-size: 14px; margin: 0 0 30px 0;">Code sent to <span id="otp-sent-email" style="color: #fff;"></span></p>
                            
                            <div style="display: flex; gap: 10px; margin-bottom: 30px; justify-content: space-between;">
                                <input type="text" maxlength="1" class="otp-box-input" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none; transition: 0.2s;" onfocus="this.style.borderColor='#23a566'" onblur="this.style.borderColor='#30363d'">
                                <input type="text" maxlength="1" class="otp-box-input" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none; transition: 0.2s;" onfocus="this.style.borderColor='#23a566'" onblur="this.style.borderColor='#30363d'">
                                <input type="text" maxlength="1" class="otp-box-input" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none; transition: 0.2s;" onfocus="this.style.borderColor='#23a566'" onblur="this.style.borderColor='#30363d'">
                                <input type="text" maxlength="1" class="otp-box-input" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none; transition: 0.2s;" onfocus="this.style.borderColor='#23a566'" onblur="this.style.borderColor='#30363d'">
                                <input type="text" maxlength="1" class="otp-box-input" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none; transition: 0.2s;" onfocus="this.style.borderColor='#23a566'" onblur="this.style.borderColor='#30363d'">
                                <input type="text" maxlength="1" class="otp-box-input" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none; transition: 0.2s;" onfocus="this.style.borderColor='#23a566'" onblur="this.style.borderColor='#30363d'">
                            </div>

                            <button id="verify-otp-final-btn" style="width: 100%; background: #23a566; color: #fff; border: none; padding: 14px; border-radius: 8px; font-weight: 600; font-size: 15px; cursor: pointer; transition: 0.2s; margin-bottom: 25px;" onmouseover="this.style.background='#28c076'" onmouseout="this.style.background='#23a566'">Verify & Enter Dashboard</button>

                            <div style="text-align: center; margin-top: auto;">
                                <span style="color: #8b949e; font-size: 13px;">Resend in <span style="color: #fff; font-weight: 600;">56s</span></span>
                            </div>
                        </div>
                    </div>"""

content = content.replace(old_right_end, new_right_end)

# Modify the JS logic to transition to step 2 instead of alert
old_js = """                        if(data.success) {
                            alert('OTP has been sent to ' + emailInput.value + ' (Check your inbox)');
                        } else {"""

new_js = """                        if(data.success) {
                            // Hide login step, show OTP step
                            document.getElementById('partner-login-step').style.display = 'none';
                            document.getElementById('partner-otp-step').style.display = 'flex';
                            document.getElementById('otp-sent-email').innerText = emailInput.value;
                            
                            // Attach event for back button
                            document.getElementById('back-to-login').onclick = function(e) {
                                e.preventDefault();
                                document.getElementById('partner-otp-step').style.display = 'none';
                                document.getElementById('partner-login-step').style.display = 'flex';
                            };
                            
                            // OTP input auto focus
                            const otpInputs = document.querySelectorAll('.otp-box-input');
                            otpInputs.forEach((input, index) => {
                                input.addEventListener('input', function() {
                                    if(this.value.length === 1 && index < otpInputs.length - 1) {
                                        otpInputs[index + 1].focus();
                                    }
                                });
                                input.addEventListener('keydown', function(e) {
                                    if (e.key === 'Backspace' && this.value === '' && index > 0) {
                                        otpInputs[index - 1].focus();
                                    }
                                });
                            });
                            
                        } else {"""

content = content.replace(old_js, new_js)

with open('common.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated common.js with OTP UI")
