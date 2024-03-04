from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, module):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.up()
        if module == "center_line":
            self.width(5)
            self.mark_board()
        else:
            self.width(10)
            self.left_score = 0
            self.right_score = 0
            self.show_score()


    def mark_board(self):
        self.goto(0, -290)
        self.setheading(90)
        while self.ycor() < 280:
            self.fd(15)
            self.down()
            self.fd(15)
            self.up()


    def show_score(self):
        score = f"{self.left_score}  {self.right_score}"
        self.goto(0, 180)
        self.clear()
        self.write("{}".format(score), align="center", font=("courier", 80, "bold"))


    def player_score(self, player):
        if player == "left":
            self.left_score += 1
        else:
            self.right_score += 1
        self.show_score()
