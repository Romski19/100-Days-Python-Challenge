import requests
from datetime import datetime, timedelta
from flight_data import FlightData
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_ENDPOINT_SEARCH = "https://tequila-api.kiwi.com/v2/search"

TEQUILA_API_KEY = os.environ['TQ_API']
departure_airport_code = "BKK"


class FlightSearch:

    def __init__(self):
        self.header = {"apikey": TEQUILA_API_KEY}
        self.date_tom = datetime.now() + timedelta(days=1)
        self.date_42days = datetime.now() + timedelta(days=(6 * 30))

    def get_destination_code(self, city_name):
        header = {"apikey": TEQUILA_API_KEY}
        params = {"term": city_name, "location_types": "airport"}
        response = requests.get(url=TEQUILA_ENDPOINT, params=params, headers=header)
        data = response.json()['locations'][0]['city']['code']
        return data

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

        response = requests.get(url=TEQUILA_ENDPOINT_SEARCH,
                                params=parameters,
                                headers=self.header)

        try:
            data_destination = response.json()["data"][0]
        except IndexError:
            print("No Flights Available")
            return None

        flight_data = FlightData(
            prices=data_destination["price"],
            city_name=data_destination["cityTo"],
            city_code=data_destination["cityCodeTo"],
            flight_date=data_destination["route"][0]["local_departure"].split("T")[0],
            return_date=data_destination["route"][1]["local_departure"].split("T")[0],
        )

        return flight_data
