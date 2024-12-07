import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255)
timmy.speed(10)
timmy.pensize(6)

directions = [0,90,180,270]

for i in range(30):
    tup = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
   # print(tup)
    timmy.pencolor(tup)
    timmy.setheading(random.choice(directions))
    timmy.forward(20) 
    
    
timmy.home()       
    
screen = Screen()
screen.exitonclick()