import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

responsive_rules = """
/* UNIVERSAL RESPONSIVE FIXES */
html, body {
    overflow-x: hidden !important;
}
img {
    max-width: 100%;
    height: auto;
}
.modal-content, .service-card, .plan-card, .option-card, .noteworthy-item, .spotlight-card, .most-booked-item {
    max-width: 100% !important;
    box-sizing: border-box !important;
}
p, h1, h2, h3, h4, h5, h6, span, div {
    overflow-wrap: break-word;
    word-wrap: break-word;
}
@media (max-width: 768px) {
    .ac-service-layout, .three-col-layout, .page-layout, .plumber-layout, .kitchen-layout {
        display: flex !important;
        flex-direction: column !important;
        width: 100% !important;
        padding: 10px !important;
    }
    .ac-left-col, .ac-main-content, .ac-right-col, .left-sidebar, .right-sidebar, .main-content {
        width: 100% !important;
        max-width: 100% !important;
        min-width: 100% !important;
    }
    .modal-content {
        padding: 15px !important;
        width: 100% !important;
    }
    .services-grid, .modal-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 10px !important;
    }
    .add-btn, .option-add-btn {
        width: 100% !important;
        max-width: 100px !important;
    }
}
@media (max-width: 480px) {
    .services-grid, .modal-grid {
        grid-template-columns: repeat(2, 1fr) !important;
    }
    .spotlight-card, .noteworthy-item, .most-booked-item {
        min-width: 200px !important;
    }
}
"""

if "UNIVERSAL RESPONSIVE FIXES" not in css:
    css += "\n" + responsive_rules
    with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Injected global responsive fixes into style.css")
else:
    print("Responsive fixes already present")
