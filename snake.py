from turtle import Turtle

INITIAL_SNAKE_SEGMENTS_NUM = 3
FORWARD_MOVE_DISTANCE = 20
SNAKE_SQUARE_SEGMENT_SIZE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for i in range(INITIAL_SNAKE_SEGMENTS_NUM):
            snake_segment = Turtle("square")
            snake_segment.penup()
            snake_segment.fillcolor("white")
            snake_segment.goto(x=-i * SNAKE_SQUARE_SEGMENT_SIZE, y=0)
            self.snake_segments.append(snake_segment)

    def move(self):
        segments = self.snake_segments
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
