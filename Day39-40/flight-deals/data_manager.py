import requests
from pprint import pprint
import os

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT")
AUTH = tuple(os.environ.get("AUTH").split())

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=AUTH)
        data = response.json()
        self.destination_data = data.get("prices")
        
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=AUTH,
                headers={"Content-Type": "application/json"}
            )
            pprint(response.text)
