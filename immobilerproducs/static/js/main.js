const navbar = document.getElementById('navBar');

window.addEventListener('scroll', () => {
    if (window.scrollY >60) { // Adjust this value based on when you want the color to change
        navbar.classList.add('Nav-scrolled');
    } else {
        navbar.classList.remove('Nav-scrolled');
    }
});