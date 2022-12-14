import turtle
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.snake_segment(position)

    def snake_segment(self, position):
        snake_piece = Turtle()
        snake_piece.penup()
        snake_piece.color("white")
        snake_piece.shape("square")
        snake_piece.shapesize(0.5)
        snake_piece.goto(position)
        self.segments.append(snake_piece)

    def add_segment(self):
        position = self.segments[len(self.segments) - 1].position()
        self.snake_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # The last one takes the position of the one before it.
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.snake_head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
