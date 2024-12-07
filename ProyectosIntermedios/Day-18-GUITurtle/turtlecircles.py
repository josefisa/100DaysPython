import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255)
timmy.speed(6)

#directions = [0,90,180,270]

for i in range(0,360,60):
    print(i)
    timmy.seth(i)
    tup = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    #print(tup)
    timmy.pencolor(tup)
    #timmy.setheading(random.choice(directions))
    timmy.circle(45)
    
    
screen = Screen()
screen.exitonclick()