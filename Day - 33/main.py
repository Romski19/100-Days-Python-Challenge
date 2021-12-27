import requests

MY_LAT = 13.756331
MY_LONG = 100.501762

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
print(data)
