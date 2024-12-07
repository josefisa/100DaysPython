from turtle import Turtle
import random

MULTIPLO = 5
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")      
        self.shapesize(stretch_len=0.5 , stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()
        
        
    #For this method a multipñe was used in order to generate the food in certain locations across the playground.    
    def refresh(self):
        rand_x = random.randint(-58*MULTIPLO,58*MULTIPLO)
        rand_y = random.randint(-58*MULTIPLO,58*MULTIPLO)
        self.goto(rand_x,rand_y)
        
    
       