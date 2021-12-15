import random
import smtplib
import datetime as dt

my_email = "testingtestromeo@gmail.com"
password = "Rabanos@121916"

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()

if day_of_the_week == 2:
    with open("quotes.txt", "r") as qt:
        all_qoutes = qt.readlines()

    send_qoute = random.choice(all_qoutes)



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="roxan.b.rabanos@gmail.com",
                            msg=f"Subject:Wednesday Quote\n\n{send_qoute}")
else:
    pass

