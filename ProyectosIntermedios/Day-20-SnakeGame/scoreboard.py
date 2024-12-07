from turtle import Turtle
from food import Food

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
#food = Food()
#info = Turtle()

class Scoreboard(Food):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("ProyectosIntermedios/Day-20-SnakeGame/scoreboard.txt") as h_score:
            self.maxscore = int(h_score.read())
        self.clear()
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.write(f"SCORE: {self.score} HIGHEST SCORE {self.maxscore}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} HIGHEST SCORE {self.maxscore}", align=ALIGNMENT, font=FONT)
        
    def reset_score(self):
        if self.score > self.maxscore:
            self.maxscore = self.score
            with open("ProyectosIntermedios/Day-20-SnakeGame/scoreboard.txt", mode="w") as h_score:
                h_score.write(str(self.maxscore))
        self.score = 0
        self.update_scoreboard()
            
    #This method was replaced by reset_score
    #def game_over(self):
     #   self.goto(0,0)
      #  self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        
    def score_increaser(self):
        self.score += 1
        #self.clear()
        self.update_scoreboard() 
        
        
        