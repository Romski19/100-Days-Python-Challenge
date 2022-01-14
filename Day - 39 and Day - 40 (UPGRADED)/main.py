
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
notify_price = NotificationManager()
sheet_data = data_manager.get_destination_data()

print("Welcome to Romeo's Flight Club")
first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()
email = input("What is your email?: ").lower()

data_manager.input_users(first_name, last_name, email)

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

    details = flight_search.get_the_price((flight_search.get_destination_code(cities)))
    if details is None:
        pass
    else:
        if sheet_data[0]["lowestPrice"] > details.price:
            print(f"Low Price Alert! "
                  f"Only ${details.price} to fly from "
                  f"Bangkok-BKK to {details.city_name}-{details.city_code}, from "
                  f"{details.flight_date} to {details.return_date}")
            notify_price.notify_low_price(details.city_name, details.city_code, details.price, details.flight_date,details.return_date)
            email_data = data_manager.get_users()
            for user_emails in email_data:
                emails = user_emails["email"]
                notify_price.email_notification(emails, details.city_name, details.city_code, details.price, details.flight_date,details.return_date)
        else:
            print(
                f"Lowest updated price from Bangkok-BKK to {details.city_name}-{details.city_code} price: ${details.price} "
                f"{details.flight_date} to {details.return_date}")




