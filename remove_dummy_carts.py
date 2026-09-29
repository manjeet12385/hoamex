import glob, re

def empty_right_cols():
    count = 0
    for f in glob.glob('*.html'):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        original_content = content
        
        # Regex to match <div class="right-col"> ... </div> and <div class="ac-right-col"...> ... </div>
        # We need to find the matching closing div. Since regex for nested divs is hard,
        # we will use a simple bracket counting parser.
        
        def empty_div(class_name):
            nonlocal content
            search_str = f'class="{class_name}"'
            idx = 0
            while True:
                idx = content.find(search_str, idx)
                if idx == -1:
                    break
                
                # find the starting <div
                start_div = content.rfind('<div', 0, idx)
                if start_div == -1:
                    idx += len(search_str)
                    continue
                    
                # find the end of the opening tag
                end_open_tag = content.find('>', idx)
                
                # count divs to find the matching closing div
                open_count = 1
                curr = end_open_tag + 1
                while open_count > 0 and curr < len(content):
                    next_open = content.find('<div', curr)
                    next_close = content.find('</div>', curr)
                    
                    if next_close == -1:
                        break
                        
                    if next_open != -1 and next_open < next_close:
                        open_count += 1
                        curr = next_open + 4
                    else:
                        open_count -= 1
                        curr = next_close + 6
                
                if open_count == 0:
                    # Replace everything inside the div with empty string (or a comment)
                    # content[start_div : curr] is the whole div
                    # We want to keep the div but empty its contents
                    content = content[:end_open_tag+1] + '\n            <!-- Dummy cart removed -->\n        ' + content[curr-6:]
                    
                idx = end_open_tag + 1

        empty_div('right-col')
        empty_div('ac-right-col')
        
        if content != original_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f'Removed dummy cart from {f}')
            count += 1
            
    print(f'Total files updated: {count}')

empty_right_cols()
