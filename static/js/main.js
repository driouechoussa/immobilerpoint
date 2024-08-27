let slideIndex = 0;
showSlides();

function showSlides() {
    let i;
    let slides = document.getElementById('bgHero');
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    
    setTimeout(showSlides, 2000); // Change image every 2 seconds

    console.log(slides.length);
}