with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    c = f.read()
import re
print("Matches for tap-acc-modal:")
print(len(re.findall(r'id="tap-acc-modal"', c)))

print("Matches for the tap acc install button:")
idx = c.find('Tap accessory installation')
idx2 = c.find('Tap accessory installation', idx + 10)
if idx2 != -1:
    print(c[idx2-50:idx2+250])
