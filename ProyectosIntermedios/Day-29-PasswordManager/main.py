import tkinter as tk
from tkinter import *
import csv
import random

# Creating global variable, as will be used in each new iteration.
website = "google.com"
email = "j.em.figue@gmail.com"
password_list = []
password_string = ""
# Creating a list with caracters to be used in the password.
LOWER = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
UPPER = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
NUMBE = ['0','1','2','3','4','5','6','7','8','9']
SYMBO = ['!','#','$','%','&','*','+','?','¿']
GREEK = ['Α','Β','Γ','Δ','Ε','Ζ','Η','Θ','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω']

# ---------- PASSWORD GENERATOR ---------#


def generator():
    # Importing global variables.
    global password_list, password_string
    password_list = []
    # Creating a list that defines the amount of each type of caracter.
    elements = [LOWER,LOWER,LOWER,LOWER,UPPER,UPPER,UPPER,UPPER,NUMBE,NUMBE,SYMBO,GREEK]
    
    # Generating the password by adding to a pasword_list, that will be converted to a string.
    for list in elements:
        char = random.choice(list)
        password_list.append(char)
        
    random.shuffle(password_list)
    password_string = ''.join([str(letter) for letter in password_list])
    password_entry.delete(0,"end")
    password_entry.insert("end", password_string)    
    
    

# ------------ SAVE PASSWORD ------------#

def archiving():
    global website, email, password_string, password_list
    structure = ["website","email","password"]
    
    # Getting the info typed by the user.
    website = website_entry.get()
    email = mail_entry.get()
    password = password_entry.get()
    
    # passwords.csv already exists, add a new line to the original archive.
    with open("passwords.csv","a",newline='',encoding="utf-8") as passwords_file:
        adding = csv.DictWriter(passwords_file, fieldnames=structure)
        adding.writerow({"website": website, "email": email, "password": password})
        
    # Once the password is saved, I set each global empty to be used again.    
    website = ""
    email = ""
    password_string = ""
    password_list = []

# --------------- UI SETUP --------------#

ventana = tk.Tk()
ventana.geometry("400x550")
ventana.minsize(400, 550)
ventana.maxsize(400, 550)
ventana.title("Generador de contraseñas")
ventana.config()

# Create two frames, upper one for the logo display, bottom one for the widgets.
frame_top = Frame(ventana, height=300, width=400)
frame_top.pack(side=TOP, fill=NONE)
frame_dow = Frame(ventana, height=250, width=300)
frame_dow.pack(side=TOP, fill=NONE, anchor=CENTER)

# Create a logo as a canva in the upper frame.
canvas = Canvas(frame_top,height=200,width=200,highlightthickness=0)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(95,100,image = lock_img)
canvas.place(x=200,y=150, anchor=CENTER)
#canvas.pack(expand=True)

# Create the widgets to be used in the second frame.
website_label = Label(frame_dow, width=13, text="Website: ")
website_label.grid(row=0,column=0)
mail_label = Label(frame_dow, width= 13, text= "Email: ")
mail_label.grid(row=1, column=0)
password_label = Label(frame_dow, width= 13, text = "Password:")
password_label.grid(row=2, column=0)

website_entry = Entry(frame_dow, width= 24)
website_entry.grid(row=0,column=1,columnspan=2)
mail_entry = Entry(frame_dow, width= 24)
mail_entry.grid(row=1,column=1,columnspan=2)
password_entry = Entry(frame_dow,  width= 14)
password_entry.insert("end", string="************")
password_entry.grid(row=2,column=1)

generate_button = Button(frame_dow, width=7, text="Generate", command=generator)
generate_button.grid(row=2,column=2)
save_button = Button(frame_dow,  width= 20, text="Add password", command=archiving)
save_button.grid(row=3,column=1,columnspan=2)

ventana.mainloop()