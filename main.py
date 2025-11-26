from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong!")
screen.tracer(0)

right_paddle=Paddle((350, 0))
left_paddle=Paddle((-350, 0))
ball=Ball()
scoreboard=Scoreboard()

#move the paddles
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

is_game_on=True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.refresh()

    #collision against the top of the screen
    if ball.ycor()>285 or ball.ycor()<-285:
        ball.y_collision()
    
    #hitting the paddles
    if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()<-320:
        ball.x_collision()
    
    #if ball goes beyond the screen for the right player
    if ball.xcor()>380:
        ball.move_beyond()
        scoreboard.left_update_score()
    
    #if ball goes beyond the screen for the left player
    if ball.xcor()<-380:
        ball.move_beyond()
        scoreboard.right_update_score()


screen.exitonclick()