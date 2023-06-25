import requests
import os
from twilio.rest import Client

# Constants
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# API Keys
OWM_API_KEY = os.environ.get("OWM_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

# Parameters
parameters = {
    "lat": 28.613939,
    "lon": 77.209023,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily"
}

# Get weather data
response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

# Check if it will rain in the next 12 hours
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

# Send SMS
if will_rain:
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='TWILIO_NUMBER',
        to='YOUR_NUMBER'
    )
    print(message.status)

    
