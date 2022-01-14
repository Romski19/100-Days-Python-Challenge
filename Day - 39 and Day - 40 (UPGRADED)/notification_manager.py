import requests
import smtplib
from twilio.rest import Client

account_sid = "AC0336a39ea9bfaa3021ee23039d77cf50"
auth_token = "91df1ebf3b9457b62178775cbaef77f7"
my_email = "testingtestromeo@gmail.com"
password = "Rabanos@121916"


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def notify_low_price(self, city, city_code, price, flight_date, return_date):
        dynamic_message = f"Only $ {price} to fly from \n" \
                          f"London-STN to {city}-{city_code}, from \n" \
                          f"{flight_date} to {return_date}",
        message = self.client.messages \
            .create(
            body=f"Low Price Alert! \n\n "
                 f"{dynamic_message}",
            from_='+14439513240',
            to='+66800785607',
        )
        return dynamic_message

    def email_notification(self, e_mail, dyn_message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=e_mail,
                                msg=f"Subject: Low Cost Flight! \n\n"
                                    f"{dyn_message}")
