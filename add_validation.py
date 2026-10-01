import os

with open('partner.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_go_to_step = """        function goToStep(stepNumber) {
            // Hide all steps
            document.getElementById('step-1-content').style.display = 'none';"""

new_go_to_step = """        function goToStep(stepNumber) {
            // Validation before going to Step 2
            if (stepNumber === 2) {
                const name = document.getElementById('partner-name').value.trim();
                const phone = document.getElementById('partner-phone').value.trim();
                const isEmailVerified = document.getElementById('email-success-msg').style.display === 'block';

                if (!name) {
                    alert('Please enter your Full Legal Name before proceeding.');
                    return;
                }
                if (!isEmailVerified) {
                    alert('Please enter your Business Email and Verify it with OTP before proceeding.');
                    return;
                }
                if (!phone) {
                    alert('Please enter your Phone Number before proceeding.');
                    return;
                }
            }

            // Hide all steps
            document.getElementById('step-1-content').style.display = 'none';"""

if old_go_to_step in content:
    content = content.replace(old_go_to_step, new_go_to_step)
    with open('partner.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added validation to goToStep(2)")
else:
    print("Could not find the target string to replace")
