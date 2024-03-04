from turtle import Screen
from Scoreboard import Scoreboard
from Paddle import Paddle
from Ball import Ball
import time

# initiate screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# set up paddles
right_paddle = Paddle(350)
left_paddle = Paddle(-360)

# set up ball
ball = Ball()

# set up scoreboard
scoreboard = Scoreboard("")
center_line = Scoreboard("center_line")

# set key pushes
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_in_progress = True

ball_speed = 0.1

while game_in_progress:
    ball.move_ball()
    screen.update()
    ball.check_wall_collision()
    if ball.check_paddle_collision(l_paddle=left_paddle, r_paddle=right_paddle):
        ball_speed *= 0.9
    if ball.check_paddle_miss(scoreboard):
        ball.reset_ball()
        ball_speed = 0.1
    time.sleep(ball_speed)

screen.exitonclick()
