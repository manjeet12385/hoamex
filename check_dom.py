with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="tap-acc-modal"')
print(c[max(0, idx-200):idx+500])
