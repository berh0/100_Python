import pandas as pd
import datetime as dt
import random
import smtplib

PLACEHOLDER = "[NAME]"
my_email = "yourmail@gmail.com"
my_password = "yourpassword"
file_path = "birthdays.csv"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)


if today_tuple in birthdays_dict:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letters:
        letter = letters.read()
        new_letter = letter.replace(PLACEHOLDER, birthdays_dict[today_tuple]["name"])
        print(new_letter)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthdays_dict[today_tuple]["email"],
                msg=f"Subject:Happy Birthday\n\n{new_letter}",
            )
    
