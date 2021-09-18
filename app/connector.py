import os 
import requests

BASE_URL = os.environ.get('SNOW_BASE_URL')
USER =  os.environ.get('SNOW_USER')
PWD = os.environ.get('SNOW_PWD')

url = f'{BASE_URL}/api/now/table/incident?sysparm_query=number%3DINC0010111&sysparm_limit=1'


# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(USER, PWD), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)