import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Append the new navbar styling for mobile
new_css = """
/* Exact Mobile Navbar Layout Override */
@media screen and (max-width: 768px) {
    .header {
        display: grid !important;
        grid-template-columns: auto 1fr auto auto !important;
        grid-template-rows: auto auto !important;
        row-gap: 15px !important;
        column-gap: 8px !important;
        padding: 15px 10px !important;
        align-items: center !important;
    }
    
    .header > div:first-child {
        grid-column: 1 / 2 !important;
        grid-row: 1 / 2 !important;
        margin-right: 0 !important;
    }
    
    .header-actions {
        display: contents !important;
    }
    
    .header-actions > .location-btn {
        grid-column: 2 / 3 !important;
        grid-row: 1 / 2 !important;
        justify-self: end !important;
        background-color: #f3e8ff !important;
        color: #6b21a8 !important;
        padding: 6px 10px !important;
        font-size: 11px !important;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 120px;
    }
    
    .header-actions > .icon-btn:nth-of-type(1) { /* User icon */
        grid-column: 3 / 4 !important;
        grid-row: 1 / 2 !important;
        width: 32px !important;
        height: 32px !important;
    }
    
    .header-actions > #open-cart-btn {
        grid-column: 4 / 5 !important;
        grid-row: 1 / 2 !important;
        width: 32px !important;
        height: 32px !important;
    }
    
    .header-actions > .partner-btn {
        grid-column: 1 / 2 !important;
        grid-row: 2 / 3 !important;
        padding: 8px 12px !important;
        font-size: 12px !important;
        border-radius: 8px !important;
        white-space: nowrap;
    }
    
    .search-container {
        grid-column: 2 / 5 !important;
        grid-row: 2 / 3 !important;
        width: 100% !important;
        margin-top: 0 !important;
        padding: 8px 12px !important;
        order: unset !important; /* Remove flex order */
    }
    
    /* Ensure no other display overrides take precedence */
    .location-btn, .partner-btn, .search-container {
        display: flex !important; 
    }
}
"""

content += new_css

with open(r'c:\Users\Divyanshi123456\Music\hoamex\style.css', 'w', encoding='utf-8') as f:
    f.write(content)
