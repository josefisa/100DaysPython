# Sent a motivational quote via email, on the current weekday.
# Reads from quotes.txt.

import datetime as dt
import smtplib
import pandas as pd
import random

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Using datetime to get the current day of the week.
days = {
    0 : "Lunes",
    1 : "Martes",
    2 : "Miércoles",
    3 : "Jueves",
    4 : "Viernes",
    5 : "Sábado",
    6 : "Domingo"
}


weekday = (dt.datetime.now()).weekday()
day = days[weekday]
print(day)

# Accessing each quoate in quotes.txt
with open('ProyectosIntermedios/Day-32-Email_Dates/quotes.txt', 'r', encoding='utf-8') as file:
    quotes = file.readlines()
    
print(type(quotes))


# Randomly choosing a quote.
my_quote = random.choice(quotes)
print(my_quote)


# Sending the quote to my mail.
mi_correo = "stalin.criollo.arg@gmail.com"
clave = "eyjkoembwmqxnrqt"


with smtplib.SMTP("smtp.gmail.com") as conection:
    conection.starttls()
    conection.login(user=mi_correo, password=clave)
    
    mensaje = MIMEMultipart()
    mensaje['from'] = mi_correo
    mensaje['to'] = 'stalin.criollo.arg@outlook.com'
    mensaje['subject'] = F"¡Es {day} de motivación!"
        
        
    mensaje.attach(MIMEText(my_quote, 'plain', 'utf-8'))
    conection.sendmail(from_addr=mi_correo, 
                       to_addrs="stalin.criollo.arg@outlook.com", 
                       msg=mensaje.as_string())