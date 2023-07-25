import requests
from datetime import datetime

MY_LAT = 42.389788  # 42.38978760538564
MY_LNG = -71.144877  # -71.14487654232931

sun_params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=sun_params)
sun_response.raise_for_status()
sun_data = sun_response.json()

sunrise = sun_data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = sun_data['results']['sunset'].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sun_data)

