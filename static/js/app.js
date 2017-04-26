
// image cycling for main page
var i = 0;
var alternate = 1
var mainGal = ["/static/img/Landscape 3.jpg", "/static/img/StillLife 6.jpg", "/static/img/Wildlife Burmese Tiger.jpg"];

function cycleImages(){
    i == mainGal.length - 1 ? i = 0 : i++;

    if (alternate==1){
        var top = $("#pic-top")
        var bot = $("#pic-bottom")
        alternate = 2
    } else {
        var top = $("#pic-bottom")
        var bot = $("#pic-top")
        alternate = 1
    }

    bot.attr("src", mainGal[i]);
    top.fadeOut(4000);
    bot.fadeIn(5000);
    // window.setTimeout(5500);
    top.css('zIndex', '1')
    bot.css('zIndex', '0')

}

$(document).ready(function(){
    $("#pic-top").attr("src", mainGal[0]);
    $("#pic-bottom").attr("src", mainGal[1]);
    setInterval(cycleImages, 6000);
});


// opens the drawer menu
function toggleNav() {
  document.getElementById("nav").classList.toggle("open");
}


// toggles fullscreen for polaroid element
function toggleFull (el) {
  el.classList.toggle("open");
}




/*
    By Osvaldas Valutis, www.osvaldas.info
    Available for use under the MIT License
*/



;(function( $, window, document, undefined )
{
    $.fn.doubleTapToGo = function( params )
    {
        if( !( 'ontouchstart' in window ) &&
            !navigator.msMaxTouchPoints &&
            !navigator.userAgent.toLowerCase().match( /windows phone os 7/i ) ) return false;

        this.each( function()
        {
            var curItem = false;

            $( this ).on( 'click', function( e )
            {
                var item = $( this );
                if( item[ 0 ] != curItem[ 0 ] )
                {
                    e.preventDefault();
                    curItem = item;
                }
            });

            $( document ).on( 'click touchstart MSPointerDown', function( e )
            {
                var resetItem = true,
                    parents   = $( e.target ).parents();

                for( var i = 0; i < parents.length; i++ )
                    if( parents[ i ] == curItem[ 0 ] )
                        resetItem = false;

                if( resetItem )
                    curItem = false;
            });
        });
        return this;
    };
})( jQuery, window, document );


// init();
$( '#gallery-link' ).doubleTapToGo();
// getPaintings();

