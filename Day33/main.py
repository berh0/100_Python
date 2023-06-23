import requests
from datetime import datetime
import smtplib
import time

MY_MAIL = ""
MY_PASSWORD = ""

MY_LAT = 39.933365
MY_LONG = 32.859741

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (
        iss_latitude - 5 <= MY_LAT <= iss_latitude + 5
        and iss_longitude - 5 <= MY_LONG <= iss_longitude + 5
    ):
        return True

def is_night():
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = float(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = float(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_MAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs=MY_MAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky.",
        )
