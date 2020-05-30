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
county_data = './jhu_covid19_filled.csv'
df = pd.read_csv(county_data, parse_dates=['dt'])
df = df[df['dt'] == '5/9/2020']

#issue: json isn't formatted correctly. should try using the data from our json
# folium.Choropleth(
#     geo_data = county_geo,
#     data = df,
#     columns = ['FIPS', 'Deaths'],
#     key_on = 'feature.id',
#     fill_color ='YlGn',
#     fill_opacity = 0.7,
#     line_opacity = 0.2,
#     legend_name = 'Deaths from Coronavirus'
# ).add_to(m)

#set the colorscale
colorscale = branca.colormap.linear.YlGnBu_09.scale(0, 30)

#collect the desired data from the pandas file
# df.fips = df.fips.astype(int)
# df.deaths = df.deaths.astype(int)
df.FIPS = df.FIPS.astype(int)
df.Deaths = df.Deaths.astype(int)
death_series = df[df['dt'] == '5/9/2020']
death_series = death_series.set_index('FIPS')[['Deaths']]

# #death_series.dropna(inplace=True)
print(death_series)

#Main issue: only grabs the FIPs value, not the deaths value. can't figure out how to change it
#stylefunction used to color the choropleth
def style_function(feature):
    death = death_series.get(death_series, int(feature['id'][-5:]))
    print(death)
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