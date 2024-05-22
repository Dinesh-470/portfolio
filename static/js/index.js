var header = document.getElementById('header');
var img = document.getElementById("profilepic")
var nav = document.getElementById('nav');
nav.style.marginTop = '300px';
img.style.height = '150px';
img.style.width = '150px';

function scrool() {
    if (window.scrollY > 1) {
        header.style.height = '180px';
        img.style.height = '100px';
        img.style.width = '100px';
        nav.style.marginTop = '250px';
    } else {
        header.style.height = '240px';
        img.style.height = '150px';
        img.style.width = '150px';
        nav.style.marginTop = '300px';
    }
}

window.addEventListener('scroll', scrool);