document.addEventListener('DOMContentLoaded', () => {
    const headerPlaceholder = document.getElementById('header-placeholder');
    if (headerPlaceholder) {
        fetch('header.html')
            .then(res => res.text())
            .then(data => {
                headerPlaceholder.innerHTML = data;
                
                // Logic for back button & search bar
                const isHomePage = window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || window.location.pathname.endsWith('/');
                const backBtn = document.getElementById('back-btn');
                const searchContainer = document.getElementById('header-search');
                
                if (!isHomePage && backBtn) {
                    backBtn.style.display = 'block';
                    backBtn.addEventListener('click', () => {
                        window.history.back();
                    });
                }
                if (isHomePage && searchContainer) {
                    searchContainer.style.display = 'block';
                }

                // Dispatch event so cart.js can hook up the open cart button
                document.dispatchEvent(new Event('headerLoaded'));
            });
    }

    const footerPlaceholder = document.getElementById('footer-placeholder');
    if (footerPlaceholder) {
        fetch('footer.html')
            .then(res => res.text())
            .then(data => {
                footerPlaceholder.innerHTML = data;
            });
    }
});

// Smooth scroll for sidebar links
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.service-item-sidebar').forEach(link => {
        link.addEventListener('click', (e) => {
            const targetId = link.getAttribute('href');
            if(targetId && targetId.startsWith('#')) {
                e.preventDefault();
                const targetEl = document.querySelector(targetId);
                if(targetEl) {
                    targetEl.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });
});

// Handle Location Button
document.addEventListener('DOMContentLoaded', () => {
    // Wait slightly for header to load
    setTimeout(() => {
        const locBtn = document.querySelector('.location-btn');
        if (locBtn) {
            locBtn.addEventListener('click', () => {
                const span = locBtn.querySelector('span');
                if(span) {
                    span.innerText = 'Connaught Place, Delhi';
                    locBtn.style.backgroundColor = '#e8f5e9';
                    locBtn.style.color = '#2e7d32';
                }
            });
        }

        // Handle Search Bar
        const searchInput = document.querySelector('.search-container input');
        if (searchInput) {
            searchInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    alert('Search results for "' + searchInput.value + '" will be available soon!');
                    searchInput.value = '';
                }
            });
        }
    }, 500);
});

// EPC Modal Sidebar highlighting
document.addEventListener('DOMContentLoaded', () => {
    const sidebarLinks = document.querySelectorAll('.epc-sidebar-link');
    sidebarLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            sidebarLinks.forEach(l => {
                l.style.borderLeftColor = 'transparent';
                l.style.background = 'transparent';
                l.style.color = '#666';
            });
            e.currentTarget.style.borderLeftColor = '#000';
            e.currentTarget.style.background = '#fff';
            e.currentTarget.style.color = '#333';
        });
    });
});

// Smooth scroll for sidebar links
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.service-item-sidebar').forEach(link => {
        link.addEventListener('click', (e) => {
            const targetId = link.getAttribute('href');
            if(targetId && targetId.startsWith('#')) {
                e.preventDefault();
                const targetEl = document.querySelector(targetId);
                if(targetEl) {
                    targetEl.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });
});

// Handle Location Button
document.addEventListener('DOMContentLoaded', () => {
    // Wait slightly for header to load
    setTimeout(() => {
        const locBtn = document.querySelector('.location-btn');
        if (locBtn) {
            locBtn.addEventListener('click', () => {
                const span = locBtn.querySelector('span');
                if(span) {
                    span.innerText = 'Connaught Place, Delhi';
                    locBtn.style.backgroundColor = '#e8f5e9';
                    locBtn.style.color = '#2e7d32';
                }
            });
        }

        // Handle Search Bar
        const searchInput = document.querySelector('.search-container input');
        if (searchInput) {
            searchInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    alert('Search results for "' + searchInput.value + '" will be available soon!');
                    searchInput.value = '';
                }
            });
        }
    }, 500);
});

// EPC Modal Sidebar highlighting
document.addEventListener('DOMContentLoaded', () => {
    const sidebarLinks = document.querySelectorAll('.epc-sidebar-link');
    sidebarLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            sidebarLinks.forEach(l => {
                l.style.borderLeftColor = 'transparent';
                l.style.background = 'transparent';
                l.style.color = '#666';
            });
            e.currentTarget.style.borderLeftColor = '#000';
            e.currentTarget.style.background = '#fff';
            e.currentTarget.style.color = '#333';
        });
    });
});

// Parallax Effect for Hero Images
document.addEventListener('DOMContentLoaded', () => {
    // For CSS-based parallax if it's a background image
    document.querySelectorAll('.uc-difference-banner').forEach(el => {
        el.style.backgroundAttachment = 'fixed';
        el.style.backgroundPosition = 'center top';
    });
    
    // For JS-based parallax on actual <img> tags (like in inner pages)
    // We scale the image slightly so it has room to translate without showing empty space
    const innerImages = document.querySelectorAll('div[style*="height: 250px"] > img');
    innerImages.forEach(img => {
        img.style.height = '130%'; // Make it taller than container
        img.style.transform = 'translateY(-15%)';
        // Remove css transition to avoid jitter on scroll
        img.style.transition = 'none';
        img.style.willChange = 'transform';
    });

    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        
        innerImages.forEach(img => {
            const speed = 0.3; // Parallax speed
            const yPos = (scrolled * speed);
            img.style.transform = `translateY(calc(-15% + ${yPos}px))`;
        });
    });
});

// Mini-Slider Logic for the first carousel card
document.addEventListener('DOMContentLoaded', () => {
    const miniSliderTrack = document.getElementById('miniSliderTrack');
    if (miniSliderTrack) {
        let currentSlide = 0;
        let slideInterval;
        const totalSlides = miniSliderTrack.querySelectorAll('img').length;
        
        const goToSlide = (index) => {
            currentSlide = (index + totalSlides) % totalSlides;
            miniSliderTrack.style.transform = `translateX(-${currentSlide * 100}%)`;
        };

        const startSlide = () => {
            clearInterval(slideInterval);
            slideInterval = setInterval(() => {
                goToSlide(currentSlide + 1);
            }, 3000); // Slide every 3 seconds
        };

        const miniPrevBtn = document.getElementById('miniPrevBtn');
        const miniNextBtn = document.getElementById('miniNextBtn');
        const miniSliderCard = document.getElementById('miniSliderCard');

        if (miniPrevBtn && miniNextBtn) {
            miniPrevBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                goToSlide(currentSlide - 1);
                startSlide();
            });

            miniNextBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                goToSlide(currentSlide + 1);
                startSlide();
            });
        }

        // Pause on hover
        if(miniSliderCard) {
            miniSliderCard.addEventListener('mouseenter', () => clearInterval(slideInterval));
            miniSliderCard.addEventListener('mouseleave', startSlide);
        }

        startSlide();
    }
});

// 24/7 Support Popup Logic
document.addEventListener('DOMContentLoaded', () => {
    const popupHtml = `
    <div class="support-popup-overlay" id="support-popup">
        <div class="support-popup-header">
            <h3 class="support-popup-title">🎧 24/7 Free Support</h3>
            <button class="support-popup-close" id="support-popup-close"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <p class="support-popup-text">
            Have any questions or doubts? Contact our 24/7 free support team for immediate assistance. Directly WhatsApp or Call us.
        </p>
        <div class="support-popup-buttons">
            <a href="tel:+919014380344" class="support-popup-btn btn-call">Call Now</a>
            <a href="https://wa.me/919014380344" target="_blank" class="support-popup-btn btn-whatsapp">WhatsApp</a>
        </div>
    </div>
    `;

    document.body.insertAdjacentHTML('beforeend', popupHtml);
    
    const popup = document.getElementById('support-popup');
    const closeBtn = document.getElementById('support-popup-close');

    // Show popup after 3 seconds
    setTimeout(() => {
        if (!sessionStorage.getItem('supportPopupClosed')) {
            popup.classList.add('show');
        }
    }, 3000);

    closeBtn.addEventListener('click', () => {
        popup.classList.remove('show');
        sessionStorage.setItem('supportPopupClosed', 'true');
    });
});


// Advanced Features for Location and Search
if (!window.hoamexFeaturesLoaded) {
    window.hoamexFeaturesLoaded = true;
    document.addEventListener('DOMContentLoaded', () => {
        
        // --- 1. Location Button Feature ---
        const locBtns = document.querySelectorAll('.location-btn');
        locBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const originalText = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Locating...';
                
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(position => {
                        const lat = position.coords.latitude;
                        const lon = position.coords.longitude;
                        // Use Nominatim reverse geocoding API
                        fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`)
                            .then(res => res.json())
                            .then(data => {
                                let locationStr = "Location Found";
                                if (data && data.address) {
                                    locationStr = data.address.city || data.address.town || data.address.state_district || data.address.state || "Location Found";
                                }
                                btn.innerHTML = `<i class="fa-solid fa-location-dot"></i> ${locationStr}`;
                            })
                            .catch(() => {
                                btn.innerHTML = '<i class="fa-solid fa-location-dot"></i> New Delhi'; // Fallback
                            });
                    }, error => {
                        btn.innerHTML = '<i class="fa-solid fa-location-dot"></i> Location Denied';
                        setTimeout(() => {
                            btn.innerHTML = originalText;
                        }, 3000);
                    });
                } else {
                    btn.innerHTML = '<i class="fa-solid fa-location-dot"></i> Not Supported';
                }
            });
        });

        // --- 2. Live Search Feature ---
        const servicesList = [
            { name: 'Hair Studio for Women', link: 'hair-studio.html' },
            { name: 'Makeup, Saree &amp; Styling', link: 'makeup.html' },
            { name: 'AC', link: 'ac-service.html' },
            { name: 'Washing Machine', link: 'appliance-repair.html#washing-machine' },
            { name: 'Refrigerator', link: 'appliance-repair.html#fridge' },
            { name: 'Television', link: 'television.html' },
            { name: 'Chimney', link: 'chimney.html' },
            { name: 'Microwave', link: 'microwave.html' },
            { name: 'RO/Water Purifier', link: 'water-purifier.html' },
            { name: 'Electrician', link: 'electrician.html' },
            { name: 'Plumber', link: 'plumber.html' },
            { name: 'Carpenter', link: 'carpenter.html' },
            { name: 'Wood &amp; Furniture Polish', link: 'wood-furniture-polish.html' },
            { name: 'Fan Installation', link: 'fan-installation.html' },
            { name: 'Furniture Assembly', link: 'furniture-assembly.html' },
            { name: 'Geyser Service &amp; Repair', link: 'geyser-service.html' },
            { name: 'IKEA Furniture Assembly', link: 'ikea-furniture.html' },
            { name: 'Tile Grouting &amp; Sealant', link: 'tile-grouting.html' },
            { name: 'Festival Lights Installation', link: 'festival-lights.html' },
            { name: 'Bathroom Cleaning', link: 'bathroom-cleaning.html' },
            { name: 'Kitchen cleaning', link: 'kitchen-cleaning.html' },
            { name: 'Living &amp; Bedroom Cleaning', link: 'living-bedroom.html' },
            { name: 'Full Home/ By Room Cleaning', link: 'full-home-cleaning.html' },
            { name: 'Cockroach Control', link: 'cockroach-control.html' },
            { name: 'Termite Control', link: 'termite-control.html' },
            { name: 'Ants &amp; Bed Bugs Control', link: 'ants-control.html' },
            { name: 'Leak &amp; gap sealing', link: 'leak-gap.html' },
            { name: 'CCTV Camera Installation', link: 'cctv-services.html' },
            { name: 'Smart Locks &amp; Doorbells', link: 'smart-locks.html' },
            { name: 'Home Alarm Systems', link: 'home-alarm.html' },
            { name: 'Solar Panel Installation', link: 'solar-installation.html' },
            { name: 'Solar Panel Cleaning', link: 'solar-cleaning.html' },
            { name: 'Solar Water Heater', link: 'solar-water-heater.html' },
            { name: 'RO / Water Purifier', link: 'ro-service.html' },
            { name: 'Water Tank Cleaning', link: 'water-tank-cleaning.html' },
            { name: 'Packers &amp; Movers', link: 'packers-movers.html' },
            { name: 'Mini Truck on Rent', link: 'mini-truck.html' },
            { name: 'Driver on Demand', link: 'driver-on-demand.html' },
            { name: 'Maid / Helper', link: 'maid-helper.html' },
            { name: 'Cook on Demand', link: 'cook-on-demand.html' },
            { name: 'Elder / Patient Care', link: 'elder-care.html' },
            { name: 'Babysitting / Nanny', link: 'babysitting.html' },
            { name: 'Window Grills &amp; Balcony Railings', link: 'grills-railings.html' },
            { name: 'Gates &amp; Doors', link: 'gates-doors.html' },
            { name: 'Sheds &amp; Roofing', link: 'sheds-roofing.html' },
            { name: 'Welding &amp; Repair', link: 'welding-repair.html' },
            { name: 'AC Repair', link: 'ac-repair.html' },
            { name: 'Full Home Cleaning', link: 'full-home-cleaning.html' },
            { name: 'Pest Control', link: 'pest-control.html' },
            { name: 'Full Home Renovation', link: 'full-home-renovation.html' },
            { name: 'Painting', link: 'painting.html' },
            { name: 'Salon for Women', link: 'salon-women.html' },
            { name: 'Spa for Women', link: 'womens-spa.html' },
            { name: 'Salon for Men', link: 'salon-men.html' },
            { name: 'Massage for Men', link: 'massage-men.html' },
            { name: 'AC Service', link: 'ac-service.html' },
            { name: 'Home Renovation', link: 'full-home-renovation.html' },
            { name: 'Washing Machine Repair', link: 'washing-machine.html' },
            { name: 'Refrigerator Repair', link: 'refrigerator.html' },
            { name: 'Water Purifier (RO)', link: 'water-purifier.html' },
            { name: 'Packers & Movers', link: 'packers-movers.html' },
            { name: 'Maid & Helper', link: 'maid-helper.html' },
            { name: 'Nanny / Babysitting', link: 'babysitting.html' },
            { name: 'Elder Care', link: 'elder-care.html' },
            { name: 'Kitchen Cleaning', link: 'kitchen-cleaning.html' },
            { name: 'CCTV Installation', link: 'cctv-services.html' },
            { name: 'Smart Locks', link: 'smart-locks.html' },
            { name: 'Solar Cleaning', link: 'solar-cleaning.html' },
        ];

        const searchInputs = document.querySelectorAll('.search-container input');
        searchInputs.forEach(input => {
            const container = input.closest('.search-container');
            if (!container) return;
            
            container.style.position = 'relative';

            const dropdown = document.createElement('div');
            dropdown.className = 'search-dropdown';
            dropdown.style.cssText = 'position: absolute; top: 100%; left: 0; right: 0; background: #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-radius: 8px; z-index: 1000; max-height: 300px; overflow-y: auto; display: none; margin-top: 5px; border: 1px solid #eee; text-align: left;';
            container.appendChild(dropdown);

            input.addEventListener('input', (e) => {
                const val = e.target.value.toLowerCase().trim();
                if (val.length === 0) {
                    dropdown.style.display = 'none';
                    return;
                }

                const matches = servicesList.filter(s => s.name.toLowerCase().includes(val));
                
                if (matches.length > 0) {
                    dropdown.innerHTML = matches.map(m => `
                        <a href="${m.link}" style="display: block; padding: 12px 15px; color: #333; text-decoration: none; border-bottom: 1px solid #f5f5f5; font-size: 14px; transition: background 0.2s;" onmouseover="this.style.background='#f9f9f9'" onmouseout="this.style.background='transparent'">
                            <i class="fa-solid fa-magnifying-glass" style="color: #999; margin-right: 8px;"></i> ${m.name}
                        </a>
                    `).join('');
                    dropdown.style.display = 'block';
                } else {
                    dropdown.innerHTML = '<div style="padding: 12px 15px; color: #999; font-size: 14px; text-align: center;">No services found</div>';
                    dropdown.style.display = 'block';
                }
            });

            // Hide dropdown when clicking outside
            document.addEventListener('click', (e) => {
                if (!container.contains(e.target)) {
                    dropdown.style.display = 'none';
                }
            });
            
            // Show dropdown again if focused and has value
            input.addEventListener('focus', (e) => {
                if (e.target.value.trim().length > 0) {
                    dropdown.style.display = 'block';
                }
            });
        });
    });
}
