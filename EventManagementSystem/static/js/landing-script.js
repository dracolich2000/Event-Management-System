//for scrolling down on click

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

//for making items appear as we scroll

document.addEventListener('DOMContentLoaded', function() {
    const featureItems = document.querySelectorAll('.feature');
    const pricingItems = document.querySelectorAll('.pricing-plan');

    const isElementInViewport = (el) => {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    };

    const checkIfInView = () => {
        featureItems.forEach(item => {
            if (isElementInViewport(item)) {
                item.classList.add('visible');
            }
        });
        pricingItems.forEach(item => {
            if (isElementInViewport(item)) {
                item.classList.add('visible');
            }
        });
    };
    

    // Check if elements are in view on scroll and load
    window.addEventListener('scroll', checkIfInView);
    window.addEventListener('load', checkIfInView);
});

//make hero section visible
document.addEventListener('DOMContentLoaded', function() {
    const heroSection = document.querySelector('.hero-text');
    const contactSection = document.querySelector('.contact-info')
    const contactForm = document.querySelector('.contact-form')

    const isElementInViewport = (el) => {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    };

    const checkIfInView = () => {
        if (isElementInViewport(heroSection)) {
            heroSection.classList.add('visible');
        }
        if (isElementInViewport(contactSection)) {
            contactSection.classList.add('visible');
        }
        if (isElementInViewport(contactForm)) {
            contactForm.classList.add('visible');
        }
    };

    // Initial check and on scroll
    window.addEventListener('load', checkIfInView);
    window.addEventListener('scroll', checkIfInView);
});


