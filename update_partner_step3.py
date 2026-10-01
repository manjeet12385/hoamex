import os
import re

with open('partner.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Step 3 Content
old_end_step2 = """        </div> <!-- End of Step 2 -->"""

new_step3 = """        </div> <!-- End of Step 2 -->

        <!-- STEP 3: Bank Details -->
        <div id="step-3-content" style="display: none;">
            <div class="progress-header">
                <div>
                    <div class="progress-title">Registration Progress</div>
                    <div class="progress-step">Step 3 of 3: Bank Details</div>
                </div>
                <div style="font-size: 13px; color: #4a3aff; font-weight: 600; margin-top: 5px;">100% Complete</div>
            </div>
            
            <div class="progress-bar-container">
                <div class="progress-bar-fill" style="width: 100%;"></div>
            </div>

            <div class="section-title">5. Payout Information</div>
            <div class="section-desc" style="margin-bottom: 25px;">Enter your bank details for weekly payouts.</div>
            
            <div class="form-group">
                <label>Account Holder Name</label>
                <input type="text" placeholder="Enter name as per bank records">
            </div>
            
            <div class="form-group">
                <label>Bank Name</label>
                <input type="text" placeholder="e.g. State Bank of India">
            </div>
            
            <div class="form-row">
                <div class="form-col">
                    <label>Account Number</label>
                    <input type="password" placeholder="Enter account number">
                </div>
                <div class="form-col">
                    <label>IFSC / SWIFT Code</label>
                    <input type="text" placeholder="e.g. SBIN0001234">
                </div>
            </div>

            <div style="background-color: rgba(74, 58, 255, 0.05); border: 1px solid rgba(74, 58, 255, 0.15); border-radius: 8px; padding: 15px; margin-top: 30px; display: flex; align-items: center; gap: 10px;">
                <i class="fa-solid fa-lock" style="color: #4a3aff;"></i>
                <span style="font-size: 13px; color: #4a3aff; font-weight: 500;">All data is encrypted and stored securely (PCI DSS Compliant)</span>
            </div>
            
            <div class="next-btn-container" style="justify-content: space-between; margin-top: 40px;">
                <button class="prev-btn" onclick="goToStep(2)">Previous</button>
                <button class="next-btn" style="background-color: #4a3aff;" onclick="submitApplication()">Submit Application &rarr;</button>
            </div>
        </div> <!-- End of Step 3 -->
"""

if old_end_step2 in content:
    content = content.replace(old_end_step2, new_step3)

# Update JS logic
old_js = """            } else if(stepNumber === 3) {
                alert('Step 3 (Bank Details) is coming soon!');
                // Temporarily stay on Step 2
                document.getElementById('step-2-content').style.display = 'block';
            }"""

new_js = """            } else if(stepNumber === 3) {
                document.getElementById('step-3-content').style.display = 'block';
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }

        function submitApplication() {
            alert('🎉 Congratulations! Your application has been submitted successfully.\\n\\nOur team will review your details and you will receive an approval email within 24-48 hours.');
            window.location.href = 'index.html';
        }"""

if old_js in content:
    content = content.replace(old_js, new_js)

with open('partner.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated partner.html with Step 3 UI")
