document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.like-btn').forEach(btn => {
        const slug = btn.dataset.slug;
        const counter = btn.querySelector('.like-count');
        const storageKey = 'likes_' + slug;
        
        // Load saved likes
        const savedLikes = localStorage.getItem(storageKey) || 0;
        counter.textContent = savedLikes;
        
        if (savedLikes > 0) {
            btn.classList.add('text-warning');
        }
        
        btn.addEventListener('click', () => {
            let currentLikes = parseInt(localStorage.getItem(storageKey) || 0);
            currentLikes += 1;
            localStorage.setItem(storageKey, currentLikes);
            counter.textContent = currentLikes;
            btn.classList.add('text-warning');
        });
    });
});