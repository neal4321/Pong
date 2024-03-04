from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.up()
        self.x_direction = 10
        self.y_direction = 10


    def move_ball(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)


    def check_wall_collision(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.y_direction *= -1


    def check_paddle_collision(self, l_paddle, r_paddle):
        if self.distance(l_paddle) < 65 and self.xcor() == -340 or self.distance(r_paddle) < 65 and self.xcor() == 330:
            self.x_direction *= -1
            return True
        else:
            return False

    def check_paddle_miss(self, scoreboard):
        if self.xcor() >= 380:
            scoreboard.player_score("right")
            return True
        elif self.xcor() <= -390:
            scoreboard.player_score("left")
            return True
        else:
            return False


    def reset_ball(self):
        self.x_direction *= -1
        self.home()
