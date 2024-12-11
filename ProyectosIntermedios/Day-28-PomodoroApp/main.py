# Creado por José Emanuel Figueroa.
# Apliación Pomodoro, contabilización y distribución de tiempo.
 
import tkinter as tk 
from tkinter import *
import asyncio
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# All time periods have been given in seconds.
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timing = None
runing = False

# ---------------------------- TIMER RESET ------------------------------- #

def resert_action():
    global timing, reps
    ventana.after_cancel(timing)
    timing = None
    reps = 0
    checks["text"] = ""
    canvas.itemconfig(display, text=f"00:00")
    upper_text.config(text="Timer",foreground=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def starter():
    global reps; reps += 1
    global runing
    
    if runing == True:
        ventana.after_cancel(timing)
    
    if reps == 8:
        upper_text.config(text="REST",foreground=RED)
        counter(LONG_BREAK_MIN)
        runing = False
        return
    elif reps % 2 == 0:
        upper_text.config(text="BREAK",foreground=PINK)
        counter(SHORT_BREAK_MIN)
    else:
        upper_text["text"] = "WORK!"
        upper_text["foreground"] = GREEN
        counter(WORK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    global timing, reps
    global runing
    runing = True 
    minutes = math.floor(count/60)
    seconds = count%60
    
    canvas.itemconfig(display, text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        timing = ventana.after(1000, counter, count-1)
    else:
        marks = [1,3,5,7]
        if (reps in marks) and (reps < 8):
            checks["text"] += "🍅"  # ✔
   
# ---------------------------- UI SETUP ------------------------------- #
ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Pomodoro App")
ventana.config(bg=YELLOW)

canvas = Canvas(width=204, height=224,bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="ProyectosIntermedios/Day-28-PomodoroApp/tomato.png")
# tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_pic)
# canvas.place(x =250, y = 200, anchor = CENTER)
display = canvas.create_text(102, 132, text= "00:00", font= ("Courier New", 36, "bold"), fill="white")
canvas.place(x =250, y =200, anchor= CENTER)

inicio = Button(text = "START", command=starter)
inicio.place(x =150, y = 340, anchor = CENTER)

detener = Button(text = "RESET", command=resert_action)
detener.place(x=500-150, y=340, anchor= CENTER)

upper_text = Label(text="Timer", font=("Courier New",44), background=YELLOW, foreground=GREEN)
upper_text.place(x=250,y=60, anchor=CENTER)

checks = Label(text="", font=("default",25),background=YELLOW, foreground=RED)
checks.place(x=250,y=340, anchor=CENTER)

ventana.mainloop()