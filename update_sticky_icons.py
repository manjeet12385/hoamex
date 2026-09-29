import os
import glob

html_files = glob.glob('*.html')

old_sticky_icons = """    <!-- Sticky Contact Icons -->
    <div class="sticky-contact-icons" style="position: fixed; left: 15px; top: 50%; transform: translateY(-50%); z-index: 9999; display: flex; flex-direction: column; gap: 15px;">
        <a href="https://wa.me/919014380344" target="_blank" style="display: flex; align-items: center; justify-content: center; width: 50px; height: 50px; border-radius: 50%; background-color: #25d366; color: white; text-decoration: none; font-size: 28px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
            <i class="fa-brands fa-whatsapp"></i>
        </a>
        <a href="tel:+919014380344" style="display: flex; align-items: center; justify-content: center; width: 50px; height: 50px; border-radius: 50%; background-color: #5c6bc0; color: white; text-decoration: none; font-size: 24px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
            <i class="fa-solid fa-phone"></i>
        </a>
    </div>"""

new_sticky_icons = """    <!-- Sticky Contact Icons -->
    <style>
        @keyframes pulse-glow {
            0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.8); }
            70% { box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
            100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }
        @keyframes pulse-glow-blue {
            0% { box-shadow: 0 0 0 0 rgba(92, 107, 192, 0.8); }
            70% { box-shadow: 0 0 0 15px rgba(92, 107, 192, 0); }
            100% { box-shadow: 0 0 0 0 rgba(92, 107, 192, 0); }
        }
        @keyframes wiggle {
            0% { transform: rotate(0deg); }
            15% { transform: rotate(-15deg); }
            30% { transform: rotate(15deg); }
            45% { transform: rotate(-15deg); }
            60% { transform: rotate(15deg); }
            75% { transform: rotate(0deg); }
            100% { transform: rotate(0deg); }
        }
        .sticky-wa-icon {
            animation: pulse-glow 2s infinite;
        }
        .sticky-wa-icon:hover {
            animation: none;
            transform: scale(1.1) !important;
        }
        .sticky-wa-icon i {
            animation: wiggle 2.5s infinite;
        }
        .sticky-phone-icon {
            animation: pulse-glow-blue 2s infinite;
            animation-delay: 1s;
        }
        .sticky-phone-icon:hover {
            animation: none;
            transform: scale(1.1) !important;
        }
        .sticky-phone-icon i {
            animation: wiggle 2.5s infinite;
            animation-delay: 1s;
        }
        .notification-badge {
            animation: bounce 2s infinite;
        }
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
            40% {transform: translateY(-5px);}
            60% {transform: translateY(-3px);}
        }
    </style>
    <div class="sticky-contact-icons" style="position: fixed; left: 15px; top: 50%; transform: translateY(-50%); z-index: 9999; display: flex; flex-direction: column; gap: 20px;">
        <a href="https://wa.me/919014380344" target="_blank" class="sticky-wa-icon" style="display: flex; align-items: center; justify-content: center; width: 55px; height: 55px; border-radius: 50%; background-color: #25d366; color: white; text-decoration: none; font-size: 32px; transition: transform 0.3s; position: relative;">
            <span class="notification-badge" style="position: absolute; right: -5px; top: -5px; background-color: #ff0000; color: white; font-size: 12px; font-weight: bold; padding: 3px 7px; border-radius: 50%; border: 2px solid white; line-height: 1;">1</span>
            <i class="fa-brands fa-whatsapp"></i>
        </a>
        <a href="tel:+919014380344" class="sticky-phone-icon" style="display: flex; align-items: center; justify-content: center; width: 55px; height: 55px; border-radius: 50%; background-color: #5c6bc0; color: white; text-decoration: none; font-size: 26px; transition: transform 0.3s; position: relative;">
            <span style="position: absolute; width: 100%; height: 100%; border-radius: 50%; border: 2px solid rgba(255,255,255,0.5); top: -2px; left: -2px;"></span>
            <i class="fa-solid fa-phone"></i>
        </a>
    </div>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The exact spacing might differ slightly, let's just find where it starts and ends if simple replace fails.
    start_str = "    <!-- Sticky Contact Icons -->"
    end_str = "    </div>"
    
    if start_str in content:
        start_index = content.find(start_str)
        end_index = content.find(end_str, start_index) + len(end_str)
        current_block = content[start_index:end_index]
        
        # Replace the old block with the new one
        content = content.replace(current_block, new_sticky_icons)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Not found in {filepath}")
