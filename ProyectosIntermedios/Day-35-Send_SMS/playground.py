import requests
import json

MY_API = "c3cd3aefc40b0d701348417944352f33"
LNG =   4.659 
LAT = -74.090

parameters = {
    "lat": LAT,
    "lon": LNG,
    "appid": MY_API,
}

try:
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    data = response.json()
    #print(json.dumps(data, indent= 4))
except requests.exceptions.RequestException as exe:
    print(f"Error perfoming request: {exe}")


