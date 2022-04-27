import geocoder
import folium

g = geocoder.ip("me")

my_loc = g.latlng

my_map = folium.Map(location=my_loc,
                    zoom_start=20)
folium.CircleMarker(location=my_loc,
                    radius=50, popup="AirportLink").add_to(my_map)

my_map.save("map.html")