import os

css_code = """
/* DEFINITIVE FIX FOR PARTNER BUTTON COLORS */
@keyframes crazyColorsSolid {
    0% { background-color: #ff007f !important; background-image: none !important; box-shadow: 0 0 20px #ff007f !important; }
    16% { background-color: #7928ca !important; background-image: none !important; box-shadow: 0 0 25px #7928ca !important; }
    33% { background-color: #0070f3 !important; background-image: none !important; box-shadow: 0 0 20px #0070f3 !important; }
    50% { background-color: #00dfd8 !important; background-image: none !important; box-shadow: 0 0 25px #00dfd8 !important; }
    66% { background-color: #ff4d4d !important; background-image: none !important; box-shadow: 0 0 20px #ff4d4d !important; }
    83% { background-color: #ffea00 !important; background-image: none !important; box-shadow: 0 0 25px #ffea00 !important; color: #000 !important; }
    100% { background-color: #ff007f !important; background-image: none !important; box-shadow: 0 0 20px #ff007f !important; color: white !important; }
}

.header.premium-navbar .partner-btn {
    background: none !important;
    background-image: none !important;
    animation: crazyColorsSolid 1.5s infinite, shakeAndGlow 3s infinite !important;
}

.header.premium-navbar .partner-btn:hover {
    animation: crazyColorsSolid 0.5s infinite !important;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n\n' + css_code)

print("Applied definitive crazy color override.")
