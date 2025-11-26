from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.color("white")
        self.penup()
        self.update_scoreboard()
        self.hideturtle()
    
    #update the score of both players
    def update_scoreboard(self):
        self.goto(x=-100, y=200)
        self.write(self.l_score, move=False, align="center", font=("Arial", 20, "normal"))
        self.goto(x=100, y=200)
        self.write(self.r_score, move=False, align="center", font=("Arial", 20, "normal"))

    #update the score of the left player
    def left_update_score(self):
        self.l_score+=1
        self.clear()
        self.update_scoreboard()

    #update the score of the right player
    def right_update_score(self):
        self.r_score+=1
        self.clear()
        self.update_scoreboard()
    
    #when game ends
    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 20, "normal"))
