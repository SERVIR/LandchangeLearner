$(document).ready(function() {
	getMapRef();
});
var map = TETHYS_MAP_VIEW.getMap();
var getNdviButton = document.getElementsByName("get_ndvi")[0];
var getNdviUrl="get-ndvi-map";
if (getNdviUrl.substr(-1) !== "/") {
        getNdviUrl = getNdviUrl.concat("/");
}

function getMapRef(){
	 if(TETHYS_MAP_VIEW.getMap()){
		map=TETHYS_MAP_VIEW.getMap();
		map.on('click', function(evt){
		    var coords = ol.proj.toLonLat(evt.coordinate);
		    var lat = coords[1];
		    var lon = coords[0];
		    var locTxt = "Latitude: " + lat + " Longitude: " + lon;

		    alert(locTxt);
		});
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
		data:{"startDate":$('#startdate').val(),"endDate": $('#enddate').val()}       
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



