from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-30,280)

    def write_score(self):
        self.write(arg=f"{self.l_score}   Score  :   {self.r_score}", font=("Arial", 18, "normal"))

    def add_l_score(self):
        self.clear()
        self.l_score += 1
        self.write_score()

    def add_r_score(self):
        self.clear()
        self.r_score += 1
        self.write_score()
