document.addEventListener('DOMContentLoaded', () => {
    let cart = JSON.parse(localStorage.getItem('joamex_cart')) || [];
    
    const cartSidebar = document.getElementById('cart-sidebar');
    const closeCartBtn = document.getElementById('close-cart-btn');
    const cartItemsContainer = document.getElementById('cart-items-container');
    const cartTotalPrice = document.getElementById('cart-total-price');
    const checkoutBtn = document.getElementById('checkout-btn');

    // Make sure add buttons work on the page
    document.querySelectorAll('.add-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const card = e.target.closest('.service-card');
            if (card) {
                const title = card.querySelector('h4').innerText;
                const priceText = card.querySelector('.service-price span').innerText;
                // extract number from string like "₹499" or "Starts at ₹1,499"
                const priceMatch = priceText.match(/\d+(,\d+)?/);
                let price = 0;
                if (priceMatch) {
                    price = parseInt(priceMatch[0].replace(',', ''));
                }
                
                // Extract image
                const imgEl = card.querySelector('img');
                const imgSrc = imgEl ? imgEl.src : '';

                cart.push({ title, price, imgSrc, id: Date.now() });
                saveCart();
                updateCartUI();
                openCart();
            }
        });
    });

    if (closeCartBtn && cartSidebar) {
        closeCartBtn.addEventListener('click', () => cartSidebar.classList.add('hidden'));
        cartSidebar.addEventListener('click', (e) => {
            if (e.target === cartSidebar) cartSidebar.classList.add('hidden');
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

    // Header is now inline, so bind cart button directly
    const openCartBtn = document.getElementById('open-cart-btn');
    if (openCartBtn && cartSidebar) {
        openCartBtn.addEventListener('click', () => openCart());
    }
    updateCartUI();

    function openCartBtnClickHandler() {
        openCart();
    }

    function openCart() {
        if (cartSidebar) cartSidebar.classList.remove('hidden');
    }

    function saveCart() {
        localStorage.setItem('joamex_cart', JSON.stringify(cart));
    }

    function updateCartUI() {
        const badge = document.getElementById('cart-badge');
        if (badge) {
            badge.innerText = cart.length;
            badge.style.display = cart.length > 0 ? 'block' : 'none';
        }

        if (cartItemsContainer) {
            if (cart.length === 0) {
                cartItemsContainer.innerHTML = '<p style="text-align:center; color:#999; margin-top:50px;">Your cart is empty</p>';
                cartTotalPrice.innerText = '₹0';
                return;
            }

            let html = '';
            let total = 0;
            cart.forEach(item => {
                total += item.price;
                html += `
                    <div style="display: flex; gap: 15px; margin-bottom: 20px; align-items: center;">
                        <img src="${item.imgSrc}" style="width: 50px; height: 50px; border-radius: 8px; object-fit: cover;">
                        <div style="flex: 1;">
                            <div style="font-weight: 600; font-size: 14px;">${item.title}</div>
                            <div style="font-weight: bold; margin-top: 5px;">₹${item.price}</div>
                        </div>
                        <button onclick="removeFromCart(${item.id})" style="background: none; border: none; color: #e53935; cursor: pointer;"><i class="fa-solid fa-trash"></i></button>
                    </div>
                `;
            });
            cartItemsContainer.innerHTML = html;
            cartTotalPrice.innerText = '₹' + total.toLocaleString();
        }
    }

    // Global function to remove item
    window.removeFromCart = function(id) {
        cart = cart.filter(item => item.id !== id);
        saveCart();
        updateCartUI();
    };

    // Global function to add item (used by most-booked-item buttons)
    window.addToCart = function(title, price) {
        let imgSrc = '';
        const imgEl = document.querySelector(`img[alt="${title}"]`);
        if (imgEl) {
            imgSrc = imgEl.src;
        }
        cart.push({ title, price, imgSrc, id: Date.now() });
        saveCart();
        updateCartUI();
        openCart();
    };
});
