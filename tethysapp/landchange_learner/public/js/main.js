$(document).ready(function() {
	getMapRef();
});
var map = TETHYS_MAP_VIEW.getMap();
var geom;
var getNdviButton = document.getElementsByName("get_ndvi")[0];
var getNdviUrl="get-ndvi-map";
if (getNdviUrl.substr(-1) !== "/") {
        getNdviUrl = getNdviUrl.concat("/");
}
var geomtype;
function getMapRef(){
	 if(TETHYS_MAP_VIEW.getMap()){
		map=TETHYS_MAP_VIEW.getMap();
		/*map.on('click', function(evt){
		    var coords = ol.proj.toLonLat(evt.coordinate);
			console.log(coords);
			geom=coords;
		    var lat = coords[1];
		    var lon = coords[0];
                   // geom=lat+','+lon;
		    var locTxt = "Latitude: " + lat + " Longitude: " + lon;
                    geomtype="point";

		});*/

var selectedCollection = new ol.Collection();
var snappableCollection = new ol.Collection();
var selectInteraction = new ol.interaction.Select({
  features: selectedCollection,
  multi: true,
});
map.addInteraction(selectInteraction);

/* Adding Selected Feature */
selectedCollection.on('add', ({ element: feature }) => {
	geom = feature.getGeometry().getCoordinates();
	geomtype=feature.getGeometry().getType();

});
 /* var vector_source = new ol.source.Vector({
            wrapX: false
        });
 var lastFeature, draw, featureType;

        var vector_layer = new ol.layer.Vector({
            name: 'my_vectorlayer',
            source: vector_source,
            style: new ol.style.Style({
                fill: new ol.style.Fill({
                    color: 'rgba(255, 255, 255, 0.2)'
                }),
                stroke: new ol.style.Stroke({
                    color: '#ffcc33',
                    width: 2
                }),
                image: new ol.style.Circle({
                    radius: 7,
                    fill: new ol.style.Fill({
                        color: '#ffcc33'
                    })
                })
            })
        });

		 map.addLayer(vector_layer);

            if (draw)
                map.removeInteraction(draw);

            draw = new ol.interaction.Draw({
                source: vector_source,
                type: 'Polygon'
            });

            map.addInteraction(draw);

                draw.on('drawend', function (e) {
                    lastFeature = e.feature;
                    geom=lastFeature.getGeometry().getCoordinates()[0];
                    geomtype="poly";

                });

                draw.on('drawstart', function (e) {
                    vector_source.clear();
                });   */     
     
}

	else{
		 setTimeOut(getMapRef,300);
	    }
}

	
 $(getNdviButton).click(function(){
	var xhr = $.ajax({
		type: "POST",
		jsonp: "callback",
		url: getNdviUrl, 
		data:{"startDate":$('#startdate').val(),"endDate": $('#enddate').val(),"geom":JSON.stringify(geom),"geomtype":geomtype}       
	});
	xhr.done(function(data) {
	    const source = new ol.source.XYZ({
		             url: data.url,
		           });

	    map.addLayer(new ol.layer.Tile({
		        source: source,
		    }));

	})
	.fail(function(xhr, status, error) {
	    console.log(xhr.responseText);
	});
}); 



