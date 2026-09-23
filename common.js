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
