var $window = $(window);

function getMapSize(screen_width, screen_height) {
    var headerHeight = $("nav.navbar").outerHeight();
    var footerHeight = $("div#ad").outerHeight();
    var size = new naver.maps.Size(screen_width, screen_height - headerHeight - footerHeight);
    return size;
};
var mapOptions = {
    center: new naver.maps.LatLng(38.0000000, 126.9783882),
    zoom: 6,
    minZoom: 3,
    maxZoom: 9,
};

var map = new naver.maps.Map('map', mapOptions);
var contentMarkers = {},
    contentWindows = {};
var markerIds = [];

$(document).ready(function(){
    map.setSize(getMapSize($window.outerWidth() - 0, $window.innerHeight()));

    $window.on('resize', function() {
        // console.log(this.screen);
        // map.setSize(getMapSize(this.screen.availWidth, this.screen.availHeight));
        map.setSize(getMapSize($window.outerWidth() - 0, $window.innerHeight()));
    });
});