from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.forward(-10)


def rotate_clockwise():
    tim.right(10)


def rotate_counter():
    tim.right(-10)


def place_center():
    tim.penup()
    tim.clear()
    tim.home()


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_clockwise)
screen.onkey(key="d", fun=rotate_counter)
screen.onkey(key="c", fun=place_center)
screen.listen()
screen.exitonclick()
