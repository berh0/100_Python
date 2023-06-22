# import smtplib

# my_email = "your_mail@gmail.com"
# my_password = "your_password"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="your_test@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email.",
#     )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=2003 ,month=9 ,day= 4,hour=12)
# print(date_of_birth)

import smtplib
import datetime as dt
import random 

my_email = "yourmail"
my_password = "yourpassword"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="yourmail",
            msg=f"Subject:Quote of the Day\n\n{quote}",
        )
