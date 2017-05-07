var source;
var size;

function getGallery(id){
    return $.getJSON(
        url = server + "gallery/JSON/" + id,
        function(data) {
            size = getSize();
            console.log(size);
            source = data.paintings;
            ko.applyBindings(new ViewModel());

        });
}


function toggleSlider(galId) {
    document.getElementById("slider").classList.toggle("open");
    getGallery(galId);
}



var painting = function(data) {
    this.title = ko.observable(data.title);
    // console.log (data.image + '-' + size + '.jpg');
    this.imgSrc = ko.observable(data.image + size + '.jpg');
    this.date = ko.observable(data.date);
}


var ViewModel = function() {
    var self = this;
    var p = 0;

    this.paintings = ko.observableArray([]);

    source.forEach(function (item) {
       self.paintings.push(new painting(item))
    });

    this.current = ko.observable(this.paintings()[p]);

    this.nextPic = function() {
        if (p == source.length - 1) {
            p = 0;
        } else  {
            p++;
        }
        this.setCurrent(p);
    };

    this.prevPic = function() {
        if (p == 0) {
            p = source.length - 1;
        } else  {
            p--;
        }
        this.setCurrent(p);
    };

    this.setCurrent = function(p) {
        var c = self.current().imgSrc();
        self.current(this.paintings()[p]);
        $("#gal-pic-below").attr("src", c);
        $("#gal-pic-below").fadeOut(2000);
    };

}


