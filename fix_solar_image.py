import re

with open('solar-water-heater.html', 'r', encoding='utf-8') as f:
    content = f.read()

# find tools.jpg and replace it with solar_water_heater.jpg
content = content.replace('images/tools.jpg', 'images/solar_water_heater.jpg')

with open('solar-water-heater.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed tools.jpg in solar-water-heater.html')
