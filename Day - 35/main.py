import requests

api_key = "747fad61ce8b8ee348c0f522b164e71a"
MY_LAT = 13.756331
MY_LONG = 100.501762

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()["hourly"][:12]

will_rain = False

for x in data:
    weather = x["weather"][0]["main"]
    status = x["weather"][0]["id"]
    if status < 700:
        will_rain = True
# will it rain for the next 6 hours?
if will_rain:
    print(f" Bring an Umbrella since the weather is {weather}")
