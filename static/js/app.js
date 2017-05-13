// image cycling for main page
var i = 1;
var alternate = 1;
var mainGal = [];
var gotoGallery = false;
var server = 'http://localhost:8000/';
// var server = 'http://34.205.41.30/';


function getSize() {
    var width = $('body').width() * window.devicePixelRatio;

    size = 'large';
    if (width < 800){
        size = 'small';
    } else if (width < 1800){
        size = 'medium';
    }
    return size;
}


function getMainGal() {
    return $.getJSON(
        mainGalUrl = server + "mainPaints/JSON/" + getSize(),
        function(data) {
            mainGal = data.paintings;
            $("#p1").attr("src", mainGal[0]);
            $("#p2").attr("src", mainGal[1]);
            setInterval(cycleImages, 4000);
        });
}


function cycleImages(){
    i = (i == mainGal.length - 1) ? 0 : i + 1;

    if (alternate==1){
        swapPics($("#p1"),$("#p2"), mainGal[i]);
        alternate = 0;
    } else {
        swapPics($("#p2"),$("#p1"),mainGal[i]);
        alternate = 1;
    }
}

function swapPics(pic1, pic2, src){
    pic1.fadeOut(2000);
    pic2.fadeIn(2000);
    setTimeout (function(){
        pic1.attr("src", src);
    }, 3000);
}


$(document).ready(function(){
    getMainGal();
});


// opens the drawer menu
function toggleNav() {
    document.getElementById("nav").classList.toggle("open");
}


$("#gal-link").bind('touchend', function(e){
    if (!gotoGallery) {
        e.preventDefault();
        e.stopPropagation();
        $(".dropdown-content").css("display", "flex");
        gotoGallery=true;
    }
});


$(".content")[0].addEventListener('touchend', function(e){
        $(".dropdown-content").css("display", "none");
        gotoGallery=false;
    }, false);



function enquiry(title) {
    var email = 'enquiries@dianewithers.com';
    var subject = title;
    document.location = "mailto:"+email+"?subject="+subject;
}
