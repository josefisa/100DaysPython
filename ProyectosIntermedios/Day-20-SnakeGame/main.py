from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("A python written in Python!")
screen.tracer(0)
    
snake = Snake()
food = Food()
display = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up") 
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right") 
    
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()     
    
    if snake.head.distance(food) < 15:
        food.refresh()
        display.score_increaser()
        snake.add_segment(snake.whole_snake[-1].position())
        
    #Colision detector:
    if snake.head.ycor() >305 or snake.head.ycor() < -305 or snake.head.xcor() >305 or snake.head.xcor() <-305:
        #game_is_on = False
        #display.game_over()
        display.reset_score()
        snake.reset_snake()
        
    #Detect collision with itself.
    for segment in snake.whole_snake[2:]:
        if snake.head.distance(segment) < 7:
            #game_is_on = False
            #display.game_over()
            display.reset_score()
            snake.reset_snake()
            
screen.exitonclick()
