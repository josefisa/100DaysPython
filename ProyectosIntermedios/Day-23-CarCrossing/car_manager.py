import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):    
    pass

    def __init__(self):
        #super().__init__()
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT
        
    def car_creator(self):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.speed(9)
        random_ypos = random.randint(-260,260)
        new_car.goto(300, random_ypos)
        self.all_cars.append(new_car)
        
        
    def car_mover(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        
                
    def increase_speed(self):
        self.car_speed += 5

        

