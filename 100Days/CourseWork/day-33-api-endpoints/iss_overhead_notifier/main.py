import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

timestamp = data['timestamp']
longitude = data['iss_position']['latitude']
latitude = data['iss_position']['latitude']

position = (longitude, latitude)

print(f"time: {timestamp}")
print(f"position: {position}")
