import smtplib
import os

my_email = os.environ['GMAIL_ACT']
password = os.environ['GMAIL_PASS']


class NotificationManager:

    def mail_sender(self, int_price, price):
        if int_price < 4000:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs='romeoramosa@gmail.com',
                                    msg=f"Subject: KEYCHRON LOW PRICE ALERT! \n\n"
                                    f"Keychron Price in Lazada is now only {price}".encode('UTF-8'))

    


        