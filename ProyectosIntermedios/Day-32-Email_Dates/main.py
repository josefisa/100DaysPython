# This is the main project of the 32 days of Python challenge.
# It reads from birthdays.csv, which of the members is on birthday the day the code runs.
# birthdays.csv isn't complete, an in order to work one has to updtade the .csv.


import datetime as dt
import smtplib
import pandas as pd
import random

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

MY_MAIL = "stalin.criollo.arg@gmail.com"
MY_PASSWORD = "eyjkoembwmqxnrqt"

LETTERS = [
    'ProyectosIntermedios\Day-32-Email_Dates\letter_1.txt',
    'ProyectosIntermedios\Day-32-Email_Dates\letter_2.txt',
    'ProyectosIntermedios\Day-32-Email_Dates\letter_3.txt'
]



# Mail sending function
def sending(name, email, year):
    
    global now
    age = now.year - year # To cangrats on your x brithday. :)
    
    archive = random.choice(LETTERS)
    with open(archive,'r', encoding='utf-8') as file:
        letter = file.read()
        personal_letter = letter.replace("[NAME]", name)    
    
    with smtplib.SMTP("smtp.gmail.com") as conection:
        conection.starttls()
        conection.login(user=MY_MAIL, password=MY_PASSWORD)
        
        mensaje = MIMEMultipart()
        mensaje['from'] = MY_MAIL
        mensaje['to'] = email
        mensaje['subject'] = F" {name}! I'm happy for your {age} birthday!"
            
            
        mensaje.attach(MIMEText(personal_letter, 'plain', 'utf-8'))
        conection.sendmail(from_addr=MY_MAIL, 
                        to_addrs=email, 
                        msg=mensaje.as_string())

# Getting todays date in month, day format.
now = dt.datetime.now()
today = (now.month, now.day)


df = pd.read_csv('ProyectosIntermedios/Day-32-Email_Dates/birthdays.csv')
# I made a list comprehension!!! Hell yeah!
birthdays = { (row['month'],row['day']):(row['name'], row['email'], row['year']) for index, row in df.iterrows() }



# Checking if someone's birthday is today.
if today in birthdays:
    name, email, year = birthdays[today]
    sending(name, email, year)
else:
    print('No one is on holiday.')
    exit()