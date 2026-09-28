with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Drain blockage removal</h3>')
end_idx = c.find('modal-overlay hidden', idx)
print(c[idx:end_idx if end_idx != -1 else idx+2000])
