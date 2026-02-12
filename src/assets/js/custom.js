$(function () {

    // Header Scroll
    $(window).scroll(function () {
        if ($(window).scrollTop() >= 60) {
            $("header").addClass("fixed-header");
        } else {
            $("header").removeClass("fixed-header");
        }
    });


    // Featured Owl Carousel
    $('.featured-projects-slider .owl-carousel').owlCarousel({
        center: true,
        loop: true,
        margin: 30,
        nav: false,
        dots: false,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: false,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 3
            },
            1200: {
                items: 4
            }
        }
    })


    // Count
    $('.count').each(function () {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 1000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });


    // ScrollToTop
    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }

    const btn = document.getElementById("scrollToTopBtn");
    btn.addEventListener("click", scrollToTop);

    window.onscroll = function () {
        const btn = document.getElementById("scrollToTopBtn");
        if (document.documentElement.scrollTop > 100 || document.body.scrollTop > 100) {
            btn.style.display = "flex";
        } else {
            btn.style.display = "none";
        }
    };


    // Aos
    AOS.init({
        once: true,
    });


    // Dynamic Pricing System (Show/Hide Logic)
    function showPricingCategory(category) {
        // Hide all categories
        $('.pricing-category').addClass('d-none').removeClass('d-flex');

        // Show selected category with animation
        const selected = $(`#pricing-${category}`);
        selected.removeClass('d-none').addClass('d-flex');

        // Refresh CSS animations if libraries like AOS are used
        if (typeof AOS !== 'undefined') {
            setTimeout(() => AOS.refresh(), 100);
        }
    }

    // Handle product type selection
    $('.dropdown-item.product-type-option').on('click', function (e) {
        e.preventDefault();

        // Get data
        const productType = $(this).data('product');
        const productName = $(this).find('span.fw-bold').text();

        // Update Dropdown Text
        $('#selectedProductType').text(productName);

        // Update Active State in Dropdown
        $('.dropdown-item.product-type-option').removeClass('active');
        $(this).addClass('active');

        // Show corresponding pricing section
        showPricingCategory(productType);
    });

    // Initialize: Show default category (Flyers) loops ensure only one is visible
    // This runs on load to ensure correct state
    showPricingCategory('flyers');

});
