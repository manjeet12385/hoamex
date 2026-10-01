import os

with open('common.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure we add an ID to the OTP button
if 'id="partner-otp-btn"' not in content:
    content = content.replace(
        '<button style="width: 100%; background: #5e35b1;',
        '<button id="partner-otp-btn" style="width: 100%; background: #5e35b1;'
    )

# Add event listener for OTP button
otp_js = """
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
"""

if 'partner-otp-btn' in content and 'data-otp-attached' not in content:
    # Insert before the end of the attachPartnerModalEvents function
    content = content.replace(
        'const closeBtn = document.getElementById(\'close-partner-modal\');',
        otp_js + '\n        const closeBtn = document.getElementById(\'close-partner-modal\');'
    )
    
    with open('common.js', 'w', encoding='utf-8') as f:
        f.write(content)
