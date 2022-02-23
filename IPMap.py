import geocoder
import folium

g = geocoder.ip("me")

my_loc = g.latlng

my_map = folium.Map(location=my_loc,
                    zoom_start=20)

my_map.save("map.html")