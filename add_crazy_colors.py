import os

css_code = """
/* SUPER FLASHY COLOR CHANGING BUTTON */
@keyframes crazyColors {
    0% { background: #ff007f !important; box-shadow: 0 0 20px #ff007f !important; }
    16% { background: #7928ca !important; box-shadow: 0 0 25px #7928ca !important; }
    33% { background: #0070f3 !important; box-shadow: 0 0 20px #0070f3 !important; }
    50% { background: #00dfd8 !important; box-shadow: 0 0 25px #00dfd8 !important; }
    66% { background: #ff4d4d !important; box-shadow: 0 0 20px #ff4d4d !important; }
    83% { background: #ffea00 !important; box-shadow: 0 0 25px #ffea00 !important; color: #000 !important; }
    100% { background: #ff007f !important; box-shadow: 0 0 20px #ff007f !important; color: white !important; }
}

.header.premium-navbar .partner-btn {
    animation: crazyColors 2s infinite, shakeAndGlow 3s infinite !important;
    border: 2px solid white !important;
    color: white !important;
}

.header.premium-navbar .partner-btn:hover {
    animation: crazyColors 0.5s infinite !important;
    transform: scale(1.15) !important;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n\n' + css_code)

print("Added crazy colors to style.css!")
