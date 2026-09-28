with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber_fixed.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("getElementById(\\'drain-block-modal\\')", "getElementById('drain-block-modal')")
c = c.replace("classList.remove(\\'hidden\\')", "classList.remove('hidden')")

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber_fixed.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed backslashes!')
