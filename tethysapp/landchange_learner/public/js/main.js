var ajax_url="get-ndvi-map";
 if (ajax_url.substr(-1) !== "/") {
        ajax_url = ajax_url.concat("/");
    }
console.log(ajax_url);

var urll;
var xhr = jQuery.ajax({
type: "POST",
url: ajax_url,        
});
console.log("after ajax");
xhr.done(function(data) {

  urll =data;
  console.log("success");

})
.fail(function(xhr, status, error) {
    console.log(xhr.responseText);
});
var map = new Map({
     interactions: defaultInteractions().extend([new Drag()]),
     layers: [
          new TileLayer({
            source: new TileJSON({
              url: urll
            })
          }),
      target: 'map',
      });
map.on('click', function(evt){
    console.info(evt.pixel);
    console.info(map.getPixelFromCoordinate(evt.coordinate));
    console.info(ol.proj.toLonLat(evt.coordinate));
    var coords = ol.proj.toLonLat(evt.coordinate);
    var lat = coords[1];
    var lon = coords[0];
    var locTxt = "Latitude: " + lat + " Longitude: " + lon;
    // coords is a div in HTML below the map to display
    console.log(locTxt);
});

//'https://api.tiles.mapbox.com/v3/mapbox.geography-class.json?secure'
