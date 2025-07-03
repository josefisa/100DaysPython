import requests


response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.raise_for_status())

data = response.json()
print(data)

coordinates = (data["iss_position"]["longitude"],data["iss_position"]["latitude"])
print(coordinates)