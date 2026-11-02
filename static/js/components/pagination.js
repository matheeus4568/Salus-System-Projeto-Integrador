document.addEventListener('DOMContentLoaded', function() {
    const scrollPos = sessionStorage.getItem('scrollPosPaginator');
    if (scrollPos) {
        window.scrollTo(0, parseInt(scrollPos));
        sessionStorage.removeItem('scrollPosPaginator'); 
    }

    const paginationLinks = document.querySelectorAll('.pagination-list button');
    
    paginationLinks.forEach(link => {
        link.addEventListener('click', function() {
            sessionStorage.setItem('scrollPosPaginator', window.scrollY);
        });
    });
});