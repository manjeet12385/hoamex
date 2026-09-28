with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_fix = """
/* ============================================
   COMPREHENSIVE MOBILE CUT-OFF FIX
   ============================================ */

/* Prevent ALL horizontal overflow */
*, *::before, *::after {
    max-width: 100%;
    box-sizing: border-box !important;
}
html, body {
    overflow-x: hidden !important;
    max-width: 100vw !important;
}

/* Plan card / service card layout on mobile */
@media (max-width: 640px) {
    /* Fix plan-header: stack price and button below text */
    .plan-header {
        flex-direction: column !important;
        gap: 12px !important;
    }
    .plan-header > * {
        width: 100% !important;
    }

    /* Fix service card layout */
    .service-card {
        flex-direction: column !important;
        gap: 12px !important;
    }
    .service-img-wrap {
        width: 100% !important;
        height: 160px !important;
        margin-bottom: 0 !important;
    }

    /* Fix plan details card */
    .plan-details-card {
        padding: 12px !important;
        overflow: hidden !important;
    }

    /* Fix add button overflow */
    .add-btn, .option-add-btn {
        width: auto !important;
        min-width: 80px !important;
        max-width: 120px !important;
    }

    /* Fix image on banner cards */
    .ac-right-col img,
    .ac-banner-img {
        width: 100% !important;
        max-height: 200px !important;
        object-fit: cover !important;
    }

    /* Fix 3-col layout cards */
    .ac-service-layout,
    .ac-details-section,
    .three-col-layout,
    .page-layout {
        display: flex !important;
        flex-direction: column !important;
        width: 100% !important;
        overflow: hidden !important;
        padding: 10px !important;
        gap: 15px !important;
    }

    .ac-left-col, .ac-main-content, .ac-right-col,
    .left-sidebar, .main-content, .center-content {
        width: 100% !important;
        max-width: 100% !important;
        min-width: unset !important;
    }

    /* Fix spotlight cards overflow */
    .spotlight-card {
        min-width: 80vw !important;
        max-width: 90vw !important;
    }

    /* Fix noteworthy/most booked cards */
    .noteworthy-item {
        min-width: 45vw !important;
        max-width: 50vw !important;
    }
    .most-booked-item {
        min-width: 200px !important;
        max-width: 220px !important;
    }

    /* Fix option cards */
    .option-card {
        min-width: 130px !important;
        max-width: 160px !important;
    }

    /* Fix AC service page top section */
    .ac-page-header {
        flex-direction: column !important;
        gap: 10px !important;
    }
    .ac-page-header > * {
        width: 100% !important;
    }

    /* Fix horizontal scrolling containers */
    .ac-service-scroll,
    .ac-service-grid {
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
    }

    /* Ensure no text overflows */
    h1, h2, h3, h4, h5, h6, p, span, li, a {
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        max-width: 100% !important;
    }

    /* Fix images inside cards */
    .plan-details-card img,
    .service-card img,
    .plan-card img {
        max-width: 100% !important;
        height: auto !important;
    }
}

@media (max-width: 480px) {
    .noteworthy-item {
        min-width: 48vw !important;
        max-width: 50vw !important;
    }
    .spotlight-card {
        min-width: 85vw !important;
    }
    .section-heading {
        font-size: 18px !important;
    }
}
"""

if "COMPREHENSIVE MOBILE CUT-OFF FIX" not in css:
    css += "\n" + mobile_fix
    with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Comprehensive mobile fix injected!")
else:
    print("Already present")
