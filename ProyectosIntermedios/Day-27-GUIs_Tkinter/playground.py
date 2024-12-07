import tkinter as tk
from tkinter import *

ventana = tk.Tk()

ventana.title("|                         Intento de GUI")
ventana.geometry("800x500")
ventana.minsize(width=300, height=200)
ventana.maxsize(width=1500, height=900)
ventana.config(background="green")

# Create labels for instructions
tk.Label(text="Enter First Name:", background="green", font=("Courier", 14)).pack()
first_name_entry = tk.Entry()
first_name_entry.pack()

tk.Label(text="Enter Last Name:", background="green", font=("Courier", 14)).pack()
last_name_entry = tk.Entry()
last_name_entry.pack()

# Create a label to display the result
result_label = tk.Label(text="Result will appear here.", background="green", font=("Courier", 18))
result_label.pack()


lbl = tk.Label(text="I am a text.", background="green", font=("Courier", 28))
lbl.pack(side="bottom", expand=0)


# Function called when the button is clicked
def buttonclicked():
    first_name = first_name_entry.get()  # Get first name from entry
    last_name = last_name_entry.get()  # Get last name from entry
    # Update the label with the values
    result_label["text"] = f"Hello {first_name} {last_name}!"
    result_label["background"] = "white"
    ventana.config(background="white")
      
      
# Create a button that calls the buttonclicked function
button = tk.Button(text="Submit", command=buttonclicked)
button.pack()
      
#Entry
input = tk.Entry(width=30)
input.insert("end", string="Type your favorite color.")
input.pack()   
in_text = input.get()

#Text _ Bigger Text Output
text = tk.Text(height=5, width=30)
text.focus()
text.insert(END,"Example of a entry.\nAnd this is another line.")
print(text.get("2.3","end"))
text.pack()
    
#button = tk.Button(text="Click Me", command=lambda:buttonclicked(text = input.get()))
#button.pack()

#Spinbox
def spinbox_used(position):
    print(position)    
spinbox = tk.Spinbox(from_=0, to=50, width=10, command = lambda:spinbox_used(spinbox.get()))
spinbox.pack()


#Scale
def scale_used(value):
    lbl["text"] = f"Position: {value}"
    #print(value)
scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()


# Radiobuttons
def radio_used():
    print(radio_state.get())
    
radio_state = IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#List
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Pera","Manzana","Uvas","Cebolla"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
    
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

ventana.mainloop()