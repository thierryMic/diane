// image cycling for main page
var i = 0;
var alternate = 1;
var mainGal = [];


function getMainGal() {
    var size;
    var width =  $('body').width() * window.devicePixelRatio;

    size = '-large';
    if (width < 800){
        size = '-small';
    } else if (width < 1800){
        size = '-medium';
    }

    return $.getJSON(
        mainGalUrl = "http://localhost:8000/mainPaints/JSON/" + size,
        function(data) {
            mainGal = data.paintings;
            $("#pic-top").attr("src", mainGal[0]);
        });
}

function cycleImages(){
    var top;
    var bot;

    if (i == mainGal.length) {
        i = 0;
    } else {
        i += 1;
    }

    if (alternate==1){
        top = $("#pic-top");
        bot = $("#pic-bottom");
        alternate = 2;
    } else {
        top = $("#pic-bottom");
        bot = $("#pic-top");
        alternate = 1;
    }

    bot.attr("src", mainGal[i]);
    top.fadeOut(4000);
    bot.fadeIn(5000);

    top.css('zIndex', '1');
    bot.css('zIndex', '0');
}


// opens the drawer menu
function toggleNav() {
  document.getElementById("nav").classList.toggle("open");
}


$(document).ready(function(){
    getMainGal();
    $("#pic-bottom").attr("src", mainGal[1]);
    setInterval(cycleImages, 10000);
});



$("#gal-link")[0].addEventListener('touchstart', function(e){
    firstTap=!$(".dropdown-content").is(":visible");
    if (firstTap) {
        $(".dropdown-content").css("display", "flex");
        e.preventDefault();
        e.stopPropagation();
    }

}, false);


$(".content")[0].addEventListener('touchstart', function(e){
        $(".dropdown-content").css("display", "none");
    }, false);
