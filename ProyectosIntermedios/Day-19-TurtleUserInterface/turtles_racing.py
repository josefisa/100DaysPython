from turtle import Turtle, Screen
import random

#Creating screen details..
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet." , prompt="Which turtle will make it first?"
                            +"\nLeonardo (Green)? Rafael (Purple)? Donatello (Red)? Miguelangel (Yellow)?"
                            +"\nWritte the name: ")
user_bet = user_bet.lower()
print(f"You've chosen {user_bet}")


#creating a subclass to hold the names.
class NamedTurtle(Turtle):
    def __init__(self, name):
        super().__init__()
        self.name = name

# Create turtle instances with names
leonardo = NamedTurtle("leonardo")
rafael = NamedTurtle("rafael")
donatello = NamedTurtle("donatello")
miguelangel = NamedTurtle("miguelangel")


leonardo.color('green')
rafael.color('purple')
donatello.color('red')
miguelangel.color('yellow')


leonardo.shape('turtle')
rafael.shape('turtle')
donatello.shape('turtle')
miguelangel.shape('turtle')


# Set initial positions
leonardo.penup()
leonardo.goto(-230, 90)
rafael.penup()
rafael.goto(-230, 30)
donatello.penup()
donatello.goto(-230, -30)
miguelangel.penup()
miguelangel.goto(-230, -90)
    

#Race code....
#Create a loop while the race is on... and all turtles to advance randomly on each iteration...
race_on = False

if user_bet:
    race_on = True
    
while race_on:
    for turtle in [leonardo,rafael, donatello, miguelangel]:
        if turtle.xcor() >230:
            race_on = False
            winning_turtle = turtle.name
            if winning_turtle == user_bet:
                print(f"Yeah you did it! {winning_turtle.capitalize()} has won!")
            else:
                print(f"You've lost. {winning_turtle.capitalize()} is the winner!. ")
            break
        
        #Moving the turtle a random speed...
        speed = random.randint(3,15)
        turtle.forward(speed)
            
#Exit the screen...
screen.exitonclick()


 