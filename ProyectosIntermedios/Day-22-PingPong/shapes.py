from turtle import Turtle, Screen


class Shapes(Turtle):
    
    def __init__(self):
        super().__init__()
    
    def central_line(self):
        line = Turtle()
        line.color("white")
        line.shape("circle")
        line.penup()
        line.goto(x=0,y=300)

        for i in range (300,-300,-40):
            line.penup()
            line.goto(0,(i-20))
            line.pendown()
            line.goto(0,i)
            
        line.penup()
        line.goto(0,-330)
        

        
        
         
        
    