import requests
from twilio.rest import Client

account_sid = "AC0336a39ea9bfaa3021ee23039d77cf50"
auth_token = "91df1ebf3b9457b62178775cbaef77f7"


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def notify_low_price(self, city, city_code, price, flight_date, return_date, dt_price):
        if dt_price > price:
            message = self.client.messages \
                .create(
                body=f"Low Price Alert! \n\n "
                     f"Only $ {price} to fly from \n"
                     f"London-STN to {city}-{city_code}, from \n"
                     f"{flight_date} to {return_date}",
                from_='+14439513240',
                to='+66800785607',
            )
            print(message.status)
