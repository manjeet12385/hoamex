import os

js_code = """
// Force navigation for all modal items
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.modal-item').forEach(item => {
        item.addEventListener('click', (e) => {
            const href = item.getAttribute('href');
            if (href && href !== '#' && !href.startsWith('javascript')) {
                // Remove default action just in case something else is messing with it
                e.preventDefault();
                e.stopPropagation();
                window.location.href = href;
            }
        });
    });
});
"""

with open('common.js', 'a', encoding='utf-8') as f:
    f.write('\n' + js_code)
print("Updated common.js with explicit click handler for modal items")
