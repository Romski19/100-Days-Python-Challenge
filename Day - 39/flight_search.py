import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_API_KEY = "AYr3koA4ZEsr0r3zLW2PpBZtNSkQZPFk"


class FlightSearch:

    def get_destination_code(self, city_name):
        header = {"apikey": TEQUILA_API_KEY}
        params = {"term": city_name, "location_types": "airport"}
        response = requests.get(url=TEQUILA_ENDPOINT, params=params, headers=header)
        data = response.json()['locations'][0]['city']['code']
        return data
