import requests
import smtplib
from datetime import datetime
import time

while True:
    time.sleep(60)

    MY_LAT = 13.756331
    MY_LONG = 100.501762
    my_email = "testingtestromeo@gmail.com"
    password = "Rabanos@121916"


    def compare_position(lat, long):
        global MY_LAT, MY_LONG
        if (int(MY_LAT) - 5) <= int(lat) <= (int(MY_LAT) + 5) and (int(MY_LONG) - 5) <= int(long) <= (int(MY_LONG) - 5):
            return True

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    #
    longitude = float(response.json()["iss_position"]["longitude"])
    latitude = float(response.json()["iss_position"]["latitude"])

    is_true = compare_position(latitude,longitude)

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    dark_hour = sunset + 7

    if time_now.hour >= dark_hour:
        its_dark = "Good Evening!"
    else:
        its_dark = "Hello"

    if is_true:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="romeoramosa@gmail.com",
                                msg=f"Subject:ISS Notification\n\n {its_dark}, Look up! ISS is above US!!")


