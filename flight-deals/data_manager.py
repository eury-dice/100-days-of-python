import os
import requests

# CONSTANTS
API_PRICES = os.environ["SHEETY_API_PRICES"]
API_USERS = os.environ["SHEETY_API_USERS"]
AUTH_KEY = os.environ["SHEETY_AUTH"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {
            "Authorization": AUTH_KEY,
        }

    def get_dest(self) -> list:
        response = requests.get(url=API_PRICES, headers=self.headers)
        response.raise_for_status()
        return response.json()["prices"]

    def update_dest(self, data: list):
        for city in data:
            put_url = f"{API_PRICES}/{city['id']}"
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=put_url,
                json=new_data,
                headers=self.headers
            )
            response.raise_for_status()

    def get_users(self) -> list:
        response = requests.get(url=API_USERS, headers=self.headers)
        response.raise_for_status()
        return response.json()["users"]
