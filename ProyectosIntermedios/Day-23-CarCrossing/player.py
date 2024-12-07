from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)
        
    def go_down(self):
        self.backward(MOVE_DISTANCE)
        
    def resetposition(self):
        self.goto(STARTING_POSITION)