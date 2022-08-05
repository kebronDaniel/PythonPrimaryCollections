from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-275, 275)
        self.hideturtle()
        self.level = 0

    def write_level(self):
        self.clear()
        self.write(arg=f"Level : {self.level}", font=FONT)

    def write_game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("Game Over", font=FONT)

    def add_level(self):
        self.level += 1
        # self.write_level()


