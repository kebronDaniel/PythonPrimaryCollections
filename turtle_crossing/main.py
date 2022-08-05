import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()
screen.update()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
speed = 0.1
while game_is_on:
    time.sleep(speed)
    screen.update()
    score_board.write_level()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) < 27:
            game_is_on = False
            score_board.write_game_over()

    if player.ycor() > 280:
        player.restart()
        speed *= 0.10
        score_board.add_level()


screen.exitonclick()