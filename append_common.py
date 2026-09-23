with open('common.js', 'a', encoding='utf-8') as f:
    f.write('''
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
''')
