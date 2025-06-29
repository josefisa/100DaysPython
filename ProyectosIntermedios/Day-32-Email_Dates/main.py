import smtplib

mi_correo = "stalin.criollo.arg@gmail.com"
clave = "eyjkoembwmqxnrqt"

coneccion = smtplib.SMTP("smtp.gmail.com")
coneccion.starttls()
coneccion.login(user=mi_correo, password=clave)
texto = "¡Viva la libertad carajo!".encode('utf-8')
coneccion.sendmail(from_addr=mi_correo, to_addrs="stalin.criollo.arg@outlook.com", msg=texto)
coneccion.close