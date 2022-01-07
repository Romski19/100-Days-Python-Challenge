import requests

USERNAME = "romski07"
TOKEN = "da52das64adw6dadaw"

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
    "id": "romeyaw19",
    "name": "Diet Graph",
    "unit": "calorie",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graphic_config, headers=headers)
print(response.text)