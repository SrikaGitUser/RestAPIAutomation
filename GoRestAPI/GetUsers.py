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
def post_request(url, filepath, headers, content_type='json'):
    try:
        with open(filepath, 'r') as file:
            if content_type.lower() == 'json':
                payload = json.load(file)
            else:
                payload = file.read()
        print(payload)

        if content_type.lower() == 'json':
             response = requests.post(url, json=payload, headers=headers)
        else:
            response = requests.post(url, data=payload, headers=headers)
        print(response)
        assert response.status_code == 201
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("json response body: ", json_str)
        user_id = json_data["id"]
        print("User id; ", user_id)

        response.raise_for_status()
        return response.text

    except FileNotFoundError:
        return "Error: Payload file not found."
    except json.JSONDecodeError:
        return "Error: Invalid JSON format in the payload file."
    except requests.exceptions.RequestException as e:
       return f"Request error: {e}"

url = base_url + "/public/v2/users"
file_path = 'C:/Users/srika/PycharmProjects/RestAPIAutomation/GoRestAPI/Payload.json'
headers = {"Authorization": auth_token}
post_request(url, file_path, headers, content_type='json')
