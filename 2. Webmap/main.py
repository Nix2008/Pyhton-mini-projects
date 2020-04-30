import pandas
import os
import folium
from folium import IFrame
import base64

data = pandas.read_csv("sample.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def marker_color(elevation):
	if elevation < 1000:
		return 'red'
	elif 1000<= elevation <=3000:
		return 'green'
	else:
		return 'blue'

# MAp for mumbai #    map = folium.Map(location = [19.0760, 72.8777])
map = folium.Map(location = [38.58, -99.09])

encoded = base64.b64encode(open('pothole.jpg', 'rb').read()).decode()
html = '<img src="data:image/jpeg;base64,{}">'.format
iframe = folium.IFrame(html(encoded), width=500, height=500)

fgm = folium.FeatureGroup(name="Remove Marker")

for lt, ln, nm, el in zip(lat, lon, name, elev):
	fgm.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe, str(nm)), icon=folium.Icon(color=marker_color(el))))

fgp = folium.FeatureGroup(name="Remove Polygon")

fgp.add_child(folium.GeoJson(data=open('world.json', encoding='utf-8-sig').read(),
style_function = lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 1000000
else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))

map.add_child(fgm)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("mumbai.html") 