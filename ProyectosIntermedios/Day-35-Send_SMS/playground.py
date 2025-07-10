import requests
import json
import os
from twilio.rest import Client

MY_API = os.environ.get("OWM_API_KEY")
LNG =   4.659 
LAT = -74.090

account_sid = "_MY_TWILIO_ACCOUNT_SID_"
auth_token = os.environ.get("TWILIO_AUT_TOKEN")

parameters = {
    "lat": LAT,
    "lon": LNG,
    "appid": MY_API,
}

try:
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    data = response.json()["list"]
    #print(json.dumps(data, indent= 4))
except requests.exceptions.RequestException as exe:
    print(f"Error perfoming request: {exe}")
    
    
weather_id = [item["weather"]["id"] for item in data]
description = [item["weahter"][0]["description"] for item in data]
timestamp = [item["dt_txt"] for item in data]


client = Client(account_sid, auth_token)
message = client.messages.create(
    body=f"Today {timestamp[0]} is goin to be {description[0]}",
    from_="MY_TWILIO number",
    to="Another number"
)

print(message.status)