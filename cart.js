document.addEventListener('DOMContentLoaded', () => {
    let cart = JSON.parse(localStorage.getItem('joamex_cart')) || [];
    
    // Normalize old cart items to have quantity if they don't
    cart = cart.map(item => {
        if (!item.quantity) item.quantity = 1;
        // Also use title as unique id for grouping if possible, but let's just group by title
        return item;
    });
    
    // Deduplicate by title just in case there were duplicates in old local storage
    const uniqueCart = [];
    cart.forEach(item => {
        const existing = uniqueCart.find(i => i.title === item.title);
        if (existing) {
            existing.quantity += item.quantity;
        } else {
            uniqueCart.push(item);
        }
    });
    cart = uniqueCart;
    saveCart();

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
                    const priceMatch = priceText.match(/\d+(,\d+)?/);
                    if (priceMatch) {
                        price = parseInt(priceMatch[0].replace(',', ''));
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
            if (cart.length === 0) {
                alert("Your cart is empty!");
                return;
            }
            window.location.href = 'checkout.html';
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
            
            const cartItem = cart.find(i => i.title === title);
            const parent = btn.parentElement;
            
            // Check if qty-control already exists next to this button
            let qtyCtrl = parent.querySelector('.qty-control-inline');
            
            if (cartItem && cartItem.quantity > 0) {
                // Hide the Add button
                btn.style.display = 'none';
                
                if (!qtyCtrl) {
                    qtyCtrl = document.createElement('div');
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
        const item = cart.find(i => i.title === title);
        if (item) {
            item.quantity--;
            if (item.quantity <= 0) {
                cart = cart.filter(i => i.title !== title);
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
        const item = cart.find(i => i.title === title);
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
        
        const existing = cart.find(i => i.title === title);
        if (existing) {
            existing.quantity++;
        } else {
            cart.push({ title, price, imgSrc, quantity: 1, id: Date.now() });
        }
        
        saveCart();
        updateCartUI();
        
        if (openSidebar) {
            openCart();
        }
    };
});
