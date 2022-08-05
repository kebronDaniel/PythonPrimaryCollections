import random
from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win the race? : Type a color ")
colors = ["red", "orange", "yellow", "blue", "purple", "black", "pink"]
all_turtles = []
game_on = False

y = -120
x = -240
for _ in range(7):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[_ - 1])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 40
    all_turtles.append(new_turtle)

if user_bet:
    game_on = True

while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_on = False
            if user_bet == turtle.pencolor():
                print(f"Your turtle won")
            else:
                print("You loss")
                print(f"{turtle.pencolor()} wins")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
