import tkinter as tk
from tkinter import *

#Window Creator
ventana = tk.Tk()
ventana.title("Convertidor de Distancia")
#ventana.maxsize(width=500,heigth=300)
ventana.maxsize(width=500, height=300)

#Function converter
def converter():
    try:
        miles = float(input.get())
    except:
        display.config(text="try again")
    else:
        kms = 1.609*miles
        kms = format(kms,".2f")
        display.config(text=kms)

#Button
button = Button(text="Convert", command=converter)
button.grid(row=2,column=1)

#input
input = Entry(width=10)
input.grid(row=0,column=1)

#Left Text
left_text = Label(text="Is equal to", font=("Arial", 11))
left_text.grid(row=1, column=0)

#Display Text
display = Label(text="", font=("Arial", 11))
display.grid(row=1, column=1)

#Km Text
km_label = Label(text="Kms",font=("Arial", 11))
km_label.grid(row=1,column=2)

#Miles Text
miles_label = Label(text="Miles", font=("Arial", 11))
miles_label.grid(row=0,column=2)

ventana.mainloop()