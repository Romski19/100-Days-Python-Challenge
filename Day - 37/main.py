import requests
from datetime import datetime
import os


USERNAME = os.environ['PX_USERNAME']
TOKEN = "da52das64adw6dadaw"
GRAPH_ID = os.environ['PIX_ID']

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


today = datetime(year=2022, month=1, day=7)

post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

input_param = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "300",
    # "optionalData": "Limit"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
#


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_params = {
    "quantity": "300",
}

delete_date = datetime(year=2022, month=1, day=6)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date.strftime('%Y%m%d')}"

# to show graph
# response = requests.post(url=graph_endpoint, json=graphic_config, headers=headers)
# print(response.text)

# to post input on graph
# response = requests.post(url=post_endpoint, json=input_param, headers=headers)
# print(response.text)

# to update graph (use put)
# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)


# delete pixel in the graph
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)