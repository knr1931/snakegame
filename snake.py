from turtle import Turtle
from constants import (
    INITIAL_SNAKE_SEGMENTS_NUM,
    FORWARD_MOVE_DISTANCE,
    SNAKE_SQUARE_SEGMENT_SIZE,
    UP, DOWN, LEFT, RIGHT
)


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def reset(self):
        for segment in self.segments:
            segment.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(INITIAL_SNAKE_SEGMENTS_NUM):
            position = (-i * SNAKE_SQUARE_SEGMENT_SIZE, 0)
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.fillcolor("white")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        segments = self.segments
        for seg_num in range(len(segments) - 1, 0, -1):
            segment = segments[seg_num]
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segment.goto(x=new_x, y=new_y)

        self.head.forward(FORWARD_MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
