import requests
from twilio.rest import Client

API_KEY = "a37709296ead1330420bf7d373c7444d"
UNITS = "metric"

SENDER = "+12565768232"
RECEIVER = "+639162143943"
account_sid = "ACd465ad963b49b777dea265b84e6f80ac"
auth_token = "e9c55a38f5a5c102a152807ad89bf442"

# # Manila, PH
# LAT = 14.676041
# LON = 121.043701

# Bauru, BR
LAT = -22.322080
LON = -49.071150

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "units": UNITS,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=API_ENDPOINT, params=params)
response.raise_for_status()
weather_data = response.json()
weather_codes = [weather_data["hourly"][i]["weather"][0]["id"] for i in range(12)]

print(weather_codes)

will_rain = False
for code in weather_codes:
    if code < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain. Remember to bring an umbrella ☔.",
        from_=SENDER,
        to=RECEIVER
    )
    print(message.status)
