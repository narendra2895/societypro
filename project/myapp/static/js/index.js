const currentLocation = location.href;
const menuItem= document.querySelectorAll('a');
const menuLength = menuItem.length

for(let i=0; i<menuLength;i++){
    if (menuItem[i].href=== currentLocation){
        menuItem[i].className="active"
    }
}


const hamburger = document.querySelector(".open");
const navBar= document.querySelector(".nav-ul");
const cross = document.querySelector(".close")
hamburger.addEventListener('click',()=>{
hamburger.classList.toggle("responsive");
navBar.classList.toggle("responsive");
cross.classList.toggle("responsive");
});
cross.addEventListener('click',()=>{
hamburger.classList.toggle("responsive");
navBar.classList.toggle("responsive");
cross.classList.toggle("responsive");
});

// #customerJS



        
$(document).ready(function() {

    $('.counter').each(function () {
$(this).prop('Counter',0).animate({
    Counter: $(this).text()
}, {
    duration: 4000,
    easing: 'swing',
    step: function (now) {
        $(this).text(Math.ceil(now));
    }
});
});

});  



