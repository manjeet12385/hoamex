import os

with open('partner.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_goToStep = """            // Show requested step
            if(stepNumber === 1) {"""

new_goToStep = """            // Validation before going to Step 3 (Documents)
            if (stepNumber === 3) {
                const docFront = document.getElementById('file-id-front').files.length;
                const docBack = document.getElementById('file-id-back').files.length;
                const docCert = document.getElementById('file-cert').files.length;
                
                if (docFront === 0 || docBack === 0) {
                    alert('Please upload both Front and Back of your ID Card before proceeding.');
                    return;
                }
                if (docCert === 0) {
                    alert('Please upload your Professional License or Certificate before proceeding.');
                    return;
                }
            }

            // Show requested step
            if(stepNumber === 1) {"""

if old_goToStep in content:
    content = content.replace(old_goToStep, new_goToStep)
    print("Added Step 2 validation")

old_submit = """            // Collect Bank Details
            const bankDetails = {
                holder_name: document.getElementById('bank-holder').value,
                bank_name: document.getElementById('bank-name').value,
                account_number: document.getElementById('bank-acc').value,
                ifsc: document.getElementById('bank-ifsc').value
            };"""

new_submit = """            // Collect Bank Details
            const bankHolder = document.getElementById('bank-holder').value.trim();
            const bankName = document.getElementById('bank-name').value.trim();
            const bankAcc = document.getElementById('bank-acc').value.trim();
            const bankIfsc = document.getElementById('bank-ifsc').value.trim();
            
            // Validate Bank Details
            if (!bankHolder || !bankName || !bankAcc || !bankIfsc) {
                alert('Please fill in all your Bank Details before submitting the application.');
                return;
            }

            const bankDetails = {
                holder_name: bankHolder,
                bank_name: bankName,
                account_number: bankAcc,
                ifsc: bankIfsc
            };"""

if old_submit in content:
    content = content.replace(old_submit, new_submit)
    print("Added Step 3 validation")

with open('partner.html', 'w', encoding='utf-8') as f:
    f.write(content)
