import ee
import json
ee.Initialize()
LC8 = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')

def calcNDVI(img):
	#takes ee image object, returns ee image with new band named ndvi
	ndvi = img.normalizedDifference(['B5','B4']).rename('ndvi')
	return img.addBands(ndvi)

def getTileUrl(img,visParams=None):
	#takes ee.Image and optional viz parameters and returns XYZ map
	map_id=ee.Image(img).getMapId(visParams);
	tile_url_template = "https://earthengine.googleapis.com/map/"+map_id['mapid']+"/{z}/{x}/{y}?token="+map_id['token']
	return tile_url_template

def getNdviMap(startTime='2018-01-01', endTime='2019-01-01'):
	#takes a start time and end time date(YYYY-MM-DD), returns NDVI map from LANDSAT for the date range
	collection = LC8.filterDate(startTime,endTime).map(calcNDVI)
	composite=collection.qualityMosaic('ndvi')
	map_url=getTileUrl(composite,{min:0, max:1, 'bands':'ndvi', 'palette':'white, lightgreen, green,darkgreen'})	
	return map_url



