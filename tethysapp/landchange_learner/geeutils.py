import ee
ee.Initialize()
LC8 = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')

def calcNDVI(){
	'''takes ee image object, returns ee image with new band named ndvi'''

	ndvi = img.normalizedDifference(['B5','B4']).rename('ndvi')
	return img.addBands(ndvi)
}

def getTileUrl(img,visParams=None){
	'''takes ee.Image and optional viz parameters and returns XYZ map'''
	map_id=ee.Image(img).getMapId(**visParams);
	tile_url_template = "https://earthengine.googleapis.com/map/{mapid}/{{z}}/{{x}}/{{y}}?token={4/dgEN0Dp237xgGm1SfA0epnOJt4doKR9ucoOUmPV3x1oISKJacplPT-o}"
	return tile_url_template.format(**map_id)
}

def getNdviMap(startTime='2018-01-01', endTime='2019-01-01'){
	'''takes a start time and end time date(YYYY-MM-DD), returns NDVI map from LANDSAT for the date range'''
	collection = LC8.filterDate(startTime,endTime).map(calcNDVI)
	composite=collection.qualityMosaic('ndvi')
	map_url=getTileUrl(composite,{'min':0, 'max':1,'bands':'ndvi','palette':'white, lightgreen, green,darkgreen'})	
	return map_url
}


