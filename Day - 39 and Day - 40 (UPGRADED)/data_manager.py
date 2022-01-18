import requests
import os

SHEETY_AUTH = os.environ['NEW_SHEETY_AUTH']

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/7f278ebeba209420cb173fc3d1db2523/myFlightDeals/prices"
USERS_ENDPOINT = "https://api.sheety.co/7f278ebeba209420cb173fc3d1db2523/myFlightDeals/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.headers = {"Authorization": f"{SHEETY_AUTH}"}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(response.text)

    def get_users(self):
        response = requests.get(url=USERS_ENDPOINT, headers=self.headers)
        data = response.json()
        users_data = data["users"]
        return users_data

    def input_users(self, firstname, lastname, email):
        data = {
            "user": {
                "firstName": firstname,
                "lastName": lastname,
                "email": email
            }
        }
        response = requests.post(
            url=USERS_ENDPOINT,
            json=data,
            headers=self.headers
        )

