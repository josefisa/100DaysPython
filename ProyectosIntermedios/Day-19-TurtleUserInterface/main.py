from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("green")
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)
    
def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    
def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
#screen.onkey(key='space', fun=move_forward)
screen.onkey(move_forward,'w')
screen.onkey(move_backwards, 's')
screen.onkey(move_right, 'a')
screen.onkey(move_left, 'd')
screen.exitonclick()