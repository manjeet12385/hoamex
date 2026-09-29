import os

css_code = """
/* UNIQUE NAVBAR STYLES ADDED PER USER REQUEST */
.header.premium-navbar {
    position: fixed !important;
    top: 15px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 96% !important;
    max-width: 1200px !important;
    background: rgba(255, 255, 255, 0.85) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08), 0 1px 3px rgba(0,0,0,0.05) !important;
    transition: all 0.3s ease !important;
    padding: 12px 25px !important;
    z-index: 99999 !important;
}

.header.premium-navbar:hover {
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.12), 0 2px 5px rgba(0,0,0,0.05) !important;
}

/* Push body down so content doesn't hide behind floating navbar */
body {
    padding-top: 90px !important;
}

@media screen and (max-width: 768px) {
    .header.premium-navbar {
        top: 0 !important;
        width: 100% !important;
        border-radius: 0 !important;
        padding: 10px 15px !important;
    }
    body {
        padding-top: 140px !important; /* Extra space for mobile stacked header */
    }
}

/* UNIQUE ATTENTION-GRABBING PARTNER BUTTON */
@keyframes shakeAndGlow {
    0% { transform: scale(1) rotate(0deg); box-shadow: 0 0 0 rgba(37, 211, 102, 0); }
    10% { transform: scale(1.05) rotate(-3deg); box-shadow: 0 0 15px rgba(37, 211, 102, 0.6); }
    20% { transform: scale(1.05) rotate(3deg); box-shadow: 0 0 20px rgba(37, 211, 102, 0.8); }
    30% { transform: scale(1.05) rotate(-3deg); box-shadow: 0 0 15px rgba(37, 211, 102, 0.6); }
    40% { transform: scale(1.05) rotate(3deg); box-shadow: 0 0 20px rgba(37, 211, 102, 0.8); }
    50% { transform: scale(1) rotate(0deg); box-shadow: 0 0 0 rgba(37, 211, 102, 0); }
    100% { transform: scale(1) rotate(0deg); box-shadow: 0 0 0 rgba(37, 211, 102, 0); }
}

@keyframes pulseBg {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.header.premium-navbar .partner-btn {
    background: linear-gradient(270deg, #25D366, #128C7E, #4CAF50, #25D366) !important;
    background-size: 300% 300% !important;
    border: 2px solid white !important;
    border-radius: 30px !important;
    color: white !important;
    padding: 10px 22px !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    animation: pulseBg 4s ease infinite, shakeAndGlow 3s infinite !important;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4) !important;
}

.header.premium-navbar .partner-btn::after {
    content: '' !important;
    position: absolute !important;
    top: -50% !important;
    left: -150% !important;
    width: 200% !important;
    height: 200% !important;
    background: rgba(255,255,255,0.3) !important;
    transform: rotate(45deg) !important;
    animation: shineEffect 3s infinite !important;
}

@keyframes shineEffect {
    0% { left: -150%; }
    50% { left: 100%; }
    100% { left: 100%; }
}

.header.premium-navbar .partner-btn i {
    animation: hopIcon 1s ease-in-out infinite alternate !important;
    margin-right: 8px !important;
}

@keyframes hopIcon {
    0% { transform: translateY(0); }
    100% { transform: translateY(-3px); }
}

.header.premium-navbar .partner-btn:hover {
    transform: scale(1.1) !important;
    box-shadow: 0 8px 25px rgba(37, 211, 102, 0.7) !important;
    animation: pulseBg 2s ease infinite !important; /* Stop shaking on hover, just pulse fast */
}

/* Enhance Search Bar */
.header.premium-navbar .search-container {
    background: rgba(245, 245, 245, 0.7) !important;
    border-radius: 30px !important;
    border: 1px solid rgba(0,0,0,0.05) !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}
.header.premium-navbar .search-container:focus-within {
    background: #fff !important;
    border: 1px solid #128C7E !important;
    box-shadow: 0 4px 20px rgba(18, 140, 126, 0.15) !important;
    transform: translateY(-1px) !important;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n\n' + css_code)

print("Added unique navbar styles to style.css!")
