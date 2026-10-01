import os

with open('partner.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Phone Number 10-digit Validation
old_phone_val = """                if (!phone) {
                    alert('Please enter your Phone Number before proceeding.');
                    return;
                }"""

new_phone_val = """                if (!phone || phone.length !== 10 || isNaN(phone)) {
                    alert('Please enter a valid 10-digit Phone Number before proceeding.');
                    return;
                }"""

if old_phone_val in content:
    content = content.replace(old_phone_val, new_phone_val)


# 2. Add Double-Click Protection on Submit Button
old_submit = """        async function submitApplication() {"""

new_submit = """        let isSubmitting = false;
        async function submitApplication() {
            if (isSubmitting) return; // Prevent double-clicks
            isSubmitting = true;
            
            const submitBtn = document.querySelector('#step-3-content .next-btn');
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.innerHTML = 'Submitting... <i class="fa-solid fa-spinner fa-spin"></i>';
            submitBtn.style.opacity = '0.7';"""

if old_submit in content:
    content = content.replace(old_submit, new_submit)

# Reset button if error occurs
old_catch = """            } catch (err) {
                alert('Network Error. Please try again.');
            }
        }"""

new_catch = """            } catch (err) {
                alert('Network Error. Please try again.');
            } finally {
                isSubmitting = false;
                submitBtn.innerHTML = originalBtnText;
                submitBtn.style.opacity = '1';
            }
        }"""

if old_catch in content:
    content = content.replace(old_catch, new_catch)


# Reset button if validation fails (Bank Details)
old_bank_val = """            if (!bankHolder || !bankName || !bankAcc || !bankIfsc) {
                alert('Please fill in all your Bank Details before submitting the application.');
                return;
            }"""

new_bank_val = """            if (!bankHolder || !bankName || !bankAcc || !bankIfsc) {
                alert('Please fill in all your Bank Details before submitting the application.');
                isSubmitting = false;
                submitBtn.innerHTML = originalBtnText;
                submitBtn.style.opacity = '1';
                return;
            }"""

if old_bank_val in content:
    content = content.replace(old_bank_val, new_bank_val)

# Fix Basic Validation early exit
old_basic_val = """            // Basic Validation
            if (!fullName || !email || !phone) {
                alert('Please go back to Step 1 and fill in your Name, Email, and Phone number!');
                return;
            }"""

new_basic_val = """            // Basic Validation
            if (!fullName || !email || !phone) {
                alert('Please go back to Step 1 and fill in your Name, Email, and Phone number!');
                isSubmitting = false;
                submitBtn.innerHTML = originalBtnText;
                submitBtn.style.opacity = '1';
                return;
            }"""

if old_basic_val in content:
    content = content.replace(old_basic_val, new_basic_val)

with open('partner.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied robust validations to partner.html")
