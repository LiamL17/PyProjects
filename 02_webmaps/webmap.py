
import folium
import pandas as pd
import numpy

def main():

    def color_choose(elev):
        if elev < 1000:
            return 'green'
        elif elev >= 1000 and elev < 3000:
            return 'orange'
        else:
            return 'red' 

    my_map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
    data = pd.read_csv("../data/Volcanoes.txt")

    lon = list(data["LON"])
    lat = list(data["LAT"])
    names = list(data["NAME"])
    elev = list(data["ELEV"])

    fg = folium.FeatureGroup(name="My Map")


    for i, j, n, e in zip(lat, lon, names, elev):
        #fg.add_child(folium.Marker(location=[i, j], popup=n + '\n' + e + ' m.', icon=folium.Icon(color=color_choose(e))))
        fg.add_child(folium.CircleMarker(location=[i, j], popup=n + '\n' + str(e) + ' m.', color=color_choose(e)))

    fg.add_child(folium.GeoJson(data=open("../data/world.json", 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

    my_map.add_child(fg)
    my_map.add_child(folium.LayerControl())

    my_map.save("Map1.html")

if __name__ == "__main__":
    main()