import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Indian toilet repair
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Indian toilet repair/installation',599)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('indian-toilet-modal').style.display='flex'">Add</button>'''
)
content = content.replace(
    '''<div id="indian-toilet-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">''',
    '''<div id="indian-toilet-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">'''
)
content = content.replace(
    '''<button id="close-indian-toilet-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>''',
    '''<button id="close-indian-toilet-modal-btn" onclick="document.getElementById('indian-toilet-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>'''
)

# 2. Western toilet repair (wall-mounted)
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Western toilet repair (wall-mounted)',599)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('wall-mounted-modal').style.display='flex'">Add</button>'''
)
content = content.replace(
    '''<div id="wall-mounted-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">''',
    '''<div id="wall-mounted-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">'''
)
content = content.replace(
    '''<button id="close-wall-mounted-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>''',
    '''<button id="close-wall-mounted-modal-btn" onclick="document.getElementById('wall-mounted-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>'''
)

# 3. Western toilet repair (floor-mounted)
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Western toilet repair (floor-mounted)',599)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('floor-mounted-modal').style.display='flex'">Add</button>'''
)
content = content.replace(
    '''<div id="floor-mounted-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">''',
    '''<div id="floor-mounted-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">'''
)
content = content.replace(
    '''<button id="close-floor-mounted-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>''',
    '''<button id="close-floor-mounted-modal-btn" onclick="document.getElementById('floor-mounted-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>'''
)

# 4. Jet spray repair/replacement
content = content.replace(
    '''<button class="add-btn" onclick="addToCart('Jet spray repair/replacement',89)">Add</button>''',
    '''<button class="add-btn" onclick="document.getElementById('jet-spray-modal').style.display='flex'">Add</button>'''
)
content = content.replace(
    '''<div id="jet-spray-modal" class="modal-overlay hidden" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: flex; align-items: center; justify-content: center;">''',
    '''<div id="jet-spray-modal" class="modal-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; display: none; align-items: center; justify-content: center;">'''
)
content = content.replace(
    '''<button id="close-jet-spray-modal-btn" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>''',
    '''<button id="close-jet-spray-modal-btn" onclick="document.getElementById('jet-spray-modal').style.display='none'" class="modal-close" style="position: absolute; top: 20px; right: 20px; background: transparent; border: none; font-size: 20px; cursor: pointer; color: #333;"><i class="fa-solid fa-xmark"></i></button>'''
)

with open(r'c:\Users\Divyanshi123456\Music\hoamex\plumber.html', 'w', encoding='utf-8') as f:
    f.write(content)
