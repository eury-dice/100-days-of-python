import requests
import smtplib
import time
from datetime import datetime


MY_LAT = 14.671536  # Your latitude
MY_LONG = 121.035042  # Your longitude
DEG_DIFF = 5
UTC_OFFSET = 8
HOST = "smtp.gmail.com"
PORT = 587
MY_EMAIL = "jericho.ardent@gmail.com"
MY_PASS = "The wall$ must h0ld"


# ------------------------ FUNCTIONS ------------------------
def is_within_position():
    res = requests.get(url="http://api.open-notify.org/iss-now.json")
    res.raise_for_status()
    data = res.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    lat_diff = iss_latitude - MY_LAT
    long_diff = iss_longitude - MY_LONG

    return (DEG_DIFF >= lat_diff >= -DEG_DIFF) and (DEG_DIFF >= long_diff >= -DEG_DIFF)


def utc_to_local(utc_hour):
    return (utc_hour + UTC_OFFSET) % 24


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_utc = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_utc = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    sunrise = utc_to_local(sunrise_utc)
    sunset = utc_to_local(sunset_utc)

    hr_now = datetime.now().hour

    return (hr_now > sunset) or (hr_now < sunrise)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    if is_within_position() and is_night():
        with smtplib.SMTP(HOST, PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"From: {MY_EMAIL}\n"
                                    f"To: {MY_EMAIL} \n"
                                    f"Subject:ISS Overhead\n\n"
                                    f"Look up! You might see the ISS passing by.")
    else:
        print(f"The ISS is somewhere else.")

    time.sleep(60)
