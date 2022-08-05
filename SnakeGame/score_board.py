from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 0
        with open("SnakeGame/score.txt") as file:
            value = int(file.read())
        self.high_score = value
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)

    def write_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score_count} : High-Score {self.high_score}", font=("Arial", 18, "normal"))

    def restart(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
        self.score_count = 0
        self.write_score()
        with open("SnakeGame/score.txt") as file:
            previous_high_score = int(file.read())
        if previous_high_score < self.high_score:
            with open("SnakeGame/score.txt", "w") as file:
                file.write(str(self.high_score))

    def write_game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=("Arial", 18, "normal"))

    def add_score(self):
        self.score_count += 1
        self.write_score()
