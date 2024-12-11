import tkinter as tk
from tkinter import *

# ---------- PASSWORD GENERATOR ---------#


# ------------ SAVE PASSWORD ------------#


# --------------- UI SETUP --------------#
ventana = tk.Tk()
ventana.geometry("400x550")
ventana.minsize(400, 550)
ventana.maxsize(400, 550)
ventana.title("Generador de contraseñas")
ventana.config()

frame_top = Frame(ventana, height=300, width=400)
frame_top.pack(side=TOP, fill=NONE)
frame_dow = Frame(ventana)
frame_dow.pack(side=TOP, fill=NONE)

canvas = Canvas(frame_top,height=200,width=200,highlightthickness=0)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(95,100,image = lock_img)
canvas.place(x=200,y=150, anchor=CENTER)
#canvas.pack(expand=True)

website_label = Label(frame_dow, text="Website: ") #, height=50, width=100)
website_label.grid(row=0,column=0)
mail_label = Label(frame_dow, text= "Email Direction:")
mail_label.grid(row=1, column=0)
password_label = Label(frame_dow, text = "Password:")
password_label.grid(row=2, column=0)

website_entry = Entry(frame_dow)
website_entry.grid(row=0,column=1,columnspan=2)
mail_entry = Entry(frame_dow)
mail_entry.grid(row=1,column=1,columnspan=2)
password_entry = Entry(frame_dow)
password_entry.grid(row=2,column=1)

generate_button = Button(frame_dow, text="Generate")
generate_button.grid(row=2,column=2)
save_button = Button(frame_dow, text="Add passwword")
save_button.grid(row=3,column=1,columnspan=2)




ventana.mainloop()