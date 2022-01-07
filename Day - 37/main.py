import requests
from datetime import datetime

USERNAME = "romski07"
TOKEN = "da52das64adw6dadaw"
GRAPH_ID = "romeyaw19"

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# r = requests.post(url=pixela_endpoint, json=parameters)
# print(r.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graphic_config = {
    "id": GRAPH_ID,
    "name": "Diet Graph",
    "unit": "calorie",
    "type": "int",
    "color": "sora",
}


today = datetime(year=2022, month=1, day=5)

post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

input_param = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "300",
    # "optionalData": "Limit"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graphic_config, headers=headers)
# print(response.text)

response = requests.post(url=post_endpoint, json=input_param, headers=headers)
print(response.text)
# print(today)