import tkinter as tk
from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    
    
ventana = tk.Tk()
ventana.title("Progamita")
ventana.minsize(width=300, height=200)
ventana.maxsize(width=1500, height=900)
ventana.config(padx=20, pady=20)

#Label
my_label = Label(text="Hello there.",font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0,row=0)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)

#Button
button2 = Button(text="Click Me", command=lambda:my_label.config(text="Button N°2"))
button2.grid(column=2,row=0)


#Entry
input = Entry(width=1)
#input.place(relx=0.35, rely=0.2, relwidth=0.5, relheight=0.1, relfont=0.3 )
input.config(width=15)
input.grid(column=3,row=2)

#Text _ Bigger Text Output
text = tk.Text(height=15, width=30)
text.focus()
text.insert(END,"Here I'am supposed to draw.\nA beautiful Carrier.")
#print(text.get("2.3","end"))
text.grid(column=4,row=0,columnspan=5,rowspan=3)


ventana.mainloop()