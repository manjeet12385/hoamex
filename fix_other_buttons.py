import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Shower installation
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Shower installation',99)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('shower-inst-modal').style.display='flex'">Add</button>'''
)
content = content.replace(
    '''<div id="shower-inst-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">''',
    '''<div id="shower-inst-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">'''
)
content = content.replace(
    '''<button id="close-shower-inst-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>''',
    '''<button id="close-shower-inst-modal-btn" onclick="document.getElementById('shower-inst-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>'''
)

# 2. Towel holder installation
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Towel holder installation',99)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('towel-holder-modal').style.display='flex'">Add</button>'''
)
content = content.replace(
    '''<div id="towel-holder-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">''',
    '''<div id="towel-holder-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">'''
)
content = content.replace(
    '''<button id="close-towel-holder-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>''',
    '''<button id="close-towel-holder-modal-btn" onclick="document.getElementById('towel-holder-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>'''
)

# 3. Wash basin leakage repair
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Wash basin leakage repair',99)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('basin-leak-modal').style.display='flex'">Add</button>'''
)
content = content.replace(
    '''<div id="basin-leak-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">''',
    '''<div id="basin-leak-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">'''
)
content = content.replace(
    '''<button id="close-basin-leak-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>''',
    '''<button id="close-basin-leak-modal-btn" onclick="document.getElementById('basin-leak-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>'''
)

# 4. Waste coupling installation
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Waste coupling installation',149)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('waste-coupling-modal').style.display='flex'">Add</button>'''
)
content = content.replace(
    '''<div id="waste-coupling-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">''',
    '''<div id="waste-coupling-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">'''
)
content = content.replace(
    '''<button id="close-waste-coupling-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>''',
    '''<button id="close-waste-coupling-modal-btn" onclick="document.getElementById('waste-coupling-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>'''
)

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'w', encoding='utf-8') as f:
    f.write(content)
