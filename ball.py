from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.color("white")
        self.goto(x=0, y=0)
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1
    
    #refresh the position of the ball
    def refresh(self):
        self.goto(x=self.xcor()+self.x_move, y=self.ycor()+self.y_move)

    #collision against the top of the screen
    def y_collision(self):
        self.y_move*=-1
    
    #hitting the paddles
    def x_collision(self):
        self.x_move*=-1
        self.move_speed*=0.9
    
    #if ball goes beyond the screen
    def move_beyond(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.x_collision()
