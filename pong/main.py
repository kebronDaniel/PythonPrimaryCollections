from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

score = Score()

ball = Ball()

screen.update()


screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="a", fun=l_paddle.go_down)
screen.onkey(key="e", fun=l_paddle.go_up)

speed = 0.1
game_on = True
while game_on:
    score.write_score()
    screen.update()
    ball.move()
    time.sleep(speed)
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        score.add_l_score()
        speed *= 0.25
        ball.restart()

    if ball.xcor() < -380:
        score.add_r_score()
        speed *= 0.25
        ball.restart()



screen.exitonclick()
