import os

css_append = """
/* Super Animated Partner Button */
.premium-navbar .partner-btn {
    /* 1. Moving Gradient */
    background: linear-gradient(270deg, #ff007f, #7928ca, #ff4d4d, #ff9a00) !important;
    background-size: 300% 300% !important;
    animation: movingGradient 4s ease infinite, pulseWiggle 4s infinite !important;
    
    border: none !important;
    border-radius: 30px !important;
    color: white !important;
    padding: 10px 22px !important;
    font-weight: 800 !important;
    position: relative !important;
    overflow: hidden !important;
    z-index: 1 !important;
    box-shadow: 0 0 15px rgba(121, 40, 202, 0.6) !important;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.3) !important;
    transition: all 0.3s ease !important;
}

/* Animations */
@keyframes movingGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes pulseWiggle {
    0%, 80%, 100% { transform: scale(1) rotate(0deg); }
    85% { transform: scale(1.08) rotate(-3deg); box-shadow: 0 0 25px rgba(255, 0, 127, 0.8) !important; }
    90% { transform: scale(1.08) rotate(3deg); }
    95% { transform: scale(1.08) rotate(-3deg); }
}

/* Sweeping Shine Effect */
.premium-navbar .partner-btn::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important;
    left: -150% !important;
    width: 60% !important;
    height: 100% !important;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent) !important;
    transform: skewX(-20deg) !important;
    animation: shineSweep 4s infinite !important;
    z-index: -1 !important;
}

@keyframes shineSweep {
    0%, 60% { left: -150%; }
    100% { left: 150%; }
}

/* Hover Effect Override */
.premium-navbar .partner-btn:hover {
    transform: scale(1.15) !important;
    box-shadow: 0 0 35px rgba(255, 154, 0, 0.9) !important;
    animation: movingGradient 1.5s ease infinite !important; /* Faster color change on hover */
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_append)
print("Updated style.css with dynamic button animations")
