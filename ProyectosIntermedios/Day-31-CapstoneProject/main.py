"""
This is a flashcard app that helps users learn a new language by displaying words in a foreign language and their translations.
It allows users to flip the card to see the translation and mark words as known or unknown.
It uses a CSV file to store the words and their translations, and it saves the known words to a separate file.

Unlike Angela from the course, I'm kinda learning German, so I imported those kind of words.


And unlike Angela's code, user can switch between German-Spanish a he wishes.
"""

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import csv
import pandas as pd
import random
import time


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGES = ["Deutsche","Castellano"]
language = LANGUAGES[0]  # Default language is German

# ------------- FUNCTIONS -------------

# Create the list of words from the CSV file.
df = pd.read_csv("de_es.csv", sep=';')
words_list = dict(zip(df['Deutsche'],df['Castellano']))
#deutsche_words = list(words_list.keys())
deutsche_words = df.iloc[:,0].tolist()  # Two ways to get the same list.
castellano_words = list(words_list.values())

def next_card():
    global language
    
    canva.itemconfig(current_card, image=front_pic)
    word = ""
    index = random.randint(0, len(deutsche_words) - 1)
    if language == LANGUAGES[0]:
        word = deutsche_words[index]
    else:
        word = castellano_words[index]
        
    canva.itemconfig(title_text, text=language, fill="black")
    canva.itemconfig(word_text, text=word, fill="black")

    ventana.after(3000, lambda: flip_card(index))

    
    
    
def flip_card(index):
    global language
    canva.itemconfig(current_card, image=back_pic)
    if language == LANGUAGES[0]:
        canva.itemconfig(title_text, text=LANGUAGES[1], fill="white")
        canva.itemconfig(word_text, text=castellano_words[index], fill="white")
    else:
        canva.itemconfig(title_text, text=LANGUAGES[0], fill="white")
        canva.itemconfig(word_text, text=deutsche_words[index], fill="white")


def change_language():
    global language
    language = LANGUAGES[1] if language == LANGUAGES[0] else LANGUAGES[0]
    change_button.config(text=language)


# ------------- UI SETUP -------------

ventana = Tk()
ventana.title("Flashcard App")
ventana.geometry("600x500")
ventana.config(padx=50, bg=BACKGROUND_COLOR)

canva = Canvas(width=500, height = 250, bg=BACKGROUND_COLOR, highlightthickness=0)
original_front = Image.open("images/card_front.png")
resized_front = original_front.resize((500, 250))
original_back = Image.open("images/card_back.png")
resized_back = original_back.resize((500, 250))
front_pic = ImageTk.PhotoImage(resized_front)
back_pic = ImageTk.PhotoImage(resized_back)
current_card = canva.create_image(250, 125, image=front_pic)
title_text = canva.create_text(250, 50, text= "¡Traduce!", font= ("Courier New", 16, "bold"), fill="black")
word_text = canva.create_text(250, 150, text= "¡Listo?", font= ("Courier New", 24, "bold"), fill="black")
canva.grid(column=0, row=0, columnspan=2, pady=(50, 0))


ok_image = PhotoImage(file="images/right.png")
ok_button = Button(image=ok_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card) #To use a lambda function to activate.
ok_button.grid(column=0, row=2, pady=(20, 0))

not_image = PhotoImage(file="images/wrong.png")
not_button = Button(image=not_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)  # To use a lambda function to activate.
not_button.grid(column=1, row=2, pady=(20, 0))

change_button = Button(text=LANGUAGES[0], command=change_language, bg=BACKGROUND_COLOR)
change_button.grid(column=0, row=3, columnspan=2, pady=(20, 0))


ventana.mainloop()