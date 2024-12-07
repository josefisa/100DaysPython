from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280,300)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def add_level(self):
        self.level += 1
        self.update_score()
        


    def game_over(self):
        pass
        self.goto(0,0)
        self.write(f"G A M E  O V E R !", align="center", font=FONT)
        