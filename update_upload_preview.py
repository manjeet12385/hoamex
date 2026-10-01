import os

with open('partner.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace upload boxes with IDs and onchange events
old_box_1 = """            <div class="upload-box" onclick="document.getElementById('file-id-front').click()">
                <i class="fa-solid fa-camera"></i>
                <p>Click to Upload Front of ID</p>
                <input type="file" id="file-id-front" style="display: none;">
            </div>"""
new_box_1 = """            <div class="upload-box" id="box-id-front" onclick="document.getElementById('file-id-front').click()">
                <div class="upload-content">
                    <i class="fa-solid fa-camera"></i>
                    <p>Click to Upload Front of ID</p>
                </div>
                <input type="file" id="file-id-front" accept="image/*,application/pdf" style="display: none;" onchange="handleFileUpload(this, 'box-id-front')">
            </div>"""

old_box_2 = """            <div class="upload-box" onclick="document.getElementById('file-id-back').click()">
                <i class="fa-solid fa-camera"></i>
                <p>Click to Upload Back of ID</p>
                <input type="file" id="file-id-back" style="display: none;">
            </div>"""
new_box_2 = """            <div class="upload-box" id="box-id-back" onclick="document.getElementById('file-id-back').click()">
                <div class="upload-content">
                    <i class="fa-solid fa-camera"></i>
                    <p>Click to Upload Back of ID</p>
                </div>
                <input type="file" id="file-id-back" accept="image/*,application/pdf" style="display: none;" onchange="handleFileUpload(this, 'box-id-back')">
            </div>"""

old_box_3 = """            <div class="upload-box" onclick="document.getElementById('file-cert').click()">
                <i class="fa-solid fa-file-contract"></i>
                <p>Click to Upload Document</p>
                <input type="file" id="file-cert" style="display: none;">
            </div>"""
new_box_3 = """            <div class="upload-box" id="box-cert" onclick="document.getElementById('file-cert').click()">
                <div class="upload-content">
                    <i class="fa-solid fa-file-contract"></i>
                    <p>Click to Upload Document</p>
                </div>
                <input type="file" id="file-cert" accept="image/*,application/pdf" style="display: none;" onchange="handleFileUpload(this, 'box-cert')">
            </div>"""

if old_box_1 in content:
    content = content.replace(old_box_1, new_box_1)
if old_box_2 in content:
    content = content.replace(old_box_2, new_box_2)
if old_box_3 in content:
    content = content.replace(old_box_3, new_box_3)


# Add JS function for handling the upload preview
old_js_end = """        let selectedGlobalSkills = new Set();"""
new_js_end = """        function handleFileUpload(inputElement, boxId) {
            const file = inputElement.files[0];
            if (!file) return;

            const box = document.getElementById(boxId);
            const contentDiv = box.querySelector('.upload-content');
            
            // If it's an image, show preview
            if (file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    box.style.padding = "10px";
                    contentDiv.innerHTML = `
                        <img src="${e.target.result}" style="max-height: 120px; max-width: 100%; border-radius: 8px; object-fit: contain;">
                        <p style="margin-top: 10px; font-size: 12px; color: #23a566; font-weight: 600;"><i class="fa-solid fa-check-circle"></i> Uploaded: ${file.name}</p>
                    `;
                }
                reader.readAsDataURL(file);
            } else {
                // For PDF or other files
                contentDiv.innerHTML = `
                    <i class="fa-solid fa-file-pdf" style="color: #e53935; font-size: 32px;"></i>
                    <p style="margin-top: 10px; font-size: 12px; color: #23a566; font-weight: 600;"><i class="fa-solid fa-check-circle"></i> Uploaded: ${file.name}</p>
                `;
            }
        }

        let selectedGlobalSkills = new Set();"""

if old_js_end in content:
    content = content.replace(old_js_end, new_js_end)

with open('partner.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated partner.html to preview file uploads")
