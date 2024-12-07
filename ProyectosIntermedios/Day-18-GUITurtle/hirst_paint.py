import colorgram
import turtle
from turtle import Turtle,Screen
from turtle import *
import random

#colors = colorgram.extract(r"hirst_paint.jpg",6)
rgb_colors =[]
colors = colorgram.extract(r"C:\Users\jeman\CursoPython\ProyectosIntermedios\Day-18-GUITurtle\hirst_paint.jpg", 15)

#print(colors)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))
    
real_rgb_colors = rgb_colors[4:(len(rgb_colors)+1)]

timmy = Turtle()
timmy.shape("circle")
turtle.colormode(255)
timmy.speed(9)
timmy.hideturtle()
size_paint = 10
timmy.up()
timmy.setposition(-150,-150)

for i in range(1,size_paint):
    timmy.up()
    timmy.setposition(-150,(-150+(30*i)))
    
    for j in range(1,size_paint):
        tup = random.choice(real_rgb_colors)
        timmy.color(tup)
        timmy.up()
        timmy.forward(30)
        timmy.down()
        timmy.dot(15)
     
screen = Screen()
screen.exitonclick()