from snake import Snake
from food import Food
from turtle import Screen
from score_board import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenxia")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    score.write_score()

    snake.move()

    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or \
            snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        snake.reset()
        score.restart()
        # score.write_game_over()
        # game_on = False

    if snake.snake_head.distance(food) < 14:
        snake.add_segment()
        food.refresh()
        score.add_score()

    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 8:
            snake.reset()
            score.restart()
            # score.write_game_over()
            # game_on = False


screen.exitonclick()
