import folium
import pandas as pd
import branca
import requests
import json

m = folium.Map(
    location=[39, -99,],
    zoom_start = 4.5,
    tiles = 'cartodbpositron'
)

#can make interactive popups throughout the map - may want a for loop that can go through
#each county on the map and put a pop-up (or each state - per county may be too busy)

#read in topo_json and county_data
topo_url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
county_geo = f'{topo_url}/us_counties_20m_topo.json'
deaths_county_data = './jhu_covid19_filled.csv'
death_frame = pd.read_csv(deaths_county_data, parse_dates = ['dt'] ,na_values=[' '])

#set the colorscale
colorscale = branca.colormap.linear.YlGnBu_09.scale(0, 100)

#collect the desired data from the pandas file
death_series = death_frame[death_frame['dt'] == '5/9/2020']
death_series = death_series.set_index('FIPS')['Deaths']
print(death_series)

#stylefunction used to color the choropleth. compares ids then graphs series
def style_function(feature):
    death = death_series.get(int(feature['id'][-5:]))
    return {
        'fillOpacity': 0.5,
        'weight': 0,
        'fillColor': '#black' if death is None else colorscale(death)
    }

folium.TopoJson(
    json.loads(requests.get(county_geo).text),
    'objects.us_counties_20m',
    style_function=style_function
).add_to(m)

m.save('index.html')