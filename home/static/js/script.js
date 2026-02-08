// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (menuToggle && navMenu) {
        // Toggle menu on button click
        menuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
        
        // Close menu when a link is clicked
        const navLinks = navMenu.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
            });
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navMenu.contains(event.target) || menuToggle.contains(event.target);
            if (!isClickInsideNav && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
            }
        });
    }
});

// Smooth scrolling for navigation links (skip contact page slides)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        // Skip sliding animation if we're on contact page
        if (document.querySelector('.slides')) return;
        
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
            
            // Update active nav link
            document.querySelectorAll('.nav-link').forEach(link => {
                link.classList.remove('active');
            });
            this.classList.add('active');
        }
    });
});

// Update active nav link on scroll
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section[id]');
    const scrollPosition = window.scrollY + 100;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');

        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            document.querySelectorAll('.nav-link').forEach(link => {
                link.classList.remove('active');
            });
            const activeLink = document.querySelector(`a[href="#${sectionId}"]`);
            if (activeLink) {
                activeLink.classList.add('active');
            }
        }
    });
});

// Typing animation for logo name (optional)
document.addEventListener('DOMContentLoaded', function() {
    const logoName = document.querySelector('.logo-name');
    if (logoName) {
        const originalText = logoName.textContent;
        logoName.textContent = '';
        let i = 0;
        function typeWriter() {
            if (i < originalText.length) {
                logoName.textContent += originalText.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        }
        setTimeout(typeWriter, 800);
    }
});

// Slide controls for contact page (presentation-style)
document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelector('.slides');
    if (!slides) return;

    const prevBtn = document.querySelector('.slide-btn.prev');
    const nextBtn = document.querySelector('.slide-btn.next');
    const indicators = Array.from(document.querySelectorAll('.indicator'));

    function getCurrentIndex() {
        return Math.round(slides.scrollLeft / slides.clientWidth);
    }

    function updateIndicators() {
        const idx = getCurrentIndex();
        indicators.forEach((btn, i) => {
            btn.classList.toggle('active', i === idx);
        });
    }

    // Scroll to the next/prev full slide width
    function goTo(offsetIndex) {
        const width = slides.clientWidth;
        slides.scrollTo({ left: offsetIndex * width, behavior: 'smooth' });
    }

    if (prevBtn) prevBtn.addEventListener('click', () => {
        const idx = Math.max(0, getCurrentIndex() - 1);
        goTo(idx);
    });

    if (nextBtn) nextBtn.addEventListener('click', () => {
        const maxIdx = slides.querySelectorAll('.slide').length - 1;
        const idx = Math.min(maxIdx, getCurrentIndex() + 1);
        goTo(idx);
    });

    indicators.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const idx = Number(e.currentTarget.dataset.index);
            goTo(idx);
        });
    });

    // Update indicators on scroll (debounced via rAF)
    let ticking = false;
    slides.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                updateIndicators();
                ticking = false;
            });
            ticking = true;
        }
    });

    // Keyboard navigation
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') nextBtn && nextBtn.click();
        if (e.key === 'ArrowLeft') prevBtn && prevBtn.click();
    });

    // Initialize
    updateIndicators();
});
