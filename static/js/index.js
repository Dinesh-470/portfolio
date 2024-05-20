var header = document.getElementById('header');
var img = document.getElementById("profilepic")
var nav = this.document.getElementById('nav');
nav.style.marginTop = '400px';

function scrool() {
    if (window.scrollY > 1) {
        header.style.height = '200px';
        header.style.display = 'flex';
        img.style.height = '120px';
        img.style.width = '120px';
        img.style.marginBottom = '0px';
        nav.style.marginTop = '240px';
    } else {
        header.style.height = '370px';
        header.style.display = 'grid';
        img.style.height = '200px';
        img.style.width = '200px';
        nav.style.marginTop = '400px';
    }
}

window.addEventListener('scroll', scrool);