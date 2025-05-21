import requests
import json
import random
import string

base_url = "https://gorest.co.in"

auth_token = "Bearer 12f23544faa0a3c532bc13e34f9e2f1677917a5224453bc25d2185eee5f39118"

#Get Request
def get_request():
    url = base_url + "/public/v2/users"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = json.dumps(response.json(), indent=4)
    print("Response Body :", json_data)

get_request()