import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=650, height=650)
screen.tracer(0)
screen.title("->                            WHY DID THE TURTLE CROSS THE ROAD?")
tim = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(tim.go_up,"Up")
screen.onkey(tim.go_down,"Down")

game_is_on = True

timer = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    timer += 1
    #Update the game if the turtle reaches the top.
    if tim.ycor() > 280:
        car_manager.increase_speed()
        score.add_level()
        tim.resetposition()

    #Here we slow the speed at which cars are created, delaying it by a factor of 10 or 6 for each iteration.
    #Angela uses a random choice generator in the car_manager class...
    if (timer%10) == 0:
        car_manager.car_creator()
    
    #Moving the cars.
    car_manager.car_mover()
    
    #Detecting colission with the car.
    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False
            score.game_over()
            
screen.exitonclick()