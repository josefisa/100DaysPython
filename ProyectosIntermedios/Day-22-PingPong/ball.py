from turtle import Turtle
import random


DIR = [10,-10]
ballSpeed = 1
#Choice random directions to start the game...

class Ball(Turtle):
     
    def __init__(self):
        super().__init__()
        
        self.color("white")
        self.shape("circle")
        self.shapesize(1)
        self.penup()
        self.yDir = random.choice(DIR)
        self.xDir = random.choice(DIR)
        self.speed(1) 
        self.velocity = 0.1
            
    def move(self):
        new_x = self.xcor() + self.xDir
        new_y = self.ycor() + self.yDir
        self.goto(new_x,new_y)
        
    def bounce(self):
        self.yDir = self.yDir*(-1)
        
    def richochet(self):
        self.xDir = self.xDir*(-1)
        
    def resetposition(self):
        self.goto(0,0)
        self.yDir = random.choice(DIR)
        self.xDir = random.choice(DIR)
        self.move()
        
        
        
        
        
        