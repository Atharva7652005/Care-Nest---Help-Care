document.addEventListener('DOMContentLoaded', function() {
    // Slideshow functionality
    let slideIndex = 0;
    const slides = document.querySelectorAll('.slide');
    
    // Initialize the first slide
    showSlides();
    
    function showSlides() {
        // Hide all slides
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        
        // Increment slide index
        slideIndex++;
        
        // Reset to first slide if at the end
        if (slideIndex > slides.length) {
            slideIndex = 1;
        }
        
        // Display the current slide
        slides[slideIndex - 1].style.display = "block";
        
        // Change slide every 5 seconds
        setTimeout(showSlides, 5000);
    }
    
    // Horizontal scroll for cards with mouse wheel
    const cardsContainer = document.querySelector('.cards-container');
    
    cardsContainer.addEventListener('wheel', function(e) {
        if (e.deltaY !== 0) {
            e.preventDefault();
            this.scrollLeft += e.deltaY;
        }
    });
    
    // Touch scroll for mobile devices
    let isDown = false;
    let startX;
    let scrollLeft;
    
    cardsContainer.addEventListener('mousedown', (e) => {
        isDown = true;
        startX = e.pageX - cardsContainer.offsetLeft;
        scrollLeft = cardsContainer.scrollLeft;
    });
    
    cardsContainer.addEventListener('mouseleave', () => {
        isDown = false;
    });
    
    cardsContainer.addEventListener('mouseup', () => {
        isDown = false;
    });
    
    cardsContainer.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - cardsContainer.offsetLeft;
        const walk = (x - startX) * 2; // Scroll speed
        cardsContainer.scrollLeft = scrollLeft - walk;
    });
    
    // Filter functionality
    const applyFilterBtn = document.querySelector('.apply-filter');
    const filterDropdown = document.querySelector('.filter-dropdown select');
    const searchInput = document.querySelector('.search-box input');
    const cards = document.querySelectorAll('.card');
    
    applyFilterBtn.addEventListener('click', function() {
        const filterValue = filterDropdown.value.toLowerCase();
        const searchValue = searchInput.value.toLowerCase();
        
        cards.forEach(card => {
            const cardTitle = card.querySelector('h3').textContent.toLowerCase();
            const cardCity = card.querySelector('p').textContent.toLowerCase();
            
            // Check if card matches both filter and search criteria
            const matchesFilter = filterValue === 'all' || cardCity.includes(filterValue);
            const matchesSearch = searchValue === '' || cardTitle.includes(searchValue);
            
            if (matchesFilter && matchesSearch) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
    
    // Explore button functionality
    const exploreButtons = document.querySelectorAll('.explore-btn');
    
    exploreButtons.forEach(button => {
        button.addEventListener('click', function() {
            const cardTitle = this.parentElement.querySelector('h3').textContent;
            alert(`You clicked to explore ${cardTitle}. This would navigate to a detailed page in a real application.`);
        });
    });
    
    // Logo placeholder (replace with actual logo)
    const logoImg = document.querySelector('.logo img');
    logoImg.src = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MCIgaGVpZ2h0PSI1MCIgdmlld0JveD0iMCAwIDUwIDUwIj48Y2lyY2xlIGN4PSIyNSIgY3k9IjI1IiByPSIyMCIgZmlsbD0iI2Y1YzU0MiIvPjxwYXRoIGQ9Ik0yMCAxNWMwIDAgNSAxMCAxMCAxMHMxMC0xMCAxMC0xMCIgc3Ryb2tlPSIjZmZmIiBzdHJva2Utd2lkdGg9IjIiIGZpbGw9Im5vbmUiLz48Y2lyY2xlIGN4PSIyNSIgY3k9IjMwIiByPSI1IiBmaWxsPSIjZmZmIi8+PC9zdmc+';
    
    // Generate placeholder images for slides and cards
    const slideImages = document.querySelectorAll('.slide img');
    slideImages.forEach((img, index) => {
        img.src = `https://picsum.photos/800/400?random=${index + 1}`;
    });
    
    const cardImages = document.querySelectorAll('.card-image img');
    cardImages.forEach((img, index) => {
        img.src = `https://picsum.photos/300/150?random=${index + 10}`;
    });
});