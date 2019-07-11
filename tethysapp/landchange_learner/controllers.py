from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import MapView, Button, TextInput, MVView, MVDraw, DatePicker
from .geeutils import getNdviMap
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def home(request):
    """
    Controller for the app home page.
    """
    drawing_options = MVDraw(
    	controls=['Modify', 'Delete', 'Move', 'Point', 'LineString', 'Polygon', 'Box'],
    	initial='Point',
    	output_format='WKT'
    )

    view_options = MVView(
        projection='EPSG:4326',
        center=[-100, 40],
        zoom=3.5,
        maxZoom=18,
        minZoom=2
    )

    landchange_map = MapView(
        height='100%',
        width='100%',
        layers=[],
        basemap='OpenStreetMap',
	view=view_options,
	draw=drawing_options
    )

    get_ndvi_button = Button(
        display_text='Load NDVI',
        name='get_ndvi',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Load NDVI'
        }
    )

    latitude = TextInput(
        display_text='Latitude',
        name='Latitude',
        placeholder='Enter Coordinates'
    )

    longitude = TextInput(
        display_text='Longitude',
        name='Longitude',
        placeholder='Enter Coordinates'
    )
    startdatepicker = DatePicker(name='startdate',
        display_text='Start Date',
        autoclose=True,
        format='yyyy-mm-dd',
        start_date='2014-02-01',
        start_view='decade',
        today_button=True,
        initial='2014-02-01')
    enddatepicker = DatePicker(name='enddate',
        display_text='End Date',
        autoclose=True,
        format='yyyy-mm-dd',
        start_date='2015-02-01',
        start_view='decade',
        today_button=True,
        initial='2015-02-01')

    context = {
       'get_ndvi_button': get_ndvi_button,
       'landchange_map': landchange_map,
       'latitude': latitude,
       'longitude': longitude,
       'startdatepicker': startdatepicker,
       'enddatepicker': enddatepicker
    }

    return render(request, 'landchange_learner/home.html', context)
@csrf_exempt
def gee(request):	
    """
    Controller for the gee home page.
    """	
    return_obj = {}
    if request.is_ajax() and request.method == 'POST':
        startDate = request.POST["startDate"]
        endDate = request.POST["endDate"]
        geom=request.POST["geom"]
        typ=request.POST["geomtype"]
        url = getNdviMap(geom,typ,startDate,endDate)
        return_obj["url"] = url

    return JsonResponse(return_obj)
    
    
