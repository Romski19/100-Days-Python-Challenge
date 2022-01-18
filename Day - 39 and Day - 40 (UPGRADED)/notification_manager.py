import requests
import smtplib
from twilio.rest import Client
import os

account_sid = os.environ['TW_SID']
auth_token = "7a3b82aeeae0f44032963e711b53e0d3"

my_email = os.environ['GMAIL_ACT']
password = os.environ['GMAIL_PASS']

used_number = os.environ['USER_NUMBER']


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def notify_low_price(self, city, city_code, price, flight_date, return_date):

        message = self.client.messages \
            .create(
            body=f"Low Price Alert! \n\n "
                 f"Only $ {price} to fly from "
                 f"Bangkok-BKK to {city}-{city_code}, from "
                 f"{flight_date} to {return_date}",
            from_='+14439513240',
            to= used_number,
        )

    def email_notification(self, e_mail, city, city_code, price, flight_date, return_date):
        email_message = f"Only $ {price} to fly from Bangkok-STN " \
                        f"to {city}-{city_code} from {flight_date} to {return_date}".encode('UTF-8')
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=e_mail,
                                msg=f"Subject: Low Cost Flight! \n\n"
                                    f"{email_message}")
