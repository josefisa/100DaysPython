"""
Password Manager

This is a password manager application that allows users to generate and store passwords securely.

For the 30rd day of the course, the software was changed to use JSON files instead of CSV files
while updating the GUI with a new feature.
I made some changes to the course project, adding a dropdown menu to select the website and
a search button to retrieve the password for that website. 

Free License: MIT License
Copyright (c) 2025 by José Figueroa.

"""


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
import random
import pyperclip
import json

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
    
    pyperclip.copy(password_string)
    
    
# ------------ SAVE PASSWORD ------------#

def archiving():
    global website, email, password_string, password_list
    structure = ["website","email","password"]
    
    # Getting the info typed by the user.
    website = website_entry.get()
    email = mail_entry.get()
    password = password_entry.get()
    data_for_json = {
     website: {
         "email": email,
         "password": password
          }
    }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Be sure to fill all\nthe requirements.")
    else:    
        # passwords.csv already exists, add a new line to the original archive.
        """ with open("passwords.csv","a",newline='',encoding="utf-8") as passwords_file:
            adding = csv.DictWriter(passwords_file, fieldnames=structure)
            adding.writerow({"website": website, "email": email, "password": password}) """
            
        try: 
        # To wirte .dump(), to readf .load() to update .update().        
            with open("data.json","r",encoding="utf-8") as passwords_file:
                data = json.load(passwords_file)
        except FileNotFoundError:    
            with open("data.json","w",encoding="utf-8") as passwords_file:
                json.dump(data_for_json, passwords_file, indent=4)
        else:
            data.update(data_for_json)
            with open("data.json","w",encoding="utf-8") as passwords_file:
                json.dump(data, passwords_file, indent=4)
        
        finally:
            website_entry.delete(0,"end")
            mail_entry.delete(0,"end")
        
        
    # Once the password is saved, I set each global empty to be used again.    
    website = ""
    email = ""
    password_string = ""
    password_list = []

# ---------- SEARCH BUTTON --------------#

def bring_info(event=None):
    global website, email, password_string
    selected_website = dropdown.get()
    
    try:
        with open("data.json", "r", encoding="utf-8") as passwords_file:
            data = json.load(passwords_file)
            if selected_website in data:
                website = selected_website
                email = data[selected_website]["email"]
                password_string = data[selected_website]["password"]
                
                # Updating the required labels.
                website_entry.delete(0,"end")
                website_entry.insert("end", website)
                mail_entry.delete(0,"end")
                mail_entry.insert("end", email)
                password_entry.delete(0,"end")
                password_entry.insert("end", password_string)
            else:
                messagebox.showinfo(title="Info", message="Website not found.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Error decoding JSON data.")


# --------------- UI SETUP --------------#

ventana = tk.Tk()
ventana.geometry("400x550")
ventana.minsize(400, 550)
ventana.maxsize(400, 550)
ventana.title("Generador de contraseñas")
ventana.config()

# Creates a popup window to select among wensites.
def open_popup():
    global dropdown
    # Create a new window for the dropdown.
    popup = Toplevel(ventana)
    popup.title("Select Website")
    popup.geometry("300x200")
    label = Label(popup, text="Select a website:")
    label.pack(pady=10)
    
    # Create a dropdown menu with the websites.
    with open("data.json", "r", encoding="utf-8") as passwords_file:
        data = json.load(passwords_file)
        websites = list(data.keys())
        dropdown = ttk.Combobox(popup, values=websites)
        dropdown.pack(pady=10)
        dropdown.bind("<<ComboboxSelected>>", bring_info)

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
website_label.focus()
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
search_button = Button(frame_dow, width=7, text="Search", command=open_popup)
search_button.grid(row=0,column=2)

ventana.mainloop()