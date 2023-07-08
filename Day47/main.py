import requests
from bs4 import BeautifulSoup
from pprint import pprint
import smtplib
import os

PRICE = 1350

your_url = "https://www.amazon.com.tr/Samsung-970-EVO-PLUS-NVMe/dp/B07MBQPQ62/ref=sr_1_12?crid=NO0OB3MJ9OBZ&keywords=ssd&qid=1688839804&sprefix=%2Caps%2C287&sr=8-12&th=1"

# Use https://myhttpheader.com/ to get your user agent and accept language
headers = {
    "User-Agent":"YOUR_USER_AGENT",
    "Accept-Language":"YOUR_ACCEPT_LANGUAGE",
}

response = requests.get(url=your_url, headers=headers)
response.raise_for_status()


soup = BeautifulSoup(response.text, "lxml")

price = soup.find(name="span",class_="a-price-whole").getText().replace(".","")[0:4]
pprint(price)

if int(price) < PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.environ("MY_EMAIL"), password=os.environ("MY_PASSWORD")
        connection.sendmail(from_addr=os.environ("MY_EMAIL"), to_addrs="EMAIL",
                            msg=f"Subject:Amazon Price Alert!\n\n{your_url}")