import requests
from datetime import datetime
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

MY_LAT = 4.692465
MY_LNG =  -74.047745
MY_MAIL = "stalin.criollo.arg@gmail.com"
MY_PASSWORD = "eyjkoembwmqxnrqt"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
    "tzid": "America/Bogota",
}

def sending(): 
    with smtplib.SMTP("smtp.gmail.com") as conection:
        conection.starttls()
        conection.login(user=MY_MAIL, password=MY_PASSWORD)
        
        mensaje = MIMEMultipart()
        mensaje['from'] = MY_MAIL
        mensaje['to'] = "stalin.criollo.arg@outlook.com"
        mensaje['subject'] = F" Hey dude, the ISS is close to you!"
            
            
        mensaje.attach(MIMEText("ISS is currently aproaching you location \nlook at the sky and see", 'plain', 'utf-8'))
        conection.sendmail(from_addr=MY_MAIL, 
                        to_addrs="stalin.criollo.arg@outlook.com", 
                        msg=mensaje.as_string())

# Getting my location parameters.
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0].split("-")[0]
sunset = data["results"]["sunset"].split("T")[1].split("+")[0].split("-")[0]

sunrise = datetime.strptime(sunrise, "%H:%M:%S").time()
sunset = datetime.strptime(sunset, "%H:%M:%S").time()

now = datetime.now().time()

# Getting ISS locations.
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_lat, iss_lng = (float(data["iss_position"]["latitude"]),float(data["iss_position"]["longitude"]))

lat_in_range = (MY_LAT - 5) <= iss_lat <= (MY_LAT + 5)
lng_in_range = (MY_LNG - 5) <= iss_lng <= (MY_LNG + 5)
is_night = True if (sunset <= now) or (now <= sunrise) else False



print(f"ISS Position: {iss_lat}, {iss_lng}")
print(f"My Position: {MY_LAT}, {MY_LNG}")
print(f"Lat in range: {lat_in_range}")
print(f"Lng in range: {lng_in_range}")
print(f"Is night: {is_night}")
print(f"Current time: {now}")
print(f"Sunrise: {sunrise}, Sunset: {sunset}")


if lat_in_range and lng_in_range and is_night:
    sending()
else:
    pass