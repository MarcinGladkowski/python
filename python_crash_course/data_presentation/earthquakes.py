# Site https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
# Data from https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

file_name = './last_earthquakes.json'

with open(file_name) as f:
    data = json.load(f)
    features = data.get('features')

    mags, lons, lats = [], [], []

    for feature in features:
        mag = feature.get('properties').get('mag')
        mags.append(mag)

        geometry = feature.get('geometry').get('coordinates')
        lon = geometry[0]
        lat = geometry[1]

        lons.append(lon)
        lats.append(lat)

    # data = [Scattergeo(lon=lons, lat=lats)]

    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Mag'},
            'size': [5*mag for mag in mags]
        },
    }]

    map_layout = Layout(title='Last earthquakes')

    fig = {'data': data, 'layout': map_layout}

    offline.plot(fig, filename='global_earthquakes.html')
