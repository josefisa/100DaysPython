#This is a practice code to import things

#import turtle
#tim = turtle.Turtle()
#aliase import turtle as t
# tim = t.Turtle()
import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
#timmy.color(random)
turtle.colormode(255)

for i in range(3,10):
    tup = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    print(tup)
    timmy.pencolor(tup)
    for j in range(i):
        timmy.forward(90)
        timmy.right((360/i))
    
screen = Screen()
screen.exitonclick()