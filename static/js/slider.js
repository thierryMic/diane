var source;
var size;
var paintingsDb = [];


function fade(img){
    $(".painting-pic").fadeIn("slow");
}

function getGallery(galId){
    return $.getJSON(
        url = server + "gallery/JSON/" + galId,
        function(data) {
            size = getSize();
            results = data.paintings;
            for (var i = 0; i < results.length; i++)
            {
                paintingsDb.push(new painting(results[i]));
            }
            ko.applyBindings(new ViewModel());
        });
}


function toggleSlider() {
    document.getElementById("slider").classList.toggle("open");
}



var painting = function(data) {
    this.title = data.title;
    this.imgSq = data.image + '-sq' + size + '.jpg';
    this.img = data.image  + '-' + size + '.jpg';
    this.dimensions = data.height + 'cm X ' + data.width + 'cm';
    this.medium = data.medium;
};




var ViewModel = function() {
    var self = this;
    var p = 0;

    // initialise variables
    this.showDetails = ko.observable(true);
    this.paintings = ko.observableArray(paintingsDb);
    this.current = ko.observable();
    this.prev = ko.observable();
    this.next = ko.observable();


    // sets the current painting in the slider
    this.setCurrent = function(p) {
        var index = self.paintings().indexOf(p);
        var prev = (index === 0) ? self.paintings().length - 1 : index - 1;
        var next = (index == self.paintings().length - 1 ) ? 0 : index + 1;

        self.current(p);
        self.prev(self.paintings()[prev]);
        self.next(self.paintings()[next]);
    };

    this.toggleDetails = function() {
        self.showDetails(!self.showDetails());
    };

};


getGallery(window.location.pathname.split("/")[2]);
