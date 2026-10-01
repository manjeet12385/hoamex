import os

with open('server.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Add new endpoint to server.js
new_endpoint = """
// API Route for Partner Registration
app.post('/api/partners/register', async (req, res) => {
  try {
    const { 
      full_name, email, phone, experience_years, primary_category, 
      skills, documents, bank_details 
    } = req.body;

    if (!full_name || !email || !phone) {
      return res.status(400).json({ error: 'Missing basic required fields' });
    }

    const query = `
      INSERT INTO partners (
        full_name, email, phone, experience_years, primary_category, 
        skills, documents, bank_details, status
      ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, 'PENDING')
      RETURNING *;
    `;
    
    const values = [
      full_name, email, phone, experience_years, primary_category, 
      JSON.stringify(skills), JSON.stringify(documents), JSON.stringify(bank_details)
    ];

    const result = await pool.query(query, values);
    
    res.status(201).json({ 
      success: true,
      message: 'Partner registered successfully!', 
      partner: result.rows[0] 
    });

  } catch (error) {
    console.error('Error saving partner:', error);
    // Handle unique email constraint error
    if (error.code === '23505') {
      return res.status(400).json({ error: 'This email is already registered.' });
    }
    res.status(500).json({ error: 'Internal Server Error' });
  }
});
"""

# Insert before fallback route
fallback = "// Fallback to serve index.html"
if fallback in content and "/api/partners/register" not in content:
    content = content.replace(fallback, new_endpoint + "\n" + fallback)

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(content)

# Now update partner.html
with open('partner.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add IDs to Step 1 fields
old_step1 = """            <div class="form-group">
                <label>Full Legal Name</label>
                <input type="text" placeholder="Enter full name">
            </div>"""
new_step1 = """            <div class="form-group">
                <label>Full Legal Name</label>
                <input type="text" id="partner-name" placeholder="Enter full name">
            </div>"""
html = html.replace(old_step1, new_step1)

old_phone = """            <div class="form-row" style="margin-bottom: 25px;">
                <div class="form-col">
                    <label>Phone Number</label>
                    <input type="tel" placeholder="Enter phone number">
                </div>
                <div class="form-col">
                    <label>Years of Experience</label>
                    <select>"""
new_phone = """            <div class="form-row" style="margin-bottom: 25px;">
                <div class="form-col">
                    <label>Phone Number</label>
                    <input type="tel" id="partner-phone" placeholder="Enter phone number">
                </div>
                <div class="form-col">
                    <label>Years of Experience</label>
                    <select id="partner-experience">"""
html = html.replace(old_phone, new_phone)

# Add IDs to Step 3 fields
old_bank_1 = """            <div class="form-group">
                <label>Account Holder Name</label>
                <input type="text" placeholder="Enter name as per bank records">
            </div>"""
new_bank_1 = """            <div class="form-group">
                <label>Account Holder Name</label>
                <input type="text" id="bank-holder" placeholder="Enter name as per bank records">
            </div>"""
html = html.replace(old_bank_1, new_bank_1)

old_bank_2 = """            <div class="form-group">
                <label>Bank Name</label>
                <input type="text" placeholder="e.g. State Bank of India">
            </div>"""
new_bank_2 = """            <div class="form-group">
                <label>Bank Name</label>
                <input type="text" id="bank-name" placeholder="e.g. State Bank of India">
            </div>"""
html = html.replace(old_bank_2, new_bank_2)

old_bank_3 = """            <div class="form-row">
                <div class="form-col">
                    <label>Account Number</label>
                    <input type="password" placeholder="Enter account number">
                </div>
                <div class="form-col">
                    <label>IFSC / SWIFT Code</label>
                    <input type="text" placeholder="e.g. SBIN0001234">
                </div>
            </div>"""
new_bank_3 = """            <div class="form-row">
                <div class="form-col">
                    <label>Account Number</label>
                    <input type="password" id="bank-acc" placeholder="Enter account number">
                </div>
                <div class="form-col">
                    <label>IFSC / SWIFT Code</label>
                    <input type="text" id="bank-ifsc" placeholder="e.g. SBIN0001234">
                </div>
            </div>"""
html = html.replace(old_bank_3, new_bank_3)

# Update submitApplication JS logic
old_submit = """        function submitApplication() {
            alert('🎉 Congratulations! Your application has been submitted successfully.\\n\\nOur team will review your details and you will receive an approval email within 24-48 hours.');
            window.location.href = 'index.html';
        }"""
new_submit = """        async function submitApplication() {
            // Collect Data
            const fullName = document.getElementById('partner-name').value;
            const email = document.getElementById('partner-email').value;
            const phone = document.getElementById('partner-phone').value;
            const experience = document.getElementById('partner-experience').value;
            
            // Get selected primary category
            let primaryCategory = 'Other';
            const activeCat = document.querySelector('.cat-box.active');
            if (activeCat) {
                primaryCategory = activeCat.querySelector('span').innerText;
            }

            // Convert skills Set to Array
            const skillsArray = Array.from(selectedGlobalSkills);

            // Collect Docs info (For real app, you'd upload to S3, but here we just send filenames)
            const docFront = document.getElementById('file-id-front').files[0];
            const docBack = document.getElementById('file-id-back').files[0];
            const docCert = document.getElementById('file-cert').files[0];
            const documents = {
                id_front: docFront ? docFront.name : 'Not Uploaded',
                id_back: docBack ? docBack.name : 'Not Uploaded',
                certificate: docCert ? docCert.name : 'Not Uploaded'
            };

            // Collect Bank Details
            const bankDetails = {
                holder_name: document.getElementById('bank-holder').value,
                bank_name: document.getElementById('bank-name').value,
                account_number: document.getElementById('bank-acc').value,
                ifsc: document.getElementById('bank-ifsc').value
            };

            // Basic Validation
            if (!fullName || !email || !phone) {
                alert('Please go back to Step 1 and fill in your Name, Email, and Phone number!');
                return;
            }

            const partnerData = {
                full_name: fullName,
                email: email,
                phone: phone,
                experience_years: experience,
                primary_category: primaryCategory,
                skills: skillsArray,
                documents: documents,
                bank_details: bankDetails
            };

            try {
                // Send to backend
                const response = await fetch('/api/partners/register', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(partnerData)
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    alert('🎉 Congratulations! Your application has been submitted successfully.\\n\\nOur team will review your details and you will receive an approval email within 24-48 hours.');
                    window.location.href = 'index.html';
                } else {
                    alert('Error: ' + (data.error || 'Failed to submit application.'));
                }
            } catch (err) {
                alert('Network Error. Please try again.');
            }
        }"""
html = html.replace(old_submit, new_submit)

with open('partner.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated server.js and partner.html for Registration Submission")
