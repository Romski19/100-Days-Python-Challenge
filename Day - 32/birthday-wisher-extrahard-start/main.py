##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import random
import smtplib

now = dt.datetime.now()
month = now.month
today = now.day
date = f"{month}-{today}"

my_email = "testingtestromeo@gmail.com"
password = "Rabanos@121916"

df = pd.read_csv("birthdays.csv")

for x in range(len(df.name)):
    email_to_send = df.email[x]
    csv_names = df.name[x]
    csv_month = df.month[x]
    csv_date = df.day[x]
    birth_day = f"{csv_month}-{csv_date}"

    if date == birth_day:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as mail_template:
            content = mail_template.read()
            new_content = content.replace("[NAME]", f"{csv_names}")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email_to_send,
                                msg=f"Subject: Have Birthday Blast!\n\n"
                                    f"{new_content}")


    else:
        pass


# Angela Short Code solution

# today = dt.datetime.now()
# today_tuple = (today.month, today.day)
#
#
# data = pd.read_csv("birthdays.csv")
# birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
#
# if today_tuple in birthday_dict:
#