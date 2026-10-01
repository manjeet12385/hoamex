import os
import re

with open('partner.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add CSS for upload boxes
upload_css = """        /* Upload Boxes */
        .upload-box {
            border: 2px dashed #ddd;
            border-radius: 12px;
            padding: 30px;
            text-align: center;
            background-color: #fcfcfc;
            cursor: pointer;
            transition: 0.2s;
            margin-bottom: 20px;
        }
        .upload-box:hover {
            border-color: #4a3aff;
            background-color: #f5f5ff;
        }
        .upload-box i {
            font-size: 24px;
            color: #888;
            margin-bottom: 10px;
        }
        .upload-box p {
            font-size: 13px;
            color: #555;
            margin: 0;
        }
        
        /* Previous Button */
        .prev-btn {
            background-color: #fff;
            color: #444;
            border: 1px solid #ddd;
            padding: 14px 30px;
            border-radius: 8px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: 0.2s;
        }
        .prev-btn:hover {
            background-color: #f5f5f5;
        }
"""

if "/* Upload Boxes */" not in content:
    content = content.replace("/* Next Button */", upload_css + "\n        /* Next Button */")

# Split main content to wrap Step 1 and add Step 2
old_main_content_start = """        <div class="progress-header">
            <div>
                <div class="progress-title">Registration Progress</div>
                <div class="progress-step">Step 1 of 3: Personal & Service Details</div>
            </div>
        </div>
        
        <div class="progress-bar-container">
            <div class="progress-bar-fill"></div>
        </div>"""

new_main_content_start = """        <!-- STEP 1: Personal & Service Details -->
        <div id="step-1-content">
            <div class="progress-header">
                <div>
                    <div class="progress-title">Registration Progress</div>
                    <div class="progress-step">Step 1 of 3: Personal & Service Details</div>
                </div>
            </div>
            
            <div class="progress-bar-container">
                <div class="progress-bar-fill" style="width: 33%;"></div>
            </div>"""

if old_main_content_start in content:
    content = content.replace(old_main_content_start, new_main_content_start)

# End of Step 1 and start of Step 2
old_next_btn = """        <div class="next-btn-container">
            <button class="next-btn">Next Step &rarr;</button>
        </div>"""

new_steps = """        <div class="next-btn-container" style="justify-content: flex-end;">
            <button class="next-btn" onclick="goToStep(2)">Next Step &rarr;</button>
        </div>
        </div> <!-- End of Step 1 -->

        <!-- STEP 2: Verification & Compliance -->
        <div id="step-2-content" style="display: none;">
            <div class="progress-header">
                <div>
                    <div class="progress-title">Registration Progress</div>
                    <div class="progress-step">Step 2 of 3: Verification & Compliance</div>
                </div>
                <div style="font-size: 13px; color: #666; font-weight: 600; margin-top: 5px;">67% Complete</div>
            </div>
            
            <div class="progress-bar-container">
                <div class="progress-bar-fill" style="width: 67%;"></div>
            </div>

            <div class="section-title">3. Identity Verification</div>
            <div class="section-desc" style="margin-bottom: 8px;">Upload ID Card (Front)</div>
            <div class="upload-box" onclick="document.getElementById('file-id-front').click()">
                <i class="fa-solid fa-camera"></i>
                <p>Click to Upload Front of ID</p>
                <input type="file" id="file-id-front" style="display: none;">
            </div>

            <div class="section-desc" style="margin-bottom: 8px;">Upload ID Card (Back)</div>
            <div class="upload-box" onclick="document.getElementById('file-id-back').click()">
                <i class="fa-solid fa-camera"></i>
                <p>Click to Upload Back of ID</p>
                <input type="file" id="file-id-back" style="display: none;">
            </div>

            <div class="section-title" style="margin-top: 40px;">4. Professional Certification</div>
            <div class="section-desc" style="margin-bottom: 8px;">Upload License or Certificate</div>
            <div class="upload-box" onclick="document.getElementById('file-cert').click()">
                <i class="fa-solid fa-file-contract"></i>
                <p>Click to Upload Document</p>
                <input type="file" id="file-cert" style="display: none;">
            </div>
            
            <div class="next-btn-container" style="justify-content: space-between; margin-top: 40px;">
                <button class="prev-btn" onclick="goToStep(1)">Previous</button>
                <button class="next-btn" onclick="goToStep(3)">Next Step &rarr;</button>
            </div>
        </div> <!-- End of Step 2 -->
"""

if old_next_btn in content:
    content = content.replace(old_next_btn, new_steps)

# Add JS logic for changing steps
old_js_start = """    <script>
        let selectedGlobalSkills = new Set();"""

new_js_start = """    <script>
        function goToStep(stepNumber) {
            // Hide all steps
            document.getElementById('step-1-content').style.display = 'none';
            document.getElementById('step-2-content').style.display = 'none';
            // Show requested step
            if(stepNumber === 1) {
                document.getElementById('step-1-content').style.display = 'block';
            } else if(stepNumber === 2) {
                document.getElementById('step-2-content').style.display = 'block';
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } else if(stepNumber === 3) {
                alert('Step 3 (Bank Details) is coming soon!');
                // Temporarily stay on Step 2
                document.getElementById('step-2-content').style.display = 'block';
            }
        }

        let selectedGlobalSkills = new Set();"""

if old_js_start in content:
    content = content.replace(old_js_start, new_js_start)

with open('partner.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated partner.html with Step 2 UI")
