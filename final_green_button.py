import os

css_code = """
/* FINAL FIX FOR PARTNER BUTTON - BACK TO GREEN BUT ANIMATED */
.header.premium-navbar .partner-btn {
    /* Solid, attention-grabbing green gradient */
    background: linear-gradient(135deg, #25D366, #128C7E) !important;
    background-size: 200% 200% !important;
    border: none !important;
    color: white !important;
    padding: 10px 22px !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    border-radius: 30px !important;
    box-shadow: 0 4px 15px rgba(37, 211, 102, 0.5) !important;
    
    /* Just a nice pulse and shake */
    animation: greenPulse 1.5s infinite, mildShake 4s infinite !important;
}

@keyframes greenPulse {
    0% { background-position: 0% 50%; box-shadow: 0 4px 15px rgba(37, 211, 102, 0.5) !important; }
    50% { background-position: 100% 50%; box-shadow: 0 4px 25px rgba(37, 211, 102, 0.9) !important; transform: scale(1.05); }
    100% { background-position: 0% 50%; box-shadow: 0 4px 15px rgba(37, 211, 102, 0.5) !important; }
}

@keyframes mildShake {
    0% { transform: rotate(0deg); }
    2% { transform: rotate(-3deg) scale(1.05); }
    4% { transform: rotate(3deg) scale(1.05); }
    6% { transform: rotate(-3deg) scale(1.05); }
    8% { transform: rotate(3deg) scale(1.05); }
    10% { transform: rotate(0deg); }
    100% { transform: rotate(0deg); }
}

.header.premium-navbar .partner-btn:hover {
    transform: scale(1.1) !important;
    animation: greenPulse 0.8s infinite !important; /* Fast pulse on hover */
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n\n' + css_code)

print("Applied final green animated button fix.")
