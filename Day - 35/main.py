import requests
from twilio.rest import Client
import os

api_key = os.environ['OW_API_KEY'] 
MY_LAT = 13.756331
MY_LONG = 100.501762

account_sid = os.environ['TW_SID']
auth_token = "e2187df6510ac584deb504bf21f12213"

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
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain. Bring an Umbrella",
        from_='+14439513240',
        to='+66800785607',
    )
    print(message.status)
