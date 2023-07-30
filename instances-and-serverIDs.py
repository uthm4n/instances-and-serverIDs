import requests
import json 

url = "https://<YOUR-MORPHEUS-URL>/api/instances?max=25&offset=0&showDeleted=false&details=false"  # 'max' parameter can be changed to a different value if >25 instances need to be returned

headers = {
    "accept": "application/json",
    "authorization": "Bearer <YOUR-API-TOKEN>"                           # add your Morpheus API token 
}

response = requests.get(url, headers=headers, verify=False)
data = response.json()

for h in data['instances']:
    print(f"INSTANCE: {h['id']}\n SERVER IDs: {h['servers']}\n")