import turtle as t

t.colormode(255)
import random

leo = t.Turtle()


def sp_graph():
    leo.speed(10)
    leo.pencolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    leo.circle(50)
    leo.left(10)
    leo.hideturtle()


for _ in range(50):
    sp_graph()


screen = t.Screen()
screen.exitonclick()
