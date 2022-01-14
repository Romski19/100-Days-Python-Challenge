# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
flight_data = FlightData()
notify_price = NotificationManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data["prices"])

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


for city_name in sheet_data:
    cities = city_name['city']
    flight_search.get_destination_code(cities)
    city, city_code, price, flight_date, return_date = flight_data.get_the_price(flight_search.get_destination_code(cities))
    data_sheet_price = sheet_data[0]["lowestPrice"]
    notify_price.notify_low_price(city, city_code, price, flight_date, return_date,data_sheet_price)

    if sheet_data[0]["lowestPrice"] > price:
        print(f"Low Price Alert! "
              f"Only ${price} to fly from " 
              f"London-STN to {city}-{city_code}, from "
              f"{flight_date} to {return_date}")

    else:
        print(f"Lowest updated price from LONDON-STN to {city}-{city_code} price: ${price} "
              f"{flight_date} to {return_date}")

