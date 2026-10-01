import os

with open('partner.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update HTML for Email Verify
old_email_html = """        <div class="form-group">
            <label>Business Email</label>
            <div class="input-with-button" style="padding: 2px;">
                <input type="email" placeholder="Enter email address">
                <button class="verify-btn">Verify</button>
            </div>
        </div>"""

new_email_html = """        <div class="form-group">
            <label>Business Email</label>
            <div class="input-with-button" style="padding: 2px;" id="email-input-container">
                <input type="email" id="partner-email" placeholder="Enter email address">
                <button class="verify-btn" id="send-otp-btn" onclick="sendPartnerOTP()">Verify</button>
            </div>
            
            <div id="otp-verify-box" style="display: none; margin-top: 10px;">
                <div class="input-with-button" style="padding: 2px; border-color: #4a3aff;">
                    <input type="text" id="partner-otp" placeholder="Enter OTP sent to email" maxlength="6">
                    <button class="verify-btn" style="background: #4a3aff;" onclick="verifyPartnerOTP()">Confirm</button>
                </div>
            </div>
            
            <div id="email-success-msg" style="display: none; margin-top: 8px; font-size: 13px; color: #23a566; font-weight: 600;">
                <i class="fa-solid fa-circle-check"></i> Email verified successfully!
            </div>
        </div>"""

if old_email_html in content:
    content = content.replace(old_email_html, new_email_html)

# Add a section to show all selected skills
old_subcat_section = """            <div id="subcat-chips" style="display: flex; flex-wrap: wrap; gap: 10px;">
                <!-- Chips will be injected here via JS -->
            </div>
        </div>"""

new_subcat_section = """            <div id="subcat-chips" style="display: flex; flex-wrap: wrap; gap: 10px;">
                <!-- Chips will be injected here via JS -->
            </div>
        </div>
        
        <div id="selected-skills-summary" style="margin-bottom: 40px; display: none;">
            <div class="section-title" style="font-size: 15px; margin-bottom: 10px;">Your Selected Services</div>
            <div id="summary-chips" style="display: flex; flex-wrap: wrap; gap: 8px; padding: 15px; background: #fdfaf6; border: 1px dashed #ccc; border-radius: 8px;">
                <!-- Selected skills will appear here -->
            </div>
        </div>"""

if old_subcat_section in content:
    content = content.replace(old_subcat_section, new_subcat_section)

# Update JS logic
old_js = """                chip.onclick = function() {
                    this.classList.toggle('selected');
                    if(this.classList.contains('selected')) {
                        this.innerHTML = '<i class="fa-solid fa-check"></i> ' + skill;
                    } else {
                        this.innerHTML = skill;
                    }
                };"""

new_js = """                chip.onclick = function() {
                    this.classList.toggle('selected');
                    if(this.classList.contains('selected')) {
                        this.innerHTML = '<i class="fa-solid fa-check"></i> ' + skill;
                        selectedGlobalSkills.add(skill);
                    } else {
                        this.innerHTML = skill;
                        selectedGlobalSkills.delete(skill);
                    }
                    updateSelectedSkillsSummary();
                };"""

if old_js in content:
    content = content.replace(old_js, new_js)

old_js_start = """    <script>
        const subcategories = {"""

new_js_start = """    <script>
        let selectedGlobalSkills = new Set();
        let expectedOTP = null;

        function updateSelectedSkillsSummary() {
            const container = document.getElementById('selected-skills-summary');
            const chipsContainer = document.getElementById('summary-chips');
            
            if (selectedGlobalSkills.size === 0) {
                container.style.display = 'none';
                return;
            }
            
            container.style.display = 'block';
            chipsContainer.innerHTML = '';
            
            selectedGlobalSkills.forEach(skill => {
                const badge = document.createElement('span');
                badge.style.cssText = 'background: #4a3aff; color: white; padding: 5px 12px; border-radius: 15px; font-size: 12px; font-weight: 500; display: inline-flex; align-items: center; gap: 5px;';
                badge.innerHTML = skill + ' <i class="fa-solid fa-xmark" style="cursor: pointer;" onclick="removeSkillGlobal(\\'' + skill + '\\')"></i>';
                chipsContainer.appendChild(badge);
            });
        }
        
        function removeSkillGlobal(skill) {
            selectedGlobalSkills.delete(skill);
            updateSelectedSkillsSummary();
            // Also unselect the chip if it's currently visible
            document.querySelectorAll('.chip.selected').forEach(chip => {
                if(chip.innerText.includes(skill)) {
                    chip.classList.remove('selected');
                    chip.innerHTML = skill;
                }
            });
        }

        function sendPartnerOTP() {
            const emailInput = document.getElementById('partner-email');
            const btn = document.getElementById('send-otp-btn');
            
            if (!emailInput.value) {
                alert('Please enter your email first.');
                return;
            }
            
            const originalText = btn.innerHTML;
            btn.innerHTML = 'Sending...';
            btn.disabled = true;
            
            fetch('/api/send-otp', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: emailInput.value })
            })
            .then(res => res.json())
            .then(data => {
                if(data.success) {
                    expectedOTP = data.otp; // Store OTP for checking
                    document.getElementById('otp-verify-box').style.display = 'block';
                    btn.innerHTML = 'Sent!';
                } else {
                    btn.innerHTML = originalText;
                    btn.disabled = false;
                    alert('Failed to send OTP.');
                }
            })
            .catch(err => {
                btn.innerHTML = originalText;
                btn.disabled = false;
                alert('Server error.');
            });
        }

        function verifyPartnerOTP() {
            const entered = document.getElementById('partner-otp').value;
            if (entered == expectedOTP) {
                document.getElementById('otp-verify-box').style.display = 'none';
                document.getElementById('email-input-container').style.display = 'none';
                document.getElementById('email-success-msg').style.display = 'block';
                document.getElementById('email-success-msg').innerHTML = '<i class="fa-solid fa-circle-check"></i> Verified: ' + document.getElementById('partner-email').value;
            } else {
                alert('Invalid OTP. Please try again.');
            }
        }

        const subcategories = {"""

if old_js_start in content:
    content = content.replace(old_js_start, new_js_start)

# We also need to fix renderSubcategories so that previously selected chips remain selected when navigating back to a category
old_render = """            skills.forEach(skill => {
                const chip = document.createElement('div');
                chip.className = 'chip';
                chip.innerHTML = skill;"""

new_render = """            skills.forEach(skill => {
                const chip = document.createElement('div');
                chip.className = 'chip';
                
                if (selectedGlobalSkills.has(skill)) {
                    chip.classList.add('selected');
                    chip.innerHTML = '<i class="fa-solid fa-check"></i> ' + skill;
                } else {
                    chip.innerHTML = skill;
                }"""

if old_render in content:
    content = content.replace(old_render, new_render)

with open('partner.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated partner.html with verification and global skills summary")
