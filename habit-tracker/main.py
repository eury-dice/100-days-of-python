import requests
from datetime import datetime

PIXELA_CREATE_USER_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_USERNAME = "ajericho"
PIXELA_TOKEN = "jsdif3WFW32iej92"

# # 1 - Create a new user
# user_params = {
#     "token": PIXELA_TOKEN,
#     "username": PIXELA_USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=PIXELA_CREATE_USER_ENDPOINT, json=user_params)
# print(response.text)

pixela_graph_endpoint = f"{PIXELA_CREATE_USER_ENDPOINT}/{PIXELA_USERNAME}/graphs"
graph_id = "graph1"
graph_name = "Sleep Graph"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

# # 2 - Create a new graph
# graph_config = {
#     "id": graph_id,
#     "name": graph_name,
#     "unit": "hours",
#     "type": "float",
#     "color": "kuro",
# }
#
# response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# today = datetime.now().strftime("%Y%m%d")
# print(today)


pixel_data = {
    "date": "20210307",
    "quantity": "5.5",
}

pixela_create_pixel_endpoint = f"{PIXELA_CREATE_USER_ENDPOINT}/{PIXELA_USERNAME}/graphs/{graph_id}"
# # 3 - Add a pixel
# response = requests.post(url=pixela_create_pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

day = "20210307"
pixela_update_pixel_endpoint = f"{pixela_create_pixel_endpoint}/{day}"
updated_data = {
    "quantity": "6.2",
}

# # 4 - Updating a pixel
# response = requests.put(url=pixela_update_pixel_endpoint, json=updated_data, headers=headers)
# print(response.text)

# 5 - Deleting a pixel
response = requests.delete(url=pixela_update_pixel_endpoint, headers=headers)
print(response.text)
