from turtle import Screen, Turtle
from shapes import Shapes#, Paddle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=900,height=600)
screen.bgcolor("black")
screen.title("Let's play Ping Pong")
screen.tracer(0)

#Creates the shapes and paddles in the interface
line = Shapes()
line.central_line()

score = Scoreboard()
ball = Ball()

r_paddle = Paddle((400,0))
l_paddle = Paddle((-400,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")

game_is_on = True
velocity = 0.1
while game_is_on:
    time.sleep(velocity)
    screen.update()
    ball.move()
    
    #Detecting collision with the upper and lower walls.
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
      
    ##Angela does use diferent methos using ball.distance() method in order to solve this, those options are commented. 
    #Detecting a colission with the left paddle.
    
    #if  ((ball.xcor()> 380) and (ball.ycor() in range(r_paddle.ycor()-70, r_paddle.ycor()+10))):
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 380 or ball.distance(l_paddle) < 50 and ball.xcor() < -380 ):
        if velocity > 0.045:
            velocity = velocity - 0.005
        ball.richochet()
        print(velocity)
        
    #Detecting collission with the right paddle.
    
    #if((ball.xcor()< -380) and (ball.ycor() in range(l_paddle.ycor()-70, l_paddle.ycor()+10))):
      #  ball.richochet()
        
    #Detecting a miss in the paddle bounce, assigning score points.
    #Angela detects collision for each paddle indepedently, in order to launch the ball to the opponent.
    #I don't use it as my starting direction is random, to make it better ;)
    if ball.xcor() > 430:
        ball.resetposition()
        score.leftScoring()
        velocity = 0.1    
        
    if ball.xcor() < -430:
        ball.resetposition()
        score.rightScoring()
        velocity = 0.1

screen.exitonclick()