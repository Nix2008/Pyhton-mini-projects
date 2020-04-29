import folium
import pandas

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

#map = folium.Map(location = [19.0760, 72.8777])
map = folium.Map(location = [38.58, -99.09])


fg = folium.FeatureGroup(name="My map")

for lt, ln, nm, el in zip(lat, lon, name, elev):
	fg.add_child(folium.Marker(location=[lt, ln], popup=['nm', el], icon=folium.Icon(color=marker_color(el))))

map.add_child(fg)

map.save("mumbai.html") 