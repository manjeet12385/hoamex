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
    // Select all potential sidebar navigation links
    const navLinks = document.querySelectorAll('.service-item-sidebar, .service-item, .service-cat-item, .left-sidebar a[href^="#"], .select-service-card a[href^="#"], .service-cat-grid a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const targetHref = link.getAttribute('href');
            if(targetHref && targetHref.startsWith('#')) {
                // Find target element by exact ID or ID + '-section'
                let targetEl = document.querySelector(targetHref);
                if (!targetEl) {
                    targetEl = document.querySelector(targetHref + '-section');
                }
                
                if(targetEl) {
                    e.preventDefault();
                    // Smooth scroll with offset for sticky header
                    const headerOffset = 100; // Account for fixed header height
                    const elementPosition = targetEl.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
  
                    window.scrollTo({
                         top: offsetPosition,
                         behavior: 'smooth'
                    });
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


// Global Location Modal Functions
window.triggerGpsLocation = function() {
    const locationBtn = document.querySelector('.location-btn');
    if (!locationBtn) return;
    
    locationBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Locating...';
    
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`)
                    .then(response => response.json())
                    .then(data => {
                        const city = data.address.city || data.address.town || data.address.state_district || 'Unknown Location';
                        locationBtn.innerHTML = `<i class="fa-solid fa-location-dot"></i> ${city}`;
                        document.getElementById('location-modal').style.display = 'none';
                        localStorage.setItem('user_location', city);
                    })
                    .catch(() => {
                        locationBtn.innerHTML = '<i class="fa-solid fa-location-dot"></i> Use Current Location';
                        alert('Could not determine city from coordinates.');
                    });
            },
            (error) => {
                locationBtn.innerHTML = '<i class="fa-solid fa-location-dot"></i> Use Current Location';
                alert('Location access denied or unavailable.');
            }
        );
    } else {
        alert('Geolocation is not supported by your browser.');
    }
};

window.setManualLocation = function() {
    const input = document.getElementById('manual-loc-input').value.trim();
    if (input) {
        const locationBtn = document.querySelector('.location-btn');
        if (locationBtn) {
            locationBtn.innerHTML = `<i class="fa-solid fa-location-dot"></i> ${input}`;
            localStorage.setItem('user_location', input);
        }
        document.getElementById('location-modal').style.display = 'none';
    }
};

// Check for saved location on load
document.addEventListener('DOMContentLoaded', () => {
    const savedLoc = localStorage.getItem('user_location');
    if (savedLoc) {
        const locationBtn = document.querySelector('.location-btn');
        if (locationBtn) {
            locationBtn.innerHTML = `<i class="fa-solid fa-location-dot"></i> ${savedLoc}`;
        }
    }
});

// Open location modal on click
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.location-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const modal = document.getElementById('location-modal');
            if (modal) modal.style.display = 'flex';
        });
    });
});

// Typing effect for search placeholder
document.addEventListener('DOMContentLoaded', () => {
    const searchInputs = document.querySelectorAll('.search-container input');
    
    // Customize the list of services you want to cycle through
    const words = ["plumber", "electrician", "carpenter", "cleaner", "ac repair", "pest control"];
    
    searchInputs.forEach(input => {
        let currentWordIndex = 0;
        let currentCharIndex = 0;
        let isDeleting = false;
        let typingTimeout;
        let isFocused = false;
        const typingSpeed = 100;
        const deletingSpeed = 50;
        const delayBetweenWords = 2000;

        function typeEffect() {
            if (isFocused) return; // Stop animation if user focused the input

            const currentWord = words[currentWordIndex];
            
            if (isDeleting) {
                // Remove a character
                input.setAttribute('placeholder', `Search for ${currentWord.substring(0, currentCharIndex - 1)}`);
                currentCharIndex--;
            } else {
                // Add a character
                input.setAttribute('placeholder', `Search for ${currentWord.substring(0, currentCharIndex + 1)}`);
                currentCharIndex++;
            }

            let nextSpeed = isDeleting ? deletingSpeed : typingSpeed;

            // If word is completely typed
            if (!isDeleting && currentCharIndex === currentWord.length) {
                isDeleting = true;
                nextSpeed = delayBetweenWords; // Pause at the end of the word
            } else if (isDeleting && currentCharIndex === 0) {
                isDeleting = false;
                currentWordIndex = (currentWordIndex + 1) % words.length; // Move to next word
                nextSpeed = 500; // Small pause before typing next word
            }

            typingTimeout = setTimeout(typeEffect, nextSpeed);
        }

        // Start typing effect initially
        setTimeout(typeEffect, 1000);

        // Handle focus and blur events
        input.addEventListener('focus', () => {
            isFocused = true;
            clearTimeout(typingTimeout);
            input.setAttribute('placeholder', 'Search for services');
        });

        input.addEventListener('blur', () => {
            isFocused = false;
            if (input.value.trim() === '') {
                // Restart animation if empty
                setTimeout(typeEffect, 500);
            }
        });
    });
});



// -----------------------------------------------------------
// Universal "View Details" Modal System for Joamex
// -----------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
    // 1. Inject Modal HTML into the body if not exists
    if (!document.getElementById('universal-details-modal')) {
        const modalHTML = `
            <div id="universal-details-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 10000; align-items: center; justify-content: center; backdrop-filter: blur(5px);">
                <div style="background: white; width: 90%; max-width: 450px; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.2); animation: modalPop 0.3s ease-out; position: relative; max-height: 85vh; display: flex; flex-direction: column;">
                    <div style="padding: 20px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; background: #fdfaf6;">
                        <h3 id="udm-title" style="margin: 0; font-size: 18px; font-weight: 700; color: #111;">Service Details</h3>
                        <button onclick="document.getElementById('universal-details-modal').style.display='none'" style="background: none; border: none; font-size: 24px; color: #666; cursor: pointer; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; border-radius: 50%;">&times;</button>
                    </div>
                    <div style="padding: 20px; overflow-y: auto; flex: 1;">
                        <div style="background: #e8f5e9; color: #2e7d32; padding: 10px; border-radius: 8px; font-size: 13px; font-weight: 600; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;">
                            <i class="fa-solid fa-shield-halved"></i> 30-Day Joamex Guarantee | Verified Professionals
                        </div>
                        
                        <h4 style="margin: 0 0 12px 0; font-size: 16px; color: #333; display: flex; align-items: center;"><i class="fa-solid fa-circle-check" style="color: #4CAF50; margin-right: 8px; font-size: 18px;"></i> What's included</h4>
                        <ul id="udm-included" style="margin: 0 0 25px 0; padding-left: 20px; color: #555; font-size: 14px; line-height: 1.6;">
                            <li>Complete diagnostic and inspection</li>
                            <li>Basic cleaning of the service area</li>
                            <li>Tool and labor charges for basic fix</li>
                        </ul>
                        
                        <h4 style="margin: 0 0 12px 0; font-size: 16px; color: #333; display: flex; align-items: center;"><i class="fa-solid fa-circle-xmark" style="color: #f44336; margin-right: 8px; font-size: 18px;"></i> What's excluded</h4>
                        <ul id="udm-excluded" style="margin: 0 0 25px 0; padding-left: 20px; color: #555; font-size: 14px; line-height: 1.6;">
                            <li>Spare parts cost (will be quoted if needed)</li>
                            <li>Any major civil or masonry work</li>
                        </ul>
                        
                        <h4 style="margin: 0 0 12px 0; font-size: 16px; color: #333; display: flex; align-items: center;"><i class="fa-solid fa-list-ol" style="color: #2196F3; margin-right: 8px; font-size: 18px;"></i> Process</h4>
                        <ol id="udm-process" style="margin: 0 0 10px 0; padding-left: 20px; color: #555; font-size: 14px; line-height: 1.6;">
                            <li>Inspection & Issue Identification</li>
                            <li>Quotation for parts (if any)</li>
                            <li>Repair/Service Execution</li>
                            <li>Final Testing & Cleanup</li>
                        </ol>
                    </div>
                    <div style="padding: 15px 20px; border-top: 1px solid #eee; background: #fff; text-align: center;">
                        <div style="margin-bottom: 15px; padding: 12px; background: #f8fcf8; border: 1px solid #e2f2e5; border-radius: 12px; text-align: center;">
                            <p style="margin: 0 0 10px 0; font-size: 13.5px; color: #444; font-weight: 700;">Have questions or doubts?</p>
                            <div style="display: flex; gap: 10px; justify-content: center;">
                                <a href="tel:+917667389146" style="flex: 1; display: flex; align-items: center; justify-content: center; gap: 8px; background: #fff; color: #333; text-decoration: none; padding: 8px; border-radius: 8px; border: 1px solid #ddd; font-weight: 600; font-size: 14px; transition: 0.2s;" onmouseover="this.style.borderColor='#000'" onmouseout="this.style.borderColor='#ddd'">
                                    <i class="fa-solid fa-phone" style="color: #2196F3;"></i> Call
                                </a>
                                <a href="https://wa.me/917667389146" target="_blank" style="flex: 1; display: flex; align-items: center; justify-content: center; gap: 8px; background: #25D366; color: #fff; text-decoration: none; padding: 8px; border-radius: 8px; font-weight: 600; font-size: 14px; box-shadow: 0 2px 8px rgba(37,211,102,0.3); transition: 0.2s;" onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='scale(1)'">
                                    <i class="fa-brands fa-whatsapp"></i> WhatsApp
                                </a>
                            </div>
                        </div>
                        <button onclick="document.getElementById('universal-details-modal').style.display='none'" style="width: 100%; background: #000; color: #fff; border: none; padding: 12px; border-radius: 8px; font-weight: 700; font-size: 16px; cursor: pointer; transition: 0.2s;" onmouseover="this.style.background='#333'" onmouseout="this.style.background='#000'">Got it</button>
                    </div>
                </div>
            </div>
            <style>
                @keyframes modalPop {
                    0% { opacity: 0; transform: scale(0.9) translateY(20px); }
                    100% { opacity: 1; transform: scale(1) translateY(0); }
                }
            </style>
        `;
        document.body.insertAdjacentHTML('beforeend', modalHTML);
    }

    // 2. Attach click events to all "View details" links
    const updateDetailsLinks = () => {
        document.querySelectorAll('a').forEach(link => {
            const text = link.textContent.toLowerCase();
            if (text.includes('view detail')) {
                // Check if we haven't attached listener yet
                if (!link.hasAttribute('data-modal-attached')) {
                    link.setAttribute('data-modal-attached', 'true');
                    link.addEventListener('click', function(e) {
                        e.preventDefault();
                        
                        // Try to find the service title near this button
                        let title = 'Service Details';
                        
                        // Strategy 1: It's inside .service-card-info -> h4
                        let cardInfo = this.closest('.service-card-info');
                        if (cardInfo) {
                            let h4 = cardInfo.querySelector('h4, h3');
                            if (h4) title = h4.textContent.trim();
                        } else {
                            // Strategy 2: It's inside .service-details or something, go up a few levels and find h3/h4
                            let parent = this.parentElement;
                            while (parent && parent.tagName !== 'BODY') {
                                let heading = parent.querySelector('h3, h4');
                                if (heading && heading !== this) {
                                    title = heading.textContent.trim();
                                    break;
                                }
                                parent = parent.parentElement;
                            }
                        }
                        
                        document.getElementById('udm-title').textContent = title;
                        
                        // --- DYNAMIC CONTENT BASED ON CATEGORY ---
                        const t = title.toLowerCase();
                        
                        // DEFAULT (General Service)
                        let included = `<li>Pre-service consultation and assessment</li><li>Standard service execution as per selected plan</li><li>Basic cleanup of the work area post-service</li>`;
                        let excluded = `<li>Cost of any additional spare parts or materials</li><li>Major structural or civil work outside scope</li>`;
                        let process = `<li>Understanding your specific requirements</li><li>Execution of the requested service</li><li>Final walkthrough and quality check</li>`;
                        
                        if (t.includes('clean') || t.includes('wash') || t.includes('dust') || t.includes('sweep') || t.includes('mop')) {
                            included = `<li>Deep cleaning of all accessible surfaces</li><li>Professional grade eco-friendly chemicals</li><li>Post-cleanup surface sanitization</li>`;
                            excluded = `<li>Cleaning of inaccessible or hazardous areas</li><li>Removal of heavy debris/furniture moving</li>`;
                            process = `<li>Initial survey of the area</li><li>Dry dusting and vacuuming</li><li>Wet cleaning and scrubbing</li><li>Final sanitization and walkthrough</li>`;
                        } else if (t.includes('salon') || t.includes('spa') || t.includes('massage') || t.includes('hair') || t.includes('makeup') || t.includes('beauty') || t.includes('beard') || t.includes('shave') || t.includes('wax') || t.includes('facial') || t.includes('pedicure') || t.includes('manicure') || t.includes('threading') || t.includes('grooming')) {
                            included = `<li>Pre-service consultation</li><li>Use of premium branded products</li><li>Disposable gowns and sterilized tools</li>`;
                            excluded = `<li>Specialized dermatological treatments</li><li>Extra product usage beyond standard measure</li>`;
                            process = `<li>Setup of hygienic workstation</li><li>Personalized consultation</li><li>Execution of beauty/spa service</li><li>Post-service cleanup and tips</li>`;
                        } else if (t.includes('ac ') || t.includes('refrigerat') || t.includes('appliance') || t.includes('washing') || t.includes('microwave') || t.includes('geyser') || t.includes('ro ') || t.includes('purifier') || t.includes('tv ') || t.includes('chimney') || t.includes('cooler')) {
                            included = `<li>Comprehensive diagnostic check</li><li>Cleaning of filters and basic components</li><li>Standard tool and labor charges</li>`;
                            excluded = `<li>Cost of gas refill (if applicable)</li><li>Replacement parts (compressor, PCB, motor, etc.)</li>`;
                            process = `<li>Appliance performance testing</li><li>Identification of root cause</li><li>Component repair or service execution</li><li>Final functionality and safety test</li>`;
                        } else if (t.includes('pest') || t.includes('termite') || t.includes('cockroach') || t.includes('ant') || t.includes('mosquito') || t.includes('bedbug') || t.includes('rodent')) {
                            included = `<li>Thorough inspection of infested areas</li><li>Application of Govt-approved safe chemicals</li><li>Protective masking of valuables</li>`;
                            excluded = `<li>Structural repairs for damages caused by pests</li><li>Post-treatment deep cleaning (can be added separately)</li>`;
                            process = `<li>Infestation level assessment</li><li>Sealing of food and sensitive items</li><li>Targeted chemical spray/gel application</li><li>Safety instructions for next 24 hours</li>`;
                        } else if (t.includes('plumb') || t.includes('electric') || t.includes('carpent') || t.includes('weld') || t.includes('drill') || t.includes('pipe') || t.includes('leak') || t.includes('wiring') || t.includes('switch') || t.includes('fan') || t.includes('wood')) {
                            included = `<li>Initial visit and defect diagnosis</li><li>Minor adjustments and tightening</li><li>Standard toolkit usage by professional</li>`;
                            excluded = `<li>Material cost (pipes, wires, wood, hinges, etc.)</li><li>Major structural breaking or patching</li>`;
                            process = `<li>On-site problem assessment</li><li>Material procurement estimation (if needed)</li><li>Execution of repair/installation</li><li>Safety and functionality check</li>`;
                        } else if (t.includes('paint') || t.includes('waterproof') || t.includes('wall')) {
                            included = `<li>Surface preparation and minor crack filling</li><li>Application of selected primer and paint</li><li>Floor masking to prevent stains</li>`;
                            excluded = `<li>Major wall repair or putty work (unless quoted)</li><li>Cost of premium textured paints (if not selected)</li>`;
                            process = `<li>Color consultation and measurement</li><li>Masking and surface prep</li><li>Painting execution (number of coats as agreed)</li><li>Final unmasking and cleanup</li>`;
                        }
                        
                        document.getElementById('udm-included').innerHTML = included;
                        document.getElementById('udm-excluded').innerHTML = excluded;
                        document.getElementById('udm-process').innerHTML = process;
                        
                        // Show modal
                        const modal = document.getElementById('universal-details-modal');
                        modal.style.display = 'flex';
                    });
                }
            }
        });
    };
    
    // Initial call
    updateDetailsLinks();
    
    // Re-run in case of dynamic injection
    setTimeout(updateDetailsLinks, 1000);
    setTimeout(updateDetailsLinks, 3000);
});


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


// -----------------------------------------------------------
// Partner Login Modal System
// -----------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
    // 1. Inject Modal HTML into the body if not exists
    if (!document.getElementById('partner-login-modal')) {
        const modalHTML = `
            <div id="partner-login-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 10000; align-items: center; justify-content: center; backdrop-filter: blur(5px);">
                <div style="background: #0d1117; width: 90%; max-width: 900px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.5); animation: modalPop 0.3s ease-out; position: relative; display: flex; flex-direction: row; height: 500px;">
                    
                    <button id="close-partner-modal" style="position: absolute; top: 15px; right: 15px; background: rgba(255,255,255,0.1); border: none; border-radius: 50%; font-size: 18px; color: #fff; cursor: pointer; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; z-index: 10;">&times;</button>
                    
                    <!-- Left Side -->
                    <div style="flex: 1; background: linear-gradient(135deg, #091316 0%, #060a0d 100%); padding: 40px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; border-right: 1px solid rgba(255,255,255,0.05);">
                        <div style="margin-bottom: 30px; position: relative;">
                            <!-- Mock graphic for the green layers -->
                            <div style="width: 150px; height: 150px; position: relative;">
                                <div style="position: absolute; top: 20%; left: 15%; width: 70%; height: 70%; border: 2px solid #1a5d3c; transform: rotateX(60deg) rotateZ(-45deg); border-radius: 8px; box-shadow: 0 0 20px rgba(26,93,60,0.3);"></div>
                                <div style="position: absolute; top: 35%; left: 15%; width: 70%; height: 70%; border: 2px solid #1f8a55; transform: rotateX(60deg) rotateZ(-45deg); border-radius: 8px; box-shadow: 0 0 30px rgba(31,138,85,0.4);"></div>
                                <div style="position: absolute; top: 50%; left: 15%; width: 70%; height: 70%; border: 2px solid #23a566; transform: rotateX(60deg) rotateZ(-45deg); border-radius: 8px; box-shadow: 0 0 40px rgba(35,165,102,0.5);"></div>
                                <div style="position: absolute; top: 35%; left: 40%; width: 30px; height: 40px; background: rgba(35,165,102,0.2); backdrop-filter: blur(4px); border-radius: 6px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(35,165,102,0.5); z-index: 5;">
                                    <i class="fa-solid fa-user" style="color: #23a566; font-size: 14px;"></i>
                                </div>
                            </div>
                        </div>
                        <h2 style="color: #fff; font-size: 28px; font-weight: 700; margin: 0 0 15px 0;">Partner Portal</h2>
                        <p style="color: #8b949e; font-size: 14px; line-height: 1.6; max-width: 280px; margin: 0;">Manage your service business, track earnings, and deliver excellence with our professional toolkit.</p>
                    </div>
                    
                    <!-- Right Side -->
                    <div style="flex: 1.2; background: #0a0c10; padding: 50px 40px; display: flex; flex-direction: column; justify-content: center; position: relative;">
                        <!-- Step 1: Login -->
                        <div id="partner-login-step" style="display: flex; flex-direction: column; height: 100%; justify-content: center;">
                            <h3 style="color: #fff; font-size: 24px; font-weight: 700; margin: 0 0 10px 0;">Partner Login</h3>
                        <p style="color: #8b949e; font-size: 14px; margin: 0 0 30px 0;">Enter your details for quick OTP access to your workspace.</p>
                        
                        <div style="margin-bottom: 20px;">
                            <label style="display: block; color: #fff; font-size: 12px; font-weight: 600; margin-bottom: 8px;">Email Address</label>
                            <input type="email" placeholder="partner@business.com" style="width: 100%; padding: 14px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box; transition: 0.2s;" onfocus="this.style.borderColor='#5e35b1'" onblur="this.style.borderColor='#30363d'">
                        </div>
                        
                        <button id="partner-otp-btn" style="width: 100%; background: #5e35b1; color: #fff; border: none; padding: 14px; border-radius: 8px; font-weight: 600; font-size: 14px; cursor: pointer; transition: 0.2s; margin-bottom: 25px;" onmouseover="this.style.background='#6e45c1'" onmouseout="this.style.background='#5e35b1'">Get OTP Code &rarr;</button>
                        
                        <div style="background: rgba(22,27,34,0.5); border: 1px solid #30363d; border-radius: 8px; padding: 15px; display: flex; gap: 15px; align-items: flex-start; margin-bottom: 30px;">
                            <div style="background: #23a566; color: #fff; width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 10px; margin-top: 2px; flex-shrink: 0;"><i class="fa-solid fa-check"></i></div>
                            <div>
                                <h4 style="color: #fff; font-size: 13px; font-weight: 600; margin: 0 0 5px 0;">Instant Access</h4>
                                <p style="color: #8b949e; font-size: 12px; margin: 0; line-height: 1.5;">Secure login via one-time passcodes. No passwords required.</p>
                            </div>
                        </div>
                        
                        <div style="text-align: center; margin-bottom: 20px;">
                            <p style="color: #8b949e; font-size: 13px; margin: 0;">New Partner? <a href="partner.html" style="color: #58a6ff; text-decoration: none; font-weight: 600;">Apply Now</a></p>
                        </div>
                        
                        <div style="text-align: center; margin-top: auto;">
                                <span style="color: #484f58; font-size: 11px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase;"><i class="fa-solid fa-shield-halved"></i> PARTNER SECURITY 2.0</span>
                            </div>
                        </div>

                        <!-- Step 2: OTP Verification -->
                        <div id="partner-otp-step" style="display: none; flex-direction: column; height: 100%; justify-content: center;">
                            <a href="#" id="back-to-login" style="color: #8b949e; text-decoration: none; font-size: 13px; margin-bottom: 20px; display: inline-block;">&larr; Back to Login</a>
                            <h3 style="color: #fff; font-size: 28px; font-weight: 700; margin: 0 0 10px 0;">OTP Verification</h3>
                            <p style="color: #8b949e; font-size: 14px; margin: 0 0 30px 0;">Code sent to <span id="otp-sent-email" style="color: #fff;"></span></p>
                            
                            <div style="display: flex; gap: 10px; margin-bottom: 30px; justify-content: space-between;">
                                <input type="text" maxlength="1" class="otp-box-input" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none; transition: 0.2s;" onfocus="this.style.borderColor='#23a566'" onblur="this.style.borderColor='#30363d'">
                                <input type="text" maxlength="1" class="otp-box-input" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none; transition: 0.2s;" onfocus="this.style.borderColor='#23a566'" onblur="this.style.borderColor='#30363d'">
                                <input type="text" maxlength="1" class="otp-box-input" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none; transition: 0.2s;" onfocus="this.style.borderColor='#23a566'" onblur="this.style.borderColor='#30363d'">
                                <input type="text" maxlength="1" class="otp-box-input" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none; transition: 0.2s;" onfocus="this.style.borderColor='#23a566'" onblur="this.style.borderColor='#30363d'">
                                <input type="text" maxlength="1" class="otp-box-input" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none; transition: 0.2s;" onfocus="this.style.borderColor='#23a566'" onblur="this.style.borderColor='#30363d'">
                                <input type="text" maxlength="1" class="otp-box-input" style="width: 45px; height: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: 20px; text-align: center; outline: none; transition: 0.2s;" onfocus="this.style.borderColor='#23a566'" onblur="this.style.borderColor='#30363d'">
                            </div>

                            <button id="verify-otp-final-btn" style="width: 100%; background: #23a566; color: #fff; border: none; padding: 14px; border-radius: 8px; font-weight: 600; font-size: 15px; cursor: pointer; transition: 0.2s; margin-bottom: 25px;" onmouseover="this.style.background='#28c076'" onmouseout="this.style.background='#23a566'">Verify & Enter Dashboard</button>

                            <div style="text-align: center; margin-top: auto;">
                                <span style="color: #8b949e; font-size: 13px;">Resend in <span style="color: #fff; font-weight: 600;">56s</span></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', modalHTML);
    }
    
    // 2. Attach click events to partner buttons
    const attachPartnerModalEvents = () => {
        document.querySelectorAll('.partner-btn').forEach(btn => {
            if (!btn.hasAttribute('data-partner-modal-attached')) {
                btn.setAttribute('data-partner-modal-attached', 'true');
                
                const existingEmail = localStorage.getItem('partnerEmail');
                if (existingEmail) {
                    btn.innerHTML = '<i class="fa-solid fa-briefcase"></i> Dashboard';
                    btn.addEventListener('click', function(e) {
                        e.preventDefault();
                        window.location.href = 'partner-dashboard.html';
                    });
                } else {
                    btn.addEventListener('click', function(e) {
                        e.preventDefault();
                        document.getElementById('partner-login-modal').style.display = 'flex';
                    });
                }
            }
        });
        
        const closeBtn = document.getElementById('close-partner-modal');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                document.getElementById('partner-login-modal').style.display = 'none';
            });
        }

        const otpBtn = document.getElementById('partner-otp-btn');
        if (otpBtn && !otpBtn.hasAttribute('data-otp-attached')) {
            otpBtn.setAttribute('data-otp-attached', 'true');
            otpBtn.addEventListener('click', () => {
                const emailInput = otpBtn.previousElementSibling.querySelector('input');
                if (emailInput && emailInput.value) {
                    const originalText = otpBtn.innerHTML;
                    otpBtn.innerHTML = 'Sending...';
                    
                    fetch('/api/send-otp', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ email: emailInput.value })
                    })
                    .then(res => res.json())
                    .then(data => {
                        otpBtn.innerHTML = originalText;
                        if(data.success) {
                            // Don't store email yet, wait for OTP validation
                            // localStorage.setItem('partnerEmail', emailInput.value);
                            
                            // Hide login step, show OTP step
                            document.getElementById('partner-login-step').style.display = 'none';
                            document.getElementById('partner-otp-step').style.display = 'flex';
                            document.getElementById('otp-sent-email').innerText = emailInput.value;
                            
                            // Attach event for back button
                            document.getElementById('back-to-login').onclick = function(e) {
                                e.preventDefault();
                                document.getElementById('partner-otp-step').style.display = 'none';
                                document.getElementById('partner-login-step').style.display = 'flex';
                            };
                            
                            // Attach event for final verify button
                            const finalBtn = document.getElementById('verify-otp-final-btn');
                            if (finalBtn) {
                                finalBtn.onclick = async function() {
                                    const inputs = document.querySelectorAll('.otp-box-input');
                                    let val = '';
                                    inputs.forEach(i => val += i.value);
                                    if(val.length < 6) {
                                        alert('Please enter the complete 6-digit OTP.');
                                        return;
                                    }
                                    
                                    const originalBtnText = finalBtn.innerHTML;
                                    finalBtn.innerHTML = 'Verifying...';
                                    
                                    try {
                                        const res = await fetch('/api/partner/verify-otp', {
                                            method: 'POST',
                                            headers: { 'Content-Type': 'application/json' },
                                            body: JSON.stringify({ email: emailInput.value, otp: val })
                                        });
                                        const data = await res.json();
                                        
                                        if (data.success) {
                                            if (data.token) localStorage.setItem('partnerToken', data.token);
                                            localStorage.setItem('partnerEmail', emailInput.value);
                                            alert('OTP Verified Successfully! ✅\\n\\nRedirecting to your Partner Dashboard...');
                                            window.location.href = 'partner-dashboard.html';
                                        } else {
                                            alert(data.error || 'Invalid OTP');
                                        }
                                    } catch (err) {
                                        alert('Network error during verification.');
                                    } finally {
                                        finalBtn.innerHTML = originalBtnText;
                                    }
                                };
                            }
                            
                            // OTP input auto focus
                            const otpInputs = document.querySelectorAll('.otp-box-input');
                            otpInputs.forEach((input, index) => {
                                input.addEventListener('input', function() {
                                    if(this.value.length === 1 && index < otpInputs.length - 1) {
                                        otpInputs[index + 1].focus();
                                    }
                                });
                                input.addEventListener('keydown', function(e) {
                                    if (e.key === 'Backspace' && this.value === '' && index > 0) {
                                        otpInputs[index - 1].focus();
                                    }
                                });
                            });
                            
                        } else {
                            alert('Failed to send OTP: ' + (data.error || 'Unknown error'));
                        }
                    })
                    .catch(err => {
                        otpBtn.innerHTML = originalText;
                        alert('Server error while sending OTP.');
                    });
                } else {
                    alert('Please enter a valid email address first.');
                }
            });
        }
    };
    
    attachPartnerModalEvents();
    
    // Re-run in case of dynamic injection
    setTimeout(attachPartnerModalEvents, 1000);
});


// --- Secret Admin Trick ---
document.addEventListener('DOMContentLoaded', () => {
    const secretTrigger = document.getElementById('secret-admin');
    if(secretTrigger) {
        let clickCount = 0;
        let clickTimer;
        
        secretTrigger.addEventListener('click', (e) => {
            clickCount++;
            
            if(clickCount === 1) {
                clickTimer = setTimeout(() => {
                    clickCount = 0; // reset if not clicked 5 times within 2 seconds
                }, 2000);
            }
            
            if(clickCount === 5) {
                clearTimeout(clickTimer);
                clickCount = 0;
                // Add a cool little transition effect before redirecting
                document.body.style.transition = "opacity 0.5s ease";
                document.body.style.opacity = "0";
                setTimeout(() => {
                    window.location.href = "admin.html";
                }, 500);
            }
        });
    }
});


// User Login Modal System
function injectUserModal() {
    if (!document.getElementById('user-login-modal')) {
        const modalHTML = `
            <div id="user-login-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 10000; align-items: flex-start; justify-content: center; backdrop-filter: blur(5px); padding: 20px 15px; box-sizing: border-box; overflow-y: auto;">
                <div style="background: #0d1117; width: 100%; max-width: 440px; border-radius: 16px; box-shadow: 0 20px 40px rgba(0,0,0,0.4); border: 1px solid #30363d; position: relative; font-family: 'Inter', sans-serif; margin: auto;">
                    <button id="close-user-modal" style="position: absolute; top: 15px; right: 15px; background: transparent; border: none; color: #8b949e; font-size: 20px; cursor: pointer; transition: 0.2s; z-index: 10;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#8b949e'">&times;</button>
                    
                    <div style="padding: clamp(20px, 5vw, 40px) clamp(15px, 4vw, 30px);">
                        <!-- Tabs -->
                        <div style="display: flex; gap: 20px; margin-bottom: 25px; border-bottom: 1px solid #30363d;">
                            <button id="tab-login" style="background: transparent; border: none; color: #fff; font-size: 16px; font-weight: 600; padding: 10px 0; cursor: pointer; border-bottom: 2px solid #4a3aff; transition: 0.2s;">Login</button>
                            <button id="tab-signup" style="background: transparent; border: none; color: #8b949e; font-size: 16px; font-weight: 600; padding: 10px 0; cursor: pointer; border-bottom: 2px solid transparent; transition: 0.2s;">Sign Up</button>
                        </div>

                        <!-- Step 1: Login -->
                        <div id="user-login-step" style="display: flex; flex-direction: column; height: 100%; justify-content: center;">
                            <h3 style="color: #fff; font-size: 24px; font-weight: 700; margin: 0 0 10px 0;">Customer Login</h3>
                            <p style="color: #8b949e; font-size: 14px; margin: 0 0 30px 0; line-height: 1.5;">Enter your email to view your bookings.</p>
                            
                            <div style="margin-bottom: 25px;">
                                <input type="email" id="user-email-input" placeholder="Enter your email" style="width: 100%; background: #161b22; border: 1px solid #30363d; padding: 14px 15px; border-radius: 8px; color: #fff; font-size: 15px; outline: none; transition: 0.2s; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                            </div>
                            
                            <button id="user-otp-btn" style="width: 100%; background: #4a3aff; color: #fff; border: none; padding: 14px; border-radius: 8px; font-weight: 600; font-size: 15px; cursor: pointer; transition: 0.2s; margin-bottom: 20px;" onmouseover="this.style.background='#3d2fd1'" onmouseout="this.style.background='#4a3aff'">Send OTP</button>
                        </div>

                        <!-- Sign Up Form (Directly visible) -->
                        <div id="user-signup-step" style="display: none; flex-direction: column; height: 100%; justify-content: flex-start;">
                            <h3 style="color: #fff; font-size: 24px; font-weight: 700; margin: 0 0 5px 0;">Create Account</h3>
                            <p style="color: #8b949e; font-size: 14px; margin: 0 0 20px 0;">Fill in your details to get started.</p>
                            
                            <div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 25px;">
                                <input type="text" id="signup-name" placeholder="Full Name (Jiske naam par address hai)" style="width: 100%; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                
                                <div style="display: flex; gap: 10px;">
                                    <input type="email" id="signup-email" placeholder="Email Address" style="flex: 1; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                    <button id="signup-verify-email-btn" style="background: #238636; color: #fff; border: none; padding: 0 15px; border-radius: 8px; font-weight: 600; font-size: 13px; cursor: pointer; transition: 0.2s;">Verify</button>
                                </div>
                                <div id="signup-email-otp-container" style="display: none; flex-direction: column; gap: 5px;">
                                    <div style="display: flex; gap: 10px;">
                                        <input type="text" id="signup-email-otp" placeholder="Enter Email OTP" style="flex: 1; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                        <button id="signup-confirm-email-btn" style="background: #4a3aff; color: #fff; border: none; padding: 0 15px; border-radius: 8px; font-weight: 600; font-size: 13px; cursor: pointer; transition: 0.2s;">Confirm</button>
                                    </div>
                                    <div style="text-align: right; padding-right: 5px;">
                                        <a href="#" id="signup-resend-otp-btn" style="color: #4a3aff; font-size: 12px; text-decoration: none; font-weight: 500;">Resend OTP</a>
                                    </div>
                                </div>

                                <input type="text" id="signup-phone" placeholder="Phone Number" style="width: 100%; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                
                                <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                                    <select id="signup-gender" style="flex: 1; min-width: 130px; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #8b949e; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                        <option value="" disabled selected>Select Gender</option>
                                        <option value="Male">Male</option>
                                        <option value="Female">Female</option>
                                        <option value="Other">Other</option>
                                    </select>
                                    <input type="date" id="signup-dob" title="Date of Birth" style="flex: 1; min-width: 130px; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #8b949e; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                </div>
                                
                                <div style="margin-top: 10px; margin-bottom: 5px; border-bottom: 1px solid #30363d; padding-bottom: 5px;">
                                    <span style="color: #fff; font-weight: 600; font-size: 14px;">Address Details</span>
                                </div>

                                <input type="text" id="signup-house" placeholder="House/Flat/Building No." style="width: 100%; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                
                                <input type="text" id="signup-society" placeholder="Building/Apartment/Society Name" style="width: 100%; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                
                                <input type="text" id="signup-street" placeholder="Street/Road/Area / Gali number" style="width: 100%; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                
                                <input type="text" id="signup-landmark" placeholder="Landmark (Optional)" style="width: 100%; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                
                                <input type="text" id="signup-village" placeholder="Village/Town/City" style="width: 100%; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                
                                <input type="text" id="signup-tehsil" placeholder="Tehsil/Taluk (Optional)" style="width: 100%; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                
                                <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                                    <input type="text" id="signup-district" placeholder="District" style="flex: 1; min-width: 120px; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                    <input type="text" id="signup-state" placeholder="State" style="flex: 1; min-width: 120px; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                </div>
                                
                                <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                                    <input type="text" id="signup-country" placeholder="Country" value="India" style="flex: 1; min-width: 120px; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                    <input type="text" id="signup-pincode" placeholder="PIN Code" style="flex: 1; min-width: 120px; background: #161b22; border: 1px solid #30363d; padding: 12px 15px; border-radius: 8px; color: #fff; font-size: 14px; outline: none; box-sizing: border-box;" onfocus="this.style.borderColor='#4a3aff'" onblur="this.style.borderColor='#30363d'">
                                </div>
                                
                            </div>

                            <button id="user-register-btn" style="width: 100%; background: #4a3aff; color: #fff; border: none; padding: 14px; border-radius: 8px; font-weight: 600; font-size: 15px; cursor: pointer; transition: 0.2s;">Sign Up</button>
                        </div>

                        <!-- Step 2: OTP Verify (For Login) -->
                        <div id="user-otp-step" style="display: none; flex-direction: column; height: 100%; justify-content: center;">
                            <a href="#" id="user-back-to-login" style="color: #8b949e; text-decoration: none; font-size: 13px; margin-bottom: 20px; display: inline-block;">&larr; Back</a>
                            <h3 style="color: #fff; font-size: 24px; font-weight: 700; margin: 0 0 10px 0;">Verify Email</h3>
                            <p style="color: #8b949e; font-size: 14px; margin: 0 0 30px 0;">Code sent to <span id="user-otp-sent-email" style="color: #fff;"></span></p>
                            
                            <div style="display: flex; gap: clamp(6px, 2vw, 10px); margin-bottom: 30px; justify-content: space-between;">
                                <input type="text" maxlength="1" class="user-otp-box" style="flex: 1; min-width: 0; height: clamp(40px, 10vw, 50px); background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: clamp(16px, 4vw, 20px); text-align: center; outline: none;">
                                <input type="text" maxlength="1" class="user-otp-box" style="flex: 1; min-width: 0; height: clamp(40px, 10vw, 50px); background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: clamp(16px, 4vw, 20px); text-align: center; outline: none;">
                                <input type="text" maxlength="1" class="user-otp-box" style="flex: 1; min-width: 0; height: clamp(40px, 10vw, 50px); background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: clamp(16px, 4vw, 20px); text-align: center; outline: none;">
                                <input type="text" maxlength="1" class="user-otp-box" style="flex: 1; min-width: 0; height: clamp(40px, 10vw, 50px); background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: clamp(16px, 4vw, 20px); text-align: center; outline: none;">
                                <input type="text" maxlength="1" class="user-otp-box" style="flex: 1; min-width: 0; height: clamp(40px, 10vw, 50px); background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: clamp(16px, 4vw, 20px); text-align: center; outline: none;">
                                <input type="text" maxlength="1" class="user-otp-box" style="flex: 1; min-width: 0; height: clamp(40px, 10vw, 50px); background: #161b22; border: 1px solid #30363d; border-radius: 8px; color: #fff; font-size: clamp(16px, 4vw, 20px); text-align: center; outline: none;">
                            </div>

                            <button id="user-verify-otp-btn" style="width: 100%; background: #4a3aff; color: #fff; border: none; padding: 14px; border-radius: 8px; font-weight: 600; font-size: 15px; cursor: pointer; transition: 0.2s;">Verify & Login</button>
                        </div>
                    </div>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', modalHTML);
    }
    
    // Attach events
    const loginBtn = document.getElementById('user-login-btn');
    if(loginBtn) {
        // ✅ Session expiry check — auto-logout after 30 days
        const _loginTime = localStorage.getItem('loginTime');
        if (_loginTime) {
            const daysSince = (Date.now() - parseInt(_loginTime)) / (1000 * 60 * 60 * 24);
            if (daysSince > 30) {
                localStorage.removeItem('userEmail');
                localStorage.removeItem('userPhone');
                localStorage.removeItem('userName');
                localStorage.removeItem('userLocation');
                localStorage.removeItem('user_location');
                localStorage.removeItem('loginTime');
            }
        }

        const existingEmail = localStorage.getItem('userEmail') || localStorage.getItem('userPhone');
        if(existingEmail) {
            loginBtn.innerHTML = '<i class="fa-solid fa-user-check" style="color: #4a3aff;"></i>';
            loginBtn.onclick = () => window.location.href = 'user-dashboard.html';
        } else {
            loginBtn.onclick = () => document.getElementById('user-login-modal').style.display = 'flex';
        }
    }
    const closeBtn = document.getElementById('close-user-modal');
    if(closeBtn) {
        closeBtn.onclick = () => document.getElementById('user-login-modal').style.display = 'none';
    }
    const tabLogin = document.getElementById('tab-login');
    const tabSignup = document.getElementById('tab-signup');
    const loginStep = document.getElementById('user-login-step');
    const signupStep = document.getElementById('user-signup-step');
    const otpStep = document.getElementById('user-otp-step');
    
    if(tabLogin && tabSignup) {
        tabLogin.onclick = () => {
            tabLogin.style.color = '#fff';
            tabLogin.style.borderBottomColor = '#4a3aff';
            tabSignup.style.color = '#8b949e';
            tabSignup.style.borderBottomColor = 'transparent';
            
            loginStep.style.display = 'flex';
            signupStep.style.display = 'none';
            otpStep.style.display = 'none';
        };
        tabSignup.onclick = () => {
            tabSignup.style.color = '#fff';
            tabSignup.style.borderBottomColor = '#4a3aff';
            tabLogin.style.color = '#8b949e';
            tabLogin.style.borderBottomColor = 'transparent';
            
            signupStep.style.display = 'flex';
            loginStep.style.display = 'none';
            otpStep.style.display = 'none';
        };
    }

    const sendOtp = document.getElementById('user-otp-btn');
    if(sendOtp) {
        sendOtp.onclick = () => {
            // ✅ FIX 1: trim + lowercase before sending OTP
            let email = document.getElementById('user-email-input').value;
            email = email.trim().toLowerCase();
            // Put cleaned value back so OTP-sent display is also clean
            document.getElementById('user-email-input').value = email;

            if(email && email.includes('@')) {
                const originalText = sendOtp.innerText;
                sendOtp.innerText = "Sending...";
                fetch('/api/user/send-otp', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email: email })
                })
                .then(async res => {
                    const data = await res.json();
                    sendOtp.innerText = originalText;
                    if(res.status === 404) {
                        // User not registered — show clear message
                        const emailInput = document.getElementById('user-email-input');
                        emailInput.style.borderColor = '#f85149';
                        emailInput.placeholder = 'No account found with this email';
                        emailInput.value = '';
                        // Show error below input
                        let errMsg = document.getElementById('user-login-error-msg');
                        if(!errMsg) {
                            errMsg = document.createElement('p');
                            errMsg.id = 'user-login-error-msg';
                            errMsg.style.cssText = 'color:#f85149; font-size:13px; margin: -10px 0 10px 0;';
                            emailInput.parentNode.insertBefore(errMsg, emailInput.nextSibling);
                        }
                        errMsg.innerText = '⚠️ ' + (data.error || 'No account found. Please sign up first.');
                    } else if(data.success) {
                        // Clear any previous error
                        const errMsg = document.getElementById('user-login-error-msg');
                        if(errMsg) errMsg.remove();
                        loginStep.style.display = 'none';
                        signupStep.style.display = 'none';
                        otpStep.style.display = 'flex';
                        document.getElementById('user-otp-sent-email').innerText = email;
                    } else {
                        alert('Failed to send OTP: ' + (data.error || 'Unknown error'));
                    }
                })
                .catch(err => {
                    sendOtp.innerText = originalText;
                    alert('Network error. Please try again.');
                });
            } else {
                alert('Enter valid email address');
            }
        };
    }
    const backBtn = document.getElementById('user-back-to-login');
    if(backBtn) {
        backBtn.onclick = (e) => {
            e.preventDefault();
            otpStep.style.display = 'none';
            // Determine which tab is active
            if (tabSignup && tabSignup.style.color === 'rgb(255, 255, 255)') {
                signupStep.style.display = 'flex';
            } else {
                loginStep.style.display = 'flex';
            }
        };
    }
    const verifyBtn = document.getElementById('user-verify-otp-btn');
    if(verifyBtn) {
        verifyBtn.onclick = async () => {
            let email = document.getElementById('user-email-input').value;
            email = email.trim().toLowerCase();

            // Collect the 6 OTP digits from individual boxes
            const otpBoxes = document.querySelectorAll('.user-otp-box');
            const otp = Array.from(otpBoxes).map(b => b.value).join('').trim();

            if (otp.length !== 6) {
                alert('Please enter the 6-digit OTP.');
                return;
            }

            verifyBtn.innerText = 'Verifying...';
            verifyBtn.disabled = true;

            try {
                // ✅ Server-side OTP verification
                const res = await fetch('/api/user/verify-otp', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, otp })
                });
                const data = await res.json();

                if (data.success) {
                    // Store cleaned email, remove old data
                    localStorage.setItem('userEmail', email);
                    localStorage.setItem('loginTime', Date.now().toString()); // ✅ session timer
                    if (data.token) localStorage.setItem('token', data.token); // Save JWT
                    localStorage.removeItem('userPhone');

                    // Close the login modal
                    const modal = document.getElementById('user-login-modal');
                    if (modal) modal.style.display = 'none';

                    // ✅ Update header icon immediately
                    const loginBtn = document.getElementById('user-login-btn');
                    if (loginBtn) {
                        loginBtn.innerHTML = '<i class="fa-solid fa-user-check" style="color:#4a3aff;"></i>';
                        loginBtn.onclick = () => window.location.href = 'user-dashboard.html';
                    }

                    alert('Login successful! Welcome back.');
                    const redirectUrl = localStorage.getItem('loginRedirect') || window.userLoginRedirect || 'user-dashboard.html';
                    localStorage.removeItem('loginRedirect');
                    window.location.href = redirectUrl;
                } else {
                    verifyBtn.innerText = 'Verify & Login';
                    verifyBtn.disabled = false;
                    alert(data.error || 'Invalid OTP. Please try again.');
                }
            } catch (err) {
                verifyBtn.innerText = 'Verify & Login';
                verifyBtn.disabled = false;
                alert('Network error. Please try again.');
            }
        };
    }

    // Email Verification Logic for Signup
    const verifyEmailBtn = document.getElementById('signup-verify-email-btn');
    const emailOtpContainer = document.getElementById('signup-email-otp-container');
    const confirmEmailBtn = document.getElementById('signup-confirm-email-btn');
    const emailInput = document.getElementById('signup-email');
    const resendOtpBtn = document.getElementById('signup-resend-otp-btn');
    let isEmailVerified = false;

    const triggerOtpSend = () => {
        const email = emailInput ? emailInput.value : '';
        if (email && email.includes('@')) {
            const originalText = verifyEmailBtn.innerText;
            verifyEmailBtn.innerText = 'Sending...';
            
            fetch('/api/user/send-otp', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: email, isSignup: true })
            })
            .then(res => res.json())
            .then(data => {
                if(data.success) {
                    verifyEmailBtn.innerText = 'Sent!';
                    verifyEmailBtn.style.background = '#8b949e';
                    emailOtpContainer.style.display = 'flex';
                } else {
                    verifyEmailBtn.innerText = originalText;
                    alert('Failed to send OTP: ' + (data.error || 'Unknown error'));
                }
            })
            .catch(err => {
                verifyEmailBtn.innerText = originalText;
                alert('Network error while sending OTP.');
            });
        } else {
            alert('Please enter a valid email to verify.');
        }
    };

    if (emailInput) {
        // Reset verify button if user edits the email after sending OTP
        emailInput.addEventListener('input', () => {
            if (!isEmailVerified) {
                verifyEmailBtn.innerText = 'Verify';
                verifyEmailBtn.style.background = '#238636';
                emailOtpContainer.style.display = 'none';
            }
        });
    }

    if (verifyEmailBtn) {
        verifyEmailBtn.onclick = (e) => {
            e.preventDefault();
            triggerOtpSend();
        };
    }

    if (resendOtpBtn) {
        resendOtpBtn.onclick = (e) => {
            e.preventDefault();
            const originalText = resendOtpBtn.innerText;
            resendOtpBtn.innerText = 'Sending...';
            
            const email = emailInput ? emailInput.value.trim().toLowerCase() : '';
            if (email && email.includes('@')) {
                fetch('/api/user/send-otp', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    // ✅ isResend:true — skip the duplicate email check
                    body: JSON.stringify({ email: email, isSignup: true, isResend: true })
                })
                .then(res => res.json())
                .then(data => {
                    if(data.success) {
                        resendOtpBtn.innerText = 'Sent again!';
                        setTimeout(() => { resendOtpBtn.innerText = 'Resend OTP'; }, 3000);
                    } else {
                        resendOtpBtn.innerText = originalText;
                        alert('Failed to resend OTP: ' + (data.error || 'Unknown error'));
                    }
                })
                .catch(err => {
                    resendOtpBtn.innerText = originalText;
                    alert('Network error while resending OTP.');
                });
            }
        };
    }

    if (confirmEmailBtn) {
        confirmEmailBtn.onclick = async (e) => {
            e.preventDefault();
            const otpVal = document.getElementById('signup-email-otp').value.trim();
            const emailVal = emailInput ? emailInput.value.trim().toLowerCase() : '';
            
            if (otpVal.length === 0) {
                alert('Please enter the OTP.');
                return;
            }

            confirmEmailBtn.innerText = 'Checking...';
            confirmEmailBtn.disabled = true;

            try {
                // ✅ Server-side verify the signup OTP
                const res = await fetch('/api/user/verify-otp', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email: emailVal, otp: otpVal })
                });
                const data = await res.json();

                if (data.success) {
                    isEmailVerified = true;
                    if (data.token) localStorage.setItem('token', data.token); // ✅ Save JWT from signup verify
                    emailOtpContainer.innerHTML = '<span style="color: #238636; font-weight: 600; font-size: 14px; display: flex; align-items: center; padding: 12px 0;"><i class="fa-solid fa-check-circle" style="margin-right: 5px;"></i> Email Verified</span>';
                    verifyEmailBtn.style.display = 'none';
                    if(emailInput) emailInput.readOnly = true;
                } else {
                    confirmEmailBtn.innerText = 'Confirm';
                    confirmEmailBtn.disabled = false;
                    alert(data.error || 'Invalid or expired OTP. Please try again.');
                }
            } catch(err) {
                confirmEmailBtn.innerText = 'Confirm';
                confirmEmailBtn.disabled = false;
                alert('Network error while verifying OTP.');
            }
        };
    }

    const registerBtn = document.getElementById('user-register-btn');
    if(registerBtn) {
        registerBtn.onclick = () => {
            const name = document.getElementById('signup-name').value.trim();
            let email = document.getElementById('signup-email').value.trim().toLowerCase();
            const phone = document.getElementById('signup-phone').value.trim();
            const pincode = document.getElementById('signup-pincode').value.trim();

            if (!name || !email || !phone || !pincode) {
                alert('Please fill in all essential fields (Name, Email, Phone, PIN Code)!');
                return;
            }

            if (!isEmailVerified) {
                alert('Please verify your email before signing up.');
                return;
            }
            
            // Build address string
            const house = document.getElementById('signup-house').value.trim();
            const society = document.getElementById('signup-society').value.trim();
            const street = document.getElementById('signup-street').value.trim();
            const village = document.getElementById('signup-village').value.trim();
            const district = document.getElementById('signup-district').value.trim();
            const state = document.getElementById('signup-state').value.trim();
            
            const gender = document.getElementById('signup-gender').value;
            const dob = document.getElementById('signup-dob').value;
            
            const fullAddress = [house, society, street, village, district, state, pincode].filter(Boolean).join(', ');
            
            const originalText = registerBtn.innerText;
            registerBtn.innerText = 'Creating Account...';
            registerBtn.disabled = true;

            const token = localStorage.getItem('token') || '';
            fetch('/api/user/register', {
                method: 'POST',
                headers: { 
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    full_name: name,
                    email: email,
                    phone: phone,
                    gender: gender,
                    dob: dob,
                    full_address: fullAddress
                })
            })
            .then(res => res.json())
            .then(data => {
                registerBtn.innerText = originalText;
                registerBtn.disabled = false;
                
                if (data.success) {
                    // ✅ Hide modal and reset button before redirect to fix browser back behavior
                    const modal = document.getElementById('user-login-modal');
                    if (modal) modal.style.display = 'none';
                    registerBtn.innerText = 'Sign Up';

                    // ✅ Store cleaned values, clear stale data
                    localStorage.setItem('userName', name);
                    localStorage.setItem('userEmail', email);
                    localStorage.setItem('userLocation', fullAddress);
                    localStorage.setItem('loginTime', Date.now().toString()); // ✅ session timer
                    // ✅ Do NOT store phone separately to avoid dual-login confusion
                    localStorage.removeItem('userPhone');
                    localStorage.removeItem('user_location');

                    // ✅ Update header icon immediately after register
                    const loginBtn = document.getElementById('user-login-btn');
                    if (loginBtn) {
                        loginBtn.innerHTML = '<i class="fa-solid fa-user-check" style="color:#4a3aff;"></i>';
                        loginBtn.onclick = () => window.location.href = 'user-dashboard.html';
                    }
                    
                    alert('Account created successfully! Welcome to Joamex.');
                    const redirectUrl = localStorage.getItem('loginRedirect') || window.userLoginRedirect || 'user-dashboard.html';
                    localStorage.removeItem('loginRedirect');
                    window.location.href = redirectUrl;
                } else {
                    alert('Error creating account: ' + (data.error || 'Unknown error'));
                }
            })
            .catch(err => {
                registerBtn.innerText = originalText;
                registerBtn.disabled = false;
                console.error(err);
                alert('Network error while creating account.');
            });
        };
    }
    
    // Auto focus OTP
    const otpInputs = document.querySelectorAll('.user-otp-box');
    otpInputs.forEach((input, index) => {
        input.addEventListener('input', function() {
            if(this.value.length === 1 && index < otpInputs.length - 1) otpInputs[index + 1].focus();
        });
        input.addEventListener('keydown', function(e) {
            if (e.key === 'Backspace' && this.value === '' && index > 0) otpInputs[index - 1].focus();
        });
    });
}

document.addEventListener('DOMContentLoaded', () => {
    setTimeout(injectUserModal, 500);
});
