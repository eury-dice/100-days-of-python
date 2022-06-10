import requests
from datetime import datetime

LAT = 14.599512
LNG = 120.984222
UTC_OFFSET = 8
SUNRISE_SUNSET_API = "https://api.sunrise-sunset.org/json"

# ISS_API = "http://api.open-notify.org/iss-now.json"
#
# response = requests.get(url=ISS_API)
# response.raise_for_status()
#
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
#
# print(iss_position)


def utc_to_local(utc_hour, offset):
    return (utc_hour + offset) % 24


parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0,
}

response = requests.get(url=SUNRISE_SUNSET_API, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = utc_to_local(int(data["results"]["sunrise"].split("T")[1].split(":")[0]), UTC_OFFSET)
sunset = utc_to_local(int(data["results"]["sunset"].split("T")[1].split(":")[0]), UTC_OFFSET)

print(f"Sunrise hour: {sunrise}")
print(f"Sunset hour: {sunset}")

current_time = datetime.now().hour
print(f"Current hour: {current_time}")
