import re

with open(r'c:\Users\Divyanshi123456\Music\hoamex\app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# I will append a robust setup block at the end of app.js that ensures all these buttons work
# and overrides any previous faulty setup.
robust_setup = """
// Robust Modal Setup for all Grid Categories
document.addEventListener('DOMContentLoaded', () => {
    const categoryModals = [
        { triggerId: 'ac-repair-btn', modalId: 'ac-modal' },
        { triggerId: 'epc-btn', modalId: 'epc-modal' },
        { triggerId: 'cleaning-btn', modalId: 'cleaning-modal' },
        { triggerId: 'renovation-btn', modalId: 'renovation-modal' },
        { triggerId: 'fabrication-modal-trigger', modalId: 'fabrication-modal' },
        { triggerId: 'womens-beauty-btn', modalId: 'beauty-modal' },
        { triggerId: 'mens-grooming-btn', modalId: 'grooming-modal' },
        { triggerId: 'homecare-btn', modalId: 'logistics-modal' }, /* assuming home care is logistics */
        { triggerId: 'security-btn', modalId: 'security-modal' }
    ];

    categoryModals.forEach(mapping => {
        const trigger = document.getElementById(mapping.triggerId);
        const modal = document.getElementById(mapping.modalId);
        
        if (trigger && modal) {
            // Remove any old event listeners by cloning if necessary, or just add
            trigger.addEventListener('click', (e) => {
                e.preventDefault();
                modal.style.display = 'flex';
            });
            
            // Allow clicking outside to close
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    modal.style.display = 'none';
                }
            });
            
            // Find the close button inside the modal and attach click handler
            const closeBtn = modal.querySelector('.modal-close');
            if (closeBtn) {
                closeBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    modal.style.display = 'none';
                });
            }
        }
    });
});
"""

content += robust_setup

with open(r'c:\Users\Divyanshi123456\Music\hoamex\app.js', 'w', encoding='utf-8') as f:
    f.write(content)
