from turtle import  Turtle
import time

STARTING_LOCATIONS = [(0,0),(-20,0),(-40,0)]
CEMENTERY = (450,0)
MOVE_CONSTANT = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self):
        self.whole_snake = []
        self.create_snake()
        self.head = self.whole_snake[0]
        
    def create_snake(self):
        for position in STARTING_LOCATIONS:
            self.add_segment(position)
            
            
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.whole_snake.append(new_segment)
        
        
    def reset_snake(self):
        for segment in self.whole_snake:
            segment.goto(450,0)
            
        self.whole_snake.clear()
        self.create_snake()
        self.head = self.whole_snake[0]
    
    #This method isn't called at all, but is used by Angela. It got replaced by calling from main.py food detection decision.    
    def extension(self):
        self.add_segment(self.whole_snake[-1].position())
        
        
        
        
            
    def move(self):
        for segment in range(len(self.whole_snake) -1 ,0,-1):
            cor_x = self.whole_snake[segment - 1].xcor()
            cor_y = self.whole_snake[segment - 1].ycor()
            self.whole_snake[segment].goto(cor_x,cor_y)
        
        self.head.forward(MOVE_CONSTANT)
        #self.whole_snake[0].left(90)  
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
        
