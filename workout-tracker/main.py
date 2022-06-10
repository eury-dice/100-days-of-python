import requests
import os
from datetime import datetime

# Nutritionix API
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_API_ENDPOINT = os.environ.get("NUTRITIONIX_API_ENDPOINT")

# Sheety API
SHEETY_API_ENDPOINT = os.environ.get("SHEETY_API_ENDPOINT")
SHEETY_AUTH_KEY = os.environ.get("SHEETY_AUTH_KEY")

HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

exercises = input("Tell me what exercises you did: ")

exercise_headers = {
    "Authorization": SHEETY_AUTH_KEY,
}
exercise_data = {
    "query": exercises,
}

response = requests.post(url=NUTRITIONIX_API_ENDPOINT, json=exercise_data, headers=HEADERS)
response.raise_for_status()
exercises = response.json()['exercises']

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

for exercise in exercises:
    workout_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        },
    }

    response = requests.post(url=SHEETY_API_ENDPOINT, json=workout_data, headers=exercise_headers)
    response.raise_for_status()
