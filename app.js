document.addEventListener('DOMContentLoaded', () => {
    const setupCarouselArrows = (carouselId, previousButtonId, nextButtonId, itemSelector) => {
        const carousel = document.getElementById(carouselId);
        const previousButton = document.getElementById(previousButtonId);
        const nextButton = document.getElementById(nextButtonId);
        if (!carousel || !previousButton || !nextButton) return;

        const updateArrows = () => {
            const maxScrollLeft = carousel.scrollWidth - carousel.clientWidth;
            previousButton.classList.toggle('is-hidden', carousel.scrollLeft <= 1);
            nextButton.classList.toggle('is-hidden', carousel.scrollLeft >= maxScrollLeft - 1);
        };
        const scrollOneItem = (direction) => {
            const item = carousel.querySelector(itemSelector);
            if (!item) return;

            const gap = parseFloat(getComputedStyle(carousel).columnGap) || 0;
            carousel.scrollBy({
                left: direction * (item.getBoundingClientRect().width + gap),
                behavior: 'smooth'
            });
        };

        previousButton.addEventListener('click', () => scrollOneItem(-1));
        nextButton.addEventListener('click', () => scrollOneItem(1));
        carousel.addEventListener('scroll', updateArrows, { passive: true });
        window.addEventListener('resize', updateArrows);
        updateArrows();
    };

    [
        ['spotlight-carousel', 'prevBtnSpotlight', 'nextBtnSpotlight', '.spotlight-card'],
        ['noteworthy-carousel', 'prevBtnNoteworthy', 'nextBtnNoteworthy', '.noteworthy-item'],
        ['most-booked-carousel', 'prevBtnMostBooked', 'nextBtnMostBooked', '.most-booked-item'],
        ['salon-carousel', 'prevBtnSalon', 'nextBtnSalon', '.most-booked-item'],
        ['spa-carousel', 'prevBtnSpa', 'nextBtnSpa', '.most-booked-item'],
        ['cleaning-carousel', 'prevBtnCleaning', 'nextBtnCleaning', '.most-booked-item'],
        ['massage-carousel', 'prevBtnMassage', 'nextBtnMassage', '.most-booked-item'],
        ['salon-men-carousel', 'prevBtnSalonMen', 'nextBtnSalonMen', '.most-booked-item']
    ].forEach(([carouselId, previousButtonId, nextButtonId, itemSelector]) => {
        setupCarouselArrows(carouselId, previousButtonId, nextButtonId, itemSelector);
    });

    // Modal Logic
    const womensBeautyBtn = document.getElementById('womens-beauty-btn');
    const beautyModal = document.getElementById('beauty-modal');
    const closeModalBtn = document.getElementById('close-modal-btn');

    if (womensBeautyBtn && beautyModal && closeModalBtn) {
        // Open modal
        womensBeautyBtn.addEventListener('click', () => {
            beautyModal.style.display = 'flex';
        });

        // Close modal on X button click
        closeModalBtn.addEventListener('click', () => {
            beautyModal.style.display = 'none';
        });

        // Close modal when clicking outside the content box
        beautyModal.addEventListener('click', (e) => {
            if (e.target === beautyModal) {
                beautyModal.style.display = 'none';
            }
        });
    }

    // Salon Options Modal Logic
    const salonOptionsTrigger = document.getElementById('salon-options-trigger');
    const salonOptionsModal = document.getElementById('salon-options-modal');
    const closeSalonOptionsModalBtn = document.getElementById('close-salon-options-modal-btn');

    if (salonOptionsTrigger && salonOptionsModal && closeSalonOptionsModalBtn) {
        salonOptionsTrigger.addEventListener('click', () => {
            if(beautyModal) beautyModal.style.display = 'none';
            salonOptionsModal.style.display = 'flex';
        });

        closeSalonOptionsModalBtn.addEventListener('click', () => {
            salonOptionsModal.style.display = 'none';
            if(beautyModal) beautyModal.style.display = 'flex';
        });

        salonOptionsModal.addEventListener('click', (e) => {
            if (e.target === salonOptionsModal) {
                salonOptionsModal.style.display = 'none';
            }
        });
    }

    // Spa for Women Options Modal Logic
    const spaForWomenTrigger = document.getElementById('spa-for-women-trigger');
    const spaForWomenOptionsModal = document.getElementById('spa-for-women-options-modal');
    const closeSpaForWomenOptionsBtn = document.getElementById('close-spa-for-women-options-btn');

    if (spaForWomenTrigger && spaForWomenOptionsModal && closeSpaForWomenOptionsBtn) {
        spaForWomenTrigger.addEventListener('click', () => {
            if(beautyModal) beautyModal.style.display = 'none';
            spaForWomenOptionsModal.style.display = 'flex';
        });

        closeSpaForWomenOptionsBtn.addEventListener('click', () => {
            spaForWomenOptionsModal.style.display = 'none';
            if(beautyModal) beautyModal.style.display = 'flex';
        });

        spaForWomenOptionsModal.addEventListener('click', (e) => {
            if (e.target === spaForWomenOptionsModal) {
                spaForWomenOptionsModal.style.display = 'none';
            }
        });
    }

    // Men's Modal Logic
    const mensGroomingBtn = document.getElementById('mens-grooming-btn');
    const mensModal = document.getElementById('mens-modal');
    const closeMensModalBtn = document.getElementById('close-mens-modal-btn');

    if (mensGroomingBtn && mensModal && closeMensModalBtn) {
        // Open modal
        mensGroomingBtn.addEventListener('click', () => {
            mensModal.style.display = 'flex';
        });

        // Close modal on X button click
        closeMensModalBtn.addEventListener('click', () => {
            mensModal.style.display = 'none';
        });

        // Close modal when clicking outside the content box
        mensModal.addEventListener('click', (e) => {
            if (e.target === mensModal) {
                mensModal.style.display = 'none';
            }
        });
    }

    // Salon for Men Options Modal Logic
    const salonForMenTrigger = document.getElementById('salon-for-men-trigger');
    const salonForMenOptionsModal = document.getElementById('salon-for-men-options-modal');
    const closeSalonForMenOptionsBtn = document.getElementById('close-salon-for-men-options-btn');

    if (salonForMenTrigger && salonForMenOptionsModal && closeSalonForMenOptionsBtn) {
        salonForMenTrigger.addEventListener('click', () => {
            if(mensModal) mensModal.style.display = 'none';
            salonForMenOptionsModal.style.display = 'flex';
        });

        closeSalonForMenOptionsBtn.addEventListener('click', () => {
            salonForMenOptionsModal.style.display = 'none';
            if(mensModal) mensModal.style.display = 'flex';
        });

        salonForMenOptionsModal.addEventListener('click', (e) => {
            if (e.target === salonForMenOptionsModal) {
                salonForMenOptionsModal.style.display = 'none';
            }
        });
    }

    // Massage for Men Options Modal Logic
    const massageForMenTrigger = document.getElementById('massage-for-men-trigger');
    const massageForMenOptionsModal = document.getElementById('massage-for-men-options-modal');
    const closeMassageForMenOptionsBtn = document.getElementById('close-massage-for-men-options-btn');

    if (massageForMenTrigger && massageForMenOptionsModal && closeMassageForMenOptionsBtn) {
        massageForMenTrigger.addEventListener('click', () => {
            if(mensModal) mensModal.style.display = 'none';
            massageForMenOptionsModal.style.display = 'flex';
        });

        closeMassageForMenOptionsBtn.addEventListener('click', () => {
            massageForMenOptionsModal.style.display = 'none';
            if(mensModal) mensModal.style.display = 'flex';
        });

        massageForMenOptionsModal.addEventListener('click', (e) => {
            if (e.target === massageForMenOptionsModal) {
                massageForMenOptionsModal.style.display = 'none';
            }
        });
    }

    // AC Modal Logic
    const acRepairBtn = document.getElementById('ac-repair-btn');
    const acModal = document.getElementById('ac-modal');
    const closeAcModalBtn = document.getElementById('close-ac-modal-btn');

    if (acRepairBtn && acModal && closeAcModalBtn) {
        acRepairBtn.addEventListener('click', () => {
            acModal.style.display = 'flex';
        });

        closeAcModalBtn.addEventListener('click', () => {
            acModal.style.display = 'none';
        });

        acModal.addEventListener('click', (e) => {
            if (e.target === acModal) {
                acModal.style.display = 'none';
            }
        });
    }

    // EPC Modal Logic
    const epcBtn = document.getElementById('epc-btn');
    const epcModal = document.getElementById('epc-modal');
    const closeEpcModalBtn = document.getElementById('close-epc-modal-btn');

    if (epcBtn && epcModal && closeEpcModalBtn) {
        epcBtn.addEventListener('click', () => {
            epcModal.style.display = 'flex';
        });

        closeEpcModalBtn.addEventListener('click', () => {
            epcModal.style.display = 'none';
        });

        epcModal.addEventListener('click', (e) => {
            if (e.target === epcModal) {
                epcModal.style.display = 'none';
            }
        });
    }

    // Cleaning Modal Logic
    const cleaningBtn = document.getElementById('cleaning-btn');
    const cleaningModal = document.getElementById('cleaning-modal');
    const closeCleaningModalBtn = document.getElementById('close-cleaning-modal-btn');

    if (cleaningBtn && cleaningModal && closeCleaningModalBtn) {
        cleaningBtn.addEventListener('click', () => {
            cleaningModal.style.display = 'flex';
        });

        closeCleaningModalBtn.addEventListener('click', () => {
            cleaningModal.style.display = 'none';
        });

        cleaningModal.addEventListener('click', (e) => {
            if (e.target === cleaningModal) {
                cleaningModal.style.display = 'none';
            }
        });
    }

    // Renovation Modal Logic
    const renovationBtn = document.getElementById('renovation-btn');
    const renovationModal = document.getElementById('renovation-modal');
    const closeRenovationModalBtn = document.getElementById('close-renovation-modal-btn');

    if (renovationBtn && renovationModal && closeRenovationModalBtn) {
        renovationBtn.addEventListener('click', () => {
            renovationModal.style.display = 'flex';
        });

        closeRenovationModalBtn.addEventListener('click', () => {
            renovationModal.style.display = 'none';
        });

        renovationModal.addEventListener('click', (e) => {
            if (e.target === renovationModal) {
                renovationModal.style.display = 'none';
            }
        });
    }
    // Home Security Modal Logic
    const securityTrigger = document.getElementById('security-modal-trigger');
    const securityModal = document.getElementById('security-modal');
    const closeSecurityBtn = document.getElementById('close-security-modal-btn');

    if (securityTrigger && securityModal && closeSecurityBtn) {
        securityTrigger.addEventListener('click', () => {
            securityModal.style.display = 'flex';
        });

        closeSecurityBtn.addEventListener('click', () => {
            securityModal.style.display = 'none';
        });

        securityModal.addEventListener('click', (e) => {
            if (e.target === securityModal) {
                securityModal.style.display = 'none';
            }
        });
    }

    // Logistics Modal Logic
    const logisticsTrigger = document.getElementById('logistics-modal-trigger');
    const logisticsModal = document.getElementById('logistics-modal');
    const closeLogisticsBtn = document.getElementById('close-logistics-modal-btn');

    if (logisticsTrigger && logisticsModal && closeLogisticsBtn) {
        logisticsTrigger.addEventListener('click', () => {
            logisticsModal.style.display = 'flex';
        });

        closeLogisticsBtn.addEventListener('click', () => {
            logisticsModal.style.display = 'none';
        });

        logisticsModal.addEventListener('click', (e) => {
            if (e.target === logisticsModal) {
                logisticsModal.style.display = 'none';
            }
        });
    }

    // Fabrication Modal Logic
    const fabricationTrigger = document.getElementById('fabrication-modal-trigger');
    const fabricationModal = document.getElementById('fabrication-modal');
    const closeFabricationBtn = document.getElementById('close-fabrication-modal-btn');

    if (fabricationTrigger && fabricationModal && closeFabricationBtn) {
        fabricationTrigger.addEventListener('click', () => {
            fabricationModal.style.display = 'flex';
        });

        closeFabricationBtn.addEventListener('click', () => {
            fabricationModal.style.display = 'none';
        });

        fabricationModal.addEventListener('click', (e) => {
            if (e.target === fabricationModal) {
                fabricationModal.style.display = 'none';
            }
        });
    }

    const modalsToSetup = [
        {trigger: 'ac-modal-trigger', modal: 'ac-modal', close: 'close-ac-modal-btn'},
        {trigger: 'epc-modal-trigger', modal: 'epc-modal', close: 'close-epc-modal-btn'},
        {trigger: 'cleaning-modal-trigger', modal: 'cleaning-modal', close: 'close-cleaning-modal-btn'},
        {trigger: 'reno-modal-trigger', modal: 'reno-modal', close: 'close-reno-modal-btn'},
        {trigger: 'beauty-modal-trigger', modal: 'beauty-modal', close: 'close-beauty-modal-btn'},
        {trigger: 'grooming-modal-trigger', modal: 'grooming-modal', close: 'close-grooming-modal-btn'}
    ];

    modalsToSetup.forEach(m => {
        const trigger = document.getElementById(m.trigger);
        const modal = document.getElementById(m.modal);
        const closeBtn = document.getElementById(m.close);
        
        if (trigger && modal && closeBtn) {
            trigger.addEventListener('click', () => modal.style.display = 'flex');
            closeBtn.addEventListener('click', () => modal.style.display = 'none');
            modal.addEventListener('click', (e) => {
                if (e.target === modal) modal.style.display = 'none';
            });
        }
    });
});

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
        { triggerId: 'logistics-modal-trigger', modalId: 'logistics-modal' }, /* assuming home care is logistics */
        { triggerId: 'security-modal-trigger', modalId: 'security-modal' }
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
