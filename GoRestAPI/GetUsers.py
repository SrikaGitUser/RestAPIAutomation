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

#POST Request
def post_request():
    url = base_url + "/public/v2/users"
    print("post url: " + url)
    headers = {"Authorization": auth_token}
    data = {"name": "Purushottam2 Reddy2",
            "email": "reddy2_purushottam2@braun.test",
            "gender": "male",
            "status": "active"}
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body: ", json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"]=="Purushottam2 Reddy2"
    return user_id

get_request()
