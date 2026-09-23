document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.getElementById('carousel');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    if (carousel && prevBtn && nextBtn) {
        prevBtn.addEventListener('click', () => {
            // Scroll left by the width of one item + gap
            const itemWidth = carousel.querySelector('.carousel-item').offsetWidth;
            const gap = 20; // 20px gap from CSS
            carousel.scrollBy({ left: -(itemWidth + gap), behavior: 'smooth' });
        });

        nextBtn.addEventListener('click', () => {
            // Scroll right by the width of one item + gap
            const itemWidth = carousel.querySelector('.carousel-item').offsetWidth;
            const gap = 20; // 20px gap from CSS
            carousel.scrollBy({ left: (itemWidth + gap), behavior: 'smooth' });
        });
    }

    // Spotlight Carousel
    const spotlightCarousel = document.getElementById('spotlight-carousel');
    const prevBtnSpotlight = document.getElementById('prevBtnSpotlight');
    const nextBtnSpotlight = document.getElementById('nextBtnSpotlight');

    if (spotlightCarousel && prevBtnSpotlight && nextBtnSpotlight) {
        prevBtnSpotlight.addEventListener('click', () => {
            const itemWidth = spotlightCarousel.querySelector('.spotlight-card').offsetWidth;
            const gap = 20; 
            spotlightCarousel.scrollBy({ left: -(itemWidth + gap), behavior: 'smooth' });
        });

        nextBtnSpotlight.addEventListener('click', () => {
            const itemWidth = spotlightCarousel.querySelector('.spotlight-card').offsetWidth;
            const gap = 20;
            spotlightCarousel.scrollBy({ left: (itemWidth + gap), behavior: 'smooth' });
        });
    }

    // Noteworthy Carousel
    const noteworthyCarousel = document.getElementById('noteworthy-carousel');
    const prevBtnNoteworthy = document.getElementById('prevBtnNoteworthy');
    const nextBtnNoteworthy = document.getElementById('nextBtnNoteworthy');

    if (noteworthyCarousel && prevBtnNoteworthy && nextBtnNoteworthy) {
        prevBtnNoteworthy.addEventListener('click', () => {
            const itemWidth = noteworthyCarousel.querySelector('.noteworthy-item').offsetWidth;
            const gap = 20; 
            noteworthyCarousel.scrollBy({ left: -(itemWidth + gap), behavior: 'smooth' });
        });

        nextBtnNoteworthy.addEventListener('click', () => {
            const itemWidth = noteworthyCarousel.querySelector('.noteworthy-item').offsetWidth;
            const gap = 20;
            noteworthyCarousel.scrollBy({ left: (itemWidth + gap), behavior: 'smooth' });
        });
    }

    // Most Booked Carousel
    const mostBookedCarousel = document.getElementById('most-booked-carousel');
    const prevBtnMostBooked = document.getElementById('prevBtnMostBooked');
    const nextBtnMostBooked = document.getElementById('nextBtnMostBooked');

    if (mostBookedCarousel && prevBtnMostBooked && nextBtnMostBooked) {
        prevBtnMostBooked.addEventListener('click', () => {
            const itemWidth = mostBookedCarousel.querySelector('.most-booked-item').offsetWidth;
            const gap = 20; 
            mostBookedCarousel.scrollBy({ left: -(itemWidth + gap), behavior: 'smooth' });
        });

        nextBtnMostBooked.addEventListener('click', () => {
            const itemWidth = mostBookedCarousel.querySelector('.most-booked-item').offsetWidth;
            const gap = 20;
            mostBookedCarousel.scrollBy({ left: (itemWidth + gap), behavior: 'smooth' });
        });
    }

    // Salon Carousel
    const salonCarousel = document.getElementById('salon-carousel');
    const prevBtnSalon = document.getElementById('prevBtnSalon');
    const nextBtnSalon = document.getElementById('nextBtnSalon');

    if (salonCarousel && prevBtnSalon && nextBtnSalon) {
        prevBtnSalon.addEventListener('click', () => {
            const itemWidth = salonCarousel.querySelector('.most-booked-item').offsetWidth;
            const gap = 20; 
            salonCarousel.scrollBy({ left: -(itemWidth + gap), behavior: 'smooth' });
        });

        nextBtnSalon.addEventListener('click', () => {
            const itemWidth = salonCarousel.querySelector('.most-booked-item').offsetWidth;
            const gap = 20;
            salonCarousel.scrollBy({ left: (itemWidth + gap), behavior: 'smooth' });
        });
    }

    // Spa Carousel
    const spaCarousel = document.getElementById('spa-carousel');
    const prevBtnSpa = document.getElementById('prevBtnSpa');
    const nextBtnSpa = document.getElementById('nextBtnSpa');

    if (spaCarousel && prevBtnSpa && nextBtnSpa) {
        prevBtnSpa.addEventListener('click', () => {
            const itemWidth = spaCarousel.querySelector('.most-booked-item').offsetWidth;
            const gap = 20; 
            spaCarousel.scrollBy({ left: -(itemWidth + gap), behavior: 'smooth' });
        });

        nextBtnSpa.addEventListener('click', () => {
            const itemWidth = spaCarousel.querySelector('.most-booked-item').offsetWidth;
            const gap = 20;
            spaCarousel.scrollBy({ left: (itemWidth + gap), behavior: 'smooth' });
        });
    }

    // Cleaning Essentials Carousel
    const cleaningCarousel = document.getElementById('cleaning-carousel');
    const prevBtnCleaning = document.getElementById('prevBtnCleaning');
    const nextBtnCleaning = document.getElementById('nextBtnCleaning');

    if (cleaningCarousel && prevBtnCleaning && nextBtnCleaning) {
        prevBtnCleaning.addEventListener('click', () => {
            const itemWidth = cleaningCarousel.querySelector('.most-booked-item').offsetWidth;
            const gap = 20; 
            cleaningCarousel.scrollBy({ left: -(itemWidth + gap), behavior: 'smooth' });
        });

        nextBtnCleaning.addEventListener('click', () => {
            const itemWidth = cleaningCarousel.querySelector('.most-booked-item').offsetWidth;
            const gap = 20;
            cleaningCarousel.scrollBy({ left: (itemWidth + gap), behavior: 'smooth' });
        });
    }

    // Massage Carousel
    const massageCarousel = document.getElementById('massage-carousel');
    const prevBtnMassage = document.getElementById('prevBtnMassage');
    const nextBtnMassage = document.getElementById('nextBtnMassage');

    if (massageCarousel && prevBtnMassage && nextBtnMassage) {
        prevBtnMassage.addEventListener('click', () => {
            const itemWidth = massageCarousel.querySelector('.most-booked-item').offsetWidth;
            const gap = 20; 
            massageCarousel.scrollBy({ left: -(itemWidth + gap), behavior: 'smooth' });
        });

        nextBtnMassage.addEventListener('click', () => {
            const itemWidth = massageCarousel.querySelector('.most-booked-item').offsetWidth;
            const gap = 20;
            massageCarousel.scrollBy({ left: (itemWidth + gap), behavior: 'smooth' });
        });
    }

    // Salon for Men Carousel
    const salonMenCarousel = document.getElementById('salon-men-carousel');
    const prevBtnSalonMen = document.getElementById('prevBtnSalonMen');
    const nextBtnSalonMen = document.getElementById('nextBtnSalonMen');

    if (salonMenCarousel && prevBtnSalonMen && nextBtnSalonMen) {
        prevBtnSalonMen.addEventListener('click', () => {
            const itemWidth = salonMenCarousel.querySelector('.most-booked-item').offsetWidth;
            const gap = 20; 
            salonMenCarousel.scrollBy({ left: -(itemWidth + gap), behavior: 'smooth' });
        });

        nextBtnSalonMen.addEventListener('click', () => {
            const itemWidth = salonMenCarousel.querySelector('.most-booked-item').offsetWidth;
            const gap = 20;
            salonMenCarousel.scrollBy({ left: (itemWidth + gap), behavior: 'smooth' });
        });
    }

    // Modal Logic
    const womensBeautyBtn = document.getElementById('womens-beauty-btn');
    const beautyModal = document.getElementById('beauty-modal');
    const closeModalBtn = document.getElementById('close-modal-btn');

    if (womensBeautyBtn && beautyModal && closeModalBtn) {
        // Open modal
        womensBeautyBtn.addEventListener('click', () => {
            beautyModal.classList.remove('hidden');
        });

        // Close modal on X button click
        closeModalBtn.addEventListener('click', () => {
            beautyModal.classList.add('hidden');
        });

        // Close modal when clicking outside the content box
        beautyModal.addEventListener('click', (e) => {
            if (e.target === beautyModal) {
                beautyModal.classList.add('hidden');
            }
        });
    }

    // Salon Options Modal Logic
    const salonOptionsTrigger = document.getElementById('salon-options-trigger');
    const salonOptionsModal = document.getElementById('salon-options-modal');
    const closeSalonOptionsModalBtn = document.getElementById('close-salon-options-modal-btn');

    if (salonOptionsTrigger && salonOptionsModal && closeSalonOptionsModalBtn) {
        salonOptionsTrigger.addEventListener('click', () => {
            if(beautyModal) beautyModal.classList.add('hidden');
            salonOptionsModal.classList.remove('hidden');
        });

        closeSalonOptionsModalBtn.addEventListener('click', () => {
            salonOptionsModal.classList.add('hidden');
            if(beautyModal) beautyModal.classList.remove('hidden');
        });

        salonOptionsModal.addEventListener('click', (e) => {
            if (e.target === salonOptionsModal) {
                salonOptionsModal.classList.add('hidden');
            }
        });
    }

    // Spa for Women Options Modal Logic
    const spaForWomenTrigger = document.getElementById('spa-for-women-trigger');
    const spaForWomenOptionsModal = document.getElementById('spa-for-women-options-modal');
    const closeSpaForWomenOptionsBtn = document.getElementById('close-spa-for-women-options-btn');

    if (spaForWomenTrigger && spaForWomenOptionsModal && closeSpaForWomenOptionsBtn) {
        spaForWomenTrigger.addEventListener('click', () => {
            if(beautyModal) beautyModal.classList.add('hidden');
            spaForWomenOptionsModal.classList.remove('hidden');
        });

        closeSpaForWomenOptionsBtn.addEventListener('click', () => {
            spaForWomenOptionsModal.classList.add('hidden');
            if(beautyModal) beautyModal.classList.remove('hidden');
        });

        spaForWomenOptionsModal.addEventListener('click', (e) => {
            if (e.target === spaForWomenOptionsModal) {
                spaForWomenOptionsModal.classList.add('hidden');
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
            mensModal.classList.remove('hidden');
        });

        // Close modal on X button click
        closeMensModalBtn.addEventListener('click', () => {
            mensModal.classList.add('hidden');
        });

        // Close modal when clicking outside the content box
        mensModal.addEventListener('click', (e) => {
            if (e.target === mensModal) {
                mensModal.classList.add('hidden');
            }
        });
    }

    // Salon for Men Options Modal Logic
    const salonForMenTrigger = document.getElementById('salon-for-men-trigger');
    const salonForMenOptionsModal = document.getElementById('salon-for-men-options-modal');
    const closeSalonForMenOptionsBtn = document.getElementById('close-salon-for-men-options-btn');

    if (salonForMenTrigger && salonForMenOptionsModal && closeSalonForMenOptionsBtn) {
        salonForMenTrigger.addEventListener('click', () => {
            if(mensModal) mensModal.classList.add('hidden');
            salonForMenOptionsModal.classList.remove('hidden');
        });

        closeSalonForMenOptionsBtn.addEventListener('click', () => {
            salonForMenOptionsModal.classList.add('hidden');
            if(mensModal) mensModal.classList.remove('hidden');
        });

        salonForMenOptionsModal.addEventListener('click', (e) => {
            if (e.target === salonForMenOptionsModal) {
                salonForMenOptionsModal.classList.add('hidden');
            }
        });
    }

    // Massage for Men Options Modal Logic
    const massageForMenTrigger = document.getElementById('massage-for-men-trigger');
    const massageForMenOptionsModal = document.getElementById('massage-for-men-options-modal');
    const closeMassageForMenOptionsBtn = document.getElementById('close-massage-for-men-options-btn');

    if (massageForMenTrigger && massageForMenOptionsModal && closeMassageForMenOptionsBtn) {
        massageForMenTrigger.addEventListener('click', () => {
            if(mensModal) mensModal.classList.add('hidden');
            massageForMenOptionsModal.classList.remove('hidden');
        });

        closeMassageForMenOptionsBtn.addEventListener('click', () => {
            massageForMenOptionsModal.classList.add('hidden');
            if(mensModal) mensModal.classList.remove('hidden');
        });

        massageForMenOptionsModal.addEventListener('click', (e) => {
            if (e.target === massageForMenOptionsModal) {
                massageForMenOptionsModal.classList.add('hidden');
            }
        });
    }

    // AC Modal Logic
    const acRepairBtn = document.getElementById('ac-repair-btn');
    const acModal = document.getElementById('ac-modal');
    const closeAcModalBtn = document.getElementById('close-ac-modal-btn');

    if (acRepairBtn && acModal && closeAcModalBtn) {
        acRepairBtn.addEventListener('click', () => {
            acModal.classList.remove('hidden');
        });

        closeAcModalBtn.addEventListener('click', () => {
            acModal.classList.add('hidden');
        });

        acModal.addEventListener('click', (e) => {
            if (e.target === acModal) {
                acModal.classList.add('hidden');
            }
        });
    }

    // EPC Modal Logic
    const epcBtn = document.getElementById('epc-btn');
    const epcModal = document.getElementById('epc-modal');
    const closeEpcModalBtn = document.getElementById('close-epc-modal-btn');

    if (epcBtn && epcModal && closeEpcModalBtn) {
        epcBtn.addEventListener('click', () => {
            epcModal.classList.remove('hidden');
        });

        closeEpcModalBtn.addEventListener('click', () => {
            epcModal.classList.add('hidden');
        });

        epcModal.addEventListener('click', (e) => {
            if (e.target === epcModal) {
                epcModal.classList.add('hidden');
            }
        });
    }

    // Cleaning Modal Logic
    const cleaningBtn = document.getElementById('cleaning-btn');
    const cleaningModal = document.getElementById('cleaning-modal');
    const closeCleaningModalBtn = document.getElementById('close-cleaning-modal-btn');

    if (cleaningBtn && cleaningModal && closeCleaningModalBtn) {
        cleaningBtn.addEventListener('click', () => {
            cleaningModal.classList.remove('hidden');
        });

        closeCleaningModalBtn.addEventListener('click', () => {
            cleaningModal.classList.add('hidden');
        });

        cleaningModal.addEventListener('click', (e) => {
            if (e.target === cleaningModal) {
                cleaningModal.classList.add('hidden');
            }
        });
    }

    // Renovation Modal Logic
    const renovationBtn = document.getElementById('renovation-btn');
    const renovationModal = document.getElementById('renovation-modal');
    const closeRenovationModalBtn = document.getElementById('close-renovation-modal-btn');

    if (renovationBtn && renovationModal && closeRenovationModalBtn) {
        renovationBtn.addEventListener('click', () => {
            renovationModal.classList.remove('hidden');
        });

        closeRenovationModalBtn.addEventListener('click', () => {
            renovationModal.classList.add('hidden');
        });

        renovationModal.addEventListener('click', (e) => {
            if (e.target === renovationModal) {
                renovationModal.classList.add('hidden');
            }
        });
    }
    // Home Security Modal Logic
    const securityTrigger = document.getElementById('security-modal-trigger');
    const securityModal = document.getElementById('security-modal');
    const closeSecurityBtn = document.getElementById('close-security-modal-btn');

    if (securityTrigger && securityModal && closeSecurityBtn) {
        securityTrigger.addEventListener('click', () => {
            securityModal.classList.remove('hidden');
        });

        closeSecurityBtn.addEventListener('click', () => {
            securityModal.classList.add('hidden');
        });

        securityModal.addEventListener('click', (e) => {
            if (e.target === securityModal) {
                securityModal.classList.add('hidden');
            }
        });
    }

    // Logistics Modal Logic
    const logisticsTrigger = document.getElementById('logistics-modal-trigger');
    const logisticsModal = document.getElementById('logistics-modal');
    const closeLogisticsBtn = document.getElementById('close-logistics-modal-btn');

    if (logisticsTrigger && logisticsModal && closeLogisticsBtn) {
        logisticsTrigger.addEventListener('click', () => {
            logisticsModal.classList.remove('hidden');
        });

        closeLogisticsBtn.addEventListener('click', () => {
            logisticsModal.classList.add('hidden');
        });

        logisticsModal.addEventListener('click', (e) => {
            if (e.target === logisticsModal) {
                logisticsModal.classList.add('hidden');
            }
        });
    }

    // Fabrication Modal Logic
    const fabricationTrigger = document.getElementById('fabrication-modal-trigger');
    const fabricationModal = document.getElementById('fabrication-modal');
    const closeFabricationBtn = document.getElementById('close-fabrication-modal-btn');

    if (fabricationTrigger && fabricationModal && closeFabricationBtn) {
        fabricationTrigger.addEventListener('click', () => {
            fabricationModal.classList.remove('hidden');
        });

        closeFabricationBtn.addEventListener('click', () => {
            fabricationModal.classList.add('hidden');
        });

        fabricationModal.addEventListener('click', (e) => {
            if (e.target === fabricationModal) {
                fabricationModal.classList.add('hidden');
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
            trigger.addEventListener('click', () => modal.classList.remove('hidden'));
            closeBtn.addEventListener('click', () => modal.classList.add('hidden'));
            modal.addEventListener('click', (e) => {
                if (e.target === modal) modal.classList.add('hidden');
            });
        }
    });
});
