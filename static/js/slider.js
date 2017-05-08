var source;
var size;
var paintingsDb = [];



function getGallery(galId, paintId){
    return $.getJSON(
        url = server + "gallery/JSON/" + galId,
        function(data) {
            size = getSize();
            results = data.paintings;
            for (var i = 0; i < results.length; i++)
            {
                paintingsDb.push(new painting(results[i]));
            }
            ko.applyBindings(new ViewModel(paintId));
        });
}


function toggleSlider(galId, paintId) {
    document.getElementById("slider").classList.toggle("open");
}


var painting = function(data) {
    this.title = ko.observable(data.title);
    this.imgSq = ko.observable(data.image + '-sq' + size + '.jpg');
    this.date = ko.observable(data.date);
};




var ViewModel = function(firstPaintId) {
    var self = this;
    var p = 0;

    // initialise variables
    this.paintings = ko.observableArray(paintingsDb);
    this.current = ko.observable();
    this.prev = ko.observable();
    this.next = ko.observable();


    // sets the current painting in the slider
    this.setCurrent = function(p) {
        var index = self.paintings().indexOf(p);
        var prev = (index == 0) ? self.paintings().length - 1 : index - 1;
        var next = (index == self.paintings().length - 1 ) ? 0 : index + 1;

        self.current(p);
        self.prev(self.paintings()[prev]);
        self.next(self.paintings()[next]);
    };

};

getGallery(2);
