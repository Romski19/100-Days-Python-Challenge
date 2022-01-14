import requests
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_API_KEY = "0B-Jdrq704EiKJIYOC6KLoa6aaIrQFaR"
departure_airport_code = "LON"


class FlightData:

    def __init__(self):
        self.destination_price = {}
        self.header = {"apikey": TEQUILA_API_KEY}
        self.date_tom = datetime.now() + timedelta(days=1)
        self.date_42days = datetime.now() + timedelta(days=(6 * 30))

    def get_the_price(self, destination_city):
        parameters = {"fly_from": departure_airport_code,
                      "fly_to": destination_city,
                      "date_from": self.date_tom.strftime("%d/%m/%Y"),
                      "date_to": self.date_42days.strftime("%d/%m/%Y"),
                      "curr": "USD",
                      "nights_in_dst_from": 7,
                      "nights_in_dst_to": 28,
                      "flight_type": "round",
                      "one_for_city": 1,
                      }

        response = requests.get(url=TEQUILA_ENDPOINT,
                                params=parameters,
                                headers=self.header)

        data_now = response.json()["data"]

        for data_destination in data_now:
            prices = data_destination["price"]
            city_name = data_destination["cityTo"]
            city_code = data_destination["cityCodeTo"]
            flight_date = data_destination["route"][0]["local_departure"].split("T")[0]
            return_date = data_destination["route"][1]["local_departure"].split("T")[0]
            return city_name, city_code, prices, flight_date, return_date