import smtplib

my_email = "testingtestromeo@gmail.com"
password = "Rabanos@121916"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="romeoramosa@gmail.com", msg="Subject:Hello Test\n\nTesting Email")
