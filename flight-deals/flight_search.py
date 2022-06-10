import os
import requests
from flight_data import FlightData

# CONSTANTS
API_KEY = os.environ["TEQUILA_API_KEY"]
API_ENDPOINT = os.environ["TEQUILA_API_ENDPOINT"]
LOCATION_SEARCH = os.environ["TEQUILA_LOCATIONS"]
FLIGHT_SEARCH = os.environ["TEQUILA_FLIGHTS"]


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {
            "apikey": API_KEY,
        }

    def search_iata(self, city):
        params = {
            "term": city,
            "limit": 1
        }

        search_iata_url = API_ENDPOINT + LOCATION_SEARCH
        response = requests.get(
            url=search_iata_url,
            params=params,
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def search_flights(self,
                       destination_location,
                       date_from,
                       date_to,
                       currency="GBP",
                       current_location="LON") -> FlightData:

        flights_url = API_ENDPOINT + FLIGHT_SEARCH
        params = {
            "fly_from": current_location,
            "fly_to": destination_location,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "one_for_city": 1,
            "curr": currency,
        }

        response = requests.get(url=flights_url, params=params, headers=self.headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
            # print(data)
            result = FlightData(price=data["price"],
                                depart_city=data["cityFrom"],
                                depart_airport=data["flyFrom"],
                                arrival_city=data["cityTo"],
                                arrival_airport=data["flyTo"],
                                outbound_date=data["route"][0]["local_departure"].split("T")[0],
                                inbound_date=data["route"][1]["local_departure"].split("T")[0]
            )
            # print(result.to_string())
        except IndexError:
            params["max_stopovers"] = 1
            response = requests.get(url=flights_url, params=params, headers=self.headers)
            response.raise_for_status()
            try:
                data = response.json()["data"][0]
                # print(data)
                result = FlightData(price=data["price"],
                                    depart_city=data["cityFrom"],
                                    depart_airport=data["flyFrom"],
                                    arrival_city=data["cityTo"],
                                    arrival_airport=data["flyTo"],
                                    outbound_date=data["route"][0]["local_departure"].split("T")[0],
                                    inbound_date=data["route"][1]["local_departure"].split("T")[0],
                                    stop_overs=1,
                                    via_city=data["route"][0]["cityTo"]
                )
            except IndexError:
                result = None
                print(f"No flight available for {destination_location}")
        finally:
            return result
