import requests
import json

# first create a json to send
# make out request

json_body = json.dumps({"postcodes": ['E146HS','RM146SW', 'E148LH']})
headers = {'Content-Type': 'application/json'}

print(json_body)

post_request_to_postcodes = requests.post('https://api.postcodes.io/postcodes/', headers = headers, data=json_body)
print(post_request_to_postcodes.json())