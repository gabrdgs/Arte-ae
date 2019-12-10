var nav = document.querySelector("nav");
var botaoNavMobile = document.querySelector(".toggle-menu");

function checkPosition() {
    if (window.matchMedia('(max-width: 768px)').matches) {
        nav.classList.remove("desktop")
        nav.classList.add("mobile")
    } else {
        nav.classList.remove("mobile")
        nav.classList.add("desktop")
    }
}
checkPosition();

window.onload = checkPosition();

function toggleMenu(){
    nav.classList.toggle("mobile-toggle")
}

botaoNavMobile.onclick = toggleMenu;