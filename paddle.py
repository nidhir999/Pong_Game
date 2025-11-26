from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.color("white")
        self.goto(position)
    
    #move up
    def up(self):
        new_y=self.ycor()+20
        self.goto(x=self.xcor(), y=new_y)
    
    #move down
    def down(self):
        new_y=self.ycor()-20
        self.goto(x=self.xcor(), y=new_y)
        


    
