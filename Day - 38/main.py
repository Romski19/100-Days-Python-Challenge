import os
import requests
from datetime import datetime

APP_ID = os.environ['TRACK_APP_ID']
API_KEY = os.environ['TRACK_API']

WEIGHT = 65
HEIGHT = 165
AGE = 29
GENDER = "Male"

parameters = {
    "query": input("What did you do in your exercise?: "),
    "gender": GENDER,
    "age": AGE,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

today = datetime.now()
whole_date = today.strftime("%d/%m/%Y")
time_today = today.strftime("%X")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
#
response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
data_exercise = response.json()["exercises"][0]
exercise_name = data_exercise["name"].title()
duration_exercise = round(data_exercise["duration_min"])
calories_exercise = round(data_exercise["nf_calories"])

sheet_inputs = {
    'sheet1': {
        'date': whole_date,
        'time': time_today,
        'exercise': exercise_name,
        'duration': duration_exercise,
        'calories': calories_exercise,
    },
}

#

sheet_endpoint = "https://api.sheety.co/7f278ebeba209420cb173fc3d1db2523/myWorkoutsRomeo/sheet1"

# get record sheety
# sheet_response = requests.get(url="https://api.sheety.co/7f278ebeba209420cb173fc3d1db2523/myWorkouts/workouts")
# print(sheet_response.json())

# input new record
# sheety_response = requests.post(url=sheety_endpoint,
#                                 json=sheety_parameters)

AUTH_BEARER = os.environ['SHEETY_BEERER']

bearer_headers = {
    "Authorization": AUTH_BEARER,
    "Content-Type": "application/json",
}

AUTH_S = os.environ['SHEETY_AUTH']
AUTH_P = os.environ['SHEETY_PASS']

sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    auth=(AUTH_S, AUTH_P),
    headers=bearer_headers,
)

print(sheet_response.text)