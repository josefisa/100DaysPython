import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mi_correo = "stalin.criollo.arg@gmail.com"
clave = "eyjkoembwmqxnrqt"

with smtplib.SMTP("smtp.gmail.com") as coneccion:
    coneccion.starttls()
    coneccion.login(user=mi_correo, password=clave)
    
    mensaje = MIMEMultipart()
    mensaje['from'] = mi_correo
    mensaje['to'] = 'stalin.criollo.arg@outlook.com'
    mensaje['subject'] = "¡Viva la libertad carajo"
    
    with open('ProyectosIntermedios/Day-32-Email_Dates/body.txt', 'r', encoding='utf-8') as file:
        cuerpo = file.read()
        
        
    mensaje.attach(MIMEText(cuerpo, 'plain', 'utf-8'))
    coneccion.sendmail(from_addr=mi_correo, 
                       to_addrs="stalin.criollo.arg@outlook.com", 
                       msg=mensaje.as_string())