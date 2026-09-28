import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

slider_fix = """
/* SLIDER SCROLL FIX */
.service-grid, .services-grid, .scroll-container {
    -webkit-overflow-scrolling: touch !important;
}
.service-item, .service-item-sidebar {
    flex-shrink: 0 !important;
}
@media (max-width: 768px) {
    .service-grid {
        display: flex !important;
        overflow-x: auto !important;
        flex-wrap: nowrap !important;
        gap: 15px !important;
        padding-bottom: 10px !important;
        -webkit-overflow-scrolling: touch !important;
    }
    .service-grid::-webkit-scrollbar {
        display: none !important;
    }
    .select-service-card {
        border: none !important;
        padding: 0 !important;
        background: transparent !important;
        overflow: hidden !important;
    }
    .select-service-card h3 {
        display: none !important;
    }
}
"""

if "SLIDER SCROLL FIX" not in css:
    css += "\n" + slider_fix
    with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Injected slider fixes into style.css")
else:
    print("Slider fixes already present")
