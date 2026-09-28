with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'a', encoding='utf-8') as f:
    f.write('''

/* ==========================================================================
   GLOBAL RESPONSIVE MEDIA QUERIES
   ========================================================================== */

/* Tablets and small laptops (max-width: 1024px) */
@media screen and (max-width: 1024px) {
    .three-col-layout {
        grid-template-columns: 200px 1fr !important; /* Hide right sidebar or move it */
    }
    .right-sidebar {
        display: none !important; /* Optionally hide cart sidebar on smaller screens initially */
    }
    .search-container {
        width: 30%;
    }
    .carousel-item {
        min-width: calc(50% - 10px);
    }
    .service-grid {
        grid-template-columns: repeat(2, 1fr) !important;
    }
}

/* Tablets portrait and large phones (max-width: 768px) */
@media screen and (max-width: 768px) {
    .header {
        flex-direction: column;
        padding: 10px 15px;
        gap: 10px;
    }
    body {
        padding-top: 130px; /* Adjust for taller header */
    }
    .search-container {
        width: 100%;
        order: 3; /* Move below logo and buttons */
    }
    .header-actions {
        width: 100%;
        justify-content: space-between;
    }
    .three-col-layout {
        grid-template-columns: 1fr !important;
        gap: 15px !important;
    }
    .left-sidebar {
        display: flex;
        overflow-x: auto;
        white-space: nowrap;
        border-right: none;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
    }
    .service-item-sidebar {
        display: inline-block;
        margin-right: 10px;
        margin-bottom: 0;
        min-width: 120px;
    }
    .carousel-item {
        min-width: 80%;
    }
    .modal-content {
        width: 95% !important;
        margin: 10px;
        padding: 15px !important;
    }
    .wm-options-carousel {
        padding-bottom: 15px;
    }
    .option-card {
        min-width: 140px !important;
    }
    .modal-grid {
        grid-template-columns: repeat(3, 1fr) !important;
    }
}

/* Small phones (max-width: 480px) */
@media screen and (max-width: 480px) {
    .header {
        padding: 10px;
    }
    .logo-text {
        font-size: 18px;
    }
    .location-btn, .partner-btn {
        padding: 8px 10px;
        font-size: 12px;
    }
    .icon-btn {
        width: 35px;
        height: 35px;
    }
    .carousel-item {
        min-width: 100%;
    }
    .service-grid {
        grid-template-columns: 1fr !important;
    }
    .svc-row {
        flex-direction: column;
    }
    .svc-media {
        width: 100%;
        margin-top: 15px;
    }
    .modal-grid {
        grid-template-columns: repeat(2, 1fr) !important;
    }
    .option-card {
        min-width: 100% !important;
    }
    #modal-carousel-drain, .wm-options-carousel {
        flex-direction: column;
    }
    .section-block {
        padding: 15px !important;
    }
}
''')
