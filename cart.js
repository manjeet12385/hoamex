document.addEventListener('DOMContentLoaded', () => {
    let cart = JSON.parse(localStorage.getItem('joamex_cart')) || [];
    
    // Normalize old cart items to have quantity if they don't
    cart = cart.map(item => {
        if (!item.quantity) item.quantity = 1;
        // Also use title as unique id for grouping if possible, but let's just group by title
        return item;
    });
    
    // Normalize titles: trim + lowercase for consistent matching
    const normalizeTitle = (t) => (t || '').trim().toLowerCase();

    // Deduplicate by normalized title
    const uniqueCart = [];
    cart.forEach(item => {
        const existing = uniqueCart.find(i => normalizeTitle(i.title) === normalizeTitle(item.title));
        if (existing) {
            existing.quantity += item.quantity;
        } else {
            uniqueCart.push(item);
        }
    });
    cart = uniqueCart;
    saveCart();

    // Expose normalizeTitle globally for use in other functions
    window._normalizeCartTitle = normalizeTitle;

    const cartSidebar = document.getElementById('cart-sidebar');
    const closeCartBtn = document.getElementById('close-cart-btn');
    const cartItemsContainer = document.getElementById('cart-items-container');
    const cartTotalPrice = document.getElementById('cart-total-price');
    const checkoutBtn = document.getElementById('checkout-btn');

    // Make sure basic add buttons (without onclick) work on the page
    document.querySelectorAll('.add-btn, .option-add-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const onclickAttr = btn.getAttribute('onclick') || '';
            if (onclickAttr.includes('modal') || onclickAttr.includes('addToCart')) return;

            const card = e.target.closest('.service-card') || e.target.closest('.svc-row') || e.target.closest('.plan-card') || e.target.closest('.option-card') || e.target.closest('.most-booked-item');
            if (card) {
                const titleEl = card.querySelector('h4, h3');
                if (!titleEl) return;
                const title = titleEl.innerText;
                
                let price = 0;
                const priceEl = card.querySelector('.service-price span, .price span, .plan-price, .option-price');
                if (priceEl) {
                    const priceText = priceEl.innerText;
                    // First try to match ₹ followed by numbers to avoid matching '50% OFF'
                    const priceMatch = priceText.match(/₹\s*(\d+(,\d+)?)/) || priceText.match(/\d+(,\d+)?/);
                    if (priceMatch) {
                        // priceMatch[1] contains the number if ₹ was matched, otherwise priceMatch[0]
                        const rawNumber = priceMatch[1] || priceMatch[0];
                        price = parseInt(rawNumber.replace(',', ''));
                    }
                }
                
                const imgEl = card.querySelector('img');
                const imgSrc = imgEl ? imgEl.src : 'images/new_plumber_icon.jpg';

                window.addToCart(title, price, imgSrc, false);
            }
        });
    });

    if (closeCartBtn && cartSidebar) {
        closeCartBtn.addEventListener('click', () => cartSidebar.style.display = 'none');
        cartSidebar.addEventListener('click', (e) => {
            if (e.target === cartSidebar) cartSidebar.style.display = 'none';
        });
    }

    if (checkoutBtn) {
        checkoutBtn.addEventListener('click', () => {
            const currentCart = JSON.parse(localStorage.getItem('joamex_cart')) || [];
            if (currentCart.length === 0) {
                alert("Your cart is empty!");
                return;
            }
            
            // Mandatory User Login Check
            const existingUser = localStorage.getItem('userEmail') || localStorage.getItem('userPhone');
            if(!existingUser) {
                // Not logged in -> Show login modal
                localStorage.setItem('loginRedirect', 'checkout');
                const loginModal = document.getElementById('user-login-modal');
                if(loginModal) {
                    loginModal.style.display = 'flex';
                    if(cartSidebar) cartSidebar.style.display = 'none'; // hide cart so modal is visible clearly
                } else {
                    alert('Please login first to proceed to checkout!');
                }
                return;
            }

            // Already logged in -> Proceed to checkout
            window.location.href = 'checkout';
        });
    }

    const openCartBtn = document.getElementById('open-cart-btn');
    if (openCartBtn && cartSidebar) {
        openCartBtn.addEventListener('click', () => openCart());
    }
    updateCartUI();

    function openCart() {
        if (cartSidebar) cartSidebar.style.display = 'flex';
    }

    function saveCart() {
        localStorage.setItem('joamex_cart', JSON.stringify(cart));
    }

    function updateCartUI() {
        const badge = document.getElementById('cart-badge');
        
        // Calculate total items
        let totalItems = 0;
        let totalPrice = 0;
        cart.forEach(item => {
            totalItems += item.quantity;
            totalPrice += (item.price * item.quantity);
        });

        if (badge) {
            badge.innerText = totalItems;
            badge.style.display = totalItems > 0 ? 'block' : 'none';
        }

        if (cartItemsContainer) {
            if (cart.length === 0) {
                cartItemsContainer.innerHTML = '<p style="text-align:center; color:#999; margin-top:50px;">Your cart is empty</p>';
                if (cartTotalPrice) cartTotalPrice.innerText = '₹0';
            } else {
                let html = '';
                cart.forEach(item => {
                    const safeTitle = item.title.replace(/'/g, "\\'");
                    html += `
                        <div style="display: flex; gap: 15px; margin-bottom: 20px; align-items: center;">
                            <img src="${item.imgSrc}" style="width: 50px; height: 50px; border-radius: 8px; object-fit: cover;">
                            <div style="flex: 1;">
                                <div style="font-weight: 600; font-size: 14px;">${item.title}</div>
                                <div style="font-weight: bold; margin-top: 5px;">₹${item.price}</div>
                            </div>
                            
                            <div style="display: flex; align-items: center; border: 1px solid #ddd; border-radius: 6px; overflow: hidden;">
                                <button onclick="decreaseQuantity('${safeTitle}')" style="width: 25px; height: 25px; background: #fff; border: none; cursor: pointer; color: #555; font-weight: bold;">-</button>
                                <span style="width: 25px; text-align: center; font-size: 13px; font-weight: 600; background: #f9f9f9; height: 25px; line-height: 25px;">${item.quantity}</span>
                                <button onclick="increaseQuantity('${safeTitle}')" style="width: 25px; height: 25px; background: #fff; border: none; cursor: pointer; color: #555; font-weight: bold;">+</button>
                            </div>
                        </div>
                    `;
                });
                cartItemsContainer.innerHTML = html;
                if (cartTotalPrice) cartTotalPrice.innerText = '₹' + totalPrice.toLocaleString();
            }
        }
        
        syncButtonsOnPage();
    }

    function syncButtonsOnPage() {
        document.querySelectorAll('.add-btn, .option-add-btn, button[onclick^="addToCart"]').forEach(btn => {
            const onclickAttr = btn.getAttribute('onclick') || '';
            let title = '';
            
            // Try to extract title from onclick="addToCart('Title', price)"
            const match = onclickAttr.match(/addToCart\s*\(\s*['"]([^'"]+)['"]/);
            if (match && match[1]) {
                title = match[1];
            } else {
                // If it relies on DOM structure
                const card = btn.closest('.service-card') || btn.closest('.svc-row') || btn.closest('.plan-card') || btn.closest('.option-card') || btn.closest('.most-booked-item');
                if (card) {
                    const titleEl = card.querySelector('h4, h3');
                    if (titleEl) title = titleEl.innerText;
                }
            }
            
            if (!title) return;
            
            const cartItem = cart.find(i => window._normalizeCartTitle(i.title) === window._normalizeCartTitle(title));
            const parent = btn.parentElement;
            
            // Check if qty-control already exists next to this button
            let qtyCtrl = parent.querySelector('.qty-control-inline');
            
            if (cartItem && cartItem.quantity > 0) {
                // Hide the Add button
                btn.style.display = 'none';
                
                if (!qtyCtrl) {
                    qtyCtrl = document.createElement('div');
                    qtyCtrl.className = 'qty-control-inline';
                    let extraStyles = '';
                    if (btn.style.position === 'absolute') {
                        extraStyles = `position: absolute; bottom: ${btn.style.bottom}; left: ${btn.style.left}; transform: ${btn.style.transform}; z-index: ${btn.style.zIndex || 2}; margin: ${btn.style.margin};`;
                    }
                    qtyCtrl.style.cssText = `display: flex; align-items: center; justify-content: space-between; width: 90px; background: #fdf5ff; border: 1.5px solid #d0d5ff; border-radius: 7px; overflow: hidden; height: 35px; margin: 0 auto; box-shadow: 0 2px 4px rgba(0,0,0,0.05); ${extraStyles}`;
                    // We insert it right after the button
                    btn.parentNode.insertBefore(qtyCtrl, btn.nextSibling);
                }
                
                const safeTitle = title.replace(/'/g, "\\'");
                qtyCtrl.innerHTML = `
                    <button onclick="decreaseQuantity('${safeTitle}', event)" style="width: 25px; height: 100%; background: none; border: none; color: #6366f1; font-weight: bold; cursor: pointer; font-size: 16px;">-</button>
                    <span style="font-weight: bold; font-size: 14px; color: #6366f1;">${cartItem.quantity}</span>
                    <button onclick="increaseQuantity('${safeTitle}', event)" style="width: 25px; height: 100%; background: none; border: none; color: #6366f1; font-weight: bold; cursor: pointer; font-size: 16px;">+</button>
                `;
            } else {
                // Show the Add button
                btn.style.display = '';
                if (qtyCtrl) {
                    qtyCtrl.remove();
                }
            }
        });
    }

    window.decreaseQuantity = function(title, event) {
        if (event) {
            event.stopPropagation();
            event.preventDefault();
        }
        const item = cart.find(i => window._normalizeCartTitle(i.title) === window._normalizeCartTitle(title));
        if (item) {
            item.quantity--;
            if (item.quantity <= 0) {
                cart = cart.filter(i => window._normalizeCartTitle(i.title) !== window._normalizeCartTitle(title));
            }
            saveCart();
            updateCartUI();
        }
    };

    window.increaseQuantity = function(title, event) {
        if (event) {
            event.stopPropagation();
            event.preventDefault();
        }
        const item = cart.find(i => window._normalizeCartTitle(i.title) === window._normalizeCartTitle(title));
        if (item) {
            item.quantity++;
            saveCart();
            updateCartUI();
        } else {
            // It shouldn't be null here if it's already in the UI, but just in case
        }
    };

    window.removeFromCart = function(id) {
        // Find by id (old logic, though we group by title now, let's just filter by id)
        cart = cart.filter(item => item.id !== id);
        saveCart();
        updateCartUI();
    };

    function getCategoryFromUrl(title = '') {
        const path = window.location.pathname.toLowerCase();
        const t = title.toLowerCase();
        
        // Smart title-based overrides for shared pages
        if (t.includes('haircut') || t.includes('shave') || t.includes('beard') || t.includes('pedicure') || t.includes('facial') || t.includes('salon')) {
            if (path.includes('men') || path.includes('grooming')) return 'Salon for Men';
            if (path.includes('women') || path.includes('beauty')) return 'Salon for Women';
        }
        if (t.includes('massage') || t.includes('spa') || t.includes('therapy')) {
            if (path.includes('men') || path.includes('grooming')) return 'Massage for Men';
            if (path.includes('women') || path.includes('beauty')) return 'Spa for Women';
        }

        if (path.includes('men-') || path.includes('-men')) {
            if (path.includes('spa') || path.includes('massage') || path.includes('grooming')) return 'Massage for Men';
            if (path.includes('salon')) return 'Salon for Men';
        }
        if (path.includes('women') || path.includes('spa') || path.includes('salon') || path.includes('beauty') || path.includes('makeup') || path.includes('hair')) {
            if (path.includes('spa') || path.includes('massage')) return 'Spa for Women';
            if (path.includes('salon') || path.includes('beauty')) return 'Salon for Women';
            if (path.includes('makeup')) return 'Makeup, Saree & Styling';
            if (path.includes('hair')) return 'Hair Studio for Women';
        }

        const map = {
            'ac-service': 'AC', 'ac-repair': 'AC', 'refrigerator': 'Refrigerator', 'fridge': 'Refrigerator',
            'washing-machine': 'Washing Machine', 'microwave': 'Microwave', 'water-purifier': 'RO/Water Purifier',
            'ro-service': 'RO/Water Purifier', 'geyser': 'Geyser Service & Repair', 'television': 'Television', 'chimney': 'Chimney',
            'electrician': 'Electrician', 'plumber': 'Plumber', 'carpenter': 'Carpenter', 'fan-installation': 'Fan Installation', 
            'leak': 'Leak & gap sealing', 'water-tank': 'Water Tank Cleaning', 'wood-polish': 'Wood & Furniture Polish', 'wood-furniture': 'Wood & Furniture Polish',
            'furniture': 'Furniture Assembly', 'ikea': 'IKEA Furniture Assembly', 'tile-grouting': 'Tile Grouting & Sealant', 'festival-lights': 'Festival Lights Installation',
            'full-home-cleaning': 'Full Home/ By Room Cleaning', 'living-bedroom': 'Living & Bedroom Cleaning', 'bathroom-cleaning': 'Bathroom Cleaning', 
            'kitchen-cleaning': 'Kitchen cleaning', 'cleaning': 'Full Home/ By Room Cleaning', 'cockroach': 'Cockroach Control', 
            'ants': 'Ants & Bed Bugs Control', 'termite': 'Termite Control', 'pest': 'Ants & Bed Bugs Control', 
            'painting': 'Walls & Rooms Painting', 'wall-panel': 'Wall Panels by Revamp', 'grouting': 'Tile Grouting & Sealant',
            'gates-door': 'Gates & Doors', 'grills': 'Window Grills & Balcony Railings', 'welding': 'Welding & Repair', 'sheds': 'Sheds & Roofing',
            'maid': 'Maid / Helper', 'cook': 'Cook on Demand', 'babysit': 'Babysitting / Nanny', 'elder': 'Elder / Patient Care', 'packers': 'Packers & Movers',
            'mini-truck': 'Mini Truck on Rent', 'logistics': 'Mini Truck on Rent', 'driver': 'Driver on Demand', 
            'cctv': 'CCTV Camera Installation', 'smart-lock': 'Smart Locks & Doorbells', 'home-alarm': 'Home Alarm Systems', 'solar-install': 'Solar Panel Installation',
            'solar-clean': 'Solar Panel Cleaning', 'solar-water': 'Solar Water Heater',
            'water-solution': 'RO / Water Purifier'
        };
        for (let key in map) {
            if (path.includes(key)) return map[key];
        }
        return 'General';
    }

    window.addToCart = function(title, price, passedImgSrc = null, openSidebar = false) {
        let imgSrc = passedImgSrc;
        if (!imgSrc) {
            imgSrc = 'images/new_plumber_icon.jpg'; // fallback
            try {
                const safeTitle = title.replace(/"/g, '\\"');
                const imgEl = document.querySelector(`img[alt="${safeTitle}"]`);
                if (imgEl && imgEl.src) {
                    imgSrc = imgEl.src;
                }
            } catch(e) {}
        }
        
        const category = getCategoryFromUrl(title);
        const existing = cart.find(i => window._normalizeCartTitle(i.title) === window._normalizeCartTitle(title));
        if (existing) {
            existing.quantity++;
            existing.category = category;
        } else {
            cart.push({ title, price, imgSrc, category, quantity: 1, id: Date.now() });
        }
        
        saveCart();
        updateCartUI();
        
        if (openSidebar) {
            openCart();
        }
    };
});
