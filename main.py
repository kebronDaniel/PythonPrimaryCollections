import turtle as t
t.colormode(255)
import random

my_turtle = t.Turtle()


def draw(sides, forward_length):
    for _ in range(sides):
        my_turtle.forward(forward_length)
        my_turtle.right(360 / sides)
        my_turtle.forward(forward_length)


direction = [90, 180, 270]


def move_anywhere():
    my_turtle.pencolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    # my_turtle.pencolor(color_pallet[random.randint(0, len(color_pallet) - 1)])
    my_turtle.pensize(5)
    my_turtle.speed(10)
    my_turtle.forward(50)
    my_turtle.right(direction[random.randint(0, len(direction) - 1)])


for _ in range(200):
    move_anywhere()


screen = t.Screen()
screen.exitonclick()
