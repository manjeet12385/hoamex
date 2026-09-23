with open('style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* ------------------------------------- */
/* Mobile Responsiveness & Layout Refactor */
/* ------------------------------------- */

/* Page Layout */
.page-wrapper { max-width: 1200px; margin: 0 auto; padding: 30px 20px; }
.top-section { display: flex; align-items: flex-start; gap: 20px; margin-bottom: 40px; }
.page-title { font-size: 32px; font-weight: 700; line-height: 1.2; margin: 0 0 8px 0; }
.page-rating { display: flex; align-items: center; gap: 5px; font-size: 14px; color: #333; }
.page-rating i { color: #f39c12; }
.page-rating span { color: #666; }

/* 3-column layout */
.three-col-layout { display: grid; grid-template-columns: 260px 1fr 220px; gap: 24px; align-items: start; }

/* Left sidebar */
.left-sidebar { position: sticky; top: 80px; }
.select-service-card { border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px; background: white; }
.select-service-card h3 { font-size: 13px; color: #64748b; font-weight: 500; margin: 0 0 14px 0; }
.service-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
.service-item-sidebar { text-align: center; cursor: pointer; text-decoration: none; color: inherit; }
.service-item-img { width: 52px; height: 52px; border-radius: 8px; overflow: hidden; margin: 0 auto 6px; background: #f8f9fa; display: flex; align-items: center; justify-content: center; border: 1px solid #eee; }
.service-item-img img { width: 100%; height: 100%; object-fit: cover; }
.service-item-sidebar span { font-size: 11px; font-weight: 500; line-height: 1.3; display: block; }

/* Center content */
.center-content {}

/* Banner */
.uc-difference-banner { background: #e8e8e8; border-radius: 14px; padding: 30px; margin-bottom: 30px; position: relative; display: flex; align-items: center; justify-content: flex-start; overflow: hidden; min-height: 250px; background-size: cover; background-position: center; color: white;}
.uc-difference-banner::before {
    content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to right, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.1) 100%); z-index: 1;
}
.banner-text { position: relative; z-index: 2; width: 60%; text-align: left; padding-left: 20px; }
.banner-text h2 { font-size: 34px; font-weight: 700; margin: 0; line-height: 1.2; text-shadow: 1px 1px 4px rgba(0,0,0,0.3); }

/* Service sections */
.section-heading { font-size: 22px; font-weight: 700; margin: 0 0 16px 0; }
.service-card { border: 1px solid #eee; border-radius: 12px; padding: 20px; display: flex; justify-content: space-between; gap: 16px; margin-bottom: 16px; background: white; }
.service-card-info { flex: 1; }
.service-card-info h4 { font-size: 17px; font-weight: 700; margin: 0 0 6px 0; }
.service-rating { font-size: 13px; color: #666; margin-bottom: 4px; }
.service-rating i { color: #1a1a1a; }
.service-rating a { color: #6366f1; text-decoration: underline dotted; }
.service-price { font-size: 14px; font-weight: 600; margin-bottom: 12px; color: #111; }
.service-price span { font-size: 13px; font-weight: 400; color: #666; }
.service-features { list-style: none; padding: 0; margin: 0 0 12px 0; }
.service-features li { font-size: 13px; color: #666; padding: 3px 0; padding-left: 14px; position: relative; }
.service-features li::before { content: '•'; position: absolute; left: 0; color: #999; }
.view-details { color: #6366f1; font-size: 13px; font-weight: 600; text-decoration: none; }
.service-img-wrap { width: 120px; height: 120px; border-radius: 12px; overflow: hidden; margin-bottom: -15px; position: relative; z-index: 1; }
.service-img-wrap img { width: 100%; height: 100%; object-fit: cover; }
.add-btn { padding: 8px 28px; background: white; border: 1px solid #ddd; color: #6366f1; font-weight: 700; border-radius: 8px; cursor: pointer; font-size: 14px; position: relative; z-index: 2; box-shadow: 0 2px 6px rgba(0,0,0,0.08); width: 100%; transition: background 0.2s; }
.add-btn:hover { background: #f3f4f6; }

/* Right sidebar */
.right-sidebar { position: sticky; top: 80px; }
.uc-promise-card { border: 1px solid #eee; border-radius: 10px; padding: 18px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: flex-start; background: white; }
.uc-promise-card h3 { font-size: 15px; font-weight: 700; margin: 0 0 10px 0; }
.uc-promise-card ul { list-style: none; padding: 0; margin: 0; }
.uc-promise-card ul li { font-size: 13px; color: #555; margin-bottom: 6px; display: flex; align-items: center; gap: 7px; }
.uc-promise-card ul li i { color: #00875a; font-size: 12px; }
.promise-badge { width: 52px; height: 52px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
.cart-card { border: 1px solid #eee; border-radius: 10px; padding: 20px; text-align: center; color: #999; background: white; }
.cart-card i { font-size: 28px; margin-bottom: 8px; display: block; }
.cart-card p { font-size: 13px; margin: 0; }

/* ------------------------------------- */
/* Mobile Media Queries */
/* ------------------------------------- */
@media (max-width: 768px) {
    /* Header */
    .header { padding: 15px 20px; }
    .search-container { display: none; } /* Hide search bar on mobile for space */
    .location-btn span { display: none; } /* Hide text, keep icon */
    
    /* Layout */
    .three-col-layout { display: flex; flex-direction: column; gap: 0; }
    
    /* Right Sidebar (Hide completely on mobile, use floating cart instead) */
    .right-sidebar { display: none; }
    
    /* Left Sidebar (Scrollable horizontal strip) */
    .left-sidebar { position: sticky; top: 60px; z-index: 90; margin-bottom: 20px; background: #f7f9fa; padding: 10px 0; width: 100%; border-bottom: 1px solid #eee; }
    .select-service-card { border: none; padding: 0; background: transparent; }
    .select-service-card h3 { display: none; }
    .service-grid { display: flex; flex-wrap: nowrap; overflow-x: auto; gap: 15px; padding-bottom: 5px; scrollbar-width: none; }
    .service-grid::-webkit-scrollbar { display: none; }
    .service-item-sidebar { min-width: 70px; }
    
    /* Service Cards */
    .service-card { flex-direction: column; padding: 15px; }
    .service-card > div:last-child { width: 100%; display: flex; justify-content: space-between; align-items: center; flex-direction: row-reverse; margin-top: 15px; }
    .service-img-wrap { width: 80px; height: 80px; margin-bottom: 0; margin-left: 15px; }
    .add-btn { width: auto; padding: 8px 20px; margin-top: 0; }
    
    /* Grid container on homepage */
    .services-grid { grid-template-columns: repeat(3, 1fr); gap: 20px 10px; }
}

@media (max-width: 480px) {
    .services-grid { grid-template-columns: repeat(2, 1fr); }
    .top-section { flex-direction: column; }
}
''')
