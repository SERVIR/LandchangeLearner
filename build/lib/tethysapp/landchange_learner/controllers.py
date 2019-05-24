from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import MapView, Button, TextInput, MVView, MVDraw

@login_required()
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

    save_button = Button(
        display_text='',
        name='save_button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
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

    context = {
       'save_button': save_button,
       'landchange_map': landchange_map,
       'latitude': latitude,
       'longitude': longitude,
    }

    return render(request, 'landchange_learner/home.html', context)
