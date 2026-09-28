import re

for filename in ['plumber.html', 'plumber_fixed.html']:
    path = rf'c:\Users\Divyanshi123456\Music\hoamex\{filename}'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # The exact string with backslashes
    bad_str = r"getElementById(\'drain-block-modal\').classList.remove(\'hidden\')"
    good_str = "getElementById('drain-block-modal').classList.remove('hidden')"

    c = c.replace(bad_str, good_str)
    # also try this exact string if the above doesn't work
    c = c.replace(r"getElementById(\'drain-block-modal\')", "getElementById('drain-block-modal')")
    c = c.replace(r"classList.remove(\'hidden\')", "classList.remove('hidden')")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

print('Fixed backslashes in both files!')
