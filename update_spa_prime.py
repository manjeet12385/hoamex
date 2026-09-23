import sys

with open('spa-prime.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_index = -1
end_index = -1

for i, line in enumerate(lines):
    if '<!-- Banner -->' in line:
        start_index = i
        break

for i in range(len(lines)-1, -1, -1):
    if '<!-- end center-content -->' in lines[i]:
        end_index = i
        break

if start_index != -1 and end_index != -1:
    new_lines = lines[:start_index]
    new_lines.append('                <div style="position: relative; border-radius: 12px; overflow: hidden; margin-bottom: 30px;">\n')
    new_lines.append('                    <img src="images/beauty.jpg" alt="Spa to your home" style="width: 100%; height: auto; display: block;">\n')
    new_lines.append('                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center;">\n')
    new_lines.append('                        <h2 style="color: #fff; font-size: 42px; font-weight: 700; text-align: center; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); margin: 0;">spa to your home</h2>\n')
    new_lines.append('                    </div>\n')
    new_lines.append('                </div>\n\n')
    new_lines.append('                <!-- Sections will be added here later -->\n\n')
    new_lines.extend(lines[end_index:])
    
    # Also fix the script at the bottom
    # find the script logic
    script_start = -1
    for i, line in enumerate(new_lines):
        if 'const sections = [' in line:
            script_start = i
            break
            
    if script_start != -1:
        script_end = -1
        for i in range(script_start, len(new_lines)):
            if '];' in new_lines[i]:
                script_end = i
                break
        if script_end != -1:
            # clear it
            new_lines = new_lines[:script_start+1] + ['                // To be added\n'] + new_lines[script_end:]

    with open('spa-prime.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print('Replaced center content')
else:
    print('Could not find start or end index')
