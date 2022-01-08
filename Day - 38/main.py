import requests
from datetime import datetime

APP_ID = "50f6ec3e"
API_KEY = "1a9746e19e6acc15be7b364bf00c2e2d"

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
# bearer_headers = {
#     "Authorization": "Bearer qwertyasdfgSaSawqe",
# }

#

sheet_endpoint = "https://api.sheety.co/7f278ebeba209420cb173fc3d1db2523/myWorkoutsRomeo/sheet1"

# get record sheety
# sheet_response = requests.get(url="https://api.sheety.co/7f278ebeba209420cb173fc3d1db2523/myWorkouts/workouts")
# print(sheet_response.json())

# input new record
# sheety_response = requests.post(url=sheety_endpoint,
#                                 json=sheety_parameters)


bearer_headers = {
    "Authorization": "Basic cm9tc2tpMTk6QXNvbWFyQDEyMTkxNg==",
    "Content-Type": "application/json",
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    auth=('romski19', "Asomar@121916"),
    headers=bearer_headers,
)

print(sheet_response.text)