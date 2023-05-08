import requests
from datetime import datetime

USERNAME = "aliendeva"
TOKEN = "aliendeva123"

pixela_endpoint = "https://pixe.la/v1/users"
graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graphs_config = {
    "id": "habbit1",
    "name": "python",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graphs_endpoint, json=graphs_config, headers=headers)
# print(response.text)

habit_graph = f"{pixela_endpoint}/{USERNAME}/graphs/habbit1"
today = datetime.now()

pixel_addition = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many minutes did you study today? ")
}

response = requests.post(url=habit_graph, json=pixel_addition, headers=headers)
print(response.text)